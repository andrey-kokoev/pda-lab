## Objective
Make the currently running mobile client build legible to the user by surfacing build-update state on the landing view. The solution must distinguish between what is running, what is available, and whether action is required—without resorting to deploy-time timestamp as the sole signal.

## Functional Requirements
- **Current Build Identity:** Surface an identifier representing the executing client build.
- **Latest Available Identity:** Reference the build identity currently served as "latest" by the deployment pipeline.
- **Refresh Necessity State:** Clearly indicate when the current build does not match the latest available build (i.e., stale state).

## Placement Policy
- **Primary Surface:** Landing view (pre-session/diagnostic context).
- **Exclusion:** Do not implement in call-view or active-session UI to avoid diagnostic intrusion during use.

## Presentation Constraints
- **Weight:** Low-weight, ambient display (non-blocking, non-modal).
- **Coherence:** Visual treatment must align with existing product language; avoid generic "update available" banners unless consistent with app patterns.
- **Steady State:** When current build matches latest, the indication should remain subtle and non-alarming.

## Success Criteria
- User can determine if their client is stale without external reference.
- Distinguishing information (current vs. latest vs. refresh-needed) is present on landing view.
- No modal interruptions or call-view diagnostics are introduced.

## Unresolved / Abstract
- Specific visual treatment (e.g., text label, icon, color indicator) remains to be determined based on design system constraints.
- Exact format of build identity (semantic version, commit hash, build number) is abstracted as "build identity" pending versioning scheme alignment.
- Thresholds for "stale" detection logic (e.g., tolerance windows, gradual rollbacks) remain unresolved.
