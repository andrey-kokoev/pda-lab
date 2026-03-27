# Example: Build/Update Visibility

## Phase 1: Descent

### Raw Task

For our app, it is difficult to know if mobile is cached or refreshed. What are coherent options to fix it? Last time of deploy?

### Live Ambiguity

The live ambiguity resides in what product state actually needs to be made legible, not yet in a specific UI treatment.

### Forced Structure

- users need to tell whether they are on a stale client
- the solution must fit the product UI coherently

### Contingent Policy

- whether the relevant state is deploy time, current build identity, latest available build, update availability, or some combination
- where in the product this state belongs
- how prominent it should be in steady state

### Decision-Relevant Question

What exact state must be legible before choosing a UI pattern?

## Optioning Readiness Test

- layer localized: yes
- concrete choice point: yes
- options can be stated cleanly: yes
- choice materially constrains implementation: yes

## Phase 2: Option Resolution

### Explicit Choice Point

User-visible build/update state.

### Options

a. Deploy time only.
b. Current build identity plus update availability, with deploy time as supporting metadata. `(*)`

### Recorded Choice

Selected `b`: the task is build/update-state visibility, not just deploy timestamp display.

### Return Check

This exposes a deeper product question: where should this information live so that it is helpful without overstating itself? Return to descent.

## Phase 1: Descent

### Live Ambiguity

The live ambiguity now resides in placement and prominence.

### Forced Structure

- the state should be user-visible
- the presentation should not read as modal or primary-action UI in steady state

### Contingent Policy

- landing view only vs call view vs diagnostics
- muted text vs badge/banner vs modal-style affordance
- whether deploy time is shown always or only as supporting metadata

### Decision-Relevant Question

Where does this state belong most coherently in the product?

## Optioning Readiness Test

- layer localized: yes
- concrete choice point: yes
- options can be stated cleanly: yes
- choice materially constrains implementation: yes

## Phase 2: Option Resolution

### Explicit Choice Point

Product placement.

### Options

a. Landing view only, as low-weight text. `(*)`
b. Call view footer/corner badge.
c. Diagnostics/about only.

### Recorded Choice

Selected `a`: status belongs on landing view as subdued text.

### Return Check

One more explicit policy fork remains about steady-state prominence and metadata composition. Continue option resolution.

## Phase 2: Option Resolution

### Explicit Choice Point

Steady-state presentation.

### Options

a. Simple muted text, interactive only when update is available. `(*)`
b. Persistent badge or floating status element.
c. Modal or banner-style presentation.

### Recorded Choice

Selected `a`: the UI should stay low-weight and non-modal in steady state.

### Return Check

A remaining metadata-composition question can now be resolved directly without deeper descent. Continue option resolution.

## Phase 2: Option Resolution

### Explicit Choice Point

Deploy-time composition.

### Options

a. Show deploy time as primary content.
b. Show deploy time only as supporting metadata beneath build/update state. `(*)`
c. Omit deploy time entirely.

### Recorded Choice

Selected `b`: deploy time is secondary to build identity and update availability.

### Return Check

No deeper ambiguity remains that materially affects execution.

## Phase 3: Recomposition

### Closure Summary

The task is now non-ambiguous as landing-view build/update-state visibility with low-weight text treatment and deploy time only as supporting metadata.

### Declared Irrelevancies / Non-goals

- in-call status UI is out of scope
- full diagnostics/about surfacing is not required for this task

### Closed Formulation

Implement low-weight landing-view text that exposes current build identity and update availability, with deploy time only as supporting metadata.

### Implementation Task

Add build metadata and update detection, surface them in subdued landing-view text, and keep call views free of the status UI.

### Validation Target

- review for product-coherent placement and prominence
- verify current-build metadata and update availability behavior
- verify deploy time is secondary rather than primary
- run project checks
