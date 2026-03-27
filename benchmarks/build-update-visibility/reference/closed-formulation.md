# Reference Closed Formulation

Target closure for this benchmark:

- The problem is not merely “show deploy time”; it is making the currently running client build legible.
- The user-visible need is strongest on the landing view, not in-call UI.
- The solution should distinguish:
  - current build identity
  - latest available build identity
  - whether refresh is needed
- Status display should be low-weight, non-modal, and product-coherent.
- The handoff should avoid overbuilding diagnostics into call views.

The benchmark should reward traces that shape the task before implementation rather than jumping straight to a badge/banner widget.
