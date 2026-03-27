# Trace

## Descent

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

## Option Resolution

### Choice Point

User-visible build/update state.

### Options

a. Deploy time only.
b. Current build identity plus update availability, with deploy time as supporting metadata. `(*)`

### Recorded Choice

Selected `b`.

### Return Check

This exposes a deeper ambiguity about placement and prominence. Return to descent.

## Descent

### Live Ambiguity

The live ambiguity now resides in placement and prominence.

### Forced Structure

- the state should be user-visible
- steady-state presentation should not read as modal or primary-action UI

### Contingent Policy

- landing view only vs call view vs diagnostics
- muted text vs badge/banner vs modal-style affordance
- whether deploy time is primary, secondary, or absent

### Decision-Relevant Question

Where does this state belong most coherently in the product?

## Option Resolution

### Choice Point

Product placement.

### Options

a. Landing view only, as low-weight text. `(*)`
b. Call view footer/corner badge.
c. Diagnostics/about only.

### Recorded Choice

Selected `a`.

### Return Check

A presentation and composition fork remains, but no deeper ambiguity was exposed. Continue optioning.

## Option Resolution

### Choice Point

Steady-state presentation.

### Options

a. Simple muted text, interactive only when update is available. `(*)`
b. Persistent badge or floating status element.
c. Modal or banner-style presentation.

### Recorded Choice

Selected `a`.

### Return Check

A final metadata-composition fork remains. Continue optioning.

## Option Resolution

### Choice Point

Deploy-time composition.

### Options

a. Show deploy time as primary content.
b. Show deploy time only as supporting metadata beneath build/update state. `(*)`
c. Omit deploy time entirely.

### Recorded Choice

Selected `b`.

### Return Check

No deeper ambiguity remains that materially affects execution.
