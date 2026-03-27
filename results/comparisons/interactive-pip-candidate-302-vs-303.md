# interactive-pip: candidate-302 vs candidate-303

## Why this comparison matters

`candidate-303` is the first PiP run generated after adding explicit `chosen-directions.md` grounding on top of the broader faithfulness contract. The question is whether this new benchmark layer recovers the remaining settled directions without reintroducing invention.

## candidate-302

Strengths:
- preserves the right abstraction level
- avoids invented numeric policy
- separates structural policy from tunable implementation parameters

Weaknesses:
- still leaves some benchmark-settled directions too open
- does not recover the actual chosen threshold, hit-zone proportions, minimum size, or default placement as settled benchmark directions

## candidate-303

Strengths:
- preserves the right abstraction level
- recovers the benchmark's settled directions explicitly
- includes the actual 8px click threshold, one-sixth hit zones, 120px minimum, unified pointer scope, metadata-inert geometry, and bottom-right default placement
- remains compact and implementation-ready without speculative extras

Weaknesses:
- still somewhat direct in its phase structure, with less visible recursive return than the hand-authored baseline

## Takeaway

Adding explicit chosen directions appears to solve the narrower bottleneck identified after `candidate-302`.

The improvement is not merely stylistic:
- `candidate-302` avoided wrong specifics by staying abstract
- `candidate-303` preserves the right specifics because the benchmark now exposes them as settled directions

This suggests a useful optimizer lesson:
- for harder benchmarks, a closed formulation alone is not always enough
- when settled directions exist, exposing them explicitly can materially improve benchmark-faithfulness without inviting fresh invention
