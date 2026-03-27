### 1. Initial Parsing & Framing Correction
The raw task frames the problem as visibility of "last time of deploy" to resolve ambiguity between cached and refreshed mobile states. This suggests a timestamp-based solution. However, the underlying user need is **build legibility**—the ability to know what code is currently executing and whether it represents the latest available version. 

**Policy Question Surfaced (Q1):** Is the goal build identity, update availability, deploy time, or all three?
- **Resolution:** The target scope requires distinguishing three distinct states: (1) current build identity, (2) latest available build identity, and (3) whether a refresh is required to reconcile them. A deploy timestamp alone is insufficient because it does not signal whether the observed client matches the server-side latest version.

### 2. Placement & Scope Boundaries
The raw task mentions "mobile" generally without specifying surface area. The reference indicates strong user need on the landing view and potential incoherence with call-view placement.

**Policy Questions Surfaced (Q2 & Q4):** Where should this state be shown? Is call-view placement coherent?
- **Resolution:** Restrict visibility to the **landing/diagnostic view only**. Exclude from in-call UI to avoid diagnostic overbuilding during active sessions. This preserves product coherence by separating pre-session orientation from mid-session interaction.

### 3. Prominence & Interaction Model
Without explicit constraints, there is risk of overbuilding (modal dialogs, blocking banners) or underbuilding (hidden in settings).

**Policy Question Surfaced (Q3):** How prominent should the UI be in steady state?
- **Resolution:** The display must be **low-weight and non-modal**—ambient information that does not interrupt task flow. This rules out popups, blocking banners, or mandatory acknowledgments.

### 4. Stale-State Definition
**Policy Question Surfaced (Q5):** What counts as enough information to know whether the client is stale?
- **Resolution:** "Stale" is defined by a mismatch between current build identity and latest available build identity, not merely by age. The system must detect and surface this mismatch state without requiring user cross-reference against external sources.

### 5. Anti-Pattern Check
The trace validates that it did not jump to a specific widget implementation (e.g., "add a version badge in the header") before establishing the above policy framework. The solution space remains open to any low-weight, non-modal treatment that satisfies the three-state distinction and landing-view placement.
