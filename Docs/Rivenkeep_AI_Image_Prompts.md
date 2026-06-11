# Rivenkeep — AI Image Generation Guide
## World View Theater Mood Boards

---

## WHAT YOU NEED

- **Midjourney v6.1+** subscription ($10/month Basic plan gives ~200 images)
- Access via Discord or midjourney.com
- This document open beside you

---

## THE STRATEGY: HERO IMAGE FIRST

Midjourney works best with prompts under 400 words. Our theaters need consistency across 10 images. The solution:

1. **Phase 1:** Generate ONE perfect "hero image" (Coastal theater) by iterating until the art style, camera angle, fortress design, and ship design are exactly right.

2. **Phase 2:** Lock that hero image as a style reference (`--sref`). Generate the other 9 theaters using SHORT prompts that describe only what changes — the terrain, colors, and atmosphere. Midjourney copies the style, composition, and rendering from the hero image automatically.

3. **Phase 3:** Upscale all 10 finals. Consistency check. Touch up any outliers.

This approach gives you 10 images that look like pages from the same storybook, because they literally share the same visual DNA.

---

## PHASE 1: THE HERO IMAGE (Coastal Theater)

The Coastal theater is your hero because it's the simplest terrain (sand + water), the most readable composition, and the first thing players see. Get this one perfect. Everything else inherits from it.

### Step 1: Paste this prompt into Midjourney

```
A medieval coastal fortress on sandy bluffs overlooking a natural harbor. 
Cream limestone walls with round crenelated towers capped in slate-grey 
conical roofs. Black iron cannons protrude from tower embrasures with 
wisps of white smoke. 5 small castle keeps with crimson pennant flags 
enclosed by thick stone walls forming irregular compounds. The sandy tan 
terrain has scattered grey boulders, clusters of palm trees, and a 
cliff formation on the far left. Deep blue ocean on the right third 
of the frame with 7 enemy ships approaching in a loose crescent — 
dark organic Mystwood hulls that look grown not built, pale grey-green 
torn sails with faint bioluminescent veins, visible wake trails. 
The harbor basin is calmer turquoise. Seafoam along the waterline. 
A broken wooden dock. Seagulls wheeling above. 

2.5D isometric view from the southwest, camera 30 degrees above 
horizontal. Hand-painted gouache illustration with visible brushstrokes, 
miniature diorama aesthetic with tilt-shift depth of field. Warm golden 
hour lighting from upper-left casting long shadows to lower-right. 
Fortress fills 40 percent of the frame, centered slightly left. 
Extremely detailed — individual stone blocks, wood grain on ship hulls, 
moss in mortar joints, rust on iron, ripples in water. Premium 
tabletop board game box art quality. --ar 4:3 --style raw --v 6.1 --q 2
```

### Step 2: Evaluate the 4 results

Look for these specific things:

| Check | What to look for |
|---|---|
| **Camera angle** | Is it 2.5D isometric from above? Not flat top-down, not full 3D perspective? |
| **Fortress style** | Cream stone walls, round towers with grey roofs, visible cannons? |
| **Ship design** | Dark organic hulls, grey-green sails, 6-8 ships on the right? |
| **Composition** | Fortress left-center, water on right third, terrain fills the rest? |
| **Art style** | Hand-painted feel, not photorealistic, not 3D rendered, not anime? |
| **Lighting** | Warm golden from upper-left, long shadows lower-right? |
| **Detail level** | Can you zoom in and see individual stones, wood grain, moss? |

### Step 3: Iterate

- **If the camera angle is wrong:** Rerun. Add `looking down at a miniature diorama on a table` to reinforce the angle.
- **If the fortress looks wrong:** Use `V1-V4` (Variations) on your best result to get close alternatives without changing everything.
- **If the ships are missing or too small:** Rerun with `a fleet of 7 dark wooden sailing ships with torn grey-green sails:: 1.5` (the `:: 1.5` increases weight on that element).
- **If it's too photorealistic:** Add `matte gouache painting, no reflections, visible brushwork, illustration not photograph` before the parameters.
- **If the composition is off:** Add `the fortress compound is the largest element in the frame, positioned in the left-center`.

