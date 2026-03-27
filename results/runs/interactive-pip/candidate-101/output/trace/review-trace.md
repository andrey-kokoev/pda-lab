# PiP Drag/Resize Wiring Review - Trace

## Initial Assessment

Started by examining the repository structure and understanding the current state of changes. Found that the PiP functionality was implemented in commit `e3a55f2` ("feat: implement picture-in-picture functionality and build info display").

The commit introduced:
- `usePipFrame.ts` composable (626 lines)
- Integration into `CallMobileLayout.vue` 
- Integration into `CallDesktopLayout.vue`
- Documentation in `docs/.../20260326-001a-free-panel-pip-interaction.md`

## Files Examined

1. `/apps/telesense/src/client/composables/usePipFrame.ts` - Core PiP logic
2. `/apps/telesense/src/client/components/CallMobileLayout.vue` - Mobile layout with PiP
3. `/apps/telesense/src/client/components/CallDesktopLayout.vue` - Desktop layout with PiP
4. `/apps/telesense/src/client/components/callLayoutShared.css` - Shared styles
5. `/apps/telesense/src/client/views/CallView.vue` - Parent view component

## Wiring Analysis

### usePipFrame Composable Structure

The composable exports:
- `style: ComputedRef<CSSProperties>` - Dynamic positioning styles
- `initialized: Ref<boolean>` - Whether frame has been initialized
- `isDragging: ComputedRef<boolean>` - Whether user is currently dragging/resizing
- Event handlers: `onPointerDown`, `onPointerMove`, `onPointerUp`, `onPointerCancel`, `onLostPointerCapture`, `onClick`, `onTouchStart`, `onTouchMove`, `onTouchEnd`

### CallDesktopLayout Wiring Status: ✅ CORRECT

```vue
const videosContainerRef: Ref<HTMLElement | null> = ref(null)
const {
  style: pipFrameStyle,
  onPointerDown: onPipPointerDown,
  onPointerMove: onPipPointerMove,
  onPointerUp: onPipPointerUp,
  onPointerCancel: onPipPointerCancel,
  onLostPointerCapture: onPipLostPointerCapture,
  onClick: onPipClick,
  onTouchStart: onPipTouchStart,
  onTouchMove: onPipTouchMove,
  onTouchEnd: onPipTouchEnd,
} = usePipFrame(videosContainerRef)
```

Bound to local video element:
```vue
<div
  class="call-desktop__video-card--local"
  :class="{ 'call-desktop__video-card--pip': desktopLayout === 'focus-remote' }"
  :style="desktopLayout === 'focus-remote' ? pipFrameStyle : undefined"
  @pointerdown="desktopLayout === 'focus-remote' ? onPipPointerDown : undefined"
  @pointermove="desktopLayout === 'focus-remote' ? onPipPointerMove : undefined"
  @pointerup="desktopLayout === 'focus-remote' ? onPipPointerUp : undefined"
  @pointercancel="desktopLayout === 'focus-remote' ? onPipPointerCancel : undefined"
  @lostpointercapture="desktopLayout === 'focus-remote' ? onPipLostPointerCapture : undefined"
  @touchstart="desktopLayout === 'focus-remote' ? onPipTouchStart : undefined"
  @touchmove="desktopLayout === 'focus-remote' ? onPipTouchMove : undefined"
  @touchend="desktopLayout === 'focus-remote' ? onPipTouchEnd : undefined"
  @click="desktopLayout === 'focus-remote' ? onPipClick : () => emit('localVideoTap')"
>
```

Note: CSS properly resets default positioning when `--pip` class is active:
```css
.call-desktop__video-card--local.call-desktop__video-card--pip {
  top: unset;
  right: unset;
  width: unset;
  aspect-ratio: unset;
}
```

### CallMobileLayout Wiring Status: ⚠️ ISSUES FOUND

Same composable usage pattern, but with structural issues:

1. **CSS Conflict**: The `.call-mobile__video-card--local` class has styles that conflict with PiP:
```css
.call-mobile__video-card--local {
  position: absolute;
  right: 0.9rem;        /* CONFLICTS with composable's left positioning */
  bottom: 0.9rem;       /* CONFLICTS with composable's top positioning */
  width: min(34vw, 8.5rem);  /* CONFLICTS with composable's width */
  aspect-ratio: 3 / 4;  /* CONFLICTS with composable's height */
  ...
}
```

The composable sets `right: "unset"` and `bottom: "unset"` inline, but doesn't override `aspect-ratio`, which causes the height calculation from the composable to conflict with the aspect-ratio from CSS.

2. **Missing PiP Reset Class**: Unlike DesktopLayout, there's no `.call-mobile__video-card--pip` class to reset CSS properties when PiP mode is active.

3. **Nesting Issue**: The PiP element is nested inside the remote video card:
```vue
<div class="call-mobile__video-card--remote" @click="emit('remoteVideoTap')">
  ...
  <div v-if="mobileLayout === 'picture-in-picture'" class="call-mobile__video-card--local">
```
This causes event bubbling concerns where clicks on the PiP could trigger remote video tap.

## Issues Identified

### Issue 1: CSS Aspect-Ratio Conflict (CallMobileLayout)
**Severity**: Medium  
**Location**: `CallMobileLayout.vue` lines 480-490  
**Problem**: The CSS `aspect-ratio: 3 / 4` conflicts with the composable's height calculation. When composable sets explicit height via inline style, aspect-ratio may cause unexpected sizing.

### Issue 2: Missing PiP CSS Reset Class (CallMobileLayout)
**Severity**: Medium  
**Location**: `CallMobileLayout.vue` styles  
**Problem**: No `.call-mobile__video-card--pip` class to reset `width` and `aspect-ratio` like DesktopLayout has.

### Issue 3: Missing Cursor Feedback
**Severity**: Low  
**Location**: `usePipFrame.ts`  
**Problem**: No visual cursor feedback (move, resize handles) based on zone detection.

### Issue 4: Unused isDragging Export
**Severity**: Low  
**Location**: Both layout components  
**Problem**: `isDragging` is exported but not used for visual feedback (e.g., shadow enhancement during drag).

## Type Check Results

```
> pnpm run typecheck
> vue-tsc --noEmit
✅ No TypeScript errors found
```

## Summary

The PiP drag/resize behavior is **mostly wired up correctly**. The core composable logic is solid:
- Zone detection (center=move, corners/edges=resize) works
- Pointer capture ensures reliable gesture tracking
- Geometry persistence to localStorage is implemented
- Touch event suppression prevents parent gesture conflicts
- Double-click to reset works

**Main issue**: CallMobileLayout needs CSS fixes to properly support the composable's positioning. The aspect-ratio and width CSS properties conflict with the composable's dynamic sizing.

**Fix required**:
1. Add `.call-mobile__video-card--pip` CSS class to reset conflicting properties
2. Apply this class conditionally in the template when PiP mode is active
