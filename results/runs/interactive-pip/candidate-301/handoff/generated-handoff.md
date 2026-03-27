# Implementation Handoff: Desktop PiP Drag/Resize

## Component Specification
Implement interactive Picture-in-Picture (PiP) overlay for desktop video player. PiP is a floating panel inside the main video region supporting drag-to-move and drag-to-resize.

## Geometry Model

### Coordinate System
- **Reference Frame:** Containing video element (0,0 at top-left, 1.0 at bottom-right)
- **PiP State:** `{x, y, width, height}` where all values are normalized floats [0.0–1.0]
- **Pixel Conversion:** Calculate at interaction time using current video client rect; never store absolute pixels

### Bounds & Constraints
- **Minimum Size:** 0.15 (15% of video dimension)
- **Maximum Size:** 0.80 (80% of video dimension)
- **Margin:** 8px padding from video edges (converted to normalized units dynamically)
- **Constraint Behavior:** Hard stop at boundaries; resize operations halt when min/max reached

## Hit Zone Definitions

Define zones as proportions of current PiP dimensions:

```
+------------------------+
| C | E (N) | C          |
| --+-------+--          |
| E |       | E          |
|(W)|   M   |(E)         |
| --+-------+--          |
| C | E (S) | C          |
+------------------------+
```

- **M (Center):** 60% × 60% central area → **Move gesture** (translate x,y)
- **E (Edges):** 20% bands on each side → **Single-axis resize**
  - N/S edges: Resize height only (y/height adjust)
  - E/W edges: Resize width only (x/width adjust)
- **C (Corners):** 20% × 20% intersection areas → **Dual-axis resize** (diagonal, adjusts x,y,width,height proportionally based on corner)

*Zones are disjoint; a point falls in exactly one category.*

## Gesture State Machine

### States
1. **Idle:** Awaiting input
2. **Pending:** Pointer down, awaiting movement threshold (3px)
3. **Active-Gesture:** Threshold crossed, mode determined by hit zone
4. **Complete:** Pointer up, cleanup required

### Transitions
- `pointerdown` → Capture pointer; set Pending; store start position and initial state snapshot
- `pointermove` + distance < 3px → remain Pending
- `pointermove` + distance ≥ 3px → determine zone from start position → enter Active-Gesture [Move|ResizeNS|ResizeEW|ResizeNE|ResizeNW|ResizeSE|ResizeSW]
- `pointermove` in Active → apply delta to relevant geometry axes; clamp to bounds; re-render
- `pointerup` → if was Active-Gesture, `preventDefault()` and stop propagation (suppress click); release capture; persist normalized state; return Idle
- `pointerup` from Pending (no movement) → release capture; allow event propagation (click passes through)

## Persistence Contract

- **Serialize:** On every gesture completion (pointerup), emit/update state with normalized coordinates.
- **Hydrate:** On mount/remount, read normalized state and convert to pixel layout using current video rect.
- **Reset:** If state invalid (e.g., video aspect ratio changed dramatically), clamp to nearest valid bounds rather than resetting to default.

## Implementation Checklist

- [ ] Implement hit zone calculator (returns zone type from normalized click position within PiP)
- [ ] Implement geometry clamp function (enforces min/max/margins)
- [ ] Implement pointer capture wrapper (handles setPointerCapture/releasePointerCapture)
- [ ] Implement move handler (delta applied to x,y)
- [ ] Implement resize handlers (delta applied to relevant edges; maintain opposite edge position for N/W resizes)
- [ ] Implement state persistence (normalized storage)
- [ ] Implement hydration (normalized → pixel conversion)
- [ ] Verify click suppression: underlying video controls should not receive click after drag operation
- [ ] Verify disjoint zones: no ambiguous cursor states (cursor changes indicate zone: move ↔ resize)

## Remaining Freedom (Out of Scope)
- Visual styling of PiP (shadows, borders) — use existing design system
- Animation during resize — optional, must not block gesture responsiveness
- Resize aspect ratio locking — not required; freeform rectangle
- Touch/mobile behavior — desktop mouse/touchpad only for this scope