### Step 4: Upscale your winner

Click `U1`, `U2`, `U3`, or `U4` on your best image. Then click `Upscale (2x)` for high resolution.

### Step 5: Save the image URL

Right-click your upscaled hero image → Copy Image Address. You'll paste this URL into every subsequent prompt as `--sref [URL]`. **This is the most important step.** This URL is your style lock.

---

## PHASE 2: THE NINE DELTA PROMPTS

Each prompt below describes ONLY what changes from the Coastal hero image. The `--sref` flag tells Midjourney to copy the art style, camera angle, fortress design, ship design, lighting approach, and rendering quality from your hero image.

**For each theater:** Copy the prompt below. Replace `[HERO_URL]` with your saved Coastal hero image URL. Paste into Midjourney. Pick the best result. Upscale.

---

### 2. RIVER

```
Same fortress style and ships. Replace the coastal terrain with a 
lush green river valley. Rich green meadow ground with wildflower 
patches. Two winding blue-green rivers split the land into 3-4 
islands. The fortress compounds are built on separate islands 
connected by narrow mossy stone arch bridges. 25 deciduous trees 
along the riverbanks with overhanging branches. Morning mist rises 
from the river surface. Reeds and cattails at the water's edge. A 
watermill with a turning wheel on the largest island. The rivers 
flow left to right with visible current lines. Dragonflies above 
the water. Ducks upstream. A collapsed bridge section. 
--sref [HERO_URL] --ar 4:3 --style raw --v 6.1 --q 2
```

---

### 3. SWAMP

```
Same fortress style and ships. Replace the coastal terrain with a 
dark murky swamp. Scattered islands of solid olive-brown ground amid 
opaque dark green bog water covered in duckweed and water lilies. 
Mangrove trees with exposed roots growing from the water. Spanish 
moss hanging from dead branches in grey curtains. Wooden boardwalks 
on stilts connecting the fortress islands. Heavy overcast sky with 
thick knee-height fog over the water. Fireflies glowing in the dark 
areas. Twisted dead trees as grey skeletons. Mushroom clusters on 
rotting logs. A half-sunken boat. Oppressive claustrophobic mood. 
The water is utterly still. Luminescent mushrooms on a dead tree. 
--sref [HERO_URL] --ar 4:3 --style raw --v 6.1 --q 2
```

---

### 4. FOREST

```
Same fortress style and ships. Replace the coastal terrain with a 
dense ancient forest. 35 massive old-growth trees with 2-3 meter 
diameter trunks creating a cathedral canopy overhead. Small clearings 
where the fortress compounds are built — the clearings feel carved 
from the living forest. Dappled golden sunlight in 4-5 visible shafts 
piercing the canopy. Dark rich green forest floor carpeted with moss 
and ferns. Bracket fungi on trunks, ivy climbing bark. A forest river 
on the right edge, ink-dark under the canopy. A massive fallen tree 
bridging two clearings. Mushroom fairy rings. Dust motes in the light 
beams. A deer at the forest edge. Deep green twilight atmosphere. 
--sref [HERO_URL] --ar 4:3 --style raw --v 6.1 --q 2
```

---

### 5. MOUNTAIN

```
Same fortress style and ships. Replace the coastal terrain with a 
narrow mountain pass between sheer cliff walls. Towering grey granite 
cliffs 30-50 meters high on both sides with layered rock bands. The 
fortress is wedged into the pass using cliff walls as natural defenses. 
Sparse alpine vegetation — twisted pines from cliff cracks, juniper 
bushes, purple alpine wildflowers. Grey gravel pass floor littered 
with fallen boulders. Snow dusting the cliff tops. A mountain lake 
visible through the pass opening on the right where ships approach. 
Small waterfalls trickling down cliff faces. An eagle soaring above. 
A rope bridge spanning the pass at height. Mountain goats on a high 
ledge. Dramatic shadow from the cliff walls across the pass floor. 
--sref [HERO_URL] --ar 4:3 --style raw --v 6.1 --q 2
```

