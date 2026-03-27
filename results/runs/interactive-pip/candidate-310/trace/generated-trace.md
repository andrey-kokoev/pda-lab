# PiP Interactive Wiring: Policy-to-Implementation Trace

## Starting Position
Raw task requires reviewing the `telesense` repo to determine if desktop PiP drag/resize behavior is wired up, completing the wiring, and fixing issues. The entry point is intentionally messy, preserving the conversational ambiguity of "actually wired up" without pre-cleaning hidden policy.

## Surfacing Governing Ambiguities

**Policy Locus 1: Object Model**
The reference formulation establishes PiP must be a *free panel*, not an aspect-preserving video object. This is a normative architectural target. Without closure here, implementation would incorrectly bind geometry to video metadata or aspect ratio.

**Policy Locus 2: Persistence Semantics**
Unbounded options include absolute pixel storage, percentage-based anchors, or normalized coordinates. The reference demands normalized top-left origin plus normalized width/height to ensure correct remount across viewport changes.

**Policy Locus 3: Hit-Zone Semantics**
Move vs. resize discrimination requires explicit spatial policy. The reference requires disjoint proportional hit zones with specific gesture semantics: center moves, edges resize one axis, corners resize two axes.

**Policy Locus 4: Input Ownership & Click Suppression**
Ambiguity exists regarding who owns the gesture (PiP vs. parent), when a pointerdown becomes a drag vs. a click, and how to suppress unintended click events after manipulation.

**Policy Locus 5: Gesture Lifecycle**
Unclear whether to use pointerdown vs. pointerup activation, and whether to support multi-pointer or desktop-only mouse events.

## Applying Settled Directions (Non-Reopenable)

Per the benchmark's chosen directions, the following are treated as forced closure rather than debate:

- **Object Model**: Free panel (not video-shaped). Video metadata changes do not reshape panel geometry; content fitting is separate from panel geometry.
- **Persistence**: Normalized top-left origin + normalized width/height, measured against the full containing region. No edge/corner snapping on restore.
- **Hit Zones**: Disjoint proportional regions using one-sixth border bands on all sides. Center moves; edges resize one axis; corners resize two axes.
- **Input Ownership**: PiP owns the active gesture once it starts. Gesture mode is fixed at pointerdown. Unified pointer-event semantics apply wherever the PiP appears (not desktop-only wiring).
- **Click Suppression**: Click is suppressed after movement past an explicit threshold of **8px**.
- **Bounds**: Minimum size fixed at **120px by 120px**. Maximum size may expand up to containing bounds (no arbitrary ratio cap).
- **Placement**: Default position is bottom-right.

## Resolution of Expected Policy Questions

1. **Free panel or video-shaped object?** → Free panel (chosen direction).
2. **What persists across resize/remount?** → Normalized top-left origin + width/height against full container (chosen direction).
3. **Hit-zone semantics for move vs. edge vs. corner?** → One-sixth border bands; center moves, edges resize single axis, corners resize dual axis (chosen direction).
4. **How is click suppressed after drag/resize?** → 8px movement threshold triggers suppression (chosen direction).
5. **Who owns the gesture during active interaction?** → PiP owns gesture once started; unified pointer events (chosen direction).
6. **What counts as sufficient closure before implementation?** → All policy loci forced by chosen directions; remaining freedom (e.g., specific easing curves, visual feedback styling) declared irrelevant to core wiring logic.

## Recomposition Gate
All policy decisions required by the reference closed formulation are now either explicitly chosen or irrelevant to the geometry/input layer. Implementation may proceed against bounded rectangle semantics, pointer ownership rules, and normalized persistence.
