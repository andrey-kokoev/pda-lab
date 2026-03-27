# pda-handoff-v2

Second PDA handoff rubric version.

`v2` preserves the `v1` structure but adds abstraction-level fidelity as a first-class concept.

## Why v2 Exists

The strongest empirical signal in the lab so far is not merely weak-vs-strong output quality.
It is failure at the wrong abstraction level:
- competent responses
- plausible recommendations
- but centered on the wrong governing ambiguity

`v2` encodes that directly instead of forcing it to be inferred indirectly from other dimensions.

## Scoring Model

Phases:
- descent: 6 dimensions, max `12`
- option resolution: 5 dimensions, max `10`
- recomposition: 6 dimensions, max `12`
- total max: `34`

New explicit dimensions:
- `descent.abstraction_level_fidelity`
- `recomposition.abstraction_level_fidelity`

New hard gate available:
- `wrong_abstraction_level`

## Interpretation Bands

- `29-34`: `strong_pda_handoff`
- `23-28`: `usable_but_leaky`
- `17-22`: `weak_closure_needs_revision`
- `0-16`: `poor_candidate`

## Relationship To v1

- use `v1` for all existing scored historical runs
- use `v2` for new scoring passes where abstraction-level fidelity should be assessed explicitly
- do not silently rewrite old `v1` scores into `v2`
