#!/usr/bin/env node

const fs = require('fs')
const path = require('path')
const { spawnSync } = require('child_process')

const ROOT = path.resolve(__dirname, '..')
const RUNS_DIR = path.join(ROOT, 'results', 'runs')
const VALIDATOR = path.join(ROOT, 'scripts', 'validate-rubric.js')

function readJson(filePath) {
  return JSON.parse(fs.readFileSync(filePath, 'utf8'))
}

function listDirectories(dir) {
  return fs.existsSync(dir)
    ? fs.readdirSync(dir, { withFileTypes: true }).filter((d) => d.isDirectory()).map((d) => d.name)
    : []
}

function validateScore(relativeScorePath) {
  const result = spawnSync('node', [VALIDATOR, relativeScorePath], {
    cwd: ROOT,
    encoding: 'utf8',
  })

  return {
    ok: result.status === 0,
    stdout: result.stdout.trim(),
    stderr: result.stderr.trim(),
  }
}

function collectRuns() {
  const benchmarks = listDirectories(RUNS_DIR)
  const rows = []

  for (const benchmark of benchmarks) {
    const benchmarkDir = path.join(RUNS_DIR, benchmark)
    const candidates = listDirectories(benchmarkDir)

    for (const candidate of candidates) {
      const scoreV2Path = path.join(benchmarkDir, candidate, 'score-v2', 'evaluation.json')
      const scoreV1Path = path.join(benchmarkDir, candidate, 'score', 'evaluation.json')
      const scorePath = fs.existsSync(scoreV2Path) ? scoreV2Path : scoreV1Path
      const manifestPath = path.join(benchmarkDir, candidate, 'manifest.json')
      const relativeScorePath = path.relative(ROOT, scorePath)

      let validation = { ok: true, stdout: '', stderr: '' }
      let payload = null
      let manifest = null
      let readError = null

      try {
        if (fs.existsSync(scorePath)) {
          validation = validateScore(relativeScorePath)
          payload = readJson(scorePath)
        }
        if (fs.existsSync(manifestPath)) {
          manifest = readJson(manifestPath)
        }
      } catch (error) {
        readError = error.message
      }

      rows.push({
        benchmark,
        candidate,
        validation,
        payload,
        manifest,
        readError,
      })
    }
  }

  return rows
}

function interpretationRank(label) {
  switch (label) {
    case 'strong_pda_handoff':
      return 0
    case 'usable_but_leaky':
      return 1
    case 'weak_closure_needs_revision':
      return 2
    case 'poor_candidate':
      return 3
    default:
      return 4
  }
}

function printBenchmarkSummary(benchmark, rows) {
  console.log(`\n## ${benchmark}`)
  console.log('| Candidate | Rubric | Kind | Source | Valid | Gates | Score | Interpretation |')
  console.log('| --- | --- | --- | --- | --- | --- | --- | --- |')

  const sorted = [...rows].sort((a, b) => {
    const aScore = a.payload?.totals?.overall ?? -1
    const bScore = b.payload?.totals?.overall ?? -1
    if (bScore !== aScore) return bScore - aScore
    const aRank = interpretationRank(a.payload?.totals?.interpretation)
    const bRank = interpretationRank(b.payload?.totals?.interpretation)
    return aRank - bRank
  })

  for (const row of sorted) {
    const rubricVersion = row.payload?.rubric_version ?? 'n/a'
    const kind = row.manifest?.run_kind ?? 'n/a'
    const source = row.manifest?.source_kind ?? 'n/a'
    const valid = row.payload ? (row.validation.ok && !row.readError ? 'yes' : 'no') : 'n/a'
    const gates = row.payload ? (row.payload?.hard_gates?.passed === false ? 'failed' : 'passed') : 'n/a'
    const score = row.payload?.totals?.overall ?? 'n/a'
    const interpretation = row.payload?.totals?.interpretation ?? 'n/a'
    console.log(`| ${row.candidate} | ${rubricVersion} | ${kind} | ${source} | ${valid} | ${gates} | ${score} | ${interpretation} |`)
  }
}

function printValidationProblems(rows) {
  const invalid = rows.filter((row) => row.payload && (!row.validation.ok || row.readError))
  if (invalid.length === 0) return

  console.log('\n## Validation Problems')
  for (const row of invalid) {
    console.log(`- ${row.benchmark}/${row.candidate}`)
    if (row.readError) console.log(`  read error: ${row.readError}`)
    if (!row.validation.ok) console.log(`  validator: ${row.validation.stderr || row.validation.stdout}`)
  }
}

function main() {
  const rows = collectRuns()

  if (rows.length === 0) {
    console.log('No runs found.')
    process.exit(0)
  }

  console.log('# PDA Lab Run Summary')
  console.log(`Generated from ${rows.length} run slot(s).`)

  const byBenchmark = new Map()
  for (const row of rows) {
    if (!byBenchmark.has(row.benchmark)) byBenchmark.set(row.benchmark, [])
    byBenchmark.get(row.benchmark).push(row)
  }

  for (const [benchmark, benchmarkRows] of [...byBenchmark.entries()].sort(([a], [b]) => a.localeCompare(b))) {
    printBenchmarkSummary(benchmark, benchmarkRows)
  }

  printValidationProblems(rows)
}

main()
