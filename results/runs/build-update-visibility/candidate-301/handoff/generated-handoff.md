## Build Update Visibility – Implementation Handoff

### Problem Statement
Users cannot determine if their mobile client is running the latest build or a cached stale version. The goal is to make the **currently running client build legible** and communicate when updates are available, without disrupting primary workflows.

### Scope Boundaries
- **In Scope:** Landing view / dashboard visibility only; build identity comparison; subtle staleness indicators
- **Out of Scope:** In-call UI diagnostics, forced update modals, detailed deployment logs, automatic refresh triggers

### Functional Requirements

**1. Build Identity Detection**
- Expose current build identifier (git commit hash or semantic version) in client metadata
- Fetch latest available build identifier from version endpoint on app launch/foreground
- Compare: `isStale = currentBuild !== latestBuild`

**2. UI Presentation (Landing View Only)**
- **Location:** Settings page footer or dashboard header (subtle corner placement)
- **Steady State (Current):** Minimal footprint—e.g., "v2.4.1" in muted text or hidden in about section
- **Stale State:** Non-blocking indicator—e.g., "Update available: v2.4.2 (refresh to update)" with soft highlight
- **Constraint:** No modals, no banners, no call-view intrusion

**3. Information Architecture**
Display three discrete data points:
- Current build identity (what is running)
- Latest available build identity (what could be running)
- Refresh required boolean (action needed)

### Technical Considerations
- Requires `/api/client-version` endpoint returning canonical latest build ID
- Cache latest version check for 5-minute TTL to prevent excessive polling
- Build ID must be baked into bundle at build time (e.g., `process.env.BUILD_ID`)

### Validation Criteria
- [ ] User can determine current build ID without entering a call
- [ ] User can detect if their build is stale vs. latest
- [ ] No build information appears in active call UI
- [ ] Stale indicator is visible but never blocks app usage
- [ ] Works offline (shows current build, gracefully hides staleness if cannot reach version endpoint)