---

### 6. VOLCANIC

```
Same fortress style and ships. Replace the coastal terrain with a 
dark volcanic wasteland. Charcoal-black basalt ground split by rivers 
of glowing orange molten lava. The lava has darker cooling crust 
breaking apart to reveal bright orange beneath, casting warm orange 
glow on everything nearby. Isolated dark rock platforms between lava 
channels. Dead petrified trees as grey skeletons. Some ground cracks 
with orange heat veins — fragile unstable crust. Obsidian outcroppings 
with glassy surfaces. The sky is dark orange-red with volcanic haze 
and drifting ash particles. Embers float upward. A lava geyser in 
the background. Steam vents where lava meets rock. Hellish dangerous 
mood. Primary lighting from lava glow below, not sun above. 
--sref [HERO_URL] --ar 4:3 --style raw --v 6.1 --q 2
```

---

### 7. DESERT

```
Same fortress style and ships. Replace the coastal terrain with a 
vast open desert. Pale warm sand with gentle rolling dunes and visible 
wind-ripple patterns. Very few natural defenses — wide open and 
exposed. 2 small oases with date palm trees and blue-green pools 
standing out dramatically against pale sand. 5 wind-eroded sandstone 
formations in warm tan-orange. A bleached dead tree on a dune crest. 
Wind-blown sand streaming across dune crests in visible ribbons. 
Heat shimmer distorting the horizon. Cloth awnings shading the cannon 
positions. Sand drifted against fortress walls. An abandoned cart 
half-buried in sand. Harsh bright overhead desert sun with short 
sharp shadows. Washed-out pale blue sky. Exposed vulnerable mood. 
--sref [HERO_URL] --ar 4:3 --style raw --v 6.1 --q 2
```

---

### 8. FROZEN

```
Same fortress style and ships. Replace the coastal terrain with a 
snow-covered landscape. Pale grey-white snow ground divided by 
horizontal frozen ice channels with visible cracks and pressure 
ridges. Ice shelf platforms extending over the frozen water. 8 bare 
white birch trees and 4 snow-laden evergreen pines. Icicles hanging 
from every fortress surface. Footprints and sled tracks in the snow. 
On the right the ice breaks into floes and dark open water where 
icebreaker ships approach. Faint aurora borealis in the pale 
lavender-grey sky. Breath-vapor plumes from cannon positions. Snow 
falling lightly. A campfire with warm orange glow inside one 
courtyard. Frozen flag stiff in the wind. Cold blue-white winter 
light from a low sun with long purple shadows on the snow. 
--sref [HERO_URL] --ar 4:3 --style raw --v 6.1 --q 2
```

---

### 9. SKY

```
Same fortress style and ships. Replace the coastal terrain with 
floating stone platforms suspended high above a sea of white clouds. 
5-6 earthen platforms of varying sizes with grass and wind-bent trees 
growing on top, exposed earth and rock layers visible at the edges. 
Narrow stone bridges and rope bridges connecting the platforms — 
nothing but clouds below. Tiny waterfalls pouring off platform edges 
into mist. Deep blue sky above, thick white cumulus clouds far below 
with gaps showing blue. Wind whips banners horizontally. Hawks soar 
between platforms. Ships emerge from the cloud layer on the right. 
A telescope pointing down through a cloud gap. Wind chimes on walls. 
A broken platform fragment drifting away. Bright airy high-altitude 
light — sharp clean shadows, no atmospheric haze. Vertigo-inducing. 
--sref [HERO_URL] --ar 4:3 --style raw --v 6.1 --q 2
```

---

### 10. CRYSTAL

