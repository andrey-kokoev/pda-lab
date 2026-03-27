# Trace

## Descent

### Raw Task

For our app, it is difficult to know if mobile is cached or refreshed. What are coherent options to fix it? Last time of deploy?

### Live Ambiguity

The live ambiguity resides in how prominently the latest deploy should be shown so users can tell whether they are on fresh code.

### Forced Structure

- users need a simple way to infer freshness
- the solution should fit the product UI coherently

### Contingent Policy

- where deploy time should be shown
- how prominent the deploy indicator should be
- whether the indicator belongs on landing or in call view

### Decision-Relevant Question

Where should deploy time be surfaced most coherently in the product?

## Optioning Readiness Test

- layer localized: yes
- concrete choice point: yes
- options can be stated cleanly: yes
- choice materially constrains implementation: yes

## Option Resolution

### Choice Point

Product placement.

### Options

a. Landing view footer text. `(*)`
b. Call-view badge.
c. Diagnostics only.

### Recorded Choice

Selected `a`: deploy time should appear as low-weight landing-view text.

### Return Check

No deeper ambiguity appears to block execution.
