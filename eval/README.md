# Eval

Lightweight automation for the current PDA lab loop.

## Current Script

- `summarize-runs.js`
  - scans `results/runs/**/score/evaluation.json`
  - validates each payload with `scripts/validate-rubric.js`
  - groups runs by benchmark
  - emits a compact markdown summary

## Usage

```bash
node eval/summarize-runs.js
```

To refresh the checked-in summary:

```bash
node eval/summarize-runs.js > results/summary.md
```
