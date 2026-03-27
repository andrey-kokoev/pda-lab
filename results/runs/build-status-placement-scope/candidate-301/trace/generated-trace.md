## Trace: Build Status Placement & Scope Analysis

**1. Role Classification (Primary Action vs. Secondary Status)**
*Policy Question: Is this UI element primary action or secondary status?*
The raw task refers to a "state section" showing build/update information. Assessment: This provides diagnostic context rather than driving the user workflow. It supports the landing environment but does not initiate calls or configure primary settings.
→ **Resolution**: Treat as secondary status information, not a primary control. Remove any styling that suggests clickability or primary action.

**2. Presentation Weight Assessment (Modal vs. Embedded)**
*Policy Question: Is the current presentation too modal or overstated for its role?*
Current implementation appears as a modal at the bottom, creating an interruptive, banner-like presence. Assessment: Modal treatment implies required attention or dismissal, which is disproportionate for background build state.
→ **Resolution**: Demote from modal/banner-like element to static embedded content. Eliminate modal chrome, backdrop, and dismiss behaviors.

**3. Surface Scope Determination (Landing vs. Call)**
*Policy Question: Should it appear only on landing view, or also on call surfaces?*
Raw task explicitly scopes this to the landing view ("We only need it on landing view. Not on call view"). Assessment: Call surfaces demand maximum clarity and minimal distraction; build status is irrelevant during active calls.
→ **Resolution**: Restrict to landing view exclusively. Explicitly omit from call view.

**4. Visual Format Decision (Badge vs. Plain Text)**
*Policy Question: Should the element be a badge/widget, or plain muted text?*
Raw task specifies "No badge. Just texts" and "muted text." Assessment: Badges imply alerts, counts, or status tags requiring attention. Build state is continuous background information.
→ **Resolution**: Use plain text only. Apply muted visual weight (secondary text styling). No badge, pill, or widget container.

**5. Information Hierarchy Placement**
*Policy Question: Where should the status live in the information hierarchy?*
Raw task requests placement "as a simple footer under the bottom buttons." Assessment: This positions the status subordinate to primary landing controls, establishing correct visual hierarchy.
→ **Resolution**: Place as footer directly beneath the bottom button group on landing view.

**Recomposition Readiness**
All policy loci are now explicit: the element is secondary status (not primary), demoted from modal to embedded, scoped to landing view only, rendered as plain muted text (not a badge), and positioned as a footer under primary controls. Placement, visual weight, and surface scope are resolved. Ready for implementation specification.
