# Final Handoff

## Closure Summary

The task is now non-ambiguous as a cross-layout PiP consistency problem: interaction support should be unified wherever PiP appears, and the existing bugs should be fixed under that scope.

## Declared Irrelevancies / Non-goals

- exact visual styling of resize affordances is out of scope
- broader refactors outside PiP interaction are not required

## Closed Formulation

Implement unified PiP drag/resize support across all layouts that expose PiP, and fix the current interaction bugs while keeping behavior consistent across the app.

## Implementation Task

Wire unified pointer-based interaction into all PiP contexts, fix the known bugs, and ensure the PiP behaves consistently across layouts.

## Validation Target

- review cross-layout consistency
- verify desktop-capable interaction wherever PiP appears
- run project checks
