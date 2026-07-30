# Handoff: OSGL Multi-Part Coloring System Build

**Next session goal:** Build a multi-part coloring (spray paint) system on 7 table-sized objects, merging OSGL as the rendering backend with the old Draw Handler's game logic / replication pattern.

---

## File Reference Keys

The next agent will NOT have access to the source files below by default — they live in a different project directory. Feed these to the model manually. Update the paths in this table to match wherever the files end up in the new directory.

| Key | What it is | Path (update after moving) |
|---|---|---|
| `[OSGL-INIT]` | OSGL public API surface (Window, Texture, Bitmap, color, Font, Video, Enum) | `C:\Users\Jonah\.pi\temp\roblox\OSGL System\OSGL\init.luau` |
| `[OSGL-TYPES]` | OSGL type definitions (Window, DrawableObject, DrawingContext) — shows all draw methods | `C:\Users\Jonah\.pi\temp\roblox\OSGL System\OSGL\types.luau` |
| `[OSGL-WINDOW]` | How a Window binds to a drawable Instance (ImageLabel/Decal/Texture/MeshPart) via EditableImage | `C:\Users\Jonah\.pi\temp\roblox\OSGL System\OSGL\DrawableObject\window.luau` |
| `[OSGL-BASE]` | Buffer math, ReadPixel/Resize/Tint/Resample on DrawableObject | `C:\Users\Jonah\.pi\temp\roblox\OSGL System\OSGL\DrawableObject\base.luau` |
| `[OSGL-DRAW-BUFFER]` | Example of the flattening math in action | `C:\Users\Jonah\.pi\temp\roblox\OSGL System\OSGL\draw\buffer.luau` |
| `[OSGL-DRAW-CIRCLE]` | The Circle draw primitive (confirm signature) | `C:\Users\Jonah\.pi\temp\roblox\OSGL System\OSGL\draw\circle.luau` |
| `[OSGL-DRAW-LINE]` | The Line draw primitive (confirm signature) | `C:\Users\Jonah\.pi\temp\roblox\OSGL System\OSGL\draw\line.luau` |
| `[DRAW-HANDLER]` | Old part-based spray paint system: AttemptSprayPaint, CreatePaintStroke, SetBrushSize/Color/Material, RaycastAtMouse | `C:\Users\Jonah\.pi\temp\roblox\Draw Handler System\Draw Handler.luau` |

---

## Summary of What Was Accomplished

### Research phase
Researched open-source Roblox spray paint systems, focusing on scalability for coloring 7 table-sized objects. Key findings:

- **No single "well-built" off-the-shelf spray paint system exists.** The decision that governs scalability is the **rendering backend**, not which game repo you fork.
- **Legacy backends (avoid for scale):** `Decal`/`Texture` instances (render geometry twice), `SurfaceGui` + Frame "pixels" (too many SurfaceGuis), per-voxel colored parts (Splatoon-style — severe lag at scale).
- **Modern backend (scalable path):** `EditableImage` — Roblox's runtime image buffer API. Out of beta late 2024, now Client Beta (usable in published experiences; no breaking changes expected, memory budgets may shift).
- **Open-source EditableImage libraries:** CanvasDraw (mature, single-threaded), OSGL (active dev, clean API, ~100–180 FPS at 1024² drawing), Ro2D (full engine with dirty-rect chunking, zero-allocation loop). Ro-Photoshop is NOT open source ($1,500–$3,000) — excluded.
- **Ready-made spray game:** Spray Paint Deluxe Simulator (HooferBevelops + ShuriDev, CC BY 4.0) is the closest to a real game; its backend likely predates EditableImage and won't scale.
- **Recommendation:** Fork Spray Paint Deluxe for UX/game logic; swap its rendering backend to EditableImage via OSGL or CanvasDraw. User chose **OSGL** and already has it on disk (see keys above).

### Learning phase (Explain-It session, in progress)
Taught OSGL fundamentals by contrasting with the old Draw Handler. Concepts covered:

1. ✅ **`buffer`** — a 1D strip of numbered bytes in memory (not an object). Painting = overwriting numbers, not spawning Instances.
2. ✅ **`* 4`** — each pixel needs 4 bytes (R, G, B, A). Canvas memory = `width * height * 4`.
3. ✅ **Flattening** — a 2D grid is stored as a 1D strip via formula `(y * width) + x`, then `* 4` to get the byte offset: `(y * width + x) * 4`. This is the core difference vs the old system (Part `.Position` set → exact byte write).
4. ✅ **Not spatial hashing** — flattening is one-to-one exact storage; spatial hashing is many-to-one bucketing for neighbor queries. OSGL uses flattening; Ro2D uses spatial chunking (closer to hashing).

### Open learning items (not yet taught)
- OSGL draw primitives (`Circle`, `Line`, `Rectangle`, `Polygon`, `Triangle`, `Pixel`, `Buffer`, `Clear`, `FloodFill`) — only signatures seen, not walked.
- How `Window.from(drawableObject, width, height)` binds a canvas to a real 3D Instance (ImageLabel/Decal/Texture/MeshPart) — the bridge from pixel buffer to rendered surface.
- `Window:Render()` — the flush step (buffer → EditableImage → GPU).
- How to map the old `CreatePaintStroke` (SprayPoint + Line + EndPoint part clones) onto OSGL draw calls.

---

## Current State and Open Decisions

