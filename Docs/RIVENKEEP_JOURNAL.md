# Rivenkeep — Project Journal
**Last Updated:** 2026-05-31
**GDD Version:** v6.2.4 (50 sections, 9 Parts — AI-Enhanced Experience section added). SDD: v1.1.0.
**Prototype:** HTML prototype v2 (Build→Deploy→Fight loop, drag from tray, extended timers)

---

## ⭐ CURRENT STATE — START HERE (for a new session)

**To continue this project in a fresh chat, upload these two files:**
1. `Rivenkeep_GDD.html` — THE source of truth. Everything about the game is here.
2. `RIVENKEEP_JOURNAL.md` — this file (full decision history).

**Optional supporting files** (upload if working on those areas):
- `Rivenkeep_Critical_Analysis_Definitive.html` — the live issue tracker (16 open items, 62 resolved)
- `Rivenkeep_Balance_Analysis.html` — deep numbers-first balance audit vs game-balance theory + Rampart (cannon cost curve, TTK/timer math, difficulty scaling, economy). 3 P0 / 4 P1 / 5 P2 findings. Recomputed from the GDD stat tables.
- `Rivenkeep_SDD.html` — Software Design Document + build plan. Architecture (deterministic Core ⟂ SpriteKit render, GameplayKit), asset pipeline, 13 milestones M0–M12 (vertical-slice-first), v1.1.0 (versioned; Appendix A "Build Playbook" — full agentic prompt sequence M0–M12 for Devin Desktop / Claude Code). 188 check-off items, per-phase testing, 14 Windsurf/Claude prompts. Includes first-class AI layer (Apple Foundation Models): piece-name moderation+suggestions (M9), debrief/tutor/rules-help/flavor/narration/recaps (M11). Progress persists in browser localStorage.
- `Rivenkeep_Map_View_Briefs.html` — 10/10 theater mood boards + portrait UI mockups + piece-catalog detail mockup
- `Rivenkeep_AI_Image_Prompts.md` — Midjourney workflow + 10 theater hero-image prompts

**The ONLY current GDD is v6.2.4.** All earlier versions (v4.x–v6.2.2) are superseded and were deleted to avoid confusion. Ignore any reference below to an older "SOURCE OF TRUTH" filename — those are historical log entries, not the current file.

**FILENAME / VERSIONING CONVENTION (as of this handoff):** Filenames are now **stable** (`Rivenkeep_GDD.html`, `Rivenkeep_SDD.html`, etc.) — versions are tracked **internally** in each document (title/meta/footer + the SDD changelog) and externally via **git/GitHub**. Do NOT put version numbers in filenames; that breaks git history continuity. Internal version strings are still maintained (GDD v6.2.4, SDD v1.0.2).

