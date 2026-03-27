# Trace

## Descent

### Raw Task

Review current changes in repo `telesense`, determine whether desktop PiP drag/resize behavior is actually wired up, complete the wiring, and fix the issues found in review.

### Live Ambiguity

The live ambiguity resides in interaction semantics, not just in implementation completeness.

### Forced Structure

- PiP must support drag/resize behavior.
- Desktop-capable input must actually be wired.
- Review findings must be fixed.

### Contingent Policy

- whether PiP should behave as a free panel or an aspect-preserving video object
- persistence semantics across resize/remount
- gesture ownership semantics
- hit-zone semantics
- click suppression semantics

### Decision-Relevant Question

What kind of manipulable object is the PiP supposed to be?

## Option Resolution

### Choice Point

PiP interaction model.

### Options

a. Aspect-preserving video object.
b. Free panel with bounded independent geometry. `(*)`

### Recorded Choice

Selected `b`: PiP is a free panel.

### Return Check

This exposes deeper ambiguity about free-panel semantics. Return to descent.

## Descent

### Live Ambiguity

The live ambiguity now resides in free-panel policy.

### Forced Structure

- geometry must stay bounded to the container
- input must work on desktop and touch-capable devices
- geometry changes should route through one canonicalization path

### Contingent Policy

- persistence semantics
- gesture ownership
- hit-zone semantics
- click suppression

### Decision-Relevant Question

Which remaining policy choice most constrains the rest of the implementation?

## Option Resolution

### Choice Point

Persistence semantics.

### Options

a. Preserve absolute pixels.
b. Preserve normalized top-left position and normalized width/height. `(*)`

### Recorded Choice

Selected `b`: use normalized origin and size.

### Return Check

No deeper ambiguity created. Continue optioning.

## Option Resolution

### Choice Point

Gesture ownership.

### Options

a. Share with parent where possible.
b. PiP owns the active gesture once started. `(*)`

### Recorded Choice

Selected `b`.

### Return Check

No deeper ambiguity created. Continue optioning.

## Option Resolution

### Choice Point

Hit-zone semantics.

### Options

a. Overlapping hit zones with precedence rules.
b. Disjoint proportional center/edge/corner zones. `(*)`

### Recorded Choice

Selected `b`.

### Return Check

No deeper ambiguity created. Continue optioning.

## Option Resolution

### Choice Point

Click suppression after drag/resize.

### Options

a. Suppress click after movement beyond a small fixed threshold. `(*)`
b. Do not suppress click.

### Recorded Choice

Selected `a`.

### Return Check

No deeper ambiguity remains that materially affects execution.
