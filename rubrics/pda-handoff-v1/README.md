# pda-handoff-v1

Machine-readable schema for PDA handoff evaluation.

## Structure

This schema captures:
- hard-gate violations
- phase-separated scored dimensions
- equal-weight `0-2` scoring per dimension
- per-phase totals and overall total
- optional human finalist review

## Scoring Model

Phases:
- descent
- option resolution
- recomposition

Dimensions per phase:
- 5 each
- `0-2` per dimension
- `10` max per phase
- `30` max overall

Interpretation bands:
- `26-30`: `strong_pda_handoff`
- `21-25`: `usable_but_leaky`
- `16-20`: `weak_closure_needs_revision`
- `0-15`: `poor_candidate`

## Explicit Additions

This version now scores:
- optioning readiness discipline
- recursive return discipline from optioning back to descent
- declared irrelevancies / non-goals in recomposition

## Hard Gates

Candidates fail before scoring if they:
- jump to implementation with tacit policy
- fail to separate forced from chosen
- skip explicit option resolution when required
- recompose prematurely
- collapse phase structure when the benchmark requires it
- omit known declared irrelevancies or non-goals from the final handoff
