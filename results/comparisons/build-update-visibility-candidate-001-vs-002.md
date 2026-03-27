# build-update-visibility: candidate-001 vs candidate-002

## Summary

This comparison tests whether the current PDA loop can reject a candidate that is product-coherent in form but misframes the task.

- `candidate-001` frames the problem as build/update-state legibility.
- `candidate-002` frames the problem as deploy-time visibility.

The second framing is plausible on the surface, but wrong for the benchmark.

## Score Difference

- `candidate-001`: `30/30`, no hard-gate violations
- `candidate-002`: `15/30`, hard-gate failures

This mirrors the stronger `interactive-pip` adversarial result rather than the obviously weak comparison.

## What The Rubric Is Catching Well

1. Task misframing beneath good product taste
`candidate-002` chooses a low-weight landing-view presentation, which is product-coherent, but still fails because it never makes current-build identity or update availability explicit.

2. False closure from a plausible UI choice
The run looks resolved after choosing landing-view placement, yet the decisive state-legibility ambiguity remains hidden.

3. Reliable execution of the wrong task
The handoff is delegation-friendly in form, but would reliably produce the wrong implementation.

4. Structural difference between deploy-time display and stale-client legibility
The rubric correctly treats these as materially different, not as interchangeable presentational variants.

## Why This Comparison Matters

This is stronger than merely showing that the rubric rejects bad traces.

It shows the loop can reject:
- a neat, coherent, product-sensible handoff
- if that handoff is centered on the wrong abstraction of the problem

That is exactly the kind of failure a PDA-oriented evaluator needs to catch.

## Current State Of The Loop

Across the first benchmark pair, the loop can now distinguish:
- strong closure
- obvious shallowness
- polished but semantically misprioritized closure attempts
- polished but product-coherent misframings

That is enough pressure to begin cautious automation work.

## Remaining Risk

All adversarial examples are still authored internally to the lab's own understanding.

So the next real threshold is not more synthetic cases of the same kind, but introducing:
- independently authored candidate traces
- or a real optimization engine producing candidate artifacts that may fail in less anticipated ways

## Next Decision

Decide whether the next step should be:
1. lightweight automation over the existing artifacts and benchmark pair
2. one more independently shaped candidate source before automation
