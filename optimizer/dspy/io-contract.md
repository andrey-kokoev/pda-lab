# DSPy IO Contract

## Input

Primary input source:
- `results/optimizer-dataset.json`

Required fields for generation:
- benchmark id
- raw task
- reference closed formulation
- expected policy questions
- validation criteria

## Output

For each generated candidate:
- `trace/*.md`
- `handoff/*.md`
- `manifest.json`

## Non-Output

DSPy generation should not emit:
- rubric scores
- benchmark edits
- rewritten reference artifacts

## Constraint

Generated artifacts should be saved in a run slot that preserves provenance, for example:
- `run_kind: automated`
- `source_kind: optimizer_generated`
