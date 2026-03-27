# build-update-visibility: candidate-301 vs candidate-302

## Why this comparison matters

`candidate-302` is the first build-update-visibility run generated after adding the benchmark-faithfulness contract. Unlike the PiP case, the earlier `candidate-301` was already strong, so the relevant question is whether the contract improves the result or merely makes it safer and more abstract.

## candidate-301

Strengths:
- localizes the correct governing ambiguity
- produces a landing-only, non-modal build-legibility handoff
- includes concrete technical hooks like latest-version fetch and build-time identity injection

Weaknesses:
- some option structure is compressed into analysis rather than explicit closure artifacts
- a few choices are more asserted than derived

## candidate-302

Strengths:
- remains benchmark-faithful throughout
- avoids invention cleanly
- makes unresolved parameters and non-goals more explicit
- preserves the same landing-only, low-weight product direction

Weaknesses:
- is slightly more abstract and less technically specific than `candidate-301`
- gives up some implementation leverage in exchange for greater faithfulness discipline

## Takeaway

The faithfulness contract still helps here, but differently than it did on PiP.

For build-update-visibility:
- it does not produce a dramatic score increase
- it mainly trades a bit of technical concreteness for safer benchmark-faithfulness

So the contract appears broadly useful, but most valuable on the harder benchmark where invention was the dominant failure mode.
