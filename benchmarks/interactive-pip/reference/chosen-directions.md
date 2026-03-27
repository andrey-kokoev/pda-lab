# Chosen Directions

These benchmark-specific directions are already settled and should be preserved in generated handoffs rather than reopened or replaced with generic defaults.

- PiP is a free panel.
- Persistence uses normalized top-left origin plus normalized width and height, measured against the full containing region.
- No edge/corner snapping on restore.
- Input uses unified pointer-event semantics wherever the PiP appears, not desktop-only wiring.
- PiP owns the active gesture once it starts.
- Gesture mode is fixed at pointerdown.
- Click is suppressed after movement past an explicit threshold.
- The movement threshold is 8px.
- Hit zones are disjoint proportional regions, using one-sixth border bands on all sides.
- Center moves; edges resize one axis; corners resize two axes.
- Minimum size is fixed at 120px by 120px.
- Maximum size may expand up to the containing bounds rather than using an arbitrary smaller ratio.
- Video metadata changes do not reshape panel geometry.
- Content fitting is separate from panel geometry.
- Default placement is bottom-right.
