# Reference Closed Formulation

Target closure for this benchmark:

- PiP is modeled as a free panel, not an aspect-preserving video object.
- Geometry is a bounded rectangle inside the containing video region.
- Input ownership belongs to the PiP once an active gesture starts.
- Gesture semantics are explicit:
  - center moves
  - edges resize one axis
  - corners resize two axes
- Hit zones are disjoint and proportional.
- Persistence uses normalized top-left origin plus normalized width/height.
- Recomposition is allowed only after remaining policy is forced, explicitly chosen, or irrelevant.

The benchmark should reward handoffs that surface and settle these policy decisions before implementation.
