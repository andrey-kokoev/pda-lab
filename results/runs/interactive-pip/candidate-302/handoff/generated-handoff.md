## Implementation Specification: Interactive PiP (Desktop)

**Repository Context**: `telesense`  
**Scope**: Complete wiring for drag/resize behavior of desktop PiP panel.

### Closed Policy Decisions (Normative—Do Not Alter)

1. **Object Model**  
   PiP is a **free panel**, not an aspect-preserving video object. The interaction layer manipulates a rectangle; video rendering letterboxes within this rectangle if necessary.

2. **Geometry & Bounds**  
   - PiP exists as a **bounded rectangle** strictly inside the containing video region.  
   - Normalized coordinate system: all values expressed as ratios of container width/height (0.0–1.0 range).  
   - Persistence model: store `{nx, ny, nw, nh}` (normalized top-left x, y; normalized width, height).

3. **Gesture Ownership**  
   - On `pointerdown` inside any hit zone, PiP **captures pointer ownership** immediately.  
   - Ownership is held until `pointerup` (or `pointercancel`), regardless of pointer leaving the panel bounds.  
   - No other component processes pointer events during active ownership.

4. **Gesture Semantics**  
   - **Center zone**: Drag translates the panel (updates `nx`, `ny`).  
   - **Edge zones** (left, right, top, bottom): Resize one axis.  
     - Left/Right adjust `nw` and translate `nx` to maintain opposite edge position (or keep edge fixed—implementation choice, but must be consistent).  
     - Top/Bottom adjust `nh` and translate `ny`.  
   - **Corner zones**: Resize two axes simultaneously (diagonal resize).  
   - Zones are **disjoint**; a point cannot be in two zones simultaneously.

5. **Click Suppression**  
   **Policy**: Stateful suppression.  
   - Track `hasGestureActive` boolean from `gestureStart` to `gestureEnd`.  
   - If `hasGestureActive` was ever true during the pointer sequence, suppress the final `click` event (consume it without propagation).  
   - This prevents accidental clicks on underlying video controls after drag/resize operations.

### Open Implementation Parameters (To Be Defined by Implementer)

- **Proportional Hit Zones**: Specific percentage of panel dimension allocated to edges and corners (e.g., edge thickness = X%, corner size = Y%). Must satisfy disjointness constraint.  
- **Minimum/Maximum Size Constraints**: Optional bounds on `nw` and `nh` (declared irrelevant to policy if unbounded; implementer may add `minSize`/`maxSize` constants).  
- **Resize Anchor Behavior**: Whether resizing from left/top edges moves the origin (floating resize) or anchors the opposite edge (fixed resize). Either is acceptable if consistent.

### Wiring Checklist

1. **Audit Existing Code**  
   - Locate PiP component in `telesense` repo.  
   - Verify if pointer event handlers are attached.  
   - Check if normalized coordinate persistence exists; if using absolute pixels, refactor to normalized model.

2. **Implement Hit-Zone Detection**  
   - Calculate zones based on current panel dimensions and chosen proportional parameters.  
   - Ensure zones are recalculated on every resize.

3. **Wire Gesture State Machine**  
   - `idle` → `dragging` (center) or `resizing` (edge/corner) on `pointerdown`.  
   - Capture pointer in `pointerdown` handler.  
   - Update normalized geometry in `pointermove`.  
   - Apply bounds clamping (keep inside container).  
   - Transition to `idle` on `pointerup`, triggering persistence save.

4. **Implement Persistence**  
   - On `gestureEnd`, serialize `{nx, ny, nw, nh}` to storage.  
   - On component mount, deserialize and convert to absolute pixels for initial render.

5. **Add Click Suppression**  
   - Intercept `click` at the capture phase; check gesture state flag.  
   - If gesture was active, `preventDefault` and `stopPropagation`.

6. **Fix Issues Found in Review**  
   - If existing wiring uses video aspect ratio to constrain resize, **remove** (violates free panel policy).  
   - If existing wiring passes pointer events to parent during drag, **add capture** (violates ownership policy).  
   - If persistence uses absolute pixels, **migrate** to normalized coordinates.

### Verification Criteria

- **Bounded Geometry**: PiP rectangle never renders outside containing video region during or after interaction.  
- **Pointer Ownership**: During active drag/resize, video controls beneath PiP do not receive hover or click events.  
- **Persistence Round-Trip**: Resize panel, reload page/remount component, verify position and size restore exactly (within floating-point tolerance).  
- **Semantic Correctness**: Dragging center moves without resizing; edge handles resize only one dimension; corners resize both.  
- **Click Suppression**: Completing a drag or resize and releasing pointer does not trigger play/pause or other video controls.
