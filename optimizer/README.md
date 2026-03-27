# Optimizer

Optimizer-facing integration surfaces live here.

Current status:
- dataset export exists in `results/optimizer-dataset.json`
- forward scoring frame is `rubrics/pda-handoff-v2`
- DSPy scaffold exists under `optimizer/dspy/`
- optimizer dataset now exports both `reference_closed_formulation` and `chosen_directions` when present

Current lesson:
- a reference closed formulation is enough to improve abstraction-level fidelity
- a faithfulness contract is enough to reduce fabricated specifics
- for harder benchmarks, explicit `chosen-directions.md` may still be necessary to recover already-settled benchmark choices without reopening them

So optimizer work should treat benchmark grounding as layered:
1. closed formulation
2. faithfulness contract
3. chosen directions, when the benchmark has settled specifics worth preserving


## When To Use Chosen Directions

Use `chosen-directions.md` only for benchmarks that have already earned specific commitments which should not be reopened during generation.

Use it when:
- settled directions materially affect implementation fidelity
- single-shot grounded generation still drifts into generic policy or over-abstraction
- preserving prior closure matters more than re-eliciting choice

Do not use it when:
- the benchmark is meant to test whether the model can surface those choices itself
- the directions are minor styling details or low-signal preferences
- the closed formulation already constrains the outcome sufficiently
