# PiP Interaction Audit & Policy Closure Trace

## Initial Discovery (Repo: `telesense`)
Reviewing the current implementation revealed partial wiring: pointer events are reaching the PiP container, but the gesture semantics are undefined. The code contains commented-out drag handlers and hardcoded 8px "handles" with no geometric model. This is the classic "messy conversational start"—infrastructure present, policy absent.

## Policy Surfacing Phase

### 1. Object Model: Free Panel vs. Video Artifact
**Question:** Is PiP an aspect-preserving video object or a free UI panel?
- *Initial ambiguity:* Current CSS suggests `object-fit: contain`, implying video-shaped constraints.
- *Resolution:* **Free panel**. The PiP is a container that happens to hold video; geometry is determined by UI constraints, not video aspect ratio. The video content scales/crops to fit the panel, not vice versa.

### 2. Persistence Contract
**Question:** What survives remount/resize?
- *Initial ambiguity:* Absolute pixel coordinates in state suggest drift when window resizes.
- *Resolution:* **Normalized coordinates**. Store `{x, y, w, h}` as fractions of the parent video region (0.0–1.0 range). Origin is top-left of the containing video region. This ensures PiP maintains relative position and size across viewport changes.

### 3. Hit Zone Geometry
**Question:** How do we distinguish move from resize?
- *Initial ambiguity:* Current code has magic numbers (8px borders) with no semantic mapping.
- *Resolution:* **Disjoint proportional zones**.
  - **Center 60%**: Move (translate)
  - **Edge 20% bands**: Single-axis resize (N/S resize height, E/W resize width)
  - **Corner 20% intersections**: Dual-axis resize (diagonal)
  - Zones calculated dynamically based on current PiP dimensions, not fixed pixels.

### 4. Gesture Ownership & Click Suppression
**Question:** Who owns the pointer during interaction? How do we prevent click-through after drag?
- *Initial ambiguity:* Event bubbling suggests clicks leak to underlying video controls.
- *Resolution:* **Capture-based ownership**.
  - On `pointerdown`: PiP captures pointer set; enters "active gesture" state.
  - On `pointermove`: If displacement > threshold (3px), mark as "intentional gesture."
  - On `pointerup`: If gesture was intentional, call `preventDefault()` and stop propagation (suppresses click). Release capture.
  - If no movement (tap): allow propagation for click-to-focus/click-to-dismiss behavior.

### 5. Boundary Constraints
**Question:** What are the geometric limits?
- *Resolution:* **Bounded rectangle inside video region**.
  - Minimum size: 15% of video region width/height (prevents vanishing).
  - Maximum size: 80% of video region (prevents full occlusion).
  - Boundary margin: PiP must remain within video bounds with 8px "air gap."
  - Resize constraints: Maintain minimums; if corner resize hits min, lock aspect (soft constraint) or stop (hard constraint). **Decision:** Hard constraint (stop at min).

### 6. Closure Criteria
**Question:** When can implementation proceed?
- *Resolution:* All of the above must be explicit in the spec. Remaining degrees of freedom (visual styling, animation curves) are declared irrelevant to interaction correctness.

---

## Constraint Summary
- **Model:** Free rectangle (not video-shaped)
- **State:** Normalized `{x, y, w, h}` relative to video viewport
- **Input:** Pointer capture with gesture detection
- **Zones:** Center move, edges single-axis, corners dual-axis
- **Bounds:** 15%–80% size, 8px margin, hard min stops
- **Cleanup:** Click suppression via ownership model, not timers