### Confirmed
- Rendering backend: **OSGL** (`[OSGL-INIT]`).
- Game logic / UX / replication pattern: port from **old Draw Handler** (`[DRAW-HANDLER]`).
- Scale target: **7 table-sized objects**.

### Architecture mapping (old → new)

| Old Draw Handler concept | OSGL replacement | Notes |
|---|---|---|
| `SprayPoint` / `SprayLine` / `EndPoint` part clones | `window:Circle(x,y,radius,color)` + `window:Line(x1,y1,x2,y2,thickness,color)` | No Instance creation; just byte writes |
| Per-stroke `Part` in `Workspace.SprayPaint.<Player>` folder | One `Window` (buffer) per paintable surface | 7 tables = 7 windows |
| `PaintLayer` (Y-offset on parts, `/150`) | No built-in layer system in OSGL | Open decision: composite multiple buffers? Or ignore layers for v1? |
| `Material` (Neon/Gold/Glass/etc. via Part properties) | N/A in pure-pixel model | Open decision: drop materials, or emulate via blend modes / separate shaders |
| `DrawRemote:FireServer(StrokeInfo, StrokeAppearance)` stroke-delta replication | **Keep this pattern** — replicate strokes, never pixel buffers | Critical for bandwidth; confirmed best practice |
| `TweenService` size-in animation | Possible by scaling the circle radius over time before `Render()` | Cosmetic |
| `SetHideOtherSprays` (reparent thousands of parts — author warned it lags) | Trivial: skip rendering that window, or swap the bound Instance's content | Huge win |

### Open decisions to resolve in next session
1. **Per-surface canvas resolution.** Table ~4×2 studs. At 10 px/stud = 40×20; at 50 px/stud = 200×100. OSGL caps at 1024×1024. Pick a target; stress-test on lowest target device.
2. **Table geometry.** Flat parts (ImageLabel/Decal suffices) or MeshParts with curves (needs `EditableImage:DrawImageProjected`)? Determines which `[OSGL-WINDOW]` `from`/`fromAssetId`/`fromBuffer` path to use.
3. **One Window per surface vs. shared buffer.** 7 surfaces — easiest is 7 independent Windows. Confirm memory budget is fine (7 × small canvas × 4 bytes is trivial).
4. **Layers.** Old system supports up to 100 PaintLayers via Y-offset. OSGL has no native layers. Decide: drop, emulate via alpha compositing, or stack buffers.
5. **Materials.** Old system has Neon/Reflective/Gold/Glass/Fire/Sparkle. Pure pixels can't do Fire/Sparkle (those are ParticleEmitters). Decide which to keep (color/material as pixel blend) vs. drop.
6. **Input → 3D point → canvas pixel mapping.** Old `RaycastAtMouse` gives world `Position` + `Normal`. Need to convert that to `(x, y)` on the specific surface's buffer. This is the trickiest new code.
7. **Replication fidelity.** Old system uses `LastReplicatedMousePosition` + `ReplicationRequirement` tick counter for low-fidelity replicated packets. Keep this; adapt StrokeInfo to carry surface ID + canvas coords instead of world Position.

### Key OSGL API entry points to use
- `OSGL.Window.from(drawableObject, width, height)` → create a canvas bound to an Instance (`[OSGL-WINDOW]`)
- `window:Circle(x, y, radius, fill, stroke, strokeThickness)` (`[OSGL-DRAW-CIRCLE]`)
- `window:Line(x1, y1, x2, y2, thickness, color)` (`[OSGL-DRAW-LINE]`)
- `window:Render()` — flush buffer → EditableImage → visible on the bound Instance
- `window:Clear(color?)` — wipe the canvas

### Critical concept recap (for the next agent)
- **Buffer = 1D byte strip.** Painting = writing 4 bytes (RGBA) per pixel. No Instances created.
- **Flattening formula:** pixel `(x, y)` → byte offset `(y * width + x) * 4`.
- **Why it scales:** old system pays Instance-creation cost per stroke segment; OSGL pays 4 byte-writes. 7 table surfaces × thousands of strokes = trivial for OSGL, lag nightmare for parts.
- **Replicate strokes, not pixels.** Reuse the old `DrawRemote` stroke-delta pattern.

---

## Suggested Skills for Next Session

- **`grill-me`** — Stress-test the architecture mapping above before writing any code. Resolve open decisions #1–#7 one at a time. Especially useful for #6 (world→canvas coordinate mapping) and #3 (per-surface vs. shared buffer).
- **`tutorial`** — Once the design is locked, walk through building the system step-by-step: (1) spawn 7 surfaces + bind Windows, (2) raycast → canvas coords, (3) draw circle on mouse move, (4) wire replication remote, (5) port brush/color/size UX from old handler.
- **`explain-it-v2`** — Continue the OSGL teaching where this session left off (draw primitives, Window binding, Render flush) before building, if you want to finish understanding the library first.
- **`docs-mcp`** — Look up `EditableImage` and `DrawImageProjected` API references (especially if tables turn out to be MeshParts — decision #2).

---

## Commands / Quick Checks for Next Session

- Verify OSGL EditableImage API is enabled: Game Settings → Security tab → "Enable EditableImage API" (the `[OSGL-WINDOW]` `dynamicCreateEditableImage` function checks for this and returns `APINotEnabled` if off).
- Sanity-check canvas memory: `width * height * 4` bytes per surface. 7 × 200×100 = 7 × 80,000 = 560,000 bytes total — trivial.
- Confirm OSGL version: v1.6.2 (from headers in `[OSGL-INIT]`, `[OSGL-BASE]`).
