# interactive-pip: candidate-001 vs candidate-003

## Summary

This comparison is more important than the `001 vs 002` comparison because `candidate-003` is not obviously weak in form.

It uses:
- clean PDA-like sectioning
- a localized ambiguity
- a well-formed question
- explicit options
- a compact final handoff

But it still fails the benchmark because it prioritizes the wrong ambiguity.

## Score Difference

- `candidate-001`: `30/30`, no hard-gate violations
- `candidate-003`: `15/30`, hard-gate failures

This is a stronger test of whether the rubric can catch semantic shallowness beneath good form.

## What The Rubric Is Catching Well

1. Misprioritized ambiguity
`candidate-003` localizes a real ambiguity, but not the decisive one for the benchmark. It foregrounds layout parity instead of interaction semantics.

2. False closure
The trace uses a polished return check to justify recomposition, but major interaction-policy ambiguity is still hidden.

3. Surface PDA mimicry
The candidate looks disciplined in form, yet still fails because the optioned fork does not constrain the benchmark's core implementation semantics enough.

4. Delegation drift risk
A worker-agent receiving the `candidate-003` handoff would still have to invent free-panel vs video-object semantics, persistence, hit-zone semantics, and click suppression behavior.

## Why This Comparison Matters

`candidate-002` showed that the rubric can reject obvious shallowness.

`candidate-003` shows something stronger:
- the rubric can also reject a candidate that is stylistically PDA-shaped but semantically off-center.

That is the first sign that the loop is not merely rewarding compliance theater.

## Remaining Risks

1. Authorial coupling still exists
The benchmark, good candidate, bad candidate, and rubric are all still authored from the same understanding.

2. The hard-gate boundary may still be too severe
A future candidate might deserve a weak-but-usable rating rather than immediate hard-fail, even if it leaves some semantic ambiguity unresolved.

3. Only one benchmark has adversarial comparison pressure so far
The same pressure needs to be applied to `build-update-visibility`.

## Current Conclusion

The current loop can distinguish:
- strong closure
- obvious shallowness
- polished but misprioritized shallowness

That is enough to justify moving forward with adversarial benchmark pressure on the second benchmark.

## Next Pressure Test

Add a `candidate-002` or `candidate-003` style counter-run for `build-update-visibility`, ideally one that looks product-coherent but still misframes the real state-legibility problem.
