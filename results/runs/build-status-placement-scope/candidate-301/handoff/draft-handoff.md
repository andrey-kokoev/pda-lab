## Handoff: Build Status Footer (Landing View Only)

**Scope & Surface**
- **View Restriction**: Landing view only. Do not render on call view.
- **Context**: Secondary diagnostic status; non-interactive.

**Placement**
- **Position**: Simple footer area located directly beneath the bottom button controls on the landing view.
- **Hierarchy**: Subordinate to primary action buttons; serves as anchoring metadata.

**Presentation**
- **Format**: Plain text only. No badge, pill, or widget wrapper.
- **Visual Weight**: Muted/secondary text styling (platform-appropriate reduced opacity or secondary color token).
- **Content**: Build/update state description as provided by data model.

**Behavior**
- **Non-modal**: Static display only. No overlay, backdrop, dismiss action, or blocking behavior.
- **Non-interactive**: No tap/click handling.

**Unresolved / Implementation Notes**
- Specific color token (e.g., `text-secondary`, `opacity-muted`) not specified; use platform standard for muted helper text.
- Exact vertical spacing value not specified; maintain standard footer padding relative to button group.
