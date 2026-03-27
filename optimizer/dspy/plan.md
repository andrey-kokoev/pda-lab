# DSPy Plan

## First Objective

Generate new candidate handoff artifacts for existing benchmarks using the exported optimizer dataset.

## Initial Candidate Shape

A DSPy-generated candidate should produce:
- a reasoning trace artifact
- a final handoff artifact
- no direct rubric score

Scoring remains external to the generator.

## First Target Benchmarks

Start with:
- `build-update-visibility`
- `interactive-pip`

## First Comparison Standard

Compare DSPy-generated candidates against:
- `candidate-001` baseline
- external candidates (`candidate-101`)
- adversarial synthetic candidates where useful

## Initial Success Condition

DSPy generates at least one candidate whose trace and handoff can be inserted into the existing run structure and scored cleanly under `v2`.
