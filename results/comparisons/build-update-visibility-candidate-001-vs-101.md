# build-update-visibility: candidate-001 vs candidate-101

## Summary

This is the lab's first comparison against a genuinely external candidate source.

- `candidate-001` is the hand-authored PDA baseline.
- `candidate-101` is an externally sourced response preserved and scored without rewriting.

The external response is competent and helpful in a general product/support sense, but it still fails the benchmark decisively.

## Score Difference

- `candidate-001`: `30/30`, no hard-gate violations
- `candidate-101`: `9/30`, hard-gate failures

This is important because `candidate-101` is neither sloppy nor obviously incoherent.

## What The External Candidate Did Well

1. It recognized the real-world importance of stale-client visibility.
2. It produced a coherent option survey.
3. It gave a practical recommendation.
4. It included implementation-oriented detail.

So the low score is not because the response was useless in general.

## Why It Still Failed The Benchmark

1. It generalized too quickly
Instead of shaping the task around the specific product ambiguity, it expanded into a generic diagnostic-feature design space.

2. It never isolated the decisive choice point
The benchmark required explicit differentiation among:
- current build identity
- latest available build
- update availability
- deploy time as supporting metadata

The external candidate never sharpened that fork.

3. It recommended before localizing
It moved to a bundled multi-layer solution before clarifying where the information belonged in the product and what state mattered most.

4. It drifted toward settings/about and debug overlays
Those are sensible generic patterns, but they miss the benchmark's intended landing-view, low-weight, product-coherent outcome.

## Why This Matters

This is the first evidence that the lab is not merely discriminating among self-authored examples.

It can also reject a competent external response when that response:
- broadens instead of localizes
- bundles instead of isolating the live fork
- recommends before de-arbitrarizing

That is a meaningful threshold.

## What This Suggests About PDA

The external candidate's failure mode is not stupidity.
It is exactly the default helpfulness pattern PDA is meant to resist:
- surface many plausible options
- recommend a reasonable bundle
- leave the decisive hidden arbitrariness unresolved

So this comparison is a good validation of the underlying method, not just the rubric.

## Remaining Caution

This is still only one external candidate on one benchmark.
A stronger claim would require:
- more external candidates
- at least one external candidate on `interactive-pip`
- and eventually optimizer-generated candidates

## Next Best Move

Prepare an external `interactive-pip` candidate slot analogous to `candidate-101`, then repeat the same test with a technically heavier benchmark.
