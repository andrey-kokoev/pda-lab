# Eval

Lightweight automation for the current PDA lab loop.

## Current Scripts

- `summarize-runs.js`
  - scans `results/runs/**/score/evaluation.json`
  - validates each payload with `scripts/validate-rubric.js`
  - groups runs by benchmark
  - emits a compact markdown summary

- `export-optimizer-dataset.js`
  - scans benchmark packages and run manifests
  - prefers `score-v2/evaluation.json` when present, else falls back to `score/evaluation.json`
  - exports a compact machine-readable dataset for future optimizer work

## Usage

```bash
node eval/summarize-runs.js
node eval/export-optimizer-dataset.js
```

To refresh checked-in outputs:

```bash
node eval/summarize-runs.js > results/summary.md
node eval/export-optimizer-dataset.js > results/optimizer-dataset.json
```
