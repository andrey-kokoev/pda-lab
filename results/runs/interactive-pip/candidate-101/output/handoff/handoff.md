# PiP Drag/Resize Wiring - Handoff

## Status

**Mostly wired up** - Core functionality works in DesktopLayout. MobileLayout has CSS conflicts that prevent proper drag/resize behavior.

## Issues Found & Fixes Required

### 1. CSS Conflict in CallMobileLayout.vue (MEDIUM)

**Problem**: The `.call-mobile__video-card--local` CSS has properties that conflict with the PiP composable's positioning:
- `aspect-ratio: 3 / 4` conflicts with composable's height calculation
- `width: min(34vw, 8.5rem)` conflicts with composable's width

**Fix**: Add PiP reset class to the CSS section of `CallMobileLayout.vue`:

```css
/* Add after line 490 (after .call-mobile__video-card--local) */
.call-mobile__video-card--local.call-mobile__video-card--pip {
  width: unset;
  aspect-ratio: unset;
}
```

Then apply the class conditionally in the template at line 229:

```vue
<div
  v-if="mobileLayout === 'picture-in-picture'"
  class="call-mobile__video-card call-mobile__video-card--local"
  :class="{ 'call-mobile__video-card--pip': true }"  <!-- Add this -->
  :style="pipFrameStyle"
  ...
>
```

Actually, since the PiP is always active when this element renders in picture-in-picture mode, we can simplify:

```vue
<div
  v-if="mobileLayout === 'picture-in-picture'"
  class="call-mobile__video-card call-mobile__video-card--local call-mobile__video-card--pip"
  :style="pipFrameStyle"
  ...
>
```

And add the CSS:
```css
.call-mobile__video-card--local.call-mobile__video-card--pip {
  width: unset;
  aspect-ratio: unset;
}
```

### 2. Optional: Add Cursor Feedback (LOW)

For better UX, expose cursor style from composable. In `usePipFrame.ts`, add:

```typescript
const cursorStyle = computed(() => {
  if (!gestureState.value) return 'default'
  const { gesture } = gestureState.value
  if (gesture.type === 'move') return 'move'
  if (gesture.type === 'corner') return `${gesture.v}-left` // e.g., 'nw-resize'
  if (gesture.type === 'edge') {
    return gesture.side === 'left' || gesture.side === 'right' 
      ? 'ew-resize' 
      : 'ns-resize'
  }
  return 'default'
})
```

Then return `cursorStyle` and use it in the layouts.

### 3. Optional: Visual Feedback During Drag (LOW)

Use the exported `isDragging` to add visual feedback:

```vue
<div
  class="call-mobile__video-card--local"
  :class="{ 'is-dragging': isDragging }"
  ...
>
```

```css
.call-mobile__video-card--local.is-dragging {
  box-shadow: 0 14px 40px rgb(0 0 0 / 0.4);
  transition: none; /* Disable transitions during drag for performance */
}
```

## Files to Modify

1. **`apps/telesense/src/client/components/CallMobileLayout.vue`**
   - Add `.call-mobile__video-card--pip` CSS class (lines ~491-494)
   - Add class to element (line 229)

## Verification Steps

1. Open app on mobile viewport
2. Enter a call
3. Switch to picture-in-picture layout
4. Try dragging the local video panel - should move smoothly
5. Try dragging from edges/corners - should resize
6. Double-click the panel - should reset to default position/size
7. Refresh page - position/size should persist

## Code Changes

### CallMobileLayout.vue (lines 227-240)

Current:
```vue
<div
  v-if="mobileLayout === 'picture-in-picture'"
  class="call-mobile__video-card call-mobile__video-card--local"
  :style="pipFrameStyle"
```

Change to:
```vue
<div
  v-if="mobileLayout === 'picture-in-picture'"
  class="call-mobile__video-card call-mobile__video-card--local call-mobile__video-card--pip"
  :style="pipFrameStyle"
```

### CallMobileLayout.vue styles (after line 490)

Add:
```css
/* When PiP is interactive, composable provides positioning */
.call-mobile__video-card--local.call-mobile__video-card--pip {
  width: unset;
  aspect-ratio: unset;
}
```

## Testing Checklist

- [ ] DesktopLayout drag/resize works correctly
- [ ] DesktopLayout double-click resets position
- [ ] DesktopLayout persistence across reloads
- [ ] MobileLayout drag/resize works correctly  
- [ ] MobileLayout double-click resets position
- [ ] MobileLayout persistence across reloads
- [ ] Touch events don't propagate to parent
- [ ] Minimum size constraint (120px) enforced
- [ ] Panel stays within container bounds
