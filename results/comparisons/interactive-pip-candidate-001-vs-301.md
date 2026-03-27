# interactive-pip: candidate-001 vs candidate-301

## Why this comparison matters

This is the first optimizer-generated run on the harder PiP benchmark. The relevant question is not whether `candidate-301` is perfect, but whether it clears the abstraction-level failure mode that defeated the earlier external run while remaining meaningfully benchmark-faithful.

## candidate-001

Strengths:
- localizes the governing ambiguity correctly
- resolves the benchmark's actual chosen policy values
- preserves cross-platform scope
- produces a canonical implementation-ready handoff with little semantic drift

This remains the benchmark-faithful reference.

## candidate-301

Strengths:
- stays at the correct semantic layer instead of collapsing into implementation review
- identifies the main policy loci: object model, persistence, hit zones, gesture ownership, and bounds
- produces a real interaction-spec handoff rather than generic UI advice

Weaknesses:
- substitutes plausible generic policy for the benchmark's actual settled values
- narrows scope to desktop only, contradicting the benchmark's unified pointer-support direction
- chooses the wrong threshold, min/max sizing policy, and hit-zone proportions
- compresses explicit option resolution into assertion more than the reference run

## What the rubric is catching

The v2 rubric scores `candidate-301` as `usable_but_leaky` rather than failing it outright.

That is the right outcome.

It should not fail for wrong abstraction level, because it clearly solves the right kind of problem.
It should not match the baseline, because benchmark-faithfulness still leaks materially in the chosen policy values.

## Takeaway

`candidate-301` is the first optimizer-generated PiP run that meaningfully crosses the main threshold for this benchmark:
- it de-arbitrarizes the task instead of reviewing code wiring

But it also shows the next bottleneck for optimizer work:
- getting the model to stay faithful to benchmark-specific closure state rather than inventing coherent generic policy.
