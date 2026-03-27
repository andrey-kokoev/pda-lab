# Mobile App Cache/Refresh Visibility: Implementation Options

## Summary

To address the difficulty of knowing whether the telesense mobile app is running cached content or has refreshed with the latest deployment, here are coherent implementation options.

---

## Recommended Solution: Multi-Layer Approach

### 1. Build Metadata Display (Standard UI)

**What:** Display version and build timestamp in Settings → About

```
App Version: 2.3.1
Build: 2024-01-15 14:32 UTC
```

**Implementation:**
- Inject build timestamp during CI/CD via environment variable
- Store in app config/constants
- Display in About screen

### 2. Debug Diagnostic Overlay (Hidden)

**What:** Shake gesture or 5-tap on logo reveals detailed diagnostic info

**Shows:**
- Build timestamp
- App version + build number
- Last content refresh time (if trackable)
- Current API environment (prod/staging)
- Cache size/age (if relevant)

**Implementation:**
```javascript
// React Native example pattern
const [debugVisible, setDebugVisible] = useState(false);

// On shake gesture or secret tap sequence:
setDebugVisible(true);

// Overlay component displays:
// - BUILD_TIME (injected at build)
// - Date app was last launched/refreshed
// - API_BASE_URL
```

### 3. Update Availability Check (Optional Enhancement)

**What:** App checks version against server on startup, prompts if update available

**Flow:**
1. App launches, calls `/api/version` or checks app store
2. Compares with current build
3. Shows "Update available" banner if newer version exists
4. For OTA updates (CodePush, etc.), can force refresh

---

## Quick Implementation: Build Timestamp

**For immediate implementation**, add a build timestamp:

### Build Script (CI/CD)
```bash
# Inject build time
export BUILD_TIME=$(date -u +"%Y-%m-%d %H:%M UTC")
# Pass to build command or write to config file
```

### App Display
Add to Settings/About screen:
```
Build: ${BUILD_TIME}
```

This alone answers "is this the latest deploy?" by correlating with your deployment logs.

---

## Decision Matrix

| Approach | User Value | Dev/Debug Value | Implementation Effort |
|----------|-----------|-----------------|----------------------|
| Build timestamp in About | Low | Medium | 30 min |
| Debug overlay | None | High | 2-4 hours |
| Version check + notify | High | Low | 4-8 hours |
| All combined | High | High | 1-2 days |

---

## Suggested Next Steps

1. **Immediate (today):** Add build timestamp to About screen
2. **This sprint:** Implement shake-gesture debug overlay for support team
3. **Future:** Consider automatic update notifications if user confusion persists

---

## Questions for Clarification

- Is telesense a native app, React Native, Flutter, or PWA?
- Do you use OTA updates (CodePush, Expo Updates, etc.)?
- Who needs this visibility most: end users, support staff, or developers?
