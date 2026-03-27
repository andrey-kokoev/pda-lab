# Findings So Far

This note records the current empirical conclusions of `pda-lab` from the initial benchmark family and optimizer work.

## 1. The strongest early failure mode was wrong abstraction level

The first external candidates did not mainly fail by being incoherent or sloppy.
They often failed by solving a real but subordinate problem:
- implementation review instead of interaction semantics
- deploy-time visibility instead of build/update-state legibility
- generic diagnostics instead of product-coherent placement and scope

This justified the move from `pda-handoff-v1` to `pda-handoff-v2`, where abstraction-level fidelity became explicit in both scoring and hard-gate language.

## 2. Closed formulation improves abstraction-level fidelity

Adding a strong reference closed formulation reliably pushed generation toward the right layer of the problem.
This was enough to move the model away from shallow implementation talk and toward semantic task shaping.

But it was not always enough to preserve settled benchmark specifics.

## 3. Faithfulness constraints reduce fabricated specifics

Adding a benchmark-faithfulness contract improved behavior further.
The model became less likely to invent unsupported numeric thresholds, arbitrary policy ratios, or convenient scope restrictions.

This improvement mattered most on harder benchmarks such as `interactive-pip`, where generic but plausible invention was a major failure mode.

## 4. Chosen directions can be necessary for harder benchmarks

For `interactive-pip`, a closed formulation alone still left a gap:
- the model either invented plausible specifics
- or stayed too abstract after avoiding invention

Adding explicit `reference/chosen-directions.md` closed most of that gap.
This let the generator preserve already-earned closure without reopening it or fabricating substitutes.

Empirically, the PiP progression looked like:
- `candidate-301`: `25/34`
- `candidate-302`: `30/34`
- `candidate-303`: `33/34`

The main improvement came from layering:
1. closed formulation
2. faithfulness contract
3. chosen directions

## 5. The current model reaches a fixed point under strong grounding

Once the grounding stack was strong enough, naive within-model sampling on `interactive-pip` collapsed.
`candidate-304` through `candidate-310` reproduced the same answer shape as `candidate-303`.

This suggests that, for the current Kimi configuration, repeated single-shot samples are not a useful search strategy once the benchmark grounding is strong.

## 6. Extra LM passes are too expensive to be the practical default

Both the full draft/critique/revise program and the lighter critique-only path proved too slow for routine use on the harder benchmark.

This means the practical default for the current model is:
- grounded single-shot generation
- optional critique/revision only as targeted experiments

## 7. The current stack transfers across multiple ambiguity classes

The current grounded single-shot stack performs strongly across three different ambiguity classes:

- `build-update-visibility`
  state-legibility ambiguity
  automated best: `31/34`

- `interactive-pip`
  interaction-semantics ambiguity
  automated best: `33/34`

- `build-status-placement-scope`
  boundary/scope and presentation-weight ambiguity
  automated best: `33/34`

This is enough to say the current method is not narrowly overfit to a single benchmark shape.

## 8. Current practical default

For this model and repo, the current best practical pipeline is:
1. package benchmark with raw task, closed formulation, expected policy questions, and validation criteria
2. add `chosen-directions.md` only when the benchmark has already settled specifics that should not be reopened
3. use grounded single-shot generation as the default path
4. score under `pda-handoff-v2`
5. use extra passes only as explicit experiments, not routine generation

## 9. Current open question

The lab has shown how to improve generation quality by improving benchmark grounding.
The next open question is not primarily about more prompt depth.
It is about how to extend the benchmark family while preserving the same empirical discipline.