```
Same fortress style and ships. Replace the coastal terrain with a 
landscape of massive translucent crystal spires. Pale lavender-purple 
ground with crystalline veins and fine crystal dust sparkle. 10 huge 
hexagonal amethyst and quartz columns rising 5-15 meters, catching 
light and throwing prismatic rainbow refractions across everything. 
Visible light beams refracting THROUGH the crystals and splitting 
into rainbow colors. Luminescent blue-white moss on crystal bases. 
Crystalline tree-like mineral formations instead of real trees. 
Geode boulders cracked open showing sparkling interiors. The sky is 
deep twilight purple even in daytime — crystals filter the light. 
A crystal formation carved into a watchtower. Rainbow caustics on 
every surface. Prismatic magical atmosphere. Cool purple tone with 
warm rainbow accent spots from refracted light. 
--sref [HERO_URL] --ar 4:3 --style raw --v 6.1 --q 2
```

---

## PHASE 3: FINAL CONSISTENCY CHECK

### Step 1: Compare
Open all 10 upscaled images side by side. They should share:
- Same camera angle (2.5D isometric from southwest)
- Same fortress architecture (cream stone, round towers, slate roofs)
- Same ship design (dark organic hulls, grey-green sails)
- Same art style (hand-painted gouache, miniature diorama)
- Same level of detail (zoom in and see individual stones)

### Step 2: Fix outliers
If any theater looks different from the rest:
- Regenerate it with `--sref [HERO_URL]` again
- Add `--sw 200` (maximum style weight) to force stronger style matching
- Try `--sref [HERO_URL] [URL_OF_ANOTHER_GOOD_THEATER]` to reference two images

### Step 3: The lineup test
Shrink all 10 to thumbnail size. If you can tell they're from the same game at thumbnail size, you've succeeded. If one jumps out as looking different, that's the one to redo.

---

## PHASE 4: PRODUCTION PIPELINE (FUTURE)

Once you have your 10 locked mood board images:

1. **Scenario.gg** — Upload all 10 as training data. Train a custom LoRA model (~15 minutes). This model can then generate ANY image in your locked Rivenkeep style: individual terrain tiles, cannon sprites, ship sprites, UI backgrounds, loading screens.

2. **Asset extraction** — Use the mood boards as color palette references for the actual SpriteKit implementation. The World View shader for each theater should match the dominant colors and lighting from its mood board.

3. **App Store screenshots** — Generate wider versions with `--ar 16:9` for landscape screenshots. Use `--ar 9:16` for portrait App Store screenshots. Same prompts, just change the aspect ratio.

---

## QUICK REFERENCE: MIDJOURNEY COMMANDS

| Command | What it does |
|---|---|
| `/imagine [prompt]` | Generate 4 images from your prompt |
| `U1` `U2` `U3` `U4` | Upscale one of the 4 results |
| `V1` `V2` `V3` `V4` | Create 4 variations of one result |
| `Upscale (2x)` | Double the resolution of an upscaled image |
| `--ar 4:3` | Landscape aspect ratio (matches game) |
| `--style raw` | Less AI-polished, more artistic |
| `--v 6.1` | Use Midjourney version 6.1 |
| `--q 2` | Higher quality (uses 2x credits) |
| `--sref [URL]` | Copy the style from a reference image |
| `--sw 100` to `--sw 200` | Style reference weight (200 = maximum matching) |
| `--seed [number]` | Reproduce a specific random seed |
| `--no [thing]` | Exclude something (e.g., `--no photorealistic`) |
| `:: 1.5` | Increase weight on the phrase before it |
| `--repeat 4` | Run the same prompt 4 times (16 total images) |

---

## BUDGET ESTIMATE

| Phase | Images | Credits |
|---|---|---|
| Hero image iterations (Coastal) | ~40 generations | ~80 credits |
| 9 delta theaters × 8 variants each | ~72 generations | ~144 credits |
| Variations and reruns | ~30 generations | ~60 credits |
| Upscales (10 finals × 2x) | ~10 upscales | ~20 credits |
| **Total** | ~152 generations | ~304 credits |

Basic plan ($10/month) gives ~200 generations. You may need one month at Standard ($30/month, unlimited) for the iteration phase, then drop back to Basic.

---

*Rivenkeep GDD v5.1.5 — Riquochet Studios*
