# interactive-pip: candidate-301 vs candidate-302

## Why this comparison matters

`candidate-302` is the first PiP run generated after adding an explicit benchmark-faithfulness contract to the DSPy generator. The question is whether that contract improved measured benchmark-faithfulness without collapsing the model back into vagueness.

## candidate-301

Strengths:
- clears the abstraction-level hurdle
- produces a genuine interaction-spec handoff
- identifies the major policy loci correctly

Weaknesses:
- invents unsupported numeric policy values
- narrows scope to desktop only
- turns some benchmark-specific closure into generic but wrong defaults

## candidate-302

Strengths:
- still clears the abstraction-level hurdle
- explicitly binds itself to the benchmark reference
- stops inventing unsupported numeric values for thresholds, percentages, and bounds
- better separates structural policy from tunable implementation parameters

Weaknesses:
- still narrows scope to desktop
- still leaves some benchmark-settled directions too open
- improves faithfulness more by avoiding wrong choices than by recovering the full reference closure state

## What changed

The key gain is not stylistic. It is epistemic:
- `candidate-301` fabricated plausible policy
- `candidate-302` refrains from fabrication when the benchmark reference does not ground a concrete value

That makes `candidate-302` safer and more benchmark-faithful even though it is not yet as complete as the hand-authored baseline.

## Takeaway

The faithfulness contract appears to work.

It did not solve the benchmark completely, but it improved the generator in the direction that matters next:
- less invented policy
- stronger attachment to benchmark closure state
- better delegation reliability

The next bottleneck is now narrower:
- preserving benchmark scope and chosen directions, not just avoiding fabricated specifics.
