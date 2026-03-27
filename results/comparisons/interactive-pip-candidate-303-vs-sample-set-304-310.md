# interactive-pip: candidate-303 vs sample set 304-310

## Why this note exists

After reaching `candidate-303`, the next question was whether within-model sampling would surface materially better or meaningfully different outputs under the same single-shot grounded generator.

## What happened

`candidate-304` through `candidate-310` collapsed to the same answer shape as `candidate-303` in both trace and handoff structure. The repeated outputs preserved the same settled benchmark directions:
- free panel
- normalized persistence
- one-sixth hit zones
- 8px click threshold
- 120px × 120px minimum
- unified pointer-event scope
- bottom-right default placement

## Interpretation

This suggests that, for the current Kimi configuration and prompt grounding stack, the generator has reached a near-deterministic fixed point on this benchmark.

That means the next bottleneck is not naive resampling. The meaningful gains so far came from better benchmark grounding:
1. closed formulation
2. faithfulness contract
3. chosen directions

## Consequence for optimization

For this model, prompt-side grounding currently appears more valuable than blind within-model sampling.

If future search is needed, it should come from:
- different program structure
- selective judging
- benchmark-packaging improvements

rather than repeated single-shot samples of the same grounded generator.
