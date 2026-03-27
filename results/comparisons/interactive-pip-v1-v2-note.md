# interactive-pip: v1 vs v2 rescoring note

This note records the second selective rescoring under `pda-handoff-v2`.

## Pair Chosen

- `candidate-001` (baseline)
- `candidate-101` (external candidate)

This pair was chosen because the external failure mode was strongly about implementation-level diagnosis replacing semantic-level clarification.

## Main Result

`v2` again does not change the headline ranking.

- baseline remains maximally strong
- external candidate remains clearly poor

But as with the build/update benchmark, `v2` improves the explanatory power of the score:
- the external failure is named directly as abstraction-level miscentering
- the hard-gate language now matches the empirical result
- the benchmark's real distinction is more visible in the scoring artifact

## Why This Matters

Across both initial benchmarks, `v2` sharpens the same pattern:
- competent external responses fail not because they are incoherent
- but because they answer the wrong governing question

## Interpretation

This is enough to justify using `v2` as the forward scoring frame for optimizer work, while preserving `v1` for historical comparability.
