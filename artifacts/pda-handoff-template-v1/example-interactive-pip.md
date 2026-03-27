# Example: Interactive PiP

## Phase 1: Descent

### Raw Task

Review current changes in repo `telesense`, determine whether desktop PiP drag/resize is wired, complete it, and fix the issues found.

### Live Ambiguity

The live ambiguity resides in interaction semantics, not only in wiring or bug-fixing.

### Forced Structure

- PiP must be draggable/resizable.
- Desktop-capable input must actually work.
- Known implementation defects must be fixed.

### Contingent Policy

- whether PiP is a free panel or a video-shaped object
- persistence semantics
- gesture ownership semantics
- hit-zone semantics
- click suppression semantics

### Decision-Relevant Question

What kind of object is the PiP supposed to be under manipulation?

## Optioning Readiness Test

- layer localized: yes
- concrete choice point: yes
- options can be stated cleanly: yes
- choice materially constrains implementation: yes

## Phase 2: Option Resolution

### Explicit Choice Point

Interaction model of the PiP.

### Options

a. Aspect-preserving video object.
b. Free panel with bounded independent geometry. `(*)`

### Recorded Choice

Selected `b`: PiP is a free panel, not a media-shaped object.

### Return Check

This choice resolves one fork but exposes deeper ambiguity about how the free panel should behave under move, resize, and persistence. Return to descent.

## Phase 1: Descent

### Live Ambiguity

The live ambiguity now resides in free-panel semantics.

### Forced Structure

- panel must stay bounded to container
- desktop and touch-capable interaction must both work
- geometry changes must be canonicalized through one path

### Contingent Policy

- what persists across resize/remount
- which hit zones define move vs edge resize vs corner resize
- how click suppression works after drag/resize
- who owns the gesture during active interaction

### Decision-Relevant Question

Which one of these policy choices most constrains the rest of the interaction model?

## Optioning Readiness Test

- layer localized: yes
- concrete choice point: yes
- options can be stated cleanly: yes
- choice materially constrains implementation: yes

## Phase 2: Option Resolution

### Explicit Choice Point

Persistence semantics.

### Options

a. Preserve absolute pixels.
b. Preserve normalized top-left position and normalized width/height. `(*)`

### Recorded Choice

Selected `b`: persistence uses normalized origin and size.

### Return Check

Other policy forks remain, but no deeper hidden ambiguity was exposed. Continue option resolution.

## Phase 2: Option Resolution

### Explicit Choice Point

Gesture ownership.

### Options

a. Share interaction with parent when possible.
b. PiP owns the active gesture once started. `(*)`

### Recorded Choice

Selected `b`: active PiP gestures suppress competing parent interaction.

### Return Check

No deeper ambiguity exposed. Continue option resolution.

## Phase 2: Option Resolution

### Explicit Choice Point

Hit-zone semantics.

### Options

a. Overlapping hit zones with precedence rules.
b. Disjoint proportional center/edge/corner zones. `(*)`

### Recorded Choice

Selected `b`: move, edge resize, and corner resize are classified by disjoint proportional zones.

### Return Check

No deeper ambiguity exposed. Continue option resolution.

## Phase 2: Option Resolution

### Explicit Choice Point

Click suppression after drag/resize.

### Options

a. Suppress click after movement beyond a small fixed threshold. `(*)`
b. Do not suppress click.

### Recorded Choice

Selected `a`: click is suppressed after meaningful drag/resize movement.

### Return Check

No deeper ambiguity remains that materially affects execution.

## Phase 3: Recomposition

### Closure Summary

The PiP is now non-ambiguous as a bounded free panel with normalized persistence, explicit gesture ownership, disjoint hit zones, and click suppression after meaningful movement.

### Declared Irrelevancies / Non-goals

- media aspect-ratio changes do not control panel geometry after initialization
- styling/theme choices of the PiP chrome are not part of this task

### Closed Formulation

Implement PiP as a free panel with explicit move, edge-resize, and corner-resize semantics, bounded to its container, with normalized persistence, exclusive gesture ownership, disjoint proportional hit zones, and click suppression after meaningful movement.

### Implementation Task

Wire desktop-capable input, route all geometry changes through one canonicalization path, and fix the known interaction defects under the chosen semantics.

### Validation Target

- review for semantic-policy fidelity
- check bounded geometry and gesture ownership
- verify persistence behavior
- verify hit-zone classification and click suppression behavior
- run project checks
