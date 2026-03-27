## Assessment of Raw Task State
The entry point is a conversational request to review the `telesense` repository and determine if desktop PiP (Picture-in-Picture) drag/resize behavior is wired up, then complete the wiring and fix issues. The raw task does not specify object model, coordinate systems, gesture ownership, or hit-zone geometry. It treats "drag/resize" as self-evident, hiding the interaction policy beneath implementation assumptions.

## Policy Surface Extraction
To prevent implementation of underspecified behavior, the task must be reconstituted against the reference closed formulation. The governing ambiguity level is the semantic model of the PiP interaction, not the specific code changes in `telesense`. The following mapping aligns the messy start with the normative target:

- **Object Ontology**: Raw task refers to "PiP" without specifying if it preserves video aspect ratio or acts as a free UI panel. Reference mandates **free panel**.
- **Spatial Model**: Raw task implies drag/resize within a window. Reference mandates **bounded rectangle inside containing video region** with **normalized persistence** (top-left origin + width/height).
- **Input Ownership**: Raw task implies pointer handling. Reference mandates **PiP owns input once an active gesture starts**, preventing competition with underlying controls.
- **Gesture Semantics**: Raw task lists "drag/resize" as monolithic. Reference decomposes into **center moves, edges resize one axis, corners resize two axes**.
- **Hit Zones**: Raw task implies hit testing exists. Reference mandates **disjoint and proportional** zones.

## Resolution of Expected Policy Questions

**Q1: Is PiP a free panel or a video-shaped object?**  
**Closed**: Free panel. Aspect ratio is not preserved by the interaction system; video content may letterbox inside the panel.

**Q2: What persists across resize/remount?**  
**Closed**: Normalized top-left origin (x, y) plus normalized width/height (w, h) relative to the containing video region. Absolute pixel values are reconstructed on remount.

**Q3: What hit-zone semantics define move vs edge resize vs corner resize?**  
**Closed**: 
- Center region → move (translate)
- Edge regions → resize one axis (left/right affect width; top/bottom affect height)
- Corner regions → resize two axes (diagonal resize)
- Zones must remain disjoint and proportional to PiP dimensions.

**Q4: How is click suppressed after drag/resize?**  
**Explicitly Chosen**: Stateful suppression. Once `gestureStart` is recognized (pointer down inside a hit zone), the PiP component consumes the pointer sequence. The subsequent `click` event (pointer up without significant movement) is suppressed if the gesture ever transitioned into an active drag or resize state. This prevents phantom clicks on underlying video controls after interaction.

**Q5: Who owns the gesture during active interaction?**  
**Closed**: The PiP panel owns the gesture exclusively from `gestureStart` until `gestureEnd`. No parent or sibling handlers process pointer events during this window.

**Q6: What counts as sufficient closure before implementation proceeds?**  
**Closed**: Recomposition (coding) is permitted only after remaining policy is forced (by reference), explicitly chosen (Q4), or declared irrelevant (see Open Parameters below).

## Closure Determination
The reference formulation forces the structural policy (geometry, ownership, persistence, semantic mapping). The click suppression policy (Q4) has been explicitly chosen to unblock implementation. Proportional hit-zone percentages and minimum/maximum size constraints are not grounded in the raw task or reference; they are declared **non-normative implementation parameters** rather than policy gaps. The implementer may select specific proportions and bounds without revisiting the closed policy framework.

## Composition Strategy
The handoff is structured to allow immediate comparison against the existing `telesense` codebase. It separates inviolable policy (which must be enforced exactly) from tunable parameters (which may vary by platform or preference). The wiring checklist is ordered to detect existing partial implementations and remediate them without architectural drift.
