#!/usr/bin/env node

const fs = require('fs')
const path = require('path')

const ALLOWED_GATE_VIOLATIONS = new Set([
  'premature_implementation_with_tacit_policy',
  'no_forced_vs_chosen_separation',
  'skipped_option_resolution_when_required',
  'premature_recomposition',
  'collapsed_required_phase_structure',
  'omitted_declared_irrelevancies_or_nongoals',
])

const INTERPRETATIONS = new Set([
  'strong_pda_handoff',
  'usable_but_leaky',
  'weak_closure_needs_revision',
  'poor_candidate',
])

const HUMAN_ANSWERS = new Set(['yes', 'mixed', 'no'])

const PHASE_DIMENSIONS = {
  descent: [
    'ambiguity_localization',
    'forced_vs_chosen_separation',
    'question_discipline',
    'non_premature_descent',
    'optioning_readiness_discipline',
  ],
  option_resolution: [
    'explicit_residual_policy',
    'option_quality',
    'default_quality',
    'resolution_sufficiency',
    'recursive_return_discipline',
  ],
  recomposition: [
    'implementation_readiness',
    'structural_fidelity',
    'canonicality',
    'delegation_reliability',
    'declared_irrelevancies_and_nongoals',
  ],
}

function fail(errors, message) {
  errors.push(message)
}

function isObject(value) {
  return value !== null && typeof value === 'object' && !Array.isArray(value)
}

function validateDimension(errors, value, label) {
  if (!isObject(value)) {
    fail(errors, `${label} must be an object`)
    return 0
  }
  if (!Number.isInteger(value.score) || value.score < 0 || value.score > 2) {
    fail(errors, `${label}.score must be an integer between 0 and 2`)
  }
  if ('rationale' in value && typeof value.rationale !== 'string') {
    fail(errors, `${label}.rationale must be a string when present`)
  }
  return Number.isInteger(value.score) ? value.score : 0
}

function validateHumanAssessment(errors, value, label) {
  if (!isObject(value)) {
    fail(errors, `${label} must be an object`)
    return
  }
  if ('answer' in value && !HUMAN_ANSWERS.has(value.answer)) {
    fail(errors, `${label}.answer must be one of yes, mixed, no`)
  }
  if ('rationale' in value && typeof value.rationale !== 'string') {
    fail(errors, `${label}.rationale must be a string when present`)
  }
}

function validate(filePath) {
  const raw = fs.readFileSync(filePath, 'utf8')
  const data = JSON.parse(raw)
  const errors = []

  if (!isObject(data)) {
    return ['Top-level value must be an object']
  }

  if (data.rubric_version !== 'pda-handoff-v1') {
    fail(errors, 'rubric_version must equal pda-handoff-v1')
  }
  if (typeof data.candidate_id !== 'string' || data.candidate_id.length === 0) {
    fail(errors, 'candidate_id must be a non-empty string')
  }
  if (typeof data.benchmark_id !== 'string' || data.benchmark_id.length === 0) {
    fail(errors, 'benchmark_id must be a non-empty string')
  }
  if ('notes' in data && typeof data.notes !== 'string') {
    fail(errors, 'notes must be a string when present')
  }

  if (!isObject(data.hard_gates)) {
    fail(errors, 'hard_gates must be an object')
  } else {
    if (typeof data.hard_gates.passed !== 'boolean') {
      fail(errors, 'hard_gates.passed must be a boolean')
    }
    if (!Array.isArray(data.hard_gates.violations)) {
      fail(errors, 'hard_gates.violations must be an array')
    } else {
      const seen = new Set()
      for (const violation of data.hard_gates.violations) {
        if (!ALLOWED_GATE_VIOLATIONS.has(violation)) {
          fail(errors, `unknown hard gate violation: ${violation}`)
        }
        if (seen.has(violation)) {
          fail(errors, `duplicate hard gate violation: ${violation}`)
        }
        seen.add(violation)
      }
    }
    if ('rationale' in data.hard_gates && typeof data.hard_gates.rationale !== 'string') {
      fail(errors, 'hard_gates.rationale must be a string when present')
    }
  }

  const computedTotals = {}

  if (!isObject(data.phase_scores)) {
    fail(errors, 'phase_scores must be an object')
  } else {
    for (const [phase, dimensions] of Object.entries(PHASE_DIMENSIONS)) {
      const phaseValue = data.phase_scores[phase]
      if (!isObject(phaseValue)) {
        fail(errors, `phase_scores.${phase} must be an object`)
        computedTotals[phase] = 0
        continue
      }
      let subtotal = 0
      for (const dimension of dimensions) {
        subtotal += validateDimension(errors, phaseValue[dimension], `phase_scores.${phase}.${dimension}`)
      }
      computedTotals[phase] = subtotal
    }
  }

  if (!isObject(data.totals)) {
    fail(errors, 'totals must be an object')
  } else {
    const overall = Object.values(computedTotals).reduce((sum, value) => sum + value, 0)
    for (const phase of Object.keys(PHASE_DIMENSIONS)) {
      const total = data.totals[phase]
      if (!Number.isInteger(total) || total < 0 || total > 10) {
        fail(errors, `totals.${phase} must be an integer between 0 and 10`)
      } else if (computedTotals[phase] !== total) {
        fail(errors, `totals.${phase} must equal computed subtotal ${computedTotals[phase]}`)
      }
    }
    if (!Number.isInteger(data.totals.overall) || data.totals.overall < 0 || data.totals.overall > 30) {
      fail(errors, 'totals.overall must be an integer between 0 and 30')
    } else if (data.totals.overall !== overall) {
      fail(errors, `totals.overall must equal computed total ${overall}`)
    }
    if ('phase_minimums_passed' in data.totals && typeof data.totals.phase_minimums_passed !== 'boolean') {
      fail(errors, 'totals.phase_minimums_passed must be a boolean when present')
    }
    if ('interpretation' in data.totals && !INTERPRETATIONS.has(data.totals.interpretation)) {
      fail(errors, 'totals.interpretation must be a valid interpretation label')
    }
  }

  if ('human_review' in data) {
    if (!isObject(data.human_review)) {
      fail(errors, 'human_review must be an object when present')
    } else {
      if ('performed' in data.human_review && typeof data.human_review.performed !== 'boolean') {
        fail(errors, 'human_review.performed must be a boolean when present')
      }
      if ('summary' in data.human_review && typeof data.human_review.summary !== 'string') {
        fail(errors, 'human_review.summary must be a string when present')
      }
      if ('questions' in data.human_review) {
        if (!isObject(data.human_review.questions)) {
          fail(errors, 'human_review.questions must be an object when present')
        } else {
          for (const [key, value] of Object.entries(data.human_review.questions)) {
            validateHumanAssessment(errors, value, `human_review.questions.${key}`)
          }
        }
      }
    }
  }

  return errors
}

function main() {
  const filePath = process.argv[2]
  if (!filePath) {
    console.error('Usage: node scripts/validate-rubric.js <rubric-json>')
    process.exit(1)
  }

  const resolved = path.resolve(process.cwd(), filePath)
  let errors
  try {
    errors = validate(resolved)
  } catch (error) {
    console.error(`Validation failed: ${error.message}`)
    process.exit(1)
  }

  if (errors.length > 0) {
    console.error('Rubric payload is invalid:')
    for (const error of errors) {
      console.error(`- ${error}`)
    }
    process.exit(1)
  }

  console.log(`Rubric payload is valid: ${resolved}`)
}

main()
