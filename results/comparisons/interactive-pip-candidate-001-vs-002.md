# interactive-pip: candidate-001 vs candidate-002

## Summary

This comparison checks whether the current PDA benchmark/template/rubric loop can discriminate between:
- `candidate-001`: a hand-authored strong run using `pda-handoff-template-v1`
- `candidate-002`: a deliberately shallow run that narrows too early and recomposes with hidden semantic ambiguity still present

## Score Difference

- `candidate-001`: `30/30`, no hard-gate violations
- `candidate-002`: `7/30`, hard-gate failures

This is a meaningful spread rather than a cosmetic difference.

## What The Rubric Is Catching Well

1. Mislocalized ambiguity
`candidate-002` treats the task mainly as desktop-wiring scope, while `candidate-001` localizes it to interaction semantics and then to free-panel policy.

2. Premature optioning
`candidate-002` introduces scope options before the decisive semantic fork is made explicit.

3. Premature recomposition
`candidate-002` produces a final handoff while major policy remains tacit.

4. Delegation unreliability
The weaker handoff would force a worker-agent to invent missing PiP semantics.

5. Missing bounded non-goals
The weaker run says `None` instead of explicitly bounding what is out of scope or irrelevant.

## What The Rubric May Still Miss

1. Self-authored perfection bias
`candidate-001` is still a hand-authored ideal trace scored by the same authorial stance that defined the rubric.

2. Over-rewarding stylistic PDA markers
A trace could potentially mimic the formal sections while still asking weak questions or choosing defaults poorly in a subtler way.

3. Limited pressure on recursive descent
`candidate-001` only returns from optioning to descent once. More difficult benchmarks may be needed to test repeated recursive descent.

4. Benchmark familiarity bias
Because the benchmark was derived from a known thread, the run benefits from hindsight about the important forks.

## Current Conclusion

The loop can now discriminate between a strong and a visibly weak handoff on the same benchmark.

That is enough to justify moving from pure scaffold-building into comparative evaluation.

It is not yet enough to claim that the rubric is robust against high-quality but semantically shallow imitations.

## Next Pressure Tests

1. Add a `candidate-003` that is polished and PDA-shaped in form, but subtly misprioritizes the ambiguity.
2. Compare performance on `build-update-visibility` with a similarly shallow counter-candidate.
3. Add a run note format for “what the scorer was uncertain about” so ambiguity in the rubric itself becomes visible.
