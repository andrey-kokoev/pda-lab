# Benchmarks

Each benchmark package should contain:
- raw task statement
- baseline repo state reference
- reference closed formulation
- expected policy questions
- validation criteria

Some benchmarks should also contain:
- chosen directions

Use `reference/chosen-directions.md` when the benchmark has already settled concrete directions that are stronger than a general closed formulation. This file exists to prevent the generator from either:
- inventing plausible generic specifics
- or staying too abstract after avoiding invention

A good rule:
- closed formulation captures the shape of adequate closure
- chosen directions capture benchmark-specific commitments that should be preserved rather than reopened


## Authoring Rule

Add `reference/chosen-directions.md` only when all of these are true:
- the benchmark already has settled concrete directions
- those directions materially affect implementation or delegation fidelity
- a closed formulation alone would likely let the model either invent specifics or stay too abstract

Do not add `chosen-directions.md` when:
- the benchmark is still supposed to elicit those choices
- the directions are merely stylistic or low-impact
- the closed formulation already determines enough without risk of generic drift

Short version:
- use `chosen-directions.md` to preserve already-earned closure
- do not use it to smuggle in choices the benchmark is supposed to surface
