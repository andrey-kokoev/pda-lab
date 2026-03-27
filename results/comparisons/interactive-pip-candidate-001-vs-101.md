# interactive-pip: candidate-001 vs candidate-101

## Summary

This is the lab's first comparison against a genuinely external candidate source on the technically heavier PiP benchmark.

- `candidate-001` is the hand-authored PDA baseline.
- `candidate-101` is an externally sourced review/handoff preserved and scored without rewriting.

The external response is technically competent and identifies a real fix, but it still fails the benchmark decisively.

## Score Difference

- `candidate-001`: `30/30`, no hard-gate violations
- `candidate-101`: `9/30`, hard-gate failures

This matters because `candidate-101` is not sloppy. It is a plausible review outcome that would likely be considered useful in ordinary engineering workflow.

## What The External Candidate Did Well

1. It inspected the actual code structure.
2. It identified a concrete CSS conflict in `CallMobileLayout.vue`.
3. It proposed a bounded implementation fix.
4. It included verification steps and optional improvements.

So the low score is not because the response lacked practical value.

## Why It Still Failed The Benchmark

1. It answered at the implementation-diagnosis layer
The benchmark required surfacing the interaction-policy semantics that govern the whole feature. The external candidate instead anchored on a concrete CSS conflict.

2. It never isolated the decisive semantic forks
The benchmark needed explicit treatment of:
- free panel vs video-shaped object
- persistence semantics
- gesture ownership
- hit-zone semantics
- click suppression semantics

The external candidate left all of these implicit.

3. It mistook a real issue for the central issue
The CSS conflict was real, but not the main hidden arbitrariness the benchmark was built around.

4. It produced a reliable fix for a partial problem
A worker following the handoff would likely apply the CSS reset successfully, yet still not be guided toward the intended semantic closure of the feature.

## Why This Matters

This comparison is strong evidence that the lab is not just rewarding broad helpfulness or technically competent review.

It can reject a response that is:
- concrete
- repo-aware
- implementation-oriented
- and still wrong-centered for the benchmark

That is an important threshold for PDA.

## What This Suggests About PDA

The external candidate failed in a way that is especially instructive:
- it found something true
- it recommended something useful
- but it never asked whether that truth was the governing truth of the task

That is exactly the kind of hidden narrowing PDA is meant to catch.

## Current Conclusion

Across both initial benchmarks, the first external candidates failed for the same deeper reason:
- they were generally competent
- but they answered at the wrong abstraction level

That is the strongest result in `pda-lab` so far.

## Next Best Move

Commit and push the current `pda-lab` state, then decide whether the next phase should be:
1. lightweight optimizer integration
2. another external candidate source
3. stricter scoring around abstraction-level mislocalization
