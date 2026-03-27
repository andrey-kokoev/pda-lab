### Initial Problem Framing
**Raw Input:** "difficult to know if mobile is cached or refreshed... What are coherent options to fix it? Last time of deploy?"

The user surfaces confusion about client state (cached vs. fresh) and gravitates toward "deploy time" as a potential solution. However, the underlying need is **legibility of the currently running build** and its relationship to available updates.

---

### Policy Question Surfacing

**1. Is the goal build identity, update availability, deploy time, or all three?**
- *Analysis:* Deploy time is a proxy, but insufficient. A client refreshed at 9am might still be running yesterday's build if the CDN cached it. We need actual build identity (version/hash) and a comparison mechanism.
- *Decision:* Scope includes **current build identity**, **latest available build identity**, and **staleness status** (boolean: refresh needed). Deploy timestamp is optional metadata, not the primary signal.

**2. Where in the product should this state be shown?**
- *Analysis:* The confusion likely occurs when users land on the app (wondering if they have the latest features). During active calls, cognitive load is dedicated to the conversation, not build metadata.
- *Decision:* Restrict to **landing view / dashboard**. Exclude from in-call UI to avoid diagnostic noise during primary task flow.

**3. How prominent should the UI be in steady state?**
- *Analysis:* If the build is current, this information is diagnostic noise. If stale, it should be noticeable but not blocking. Modal dialogs are too heavy for background update notifications.
- *Decision:* **Low-weight, non-modal presentation**. Steady-state (current build): subtle or collapsed. Stale-state: visible but dismissible indicator (e.g., footer text or subtle badge), never a blocking modal.

**4. Is call-view placement coherent, or should it be restricted to landing/diagnostics?**
- *Analysis:* Call UI requires minimalism. Build diagnostics here would violate context coherence—users in calls care about connection quality, not deployment artifacts.
- *Decision:* **Explicitly exclude** from call views and active session UI. Restrict to pre-engagement contexts (landing, settings, about page).

**5. What counts as enough information to know whether the client is stale?**
- *Analysis:* Requires client-side build identifier (build hash or version) and an endpoint to fetch the canonical "latest" build identifier for comparison.
- *Decision:* Staleness = `currentBuildId !== latestBuildId`. UI must surface both identities to make the gap legible.

---

### Scope Convergence
**Shaped Task:** Implement a non-modal, landing-view-only build legibility system that surfaces:
1. Current running build identity
2. Availability of newer builds
3. Clear "refresh needed" signal when stale

Avoid the trap of "just add a timestamp" or "add a banner in calls." The solution must respect product context (pre-call vs. in-call) and information hierarchy (diagnostic vs. blocking).
