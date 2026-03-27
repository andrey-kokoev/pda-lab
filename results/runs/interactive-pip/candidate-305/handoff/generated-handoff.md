# PiP Interactive Wiring: Implementation Handoff

## 1. Geometry Model
- **Type**: Free panel (decoupled from video aspect ratio).
- **Bounds**: Rectangle inside containing video region.
- **Constraints**:
  - Minimum: 120px × 120px.
  - Maximum: Up to full containing bounds (no arbitrary ratio limit).
- **Default Placement**: Bottom-right of containing region on initial mount.

## 2. Persistence & State
- **Storage Format**: Normalized values (0.0–1.0 range):
  - `origin`: top-left corner (x, y) relative to full containing region.
  - `size`: width and height relative to full containing region.
- **Restore Behavior**: No edge/corner snapping; geometry restored exactly from normalized values.
- **Video Metadata Independence**: Changes to video resolution or aspect ratio do not trigger panel reshape. Content fitting logic remains separate from panel geometry.

## 3. Input & Gesture Ownership
- **Event Model**: Unified pointer events (pointerdown/pointermove/pointerup/cancel), active wherever PiP appears.
- **Ownership**: PiP captures input once `pointerdown` occurs inside its bounds; owns the gesture until `pointerup` or `pointercancel`.
- **Mode Detection**: Gesture mode (move vs. resize) is fixed at `pointerdown` based on hit-zone location; does not change mid-gesture.

## 4. Hit Zones & Interaction Semantics
- **Layout**: Proportional bands, each one-sixth of panel dimension.
- **Disjoint Regions**:
  - **Center (2/3 × 2/3 inner area)**: Drag to move panel.
  - **Edges (one-sixth bands on sides)**: Drag to resize single axis:
    - Left/Right: Horizontal resize.
    - Top/Bottom: Vertical resize.
  - **Corners (one-sixth × one-sixth intersections)**: Drag to resize both axes simultaneously.
- **Click Suppression**: If pointer movement exceeds 8px from `pointerdown` origin, suppress the subsequent click event to prevent unintended navigation/controls.

## 5. Implementation Boundaries
- **Recomposition Allowed**: Implementation may proceed; all governing policy is forced.
- **Reviewable Against**: Bounded geometry (120px min, container max), pointer ownership (PiP-captured), and reset/persistence semantics (normalized coordinates, no snapping).
- **Exclusions**: Visual feedback styling, animation easing, and z-index stacking are outside the scope of this wiring task unless issues are found during review.
