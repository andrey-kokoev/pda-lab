# build-update-visibility: v1 vs v2 rescoring note

This note records the first selective rescoring under `pda-handoff-v2`.

## Pair Chosen

- `candidate-001` (baseline)
- `candidate-101` (external candidate)

This pair was chosen because the external failure mode was most clearly about abstraction-level miscentering.

## Main Result

`v2` does not radically change the numeric separation in this pair.

- baseline remains maximally strong
- external candidate remains clearly poor

But `v2` improves the explanation quality of the score:
- the external failure is no longer only inferred from several dimensions
- it is now stated directly as abstraction-level failure
- the hard-gate vocabulary can name `wrong_abstraction_level`

## Why This Matters

The lab's strongest empirical result so far is that competent external candidates often fail by answering the wrong governing question.

`v2` now encodes that result directly.

## Interpretation

This suggests `v2` is a better fit for future optimizer work than `v1`, even if the first selective rescore does not yet change the headline ranking.