**Project status as of this handoff:**
- GDD design phase is COMPLETE. Every gameplay system, economy, monetization stream, UI layout, challenge, leaderboard, social feature, backend architecture, and future roadmap is fully specified.
- Final integrity pass done (v6.1.0): castle-HP-vs-ships contradiction fixed, duplicate Leaderboard Structure removed, redundant Wall Stacking section consolidated, layers-vs-levels distinction clarified, Quick Answers master index added at top.
- **Fresh-eyes pass + reorganization done (v6.2.0):** reconciled 6 internal contradictions (Build timer specified two ways → unified to the Phase-Timing 25→20s/+10s-S1/Boss-22 model; "destroy all ships" victory wording → enclosure-only; "ships cannot damage castles" prose → ships hit exposed castles after a breach; obsolete walls/time star formula → canonical 3-lever; stale "ships remaining" defeat reason; interior "4 blocks = 1 ω" → 10). Closed lore numbering gap (X→XI→**XIV** → renumbered Battle Messages to XII). Fixed Cam-1 storage-slot error. Reorganized: Wind & Drift → Build (it's a Build mechanic); enemy cast (Enemies, Bosses) moved ahead of Fight mechanics; one-section "Part VI — Castles" dissolved into Combat; Loss & Replay → Progression; renumbered to **9 Parts**; nav rewritten to match. Folded in 7 Critical-Analysis items (BAL-1/2, FLOW-1/2, INFRA-3, FUT-1, POL-1/2/3).
- 16 open items remain, ALL tracked in the Definitive Critical Analysis: 2 balance (Lightning, Chain Shot — playtest only), 2 flow (early-game Deploy/Fight pacing), 3 policy (privacy, notifications, analytics — pre-submission), 2 future (spectator, endless mode), 10 infrastructure (content production + engineering).
- NO outstanding tasks from the design phase. The next phase is prototype development + content production (the INFRA items).

**Key facts a new session must not re-litigate** (these are LOCKED decisions):
- Victory = enclose required castles only. Ships NOT required (except Boss Finale).
- Stars = 3-lever average (Ships / Cannon Health / Area Enclosed), rounded up. ★★★! = 2 levers maxed + 1 at ★★★.
- Battle Score = raw sum of 3 lever % (max 400). Powers leaderboards + Weekend Race.
- 4 difficulty LEVELS (Recruit/Commander/Veteran/Legend) × 190 battles = 760 experiences. Separate from the 5 difficulty LAYERS (A–E) baked into campaigns.
- Stonwryt economy is ×10 scale, 25 purchasable items, pause-panel UI (time stops), earned-only (never purchasable with real money).
- Cannons carry between battles within a campaign (≥100%), cap 200% (perfect accuracy + double firepower), move bonus +5%→0% by distance.
- Backend = CloudKit + GameKit + Firebase (Option A, chosen by Jack). ~500 lines server-side TypeScript.
- Studio name "Riquochet Studios" is an INTENTIONAL spelling (not a typo of Ricochet).

---

## PROJECT STATUS

### Documents Produced
- `Rivenkeep_GDD_v5_1_5.html` — Complete game design document (SOURCE OF TRUTH)
- `Rivenkeep_GDD_v4_8.html` — Previous version (archived, content reference only)
- `Rivenkeep_Critical_Analysis.html` — Final Inspection v3: 5 lenses (Virality, Monetization, Flow, Unanswered, Professional) — 40 items
- `Rivenkeep_Prototype.html` — Playable HTML prototype of core loop
- `Rivenkeep_Setup_Guide.md` — Xcode + Claude Code + project setup (from zero)
- `RIVENKEEP_JOURNAL.md` — This file

### GDD Completeness (v5.0.2)
- ✅ 46 sections across 10 parts (Foundations → Reference)
- ✅ v5 restructure complete: single-source-of-truth per concept, cross-references via links
- ✅ Full editorial pass: 30+ structural HTML fixes, section nesting balanced
- ✅ Visual Language & Color System section (restored from v4.8, was missing)
- ✅ 190-battle spreadsheet with Deploy timer column (JS-generated, 198 rows verified)
- ✅ 198-piece catalog with 51 nicknames (JS-generated)
- ✅ 330 campaign quotes from 20 soldiers (JS-generated)
- ✅ 77-term inline glossary with tap-to-expand definitions + Reference section with ⤴ links
- ✅ 10 cannon types with absolute values (eDPS, TTK)
- ✅ 12 ships, 7 troops with absolute values
- ✅ 10 bosses with HP, damage, stealth timing
- ✅ 4 base units (Wall HP=100, Cannon Dmg=25, Ship Dmg=15, Reload=4 ticks)
- ✅ Complete phase timing balance (Build 35→22s, Deploy 20→30s, Fight 25→90s)
- ✅ Sortie 1 bonus (+15s, rolls over normally)
- ✅ Session length verification math for all campaign ranges
- ✅ Full audio/haptic tables (40+ entries each)
- ✅ Tutorial design (live playable first-launch)
- ✅ Save/Pause system (X button, auto-save)
- ✅ Monetization ($4.99 ad-free, team colors, piece naming)
- ✅ Daily challenges (7 types, 14-day streaks)
- ✅ Fight targeting (auto-fire + directed + 2-finger + tap-to-prioritize)
- ✅ Stonwryt currency (9 spending options, earned only, never purchasable)
- ✅ 30+ Challenges across 5 categories
- ✅ Weekend Race (48hr Friday-Sunday, 50 players, Stonwryt pool)
- ✅ Last Garrison (castle <5% HP desperation state)
- ✅ 10 theaters in progressive order with detail cards
- ✅ 6 fragile grid types (no cannons on any fragile grid)
- ✅ DMZ advance mechanic (replaces "flooding")
- ✅ Team color sprites + enclosed/non-enclosed visual distinction
- ✅ Cannon HP a11y (dot marker at 100%)
- ✅ Enemy red outline, unknown yellow outline
- ✅ Interior blocks → Stonwryts (4 blocks = 10 Stonwryts, ×10 scale)
- ✅ Wind & Drift system (4 strengths, 8 compass directions, complete table)
- ✅ Castle Degradation 3-strike rule in Part VI
- ✅ Unlock Timeline with cannon star milestones
- ✅ "What Makes This Game Special" — 12 numbered prose paragraphs

### Architecture Decisions
- **Platform:** iOS (iPhone), Swift + SpriteKit
- **IDE:** IntelliJ/Windsurf for code, Xcode for build/deploy
- **CLI:** Claude Code for direct filesystem access
- **Grid:** 48×64 (3,072 grids per map), orthogonal (not isometric)
- **Castle system:** 10 castles numbered #1-#10, progression 1/4→9/10→4/4
- **Map layers:** Base (10) + Environmental (190) + Enemy (190) → collapsed into 190 battlefield files
- **Theater order:** Coastal→River→Swamp→Forest→Mountain→Volcanic→Desert→Frozen→Sky→Crystal
- **Terminology:** "Wall Rack" (not selection tray), "grid" (not tile/pixel), "environmental overlay" (not terrain overlay), "fragile grid" (group term for ice/crust/crag/bog/fract)
- **Core/ has zero SpriteKit imports** — all game logic is pure Swift, testable without UI
- **Version convention:** Major.Minor.Patch (significant=+1.0, moderate=+0.1, small=+0.0.1)

### Key Design Rules (Quick Reference)
- Player NEVER encloses all castles (except Boss 4/4)
- Deterministic battles — fixed spawn order, fixed troops, this is a puzzle game
- Walls ≥25% HP fully repaired to 100% each Build. Cannon rebuild +50% (cap 100%). Two lock-in windows: Pre-Build (rebuild +50%, enclosure +8%/+6%/+4%) and Post-Deploy (+6%/+4%/+1%, unmoved +2%).
- Time rollover: Build→Deploy→Fight→50% to next Build. Final Fight→Last Stand = 100%. No cross-battle.
- Piece algorithm: no duplicates in Wall Rack, guaranteed 1 per 50, anti-streak
- Wall pieces: ALL blocks must be on valid ground to soft-lock (whole piece fails). Spackle: partial placement OK.
- Wall pieces can replace trees (clear-cut, permanent). Only troop-damaged trees grow back.
- Nothing can be placed on rocks. Ever.
- Castles appear gradually: 4 visible (Cam 1-6) → 6 (Cam 7-16) → 8 (Cam 17-26) → 10 (Cam 27+). Boss = 4/4.
- Enclosure: exterior flood fill from map edges + DMZ. Walls/cliffs/spackle/castle = BARRIER. 4-way flood. Cliff↔cliff diagonal closes gap (only exception). Map edges do NOT enclose. Castle enclosed if ≥1 of 16 surrounding grids is enclosed.
- Castles and cliffs count as walls for enclosure AND isolation cleanup checks
- Castle HP recovery: 1/3 per enclosed sortie, applied during Build Step 1 wipe
- Spawn points are in Layer 3 (enemy overlay), NOT the base map. Sortie count also hand-tuned in enemy overlay.
- Ship destination grids: clusters of 3+ grids per ship (deterministic positioning)
- Friendly fire OFF until Campaign 11
- Area denial lifecycle: fire (1st Build) → holes (2nd Build) → cleared (3rd Build). Each step advances during Step 1 wipe.
- Spackle: 2×2 (Cam 1-16), 3×3 (Cam 17+), no rotation. CAN be placed on fragile grids.
- Build: 25s→20s (+10s S1 bonus → Cam1 S1=35s, Boss 22s). Deploy: 12s→15s. Fight: 25s→90s. Ready button in all three. (v6.2.0 unified the Build timer; old "35s→22s/+15s" was a stale second spec.)
- Stonwryts: earned only, NEVER purchasable. 9 spending options. Purchase popup with +/- adjuster, timer never stops.
- Last Garrison: castle <5% HP → +100% fire rate, -20% accuracy, 5% destruction cascade. Does not stack.
- Fragile grids: NO CANNONS on any of 6 types (ice, crust, crag, bog, fissure, fract). Walls take damage. Spackle OK.
- Troops: weighted A* pathfinding. open=1, damaged tree=2, cliff=2, healthy tree=4, wall=hits_to_destroy+1, rocks/DMZ/AoD=∞. Re-evaluate every tick (adaptive batching for 9+ troops). Always a path through walls.
- Fog of war: ships only. Troops always visible (on our land). Friendly zone always visible.
- Proximity fire rate: +15% at close range (linear falloff). Ships want to push closer.
- DMZ advance: 1 grid/sortie in all theaters except Coastal, River, Swamp. Walls on stable ground hold indefinitely; fragile = 2 sorties. Cliffs stop advance.
- Wind: one direction per battle. Desert and Frozen get +1 base drift.
- Mountain: troop map (max cliffs, heavy troop compositions, no elevation mechanic)
- Crystal: same elements as all maps (pillars=rocks, growths=trees, ridges=cliffs) + shot bounce
- Theaters are locations, not different mechanics. Same terrain elements, different art.
- Interior isolated blocks → Stonwryts (4 blocks = 10 Stonwryts, ×10 scale, rounded down)
- Weekend Race: Friday 6PM→Sunday 6PM, 50 players, opt-in, Stonwryt pool prizes
- Camera: pan/zoom available in ALL phases (Build, Deploy, Fight). Fight: quick drag = pan, 200ms hold = target.
- iCloud sync: automatic background sync. Conflict = more stars wins. Core campaign fully offline.
- Settings: Restore Purchases (syncs iCloud + App Store), Restart Game (double confirm, purchases kept)
- Wind drift: applies on SOFT lock (every pick-up/drop re-drifts). Spackle exempt from drift (emergency exception).
- Spackle = wall block for isolation cleanup (saves adjacent walls). Only differences: no cannon bonus, removed after Fight.
- No cannon type limit: player can fill all slots with same type. Variety from encounter design.
- Max cannons: min(start + sorties + floor(totalShips/5), 12). Based on campaign, sortie count, AND fleet size.
- Cannon recoil: 3 HP per cannon shot to all adjacent troops.
- Ship target fallback: primary destroyed → secondary → tertiary. All structures gone → stand down.
- Ship locations visible during Build/Deploy as solid red grid blocks (generic, player remembers types).
- Spawn points marked yellow-orange with cross-hatching after first use. Edge-of-map only. Stealth never marked.
- Theater order in campaigns: Coastal first, in order. Later theaters skipped in early campaigns. All 10 by Cam 32.
- Challenge a Friend: deep link on victory popup (battle #, stars, commander name). Opens App Store if no game.
- Replay export: 9:16 vertical (1080×1920 MP4) with side panels for branding. HUD elements move to panels.
- Defeat popup: Replay + Challenge + near-miss metrics. Retry button (primary). Shareable defeats.
- ★★★! frequency: 1 per 15-20 battles for skilled player. Hard-earned surprise. At least one by Cam 15.
- Tutorial: video-guided demo. Tap to interrupt, scrub bar, resume button, looping. All 10 cannons available. Safety nets auto-complete. Endless Fight. Win/loss video. "Ready for your first battle?" popup.
- Civilization Skin Bundles: $2.99-$3.99. Walls + cannons + castles themed together. Highest-value cosmetic.
- Commander's Pack: $4.99 one-time at Campaign 3. Ad-Free + Color + Exclusive Avatar. First-purchase conversion.
- Commander's Circle: $9.99/year supporter tier. Ad-Free + monthly exclusives + gold badge. No gameplay advantage.
- Streak badges: Silver (28d), Gold (60d), Platinum (90d), Diamond (180d), Obsidian (365d). Permanent avatar badge + frame + Stonwryt bonus.
- Ads: 1 interstitial per battle (before gameplay). Never between sorties. Never after defeat.
- Rewarded video: +10s Last Stand after defeat, double Stonwryt after daily, 5 Stonwryts per video (2/day max from home screen).
- Piece naming: 3 tiers (30d/90d/1yr). A-B costs 1.5×, G-H costs 0.6×. "My Pieces" tab. A1 is Golden Piece (permanent, locked).
- **Board: 64×48 grids (landscape). Both portrait and landscape orientations supported.**
- **Fight phase: 2.5D isometric perspective. Build/Deploy stay 2D top-down. 3-2-1-FIGHT is animated camera tilt.**
- 3-strike defeat: 3 losses to same battle = drop back 1 level. Retry button is primary. Strikes visible.
- Cannon type deployment limits: max per type = floor(totalStars/unlock_threshold), cap 5. ∞ in Cam 1-6. Standard always ∞.
- Star criteria: 3-lever average (Ships Destroyed / Cannon Health / Area Enclosed), rounded up; ★★★! = 2 levers at the hidden ! threshold + 1 at ★★★; shown on battle page + Build panel, server-tunable. (v6.2.0 removed the obsolete "50% walls+time / 75% / 90%+no-degradation" formula that still lingered in Victory Celebration.)
- Home screen: 4 tabs (Home, Campaign, Daily, Store). Campaign scrolls Angry Birds-style.
- Leaderboards: geographic regions (20-50), campaign-based matching, friends with normalized cross-level scoring.
- Daily challenges: unlock after Cam 1. 3/day (Build, Deploy+Fight, Combined). 28+ unique. Replay unlimited, reward from last play. Ad to lock in score.
- Studio: Riquochet Studios. Art style: 2.5D isometric miniature diorama (tabletop game feel). AI-generated with human curation.
- NARRATIVE: Tagline = "In memory of our home, our families, our God, our freedoms, our peace." Chiasmus.
- NARRATIVE: Tagline = "In memory of our home, our families, our God, our freedoms, our peace." Chiasmus.
- NARRATIVE: Captain of the Title of Liberty → Commander. He/his. Humble soldier, leader of True Men. Anointed by Stonewrights.
- NARRATIVE: Mystaeri (NOT Mystborn — trademarked). Flat forested land. Live 1.5x longer. Thunder-tongue. Mystwood speaks quiet truths.
- NARRATIVE: Mystwood is intelligent — translates between dialects, remembers, navigates. Mystholders anchor the fog barrier.
- NARRATIVE: Ancestors accidentally destroyed fog barrier through unknowing Mystholder harvesting 4 generations ago. Pride cycle.
- NARRATIVE: Ael'thar — Mystaeri emissary offered blood fellowship. Banished nobleman's son killed him. Henchmen did the deed. Mystwood ship carried bones home in grief-fire.
- NARRATIVE: Fleet GROWN from living Mystwood over decades. Orders in Mystwood. Mystaeri nearly extinct by arrival. Can't be recalled.
- NARRATIVE: Stonewrights = keepers of religion, scholars of stone, pacifists. Elderess Rhyna leads. Aetherbond unions (12x coordination, die together). Theoliths teach children.
- NARRATIVE: Stonwryt = vow in living rock (sacred) AND currency (gold + black stone, governed by Stonewrights).
- NARRATIVE: Rivenkeep = ancient myth, long abandoned. Shadow of itself. People fracture → Captain's Title of Liberty → Rhyna wakes Stonewrights.
- NARRATIVE: "Rise, Stonewrights! Lay stone upon stone. Stand every wall to the very end." Husband: "Rise! Rise! Rise!"
- NARRATIVE: Rite of the Cornerstone recovered by Rhyna in Rivenkeep's vaults. Contains secrets of building for battle.
- NARRATIVE: Rivenmen = new identity. Shorelands = the old name for a more peaceful time.
- NARRATIVE: Battle messages — 5-8 unique per battlefield, random selection each play, same flavor per battlefield.
- 5 DIFFICULTY LEVELS: Recruit, Soldier, Commander (baseline), Veteran, Legend. 190×5=950 experiences. Separate leaderboards.
- Assist Mode: silently activates after 5 consecutive defeats. +5s Build, +1 spackle. No ★★★!. No UI indicator.
- Fight transition: dramatic crossfade (map on table → window → dark sky → 2.5D battlefield). 2.5-3.0 sec. NOT a camera tilt.
- All phase timers are server-side configurable. Current formulas = initial estimates. Rampart arcade timing as baseline.
- Cannon type limits: max per type = floor(totalStars/unlock_threshold), cap 5. Standard = ∞. Cam 1-6 = all ∞.
- 3-strike drop-back: same campaign only. Battle 1 = no drop-back.
- Piece naming pricing: all IAP conform to Apple App Store price tiers.
- Progressive onboarding: brief 3-5 sec video for each new mechanic. Tap to dismiss. Once per mechanic.

---

## CONVERSATION THREADS

### Thread 1: GDD Refinement
**Purpose:** Continue adding design details, edge cases, and polish
**Start with:** Upload RIVENKEEP_JOURNAL.md + Rivenkeep_GDD_v5_1_5.html. State what to refine.
**Current GDD file:** Rivenkeep_GDD_v5_1_5.html

### Thread 2: UI/UX Design
**Purpose:** Screen mockups, layout decisions, visual flow
**Start with:** Upload journal. "I want to design [specific screen]."

### Thread 3: Art/Entity Design
**Purpose:** Sprite design, color palettes, visual identity
**Start with:** Upload journal. "I need sprites/visuals for [specific entities]."

### Thread 4: Analysis & Future
**Purpose:** Deep analysis, War II/III ideas, game theory, competitive analysis
**Start with:** Upload journal + GDD. "Deep dive on [topic]."

### Thread 5: Game Coding (Evenings/Weekends)
**Purpose:** Swift code generation, debugging, architecture
**Start with:** Upload journal + relevant code files. "We're working on [specific module]."

---

## CODING PROGRESS TRACKER

### Phase 1 — Core Logic (Pure Swift, No UI)
- [ ] Grid.swift + tests
- [ ] Piece.swift (198 pieces) + tests
- [ ] PieceAlgorithm.swift (Wall Rack draw, anti-streak) + tests
- [ ] Enclosure.swift (flood-fill, cliff/castle rules) + tests
- [ ] Cannon.swift (10 types, stats, HP/bonus pipeline) + tests
- [ ] Castle.swift (HP, degradation, healing, ruins) + tests
- [ ] Wall.swift (HP, isolation cleanup, fragile grid damage) + tests
- [ ] Enemy.swift (ships, troops, AI, destination grids) + tests
- [ ] Boss.swift (10 bosses, stealth, mechanics) + tests
- [ ] Battle.swift (sortie state machine, phases) + tests
- [ ] TimeRollover.swift + tests
- [ ] StarCriteria.swift (scoring) + tests
- [ ] Campaign.swift (32 campaigns, layer configs) + tests
- [ ] BattleData.swift (190 battle parameters) + tests
- [ ] FragileGrid.swift (5 types, damage rules) + tests
- [ ] Flooding.swift (advance, wall hold, DMZ shift) + tests
- [ ] Stonwryt.swift (9 spending options, earning, balance) + tests

### Phase 2 — Rendering (SpriteKit)
- [ ] GridNode.swift (48×64 board rendering, zoom/pan)
- [ ] PieceNode.swift (drag, ghost, snap, soft-lock)
- [ ] WallRackNode.swift (bottom tray)
- [ ] CannonNode.swift (sprite, HP bar with dot marker, bonus animation)
- [ ] CastleNode.swift (sprite, halo, enclosed/non-enclosed visual)
- [ ] ShipNode.swift (enemy rendering, red outline, HP bars)
- [ ] ProjectileNode.swift (ballistic arcs, ground bounce for Crystal)
- [ ] BattleScene.swift (phase loop, transitions)
- [ ] Phase bar + timer UI

### Phase 3 — Content + Polish
- [ ] Map data pipeline (10 base maps as JSON)
- [ ] Environmental overlays (190 JSON, incl fragile grids + flooding)
- [ ] Enemy overlays (190 JSON, incl ship destinations)
- [ ] Battlefield compiler (merge 3 layers → single file)
- [ ] Audio manager + haptic patterns
- [ ] Home screen / campaign list
- [ ] Victory celebration
- [ ] Tutorial (live playable)
- [ ] Save/Resume system
- [ ] Settings menu
- [ ] Daily challenges
- [ ] Stonwryt UI (purchase popup, balance display)
- [ ] Challenge tracking + UI
- [ ] Weekend Race matchmaking + UI

### Phase 4 — Ship
- [ ] Balance playtesting (Cam 1-10)
- [ ] Balance playtesting (Cam 11-20)
- [ ] Balance playtesting (Cam 21-32 + Boss)
- [ ] TestFlight
- [ ] App Store submission

---

## DECISIONS LOG
| Date | Decision | Rationale |
|------|----------|-----------|
| 2026-04-04 | Swift + SpriteKit (not Unity) | Native haptics, no licensing, Java→Swift transition |
| 2026-04-04 | IntelliJ/Windsurf for editing | Jack's preferred IDE for 12 years |
| 2026-04-04 | Core/ pure Swift, no SpriteKit | Testable without UI, clean architecture |
| 2026-04-04 | Multi-conversation workflow | GDD, UI, Art, Analysis, Coding as separate threads |
| 2026-04-05 | Renamed to Rivenkeep | "Riven" (torn) + "Keep" (fortress). Unique, trademarkable. |
| 2026-04-06 | Build 35→22s, Deploy 10→20s, Fight 25→90s | Old timers too generous early. Deploy scales with cannon count. Fight timer is safety net. |
| 2026-04-06 | Sortie 1 gets +15s bonus (rolls over) | Empty map needs construction time. Rolls over like all Build surplus. |
| 2026-04-06 | Version convention: major.minor.patch | Significant=+1.0, moderate=+0.1, small=+0.0.1 |
| 2026-04-06 | Complete unit balance pass | 4 base units, absolute values, eDPS/TTK for all entities |
| 2026-04-06 | Stonwryt currency (9 options) | Earned only. Nudge not win. Purchase popup, timer never stops. |
| 2026-04-06 | Challenges (30+) + Weekend Race | Meta-achievements + 48hr competition. Both earn Stonwryts. |
| 2026-04-06 | Last Garrison | Castle <5% HP → +100% fire rate, -20% acc, 10% cascade. |
| 2026-04-06 | Inline glossary (62 terms) | Tap dotted-underline terms to expand. Reference section at end. |
| 2026-04-06 | Theater order: Co→Ri→Sw→Fo→Mt→Vo→De→Fr→Sk→Cr | Progressive difficulty. Debuts every 2 campaigns. |
| 2026-04-06 | Fragile grids: no cannons, wall damage | 5 types (ice/crust/crag/bog/fract). Simplified from complex per-theater cannon effects. |
| 2026-04-06 | Flooding: Swamp/Volcanic/Sky | 1 grid/sortie advance. Walls hold 2 sorties. DMZ moves. |
| 2026-04-06 | Crystal: ground bounce (not ricochet) | Missed shots bounce 3 grids along floor. Fract grids = vibration damage only. |
| 2026-04-06 | Interior blocks → Stonwryts | 4 blocks = 1 Stonwryt (was: earned time for Last Stand). |
| 2026-04-06 | Trees: clear-cut permanent | Wall-replaced trees gone forever. Only troop-damaged trees reset. |
| 2026-04-06 | Orthogonal grid (not isometric) | Touch precision, rotation clarity, drag UX on mobile. Art creates depth. |
| 2026-04-06 | Castles/cliffs count as walls for isolation | Walls touching castles/cliffs not cleaned up. Simplifies enclosure building. |
| 2026-04-06 | 190 battles (180+10 boss) | Fixed from 197. Trimmed overrepresented theaters in mid/late campaigns. |
| 2026-04-06 | 6 fragile grids (added Fissure for Desert) | Ice, Crust, Crag, Bog, Fissure, Fract. No cannons on any. |
| 2026-04-06 | Swamp: no flooding, just bog grids | Single mechanic per early theater. Flooding reserved for Volcanic/Frozen/Sky. |
| 2026-04-06 | Frozen: added flooding + blizzard fog | Ice advancing from edges. Periodic blizzard = fog of war. |
| 2026-04-06 | Crystal: ALL shots bounce (cannon+ship) | 100%/50%/25%. Boss 4 bounces 100%/60%/35%/20%. Each bounce clears 3x3 fog. |
| 2026-04-06 | Fog of war: Forest, Mountain, Desert, Frozen, Crystal | Each with unique trigger (trees, clouds, sandstorm, blizzard, darkness). |
| 2026-04-06 | Zone ratio 60:40 → 40:60 | Coastal generous, later theaters compress friendly zone. |
| 2026-04-06 | Trees: cannon/ship can damage empty trees | ¼ speed in healthy, ½ speed in damaged. Clear-cut permanent. |
| 2026-04-06 | Cliffs: unbuildable like rocks | Still count as walls for enclosure/isolation. |
| 2026-04-06 | 2.5D Fight transition | Flat Build/Deploy → animated 2.5D Fight. Recommended v2 polish. |
| 2026-04-06 | Walls hold back DMZ on flooding edge | DMZ doesn't advance past walls until they crumble (sortie 3). |
| 2026-04-06 | Troops seek easiest path, climb cliffs ½ speed | Cliffs are barriers but not walls. Troops exposed while climbing. |
| 2026-04-06 | Flooding from DMZ, Build Step 1, 3×3 wall protection | Flood = enemy gaining ground. Walls hold DMZ for 2 sorties. |
| 2026-04-06 | Mountain = troop map (no elevation) | Removed elevation mechanic. Max cliffs, troops flood over from all angles. |
| 2026-04-06 | Crystal = same elements as all maps | Pillars=rocks, Growths=trees, Ridges=cliffs. Theaters are locations not mechanics. |
| 2026-04-06 | Fog of war: ships only, troops always visible | Troops on friendly land = always seen. Fog only hides enemy ships. |
| 2026-04-06 | Proximity fire rate +15% at close range | Incentivizes ships to push closer. Creates natural risk/reward positioning. |
| 2026-04-06 | Wind simplified to one direction | Desert+Frozen get +1 base drift. Single compass direction per battle. |
| 2026-04-06 | 6 fragile grids (added Fissure for Desert) | Desert sand erosion 2 HP/sortie. Same no-cannon rule as all fragile grids. |
| 2026-04-06 | Swamp confirmed no flooding | Single mechanic (bog grids). Flooding reserved for Volcanic/Frozen/Sky. |
| 2026-04-06 | Swamp: NO FLOODING (3rd fix, final) | Bog grids only. Stagnant water. |
| 2026-04-06 | Desert Canyon never calm | +1 base drift always active, even without Layer D. |
| 2026-04-06 | Frozen: ice drift removed | No ice-specific wall drift. Wind drift (+1 base) covers all drift. Ice grids = 3 HP cold damage. |
| 2026-04-06 | Crystal: not fragmented, has flooding | Cavern collapse = flooding mechanic. Final theater gets everything. |
| 2026-04-06 | Flooding theaters: Volcanic, Frozen, Sky, Crystal | Four theaters with advancing flood from DMZ line. |
| 2026-04-06 | Rotation algorithm: rotate within 4×4 ghost | (row,col)→(col,−row), normalize, center via floor(). Ghost stays put. Max ½ grid shift. |
| 2026-04-06 | Build tray ≠ Deploy tray | Build: trash+spackle+rack+storage. Deploy: cannon trash + full-width carousel. Same tray size. |
| 2026-04-06 | Cannon trash bin | Previous-sortie cannons can be trashed; slot reopens next sortie. Tap to view/recover. Invalid cannons auto-trashed. |
| 2026-04-06 | Cannon carousel full-width with arrows | Scrollable both directions. All unlocked types visible. |
| 2026-04-06 | Off-viewport frame brightness animation | Frame fades in progressively as piece scrolls out. Selectable at any brightness. |
| 2026-04-06 | Storage slot swapping | Drag stored piece over another = swap positions. Player sorting. |
| 2026-04-06 | Ghost shows 4×4 grid lines, faded on soft-lock | Light grid helps visualize rotation. Faded ghost = "still adjustable." |
| 2026-04-07 | Walls ≥25% HP fully repaired to 100% each Build | Stonwryts repair everything. HP bars disappear. Clean board each sortie. |
| 2026-04-07 | Wall Rack refresh prevents hoarding | Use it, store it, or lose it. Fresh draw every Build phase. |
| 2026-04-07 | Troops move diagonally (1.414× time) | √2 cost. Enables pathing around single-grid obstructions. |
| 2026-04-07 | ω symbol on interior blocks (Stonwryt icon) | Pulsing blue + ω. Red + X for exterior removed blocks. Consistent visual language. |
| 2026-04-07 | Cannon bonuses applied after Deploy, not Build | Player can move cannons during Deploy, so enclosure not final until Deploy ends. |
| 2026-04-07 | Cannon enclosure preview during Build (projected) | Shows projected HP gain in real-time as player builds. Not applied until post-Deploy. |
| 2026-04-07 | Spackle has same ghost frame + anchor as walls | Consistent drag language. Cannons also use centered frame. |
| 2026-04-07 | Red + X = universal "can't go there" | Walls, cannons, spackle all use red blocks with X for invalid placement. |
| 2026-04-07 | Gray tiled floor = mirror of black tiled floor | a11y: pattern alone distinguishes spackle-enclosed from permanent enclosed. |
| 2026-04-07 | Spackle does not roll over between battles | Each battle starts with full allotment. Unused spackle lost. |
| 2026-04-07 | Deploy timer 20s→30s (was 10s→20s) | Human factors: 5-8s board recognition + 3-6s per cannon. 20s min ensures fairness. |
| 2026-04-07 | Old cannons CAN change type via trash | Trash old → slot consumed this sortie → place new type next sortie. Misses one Fight. |
| 2026-04-07 | Selection frame (not halo), swap icon for a11y | Brightness distinguishes new/old. Swap icon on first-sortie frames provides shape-based a11y. |
| 2026-04-07 | DMZ advances every sortie (except Coastal/River/Swamp) | Universal mechanic. Replaces "flooding." Walls on stable ground hold indefinitely; fragile ground = 2 sorties. Cliffs also stop advance. |
| 2026-04-07 | Siege Tower → Siege Ship | Global rename. |
| 2026-04-07 | Ship stacking on same grid | Multiple ships can occupy one grid. One cannon shot hits all. Hides numbers. |
| 2026-04-07 | Shot trajectory = arrival speed, not reach | Cannons never fall short. Powerful cannons = lower arc = faster arrival. |
| 2026-04-07 | 2 tap-to-prioritize targets | First tap = target 1, second tap = target 2, third tap = removes first. Crosshair fades 5→0 sec. |
| 2026-04-07 | Ships fire OVER troops | No friendly-fire exploitation from troop positioning. |
| 2026-04-07 | Transport docks, troops exit any side | Troops fan out from all sides of 1×2 dock. Transport frozen unless DMZ shifts. |
| 2026-04-07 | Bombers: straight line, ±1 Crazy Ivan, random castle | Turn around if target castle destroyed mid-flight. Carrier fire rate = bomber speed. |
| 2026-04-07 | Battering Ram targets diagonal walls | Creates isolation-cleanup vulnerabilities. Prefers multi-layer sections. |
| 2026-04-07 | Multiple hospital ships, 0% cannot be resurrected | All hospital ships distribute healing evenly. Dead ships stay dead. |
| 2026-04-07 | Spawn points in Enemy Overlay, not base map | Later battlefields can spawn closer to DMZ for stealth. |
| 2026-04-07 | DMZ = dashed black line (not red) | Red is reserved for invalid placement indicators. |
| 2026-04-07 | DMZ advances after Deploy phase (not Build) | Cannons and castles also permanently hold DMZ back. |
| 2026-04-07 | Fragile grids never in enemy territory | Fragile grids are always friendly zone. DMZ pushes them inward. |
| 2026-04-07 | Bombers always visible (troops + airborne) | Fog of war doesn't hide troops or bombers. |
| 2026-04-07 | Bomber area denial only on repeated open-ground hits | Single hits don't create craters. |
| 2026-04-07 | Terrain (rocks/cliffs/trees) in enemy zone too | Same rules apply. Shapes enemy approach paths. |
| 2026-04-07 | DMZ protection zones: cannon 4×4, castle 5×5, cliff 4×4, wall 3×3 | Rocks/trees/open ground do NOT protect. Fragile grid cant push under protected/trees/rocks. |
| 2026-04-07 | 3 firing modes: Auto, Hold, Touch-lock | Auto=slower+-15%. Hold=accuracy circle around finger. Touch-lock=tap ship for 5s, up to 2 targets. |
| 2026-04-07 | Spawn grid: 1×4 in 7×6 staging area | Ships exit 4-side, fast speed until clear of 7×6 box. |
| 2026-04-07 | 4× troop stacking: 4× damage, 2.5× HP | Stacking makes troops dangerous but fragile — one shot kills 4. |
| 2026-04-07 | Friendly fire = ½ damage (was ¼) | More punishing. Makes targeting near own walls a real tradeoff. |
| 2026-04-07 | Battering Ram: diagonal movement, every-other-block pattern | Creates maximum isolation-cleanup damage. |
| 2026-04-07 | Fire Ship area denial: fire→holes→open over 3 sorties | Not permanent. Cycles through states. |
| 2026-04-07 | Transport seeks shortest path from shore to troop target | Optimizes docking position. Redocks on DMZ shift + can seek better spot. |
| 2026-04-07 | Carriers venture closer for shorter bomber turnaround | Risk/reward positioning — closer = faster bombers but more exposed. |
| 2026-04-07 | Fight timer ≥ all ship spawns + 5 seconds | Ensures every ship enters play. |
| 2026-04-07 | Ships cannot fire in staging area, can be hit | 1×4 spawn in 7×6 staging box. Fast speed until clear. |
| 2026-04-07 | 3 firing modes: Auto (slower), Hold (accuracy circle), Touch-lock (tap=5s) | Hold circle tighter at close range, wider at distance. |
| 2026-04-07 | Ship movement is grid-locked (not smooth) | Tactical map representation. Hit a grid = hit the ship. |
| 2026-04-07 | Ship AI determines own position (no destination grids in overlay) | Deterministic AI per ship type. |
| 2026-04-07 | Bombers: 1×2, same altitude, can share grid but no stack | Cannon shots go vertical. Crossing shots can hit. Miss = falls to earth. |
| 2026-04-07 | Bomber area denial = 4 hits on same open ground | 4th hit creates crater. |
| 2026-04-07 | Troop stack max = 4 (was inconsistent 3/4) | 4× damage, 2.5× HP. Consolidated. |
| 2026-04-07 | Changed sections marked with v4.8.6 tags | Left-border accent + version superscript on modified h3 headers. |
| 2026-04-07 | Full consistency pass | flooding→DMZ advance throughout, troop stack 3→4, bomber table, glossary fix. |
| 2026-04-07 | DMZ is 1-2 grids wide, grids look normal | Red only on invalid placement. Width depends on where line falls. |
| 2026-04-08 | **v5.0.1 — Full editorial pass (Task 4)** | 30+ structural fixes, content transfer audit, consistency pass. |
| 2026-04-08 | Fixed 46 section open/close balance | Removed stray `</section>` tags, added missing closes (cannonhp before Part V, wall stacking before Part IX). |
| 2026-04-08 | Removed duplicate Between-Sortie Performance System | Was in both Deploy area and Cannon HP section. Kept authoritative copy in Cannon HP. |
| 2026-04-08 | Removed duplicate Medic row + orphan `</table>` | Stray HTML outside table in Enemies reference. |
| 2026-04-08 | Fixed Wind table (Medium/High rows missing) | Castle Degradation content had been jammed into the wind speed table. Separated and restored both. |
| 2026-04-08 | Castle Degradation restored to Part VI | Content was previously embedded in Wind section. Now proper h3 with full 3-strike rule, enclosure healing, example math. |
| 2026-04-08 | Part VI restructured | Proper Castle & Wall Health section (id=castlehp), Castle Degradation, Destroyed Cannon Recovery, Loss & Replay as separate sections. |
| 2026-04-08 | Visual Language & Color System added to Part IX | 17-row reference table restored from v4.8 — was completely missing from v5. |
| 2026-04-08 | Unlock Timeline populated | Was empty section. Added cannon star-milestone unlock table (10 cannons, 15★–250★). |
| 2026-04-08 | Section IDs/classes standardized | Fixed `id="enemies"` → `id="deploy"`, `id="pieces" class="p-build"` → `id="enemy-ref" class="p-fight"`, added missing classes to 7 sections. |
| 2026-04-08 | Removed "We have amazing Stonwryts" test string | From Build cleanup wipe description. |
| 2026-04-08 | "Siege towers" → "Siege ships" in Campaign 3 quote | Journal rename hadn't been applied to quote text. |
| 2026-04-08 | Team color count: 15 → 20 in Settings | Aligned with Monetization section (20 Tailwind colors listed). |
| 2026-04-08 | Medic healing: "5% per tick" → "3 HP/tick" | Enemies reference table aligned with authoritative absolute values table. |
| 2026-04-08 | Banned terms cleaned | "base level"→"base difficulty", "wave of bombers"→"group of bombers", "separate level"→"separate game mode". |
| 2026-04-08 | Daily Challenges section tag added | Content was floating outside any `<section>`. Now `id="dailies" class="p-econ"`. |
| 2026-04-08 | Castle notation conflict flagged (P1) | Two models conflict: R/V growing visible (campaign tables) vs V/R always-8 visible (Kahneman section). Needs design decision. |
| 2026-04-08 | **v5.0.2 — Castle notation standardized + final polish** | All castle values now R/V: 1/4→9/10, 4/4 Boss. Content transfer verified. 19 dead links fixed. #13 added to Special. |
| 2026-04-08 | Castle progression standardized R/V | 1/4(Cam 1-3)→2/4(4-6)→3/6(7-10)→4/6(11-13)→5/6(14-16)→6/8(17-20)→7/8(21-26)→8/10(27-31)→9/10(32)→4/4(Boss). Visible grows 4→6→8→10. |
| 2026-04-08 | Kahneman section rewritten to R/V | Was V/R "8/1 through 8/8". Now R/V with growing visible counts matching campaign tables. |
| 2026-04-08 | Boss castle count: 3→4 | Boss Finale section said "3 castles, all 3 required". Fixed to 4/4 matching progression and journal. |
| 2026-04-08 | Cam 27 "Missing" description fixed | "E (single castle)" → "E (no territory expansion)". |
| 2026-04-08 | 19 dead internal links fixed | Added id attributes to 15+ headings: theory, build, walls, cannons, castles, ships, troops, campaigns, enclosure, spackle, transport, bombers, ship-spawn, map, rotation, tray-build, piece-catalog. |
| 2026-04-08 | Overview sentence fixed | "Ships with 198 wall pieces" → "The player builds fortifications with 198 wall pieces". Also iOS-only (not iOS/Android), 2-8 min (not 2-5). |
| 2026-04-08 | #13 Boss Encounters added to "What Makes This Game Special" | 13 numbered prose paragraphs now. Bosses as theater capstones, 8-12 sortie marathons, each mechanically unique. |
| 2026-04-08 | Visual-lang section close added | Was nesting settings inside visual-lang. |
| 2026-04-08 | Deploy timer JS comment: 10→20 fixed to 20→30 | Stale comment in battle spreadsheet generator. |
| 2026-04-08 | v4.8 content transfer verified complete | All key content blocks confirmed present: wind, castle degradation, visual language, finger anchor, phase bar, storage swap, off-viewport frame, build steps 1-6, all ship/troop/boss values. |
| 2026-04-08 | **Critical Analysis v2 — fresh deep dive** | 40 items across 4 priorities. Focused on "what blocks a developer from coding this?" Key gaps: enclosure algorithm, ship AI rules, troop pathfinding, spackle+fragile, castle recovery timing, earned time formula. |
| 2026-04-09 | **v5.0.3 — Critical Analysis P0/P1 resolutions** | 11 design decisions integrated into GDD. |
| 2026-04-09 | Spackle CAN be placed on fragile grids | Spackle is lighter than permanent walls. Fragile HP damage irrelevant since spackle disappears after Fight. |
| 2026-04-09 | Castle HP recovery added to Build Step 1 | Enclosed castles recover 1/3 HP during the cleanup wipe. Uses end-of-Fight snapshot (same as cannon Lock-In 1). |
| 2026-04-09 | Ready button during Deploy confirmed | Same behavior as Build — ends Deploy early, unused time rolls to Fight. |
| 2026-04-09 | Last Stand earned time = 100% of final Fight | Was 50% like other sorties. Final Fight→Last Stand now 100%. Alter Time (Stonwryt) can extend by up to 30s. |
| 2026-04-09 | Partial wall piece placement: whole piece fails | All blocks must be on valid ground. Spackle is the exception (partial placement). |
| 2026-04-09 | Sortie count is hand-tuned per battle | Defined in the Enemy Overlay. Added to Layer 3 description. |
| 2026-04-09 | Castles appear gradually | 4 visible (Cam 1-6) → 6 (Cam 7-16) → 8 (Cam 17-26) → 10 (Cam 27+). Castle numbering: #1-#4 starting + boss, #5-#6 at 6 visible, #7-#8 at 8, #9-#10 at 10. |
| 2026-04-09 | Area Denial lifecycle: fire→holes→cleared | Each step advances during Build Step 1 wipe. 3 Build phases to fully clear. Not instantly wiped. |
| 2026-04-09 | Camera pan/zoom during Fight | Same as Build/Deploy. Quick drag = pan, 200ms hold = target. Two-finger pinch = zoom. |
| 2026-04-09 | iCloud sync added | Automatic background sync. Conflict resolution: more total stars wins. Core campaign fully offline. |
| 2026-04-09 | Settings: Restore Purchases + Restart Game | Restore syncs iCloud + App Store receipts. Restart requires double confirmation + typing RESTART. Purchases not reset. |
| 2026-04-09 | iOS only (removed Android references) | Mobile UX section updated. |
| 2026-04-09 | **v5.0.4 — P0-1 Enclosure Detection Algorithm specified** | Full 6-step exterior flood fill algorithm with cliff diagonal exception. |
| 2026-04-09 | Enclosure algorithm: exterior flood fill | BFS from map edges + DMZ boundary through friendly zone. Grids not reached = ENCLOSED. O(n) on ~1,500 friendly grids. |
| 2026-04-09 | Map edges do NOT enclose | Only walls, cliffs, spackle, and castle edges form perimeters. |
| 2026-04-09 | Castle enclosed = ≥1 of 16 surrounding grids is ENCLOSED | The ring around the 3×3 castle footprint. Two separate enclosures both touching = valid. |
| 2026-04-09 | Cliff↔cliff diagonal = only diagonal closure | All other perimeter pairs (wall, spackle, castle, cliff) are 4-way side-to-side only. |
| 2026-04-09 | Enclosure re-runs on every wall destruction during Fight | Tiled floor reverts instantly on breach. |
| 2026-04-09 | Fixed glossary: rocks do NOT form perimeters | Was incorrectly listed as perimeter element. |
| 2026-04-09 | **v5.0.5 — P0-3 Troop Pathfinding Algorithm specified** | Weighted A* with cost table, adaptive batching, greedy 8-grid deadlock fallback. |
| 2026-04-09 | Troop pathfinding: weighted A* | Cost table: open=1, damaged tree=2, cliff=2, healthy tree=4, wall=hits_to_destroy+1, same-type troop(stackable)=1, unstackable/rocks/DMZ/AoD=∞. Diagonal ×1.414. |
| 2026-04-09 | Wall cost = hits_to_destroy + 1 | Troops naturally route toward damaged walls (lower cost). There is always a path — walls are finite cost, not impassable. |
| 2026-04-09 | Path re-evaluation every tick, with adaptive batching | ≤8 troops: all every tick. 9-16: 2 groups alternating. 17-24: 3 groups. 25+: 4 groups. Simulates command confusion. Deterministic group assignment by spawn order. |
| 2026-04-09 | Deadlock fallback: greedy 8-grid | If A* returns no path, check 8 neighbors for closest-to-target passable grid. Same-type blocked grids treated as temporarily passable. Truly stuck = wait. |
| 2026-04-09 | Critical Analysis updated | 12 of 40 items marked resolved (8 P0, 4 P1). Resolved items show ✅ with strikethrough. |
| 2026-04-09 | **P0-2 Ship AI Positioning — deterministic scoring functions** | 11 ship types with grid-scoring formulas. Factors: dDMZ, dWall, dCannon, dCastle, inRange, clearLOS, shield, occ, dmgWall. Recalculate every 4 ticks. Tie-break by grid index. Hit response: temporary flee impulse (Crazy Ivan). |
| 2026-04-09 | **P0-7 Max Cannon Count Formula documented** | Start = min(2 + floor(cam/6), 7). Max = min(3 + floor(cam/3), 12). Boss: 6/12. Fixed getCannons() cap from 6→7 to match Deploy Timer table. |
| 2026-04-09 | Battering Ram + Siege Ship: ship movement in enemy zone, troop pathfinding in friendly | Clarified hybrid movement pattern. |
| 2026-04-09 | Critical Analysis: ALL 10 P0s now resolved | 14 of 40 total resolved. 0 P0, 6 P1, 10 P2, 10 P3 remain open. |
| 2026-04-09 | **v5.0.6 — All P1 + P2 items resolved** | 16 design decisions in one batch. 30 of 40 analysis items now resolved. Only 10 P3 (infrastructure) remain. |
| 2026-04-09 | Max cannon formula updated | Now includes sortie count + ship count: max = min(start + sorties + floor(totalShips/5), 12). |
| 2026-04-09 | P1-2: Fragile under cannon = disappears | Cannon shores up ground. Fragile grid vanishes permanently (even if cannon moves). Other fragile can fill later. |
| 2026-04-09 | P1-5: Spawn points variable | 2-4 per battle, defined in Enemy Overlay. Fixed "4 spawn points" in base map description. |
| 2026-04-09 | P1-6: Wind drift on soft lock, spackle exempt | Drift applies every time player drops a piece. Spackle has no drift (emergency exception). |
| 2026-04-09 | P1-8: Uniform troop damage | Same damage/tick to walls, cannons, castles. TTK differences from structure HP only. |
| 2026-04-09 | P1-9: Spackle = wall for isolation cleanup | Spackle saves adjacent walls from cleanup. Rule of thumb: spackle = wall except no cannon bonus + removed after Fight. |
| 2026-04-09 | P1-10: No cannon type limit | Player can fill all slots with same type. Variety encouraged by encounter design. |
| 2026-04-09 | P2-1: Only Hydra regenerates (5%/sortie) | Visible green pulse on HP bar. All other bosses retain exact HP. |
| 2026-04-09 | Ship locations visible during Build/Deploy | Solid red grid blocks at last positions. Generic — player must remember types. |
| 2026-04-09 | Spawn points marked after first use | Yellow-orange with cross-hatching on edge-of-map spawn points only. Stealth spawns never marked. |
| 2026-04-09 | P2-2: Cleanup always runs (even zero pieces) | Steps 4/5/6 execute regardless. No castles enclosed = defeat. |
| 2026-04-09 | P2-3: Ships switch targets | Primary destroyed → secondary → tertiary. All structures gone → stand down. |
| 2026-04-09 | P2-4: Stonwryt popup goes semi-transparent on events | Red flash behind popup. Does not auto-close. |
| 2026-04-09 | P2-5: Wind compass lower-left (RH) / lower-right (LH) | 32×32pt during Build. Hidden during Deploy/Fight. |
| 2026-04-09 | P2-6: Two replay types | 15-sec quick highlight (victory popup) + 45-90s full time-lapse (battle page). |
| 2026-04-09 | P2-7: Cannon recoil = 3 HP per cannon shot | Damages all adjacent troops. |
| 2026-04-09 | P2-9: Theater order = Coastal first, in order | Later theaters skipped in early campaigns. All 10 used by Campaign 32. |
| 2026-04-09 | P2-10: iCloud sync at phase boundaries + app close | Matches auto-save triggers. Player returns to exact state on any device. |
| 2026-04-09 | **Critical Analysis v3 — Final Inspection** | 40 new items across 5 lenses: Virality (8), Monetization (8), Flow State (8), Unanswered Questions (10), Professional Standards (6). Separate from the v2 analysis (which is fully resolved). |
| 2026-04-09 | **v5.0.7 — Virality items V1-V8 resolved + Tutorial rewrite** | 9 design decisions integrated. |
| 2026-04-09 | V1: Challenge a Friend | Deep link on victory popup: battle #, star count, commander name. Opens App Store if recipient doesn't have game. |
| 2026-04-09 | V2: 9:16 vertical replay export | Left/right side panels for logo, commander, battle info, phase/timer. 1080×1920 MP4 for TikTok/Reels. |
| 2026-04-09 | V3: Defeat is shareable | Replay + Challenge buttons on defeat popup. Near-miss metrics: "1 block from enclosed", "2 ships at <10% HP". |
| 2026-04-09 | V4: Social proof on home screen | Game Center friends badge on campaign cards. Estimated duration on battle page ("~4 min • 5 sorties"). |
| 2026-04-09 | V5: ★★★! frequency = 1 per 15-20 battles | Hard-earned surprise. At least one by Campaign 15. Server-tuned thresholds target this frequency. |
| 2026-04-09 | V6: Seasonal event skeleton (Winter Siege) | 5 maps, 1 boss, free color, 2 cosmetic packs. Quarterly cadence (4 events/year). |
| 2026-04-09 | V7: Free vote mechanic for piece names | Daily upvote/downvote. Top-voted names get free 7-day extension. Free players participate in social layer. |
| 2026-04-09 | V8: Featured Fortresses gallery | Weekly curated top-player screenshots on home screen. Opt-in submission at victory. |
| 2026-04-09 | **Tutorial complete rewrite** | Video-guided demo: tap-to-interrupt, scrub bar, resume button, looping. All 10 cannons available. Auto-complete safety nets. Endless Fight shooting gallery. Win/loss video. "Ready for your first battle?" popup with Yes + Restart Demo buttons. |
| 2026-04-09 | **v5.0.8 — Monetization M1-M8 resolved + Group C fix** | All 8 monetization items integrated. Shape Catalog Group C bug fixed. |
| 2026-04-09 | M1: Civilization Skin Bundles | $2.99-$3.99 each. Walls + cannons + castles themed together (Crystal Kingdom, Obsidian Forge, Marble Empire, Ironclad, Vine-Wrapped, Golden Age). |
| 2026-04-09 | M2: Commander's Pack ($4.99 one-time at Cam 3) | Ad-Free + 1 Color + 1 Exclusive Avatar. First-purchase conversion. |
| 2026-04-09 | M3: Streak achievement badges | Silver (28d), Gold (60d), Platinum (90d), Diamond (180d), Obsidian (365d). Avatar badge + frame + Stonwryt bonus. Persists after streak breaks. |
| 2026-04-09 | M4: 1 ad per battle, before gameplay | Never between sorties. Never after defeat. |
| 2026-04-09 | M5: Commander's Circle ($9.99/year) | Supporter tier: Ad-Free + monthly exclusive color + avatar + early seasonal access + gold badge. |
| 2026-04-09 | M6: Piece naming 3 tiers (30d/90d/1yr) | A-B cost 1.5×, G-H cost 0.6×. "My Pieces" tab with days remaining. A1 is the Golden Piece. |
| 2026-04-09 | M7: Victory screen cosmetic suggestion | Soft sell below share button. Never on defeat. Rotates suggestions. |
| 2026-04-09 | M8: Rewarded video ads | +10s Last Stand after defeat, double Stonwryt after daily, 5 Stonwryts per video (2/day max). |
| 2026-04-09 | Shape Catalog: Group C restored | Group B was rendering C data. Now all 8 groups (A–H) display correctly. |
| 2026-04-09 | Critical Analysis: P3 items added | 10 P3 infrastructure items from v2 now included in the v3 analysis document. |
| 2026-04-09 | **v5.0.9 — ALL CRITICAL ANALYSIS ITEMS RESOLVED** | F1-F8, Q1-Q10, PRO1-PRO6, P3-1 to P3-10. Plus 2 major architectural changes. 50/50 items resolved. |
| 2026-04-09 | **ARCHITECTURE: Board rotated to 64×48 (landscape)** | Was 48×64 portrait. Optimized for horizontal video sharing. Both portrait and landscape orientations supported. |
| 2026-04-09 | **ARCHITECTURE: 2.5D Fight Phase** | Build/Deploy stay 2D top-down. Fight transitions to 2.5D isometric. 3-2-1-FIGHT countdown is an animated camera tilt. SpriteKit pre-rendered sprites. |
| 2026-04-09 | F1: Deploy is a learning phase | Cannons persist between sorties. No auto-deploy. |
| 2026-04-09 | F2: Targeting prompt Cam 1-2 | "Tap a ship to focus fire!" Disappears after first tap or 5 seconds. |
| 2026-04-09 | F3: Timing needs deep analysis | Phases may be too rushed. Needs realistic timing study per battle. |
| 2026-04-09 | F5: Boss duration warning | "~12 min / 10 sorties" on battle page. |
| 2026-04-09 | F6: Star criteria visible | Shown on battle page + during Build. 1★=complete, 2★/3★/! have clear criteria. |
| 2026-04-09 | F7: 3-strike defeat drop-back | 3 losses to same battle = drop back 1 level. Retry button is primary/default. Strikes visible at battle start + defeat popup. |
| 2026-04-09 | F8: Daily challenges unlock after Campaign 1 | 3 challenges/day (Build-only, Deploy+Fight, Combined). 28+ unique setups. Replay unlimited, reward from last play. Watch ad to lock in score. |
| 2026-04-09 | Q1: Star baseline formula | ★=victory, ★★=50% walls+time, ★★★=75%+all cannons, ★★★!=90%+no degradation. Server-tunable. |
| 2026-04-09 | Q4: Geographic leaderboards | 20-50 regions. Campaign-based. Friends board with normalized cross-level scoring. |
| 2026-04-09 | Q5: 4-tab home screen | Home, Campaign (Angry Birds scroll), Daily Challenge, Store. |
| 2026-04-09 | Q10: Cannon type deployment limits | Max per type = floor(totalStars/unlock_threshold), cap 5. ∞ in Cam 1-6. Standard always ∞. |
| 2026-04-09 | PRO1-6 added | Competitive analysis, revenue projections ($22-27K/mo at 100K MAU), tech requirements (iOS 17+, iPhone 12+), 12-month timeline, art direction (Riquochet Studios, 2.5D isometric miniature diorama), WCAG 2.1 AA accessibility. |
| 2026-04-09 | P3 infrastructure: all recommendations accepted | App size, performance, accessibility, server, moderation, privacy, notifications, Game Center, loading, analytics. |
| 2026-04-09 | Shape Catalog: Group C restored | Group B was rendering C's data. All 8 groups (A-H) now display correctly. |
| 2026-04-09 | **Critical Analysis v4 (Brutal Honesty) — 32 items identified** | Major risks, content gaps, balance issues, competitive analysis, minor fixes. Separate document. |
| 2026-04-09 | **NARRATIVE ADDED** | "The Story of Rivenkeep" — Captain Moroni / Title of Liberty inspired. Commander rallies soldiers against unknown fleet. Emotional arc through campaign quotes: confidence→humility→fear→resolve→defiance. No cutscenes, just evolving flavor text. |
| 2026-04-09 | **5 DIFFICULTY LEVELS** | Recruit, Soldier, Commander (baseline), Veteran, Legend. 190×5=950 experiences per War. Modifies timers, pieces, ships, spackle. Separate leaderboards. |
| 2026-04-09 | Assist Mode | Activates silently after 5 consecutive defeats. +5s Build, +1 spackle. No ★★★!. No UI indicator. |
| 2026-04-09 | **BOARD CONFIRMED 64×48** | Landscape orientation. Both portrait and landscape supported. All stale portrait/3:4 references fixed. |
| 2026-04-09 | **2.5D FIGHT TRANSITION = DRAMATIC CROSSFADE** | Map on table → pan to window → fly into dark sky → crossfade to 2.5D battlefield. 2.5-3.0 seconds. Not a camera tilt (SpriteKit has no 3D camera). |
| 2026-04-09 | Server-tunable phase timing | All timer values server-configurable. Current formulas are initial estimates subject to playtest. Rampart arcade timing as baseline reference. |
| 2026-04-09 | 3-strike drop-back: same campaign only | Battle 1 of any campaign = no drop-back, just retry. |
| 2026-04-09 | Stonwryt economy rebalanced | Rewarded video: 3 Stonwryts, 1/day (was 5, 2/day). Daily earn ~20-35 (was 15-25+10 video). |
| 2026-04-09 | Piece naming pricing: App Store tiers | All IAP prices snapped to valid Apple price tiers. G-H 30-day now $0.99 (was $1.19). |
| 2026-04-09 | Progressive onboarding | Brief 3-5 second video for each new mechanic first encountered. Tap to dismiss. Replayable from Settings. |
| 2026-04-09 | Competitive analysis researched | Sky Cannoneer (dead), Castleparts (abandoned), Isle of Arrows (closest active), Cataclismo (PC gold standard). No direct iOS competitor. |
| 2026-04-09 | **v5.1.0 — Full narrative + v4 analysis resolutions** | Deep lore added. 26 of 32 v4 items resolved. |
| 2026-04-09 | **DEEP NARRATIVE: The Story of Rivenkeep** | 7-chapter history: The World Before, Coming of the Fleet, Last Retreat, The Commander, The Whispers, Campaign Arc, Battle Messages. Inspired by Title of Liberty + Ender's Game moral ambiguity. Tagline: "In memory of our homes, our families, our freedom, and our peace." |
| 2026-04-09 | Battle messages system | Each battlefield has 5-8 unique messages drawn randomly at battle start. Same flavor per battlefield, different message each play. Stored in battlefield data. |
| 2026-04-09 | Assist Mode refined | Turns off when player wins. Never activates on previously won battlefields. Only helps push past unbeaten battles. |
| 2026-04-09 | v4 Brutal Honesty analysis updated | 26/32 items marked resolved with green styling. 6 remain open (Chain Shot balance, Lightning dominance, spreadsheet approximation, endless mode, App Store listing, Group B verify). |
| 2026-04-09 | **v5.1.5 — Narrative refinements + link color fix** | Major narrative revision: accidental harm, generational distance, Mystaeri villainous elements, Stonewrights lore. |
| 2026-04-09 | Tagline updated | "In memory of our home, our families, our God, our freedoms, our peace." Chiasmus structure. |
| 2026-04-09 | Commander = he/his | Not they/their. The Commander is a specific person. |
| 2026-04-09 | Narrative: accidental harm, 4 generations removed | Current Shorelands didn't know Mystaeri existed. Ancestors harvested Mystwood unknowingly. |
| 2026-04-09 | Narrative: fleet launched 2 generations ago, can't be recalled | Ships follow carved instructions. Autonomous war machines following ancient orders. |
| 2026-04-09 | Narrative: Mystaeri slightly more villainous | Chose warships over words. Had centuries to learn Shoreland language. Built cannons instead. Disproportionate response to accidental harm. |
| 2026-04-09 | Narrative: Shorelands are defending, not attacking | Commander reclaims defensive positions, pushes fleet back from Rivenkeep's approaches. |
| 2026-04-09 | Stonewrights woven into lore | Ancient guild of master builders. Stonwryt = unit of trust earned through skill. Currency honors guild principle. |
| 2026-04-09 | Link color changed | From #4fc3f7 (hard to read) to #b2dfdb (bright mint). New --link CSS variable. All 25+ inline styles updated. |
| 2026-04-09 | **v5.1.5 — Complete narrative rewrite** | Clean through-line. All Jack feedback integrated. |
| 2026-04-09 | Mystaeri → Mystaeri (y spelling) | All references updated. |
| 2026-04-09 | Ael'thar ritual scene | Emissary performs blood fellowship, commander kills him, burns body on Mystwood ship, intelligent wood carries bones home. Mystaeri see peace offering returned as pyre. |
| 2026-04-09 | Mystwood intelligence | Wood is alive, remembers, can navigate. This is why it made great ships. Cutting it thinned the fog barrier. |
| 2026-04-09 | 4 generations removed | Current Shorelands didn't know Mystaeri existed. Harm was accidental and unknowing. |
| 2026-04-09 | Mystaeri chose revenge over restoration | Young elders overruled patient elders. Had centuries to try again. Chose warships over words. Slightly more villainous. |
| 2026-04-09 | Stonewrights as scholars + religious elders | Pacifists who don't fight. Readers of stone — the ones who decipher Mystaeri language. Commander's Title of Liberty wakes them from pacifist slumber. Elderess Rhyna: "We do not fight. But we will build faster than they can destroy." |
| 2026-04-09 | Removed "nowhere left to go" | Commander's request alone is more impactful. |
| 2026-04-09 | Mystaeri language sounds harsh | "Cracking rock and grinding gravel." Angular, brutal, carved with precision. |
| 2026-04-09 | **v5.1.5 — Complete narrative rewrite from Jack's prose** | 12 chapters (I-XII). All feedback integrated. |
| 2026-04-09 | Mystaeri language: thunderclap/tree-like | Not stone-grinding. Sharp syllables like "thunder rolling through a forest canopy." Elvish but abrupt. |
| 2026-04-09 | Ael'thar (was Rak'thol) | Blood fellowship ritual. Emissary drops petrified Mystwood, attempts broken Shoreland words, performs forehead-to-forehead blood binding. |
| 2026-04-09 | Mystwood communication system | Mystwood translates intent between speakers. Mystaeri carved warnings on stone thinking it would translate like Mystwood does. Stone doesn't speak. |
| 2026-04-09 | Mystholders: specific Mystwood type | Tall, straight, dark. The anchor trees of the fog barrier. Only these were harvested. Many other Mystwood types exist. |
| 2026-04-09 | Why Mystaeri need the mist | Symbiosis: Mystwood exhales mist, mist nourishes Mystaeri. Without mist, children born weaker, elders fade. Thinning fog = slowly suffocating their civilization. |
| 2026-04-09 | Pride cycle | Shorelands ignoring Stonewright counsel during harvesting = pride/wickedness. When ships came, already humbling. Too late. |
| 2026-04-09 | Captain of the Title of Liberty | Humble soldier, leader of True Men. Not a general. Claimed leadership when people fractured. Named Commander through Stonewright anointing. |
| 2026-04-09 | Anointing ceremony | Ceremonial oils (cedar, granite-bloom, myrrh) + ashlar stone staff. Rite of the Cornerstone. Captain too humble for outward display. |
| 2026-04-09 | Elderess Rhyna (was Kiera) | Stone-derived name. Stonewright elder. "The mortar cries out from the ground. Rise, Stonewrights. Lay stone upon stone until the last wall stands." |
| 2026-05-07 | **v5.1.5 — Deep narrative cleanup session** | Complete rewrite with mythic tone. Mystaeri (was Mystborn). Aetherbond, Theoliths, Rivenmen. All 30+ narrative notes integrated. |
| 2026-05-07 | Mystaeri (was Mystborn) | Trademark safe. All references updated across GDD + journal. |
| 2026-05-07 | Shorelanders, Rivenmen | Men of Shoreland = Shorelanders. After unity in Rivenkeep, renamed themselves Rivenmen. |
| 2026-05-07 | Aetherbond + Theoliths | Ordained infant unions. 12x coordination. Die together. Theoliths = teaching pairs. |
| 2026-05-07 | Stonwryt dual meaning | Original = vow in living rock. Currency = gold + black stone, governed by Stonewrights. |
| 2026-05-07 | Elderess = women Stonewrights | Rhyna is Elderess Rhyna. |
| 2026-05-07 | Emissary scene expanded | Banished nobleman's son. Mystwood = wealth trophies. Henchmen mock + kill. Mystwood ship rages in grief-fire. Cover-his-ass report. |
| 2026-05-07 | Ael'thar ritual revised | Grab neck → foreheads → cut commander's arm → release → cut own arm → shoulders together mixing blood. Commander recoils, cut deeper, screams, orders henchmen to kill. |
| 2026-05-07 | Mystaeri symbiosis deepened | Mist filters sun into gentle radiance. Without mist, Mystaeri wither like deep-forest fern in desert. Elders dying of the wound they counseled patience about. |
| 2026-05-07 | Fleet grown from Mystwood | Not built — grown over decades. Orders in Mystwood (not stone). Mystaeri nearly extinct by arrival. |
| 2026-05-07 | Rivenkeep as myth | Ancient hold, long abandoned. Shadow of itself when refugees arrive. People fracture at the sight. |
| 2026-05-07 | Title of Liberty refined | "Will you build for your people, or will you watch them die?" |
| 2026-05-07 | Rhyna's rallying cry refined | "Rise, Stonewrights! Lay stone upon stone. Stand every wall to the very end." Husband: "Rise! Rise! Rise!" |
| 2026-05-07 | Rite of Cornerstone recovered | Ancient tradition found in Rivenkeep's vaults by Rhyna. Contains secrets of building for battle. Staff = polished wood + ashlar cap. |
| 2026-05-07 | Stonewright Seren | Rhyna's apprentice (replaces Hale as translator). Private Hale remains as soldier/discoverer. |
| 2026-05-07 | Mystwood translates dialects | Added: Mystwood bridges Mystaeri dialects, clears confusion. Stone doesn't. |
| 2026-05-07 | Link color: #b2dfdb (bright mint) | --link CSS variable. All inline link styles updated. |
| 2026-05-07 | **Narrative: Final poetic rewrite** | Cohesive mythic prose. Silmarillion-inspired compression. Redundancy eliminated. Single flowing narrative voice. Research: mythic storytelling, Tolkien prose style, poetic cadence, lyrical prose technique. All elements preserved, woven into unified legend. |
| 2026-05-23 | **v5.1.4 — Grammar cleanup + remaining v4 items** | 17 spelling fixes, 12 grammar fixes from Jack's hand-edited v5.1.3c. Chapter numbering (I–XI + XIV) restored. HTML error fixed (unclosed div at Part VI boundary, line 1638). Rivenmen section rewritten in mythic tone. |
| 2026-05-23 | Rampart timing baseline | Build: 25s→20s (Rampart normal=21s). Deploy: 12s→15s (Rampart=10s). Fight: safety net timer unchanged. |
| 2026-05-23 | Chain Shot eDPS narrowed | 4.7–9.2 (was 4.3–12.8). 60% chain decay (was 80%). Damage 22. |
| 2026-05-23 | Lightning takes 2× damage | Explicit glass cannon weakness. Dies first when walls breach. |
| 2026-05-23 | 3-strike avoidance | 15 Stonwryts OR 30-sec ad to avoid drop-back. Strikes reset. |
| 2026-05-23 | App Store listing strategy | "Rivenkeep: Fortress Defense." "Build Walls. Place Cannons. Fight." Position as "Tetris meets Tower Defense." |
| 2026-05-23 | Mystarchs | 10 boss ships renamed. Sovereign commanders grown from eldest Mystholders. Leviathan Mystarch etc. |
| 2026-05-23 | Aelvaren | Emissary's ship. "Bearer of the Binding." Turned against the current, sailed itself home. |
| 2026-05-23 | **v5.1.5 — Grid & Map visual design overhaul** | Two visual modes: Map View (Build/Deploy) + World View (Fight). Grid 24×24px at furthest zoom. 3 color variants per grid type. DMZ moved to Layer 2. Optical illusion correction noted. Future destructible rocks noted. |
| 2026-05-23 | Map View = WWII command table | Flat color-coded tiles. Standardized icons same across all theaters. Build/Deploy phases only. |
| 2026-05-23 | World View = 2.5D isometric | Rich theater-specific rendering. Fight phase only. Dramatic crossfade transition. |
| 2026-05-23 | Layer example images (3) | SVG examples for Base Map, Environmental Overlay, Enemy Overlay created in chat. |
| 2026-05-23 | **Theater mood boards (10/10 complete)** | Full Map View art direction briefs for all 10 theaters. Each shows: open space (3 color variants), trees, rocks, cliffs, 5 castles with walls + cannons, DMZ, spawn points, ships. WWII command table aesthetic. Unique color palette per theater. |
| 2026-05-23 | Theater palettes | Coastal=sandy tan+blue. River=valley green+blue. Swamp=murky green+bog. Forest=deep green+clearings. Mountain=stone gray+cliff brown. Volcanic=dark rock+orange lava. Desert=pale sand+oasis. Frozen=ice blue-gray+channels. Sky=light blue+platforms over void. Crystal=purple+spire triangles+reflection lines. |
| 2026-05-23 | VERSION RULE established | Every GDD change increments version number. Standing rule for all conversations. |

---

## HOW TO START A NEW CONVERSATION
1. Upload this journal file
2. Upload the specific file(s) you need to work on
3. State which thread you're in (GDD / UI / Art / Analysis / Coding)
4. State what you want to accomplish this session
5. Claude will read the journal, understand context, and continue

---

## v5.0.0 RESTRUCTURE PLAN (COMPLETE)

### Principles
1. Single-source-of-truth: every concept defined in ONE place
2. Cross-references via links, not repeated explanations
3. Zero references to previous iterations
4. Consistent left-bar styling with color per Part
5. Expanded glossary with dotted underline + section links (⤴)
6. Changed text marked (latest conversation only)
7. Readable top-to-bottom AND usable as reference
8. Versioning: conversation = +0.0.1, 10 patches = +0.1.0, significant = +0.1, major = user only

### New Part Structure
- **Part I — Foundations** (keep as-is)
- **Part II — The Battlefield** [teal] (Grid, DMZ complete, Terrain complete, Fragile Grids, Fog of War, Theaters)
- **Part III — Build Phase** [green] (Timer, Steps 1-6, Wall Blocks complete, Wall Pieces, Rotation, Tray, Interaction, Spackle, Enclosure, Time Rollover)
- **Part IV — Deploy Phase** [blue] (Timer, Tray, Cannons complete, HP System complete, Bonus System complete, Drag Rules)
- **Part V — Fight Phase** [coral] (Timer, Ticks, Firing Modes complete, Trajectory, Ships complete, Spawn, Troops complete, Battering Ram, Transport, Bombers, Hospital, Bosses, Friendly Fire, Area Denial, Last Garrison)
- **Part VI — Castles** [purple] (Definition, Progression, Degradation, Recovery)
- **Part VII — Progression** [amber] (Campaigns, Layers, Stars, Wars, Spreadsheet, Quotes)
- **Part VIII — Economy** [pink] (Stonwryt, Dailies, Challenges, Weekend Race, Monetization, Naming, Replay)
- **Part IX — Experience** [gray] (Tutorial, Settings, Save, Navigation, Transitions, Victory, Audio, Timing, Visual Language, Future)
- **Part X — Reference** (Expanded Glossary with ⤴ links, Piece Catalog)

### Key Consolidation Targets
- **DMZ**: currently in Map section, Fight section, DMZ Advance section, glossary → ONE section in Part II
- **Cannon HP/Bonus**: currently in Build steps, Deploy detail, Cannon Health section → ONE section in Part IV
- **Enclosure**: currently in Map section, Build steps, Spackle, Castle section → ONE section in Part III
- **Troop behavior**: currently in Enemy Movement, Troop Combat, Troop Targeting → ONE section in Part V
- **Timer formulas**: currently in Build detail, Deploy detail, Phase Timing section → each in its own Part + summary in Part IX
- **Ship types**: currently in Ship AI, Entity Reference, Balance tables → ONE section in Part V
- **Visual indicators**: currently in Visual Language, scattered across Build/Deploy/Fight → ONE section in Part IX + linked

### How to Start Next Conversation
1. Upload RIVENKEEP_JOURNAL.md + Rivenkeep_GDD_v5_1_5.html
2. State what to work on (castle notation fix, new refinement, UI design, coding, etc.)
3. Claude reads the journal, understands context, and continues

## v5.0.0 REMAINING TASKS — ALL COMPLETE

### ✅ Task 1: Consolidate Part V (Fight Phase)
Single-sourced each section. Ships, troops, bombers, targeting merged into authoritative sections. DMZ refs link to Part II. Ship types in one complete table.

### ✅ Task 2: Add Theater Detail Cards to Part II
10 theater descriptions (Coastal through Crystal) with land description, the problem, Layer A mechanic, and enemy vehicle theming inserted as cards.

### ✅ Task 3: Expand Glossary with ⤴ Section Links
77 terms with dotted underline spans throughout. Reference glossary (Part X) has ⤴ links to authoritative sections.

### ✅ Task 4: Full Read-Through for Flow (v5.0.1)
Top-to-bottom editorial pass. 30+ structural HTML fixes: balanced all section/div/table tags, removed duplicates (cannon bonus system, Medic row), restored missing content (Visual Language & Color System, Wind table rows, Castle Degradation), fixed orphaned sections (Last Garrison, Wind, Castle), standardized section IDs/classes, fixed terminology ("Siege towers"→"Siege ships", "wave"→"group", Medic healing 5%→3 HP/tick), added missing sections (Unlock Timeline content, Daily Challenges section tag). All v4.8 content verified transferred.

---

## v5.0.9+ OPEN ITEMS

### 🎉 ALL CRITICAL ANALYSIS v2 + v3 ITEMS RESOLVED (90 total)
### Critical Analysis v4 (Brutal Honesty) — 32 items identified, key items addressed:
- ✅ Narrative added (COMP-3/RISK-4)
- ✅ 5 difficulty levels (RISK-7): 950 experiences per War
- ✅ 2.5D transition specified as crossfade (RISK-2)
- ✅ Server-tunable timing (RISK-5)
- ✅ 3-strike boundary fix (BAL-4)
- ✅ Stonwryt economy rebalanced (BAL-1)
- ✅ Pricing fixed to App Store tiers (MINOR-4)
- ✅ Progressive onboarding (GAP-5)
- ✅ Stale references fixed (GAP-6, MINOR-3)
- ✅ Assist Mode after 5 defeats (RISK-7)

### Remaining v4 items for future resolution:
- **RISK-1:** Build 2D first, 2.5D as later milestone. Track sprite production.
- **RISK-3:** Build map editor tool (laptop app). No timeline pressure.
- **RISK-6:** Launch with 14 daily challenges, expand monthly.
- **RISK-8:** Phase 1 (12mo, 3 theaters, 50 maps). Phase 2 (6mo, full). Phase 3 (ongoing).
- **BAL-2:** Chain Shot eDPS variance — needs encounter design validation.
- **BAL-5:** Lightning dominance — needs encounter-specific counters.
- **BAL-6:** Spreadsheet cannon counts are approximations pending enemy overlay design.
- **GAP-1:** Map editor tool planned (laptop app, JSON-like compressed format).
- **GAP-2:** Audio: all AI-generated. Part of the fun.
- **GAP-3:** 2.5D sprite pipeline: design in 2.5D first, derive 2D. To be explored with Claude.
- **GAP-4:** 5 difficulty levels partially address. Endless/community mode planned for post-launch.
- **GAP-7:** App Store listing strategy needed before submission.
- **GAP-8:** Community map editor planned for post-launch.
- **COMP-2:** Community map editor preferred over procedural generation (fairness for leaderboards).
- **COMP-4:** PvP is a separate game (attacker vs defender). Not in scope for Rivenkeep v1.
- **COMP-5:** Subscription model with decreasing annual price considered.

### How to Execute
Upload: RIVENKEEP_JOURNAL.md + Rivenkeep_GDD_v5_1_5.html + Rivenkeep_Critical_Analysis.html
- Resolve v3 analysis items: "Let's resolve [Flow / Unanswered / Professional / Infrastructure] items"
- Any new refinement: "Refine [topic] in the GDD"
- Start coding: "Begin implementation per Thread 5 (Coding)"

---

## SESSION: 2026-05-31 — Marathon GDD v5.1.7 → v5.2.3

### v5.1.7 — Controls, Pieces, Naming, Enclosure
- [DECISION] Build phase wipe: right-to-left (opposite Deploy→Fight, helps recognize phase)
- [DECISION] Enclosure barriers: walls, cliffs, spackle, castles. Cannons NOT barriers.
- [DECISION] Troops can bypass enclosures if faster route exists (weighted A* pathfinding)
- [DECISION] Tile floor only displays over open space. Trees/rocks/cliffs retain appearance.
- [DECISION] "Waterways" replaces "enemy zone" — ships travel on waterways. Can cut through friendly territory.
- [DECISION] Spackle: wall CAN be placed on spackle (replaces it). Spackle DOES count for cannon enclosure bonuses.
- [DECISION] 4×4 ghost for all spackle sizes (both 2×2 and 3×3).
- [DECISION] Fairness: 5-6 groups = no 4 consecutive (relaxed from 2). 7-8 stays at 3.
- [DECISION] All 198 pieces named in NICKNAMES JavaScript object. Separate HTML table removed.
- [DECISION] Piece naming store: 3-day approval, AI screening, community reporting, 3 chances, stacking (2 slots).
- [DECISION] Default names in white, player-named in gold. Shape Catalog shows 4×4 grid per piece.
- [DECISION] Naming convention: B-D shape-descriptive, E-F tools/creatures, G fortress/mythology arcs, H escalating dread.

### v5.1.8 — Wind & Drift
- [DECISION] Wind compass: upper-right corner of map area.
- [DECISION] Calm = only for no-wind battlefields. Low=1 grid (common), Medium=2 (uncommon), High=3 (very rare).
- [DECISION] Drift-stop: drifting wall stops at any obstacle (walls, castles, cannons, rocks, cliffs, DMZ, waterways, map edges).
- [DECISION] Spackle exempt from drift.

### v5.1.9 — Boss, Cannon, Castle
- [DECISION] 3-2-1 countdown IS the Map→World View transition (2.5-3.0 seconds, one continuous animation).
- [DECISION] Rocks in enemy waterways — ships must navigate around them.
- [DECISION] AoE friendly fire: area-of-effect damage DOES hit enemy troops. Bombers hitting own troops = damage.
- [DECISION] Last Garrison cascade: 5% (was 10%).
- [DECISION] Boss retreat: when hit while attacking castle, retreats. Resumes after 4-6 ticks without fire.
- [DECISION] Ships can damage castles directly (exposed castles after breach).
- [DECISION] Boss castles = starting 4 visible castles. 6 other regular castles.
- [DECISION] Destroyed cannon: enclose immediately → 50%. Not enclosed + not trashed → permanent ruin.
- [DECISION] Cannon trash budget = ⌈total_sorties / 2⌉.

### v5.2.0 — Victory, Stars, Economy (MAJOR)
- [DECISION] **Victory = enclose required castles ONLY. Ships do NOT need to be destroyed.**
- [DECISION] **Star system: 3-lever averaging.** Ships (★:any, ★★:60%, ★★★:90%, !:100%). Cannon Health (★:1 survives, ★★:majority, ★★★:all avg≥100%, !:all avg≥125%). Area Enclosed (★:any, ★★:35%, ★★★:50%, !:85%). Final = average rounded up.
- [DECISION] ★★★! requires 2 levers at ★★★! + third at minimum ★★★.
- [DECISION] 0★ Pacifist easter egg: 0 ships + 0 cannons + minimal enclosure = 10 × campaign level Stonwryts (first time per campaign).
- [DECISION] Difficulty levels: dropped Soldier. Now 4: Recruit, Commander, Veteran, Legend. 190×4=760 experiences.
- [DECISION] War reset: FULL reset including Stonwryts and difficulty. Per-War AND per-difficulty-level economy.
- [DECISION] Cannon type NOT permanently locked — can be moved in subsequent Deploy. Distance-based move bonus: 0 grids=+5%, 1-2=+4%, 3-4=+3%, 5-6=+2%, 7-8=+1%, 9+=0%.
- [DECISION] Firepower AND accuracy scale with bonus. 200% = perfect accuracy + double firepower.
- [DECISION] Cannon carry between battles (within campaign). ≥100% carry forward. Reset at campaign boundary.
- [DECISION] Bonus displays as number on cannon ("+7%").
- [DECISION] "Battle Score" = ships_% + area_% + cannon_% (raw, max 400). Universal performance metric.

### Stonwryt Economy ×10 Overhaul
- [DECISION] All Stonwryt values ×10 with non-round numbers (93, 47, 142, 237, etc.)
- [DECISION] Cannon boost = 6 Stonwryts per 1%.
- [DECISION] Expanded from 9 to 25 purchasable items across Build (9), Deploy (6), Fight (6), Any (2), Defeat (1).
- [DECISION] Stonwryt UI = pause panel. TIME STOPS. Only current-phase items shown. Multi-purchase in single pause.
- [DECISION] Tappable Stonwryt counter in info area opens same panel.
- [DECISION] Purchases immediate, no storing. "Watch Ad (+15)" when insufficient (max 3/day).

### Daily Challenges — 14-Day Game Pack Cycle
- [DECISION] 7 game packs × 2 days each. All skill-building within core gameplay.
- [DECISION] Pack 1: Speed Enclosure. Pack 2: Efficient Enclosure. Pack 3: Castle Defense. Pack 4: Ship Hunting. Pack 5: Wind Mastery. Pack 6: Full Siege. Pack 7: Cannon Endurance.
- [DECISION] Progressive levels 1→5. Must complete each to unlock next. Loss ends run.
- [DECISION] Package rewards: L1=20◆/30min, L2=47◆/1hr, L3=93◆/2hr, L4=163◆/4hr, L5=243◆/8hr.
- [DECISION] One package opening at a time. Replay resets package. Opening grays out Start button.
- [DECISION] 3 package slots.
- [DECISION] Daily streak: 14-day progression. Day 15=Day14+Day1. Day 28+=2×Day14 indefinitely.
- [DECISION] Streak shields (DiMaggio): 28=Bronze, 56=Silver, 112=Gold, 168=Platinum, 224=Diamond, 280=Obsidian, 336=Master, 392=Grand Master.

### Leaderboard Scoring
- [DECISION] Score = raw Battle Score addition (ships_% + area_% + cannon_%). Max 400/battle.
- [DECISION] Each entry shows 3 sub-scores + total. Sortable by any column.
- [DECISION] Overall (all battles/levels, by region), Per-Level, Per-Campaign, Friends (normalized). No daily challenge ranking.

### v5.2.1 — Challenge System Expansion
- [DECISION] 10 categories × 18-20 challenges = 182 total. Package-based rewards (timers, not direct Stonwryts).
- [DECISION] Streak bonus moved to Challenges section.
- [DECISION] 8 easter eggs: Pacifist, Speed Demon, The Impossible, Ghost Fortress, One Cannon Army, No Man's Land, Perfect Storm, Rhyna's Blessing.
- [DECISION] Cosmetic badges earned through challenges. Player can choose which 3 to display.

### v5.2.2 — Monetization & Replay Overhaul
- [DECISION] Team color: 1pt code-drawn outline on walls/castles/cannons/avatar. 20 named colors ($0.99 each).
- [DECISION] Enemy color: same technique, changeable from default Red.
- [DECISION] All cosmetic purchases one-time permanent (Civ Skins, Colors, Avatar Packs, Piece Naming).
- [DECISION] Subscriptions: Ad-Free $4.99, Commander's Pack $4.99, Circle $8.99 (sub) vs $5.99/$5.99/$9.99 (one-time).
- [DECISION] Universal structure look across all maps. Civ Skins change structures; Seasonal Theater Skins change terrain.
- [DECISION] Piece naming: G-H base ($0.99/30d), ×2 E-F, ×4 C-D, ×6 A-B. 4 durations (30d, 90d, 6mo, 1yr).
- [DECISION] Ad-free players CAN still watch rewarded ads for Stonwryts.
- [DECISION] Avatar Style Packs: Realistic, Pencil, Cartoon, Anime, Watercolor, Pixel Art, Oil Painting.
- [DECISION] Replay: Camera Roll only, no in-app storage. Save at victory/defeat or lost forever.
- [DECISION] Commander avatar always upper-left info bar. Campaign/battle/sortie always visible.
- [DECISION] Featured Fortresses: ★★★! submission, loading screen showcase, weekly mini-gallery, 47◆ reward.

### v5.2.3 — Revenue, Timeline, Glossary
- [DECISION] Revenue projections: Low 10K MAU ~$17K/yr, Realistic 50K MAU ~$85K/yr, Top 200K MAU ~$347K/yr.
- [DECISION] Production timeline: 18-24 months solo, 6 phases, fun project no pressure.
- [DECISION] Challenge Express, Seasonal Theater Skins, Replay Filters added to Revenue Streams table.
- [DECISION] Sound Packs, Battle Emblems, Theater Unlock Pass, Legacy Commander rejected.
- [DECISION] Nav bar updated to match current document structure.
- [DECISION] Glossary: 84 terms defined, 211 inline tags (yellow), 11 outdated entries fixed, 6 new terms added.
- [DECISION] Wall Stacking future feature fleshed out: Double Wall (bluish, 4% draw rate) + Reinforced Wall (bright, 1% draw rate). Cannot stack on already-doubled. ~5% total draw rate in War II.

### Documents Updated This Session
- `Rivenkeep_GDD_v5_2_3.html` — 4,449 lines, 10 Parts (SOURCE OF TRUTH)
- `Rivenkeep_Map_View_Briefs.html` — 671 lines (8/10 theater SVGs + portrait tray mockups)
- `Rivenkeep_AI_Image_Prompts.md` — Hero image workflow + 10 theater Midjourney prompts
- `RIVENKEEP_JOURNAL.md` — This file (updated)

### Key Design Rules (Updated v5.2.3)
- Victory = enclose castles only. Ships NOT required (except Boss Finale).
- Stars: 3-lever average (Ships/Cannons/Area), rounded up. ★★★! needs 2 levers at ! + 1 at ★★★.
- Battle Score = ships_% + area_% + cannon_% (raw, max 400). Used for leaderboards & Weekend Race.
- 4 difficulty levels: Recruit→Commander→Veteran→Legend. 190×4=760 experiences.
- Board: 64×48 grids. Grid 12pt × 11.25pt. Both orientations supported.
- Cannon move bonus: 0 grids=+5% → 9+ grids=0%. Cannons carry between battles (≥100%, within campaign).
- 200% cannon cap = perfect accuracy + double firepower.
- Destroyed cannon: enclose immediately → 50%. Not enclosed + not trashed → permanent ruin.
- Cannon trash budget: ⌈sorties/2⌉.
- Spackle counts for enclosure AND cannon bonuses. Wall can replace spackle.
- Waterways replace "enemy zone". Can cut through friendly territory. Rocks in waterways.
- Build wipe: right-to-left. 3-2-1 countdown = Map→World transition (2.5-3.0s).
- Boss retreat when hit while attacking castle. AoE friendly fire on enemy troops.
- Last Garrison cascade = 5%. Ships can damage castles directly.
- Stonwryt economy ×10 scale. 25 purchasable items. Pause panel UI (time stops).
- Daily challenges: 14-day cycle, 7 game packs, progressive levels 1-5, package rewards.
- 182 challenges across 10 categories with package-based rewards and cosmetic badges.
- Leaderboard: raw Battle Score addition, sortable columns, 4 board types.
- 20 named team/enemy colors. Universal structure look + theater terrain skins.
- VERSION RULE: Every GDD change increments version number.

### Consistency Sweep (same session)
- [FIX] All "enemy zone" references → "waterways" (0 remaining)
- [FIX] All "all ships destroyed" victory references removed (enclosure-only victory)
- [FIX] Deploy timer: fixed from 20-30s → 12-15s throughout (was inconsistent with Phase Timing table)
- [FIX] Deploy timer JS comment: 20s→30s → 12s→15s
- [FIX] Last Stand short circuit: removed ship destruction requirement
- [FIX] Victory trigger: changed to enclosure-only
- [FIX] 1-star description: ships not required
- [FIX] Post-Deploy cannon bonus: +2% unmoved → +5% distance-based
- [FIX] Level 5 Legend → Level 4 Legend
- [FIX] Spackle glossary: "NOT for cannon bonuses" → "counts for cannon bonuses"
- [FIX] Fight timer rationale: rewritten for scoring opportunity, not pass/fail
- [FIX] Session length: Commander baseline noted, 4 difficulty scaling added
- [FIX] App Store Listing: fully expanded (identity, SEO, description, video, screenshots, positioning, launch, localization)

### v6.0.0 — Full GDD Pass (Major Version)
- [MILESTONE] Version bumped to v6.0.0 (user-authorized major version)
- [ADD] Backend Architecture section: CloudKit + GameKit + Firebase (Option A). 3 layers, 7 CloudKit record types, 8 Cloud Functions, service layer pattern. ~500 lines server-side TypeScript.
- [ADD] "Quick Answers — 30-Second Reference" master index at top: 18 common questions with short answers + section links. Makes GDD the ultimate game reference.
- [FIX] Removed duplicate "Leaderboard Structure" section with stale star-based scoring (was conflicting with Battle Score system)
- [FIX] Removed redundant "Wall Stacking (Experimental)" section — consolidated into detailed v5.2.2 wall stacking spec with cross-reference
- [FIX] Removed redundant "Reinforced Pieces" future variant (overlapped with Reinforced Wall stacking)
- [CLARIFY] Overview now distinguishes "5 difficulty layers" (A-E campaign dimensions) from "4 difficulty levels" (Recruit/Commander/Veteran/Legend player settings)
- [VERIFY] 220 glossary tags, span balance 371/371, 0 stale version refs, all anchor links valid
- GDD: 4,623 lines, 10 Parts, 84 glossary terms

### v6.1.0 — Final Integrity Pass + Definitive Analysis (current)
- [MILESTONE] Version bumped to v6.1.0. Final integrity pass before handoff to new chat.
- [FIX] Castle HP table (Structure HP) said "ships can't target" — contradicted the rule that ships CAN target exposed castles after a breach. Fixed to "Damaged by troops, bombers, AND ships."
- [VERIFY] Confirmed non-issues: storage slots scale 1→5 by campaign (consistent); "20 soldiers" = narrative quote-givers, NOT the dropped Soldier difficulty level; Deploy timer 12–15s consistent everywhere (incl. JS comment); enemy types match between stats table and glossary.
- [VERIFY] Part structure (I Foundations → X Reference) confirmed as ideal first-read order. No reflow needed — Build→Deploy→Fight matches the gameplay loop.
- [CREATE] Rivenkeep_Critical_Analysis_Definitive.html — merges ALL prior analyses (original 5-lens + v4 + v5). 78 total issues: 62 resolved (logged), 16 open. Supersedes all prior analysis docs.
- [HANDOFF] Added "CURRENT STATE — START HERE" block at top of this journal. Updated header to v6.1.0. Clarified the single source of truth.

### v6.2.0 — Fresh-Eyes Pass + Reorganization (current)
- [MILESTONE] Version bumped to v6.2.0 (significant change: contradiction reconciliation + structural reorg + Critical-Analysis fold-ins). NOTE: this supersedes v6.1.0's "no reflow needed" conclusion — the user explicitly directed a reorganization if a better structure existed, and there was.
- [FIX] **Build timer was specified two incompatible ways.** §Build said 35s→22s (`35−(camp−1)×0.42`, Boss 25s); §Phase Timing said 25s→20s (`25−(camp−1)×5/31`, Boss 22s, +10s S1). Remote Config (`build_timer_base=25`) and the session-length math both use the 25s model → reconciled §Build to it. (Most important fix — timing is "make or break.")
- [FIX] §Fight "Ship Rollover & Victory" said "Victory requires destroying ALL ships" → rewritten to enclosure-only; ship destruction feeds the Ships-Destroyed star lever, not the win condition.
- [FIX] §Castle HP prose said "Ships cannot damage castles directly" — contradicted the Structure-HP table (fixed in v6.1.0) and the "Ships Targeting Castles" rule. Aligned: ships hit exposed castles after a breach.
- [FIX] **Third, obsolete star-criteria definition** in §Victory Celebration still used the old walls%/time%/no-degradation formula, contradicting the canonical 3-lever system. Rewritten as a 3-lever recap (kept battle-page display, hidden !, server-tunable, frequency facts).
- [FIX] Stale defeat reason "Ships remaining — no sorties left" (not a defeat condition) → "Boss survived — no sorties left."
- [FIX] §Visual-Language interior conversion "4 blocks = 1 ω" → "4 blocks = 10 ω" (×10 economy).
- [FIX] §Unlock Timeline wrongly granted "1 storage slot" at Campaign 1 (storage starts Campaign 2) → corrected.
- [FIX] Lore numbering gap (I–X, XI, then jumped to XIV) → Battle Messages renumbered XII.
- [REORG] **Wind & Drift moved from Fight → Build** (it's a Build-phase mechanic; the nav already listed Wind under Part III). Recolored p-fight→p-build.
- [REORG] **Part V (Combat) reordered to cast-before-mechanics:** Enemies → Boss Mechanics → Fight → Castle & Wall Health → Unit & Structure Statistics → Victory & Defeat. (Previously the deep Fight mechanics preceded the roster that defines the units.)
- [REORG] **One-section "Part VI — Castles" dissolved** into Combat (Castle & Wall Health recolored p-castle→p-fight). **Loss & Replay moved to lead Progression** (recolored p-castle→p-prog — it's progression, not a castle topic).
- [REORG] Renumbered to **9 Parts** (was 10): I Foundations, II Battlefield, III Build, IV Deploy, V Combat, VI Progression, VII Economy & Meta, VIII Experience & Polish, IX Reference. Nav rewritten to match (was already out of sync with the body).
- [FOLD-IN] 7 Critical-Analysis items added to the GDD: BAL-1/BAL-2/FLOW-1/FLOW-2 → new "Open Balance & Flow Questions" box in §Unit Statistics; INFRA-3 → determinism caveat in §Design Philosophy; FUT-1 → "Spectator / Watch a Pro" in §Future; POL-1 → "Privacy & Data Policy" in §Production; POL-2 → "Notification Strategy" + Notifications setting row in §Settings; POL-3 → "Analytics event schema" in §Backend.
- [VERIFY] Sorted-line diff vs v6.1.0: the only 41 removed lines were ALL intended edits (zero unintended content loss). Sections 48/48, scripts 5/5, tables 77→77, inline glossary tags 220→222 (none dropped), all JS generated-content containers intact (quotes, roster, battle spreadsheet, piece catalog, glossary, star-criteria, polyomino generator). All 6 contradiction strings now count 0; lore XII present, XIV gone; no v6.1.0 strings remain.
- [UPDATE] Critical Analysis re-checked against v6.2.0; the 9 now-documented items annotated inline (still open work — playtest/pre-submission/dev tasks). Counts unchanged (62 resolved / 16 open).

### v6.2.1 — Difficulty Levels Relocation + Cleanup (current)
- [MILESTONE] Version bumped to v6.2.1 (significant change: section relocation + consistency reconciliation, on top of the v6.2.0 fresh-eyes pass).
- [REORG] **Difficulty Levels (4 player-selectable: Recruit/Commander/Veteran/Legend) moved from Part I Overview → Part VI Progression**, placed directly after "Difficulty Layers & Combination Matrix" so the two confusable difficulty systems (5 campaign layers vs. 4 player levels) sit adjacent. Promoted from an h3-in-Overview to its own `<section id="difficulty">` (anchor preserved); added a levels-vs-layers pointer paragraph; added "Levels" to the Part VI nav. Part I now flows lore → Game Theory directly.
- [FIX] **Chain Shot eDPS reconciled.** GDD table value (4.7 single-target → 9.2 vs 3+ clustered) is mathematically correct from the GDD's own stats (22 dmg × 85% acc ÷ 4-tick reload, 60% per-chain decay, max 3 targets). The Critical Analysis's stale 4.3–12.8 estimate was superseded in BAL-2.
- [FIX] Minor consistency nits: Fight-timer prose "55s" → "56s" (matches the Cam-16 table value); Map Zones heading "Enemy Zone / Waterways" → "Waterways" (canonical term used everywhere else).
- [VERIFY] Sections 49/49 (Difficulty Levels is now its own section), scripts 5/5, 4,652 lines, 222 inline tags. Content-preservation diff vs v6.1.0: all removed lines are intended edits (zero unintended loss). GDD version strings (title/meta/footer) all v6.2.1; 0 stale v6.2.0 strings in the GDD.
- [UPDATE] Critical Analysis re-checked against v6.2.1 (header/verdict/footer bumped; BAL-2 reconciled). Historical "v6.2.0" fold-in annotations retained as accurate records of where each item was first folded in.

### v6.2.2 — Header Color Fixes
- [MILESTONE] Version bumped to v6.2.2 (two section header-color corrections).
- [FIX] **Wall Storage** header color `p-build` → `p-prog`. The section lives in Part VI Progression but was rendering build-green; now Progression-orange like its neighbors (Unlock Timeline, Battle Spreadsheet).
- [FIX] **Future Release Framework** header color `p-exp` → `p-econ`. It was the lone gray-headed section inside Part VII Economy & Meta (a content roadmap fits "Meta"); now pink like its neighbors (Monetization, Replay, Piece Naming). Kept in Part VII — the nav already groups it there.
- [VERIFY] Sections 49/49, scripts 5/5, 4,652 lines unchanged (color-only edits). GDD version strings all v6.2.2; 0 stale v6.2.1 strings in the GDD.

### v6.2.3 — AI-Enhanced Experience
- [MILESTONE] GDD bumped v6.2.2 → v6.2.3. Added new **Part VIII section `#ai` "AI-Enhanced Experience — Apple Foundation Models"** (sections 49 → 50). Designed AI as a first-class, non-optional layer everywhere EXCEPT the deterministic sim.
- [FIREWALL] Section leads with the inviolable rule: AI never touches ship AI, troop AI, RNG, enclosure, stars, Battle Score, or replay. It reads post-hoc structured summaries / writes player-facing text only, off the timed loop, non-authoritative.
- [DESIGN] 8 deep subsections: (1) intelligent piece naming — on-device moderation (fail-closed, layered with denylist baseline) + creative suggestions; (2) post-battle debrief "what went right/wrong" (typed Debrief from BattleSummary, tone-adaptive, advisory); (3) living tutorial (adaptive hints, in-game free-text helper, adaptive pacing — tutorial battle stays deterministic); (4) NL rules help (tool-grounded); (5) dynamic flavor & narrative; (6) daily/challenge framing; (7) accessibility board narration + plain-language settings; (8) recaps & replay commentary. Plus Technical & Safety Constraints table (guided generation, LanguageProvider swappability, device baselines, privacy). [Help personas renamed in v6.2.4.]
- [LINK] Added nav "AI" link (Part VIII); cross-linked Piece Naming (#nicknames), Tutorial (#tutorial), Victory Celebration (#victory) to #ai.
- [CASCADE] Critical Analysis GDD pointers bumped v6.2.2 → v6.2.3 (6 refs; 1 historical v6.2.2 color-fix note kept as accurate history).
- [SDD] **Software Design Document first versioned — v1.0.1**, with a strict rule: EVERY change increments the version (patch=content, minor=section/milestone, major=restructure) + a maintained changelog table. Integrated the AI layer as first-class: new `#ai-arch` architecture section (RivenkeepAI module, `LanguageProvider` protocol, firewall enforced at the module boundary, required baselines per service); piece-name moderation+suggestions → M9; DebriefCoach + TutorGuide + RulesAssistant + FlavorWriter + BoardNarrator + RecapWriter → M11; BattleSummary data-dependency note → M10; "AI features" testing row added. SDD: 23 sections, 13 milestones, 188 check-off items, 14 prompts.
- [VERIFY] GDD sections 50/50, version strings all v6.2.3 at the time, Last Garrison intact. SDD balanced, script intact.

### v6.2.4 — AI Help Persona Naming (current)
- [MILESTONE] GDD bumped v6.2.3 → v6.2.4. Renamed the two AI help personas for in-world consistency (no mechanic/content changes).
- [RENAME] Building & gameplay helper: **"Ask the Stonemason" → "Ask the Stonewright"** (matches the Stonewrights who build — "Assign Stonewrights"). Updated in the Tutorial cross-ref and AI §3.
- [RENAME] Rules help + narrative voice: **"Ask the Garrison" → "Ask the Emissary"** (AI §4) — deliberately avoids collision with the **Last Garrison** castle desperation mechanic, which is UNCHANGED (6 refs intact). Personas now explicit: Stonewright = master builder (building/gameplay help); Emissary = herald/lore-keeper (rules knowledge + dynamic flavor & narrative, §5 attributed to the Emissary's voice).
- [CASCADE] CA GDD pointers v6.2.3 → v6.2.4 (6 refs; 1 historical v6.2.2 kept). Journal version + GDD filename refs bumped.
- [SDD] **v1.0.1 → v1.0.2** (every-change rule). Same persona renames applied (M11 RulesAssistant label + UI; tutorial helper); changelog row added; GDD ref → v6.2.4.
- [VERIFY] GDD 50/50 sections, version strings all v6.2.4, 0 stale v6.2.3, Last Garrison intact. SDD balanced, v1.0.2, 0 stale v6.2.3.

### FINAL DOCUMENT SET (v6.2.4 — current)
- **Rivenkeep_GDD.html** — 9 Parts, 50 sections (THE SOURCE OF TRUTH)
- **Rivenkeep_Critical_Analysis_Definitive.html** — re-checked vs v6.2.4 (62 resolved, 16 open)
- **Rivenkeep_Balance_Analysis.html** — deep balance audit (3 P0 / 4 P1 / 5 P2)
- **Rivenkeep_SDD.html** — Software Design Document + build plan, v1.0.2 (versioned; AI layer integrated)
- **Rivenkeep_Cannons_Towers.html** — Cannon & Tower Design (MODULE of the GDD), v1.0.0. The defender combat model. Stable filename, version internal (git convention).
- **RIVENKEEP_JOURNAL.md** — this file
- **README.md** — repo front page (orientation + doc index)
- **.gitignore** — Swift/Xcode/macOS ignore rules
- All earlier GDD versions (v4.x–v6.2.3) DELETED to prevent confusion.

---

## COMBAT-CONTROL-MODEL SESSION (defender: cannons & towers)

Big design session rethinking the combat roster from counter-web first principles. Produced `Rivenkeep_Cannons_Towers.html` (the source of truth for the defender). Research drew on Rampart (weak roster model — depth was aiming, which we removed), Kingdom Rush (4 archetypes + rich enemy matrix = the model), and hard/soft-counter theory (avoid dominant generalists; prefer soft counters; "perfect imbalance").

**LOCKED decisions (settled):**
- **Pillar:** commander, not soldier. Player controls coverage + ammunition, never aim/fire. Tight toolkit + rich (future) bestiary. Deploy = plan; Fight = watch plan + adapt. Determinism = the teacher.
- **8×3 matrix:** 8 cannon ARCHETYPES × 3 DOMAINS (Land/Sea/Air). Learn 8, not 24. Domain = loaded ammo (per group). Air is a domain-mode, NOT a separate AA cannon.
- **Efficiency = directional cycle:** Land full-vs-land / reduced-sea / heavily-reduced-air; Sea heavily-reduced-land / full-sea / reduced-air; Air reduced-land / heavily-reduced-sea / full-air. No dead picks.
- **Range: CUT (v1.1.0).** Range removed entirely — the AoR *is* the reach; if a target is in the zone, cannons hit it. Domains differ only by the efficiency cycle, not reach. AoR move-distance limit also considered + disfavored. (Reversed an earlier Land-close/Sea-mid/Air-far idea.)
- **Groups:** touching cannons = group; DEPLOY-ONLY (no merge/split in Fight). **More cannons → BIGGER AoR (~linear: 1→base, 2→2×, 3→3×) AND more firepower — grouping is advantageous.** LONE WOLF cannons are the exception: they SHRINK the group's AoR (antisocial). New tension = concentration vs flexibility: one big group = max power but ONE domain + one direction; many groups = multi-domain + independent zones. AoRs may overlap. Heuristic: ~3–4 groups of 3–4 cannons blanket a coastline. Lone cannon = group of one. **(Corrects an earlier note that said "more cannons → smaller AoR" — that was backwards.)**
- **AoR = coverage, not targeting.** Big lazy overlapping zones are the intended steady state. Crews hold fire when AoR empty; fire immediately on entry (must read "coiled," not "asleep").
- **Falloff:** P(hit)=100%−75%×(dist/radius), linear. Centre 100%, edge 25%. 4 cannons at edge ≈ 1 hit. Overlap stacks fringes (the cure for edge-weakness) — a DEPLOY decision. Must show a visible gradient; seeded RNG.
- **Firepower = probabilistic** (not assigned/locked); overkill wasted → discourages over-stacking.
- **Two Fight verbs, both cost silent time:** (A) Re-task AoR — hold-drag, soft-lock until finger lifts, cooldown scales with distance, desaturate. (B) Switch domain — per group, whole group, expensive, RESTARTABLE (timer resets on change of mind), whole group silent, countdown + desaturate over group. Both domain + AoR set in DEPLOY, adapted in Fight.
- **6 towers** (2×2, no damage, one per group incl. lone cannon, NOT upgradeable, no in-battle improvement, DESTRUCTIBLE → enemies prioritize them): Stonewright Post (repair — FIRST taught, fits backstory), Spotter (extend AoR + lift fog of war: spot ships sooner / reveal type earlier), Forge (cut reload + domain-switch cooldowns), Rangefinder (tracking + tighten out-of-domain penalty), Powder Store (damage amp), Jammer (slow enemies in AoR).
- **Upgrades:** cannons get a 3-rank Stonwryt mastery track, PERMANENT account unlocks, per-cannon-TYPE, expensive-but-optional (rank-0 always viable → no capital-cliff, "favored not locked in"). Individual-cannon improvements (existing, e.g. HP carry) stay. Towers do NOT upgrade.
- **All shots lob over walls (NO line-of-sight).** → encourages enclosing your guns → cannon defense reinforces the enclosure victory condition.
- **Mini-game onboarding:** early play IS a ladder of concept-drills (wall → enclose → deploy → AoR → domain → tower), combine phases, until the LAST mini-game IS Campaign 1 Battle 1. Replayable for Stonwryts; re-appear at campaign starts; teach transferable mechanics only.
- **Ship "personalities":** flavor unpredictability inside determinism (e.g. transports doing "crazy Ivans"). Deferred to ships session.

**PARKED / FUTURE ("War 2" & later):** symmetric friendly fire (likely first version = heavily-reduced self-splash to discourage troop wall-camping; ship OFF by default behind a flag); per-cannon overheat/cooldown rhythms; commander-triggered cannon actives; Relay tower.

**8 ARCHETYPES = v1 DRAFT, NOT settled** (system is locked, roles are clay until the bestiary exists): Standard, Rapid, Piercer, Splasher, Chain, Burner, Marksman (recast from "Siege" when range was cut — identity is target-selection: always fires the highest-value threat), Breaker. FLAG: Splasher/Chain/Burner are all multi-target and may blur → consider consolidating to 6–7.

**OPEN QUESTIONS to prototype before locking:** the multi-target trio; falloff readability; idle-as-coiled feel; cooldown lengths (domain-switch heavier than AoR-move?); and the load-bearing one — a stripped M4 prototype answering "does managing AoRs feel like COMMANDING or FLAILING?" Validate that BEFORE investing in the bestiary.

**NEXT SESSIONS (user's plan):** a dedicated **Ships / bestiary** doc (the missing half — the crises the defender answers), then a **Troops** doc (own levers: target priority, path behavior, formation tricks; revealed on landing). GDD will eventually reference the three module docs.

**PROCESS NOTE:** user asked for calibrated honest feedback in design — flag risks in the same breath as praise, say when something is a prototype question vs a known answer, don't manufacture enthusiasm, don't swing to reflexive contrarianism. Biggest correction this session: the Fight is NOT meant to be high-APM; big overlapping AoRs + rare moves = "watch the plan, nudge occasionally." (Assistant had over-worried this; user's AoR-coverage framing resolved it.)

### ▲ REVISIONS — Cannons & Tower doc v1.2.0 (supersedes any conflicting note above)
- **AoR SCALING (corrected):** more cannons → BIGGER AoR (~linear) AND more firepower; grouping is advantageous. Only LONE WOLF cannons shrink a group's AoR. Tension is now concentration-vs-flexibility (one big group = one domain/one direction; many groups = multi-domain + independent zones — domain diversity is the reason to split).
- **RNG seed PER SORTIE** (not just per battle): same board + same layout → identical ship movement and hit rolls. (Falloff miss rolls seeded here too.)
- **Fight verbs (now up to 3):** (A) re-task AoR, (B) switch domain — both can be CANCELLED mid-cooldown → guns immediately re-fire in the old state (cost only paid if the change completes); the two also STACK (do both at once). (C) PROPOSED 3rd verb = Abilities (timed Stonwryt consumables — barrage/flak/wall-patch); ALT = per-group "firing-orders" priority toggle. Decide in roster pass.
- **Archetypes: 16 CANDIDATES → pair to ~8 against the ships** (was 8 draft). List: Standard, Rapid, Piercer(LW), Splasher, Scatter(multishot), Volley(multishot), Chain, Burner, Frost, Marksman(LW), Breaker, Interdictor, Finisher, Overwatch, Disabler(LW), Suppressor. Three Lone Wolves. Explores multi-SHOT (Scatter/Volley) alongside multi-TARGET (Splasher/Chain). Clusters to resolve: multi-hit, control (Frost/Suppressor/Disabler/Jammer-tower), target-personality (Marksman/Interdictor/Finisher).
- **Towers: 10 CANDIDATES → pair to ~6** (was 6). Stonewright Post(first), Spotter(+AoR +fog), Forge(−cooldowns), **Sights** (renamed from Rangefinder — "range" word banished; = accuracy/tracking), Powder Store(+dmg), Magazine(+fire rate), Jammer(slow), Bulwark(+durability), Rally Flag(faster AoR moves/cancel-recovery), Decoy Mast(draws enemy fire).
- **Idle animation:** idle muzzles randomly SWEEP/search the horizon; on ship entry every barrel SNAPS to the same bearing in unison (coiled, not asleep).
- **Mini-games = the "CANDY CRUSH" casual layer:** several per skill, progressive difficulty that EXCEEDS the early campaign, replayable for Stonwryts, combine phases as they climb until the last one IS Campaign 1 Battle 1; player should hit the first real battle thinking "this is easy." Standalone-fun, not just tutorial.
- **RANGE: permanently removed from the game AND from the Cannons doc.** Recorded ONLY here per user. Rationale: range "just seems unfair" and fought the coverage model — the AoR IS the reach (in-zone = hittable). The earlier Land-close/Sea-mid/Air-far idea and any AoR move-distance limit are both rejected; do not reintroduce. Domains differ ONLY by the efficiency cycle.
- **Ships session = SILOED:** develop the bestiary freely on its own first, THEN bring it to the cannon design so the 16→8 and 10→6 pair-downs are a real meshing to what works against each other (no good idea cut early).
- Doc version: Cannons & Tower **v1.2.0**.
