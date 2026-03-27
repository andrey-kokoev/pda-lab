# Forward Scoring Frame

## Decision

Use `rubrics/pda-handoff-v2` as the forward scoring frame for optimizer work.

Keep `rubrics/pda-handoff-v1` for historical comparability of existing scored runs.

## Reason

The lab's strongest empirical result so far is:
- competent responses often fail not because they are incoherent
- but because they answer the wrong governing question

`v2` encodes that directly through:
- abstraction-level fidelity in descent
- abstraction-level fidelity in recomposition
- the `wrong_abstraction_level` hard gate

## Practical Rule

- new rescoring work aimed at optimizer preparation should use `v2`
- old `v1` runs should not be silently rewritten
- where needed, keep side-by-side `score/` and `score-v2/` payloads
