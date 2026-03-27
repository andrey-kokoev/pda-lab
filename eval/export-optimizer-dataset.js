#!/usr/bin/env node

const fs = require('fs')
const path = require('path')

const ROOT = path.resolve(__dirname, '..')
const BENCHMARKS_DIR = path.join(ROOT, 'benchmarks')
const RUNS_DIR = path.join(ROOT, 'results', 'runs')

function readText(filePath) {
  return fs.existsSync(filePath) ? fs.readFileSync(filePath, 'utf8') : null
}

function readJson(filePath) {
  return fs.existsSync(filePath) ? JSON.parse(fs.readFileSync(filePath, 'utf8')) : null
}

function listDirectories(dir) {
  return fs.existsSync(dir)
    ? fs.readdirSync(dir, { withFileTypes: true }).filter((d) => d.isDirectory()).map((d) => d.name)
    : []
}

function pickScorePayload(runDir) {
  const v2 = path.join(runDir, 'score-v2', 'evaluation.json')
  const v1 = path.join(runDir, 'score', 'evaluation.json')
  if (fs.existsSync(v2)) return { path: v2, payload: readJson(v2), preferred: true }
  if (fs.existsSync(v1)) return { path: v1, payload: readJson(v1), preferred: false }
  return null
}

function collectBenchmarks() {
  const benchmarkIds = listDirectories(BENCHMARKS_DIR)
  return benchmarkIds.map((id) => {
    const dir = path.join(BENCHMARKS_DIR, id)
    return {
      benchmark_id: id,
      raw_task: readText(path.join(dir, 'raw', 'task.md')),
      reference_closed_formulation: readText(path.join(dir, 'reference', 'closed-formulation.md')),
      expected_policy_questions: readText(path.join(dir, 'reference', 'expected-policy-questions.md')),
      validation_criteria: readText(path.join(dir, 'validation', 'criteria.md')),
      baseline: readText(path.join(dir, 'baseline.md')),
    }
  })
}

function collectRuns() {
  const benchmarkIds = listDirectories(RUNS_DIR)
  const runs = []

  for (const benchmarkId of benchmarkIds) {
    const benchmarkDir = path.join(RUNS_DIR, benchmarkId)
    const candidateIds = listDirectories(benchmarkDir)

    for (const candidateId of candidateIds) {
      const runDir = path.join(benchmarkDir, candidateId)
      const manifest = readJson(path.join(runDir, 'manifest.json'))
      const score = pickScorePayload(runDir)

      runs.push({
        benchmark_id: benchmarkId,
        candidate_id: candidateId,
        manifest,
        score: score?.payload ?? null,
        score_path: score ? path.relative(ROOT, score.path) : null,
        score_is_v2_preferred: score ? score.preferred : false,
      })
    }
  }

  return runs
}

function main() {
  const payload = {
    generated_at: new Date().toISOString(),
    forward_rubric: 'pda-handoff-v2',
    historical_rubric: 'pda-handoff-v1',
    benchmarks: collectBenchmarks(),
    runs: collectRuns(),
  }

  process.stdout.write(JSON.stringify(payload, null, 2))
}

main()
