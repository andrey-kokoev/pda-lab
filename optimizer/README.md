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
