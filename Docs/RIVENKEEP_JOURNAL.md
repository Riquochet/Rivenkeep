# Rivenkeep — Project Journal
**Last Updated:** 2026-09-03 (cont.20c)
**Design docs (current):** GDD v6.7.0 (paired-down hub) · Removed-Content Archive v1.3.0 · The **Why v2.4.0** · Build v1.5.0 · Deploy v1.4.0 · Shape Catalog v1.0.0 · **Cannons & Towers v2.7.0** · **Ships v2.7.0** · **Fleet Memory v2.4.0** · **Campaign v2.4.0** · **Victory v2.7.0** · Fight v1.5.0 · Mini-Games v0.1.0. Governed by The Why. **Every HTML doc single-sources its own version** — one `--doc-version` in `:root`, rendered via `<span class="ver"></span>`. **Design detail lives in the module docs — this journal holds the control panel, the current design canon, and session records.**
**Phase:** DESIGN — ongoing (not prototyping yet; see Design Philosophy).
**Stack:** Flutter + Dart + Flame · iOS + Android · IntelliJ. *(Swift + SpriteKit / CloudKit / GameKit / StoreKit were evaluated and rejected as Apple-only.)*
**Layout:** ⭐ panel → DESIGN CANON → RECENT SESSIONS → ARCHIVE (full pre-redesign history, preserved).

---
## ⭐ START HERE — Master Control Panel (read first, every new session)

### How to start a new session
Upload **only this journal** (`RIVENKEEP_JOURNAL.md`) and say what you want to work on. Claude reads this panel and then tells you **which other docs to upload** for that task (see the Document Index) *before* doing the work. Do NOT bulk-upload everything — the GDD is ~4,200 lines (a hub now, but still large) and can exhaust a single turn's token budget.

### Jack's Design Philosophy — LOCKED (do not re-litigate — this has been restated across three chats)
- **Design-first, fully.** Every element is spelled out ahead of time. We keep designing — in depth, adding new parts as needed — until the design is **elegant and there is genuinely nothing left to design.** Only then do we prototype.
- **Prototyping is tweaking, not changing.** The prototype builds small parts to see how the design is fulfilled and to tune *felt* values — it never discovers or redesigns. **Designs are the facts; the prototype is just feelings.**
- **Why this inverts the usual "prototype early" wisdom.** That wisdom exists because human teams forget ideas, drift, and can't hold a whole design in their heads — so they're forced to find the design by building. Those failure modes are removed here: the docs hold every idea without loss, there is no committee pulling different directions, and Claude verifies each design against game theory and real successful/failed games and flags seams and blind alleys while they are still a paragraph — not a month of code. Design-first is the method this setup is built for.
- **Even felt elements get designed — as specified targets.** Anything only playing can confirm (does managing AoRs feel like commanding? the exact magnitude of the cognition creep? legibility under full load?) is still designed: state the *intended feel* precisely (e.g. "subtle in magnitude, legible in kind") so nothing is left blank. Prototyping later confirms we hit a written target.
- **No hurry to release.** Release, monetization, and the build come in time; not the focus now.

### How Claude must work on this project — LOCKED
- **Be honest, always — Jack should never have to ask for it.** Verify designs against game theory and the corpus of real games; flag risks, seams, and blind alleys early and plainly; give calibrated praise-and-risk together. Never just cheer-lead. (Jack strongly dislikes having to request honesty.)
- **Keep THIS journal current.** It is the through-line record of every decision, across all chats — the one doc that carries continuity. Update it *as* decisions are made, not only at the end.
- **Warn about chat length.** Long chats are problematic — flag when the conversation is getting long and *before* a compaction is likely, so context is not lost mid-thought.
- **Docs are shared memory — Claude writes to them freely, NO permission needed.** The journal + module docs are the memory across all chats and must stay *open and current*. Claude may edit any doc at any time without asking. *(Established 2026-08-29.)*
- **Each turn is COMPLETE — do the pending work, don't just report it.** If something is pending, Claude finishes it this turn (builds the doc, not a delta). No "say the word" hand-offs. Jack reviews Claude's written explanation of what changed and corrects anything astray; **silence = approval**.
- **When unsure, ask ONE clear question. Two or more real options → lay them out in detail** (each option's trade-offs), then let Jack choose. Otherwise proceed.
- **Build, don't hand deltas.** Any change to a doc = Claude edits and presents the file. Design detail lives in the module docs; the journal holds session records + summaries + pointers.
- **Web of documents, not a list.** Every doc is *self-contained on its own design section* (a reader gets that topic without leaving the doc) but *cross-references text in the other docs* wherever a concept lives elsewhere (same-directory links). The GDD is the hub — it links out to every module doc; the docs link back and to each other where relevant. *(Established 2026-08-29.)*
- **Direction of travel — extract to pages.** Eventually every design element gets its own page pulled out of the GDD (easier to work on). The GDD trends toward pure overall-guidance + philosophy + description + a web of links; the module docs hold the detail.
- **ALWAYS name the docs to upload — every turn (Jack, 2026-09-02).** At the end of every turn, state which documents Claude will need for the next piece of work. Jack has them all to hand; the constraint is Claude's token budget, not his access. Corollary: **only parse an uploaded doc when the information is actually needed** — grep/slice for the part in question rather than reading whole files.
- **REAL NUMBERS ARE INPUTS, NOT AUTHORITIES — THE TRANSLATION STEP (Jack, 2026-09-03).** *"Remember that we have to couch it in terms of the game. In the real world, humans die. In the game, bits die. The game has to feel real and always just barely overwhelming."* So derivation from the real world is **step one of two**, never the whole job. Every imported figure gets a **translation check** before it ships:
  1. **What was actually scarce in the real case?** A sniper fires 1.5 rounds per kill because a second shot reveals his position and gets him killed — the scarce thing is *the sniper's life*, not the ammunition. Import the number without the scarcity and you have imported arithmetic while dropping the reason.
  2. **What is scarce here instead?** Cannons are static and effectively unlimited; a hull is a bit that comes back as queue depth. Our scarcities are **attention, coverage, slots, reload cycles, banked time** — and those are what the number has to be re-expressed in.
  3. **Which way does the asymmetry push?** Consistently *one* way: because bits die cheaply, a historically-calibrated pressure will feel **slacker** in-game than it did in life. So restoring the felt weight means **erring toward the harsher end of the evidence**, not the midpoint. When a real range is available and the design has to pick, pick against the player.
- **THE FELT TARGET — "REAL, AND ALWAYS JUST BARELY OVERWHELMING" (Jack, 2026-09-03). This is now the named design target for load, and it has a test.** The design should sit at the **top of every legible band, never the middle**. That is not a new preference — it is the through-line already running under several separate rulings, and naming it unifies them:
  - Contacts: *"eight is the destination, not the danger line"* — the late campaign targets the measured ceiling, not a safe distance below it.
  - Decision-bearing load: ≤4 is a *cap the late game should sit against*, not a budget to underspend.
  - Supply: S ≈ 0.55 means **45% of arrivals leak through even under perfect play** — the fort is permanently, deliberately insufficient.
  - The wall: the requirement squeezes freedom rather than the enemy getting bigger.
  - Timers: low-pressure but *timed*.
  **The test:** at the widest wave the campaign fields, a player should be able to say what every approach is doing — and should have no attention left over while doing it. If there is slack, the band is underspent.
  **"BARELY" is doing the load-bearing work, and it is the red line.** Overwhelming is the target; *unfair* is a failure. The existing red lines are what keep them apart and they are not negotiable: no board may punish a player for not watching a contact that gave no reason to be watched; every loss must be attributable; the game must never be winnable only by placing fast. Overwhelmed-and-reading is the goal. Overwhelmed-and-guessing is a bug.
- **EVERY NUMBER IS DERIVED — NEVER ARBITRARILY SET (Jack, 2026-09-03).** *"Every number should be derived, never arbitrarily set."* And the corpus to derive from is named: *"We need to do the best we can to have real numbers backing our claims. We know facts about humans, game play, wars, and everything else in this game. We should be basing all of our numbers and ideas off of that."* So a number's provenance is part of its definition. The **hierarchy of acceptable sources**, best first: (1) a value inverted from something already locked in the design; (2) a measured real-world figure — military history, operations research, perceptual psychology, shipped-game values; (3) a midpoint of a measured range, with the range recorded; (4) a value derived to a stated design requirement (kill-in-N-passages, slot-indifference). **"Set" is not on the list.** When Claude cannot get past (4), the number ships with its derivation route named in the doc so future-you knows what would replace it. Corollary already bitten twice: a *soft* number is not a number to flag, it is a number to **re-derive** — and re-deriving it has twice found an error in supposedly-settled work (the impossible chord, cont.18; the geometric escort curve, cont.19).
- **BEWARE THE BEST CASE USED AS THE BASELINE (cont.19, the error pattern).** The old Lone Wolf floor (coordination 2.3) turned out to sit at the *optimistic end* of the real sniper range (1.3 rounds/kill), used as though it were typical. That is the specific failure mode to watch for when a number "feels" right: it is often a real figure from the best case. Adopt midpoints of measured ranges, and record the range.
- **JACK'S NUMBERS ARE SUGGESTIONS, NOT CONSTRAINTS (Jack, 2026-09-03).** *"When I sight a number, it is only a suggestion to the current state. If we need to modify that number to fit the game better, then do it."* So any figure Jack has quoted is a **read of the design as it stood when he said it**, not a fixed point to fit the rest of the design around. If a derivation says a number should move, move it and record what moved and why. Corollary, and the reason this matters: when Claude flags a number as *soft*, the correct next move is usually to **re-derive it**, not to leave it flagged — Jack's answer to "core count is the softest number in the pass" was **"then make it harder."**
- **WRITE IT — do not ask permission to be right (Jack, 2026-09-03).** *"For the future, if something is just inherently good, then write it. If you are unsure, or a decision is needed, call those out. You should not have to ask me for permission every time."* So the rule is a **two-bucket rule**: anything that is inherently good goes straight into the docs as canon; anything genuinely uncertain, or that needs Jack's judgement, is written into the doc as an explicit **CALL-OUT** block (not omitted, not softened, not held back for a later turn). Silence on a call-out = Claude proceeds as written; Jack corrects what is astray. This supersedes any turn that ended by asking whether to build the docs.
- **DOCS GET WRITTEN BEFORE A NEW SESSION STARTS (Jack, 2026-09-03).** *"We always write to the docs before we start a new session."* No design work carries forward in chat only. A session is not finished until the module docs and this journal hold its output — the docs are the memory, and an unwritten decision is a lost decision.
- **Style:** terse, peer-level; low tolerance for over-explanation or hedging; no scope-scolding during ideation.

### Document Index — what to upload for what
Stable filenames; versions live *inside* each doc + in git, never in filenames.

| Doc | What it is | Upload when working on… |
|---|---|---|
| `RIVENKEEP_JOURNAL.md` | **This file** — through-line / decision record + this panel | Always (the only file Jack must upload) |
| `Rivenkeep_Why.html` | **The "why"** — design philosophy & first principles; the standing guide governing all docs (v2.0.5) | Any design decision (it governs everything) |
| `Rivenkeep_GDD.html` | **The "how" → now a starting-place hub** — overall guidance + description + a web of links to the module docs (v6.7.0). **~3,360 lines** | Only when GDD detail is needed; upload selectively — still big enough to strain the token budget |
| `Rivenkeep_GDD_Removed.html` | **Removed-content archive** — verbatim record of everything cut from the GDD in the v6.x pair-down (extracted-and-owned + designed-out), badged + indexed (v1.3.0) | Only to recover or check something the pair-down removed |
| `Rivenkeep_Fleet_Memory.html` | Attacker's mind — 3-channel cognition, baiting, flagship, resolve (v2.0.1) | Enemy AI, cognition, resolve/intensity, baiting |
| `Rivenkeep_Cannons_Towers.html` | Defender toolkit — 8 cannons, groups, AoR, 7 towers (v2.0.7) | Defender tools, cannons, towers, AoR, Fight verb *mechanics* |
| `Rivenkeep_Fight.html` | **The unified Fight phase (connective tissue)** — the lived moment-to-moment: sortie tempo, the assembled grid-read, the attention economy, reading the ending. References Cannon/Fleet Memory/Ships/Victory; owns none of their mechanics (v1.2.1) | The Fight phase as an experience; grid-reading; verb cadence; how it feels to play |
| `Rivenkeep_Deploy.html` | **The Deploy phase (phase owner + connective tissue)** — the plan: phase tempo, the cannon economy (slots / type-limits / carousel / trash), placement as a territorial act, emergent grouping + the Build↔Deploy seam, the order card, the auto-AoR default rule, lock-in + handover (v1.0.0) | The Deploy phase; cannon slots & economy; placement; grouping; AoR defaults; standing orders; the Deploy clock |
| `Rivenkeep_Ships.html` | Enemy roster — lineage × axis, troops, bombers (v2.0.1) | Enemy roster/bestiary, troops, formations |
| `Rivenkeep_Campaign.html` | Campaign layout, difficulty model, cognition ramp (v2.0.1) | Campaign structure, difficulty, progression staging |
| `Rivenkeep_Victory.html` | Win condition, sortie resolution, ammo, stars/Battle Score (v2.0.5) | Victory, sorties, scoring, ammo, breakthrough |
| `Rivenkeep_Build.html` | **The Build phase (complete owner)** — pieces + full 16-tier table + selection algo, enclosure + the 2×2 minimum rule, triage geometry, the six-step carryover machine + wall-HP/degradation, full piece state machine + rotation, wind, the rebuild-tax loop (v1.1.1) | Build phase, pieces/tiers, enclosure, triage, wind, spackle, wall roles, state machine |
| `Rivenkeep_Shape_Catalog.html` | **The 198-shape catalog** — every one-sided polyomino grouped A–H with IDs + names, generated algorithmically, + an interactive **rotate-all** button (node-verified) (v1.0.0) | shape catalog, piece shapes, rotate-all, piece names visual |

*Legacy / situational (predate the module set — upload only for their area):* `Rivenkeep_SDD.html` (build plan/architecture), `Rivenkeep_Critical_Analysis_Definitive.html` (issue tracker), `Rivenkeep_Balance_Analysis.html` (numbers audit), `Rivenkeep_Map_View_Briefs.html` (theater mood/UI), `Rivenkeep_AI_Image_Prompts.md` (art prompts).

### Current design state
- **The module docs:** Why, Fleet_Memory, Cannons_Towers, Ships, Victory, **Campaign**, **Build**, **Fight** at their current versions (see the header) plus the **Mini-Games** doc (v0.1.0). GDD v6.7.0 references them via a module-doc map and now **defers detail to them** (paired down to a hub). Governed by `Rivenkeep_Why.html`, internally consistent (pre-Build alignment audit 2026-08-29). GDD v6.7.0 is the underlying "how."
- The game: a Rampart-like **Build→Deploy→Fight** tower-defense that is a **thinking game — strategy is the fun.** Difficulty is the enemy's *cognition*, not its stats. Deterministic → skill (not luck) decides → fair leaderboards via Battle Score.

### STILL TO DESIGN (the queue — design phase is NOT done), priority order
*(Confirmed by the pre-Build audit, 2026-08-29 — see the audit session entry + the MINI-GAMES brief below.)*
1. **The Build phase — DONE (`Rivenkeep_Build.html` v1.1.0; GDD culled to hub stubs at v6.6.0, cont.8–9).** The Build doc is the complete owner — piece taxonomy + full 16-tier table + selection algorithm, enclosure flood-fill + the 2×2 minimum-enclosure rule, triage geometry (first-class), the six-step carryover machine + wall-HP/castle-degradation, the full piece state machine + rotation, wind, the C×E rebuild-tax loop. The GDD Controls/Build/Spackle/Pieces/Wind sections are now hub stubs linking the Build doc (anchors + the naming-linked catalog visual preserved); the Deploy-tray block was archived. Nothing left on this item.
2. **The Fight phase — DOC CREATED (`Rivenkeep_Fight.html` v1.0.0, cont.11).** A new module doc owning only the **connective tissue** (Jack's call: reference the others, own the seams) — the four things nobody owned: (1) the **sortie tempo** (the beat structure: 3-2-1 → assembly window → first contact → steady watch → the one big fire-control call → maybe-correction → withdrawal read; two act-beats, the rest read-beats = the anti-plate-spinning promise made checkable); (2) the assembled **grid-read** (every on-screen layer composed into one picture, one-hard-rail-plus-soft-haze; the bad-load red line); (3) the **attention economy** (the doc's sharpest original claim — actions are cheap/rare, *attention* is the bottleneck; reframes "no morale bar" and the 3-verb ceiling as attention decisions); (4) **reading the ending** (seeing Held/Repel/Breakthrough develop before Victory stamps it). Reverse cross-links added to Cannons (§6 → v2.0.4, + companion list de-pinned + third-domain rule dropped + §5 fog-reveal render), Fleet Memory (holding-fire thread + two-fog visual languages → v2.0.3), Victory (§4 → v2.0.3). **FORK RESOLVED (cont.11 cont.):** domain-switch legibility — Jack tabled the third-domain-mid-reload change entirely; a switch now only cancels (reverses) or plays through, so the meter direction is unambiguous. **FOGS SPECIFIED (Jack):** board fog = opacity + reveal lens; mind fog = twilight→noon saturation; DMZ/spawns/safe-zones always visible. Remaining = felt targets awaiting prototype.
0. ✅ **FLEET SIZING + THE CANNON ECONOMY — DONE (cont.13), REVISED + HARDENED (cont.14).** Sizing model owned by **Victory §3** (`Rivenkeep_Victory.html#sizing`); cannon economy rebuilt in **Deploy §2** (`#slots`); wall budget in **Build §5** (`#wallbudget`); contact ramp in **Campaign §4** (`#contactramp`); throughput in **Cannon §5** (`#throughput`). Run greenfield — no legacy number inherited. See the cont.13 record below.
0b. **ALL THREE PHASE TIMERS — NOW UNBLOCKED, and it is the next session.** #0 is closed, so the derived inputs exist: sortie ≈45 s target and ~1 grid/s ship speed (Victory §3 calibration), and **8–9 pieces for a late-War sortie 1** with 3–4 s per piece plus 5–8 s recognition (Build §5) → sortie 1 wants ≈35–45 s, so the current 25→20 s Build band is short and Deploy's 12–15 s is void. Calibrate against Rampart. Docs: journal + Build + Deploy + Victory + Fight. **Suggested: Sonnet-tier, medium effort** — bounded arithmetic against a benchmark, with the hard inputs already derived.
3. **Terrain & theater mechanics (Layer A).** The 10 environmental systems in depth — especially vs a blind mind. (Docs: GDD + Fleet_Memory.)
4. **Stonwryt economy & meta-progression.** Currency, purchases, how stars/veterancy/3-cannon-carry/unlocks form the progression arc. (Docs: GDD.)
5. **Campaign layout — FRAMEWORK DONE (Campaign v2.0.1, audited aligned).** Introduce→Isolate→Combine, the 5-layer matrix, cognition ramp, roster debut schedule, toolkit teaching order, boss finale are all in the Campaign doc. Remaining piece = the **190-battle generator regen** against the new lineage/cognition vocabulary (a later / data-gen item, below), not new design.
6. **MINI-GAMES (MAJOR — the "candy-crush") — DOC STARTED (Rivenkeep_MiniGames.html v0.1.0 brief).** Vision + 4-rung ladder + the 7 GDD packs mapped + two flagged decisions (no-downside reframe; systematise the ladder) captured. FULL design still waits for Build + Fight (built from the phases).
7. **Boss set-pieces — the 10 Mystarchs.** The roof: promote the chosen flagship chassis into bespoke theater bosses. Later.
8. ✅ **The DEPLOY phase — DONE (`Rivenkeep_Deploy.html` v1.0.0, cont.12).** The third phase-owning doc, parallel to Build (#1) and Fight (#2). Owns the lived Deploy experience: the 6-beat phase tempo (read/act split), the **cannon economy** (slot formulas, per-archetype type limits, carousel/trash — previously homeless, archive-only), placement's three consequences (coverage + grouping + **territory**: DMZ pinning and the permanent fragile-ground cure), **emergent grouping** and the Build↔Deploy seam (courtyard geometry = command granularity) with a JOIN/FUSE/NEW pre-commit preview, **the order card** (4 fields; the 3 Fight verbs reuse its widgets, so Deploy teaches the Fight), the **auto-AoR default-assignment rule** + free instant nudge (the item parked out of the Fight work), the information-state arc (hypothesis → revision → rehearsal), the Deploy read (Map View, exposed health + %, three-state coverage minus the firing state, DMZ ghost, pending-nurture readout, coverage-holes toggle), the locked boundaries + **no auto-deploy**, and lock-in/handover ordering. **One real contradiction surfaced rather than papered over: the Deploy timer** (see cont.12 below).
- **RESOLVED (cont.11) — Fight time-control:** there is NONE. The Fight is continuous real-time; the only stop is hiding the app (freezes, resumes on a 3-2-1 countdown). Screenshot-then-hide is possible but high-effort/low-gain — not designed for or against. NEW: the **battle is replayable, win or lose**, as a strategic tool (deterministic → replay refines execution across the whole battle; fair by the leaderboard's own logic). **RESOLVED (cont.11):** the earlier "Fight-only vs full-sortie replay + scoring" fork is dissolved — the **checkpoint is always the BATTLE** (sortie/phase are pacing + document subdivisions, not save points), and the battle is already the scored unit, so no special replay-scoring rule is needed.
- **Smaller open DESIGN items:** the Mimic-mechanic choice (disguise / mirror-projection / both — a real design decision, gated by legibility); fog-of-war + searching-fire behaviour (borderline design/feel); multi-group serial-command throughput (does the spacing law hold per-commander, not just per-group? — Fight §10 feel-check); the Fight feedback/audio vocabulary (polish, later phase).
- **NUMBERS are the next layer up (deferred until the design layer is done):** resolve magnitudes (per-hull thresholds, broadcast strengths, contagion susceptibility, cascade tipping fraction, recovery, drain weights), air-density, AoR area-scaling, falloff shape/floor, verb costs, cognition-creep rate, ammo amounts.
- ✅ **DONE 2026-08-29: Resolve & Intensity** (per-ship resolve network — Ships §4) and the **pre-Build alignment audit** (5 docs reconciled to v2.0.1; two contradictions fixed).

### MINI-GAMES — design brief (MAJOR; captured 2026-08-29, full design pending)
Jack: the mini-games are a MAJOR part of the game — **"the candy-crush of our game."** Requirements, to be designed to our full standard:
- **Purpose:** develop ALL the skill a player needs to intuit the game, so Rivenkeep becomes the strategy game it's meant to be. They ARE the on-ramp to the north star (a player who can't read the mind can't enjoy the strategy). Now recorded as a supporting law in the Why (§4).
- **Fun, ZERO downside:** no punishment, no loss states — players should WANT to replay them over and over. This is the retention engine.
- **Progressive build-ladder (the core structure):** parts of a phase → a full phase → two phases together → a single run through all phases. Skill assembled bottom-up until the whole game is intuitive.
- **Designed like everything else:** design-first, in depth, verified, honest — never an afterthought.
- **Sequencing (design insight):** built FROM the phases, so they can't be fully designed until the Build phase and the unified Fight phase are locked → design AFTER those. A dedicated module doc gets created when we design them.
- **Protects the Why's tensions:** they build the reasoning that stops retry becoming brute-force (#2) and train the legibility-reading the system leans on as it combines (#3) — not just onboarding, they defend the core promise.

### LOCKED decisions (do not re-litigate — full detail lives in the module docs)
- **⚠ VICTORY CORRECTED (cont.15, Jack) = BEAT BACK THE ATTACK *and* MAINTAIN the required enclosure count.** NOT "enclose castles." Enclosing does not end the battle — the fleet does. The **Last Stand** is the final unopposed window to reach or restore the required count (and to push past it for Area), which is why it inherits 100% of banked time. Defeat = the required count becomes unreachable (castles destroyed below it, or required castles un-enclosable); mid-Build impossibility = clean immediate loss. Being *temporarily* below the count after a breakthrough is a wound, not a loss. **Consequence: the battle is a RACE between the fleet's clock (queue ÷ elimination rate) and the wall's clock (Build phases the requirement demands).**
- **Stars** = 3-lever avg (Ships / Cannon Health / Area Enclosed), rounded up; hidden ★★★!; 0★ pacifist easter egg. **Battle Score** = ships%+area%+cannon% (max 400) = the skill-ranked leaderboard metric (the fairness engine).
- **Difficulty is COGNITION, not stats** — enemies get harder by thinking better; HP/gun/quantity bumps are subordinate, never a parallel treadmill. Cognition rises as a fine, continuous, monotonic per-battle creep (subtle in magnitude, observable in kind).
- **Fleet mind = 3 channels**: LOS (live vision), Contact (persistent hard facts), Effect (decaying fear grid). Blind + deterministic + learns within a battle.
- **Ship pool** = capped, fixed emergence order, fixed spawn-rate, deterministic; sortie COUNT is emergent from outcomes. Pool empties → time rolls to the Last Stand.
- **Sortie = one wave** → HELD (spends its ammo; timer backstops), REPEL (break resolve early → rout, bank time), or BREAKTHROUGH (a required enclosure breached — event, not terminator). All survivors retreat to spawn, re-emerge first in prior order (sunk stays dead), carrying damage, a cognition-tick smarter → player learns motivation, not script. Retreating ships take fire (annihilation = a repel with a full sink).
- **Ammo** = ships shoot only what they carry (finite, relative per-lineage); cannons effectively unlimited (static). Ammo = the sortie's diegetic clock; the GDD **time-rollover economy is kept whole** (unused Build→Deploy→Fight; 50% unused Fight→next Build; 100% final Fight→Last Stand) — ending early banks more. Felt, not managed (no ammo UI).
- **Toolkit paired down**: 8 cannons (Standard, Piercer, Marksman, Interdictor, Suppressor, Breaker, Splasher, Saturation) + 7 towers (Spotter, Powder, Stonewright, Camouflage, Rally, Flare, Jammer). Superset preserved in the docs.
- **Cannon carry**: within a campaign = all cannons' veterancy (cap 200%); BETWEEN campaigns = only the 3 best carry (player picks, with recommendation); difficulty tuned to assume the veteran core.
- **Flagship ↔ Boss**: every battle has a flagship (coordination hub + morale anchor = the standard bearer, the resolve network's primary anchor); a boss is a rare, promoted flagship (fanatical resolve + bespoke mechanics). NOT every flagship is a boss. *(Full flagship spec — flag icon, buff, field promotion, deployment — in Ships §4 v2.0.1.)*
- Studio name **"Riquochet Studios"** is an intentional spelling (not a typo of Ricochet).
- **RESOLVE / INTENSITY / FLAGSHIP — designed; authoritative home = Ships doc §4 (v2.0.1).** *Memory summary only — keep design detail in the doc, not here.* Resolve is a **per-ship network** (own-experience + peer contagion + a flagship anchor broadcast; rides the existing propagation batching; deterministic). No morale bar — read off a **motion signature** (lateral = fear / fore-aft = nerve). Flagship = normal-looking hull with a **flag icon**, one of the first out, screened, **slightly buffed** (durability + speed only, flat/non-scaling); **on death → survivor field-promoted (no buffs), fleet takes on its personality** (succession; chain-decapitation ratchets will down; fanatical inheritor can backfire). **Intensity = one dial** (the flag's broadcast strength) — a **strategy-selector not a power knob**: bluffable = evasive+breakable, fanatical = committed+slaughterable. Spawns have a **safe launch zone** (accelerate fast, can't be hit — anti-camp), shown as a **dead zone** in the AoR coverage. Sortie/battle outcomes (repel/held/breakthrough/retreat/annihilation) are **emergent** from rout cascades and lock to the Victory doc. Dead & superseded: the earlier global-scalar + rally-barometer pass, and the "no-marker / deploy-order-identification" pass.
- **BUILD PHASE — designed + fully extracted; authoritative home = `Rivenkeep_Build.html` v1.1.0 (cont.8–9); GDD culled to hub stubs at v6.6.0.** *Memory summary only — detail lives in the doc.* Extracted the GDD's Build design and elevated three things. (1) **Triage geometry = first-class:** castle layout is a designed set-puzzle (cost-to-enclose / keystones-shared-perimeters / coverage-overlap / exposure) under a hard law — **every board must ship ≥2 near-equal triage solutions** (wide-solution-space); difficulty rises by the requirement ladder *squeezing* freedom, not bigger enemies. **Courtyard of coverage** = every enclosure needs an interior big enough to seat its defending guns (the enclosure tradeoff — tight/cheap vs big/more-Area). (2) **The wall has four jobs:** enclose / buffer / block-troops / conceal-guns; the best placement for one is often not another = the decision. **Defense-in-depth is PHYSICAL, not a rule** — outer wall shields inner wall + courtyard by being a buffer; **enclosure stays binary** (Fork 1 resolved: no redundancy rule; a 2nd ring buys time/distance, never enclosure-redundancy). **Castles are strong wall** (part of the perimeter → consistent build language + cheaper to enclose). **Standalone walls** exist for troop-block + gun-conceal. (3) **The C×E rebuild-tax loop:** ships prioritise walls to *tax your next Build* (worst when your draw is awkward + the gap tight); a sharper fleet hits your **weakest seam**, so Build difficulty = build seam-free + breach-anticipating gun placement, never bigger numbers = difficulty-as-cognition inside Build. Choreography law: piece-pressure (C) and cognition (E) never turn together (Introduce→Isolate→Combine) — one screw per campaign, to protect the legibility ceiling. **Pieces (Fork 3):** the 16-tier escalation is an **engagement mechanism woven INTO the cognition curve, NOT a difficulty treadmill** — piece difficulty is *contextual* (burden in a tight re-plug, a gift across open ground); the decision is matching the drawn hand to the ground; red line — awkward shapes must never be *the* reason a late board is hard. **Wall stacking (Fork 2) = War II** (partial-stack-within-a-piece idea noted as a War-II hook; too much for War 1). **Timer band is load-bearing** — low-pressure timed (see §2 fix below), a red line for tuning: if a board is only winnable by placing fast, the timer is mistuned. Kept whole from the GDD: the six-step cleanup/carryover machine, flood-fill enclosure, spackle tradeoff, wind + drift-stop, one-finger interaction, time rollover. **NEW (cont.9): the 2×2 minimum-enclosure rule** — an enclosed region must hold at least a 2×2 open area to count; a 1×1 pocket or 1-wide slot is dead space, not a courtyard ("otherwise it's just a wall"). Physical reason: a cannon is 2×2, so anything smaller can't seat a gun — it's the concrete floor under courtyard-of-coverage, and it closes the micro-enclosure cheese. **Mini-games (Jack, cont.9):** the Build phase is where much of the mini-game work will live — it's the greatest puzzle-piece game and, mastered, the greatest heart of the game; the Introduce→Isolate→Combine ladder maps onto Build drills (place one piece → close one ring → triage a set → full Build under wind + a reading fleet), plus a board-audit checklist for the ≥2-solutions law. Noted in Build §14; full design waits for the Mini-Games doc.

---

## DESIGN CANON — current quick reference
*Full detail lives in the module docs; this is the fast lookup. The pre-redesign decision ledger + version history is preserved in the ARCHIVE at the bottom.*

GDD reached full feature-completeness around v5.0.2 (46 sections / 10 Parts — the 190-battle spreadsheet, the 198-piece catalog, all entity/timing/audio tables, monetization, tutorial); it has since been restructured into the module-doc set and culled to a starting-place hub at v6.7.0, so that completeness now lives in the module docs.

### Build stack & architecture
- **Stack:** Flutter + Dart + Flame; cross-platform **iOS + Android**; coded in IntelliJ. *(Swift + SpriteKit, and CloudKit / GameKit / StoreKit, were evaluated and **rejected as Apple-only**.)*
- **Backend:** Firebase (Firestore primary) + games_services + in_app_purchase.
- **AI:** 3-tier hybrid behind a `LanguageProvider` — on-device (Apple Foundation Models / Gemini Nano) → cloud fallback → templated/denylist baseline — handling ~8 small text tasks.
- **Board:** 64×48 (landscape); both orientations supported. Fight renders **2.5D** isometric; Build/Deploy stay 2D top-down.
- **Version rule:** every change increments the version; versions live inside each doc + git, never in filenames.

### Key Design Rules (Quick Reference)
- Player NEVER encloses all castles (except Boss 4/4)
- **Structure & checkpoint (Jack):** the hierarchy is **BATTLE → waves of sorties → phases (Build → Deploy → Fight)**. The sortie and phase breakups are for **game pacing and document communication**, NOT save points. The **checkpoint is always the BATTLE** — the whole battle is the replayable *and* scored (Battle Score) unit.
- **Fight time-control: NONE — continuous real-time.** Only in-place "pause" is hiding the app (freezes; resumes on a 3-2-1 countdown) — a convenience, distinct from the checkpoint. The **battle is replayable win or lose** as strategy (deterministic → refines execution across the whole battle; fair by leaderboard logic; no special replay-scoring rule since the battle is already the scored unit). *(Earlier "Fight-only vs full-sortie replay" fork is DISSOLVED — resolved by battle-checkpoint.)*
- **AoRs are auto-assigned defaults** the game gives every cannon/group; the player **nudges** them in Deploy (easy to move), never draws from scratch. Command is **per individual group** — no group-of-groups / multi-select.
- **Audio & haptics (NEXT LAYER — constraint set now):** sound/haptics must be **beneficial, never a constant drone** — each cue earns its place by aiding a read/decision. Hard rule: **the game must be fully playable, and playable well, with no sound.** Legibility stays visual-first; audio only reinforces.
- Deterministic battles — fixed spawn order, fixed troops, this is a puzzle game
- **SIZING (cont.14, revised cont.15):** contacts (objects of attention / target groups per sortie) 2→8, ≤4 decision-bearing at once · approaches 1→3 · hulls 6→24 · pool ≈2.5× peak wave · **queue depth 4–5 → 15–20 formations** · **sorties 3→10 = queue depth ÷ elimination rate (set by the FLEET, not by the wall)**, skill moves it −1/+2 via the elimination rate · guns 2→12 · TKP(n) = 0.45·n^1.5 · S ≈0.55 perfect / ≈0.25 default. Owner: Victory §3/§4b.
- **TARGETING → WHY SCREENS WORK (cont.16, Jack).** Cannons fire at the target **nearest their group's AoR centre** (highest hit probability). Screening is therefore **emergent, not scripted**: screens occupy the high-probability positions while the core sits at the chancy fringe, so *the fleet arranges itself so the player's own targeting preference protects what the fleet wants protected.* Every cannon fires **independently**, so a screen **leaks** — it buys the core time and odds, never immunity. **The lever, with no new mechanic: where you CENTRE the zone decides which hull is most likely to be shot** — forward centre strips escorts, deep centre reaches for the core at the cost of approach coverage.
- **FORMATION SHAPE (cont.16, Jack):** a screen can cover **2–3 cores** (e.g. 6 hulls escorting 2–3 troop ships) — a concentration of value, and screen thickness is a readable signal about what is behind it.
- **PURPOSE COLLAPSE IS A PRESSURE, NOT A KILL SWITCH (cont.16, Jack).** Sinking the last core does **not** end the battle — orphaned screens stay armed and dangerous and may be briefly **more** committed ("out for revenge"). And the symmetric route: **strip enough screens and the cores may refuse to sail.** So there are **two opposite legitimate lines** to beating back the attack — strip the *reason* or strip the *nerve* — answered by different defender tools, which is what stops core-hunting being the single dominant strategy.
- **FLEET DEFEAT (cont.15) = two ways.** (A) **ANNIHILATION** — no ships left. (B) **PURPOSE COLLAPSE** — no purpose-bearing hulls left, so screens have nothing to escort and resolve has nothing holding it up → queue-wide retreat. Hulls split **purpose-bearing (cores: transports, carriers, bombards/breachers, flagship)** vs **purpose-serving (screens)**. Third path: **stalemate retreat** — valid but costly, and scores nothing (see credit rule). **So fleet-scale decapitation is the primary strategic line, and every back-line-targeting tool now runs to the win condition.**
- **FORMATIONS PERSIST (cont.15)** with role slots: one **core** + **screen slots**. Empty screens **refill fresh from the queue** (costing queue depth) or go out under-screened if dry; a **sunk core dissolves the formation** → survivors become **orphans**, reallocated to under-screened formations **keeping their damage** ("probably damaged and soon sunk"); orphans with nowhere to go = a **coreless residual**, the state that collapses resolve. **Damage is temporary; purpose is permanent.**
- **RESOLVE IS QUEUE-WIDE (cont.15)**, not per-sortie: it spans unsailed reserves, accumulates across the battle, and **purpose is a fourth resolve input** alongside own-experience, peer contagion and the anchor broadcast.
- **FORMATION GRAMMAR = THREE KINDS (cont.17).** **Convoy** (1–3 cores + screen slots; purpose in the core hull) · **Wolfpack** (2–4 like hulls, NO core; purpose = a shared *errand*, borne by every hull — Jack: *"they do not escort anything, they are just an attack wave"*) · **Solo** (Mimic only). Purpose-bearing still = **cores only**, so purpose collapse is untouched. Wolfpacks are purpose-*serving at fleet scale* — they prepare the next convoy's run. Screen slots split into **shields** (interpose — occupy the position nearest your AoR centre) and **riders** (Quartermaster / Chirurgeon / Herald / attached Recon or Sower — never interpose). **Only shields count for sortie refusal.** Owner: Ships §9.
- **SCREEN SLOT ≈ ONE TKP-HULL (cont.17).** Slot counts derived from Victory §3's TKP(4)=3.7, not chosen: **Runner 4 · Skyfall 4+1 rider · Breacher 3 · Bombard 2 · Leviathan 1 · command 4+1–2 riders.** The **axis prices the screen** (Durability/Evasion drop slots, Payload adds one) — no new dial. A shield is a **positional** asset, not HP-in-hulls, which is what keeps it off the treadmill. Shared screens scale **sub-linearly** for a geometric reason (circumference ∝ √area): 1 core → 4 shields, 2 → 6, 3 → 6–7 — which reproduces Jack's "six hulls, two or three troop ships" without being fitted to it. Killing one core of several **releases surplus shields as orphans**, so attacking a shared screen core-by-core reinforces the rest of the fleet; the only good answer is to break it inside one engagement.
- **THE SCREEN IS A LIVE ALLOCATION, NOT A SET OF STATIONS (cont.17, Jack).** Escort **tightness = the fleet's confidence in its own map** (loose in unknown waters, closes up when it believes it has your AoRs pinned — a fourth belief register, and **baitable**: tighten it against a zone you already moved). A screen **need not be a ring** — it can be a **picket line forward, nearer the AoR centre, whose job is to draw fire**, which is the purest expression of the cont.16 targeting rule. Escorts are **faster than their core and reallocate under fire** — a healthier shield slides across to cover a failing one, so **focus-firing one shield summons a better hull rather than opening a hole**; the counter is to make two holes at once. Falls out free: a convoy moving at **escort speed has lost its core**.
- **SHAPE READS PURPOSE (cont.17, expanded on Jack's note).** Four independent reads off one glance, no UI: **geometry** = which core is inside (column=transport · ring=carrier · line abreast=bombard · wedge=breacher · shieldwall=command · picket=bait screen · scatter=wolfpack · **shapeless=orphans**) · **thickness** = value · **tightness** = belief · **quality** = cognition tier. Two authoring laws: a shape must never lie by accident (Mimic is the sole licensed liar, with a fair tell); shape must survive the switch-moment (→ hard cap of **two domains per shared screen**).
- **BOMBERS GET AN ESCORT SCREEN (cont.17, Jack).** The core/screen grammar is **not sea-only**. An **escort flight never shoots, takes damage, and sits OUTSIDE the carrier's linked HP pool** — that separate pool is the load-bearing detail (sharing it would dilute the carrier's life and make shooting escorts kill the carrier, which is backwards). 1 escort flight per 2 bombers, capped at 3. Fixes anti-air being a pure throughput check; gives air the same "what inside the cloud do I shoot" decision the sea has. Contact accounting unchanged (cloud + escort = 1 contact). Owner: Ships §8.
- **ELIMINATION RULE (cont.17) = A FORMATION IS FINISHED WHEN ITS PURPOSE CAN NO LONGER BE CARRIED.** Convoy: **the moment its last core slot empties.** Wolfpack: **last hull dead, OR errand void** (its target gun destroyed or re-enclosed, its sector already mapped, its field already laid, the Provocateur you never fired at) — so **enclosure discipline literally shortens the battle**, and purpose collapse resolves *through* the wolfpack rule with no special case. Rejected: "all hulls dead" (turns elimination into a throughput metric and inverts the incentive) and "core dead + orphans absorbed" (makes the rate depend on the fleet's bookkeeping, retroactive and unreadable). **TWO CLOCKS:** *Q* (formations) drains by elimination only and **shortens** the battle; the *pool* (hulls) drains by every sink and **weakens** it. Killing cores fast = shorter but denser. Supersedes cont.15's "a refill costs a formation-slot": refills draw hulls from the reserve, so screens are paid for in pool, not queue depth.
- **QUEUE COMPOSITION (cont.17).** Ratios across the pool: **cores ≈1/5 of hulls, shields ≈2/5, wolfpacks + riders ≈2/5.** *Q* = **5 / 11 / 17** formations (15 / 37 / 54 hulls; 3 / 6 / 10 cores) against the 4–5 / 10–14 / 15–20 brackets. The mix **inverts** across the campaign — early battles are mostly payloads, late battles mostly the preparation around payloads (the cognition ramp as fleet structure). **The elimination rate now DECOMPOSES:** late-War ≈0.8 convoy + ≈1.4 wolfpack = **≈2.2/sortie** → 17 ÷ 2.2 = **7.7 sorties**, inside Jack's 7–10; mid 2.0, early 1.7. First time this number has structure under it. **Sortie composition law:** at least one convoy sails every sortie *while one is willing*; at most one consecutive all-wolfpack **preparation** sortie — without it, skittish wolfpacks repel early, survive, re-emerge first and clog the queue so cores are never reachable.
- **THE ORPHAN FORK (cont.17, Jack) — revenge OR retreat, arbitrated by resolve.** Jack: *"the screen could continue as a wolfpack, but it could also retreat — it lost its purpose."* Resolve above its rout threshold when the last core dies → **turns wolfpack** (drops escort behaviour, stops interposing, starts shooting); below → **breaks off and retreats**. So **the player's own prior pressure decides which** — a clean early decapitation buys an angry wolfpack, the same kill on a ground-down formation buys a retreat. **A surgical kill is more dangerous than a worn-down one**, which finally gives the grind line a payoff of its own. **Revenge is a BEHAVIOUR SWAP, not a resolve spike** — purpose is removed, never inverted; resolve keeps falling while the board gets more dangerous (both halves of the ruling, no new state, no timer; it ends at reconstitution or at rout). Legibility answered by Jack's own line, now canon: **orphans keep their damage and have no shape, so they look battered and shapeless where a wolfpack looks deliberate.** Trigger on the **last** core, not any core.
- **SORTIE REFUSAL (cont.17) = a core refuses when its SHIELDS fall below half its own screen requirement**, re-evaluated every sortie (a stall, not a state). **Intensity moves the threshold, and therefore decides WHICH ROUTE A BOARD OFFERS:** bluffable → approach cores refuse at ≤2 shields (nerve route open, decapitation hard); default → ≤1 / 0; fanatical → 0 / never (sails alone — decapitation open, nerve route shut); Herald-pinned → never. So the intensity dial is now structural on the **win condition**, not just on rout behaviour — every board offers a route and reading which one is the skill. **The tell must be a presence, not an absence:** refusing cores **loiter visibly in the safe launch zone** (never fogged) while their wolfpacks sail without them — the nerve route's equivalent of the coreless residual.
- **THE SNIPER KEEPS THE ROUTES HONEST — AND THE WOLFPACK KEEPS THE SNIPER HONEST (cont.17, Jack).** The **Marksman ignores the screen** (not bound by the nearest-to-AoR-centre rule — *that is why it is a sniper*), **pays in rate of fire** because it is *looking for the payload* (diegetic cost, not a balance tax), and **is confused by a wolfpack** — no core in its zone means nothing to search for, so it dwells and wastes its slow shots. **The wolfpack is the anti-sniper formation, with no special rule.** Completes the chain: core-hunting → answered by the screen → answered by the sniper → answered by the wolfpack → which has no payload and cannot win on its own. Nothing dominates. ⚠ **Owner note: these are CANNON DOC changes (Cannons §4 / Lone Wolf family), flagged not yet applied — that doc was not in the cont.17 session.**
- **THE FLAG DOES NOT SAIL FIRST — ITS CONVOY DOES (cont.17, Jack).** *"The flagship does not come out first. Its convoy does. It is the standard bearer. The flagship should be just like any other ship. It has a job to do."* The flag is a **marker on a hull with its own job**, occupying the **command core** slot of an ordinary convoy. Consequences: the flag's **lineage now matters twice** (its promotion effect *and* what it is physically doing — a Bombard flag shells your wall while it anchors the net); **decapitation becomes target selection inside a live formation** rather than a race to catch a lone hull; and the command convoy is an **ordinary formation for queue purposes** (promotion moves the standard elsewhere rather than resurrecting it), so *Q* needs no exception. **Superseded:** "deploys first, takes station at the back, broadcast dormant until the wave assembles." The **assembly window survives relocated** — the baitable moment is a convoy *forming up* at its launch zone. ⚠ **OPEN CALL-OUT: does the flag's "slightly buffed" durability+speed survive this ruling?** It was justified by the old lone-arrival opening; "just like any other ship" argues it should go. Left in place, flagged in Ships §4.
- **⚠ CORRECTED (cont.17) — THE FLAG IS *NOT* ALWAYS ITS OWN CONTACT.** It is a **label on its formation while screened**, and becomes its own contact **only once separable** (thinned, or maneuvering clear). The old rule failed the arithmetic: at C=2 the flag plus escort ate the entire contact budget every sortie and no payload ever arrived. Common fate is the measured criterion and it gives the right answer. Consequence worth keeping: **stripping the flag's escort costs the player an attention slot** — committing to the kill makes the board harder to read at the moment you commit. Fixed in **both** Victory §3 and Ships §9.
- **LONE WOLF FLOOR DERIVED (cont.19) — from sniper rounds-per-kill. Coordination 0.5, F = 34%** (was coordination 3 / F 64%, *set*). Anchor: **US snipers in Vietnam averaged one kill per 1.3–1.7 rounds expended.** That is directly our quantity (shots per hit against a designated target); the companion figure (≈200,000 rounds per body for infantry on full auto) is deliberately NOT used — it is dominated by suppression, so a "1.5 vs 200,000 precision ratio" would be fake grounding. Midpoint 1.5 → P(hit) 0.67 → F = 2P−1 = 0.34 → coordination 0.5. Range recorded: 1.3 → coord 2.15, 1.7 → below 0. **Status: derived but WIDE** — the path-mean transform doubles input uncertainty, so this ships with a confidence interval rather than pinned. **Two findings worth more than the number:** (a) the old 2.3 was the *best-case sniper taken as baseline*; (b) the real data says a sniper's edge is **SELECTION, not precision** — 67% single-shot is a good crew, not a magic one — which independently confirms cont.18's arithmetic conclusion that the Marksman's value is reach, not throughput. **So "precision baked in" is redefined: a Lone Wolf is FOCUSED, not ACCURATE** — the tightening is the *zone not growing* (r stays 4), not a higher floor.
- **⚠ CONTRADICTION RESOLVED (cont.19) — "two Lone Wolves grouped → ~90%" could never have been right.** §9 defines the Lone Wolf as **"penalty when grouped"** while §4's table gave grouped Lone Wolves the **highest floor in the game**. Both were canon. Resolution follows from the definition, not taste: **a Lone Wolf gains no coordination from grouping, because not coordinating is what makes it a lone wolf** — floor stays 34% however many you group, and the penalty is purely geometric (grouped Lone Wolves forfeit the zone growth, so two cover the same r=4 circle for two slots). Retires the last "bonus ladder" rung the Coordination stat existed to eliminate.
- **MARKSMAN ×1.5 RELOAD — now derived to a target (cont.19).** 3 hits ÷ 0.67 hit rate = ≈4.5 shots; at 1.33 shots per 8-grid transit = **≈3 passages ≈ 1.5 sorties to delete a core** — slow enough that the slot is a real decision, fast enough to pay inside a battle. Output revised **0.36 → 0.30 cores/passage**, still ≈5× a forward-centred 4-gun group *per slot*. Real fire-rate evidence would support a **harsher** penalty (deliberate aimed fire recorded at just over 3 rpm against a mechanical 15–30 for trained riflemen), so ×1.5 is the generous end of the evidence and is the first lever to pull if the Marksman proves too strong.
- **SHARED-SCREEN CURVE RE-DERIVED (cont.19) — exponent 0.775, measured in the Atlantic, replacing my geometric √x.** Anchor: the WWII operations-research finding that convoy losses could be cut ≈64% by raising merchants per convoy **32 → 54** while escorts rose only **6 → 9**. `ln(9/6) ÷ ln(54/32) = 0.775` → **shields = 4 × cores^0.775** → **1 core → 4 shields, 2 → 7, 3 → 9** (my √x model said 4 / 6 / 7). **Why real is flatter than geometric:** √x treats a screen as a *ring*, but a real screen is ring + depth + detached picket stations, and stations answer *bearings*, which do not thin out as the formation grows — the same reason Jack ruled that a screen need not be a ring (cont.17). Two findings arrived independently and agreed. **Jack's "six hulls for two or three troop ships" now matches the TWO-core case exactly and undershoots three** — per the suggestions rule, the curve wins and the example moves.
- **NOT EVERY FORMATION IS ESCORT-SCALED — and history supplies the categories (cont.19).** Real escort share varies by an order of magnitude with what the formation is *for*: **merchant convoy ≈12–24%** (ON.153 45/6 · HX.231 67/19 · HX.300 159/32) → our shared Runner convoy, the curve's home case; **carrier task group ≈85–95%** (one carrier behind battleships, cruisers, a destroyer ring) → our Skyfall battlegroup and command convoy, which are *supposed* to look absurdly over-escorted; **line of battle** — no meaningful ratio, every ship a shooter → Bombard line / Leviathan pair, **flat 2 shields or self-screening, NOT curve-scaled**; **assault wedge** — the point is expendable → Breacher, **flat 2–3**. So the fleet is **four real doctrines side by side**, which is also why shape can read as purpose: the shapes differ in the world for the same reasons they differ here. Honest check: our fleet overall is ≈24% cores where a merchant convoy is 76–88% payload — we sit between convoy and task group because our fleet is *both*, which no single real formation is. First external check this composition has ever had.
- **CORE-KILLS/SORTIE DERIVED FROM THE COVERAGE LAW (cont.19) — the cont.18 assumption removed.** ≈1.4/sortie had *assumed* a doctrine of one hunting group. The doctrine is **forced** instead: ≤3 approaches may be live and a late fort is 3 groups of 4, so holding every bearing consumes every group — **any group diverted to deep-centred core-hunting uncovers a bearing outright**, which delivers its payloads and buys a castle-degradation tick. Sustainable *h* = 1. Table: **h=0 → ≈0.6** (leak only, decapitation never happens) · **h=1 → ≈1.2 sustained** · **h=2 → ≈1.8, a 1–2 sortie BURST not a doctrine**. So the figure is a **range with a hard ceiling: 1.2 sustained, ≈1.5 with bursts** — both terms (approach limit, leak fraction) themselves derived.
- **CONSEQUENCE — 14 CORES MEANS PURE DECAPITATION CANNOT FINISH THE BATTLE (cont.19).** 14 ÷ 1.2–1.5 = **9.3–11.7 sorties against a cap of 10.** Stronger than cont.18's "it buys the long battle": core-hunting alone lands at the cap in the best case and past it otherwise. Purpose collapse stays a real route — you reach it by killing cores **and** stripping screens until survivors refuse and their wolfpacks void their errands; together that closes inside 7–8 sorties. **The boundary is the actual design choice and is recorded: 12 cores = pure decapitation finishes exactly at the cap; 14 = it requires help. 14 chosen (Jack: make it harder).**
- **⚠ Q BRACKET SUPERSEDED (cont.19): Q = 4 / 9 / 11**, not 5/11/17 and not the old 15–20 late. The 15–20 came from dividing the pool by an *assumed* 3 hulls/formation; on the measured escort curve convoys are 5–12 hulls and the mean rises to ≈5.3, so Q must fall. **Nothing was lost — it was a derived intermediate, not a design target.** Pools unchanged (17 / 41 / 58). Elimination rate now **≈1.1–1.3/sortie** late (≈0.6–0.75 convoy + ≈0.5 wolfpack) → 11 ÷ 1.3 = **8.5 sorties**; mid 9 ÷ 1.6 = 5.6; early 4 ÷ 1.3 = 3.1. **Jack's 3–10 sortie range unchanged at all three stages.**
- **HULL CAP BEATS CONTACT CAP LATE — so a sortie is WIDE or HEAVY, physically (cont.19).** Three separately-derived limits collided: 16–24 simultaneous hulls (Rampart), 6–8 simultaneous contacts (tracking research), convoys of 5–12 hulls (convoy history). Eight contacts of real convoys = 60+ hulls, triple the cap. **Not a contradiction to patch — it is "wide and simple OR narrow and clever, never both" becoming PHYSICAL, enforced with nothing authored.** *Payload sortie* = 1–2 convoys + 1–2 wolfpacks → **3–4 contacts, 19–24 hulls**. *Preparation sortie* = 6–8 wolfpacks → **6–8 contacts, 16–22 hulls**. So the 2→8 contact ramp stands and **8 is reached on preparation sorties** — exactly when the player most needs to read wide, since there is no payload to anchor attention. Bonus: the two sortie kinds are now **legible at a glance from the wave's silhouette** — wide and thin means no core came out, so the refusal tell and the wave's shape are the same signal. Watch-out: a payload sortie sits at 3–4 contacts *all decision-bearing* — the ≤4 law at its ceiling with nothing spare, and the tighter prototype case.
- **FALLOFF REBUILT (cont.18) — F IS NOW DERIVED, NOT CHOSEN.** `F = 28% + 12% × (coordination)`, soft-capped below 100%: mixed group 28% · pure same-type 40% · Lone Wolf (coord 3) 64% · two LW grouped 88%. Derived by **inverting the two supply ratios the locked star thresholds already fix** — S≈0.55 (perfect allocation, diametral transit, path-mean) gives F=0.38; S≈0.25 (default zones, clipped chord, area-mean) gives F=0.28; the increment is the gap between them. **Mean P(hit) = 0.69 coordinated / 0.52 default** — ≈0.55 is SUPERSEDED everywhere. Formulae: path-mean `= 1 − (1−F)/2`, area-mean `= 1 − ⅔(1−F)`. Owner: Cannons §4.
- **⚠ ERROR FOUND & FIXED (cont.18) — the old bottom-up k₁ route used an IMPOSSIBLE CHORD.** Victory §3 route 2 read *"a 4-gun group has r=8, so the mean chord across it is ~20 grids"* — **a chord of a radius-8 circle cannot exceed 16.** The 20 was load-bearing (20 shots × 0.55 = 11 hits = TKP(4) 3.7), so the celebrated "two independent routes agree" rested on a geometric impossibility. **Fixing it strengthened the result:** correct chord 16 grids → 16 shots → required mean P rises to 0.69 → which is exactly what a 38–40% floor produces. So the mean is no longer an *input* to route 2, it is route 2's **output**, and **k₁ = 0.46 held** — the most load-bearing constant in the game survived its own audit. New structure: route 1 pins k₁ from the star thresholds; route 2 pins the edge floor from k₁.
- **SCREEN LEAK QUANTIFIED (cont.18) — the missing rule was that target preference is PROBABILISTIC, not argmax.** "Fire at the highest-probability target" taken literally leaks **nothing**, which would make the screen perfect cover and core-hunting a locked door — exactly what Jack's ruling forbids. The rule: **a crew picks its target with probability proportional to hit probability**; barrel share on target *t* = Pₜ ÷ ΣPᵢ. Everything the screening model claims follows from that one line. Numbers: **forward-centred zone → 10% of barrels reach the core ≈ 0.21 cores/passage (≈1 per 5); deep-centred → ≈35% ≈ 0.8 cores/passage (≈1 per 1)**, which straddles the cont.17 bracket (≈1 core per 2 passages) from both sides — so the screen is real AND the core is reachable. **Closes the cont.16 coupling.** The cost of deep-centring is not a penalty: the escort crosses untouched, so the formation still delivers — you killed the purpose and lost this passage.
- **THE MARKSMAN, SPECIFIED (cont.18 — the cont.17 debt paid).** Ignores the screen **absolutely** (not bound by the probability weighting — selects the core outright, whatever is interposed) · **×1.5 reload** (≈6 s — the search is the cost, diegetic not a balance tax) · **dwells with no core in zone** (so the wolfpack is the anti-sniper formation, via the sniper's own logic, no special rule) · Lone Wolf, zone doesn't grow (r=4), coord 3 → F=64%. **Honest output ≈ 0.36 cores/passage — LESS than a deep-centred 4-gun group, and that is correct: four barrels beat one.** The Marksman's value is not throughput, it is that **it kills cores without trading away an approach.** Completes the four-link counter-chain: core-hunting → screen → sniper → wolfpack → (no payload, can't win alone). Red line: if the Marksman becomes a mandatory late slot, the wolfpack share of the queue is too low — fix the fleet, not the gun.
- **CORE COUNT RAISED (cont.18, Jack: "then make it harder") = 4 / 9 / 14** across the campaign, re-derived from throughput instead of feel. A strong decapitator manages ≈1.4 core-kills/sortie late (one group deep-centred at ≈0.8 + two approach groups leaking ≈0.2 each), so **14 ÷ 1.4 = 10 sorties → pure decapitation now buys the LONG battle** (worst banked time, worst Cannon Health). It still wins; it no longer wins *best*. **The 7-sortie battle requires mixing routes** — strip screens until cores refuse, stalling the queue into all-wolfpack preparation sorties whose errands then void. **So the two routes become COMPLEMENTS rather than alternatives, at the level of arithmetic and not just tools.** Paid for without growing the pool: cores 19% → 24% of hulls and **shields fall**, affordable only via the sub-linear shared-screen curve (14 cores across ≈7 convoys, so most carry 2–3). Emergent second-order effect: **a late fleet commits more purpose behind thinner escorts** — more desperate and more brittle at once, and since refusal is measured in shields, **the nerve route opens naturally as the battle goes long.** Rosters: Q = **5 / 10 / 15**, pools 17 / 41 / 58. Elimination rate moves to **≈1.5–2.1/sortie** (superseding ≈2–2.5) because a convoy dies only when its *last* core does; **Jack's 3–10 sortie range is unchanged.**
- **DECAPITATION IS NOT AVAILABLE EARLY — and should not be (cont.18, falls out).** Early cores are 4 but an early fort is **2–4 guns**, nowhere near the throughput to deep-centre a zone *and* hold an approach. So Cam 1–6 is won by annihilation (pool only 17 hulls) or by holding the wall clock; **the decapitation route debuts at 5–8 guns.** That is Introduce → Isolate → Combine applied to the win condition itself, and the campaign should stage it deliberately. Owner: Campaign §4.
- **FLAG BUFF — RESOLVED (cont.18, Jack): THE FIRST FLAG IS BUFFED; SUCCESSORS ARE NOT.** *"The first flag ship should be buffed. It is the captain of the team, so there is a reason why. If it fails, the battle promotion on the next sortie does not have the buff."* The buff is **who the ship is**, not a consequence of the old lone-arrival opening — the fleet's original commander is a better-built hull with a better crew because the fleet chose it for the job; an inheritor is a lieutenant standing in. This sits cleanly beside cont.17's "just like any other ship" because the two are about different things: the flag has an **ordinary job** and an **extraordinary crew**. What it buys: **the decapitation ratchet gets a first step that is genuinely harder than the rest** — chain-decapitation *accelerates*, which is the mechanical form of a command structure degrading. The recorded risk still stands and now matters more: handing the flag to a **fanatical** survivor makes the fleet harder to break while making it easier to kill.
- **AoR scaling = LINEAR IN AREA** (n guns = n× area ⇒ radius ∝ √n; r₁ = 4 grids, 4-gun group r = 8). Chosen for immediate human comprehension, not realism. Lone Wolves are the sole exception (zone doesn't grow; falloff tightens).
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
- ⚠ ALL PHASE TIMERS VOID pending #0b (cont.13). The old set — Build 25s→20s (+10s S1 bonus), Deploy 12s→15s, Fight 25s→90s — was set under pre-AoR ship counts. Derived inputs now exist: 8–9 pieces for a late sortie 1 at 3–4 s/piece + 5–8 s recognition → ≈35–45 s. Ready button in all three (kept). (v6.2.0 unified the Build timer; old "35s→22s/+15s" was a stale second spec.)
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
- Cannon slots: DERIVED from fielded load — solve TKP(n) = S × arriving hulls, round down, grow in-battle by Fight performance, cap 12 (= 3 approaches × 4 guns, where r = 8 is the readable viewport height). Voids the old `min(start + sorties + floor(totalShips/5), 12)` (cont.13, Deploy §2).
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
- **Board: 128×80 grids RECOMMENDED (derived cont.14; supersedes the inherited 64×48, which fails all three sizing requirements).** Derived from approach depth (≈39 grids/bearing), fear-cell crossing (2–3 cells ≈ 26–38 grids), and fort-core triage variety (≈50×35). Phone-legibility ceiling ≈108 grids tall. Middle option 96×64 (2× area) if authoring cost bites. Both orientations supported; landscape primary. **Zoom/pan = a designed see-vs-act tradeoff, and pan/zoom performance is a DESIGN BOUND** (smooth at the widest wave on the oldest device; if a board can't hold it, shrink the board or the wave, never the camera).
- **Fight phase: 2.5D isometric perspective. Build/Deploy stay 2D top-down. 3-2-1-FIGHT is animated camera tilt.**
- 3-strike defeat: 3 losses to same battle = drop back 1 level. Retry button is primary. Strikes visible.
- Cannon type limit: `max(2, ceil(slots/3))` — a fraction of your slots, so it scales with a derived slot count (Deploy §2, cont.13). SUPERSEDES both "no cannon type limit" and the old `floor(totalStars/unlock_threshold), cap 5`.
- Star criteria: 3-lever average (**Ships Accounted For** / Cannon Health / Area Enclosed) — sunk 1.0, **routed 1.0**, normal withdrawal 0, and **unemerged reserves × the fraction of purpose-bearing hulls destroyed** (revised cont.15 — the old "only on a Retreat, 0 on a fast enclosure victory" test is obsolete because a fast enclosure win no longer exists; the proportional rule needs no retreat-type test, cannot be gamed by turtling, and points the scoring at the same target the win condition does). Thresholds (any/60%/90%/100%) and denominator (the capped pool) unchanged, rounded up; ★★★! = 2 levers at the hidden ! threshold + 1 at ★★★; shown on battle page + Build panel, server-tunable. (v6.2.0 removed the obsolete "50% walls+time / 75% / 90%+no-degradation" formula that still lingered in Victory Celebration.)
- Home screen: 4 tabs (Home, Campaign, Daily, Store). Campaign scrolls Angry Birds-style.
- Leaderboards: geographic regions (20-50), campaign-based matching, friends with normalized cross-level scoring.
- Daily challenges: unlock after Cam 1. 3/day (Build, Deploy+Fight, Combined). 28+ unique. Replay unlimited, reward from last play. Ad to lock in score.
- Studio: Riquochet Studios. Art style: 2.5D isometric miniature diorama (tabletop game feel). AI-generated with human curation.
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

## RECENT SESSIONS — the module-doc redesign arc (2026-08)

## SESSION: 2026-08-28 — Module-doc design arc + v2.0.0 consolidation

The stretch that took the design from "attacker foundation only" to a complete, coherent, internally-consistent foundation. Six module docs now sit under `Rivenkeep_Why.html`, all at **v2.0.0**.

### What was designed
- **Fleet Memory → v2.0.0.** Confirmed the 3-channel mind (LOS / Contact / Effect); fixed stale "two-channel" phrasing (the 3 UI registers mirror the 2 *persistent* channels — LOS is live, not a remembered register; troops ride the full 3-channel mind).
- **Ships (roster sweep) → NEW, v2.0.0.** The bestiary as **lineage × axis** over the 3-channel mind. Troops + bombers folded in (GDD mechanics kept, spelled-out TYPES dropped). Herald reframed **boss-only** (resolve is a flagship *intensity knob*, not a common lineage).
- **The pair-down → LOCKED.** 16 archetypes → **8 cannons** (Standard, Piercer, Marksman, Interdictor, Suppressor, Breaker, Splasher, Saturation) + **7 towers** (Spotter, Powder, Stonewright, Camouflage, Rally, Flare, Jammer). Superset preserved. AoR re-task made a **costed crawl** (Cannon doc).
- **Campaign → NEW, v2.0.0.** Meshed the GDD skeleton (Introduce→Isolate→Combine, 5-layer matrix / 32 campaigns, triage, 10 theaters, 190-battle generator, boss finale) with the cognition model + locked cast. **Cognition ramp = a fine, continuous, monotonic per-battle creep** (subtle magnitude, observable kind). HP/quantity **subordinate to cognition**, superseding older GDD text. Expansion-lineage debut schedule locked (Provocateur/Corsair in Pairs; Wraith mid-Triples; Mimic late/Quads; boss forms in the finale).
- **Victory → NEW, v2.0.0.** Battle win kept from GDD (enclose required castles; stars + Battle Score). Added: the **capped, fixed-order ship pool** with emergent sortie count; the **three sortie end-states** (repel / held / breakthrough) with unified retreat-to-spawn and same-ships-same-order; **ammo** as the sortie's diegetic clock with the **time-rollover economy kept whole**; breakthrough with real-but-recoverable stakes + the anti-death-spiral guarantee; **3-best-cannon carry between campaigns**.
- **The Why → NEW, v2.0.0.** The design-philosophy / first-principles doc — the "why" to the GDD's "how"; the standing guide. Holds the north star, the guiding principles, the fairness-as-values argument, and the foundational tensions.

### Resolved (previously open)
- **Win-condition seam** (long-standing cross-doc open) → unified in Victory.
- **Multi-target cannon question** (Splasher / Chain / Sweeper / Saturation) → resolved by the pair-down (kept Splasher + Saturation; cut Chain + Sweeper).
- **Ammo ↔ time-rollover** → reconciled: ammo decides *when* the wave withdraws; the GDD rollover runs underneath (ending early banks more time toward the Last Stand).

### Method note (why this arc mattered)
Jack's **design-first philosophy** was made explicit and LOCKED (see panel). The prototype-early reflex was set aside: design fully first, prototype only to tune *felt* values against written targets. Claude's standing job: verify against game theory + real games, flag seams early, be honest without being asked, and keep this journal current.

### Next
**Resolve & Intensity** (the thinnest load-bearing piece). Then Build / enclosure, Stonwryt economy, terrain (Layer A), the unified Fight phase.

---

## SESSION: 2026-08-29 (cont.) — Resolve reframed to a per-ship network; four corrections

The resolve piece, hardened. The first pass (earlier same day) proposed a global scalar + a flagship-rally "barometer" read. Jack pushed on four points; the model is stronger for it and is now definitive (design-first: facts, not prototype punts). The whole layer now sits as a peer of the fear grid — fear is a spatial field of the *defender's danger* (on the map); resolve is a network field of the *fleet's will* (on the hulls). Both propagate with lag, both read as shapes/behaviour, both deterministic, both manipulable — the design's recurring signature (same principle across layers).

### The four corrections
- **Per-ship network (was: global scalar).** Every hull carries its own resolve; hulls influence neighbours (panic contagion + steady-cluster stiffening) under a top-down anchor broadcast. Gives "one hull routs, another stays," the flagship-death reroute, and fanatical contagion-immunity — none of which a scalar could produce. Propagation reuses the command-confusion batching (resolve rides the same lagged net as fear/contact). Fully deterministic.
- **Anchor hierarchy + reroute.** Flagship = primary (its broadcast strength = the intensity dial). On its death the net re-anchors on the next node (Herald > Quartermaster > capital > peers) — weaker, fragmented, slow/local. Herald boss = a resilient primary anchor you must kill to drop the floor ("break their will through the standard, not the hull").
- **The tell is DEFINITIVE, not a felt-target** (fixes the punt Jack rightly rejected — "prototype is sanding, not sawing"). Two orthogonal motion components: LATERAL = fear (nets forward, skirts around a HOT cell), FORE-AFT = nerve. Wavering = rearward drift; routing = the run to spawn; retreated = off-field. You cannot confuse advancing-around (lateral) with drifting-back (aft). No UI, no barometer — motion IS the display (real battles have no morale bar; you read behaviour). The binding rule that makes "no UI" honest: a hull's motion is a deterministic FUNCTION of its resolve, so behaviour is a faithful render of the network by construction, never a lossy approximation.
- **Fanatical cuts both ways.** Evasive+breakable (skittish) vs committed+slaughterable (fanatical) — a strategy-selector, not a power knob. Fanatical fleets ignore the fear grid and drive into kill-zones; vs them you build the grinder and let them come. This is also the definitive "switch to grind" read (they don't skirt, don't drift back — they drive straight in). Satisfies the anti-treadmill law: high intensity is a *different problem with its own exploit*, never "more HP."

### Flagship deploy behaviour (gut-checked, adopted)
Flagship comes out FIRST and takes STATION (back line), program DORMANT until the wave assembles on it. Verdict: consistent and good — it arrives first to *hold station as the anchor point*, not to charge in first (resolves the "why is the screened ship in front" objection). Creates an assembly window (broadcast off → fleet shakiest & most baitable, flagship briefly catchable before the screen forms). Caveat handled: not a free snipe (far back, short window, high-risk reach) — rewards aggression without letting a player skip the screen. Reinforces the network: an opening alpha *before the anchor is up* seeds a cheap cascade, and the fleet firms up as it assembles and the broadcast comes online (a within-sortie resolve ramp — shaky open → anchored mid).

### Retracted
The global scalar (R, and τ_rout / τ_commit / ρ as global constants) and the flagship-rally-effort barometer. Dead. Thresholds are now per-hull; the read is behavioural (the motion signature).

### Definitive vs sanding (honouring "design is facts, prototype is feelings")
DESIGN FACTS (locked): the network structure; the anchor hierarchy + reroute; the motion-signature tell (lateral = fear / fore-aft = nerve); resolve→motion as a deterministic function; fanatical-as-tradeoff; the assembly window; and the emergent map to Held / Repel / Breakthrough / Retreat / Annihilation. SANDING MAGNITUDES (specified targets; final values tuned in prototype — feelings, not facts): per-hull rout thresholds and anchor broadcast strengths per intensity tier; contagion susceptibility per tier; the cascade tipping fraction (target: once a cascade starts, the wave visibly unravels over ~2–3s); recovery rate; the relative drain weights (cluster-sink vs scald-crossing vs stalemate-tick vs anchor-kill).

### Verification (game theory + real games)
- Total War morale (the doc's own precedent), now matched *exactly*: per-unit morale, rout on threshold, panic contagion/cascade, general's death cratering + re-anchoring on sub-commanders, army-wide collapse when the net can't hold. The scalar under-modelled this; the network is the faithful version.
- Real crowd/panic dynamics: morale as a contagion field on a network of agents is the standard model — cascades, thresholds, and immune (fanatical) nodes are textbook.
- Signaling core preserved: resolve reads the (bluffable) fear grid, so "break their will" is a well-defined deception against a deterministic receiver.
- Anti-turtle & two-paths hold: a turtle gets Held/breakthrough, not repels (can't ratchet the net down the fast way) → relies on slow stalemate-drain + risks breakthrough (valid-but-costly). Fanatical fleets can't be repelled → the grind path is never vestigial.

### Cross-doc edits — ✅ ALL DONE (v2.0.1 built 2026-08-29)
Resolve / Intensity / flagship is now reconciled across every doc — nothing pending.
- ✅ **Ships §4** — the authoritative home: full per-ship resolve network, anchor hierarchy + field promotion, flag-icon marker, motion-signature tell, intensity dial, deployment / assembly window / safe launch zone; §13 resolve open-Q closed.
- ✅ **Fleet_Memory** — §12 ledger row rewritten to the per-ship network (per-hull rout continuous mid-Fight; cascade→repel mid-Fight; battle-Retreat at the boundary); "three ways a battle ends" labelled battle-level + cross-ref to Victory's sortie-level three; the resolve-belief block points to Ships §4; §14 resolve open-Q CLOSED; the legibility risk marked resolved (the motion-signature tell).
- ✅ **Victory** — §4 repel row = an emergent rout-cascade in the network, and repels drop the fleet's resolve baseline (the break-will currency); lead points to Ships §4.
- ✅ **Cannon** — §3 enemy spawn **safe launch zone** (accelerate fast, can't be hit; anti spawn-camp) rendered as a **displayed dead zone** in the AoR coverage.
- All three → **v2.0.1** when applied.

### Next
Build phase — pieces & enclosure (queue #1). Docs to upload: GDD (selectively — ~4,700 lines) + Cannon.

### Flagship spec refined (2026-08-29 cont.)
The flagship = the standard bearer (network primary anchor), now fully specified. **Looks like a NORMAL ship** — retires the "unmissable silhouette" (a boss visual would trivialise the decapitation read). **Slightly buffed** — modest durability + speed, sub-boss, NOT firepower — so reaching it is a committed play, never a stray-shot snipe; the buff is a FLAT STRUCTURAL fact, not a scaling knob (intensity scales, HP/speed don't — anti-treadmill). **Identification is a true commander action with NO marker/UI:** PRIMARY tell = deploy order (comes out first / among the first); RE-ACQUISITION tells (the fair, non-bookkeeping path) = the fleet screens & forms on it, it holds station at the back, it shrugs off hits a normal hull wouldn't. Always among the first out → no marker needed (marker only as a fallback if a lineage can't deploy early). **Honest flag raised & resolved:** pure "memorise hull #7 for an hour" would be the bad load Why §4 forbids; the behavioural re-acquisition tells keep it reasoning, not clerical. **Escalation ladder:** the Mimic/Impostor boss fakes these tells with decoys, so identifying the real flag becomes its puzzle. (Now built — Ships §4, v2.0.1.)

---

## SESSION: 2026-08-29 (cont. 2) — Flagship finalised; design moved into the Ships doc
Workflow correction from Jack: the JOURNAL is the cross-chat memory record; module DOCS hold the design. Acted on it — the full Resolve/Intensity/flagship design is now written into **Ships §4 (v2.0.1)**, and the journal's LOCKED block is collapsed to a summary + pointer. Going forward: design → the relevant module doc (built, not deltas); journal → light session records.

Flagship decisions this turn (now in Ships §4):
- **Flag icon** — the flagship is a normal-looking hull wearing a flag-icon marker. REVERSES last turn's "no marker / identify-by-deploy-order"; the icon makes the bad-load concern moot. (Icon marks WHICH hull; behaviour still tells HOW CLOSE — no morale bar.)
- **Field promotion** — kill the flag and a survivor is promoted (flag icon, NO buffs); the fleet takes on that hull's personality. Succession: you inherit whatever you leave alive; chain-decapitation ratchets will down; a fanatical inheritor can backfire.
- **Buff confirmed** — durability + speed only (not firepower); flat / non-scaling; successors unbuffed. Other ships actively protect the flag (the screen).
- **Spawn safe launch zone** — every spawn has a corridor where hulls accelerate fast and can't be hit (anti spawn-camp); shown as a displayed dead zone in the AoR coverage. ✅ Now built into Cannon §3 (v2.0.1).

### Next
Build phase — pieces & enclosure (queue #1); GDD (selectively) + Cannon.

---

## SESSION: 2026-08-29 (cont. 3) — Two pending fixes done; standing working agreement set
Jack: fix the two pending items, and a standing rule — **Claude writes to the docs freely (no permission), each turn is complete, no dangling "pending"; if unsure ask one clear question, if 2+ options lay them out in detail; docs are our cross-chat memory and must stay open.** Recorded in the START HERE working-rules list above.

Both fixes built (docs all → v2.0.1):
- **Fleet_Memory** — resolve reconciled to the per-ship network: §12 ledger row rewritten (per-hull rout continuous mid-Fight; cascade→repel mid-Fight; battle-Retreat at the boundary); "three ways a battle ends" now labelled battle-level with a cross-ref to Victory's sortie-level three; belief block points to Ships §4; §14 resolve open-Q closed; legibility risk marked resolved.
- **Victory** — §4 repel row is now an emergent rout-cascade in the network, and repels drop the fleet's resolve baseline (the break-will currency).
- **Cannon** — §3 gains the enemy spawn **safe launch zone** (accelerate fast, can't be hit — anti spawn-camp), rendered as a **displayed dead zone** in the AoR coverage.

### Next
Build phase — pieces & enclosure (queue #1); GDD (selectively) + Cannon.

---

## SESSION: 2026-08-29 (cont. 4) — Pre-Build audit; mini-games captured as a first-class pillar
Jack: before Build, a brutally-honest audit — anything left to design in cannons/towers vs ships/troops? are all non-GDD docs aligned, no contradictions? have we hit every part that needs design (not numbers yet)? Plus: don't forget the **mini-games** — a MAJOR part, the "candy-crush."

### Audit verdict (5 non-GDD docs I have: Why, Fleet_Memory, Cannon, Ships, Victory)
- **Cannons/towers vs ships/troops — COVERAGE COMPLETE.** Counter-Web (Ships §12) + locked shortlist (Cannon §11): every enemy threat-angle has a defender answer, every kept lever is stressed — no orphans, nothing uncovered. Watch-item: Saturation's breadth depends on wide formations staying common (open air-density number).
- **Two contradictions found & FIXED this turn:**
  1. **Pair-down status** — Cannon §11 had it locked ("Decisions — all three settled") while Cannon §13 and Ships §13 still called it "the next joint session, nothing committed." Reconciled both §13s → LOCKED (8 cannons, 7 towers); remaining = campaign staging, not a cull. (Cannon §13's other stale open-Qs — multi-target family, control clusters, domain-switch weight, "unvalidated until bestiary" — also marked resolved/validated; falloff feel kept as a legit prototype item.)
  2. **Fleet_Memory win-condition seam** still pointed to "GDD/Cannon"; repointed to the **Victory doc**.
  Otherwise aligned: resolve reconciled last turn (Fleet_Memory/Victory ↔ Ships §4), flagship authoritative in Ships §4, win-condition in Victory.
- **Design-layer work remaining** (numbers are the NEXT layer, deferred): Build, unified Fight, terrain/theater (Layer A), Stonwryt economy/meta, campaign layout/mind-sequencing (Why-critical), boss set-pieces, mini-games (new/major) + the Mimic-mechanic choice + fog/searching-fire. See the queue above.

### Mini-games — captured, not yet designed
Recorded as a supporting law in the Why (§4) and as a full design brief above (see MINI-GAMES). Key call: they're built FROM the phases, so they're sequenced AFTER Build + Fight; a dedicated module doc gets created when we design them. I can spin up that doc stub now if you'd rather it have a home immediately — say the word.

### ⚠ GAP — Campaign doc not provided
The alignment audit is complete for the 5 docs I have, but **`Rivenkeep_Campaign.html` wasn't uploaded**, so I couldn't verify its alignment or whether its board-layout / mind-sequencing design is actually complete — and per the Why that layout is where the north star is won or lost. **Upload it and I'll fold it into the audit.**

### Next
Build phase — pieces & enclosure (queue #1); GDD (selectively) + Cannon. (And the Campaign doc whenever you want the audit closed out.)

---

### GDD UNIFYING PASS — status & cull checklist (started 2026-08-29 · CULL DONE 2026-08-30)
The GDD was unified against the module docs in stages. **The deep cull + summarise-and-link is now DONE (v6.4.0, 2026-08-30 — see SESSION cont. 6).** GDD is 4,212 lines (from 4,745); everything removed is preserved verbatim in `Rivenkeep_GDD_Removed.html` v1.0.0.
**DONE this turn (safe — nothing lost):** a **Module Documents** section at the top of the GDD (same-directory HTML links to all 7 docs + a supersession map: which doc owns what, what it supersedes here); a banner on the Daily-Challenges section pointing the drill design to the new Mini-Games doc; and the rule, stated in the GDD, that where a module doc disagrees the module doc wins and the GDD is the stale copy until extraction.
**DONE 2026-08-30 (the plan below was executed exactly — extracted sections became short GDD-level summaries linking to the owning doc; designed-out content removed; both archived verbatim):**
- **REMOVE (designed out — contradicts the docs):** the old **"tap a ship to focus fire" targeting** everywhere it appears — the Fight-phase section, the tutorial section, and the Daily-Challenges "Focus Fire" table row (grep `tap a ship to focus fire` and `Focus Fire`; the earlier line numbers shifted when the module-doc reference map was inserted at the top). It is replaced by auto-fire + target-personality + fire-control (Cannon §6 explicitly forbids a 4th live verb). Also scan Enemies / Boss / Victory&Defeat / Cannon-Health for any pre-module-doc morale, win-condition, or targeting text now contradicted by Ships §4 / Victory / Cannon.
- **EXTRACT then link (aligned detail the docs now own):** Fight Phase (1289) → Cannon/Fleet_Memory/Victory; Enemies (1237) + Boss Mechanics (1266) → Ships + Campaign; Cannon Health (1179) + Deploy (1130) → Cannon; Victory & Defeat (1713) + Star System (2370) → Victory; Fog of War (621) → Cannon §5; Daily-Challenges leaderboards → Victory and streaks/rewards → economy; Design Philosophy (403) + Game Theory (350) → The Why.
- **KEEP in the GDD (high-level guide + not-yet-owned):** Game Overview, terrain/map/DMZ/theaters (Layer A — no doc yet), Build phase / pieces / wind (queue #1 — no doc yet), the 190-battle parameter spreadsheet (Campaign references it), monetization, AI-enhanced, production standards, tutorial, UX / timing / audio / visual.
- **Sequence:** this is Jack's "truly unifying pass"; *extracting* the aligned detail into the docs is the step AFTER the cull (his plan), leaving the GDD as the overall-guidance starting place.

---

## SESSION: 2026-08-29 (cont. 5) — Campaign audit closed; Mini-Games doc started; GDD unifying pass begun
- **Campaign audit CLOSED.** `Rivenkeep_Campaign.html` read and verified ALIGNED — no substantive contradictions (its §3 already defers difficulty to the module docs; it uses the blind-mind model, the locked cast, enclosure-as-tradeoff, boss = max-intensity promoted flagship). Only needed a version-ref sync → v2.0.1. Finding: the campaign FRAMEWORK is designed; the only remaining piece is the 190-battle generator regen (a later/data-gen item), not new design.
- **Mini-Games doc STARTED** — `Rivenkeep_MiniGames.html` (v0.1.0 brief), seeded from the GDD's Skill-Building Game Packs. Jack's vision (candy-crush skill on-ramp, zero downside, endless replay) + the 4-rung ladder (phase-parts → full phase → two phases → full run) + the 7 GDD packs mapped onto the rungs + two flagged decisions for the full pass: the **no-downside reframe** (the GDD's "complete-or-lose" contradicts zero-downside → go progress-only) and **systematise the ladder** (the packs don't yet cleanly hit all four rungs). Concerns separated: drills = Mini-Games doc; leaderboards → Victory; streaks/rewards/Stonwryt → economy.
- **GDD unifying pass BEGUN** — reference architecture + mini-games banner added; deep cull staged (checklist above).

### ⚠ CHAT LENGTH — recommend a fresh chat before the deep GDD cull
This conversation is very long. The deep GDD cull/extraction is a big, careful, multi-section job on a 4,745-line doc where mis-cutting loses aligned content — the one thing Jack said must not happen. Strongly recommend doing it in a FRESH chat: upload the journal + the GDD + the module docs; the GDD's new module-doc map + the cull checklist carry the plan forward.

### Next
Either (a) the deep GDD cull (fresh chat, per above) or (b) the Build phase — pieces & enclosure (queue #1). Your call.


---

## SESSION: 2026-08-30 — GDD deep cull + summarise-and-link executed (v6.3.0 → v6.4.0); Removed-Content Archive created
Fresh chat, as cont. 5 recommended. Did the one-pass job on the GDD: reshaped it into the **starting-place hub** — designed-out content removed, module-owned detail replaced by short GDD-level summaries that link to the owning doc (cited by section, e.g. "Cannon §6", "Victory §2"), everything else kept in full. **Nothing was rewritten or lost:** every removed block is saved VERBATIM in the new **`Rivenkeep_GDD_Removed.html` (v1.0.0)**, tagged `OWNED BY <doc>` (extracted) or `DESIGNED OUT` (superseded), with a top index. GDD 4,745 → 4,212 lines. Module docs untouched — they were already right, and I trusted them over the GDD throughout.

### What moved where
| GDD section (old) | Action | Now owned by / status |
|---|---|---|
| Game Theory & Player Psychology | extract → link | The Why (⚠ applied-psychology catalog only in the archive until folded into The Why) |
| Design Philosophy | extract → link | The Why §4–§5 |
| Fog of War | extract → link | Cannon §5 |
| Deploy Phase (detail) | extract → link | Cannon §6/§8 (⚠ deploy numbers only in the archive until they migrate to the Cannon doc) |
| Cannon Health & Performance | extract → link | Cannon §8 (+ old "no carry between campaigns / reset 100%" line **designed out** by Victory §7) |
| Enemies | extract → link | Ships §5–§8 + Campaign §5 (old flat roster kept in archive as a reconciliation seed) |
| Boss Mechanics | extract → link | Ships §4 + Campaign |
| Fight Phase | extract → link (mixed) | Cannon §5–§6 / Fleet Memory / Ships / Victory §4–§6 — designed-out sub-parts (three firing modes, tap-target prompt, roll-in-place, staging-can-be-hit, boss-retreat) archived. **Last Garrison KEPT in the GDD** (no doc owns it). |
| Victory & Defeat | extract → link | Victory §2 |
| Star System + Star Earning / Battle Score | extract → link | Victory §2 (per-lever threshold tables + worked examples in archive) |
| "tap a ship to focus fire" targeting — Controls para, Tutorial video, Mobile-UX camera para, a Phase-Timing flow-note | **remove** | designed out → auto-fire + 3 verbs (Cannon §5–§6) |
| Stonwryt "Focus Fire" purchase row | **remove** | designed out (no manual focus-fire) |
| Audio cues for targeting inputs (×3) | **remove** | designed out |
| Glossary `directed_fire`, `touch_lock` (+ their dangling index entries) | **remove** | designed out; `auto_fire` / `hold_fire` **redefined** (kept, new meaning), `crazy_ivan` reworded (Ships trait) |

### Kept whole (cross-link banner added, NOT extracted)
- **Difficulty Layers & Combination Matrix** (the 5-layer matrix + 190-battle generator) — kept; added a banner pointing the difficulty *model* to Campaign §3–§4. The matrix reads as treadmill-clean (its one stat-mention explicitly says "skill, not stats"). Full extraction is a later option.
- **Unit & Structure Statistics** — kept; added a ⚠ stale-roster banner (old flat roster + first-pass numbers; authoritative roster now Ships §5–§8 / Campaign §5, combat model Cannon §5–§6/§8 + Victory). This is the GDD's central numbers anchor with no replacement yet — the main "kept but known-stale" item.

### Flags for Jack (the honest rundown)
- **Numbers now live only in the archive.** Deploy counts / slot-earning / type-limits, the cannon-health curve + lock-in windows, star per-lever thresholds — the *models* are owned by the docs but the **numbers were never physically moved into them**, so post-cull they exist only in `Rivenkeep_GDD_Removed.html`. Trivial to reinstate to the GDD if you'd rather keep them visible there; the right long-term home is each module doc.
- **Same for the psychology catalog** (flow, loss-aversion, variable-ratio, the four loops, anti-frustration table) — The Why owns the *rationale*, not this applied catalog. Archive-only until folded in.
- **Transparency:** the cont-5 checklist guessed the "Focus Fire" line was a Daily-Challenges row; it was actually a **Stonwryt spending row**. Still designed out, still removed — just noting the checklist's line reference was off.
- **4 supersessions confirmed (docs right, GDD was stale), all recorded in the archive:** ship rollover → Victory §4 retreat-to-spawn + smarter re-emerge; between-campaign cannon carry → Victory §7 (3 best carry); spawn staging "can be hit" → Ships §4 safe-launch-zone (cannot); manual targeting → Cannon §5–§6 auto-fire + 3 verbs. **No case where a doc looked *wrong* rather than *stale*** — nothing flagged for redesign.
- **Anchors + glossary integrity checked:** all in-page links whose targets sat inside extracted sections were re-declared in the summaries (`#cannons`, `#ships`, `#ship-spawn`, `#transport`, `#bombers`, `#troops`, `#battle-score`, etc.); the glossary's category/section maps were cleaned of the deleted terms so the tap-to-expand has no dead lookups. Pre-existing benign `<div>` −1 imbalance left as-is (not introduced by this pass).

### Versions
- **GDD → v6.4.0** (paired-down hub). **New: `Rivenkeep_GDD_Removed.html` v1.0.0** (verbatim archive, house style, badged + indexed). Module docs unchanged (v2.0.1; Mini-Games v0.1.0).

### Next
Two clean options: **(a)** the **deeper extraction pass** — pull each still-kept-but-owned detail *into* its module doc and migrate the archived numbers into the docs (the direction-of-travel goal), or **(b)** **Build phase — pieces & enclosure (queue #1)**, the higher-priority design work. The GDD is the clean starting place either way.


---

## SESSION: 2026-08-30 (cont. 7) — Deeper extraction pass: numbers → owning docs, psychology → The Why, "What Makes Special" rewritten
Same-day continuation, fresh chat (Jack heading out — ran the whole job autonomously in one turn). Executed the previous session's **Next-(a)**: moved the archive-only numbers into their owning docs, gave the applied-psychology catalog a permanent home in **The Why**, rewrote the GDD's identity section to current design, and moved the obsolete flat-roster stat tables out of the GDD into the archive. **Found and fixed a live doc-vs-doc contradiction** on the way (below). Verified structurally (tag balance, byte-fidelity on every migrated block, residual greps); no browser render available.

### ⚠ Live contradiction found and fixed (the headline)
**Cannon §8 said "a new campaign resets everyone to 100%"** — directly contradicting **Victory §7** ("the three best cannons carry across campaigns"). This was **not** GDD-vs-doc staleness; it was **two current module docs disagreeing.** Victory §7 owns between-campaign carry, so **Cannon §8 was reconciled to it** (within a campaign ≥100% carries; at a boundary everyone resets to 100% *except* the three best the player carries forward). The "reset to 100%" line had propagated to three places (archive, the GDD Cannon-Health summary, and the live Cannon doc); the GDD summary already flagged it, but the Cannon doc itself still carried it. Lesson: cull-time flags catch the GDD copy, not sibling docs — check the owning doc directly.

### What moved where
| Content | From | To (canonical) | Validated? |
|---|---|---|---|
| Applied-psychology catalog (flow, loss-aversion, variable-ratio, near-miss, Zeigarnik, endowment/SDT, four loops, anti-frustration table) | archive (old Game Theory §) | **The Why §7** (new section; Commitment → §8) | ~95% valid; fixed 2 designed-out bits (2-finger-targeting row → auto-fire + 3 verbs; "tick of targeting" → "tick of fire") |
| Cannon health/nurture numbers (rebuild +50%, enclosure +8/6/4 & +6/4/1, two lock-in windows, move-distance table 0→+5%…9+→+0%, 150%/200% breakpoints, health-bar display, carry rules) | archive (Cannon Health §) | **Cannon §8** ("The quantification" subsection) | model already in §8; numbers additive; carry reconciled to Victory §7 |
| Star per-lever thresholds (Ships any/60/90/100 %, Cannon 1+/majority/all≥100/all≥125 %, Area any/35/50/85 %), hidden ★★★! rule, adaptive tuning, 0★ pacifist egg, worked examples | archive (Star System + Star Earning §) | **Victory §2** ("The star thresholds" subsection) | model already in §2; additive; consistent |
| Obsolete cannon table (Scatter/Long/Chain/Lightning/Doom/Mirror/Mortar/Healing), old flat-roster ship + boss tables, Balance Relationships prose, Lightning/Chain balance questions | **GDD** Unit-Statistics § | **archive** (new "Superseded" group, badged Obsolete) | obsolete — superseded by the 8×3 cannon lineup + lineage×axis roster |

### What was NOT moved, and why (honest scope)
- **Deploy cannon-economy numbers** (count / slot-earning / type-limit formulas, carousel UX) — **left in the archive.** No module doc owns the Deploy economy yet; forcing them into Cannon §8 (nurture) or Campaign would be wrong. Flagged in the GDD Deploy pointer + archive as "awaiting a home in the numbers pass." **The one genuinely homeless number-set.**
- **Two early-game flow watch-items** (thin early Deploy, early Fight passivity) — **kept live in the GDD** Unit-Stats as playtest tracking. Didn't spin up a Campaign-doc edit for two notes.
- **Base-unit framework** (Wall Block HP 100, Standard Cannon Dmg 25, tick = 0.5 s, derive-from-base methodology) — **kept in the GDD** as balance methodology, not roster data. Renamed the "Warship Damage" row → "Baseline Enemy Damage" (Warship-as-named-unit is old roster) with a caveat.
- **Full line-by-line reconciliation of every extracted section into its doc** — NOT done. The docs already hold the *models*; the concrete archive-only content was numbers + the psych catalog, which is what got migrated. Remaining archive "Owned by" entries are old GDD prose whose canonical model already lives in the doc — annotated ("migrated" notes), not re-migrated.

### "What Makes This Game Special" — rewritten (GDD)
Old 13-item list was pre-cognition-era (led on targeting/Sniper-Duel, flat maps, daily-challenge retention). Rewrote to 13 current items, **identity-first**: #1 the enemy has a mind and the mind is the difficulty; #3 skill-not-luck leaderboards (Battle Score); #4 command by intent / three verbs / no lock-on; #5 enclosure-as-win-and-tradeoff; #9 lineage×axis minds; #11 mini-games on-ramp ("candy-crush"). Kept the still-true pillars (deterministic-fair, castle sacrifice, cannon investment, cognitive rotation, time rollover, monetization-on-trust) and merged nicknames + war-reset + bosses + viral into one endgame closer. Fixed the stale castle-sacrifice numbers; dropped the targeting-centric daily-battles item.

### Other stale bits spotted, left for a future pass (flagged, not fixed)
- **Unlock Timeline** still lists old cannon names ("15★ → Scatter Shot"). Part of the broader roster-rename reconciliation — and the cannon *unlock* model itself may still be pending (Cannon doc §9–§11 still carry "pair down" pills though §13 is locked). Left alone.
- Boss-name lists (Leviathan/Colossus/Sandworm/…/Magma Titan) remain — bosses aren't redesigned yet (STILL-TO-DESIGN), so not obsolete.

### Versions
- **GDD → v6.5.0** · **Archive → v1.1.0** · **The Why → v2.0.2** (new §7 Applied Psychology; Commitment → §8) · **Cannon & Tower → v2.0.2** (§8 numbers + carry reconciliation) · **Victory → v2.0.2** (§2 star thresholds). Fleet Memory / Ships / Campaign unchanged (v2.0.1); Mini-Games v0.1.0. All edited docs tag-balanced; pre-existing GDD `<div>` −1 imbalance (present since v6.3.0) left as-is.

### Next
Direction-of-travel extraction is now largely done for everything with an existing home. Remaining bookkeeping (lower value): give the **Deploy cannon-economy numbers** a home, reconcile the **Unlock Timeline** to the 8×3 lineup, clear the stale **pair-down pills** in Cannon §9–§11. Higher value and still the recommendation: **Build phase — pieces & enclosure (queue #1)**, the biggest core-loop piece with no doc yet.


---

## SESSION: 2026-08-30 (cont. 8) — Build phase DESIGNED + EXTRACTED → `Rivenkeep_Build.html` v1.0.0
Queue #1, the biggest core-loop piece with no doc. Ran a **dream-big → edit-down-against-The-Why** pass on the Build phase (Jack: "this was the strongest part designed"), then extracted it into a new module doc in the house style + web-of-docs. Governed by The Why. Design beat first (full space on the table); doc built once decisions locked.

### The dream-big space, then the edit-down
Put the whole surface up (triage geometry, dual-role walls, C×E interplay, nested enclosures, wall stacking, piece-difficulty reframing, special pieces, storage-as-bank), then cut against The Why.
- **KEEP (already right):** triage, route geometry, the dual-draw + trash/store/spackle economy, the six-step carryover machine, time rollover + Ready, wind + drift-stop, one-finger interaction, gun-protection-via-enclosure.
- **ELEVATE (passed the one test):** (1) **triage geometry** → first-class set-puzzle + the ≥2-solutions law + courtyard-of-coverage; (2) **the wall's four jobs** (enclose/buffer/block/conceal); (3) **the C×E rebuild-tax loop** (ships break walls to tax the next Build; sharper fleet hits the weakest seam → build seam-free, not bigger).
- **CUT:** special/conditional pieces (breaks "no one-off mechanics" + adds load; GDD already forbids); anything making enclosure pure-upside (the turtle, tension #4).

### Jack's rulings this session (all integrated)
- **Fork 1 (nested enclosures) — WITHDRAWN as over-engineered.** Jack's model wins and is simpler: **enclosure stays binary**; defense-in-depth is **physical/emergent** (outer wall shields inner wall + courtyard by being a buffer — more wall to chew, longer troop paths, concealment), never a flood-fill change. **Castles are strong wall** → part of the perimeter (consistent build language + cheaper to enclose). **Standalone walls** exist for troop-block + gun-conceal. **Courtyard of coverage** = every enclosure needs an interior big enough for its defending guns. *(Open: confirm "courtyard" = "the enclosed interior where coverage lives" — my read.)*
- **Fork 2 (wall stacking) → War II.** Partial-stack-within-a-drawn-piece idea logged as a War-II hook (Build §13). Too much for War 1.
- **Fork 3 (piece difficulty) — reframed.** NOT a difficulty lever — an **engagement mechanism woven into the cognition curve**. Piece difficulty is **contextual** (burden in a tight re-plug, a gift across open ground); the decision is matching the drawn hand to the ground; red line = awkward shapes must never be *the* reason a late board is hard.
- **§2 seam → GDD wins, Why catches up.** Build is **low-pressure timed**, not "untimed." Fixed in The Why §2 (→ v2.0.3); Build §2 owns the timer-band rationale (a red line for tuning).
- **Ships-break-walls → rebuild-tax chain** (Jack): ships prioritise walls to deny the rebuild, worst with awkward pieces. Folded in as the C×E mechanism (Build §11). Also resolves "shots lob over walls" vs "target walls first" = targeting priority, not trajectory blocking.
- **Spackle tradeoff** already defined in the GDD (limited supply + auto-clears + no veterancy) — carried in as-is (Build §9), not a seam.

### Build doc structure (14 sections)
What-this-is → Loop&Timer → Six Steps (carryover machine) → Enclosure (flood-fill) → **Triage Geometry** → **The Wall's Jobs** → **Pieces** (draw/fit/cognition-curve) → Economy → Spackle → Wind → **Why Ships Break Walls (C×E)** → Controls → War II Hooks → **Why It Works (north-star check)**. Web-of-docs links out to Cannon/Victory/Ships/Fleet-Memory/Campaign; GDD trends to hub.

### What is NOT done, and why (honest scope)
- **GDD Build-section extraction** (replace the in-GDD Build detail — Controls / Build Phase — Detailed / Spackle / Wall Piece Groups & Tiers / Wind — with a short summary + link, and move the 16-row tier table + the exhaustive piece state-machine into the Build doc) = the **fresh-chat follow-on** with the rest of the deep GDD cull. NOT done here on purpose: don't mis-cut the ~4,200-line GDD mid-long-chat (the thing Jack said must not happen). The Build doc currently *links back* to the GDD for the tier table + edge-case state-machine detail until that pass moves it.
- The Build doc leads with design rationale (house style); a couple of exhaustive implementation specs are summarised with a GDD pointer rather than copied verbatim this pass.

### Versions
- **NEW: `Rivenkeep_Build.html` v1.0.0.** · **The Why → v2.0.3** (§2 low-pressure-timed reconciliation + Build added to companions). GDD unchanged (v6.5.0 — extraction is the follow-on). All other docs unchanged.

### Next
Two clean options: **(a)** the **GDD Build-section extraction** (fresh chat, folded into the broader deep-cull job) — summarise + link the now-owned Build detail, migrate the tier table + state-machine into the Build doc; or **(b)** **queue #2 — the Fight phase as one unified experience** (assemble the three verbs + grid-reading + moment-to-moment, currently scattered across Cannon + Fleet_Memory). Mini-games (queue #6) unlock once Build + Fight are both locked (they're built from the phases).


---

## SESSION: 2026-08-30 (cont. 9) — GDD Build extraction COMPLETED + the 2×2 rule + mini-game note
Jack directed the GDD cull now (not a fresh chat): "all of the build phase information in one location [the Build doc]; anything cut and not transferred → the Removed doc." Done.

### New design decision — the 2×2 minimum enclosure
A courtyard (enclosed area) **must be at least a 2×2** to count as enclosure. A 1×1 pocket — or a 1-wide slot — is **dead space, not a courtyard** ("otherwise it's just a wall"), and does NOT enclose a castle. Concrete reason: a **cannon is 2×2**, so anything smaller can't seat even one gun — it's the physical floor under courtyard-of-coverage (§5). The flood-fill gates ENCLOSED regions by this floor; closes the micro-enclosure cheese. → Build §4 (+ tie in §5).

### Build doc v1.0.0 → v1.1.0 — now the complete owner
Folded in from the GDD (design INFORMATION, all of it): the full **16-row tier table** + the **selection algorithm** (§7); the full **piece state machine** (4 states + invalid-placement / off-viewport frame / no-auto-scroll / full-zone rules) + the **rotation algorithm** + bounding-box table (§12); **wall-block HP** (≥25% repair line) + **castle degradation** 3-strike (§3, as the carryover). Added the 2×2 rule (§4) and strengthened the mini-game + board-audit note (§14). Build doc kept **script-free** (renders clean — Jack confirmed).

### GDD v6.5.0 → v6.6.0 — culled to hub stubs
The three contiguous Build sections (`controls` + `pieces` + `wind`, GDD lines 692–1055) replaced with concise hub stubs that link the Build doc; wall-HP + castle-degradation subsections in the `castlehp` section stubbed to Build §3. **All referenced anchors preserved** (controls, build, spackle, enclosure, rotation, tray-build, pieces, walls, tier-table, wind, castles) so no internal links break. **The 198-shape catalog visual + its `#piece-catalog`/`#piece-display` divs were KEPT** — the generator is shared with the piece-naming system, so pulling it would break naming; the design detail moved, the entangled visual stayed (flagged). Kept in the GDD: Castle-HP halo display, Destroyed Cannon Recovery (→ Cannon §8), Last Garrison. 4,126 → 3,770 lines; section 51/51, div 242/243 (the pre-existing −1, unchanged), scripts 4/4 intact.

### ⚠️ Process note — a regex over-match, caught and fixed
First attempt at the castle-degradation stub used a `.*?</div>\s*</div>` regex (DOTALL) that OVER-MATCHED ~2,350 lines into a `<script>` template literal (the .s box doesn't end in a double `</div>`). Corrupted the GDD (1,410 lines, stray `` `; `` inside a script). Caught it on verification, restored the pristine GDD from uploads, and redid the entire cull with **exact-string replacements only, no regex across HTML**. Lesson logged: never regex-match across HTML block boundaries in these docs — use verbatim exact-string or line-range slicing, and always diff line-count + tag balance after.

### Removed doc v1.1.0 → v1.2.0
Archived the **Deploy Tray Layout + cannon carousel** block verbatim (cut from the GDD Controls section; it's Deploy content, not Build, so it did not go to the Build doc — badged "awaiting a home," Deploy has no owning doc yet). Index + meta updated.

### Versions after cont.9
Build **v1.1.0** · GDD **v6.6.0** · Removed **v1.2.0** · Why v2.0.3 (unchanged). All cross-links resolve; the Build phase is one self-contained doc.

### Next
Queue #2 — **the Fight phase as one unified experience** (assemble the three verbs + grid-reading + moment-to-moment, scattered across Cannon + Fleet_Memory). Mini-games (queue #6) unlock once Build + Fight are both locked — and per cont.9, a lot of the mini-game work lives in Build (the heart). Possible smaller follow-ons if wanted: pull the GDD "Wall Storage" section (1811) into Build §8 too (not in the named-5 scope this pass), and eventually split the piece-catalog generator so the visual can move to the Build doc without breaking naming.


---

## SESSION: 2026-08-30 (cont. 10) — Shape Catalog doc + rotation regression fixed + 2 design ideas logged
Jack: the interactive shape-rotation was missing (a cont.9 regression), and he wants the shape catalog in its own doc with a "rotate all" button. Both done. Plus two new design ideas floated — logged with honest reads below. Principle restated: **the GDD is becoming a series of docs; we cannot lose anything.**

### Regression I introduced (cont.9) — owned + fixed
When I culled the GDD Controls block (cont.9) I removed the **Interactive Rotation Reference** widget and did NOT archive or relocate it — a straight "don't lose anything" violation. The pristine original was safe in uploads, so nothing was permanently lost. Fixed by moving it into the new Shape Catalog doc (as the rotate-all engine). I also re-audited the ENTIRE culled Controls block heading-by-heading: everything is now either in the Build doc or the archive. Second gap found + closed: **Wall Rack Selection & Feedback** — its tap-to-store/trash is in Build §12; the selection-frame + new-vs-old-cannon UX had no home, now archived (Removed v1.3.0).

### NEW DOC — `Rivenkeep_Shape_Catalog.html` v1.0.0
The full 198-shape catalog moved out of the GDD into its own doc (Jack's request). The catalog **generator** (the algorithmic polyomino enumerator + renderer, ~405 lines of self-contained JS, previously GDD lines 3275–3680) moved verbatim, then I added a **rotate-all** layer: a global rotation state applied to every shape's cells before centering (reusing the generator's own `rot90cw`/`norm`/`bbox`), the render wrapped in a re-runnable `renderCatalog()`, and a "↻ Rotate All 90°" button + degree readout. **Verified with node** (v22 present): 198 shapes render, A1…H62 all present, rotates through 0/90/180/270/back with zero errors — done because there's no browser here to eyeball it. Design INFO (tiers, selection algo, taxonomy) stays in Build §7; the naming FEATURE stays in the GDD; both link the new doc. This also resolves the cont.9 "entangled catalog visual" flag — it's no longer entangled, it's its own doc.

### GDD v6.6.0 → v6.7.0
Removed the catalog generator `<script>` (byte-exact match against the pristine block — NOT regex, per the cont.9 lesson). Repointed the `pieces` stub + the Piece-Naming section to link `Rivenkeep_Shape_Catalog.html`; kept the `#piece-catalog` anchor (nav still resolves). Scripts 4→3, `genPolyominoes` gone, section 51/51, div −1 (pre-existing, unchanged). 3,770 → 3,363 lines.

### DESIGN IDEA #1 (off-book, Jack) — AoR-distance reload
**Idea:** a cannon's reload time scales with the distance from the cannon to where its AoR is aimed. Coast cannon firing at the shoreline reloads fast; back-line cannon aimed at the ships' back line reloads slow. Flavor: the gun must "know where it's hitting" (ranging/spotting) before the next volley — not strictly projectile travel time, "something like that." *Status: PROPOSED, not locked. Belongs to the Cannon & Tower doc (not loaded this session) — do not build until that doc is up.*
- **My read — strong upside:** adds a real placement dimension to triage (cover the zone AND be close enough to fire fast), which is exactly difficulty-as-cognition — more interesting placement decisions, no new stat treadmill. Ties beautifully into Build triage geometry (a back-line courtyard trades coverage reach for rate of fire).
- **The one real risk — legibility (The Why §3, §6 tension #3):** a reload time that varies by AoR distance is an invisible stat unless the game SHOWS it. Needs a clear visual (AoR indicator encodes reload, or a legible falloff) or it becomes "why is this gun slow?" — the fairness failure. Also must reconcile with the existing reload/fire-rate stat + veterancy curve (Cannon §8) and the "AoR re-task is a slow costed crawl" rule (Why §2). Open question to resolve before locking: **how does the player see the distance→reload relationship?**
- **cont.10 refinement (Jack) — the legibility answer:** the distance shows in the projectile **arc**. A distant AoR = a **higher, slower-flying** arc; a near AoR = a **flatter, faster** one. The arc is diegetic and readable, so the reload/cadence difference is *visible*, not a hidden stat — this resolves the main risk I flagged. Remaining nuance for the Cannon doc: does the next volley literally wait on arc flight time (fully diegetic), or is reload a stat the arc merely *signals* (Jack's "something like that")? Either works; the arc carries the legibility.

### DESIGN IDEA #2 (gut check, Jack) — one deterministic seed per battle
**Idea:** one RNG seed per battle drives ALL "randomness" — which wall piece shows, ship spawn order, what makes a ship turn back, etc. Because the seed is fixed, the battle is fully reproducible and **always fair**; RNG can be used freely as a design/simplification tool while staying deterministic. Jack is fine with walkthroughs existing ("sometimes you just get stuck").
- **My read — this is excellent and it's the mechanical backbone of the determinism pillar.** It's the engine that makes the Build doc's already-stated "slot-machine *feel* over a fully deterministic *outcome*" literally true, and it resolves foundational tension #1 (determinism vs renewable strategy) and — cleanly — tension #2 (retry-can-brute-force): with a fixed seed, retry gives the *identical* battle, so there's no luck to reroll; you can only solve it better. Strong candidate to become a first-principle in **The Why**.
- **The one fork to decide before it goes in The Why:** is the seed **fixed per level** (every attempt at Level N is the identical puzzle — puzzle-game identity, walkthroughs work, hand-tunable boards) or **fresh per attempt** (roguelike-ish, new each play)? Jack's "always fair + walkthroughs OK + one seed per battle" language points hard at **fixed-per-level**, and that's my recommendation — it's the strongest fit for "deterministic thinking puzzle." Sub-decision: does the offered piece sequence depend only on the seed, or on seed + play (trashing/storing advancing the stream)? *Status: gut-check; NOT yet written into The Why — confirm the fork first, then it likely becomes a Why first-principle + a note across Build §7/§8 (draws), Ships (spawn order), Fleet Memory (turn-back/resolve).*

### Versions after cont.10
Shape Catalog **v1.0.0 (NEW)** · GDD **v6.7.0** · Removed **v1.3.0** · Build v1.1.0 · Why v2.0.3.

### Next
Unchanged: queue #2 the unified Fight phase. Before/around it, two decisions to lock: the **seed fork** (fixed-per-level vs per-attempt — likely a Why first-principle) and, when the Cannon doc is up, the **AoR-distance reload** (with its legibility answer). Both logged above.


### cont.10 (continued) — consistency passes + the seed/RNG model
Follow-on work after the Shape Catalog (all in cont.10):
- **Shape Catalog rotate-all button made sticky** (pins below the nav while scrolling the catalog; node-reverified).
- **AoR-distance reload — legibility answer (Cannon doc's domain, logged not built):** a cannon's reload scales with distance to its aimed AoR; the difference is shown by the **projectile arc** — distant AoR = higher + slower arc, near = flatter + faster — so it's visible, not a hidden stat.
- **Two full cross-document consistency passes over all 11 docs.** No data/explanation contradictions (198 pieces / 190 battles / 16 tiers / 8 groups / 4×4 / 5 layers all agree). Fixes: (a) **de-pinned every cross-reference version** — companion lists, "Rides Fleet Memory v2.0.0", "Companion to the Cannon & Tower doc (v2.0.x)", stale "Module of the GDD (v6.x)" — every doc now names companions with no version numbers (Jack's rule), robust to future bumps; (b) restored the GDD's dangling `#battles` anchor (a cont.9 cull removed it) and repointed the pre-existing `#waterways` links to `#map`; (c) Cannon doc "pieces are 2×2" → **"cannons are 2×2"** (3 refs, §3 grouping rule); (d) added the "Governed by The Why" meta tag to the 3 module docs missing it → all 8 module docs uniform. GDD/Removed keep their versioned `<title>` (Jack: correct). Removed-archive dangling links are expected verbatim-snippet artifacts; the GDD's −1 div is the known-benign quirk. Meta/text hygiene → no version bumps except The Why (below).
- **SEED MODEL — locked as a Why first-principle.** One fixed seed per battle drives all randomness; restart re-seeds identically → the same battle every attempt (retry = solve it better, never reroll); the 190 seeds are spread far apart so each battle is a distinct problem. Refined into a **multi-stream architecture**: the one seed feeds separate, independent RNG streams — **piece draw / fleet / a general stream** — decorrelated (piece luck can't perturb the fleet) but all reproducible from the seed. Sub-fork resolved: the **piece stream is play-consumed** (seed + play) — identical play deals identical pieces; trashing pulls the next from the fixed sequence (a costed deterministic lever, not a luck-reroll). Ships + Fleet Memory already encoded this ("deterministic policy over (seed + observation history)"; "on replay the seed resets and the fleet forgets"). Captured in **The Why v2.0.3 → v2.0.5** (seed pillar, §3) and **Build v1.1.0 → v1.1.1** (§7 draw box: own seeded stream, consumed as you draw + consolidated a duplicated "deterministic-fair" box). Full stream **topology** (stream count, derivation, the general stream's scope) flagged for the **SDD** when next worked.


## SESSION: 2026-08-31 (cont. 11) — Unified Fight phase designed → `Rivenkeep_Fight.html` v1.0.0 (queue #2)
Next in the STILL-TO-DESIGN queue after Build. Fresh chat; uploaded journal + the 5 Fight-relevant docs (Why, Cannons, Fleet Memory, Ships, Victory).
- **Architecture call (Jack ruled up front):** the Fight becomes its **own module doc** that **references** the others and owns **only the connective tissue** — NOT the verb mechanics (those stay in Cannon §6). Parallel to how Build got its own doc, but lighter: no stubbing-out of the source docs, just reverse cross-links.
- **Created `Rivenkeep_Fight.html` v1.0.0** — 10 sections, house web-of-docs style, governed by The Why, companions by name (no version pins). The design spine: *the Fight is the **reveal of a committed plan**, read through a legible-but-blind mind, nudged by three costed verbs, where the scarce resource is **attention** not actions, and the one live skill is **timing a single withheld signal**.* The four un-owned things it now owns:
  1. **Sortie tempo** (§3) — the beat structure (3-2-1 → assembly window → first contact → steady watch → the one big call → maybe-correction → withdrawal read). Two *act*-beats, the rest *read*-beats; that ratio IS the anti-plate-spinning guarantee, now a checkable red line.
  2. **The grid-read** (§4) — every on-screen layer (your AoR gradients/health/ammo-felt; their two fogs, exposure glint, fear haze, decay; the motion signatures + flag icon + crazy-Ivan) composed into ONE picture via **one-hard-rail + soft-haze**. Restates the bad-load red line: if the read becomes "hold a hundred cells," the fix is always more summarising, never more to track. This is where Fleet Memory's stacked-fog risk actually bites.
  3. **The attention economy** (§5) — the doc's sharpest original claim: auto-fire makes actions cheap + the verbs make them rare, so **attention (where you look) is the bottleneck**. Reframes existing choices as attention decisions — "no morale bar" (tells read *peripherally* as motion), idle-gun sweep (board alive without demanding attention), the 3-verb ceiling (a fourth verb adds a thing the *eye* must track). Design job: exactly TWO events seize the eye (valuable target committing into a core; a flank going wrong); everything else glanceable.
  4. **Reading the ending** (§8) — Victory owns Held/Repel/Breakthrough mechanics; Fight owns *seeing which is coming* (fire slackening = held; signatures cascading aft = repel tipping; a Committed hull driving a seam = breakthrough imminent, correct NOW). The ending is the debug loop's "read why" step.
- **Reverse cross-links (web stays bidirectional):** Cannons §6 got a "mechanics here, experience there" box → **v2.0.3**; Fleet Memory's holding-fire pillar points to Fight → **v2.0.2**; Victory §4 points to Fight → **v2.0.3**. All tag-balanced, verified.
- **Incidental fix:** the uploaded Cannons copy still carried **version pins** in its companion list ("Fleet Memory (v2.0.1)"…) — the cont.10 de-pin hadn't landed on it (stale upload vs a de-pinned canonical elsewhere is unresolved — FLAGGED to Jack). De-pinned it to names in this pass per the locked rule.
- **ONE OPEN FORK — Jack to rule (touches Cannon §6, which is loaded, but the ruling is his):** **domain-switch legibility.** Cannon §6's late third-domain "longer path" makes the reload meter sometimes count *up* for a "switch to Air" tap — the too-clever rule the Grok mockup already defaulted away from. **(A)** keep the reversal (punishes indecision; leans hard on the slider to sell direction) vs **(B)** simplify to continue-the-count (reads instantly; loses "flip-flopping is expensive"). Fight-legibility read favours **B**, or A only if the slider makes direction unmistakable. Carried as an open seam in Fight §10; Cannons NOT edited on this pending Jack's call.
- **cont.11 (continued) — Jack's rulings applied, same session.** (1) **Domain-switch fork CLOSED by removing the situation:** the third-domain-mid-reload rule is tabled; a switch only cancels (meter reverses to old) or plays through (meter runs to new) — direction now unambiguous, glance-legibility hazard gone. Cannon §6-B bullet + UI-concept line + honest-flag rewritten; **Cannons v2.0.2→v2.0.4** (the v2.0.3 I presented last turn was rebased onto Jack's freshly re-uploaded canonical v2.0.2, which confirmed the cont.10 de-pin never persisted — so v2.0.4 subsumes de-pin + §6 Fight box + third-domain-drop + §5 reveal render in one clean file). (2) **Two fogs given concrete visual languages (Jack):** BOARD FOG = **opacity** — opaque where blind; a reveal opens a **transparent-centre / opaque-edge circle** that holds for a **visible-timer** then **collapses inward** over a second timer; **fog-theaters only**. MIND FOG = **saturation** — the player's own fort sits in **twilight** (desaturated) where the fleet hasn't confirmed it and jumps to **noon** (full colour) as the fleet opens LOS or lands a hit ("twilight vs noon-day sun"). Opacity vs saturation = distinct eye-channels, so the two never conflate (meets Fleet Memory's distinct-languages requirement by construction). (3) **Always-visible fairness constants:** spawn points + their safe launch zones, and all **DMZ / area-denial grids**, stay fully visible + full-colour every sortie, exempt from both fogs. Captured: Cannon §5 (render + constants), Fleet Memory §8 (register-1 render → saturation; two-fog line → settled) **→ v2.0.3**, Fight §4/§7/§10 **→ v1.0.1**. All tag-balanced, script-free, verified. Victory unchanged (its v2.0.3 §4 cross-link from earlier this session stands).
- **cont.11 — AoR three-state render + full Fight completeness audit** *(Fight v1.0.2→v1.1.0, the latest pass this session).* (A) **AoR RENDER finalised to THREE states** (Jack): resting = grid-square OUTLINE (extent only); firing-but-unselected = outline + bright CORE + OUTER BOUNDARY RING (reads "zone is hot, here's its core + reach" live, so a fringe-miss is fair without a tap); selected/tapped = FULL centre-to-edge gradient. Closes the prior "should a firing group show its gradient?" watch-item — the firing state serves live fringe-fairness, the selected state gives full precision, neither floods the colour channel the fogs need. Cannon §4 → **v2.0.6** (also corrected a stale §13 status line: Build+Fight now have owning docs). Fight §4 mirrors it. (B) **FULL COMPLETENESS PASS over the Fight doc** (Jack asked: make sure everything is designed; fix small, queue big). Nothing was a stub — the audit was about missing TOPICS. FIXED inline (Fight → **v1.1.0**): (1) **the input grammar + what's-locked** (§6, new subsection — was genuinely un-owned connective tissue): tap=select+highlight AoR, hold-drag=re-task the selected group, domain-slider + fire-control toggle on the selected group, quick-drag=pan / pinch=zoom; the quick-drag-pan vs hold-drag-retask distinction must stay unambiguous (same as Build's pan-vs-move); and LOCKED in the Fight = no placing cannons/walls, no group form/split/merge, no tower re-stack (all Build/Deploy) — the hard boundary that keeps the Fight a reading phase. (2) **choreography fragility** (§6): a sniped Rally Flag slows your crawl → a timed maneuver arrives late; protecting the tower that underwrites your plan is part of the plan (the fleet attacking your TIMING — answered in Deploy, not a scramble). (3) **battle-level terminal read** (§8): above the sortie endings, you feel the capped pool DRAINING → Last Stand (enclose freely, pressure off); Retreat/Annihilation read off the same tells at scale; the moment-to-moment has two horizons (is this wave breaking / is the fleet out of will-or-hulls). (4) **AoR shrinks when a group loses a cannon** (§4) — a spatial read of damage on top of the health colour. (5) **viewport concern** (§5): 64×48 board > screen, so an off-screen decision-critical event (breaking flank / committing target) needs a legible off-screen cue — target stated. QUEUED as bigger gaps (Fight §10 + queue above): **pause/time-control** (the one big undecided — architecture implies continuous real-time but it's unstated; needs a ruling); **the un-owned DEPLOY phase** (new queue item #8, parallel to Build/Fight); **multi-group serial-command throughput** (spacing law must hold per-commander, not just per-group); **the feedback/audio vocabulary** (polish, later). Cannons v2.0.6, Fight v1.1.0 — both tag-balanced, script-free, verified. Fleet Memory (v2.0.4) + Victory (v2.0.3) unchanged this pass.
- **cont.11 — planned-command reframe + concrete fogs + breach sun-ray** *(Fight v1.0.1→v1.0.2; this happened earlier in the session than the completeness pass above — versions disambiguate order).* (1) **BIG REFRAME — the live verbs are a PLANNED COMMAND LANGUAGE, not just corrections.** Jack: because the battle is deterministic, threats arrive on a known, SPACED schedule, so a single group can be PLANNED to walk a route — e.g. north SEA (ships) → east LAND (troops) → north AIR (bombers) — re-tasking its AoR and switching its domain on cue. That is direct command (conducting a learned score), the opposite of plate-spinning. Corrected my v1.0.0 over-restriction ("constant re-tasking = arcade drift" was WRONG). New distinction: **command = planned/sequential/spaced/foreknown; plate-spinning = forced/simultaneous/surprise under speed.** Frequency is NOT the test. The arcade red line RELOCATED to a board/wave-design law: multi-threat sequences must be spaced so a planned single-group line (crawl+reload) physically fits the gaps — *if a board forces two costed moves at once, the BOARD failed, not the player.* (Sibling to the ≥2-solutions law; owned by Campaign/Build triage.) Also reconciled with attention economy: planned maneuvers are self-scheduled = cheap attention; reactive surprises = dear attention (same line viewed twice). Fight §2/§3/§5/§6 rewritten → **v1.0.2**. (2) **AoR render:** resting = light grid-square OUTLINE (coverage extent, low visual weight); **tap a group → its AoR highlights** into the full centre-to-edge colour gradient over water/fog. Keeps the colour channel for the fogs; solves the 3-colour-channel clutter seam I flagged. Watch-item: whether an actively-firing group should surface its gradient live for fringe-miss fairness (lean yes-while-firing). Cannon §4 → **v2.0.5**. (3) **Health bars:** in the FIGHT, a cannon shows NO bar until first hit; damage brings bar+colours in (attention-economy win). Build/Deploy keep always-on bar+%. Cannon §8 phase-split → v2.0.5. (4) **Breach SUN-RAY (Jack's image):** a troop breaking a wall instantly lights the sightline to the next wall "like a sun ray" (mind-fog noon shaft into a twilight interior) — the breach-reveals-next-layer render; AND the fort's overall saturation doubles as an at-a-glance battle-health gauge (mostly-twilight = still hidden; creeping-noon = being found). Fleet Memory §8 → **v2.0.4**; Fight §4. All tag-balanced, script-free, verified.
- **Honest status:** the Fight design is a complete first cut of the connective layer; nearly all its felt claims are **specified targets awaiting prototype** (does watching feel like commanding? is the two-fog read tense or noisy? how many groups before attention saturates?) — stated precisely per design-first, not left blank. **Parked, noted-not-built:** AoR-distance reload (belongs to Cannon; would live in the Fight grid-read via the arc). **NEXT in queue:** #3 terrain/theater (Layer A), or #4 Stonwryt economy — Jack's pick. Mini-games (#6) now unblocked in principle (Build + Fight both have owning docs), though full mini-game design still wants both phases settled.- **cont.11 — pause/replay/auto-AoR/audio rulings** *(Fight v1.1.0→v1.2.0; Cannons v2.0.6→v2.0.7; Victory v2.0.3→v2.0.4; latest pass this session).* Jack closed the queued open questions: (1) **PAUSE — none.** Continuous real-time; the only stop is hiding the app (freezes → 3-2-1 resume); screenshot-then-hide is permitted-but-not-worth-it (not designed for/against). Confirms the continuous-RT reading the architecture was built for. (2) **REPLAY — the Fight is replayable, win OR lose,** as a first-class strategic tool: deterministic, so a replay refines *execution* (time the alpha, start the crawl earlier), and fair by the leaderboard's own logic (same problem + same chance for all; skill = the ceiling reached). Captured in Fight §2 + §10 + Victory §4. The precise mechanic — **Fight-only (keep committed Build+Deploy — my lean) vs full-sortie retry; unlimited/free?; how a replayed result touches Battle Score + the time-bank** — is a real fork, deferred to the Deploy pass (#8) where it couples. (3) **AUTO-AoR + individual command:** the game auto-assigns a sensible default AoR to every cannon/group; the player *nudges* it in Deploy (easy to move), never draws it; command is **per individual group** (no group-of-groups / multi-select). This retires the "multi-group serial-command throughput" worry (individual + light setup + spacing law = comfortable). Captured Cannon §3, Fight §6. (4) **AUDIO/HAPTICS — next layer, constraint set now:** beneficial not a constant drone; **fully playable well with no sound** (legibility visual-first). Recorded in the design canon + Fight §10. (5) **DEPLOY (#8) confirmed as the NEXT session.** All four edited docs tag-balanced, script-free, verified; Fleet Memory (v2.0.4) unchanged this pass.

- **cont.11 — structure/checkpoint clarification** *(Fight v1.2.0→v1.2.1; Victory v2.0.4→v2.0.5).* Jack: **the checkpoint is ALWAYS the battle.** Canonical hierarchy = **BATTLE → waves of sorties → phases (Build→Deploy→Fight)**; the sortie/phase breakups exist for **game pacing and document communication**, not as save points. This **dissolves** last turn's deferred replay fork (Fight-only vs full-sortie + per-phase scoring): there's one checkpoint/replay/scored granularity — the battle. You replay the whole battle (deterministic → re-execute across it better), win or lose; Battle Score already scores the battle, so no special replay-scoring rule. Corrected the framing I'd written at phase/sortie level: Fight §2 (replay pillar → battle-unit), §3 (pause is in-place, distinct from the battle checkpoint), §10 (fork resolved); Victory §4 (replay note → battle-level). Removed the replay item from Deploy(#8)'s parked list — resolved. Design-canon updated with the hierarchy. Docs tag-balanced/verified. Deploy (#8) still the agreed next session.

## SESSION: 2026-09-02 (cont. 12) — Deploy phase designed → `Rivenkeep_Deploy.html` v1.0.0 (queue #8)
Jack: "let's start on the deploy phase." Built the third and final phase-owning doc. Same treatment as Build and Fight: it owns the **lived phase**, references the others, owns none of their mechanics. Uploaded: journal + Why + Cannons & Towers (exactly the Document-Index recommendation).

### What the doc establishes
- **The phase thesis:** *Build decides where you can fight from; Deploy decides what your fort will do without you.* Deploy is the only phase whose entire output is instructions to somebody else — and therefore the **highest-leverage seconds in the game**: a Build mistake costs a wall, a Fight mistake costs a moment, a Deploy mistake is wrong for the whole sortie and only one slow costed verb can reach it. Upgrades the Cannon doc's pillar-3 ("Deploy is the plan, the Fight is the reveal") into the actual structure of the phase.
- **The 6-beat tempo** (sibling to the Fight's sortie tempo), each beat tagged **read** (free) or **act** (costs a slot / a bonus / ground): handover (left-to-right wipe, tray swaps to the cannon carousel) → state read (bars + exact %, new slots, DMZ ghost) → siting → orders → seam read → lock-in. Healthy Deploy = two reads, two-three acts, one read. A Deploy that becomes six rushed acts under a clock has turned into an execution test.
- **The cannon economy — the homeless numbers now have a home.** Adopted from the archive: `start = min(2 + floor(cam/6), 7)`, `max = min(start + sorties + floor(ships/5), 12)` (boss 6/12), slots earned by Fight performance, unfilled slots roll over; carousel (full-width, arrows, progressive edge fade, selectable at any brightness), selection **frame** not halo + swap icon for a11y, cannon trash (slot reopens **next** sortie, so a type change costs one Fight), tap-to-recover before lock-in, invalid guns auto-trashed **visibly**. **This closes the "one genuinely homeless number-set" flag from cont.6/7.**
- **Type limits given a concrete shape:** `per-archetype cap = max(2, ceil(max slots / 3))` — reads as "at most a third of your guns can be the same idea," floor 2 so doubling up is always available. Red line attached: the cap must never be why a board is unbeatable.
- **Placement = three decisions in one gesture** (coverage + grouping + **territory**). Two already-decided rules that had never been connected to a *reason to place a gun*: (a) the DMZ advances after Deploy and **cannons/castles pin it permanently**, so a forward gun is a territorial act; (b) a **fragile grid under a cannon disappears permanently, even if the cannon later moves** — placement is quietly terraforming and widens next sortie's build space. Tabulated forward-vs-enclosed across coverage / territory / survival / nurture: neither dominant, and it re-poses coverage-vs-concentration one layer down (the design's signature).
- **Emergent grouping named as the Build↔Deploy seam — the doc's sharpest original claim.** There is no "create group" button, so command structure is read off fort geometry, which means **enclosure geometry *is* command granularity**: a player who wants Sea here and Air there must *build two separated seats* to hold them. One big courtyard = density + one tower buffing many guns; two small courtyards = independent domains and AoRs. Build's triage puzzle was always a coverage puzzle; it is also a **command-structure** puzzle, authored before the fleet is known. Flagged that no player will infer this — wants a Build drill in Mini-Games.
- **The order card** — Deploy's entire product: 4 fields (AoR / domain / fire-control / tower priority), all pre-filled, all editable, one group at a time. **The three Fight verbs reuse these exact widgets**, so nothing new appears when the countdown ends — only the cost. Deploy therefore *teaches the Fight's whole control surface, unhurried, with no enemy on the board, every sortie.* Also explains the verb budget from the other side: 3 live verbs because 3 live order fields; tower priority is deliberately the set-and-forget fourth. **Do not add a fifth field.**
- **Domain default ruled:** persisting group keeps last sortie's load; a new group takes the domain of the approach its default AoR faces; **Air is never a default** (always a read the player makes).
- **Auto-AoR default rule specified** (the item parked out of cont.11's Fight work): radius from cannon count + archetype AoR contribution; centre offset toward the nearest **uncovered approach corridor**; two clamps (group covers itself; the launch-zone dead hole may not swallow the majority of the zone); if everything is covered, bias to **overlap the weakest seam** — so the default *demonstrates* the overlap cure; deterministic grid-index tie-break (required for replay/leaderboard exactness). **Deploy AoR moves are instant and free** — the crawl is a Fight-only cost — and never touch nurture.
- **Information-state arc:** decision load rises across a battle while uncertainty falls. Sortie 1 = **hypothesis from geometry**; sortie 2+ = **revision**; battle replay = **rehearsal**. States plainly that **Deploy, not the Fight, is the mechanical home of the Edge-of-Tomorrow touchstone** — the Fight is where you learn, Deploy is where the learning is spent. Corollary for Campaign/Build: the ≥2-solutions law needs a **Deploy twin** (a board should admit more than one viable *deployment*, not just one viable wall layout).
- **The Deploy read:** Map View; health bars + exact % fully exposed (opposite of the Fight's quiet board, per the Cannon §8 phase split); **coverage in the same three-state grammar minus the firing state** (all groups resting outlines, selected group full gradient) — no new render vocabulary; **DMZ ghost** (fairness requirement, not convenience — otherwise a forward placement is a hidden trap); **pending-nurture readout on the card** ("+6% enclosed, +3% moved 3") so the enclosure-vs-relocation tradeoff is legible *while being made*; **coverage-holes toggle** (safe here because nothing is moving) with a hard red line — **it shows holes, it must never grade the plan** (no score, no "3 gaps remaining"; a deliberate hole on an approach you read as quiet is often correct).
- **Locked boundaries both ways** + the identity rule: **there is no auto-deploy.** The game defaults *orders* and never *placement* — which is exactly why the defaults can be generous without being a slippery slope.
- **Lock-in ordering ruled:** Lock-In 2 fires **before** the DMZ advance, so nurture reads the fort you built and ordered, not the fort the map bit a second later. Then wipe left-to-right → Map View crossfades to World View on the 3-2-1 animated camera tilt.

### ⚠ THE ONE REAL CONTRADICTION — the Deploy timer (needs Jack's ruling)
The decision log holds two incompatible values and the later one is very likely a table-consistency artifact, not a design decision:
- **20→30s**, set on explicit human factors: *5–8s board recognition + 3–6s per cannon*.
- **12→15s**, normalised later by a consistency sweep to match a phase-timing table — **without re-deriving the human-factors number.** It doesn't survive its own arithmetic: at 7 slots the stated model gives **26–50s**, which 15s does not cover on any reading.

This matters more than a number, because of the phase law the doc establishes: **Deploy is the most dangerous clock in the game** (highest leverage-per-second), so a tight Deploy clock is the closest this design comes to the arcade test The Why §2 forbids. Three models laid out in Deploy §11: **A · load-scaled clock (recommended)** — base recognition + per-slot allowance, same "low-pressure timed" band as Build; **B · untimed — rejected** (breaks the time-bank rollover, lets a battle stall against the 2–5 min target, drops a Zeigarnik hook, and the danger is a *tight* clock not a clock); **C · idle-bounded clock** (extends on each meaningful action) as the fallback if A still bites. Red line either way, word-for-word the sibling of Build's: **if a sortie is ever lost because the player couldn't finish stancing their groups in time, the timer is mistuned for that board.** 12–15s should be treated as void until re-derived.

### Honest flags raised in the doc (not resolved — targets stated)
- **The move tax cuts against the touchstone.** The nurture unmoved-bonus decay literally *taxes the act of folding in a lesson* — direct tension with Edge of Tomorrow, where spending knowledge is the reward. Probably still right (small: a 5-point swing in a 100-point band; and it separates a considered re-site from fidgeting), but the red line is stated: **if players stop re-siting because of the tax, cut it to zero.**
- **A good default can eat the decision.** Guard: the default is *always reasonable, never optimal* — it knows the geometry, it knows nothing about the fleet. Test: **if a never-nudged Deploy clears boards a nudged one clears, the default is too strong.**
- **The accidental fuse** is the real risk emergent grouping creates (place one gun, silently destroy a two-domain plan). Answered by the JOIN/FUSE/NEW preview + merged-AoR preview + towers-including-grayed coverage — needs a prototype check that it's enough.
- **Thin early Deploy** (a long-standing watch item) — Campaign 1 is 2 slots / 1 type / 1 group, so Deploy is a 3-second empty phase for several battles, which teaches the player to skip the phase that carries the sortie. **Proposed answer (needs a Campaign-doc ruling): introduce exactly one order field per early battle** — placement → AoR nudge → domain → fire-control → tower stack — so Deploy is never empty, only small. Introduce→Isolate→Combine applied to Deploy.

### Cannons & Tower doc → v2.0.8 (reverse cross-links + a CSS bug)
Per the web-of-documents rule: §3 grouping (+ the fuse preview), §3 auto-AoR bullet (retargeted from "queue item #8" to the real doc), §3 + §10 tower priority stack, §6 "Set it in Deploy" box (+ the shared-widgets teaching point), §8 Held-position bullet and the unmoved-bonus paragraph (+ the pending-bonus requirement), and the §13 next-documents status line (all three phases now have owning docs; Deploy absorbed the homeless economy numbers). **Also fixed a pre-existing bug I noticed while matching the CSS:** `.s.law` is used by the §3 launch-zone callout but was never defined in the stylesheet, so that box has been rendering unstyled — rule added (green, matching the other variants). Defined in the Deploy doc from the start. Both docs tag-balanced, script-free, zero dangling internal anchors, node-free (no scripts to verify).

### cont.12 (continued) — Jack's six rulings on the Deploy doc → Deploy v1.1.0, Cannons v2.0.9
Jack reviewed the Deploy doc and returned six items. All applied this turn. Two of them opened new blocking queue items (#0, #0b above).

**1 · CANNON ECONOMY VOIDED AND REBUILT (the big one).** Jack: *"Now that we have changed how the ships fight, more ships are needed for each fight than I originally thought. That would also mean more cannons. So I don't think we should keep the cannon economy. We need to rebuild this part."* Correct, and the reason is sharper than "more ships": **the defender's model changed from targeting to allocation.** Under the superseded model the player tapped a ship to focus fire — one hull was a real engagement because engaging it was an *act*. Under AoR coverage, guns auto-fire into a zone and the only lever is where the zones are; that is an allocation problem, and **allocation problems do not exist below a population.** Two ships cannot pose a coverage dilemma; twelve can. Three independent parts of the design converge on it: (a) the coverage-vs-concentration tension (Cannons §3) is only a decision when you *cannot cover everything* — under-population makes every layout correct, which makes none interesting; (b) Fleet Memory's resolve network, fear contagion and cascade tipping fractions are **statistical** mechanics — a cascade across three hulls is not a cascade, and the intensity dial has nothing to act on; (c) enclosure victory + retreat-and-re-emerge + a performance-drained pool means the fleet is **not a stack of HP you grind down — it is a rate of arrival you must survive**, so pressure comes from concurrency, not attrition.
- **The structural finding — one input, four number-sets.** What looked like four independent number sets is one derivation: **simultaneous contacts → cannons needed → courtyards & wall needed → Build/Deploy/Fight timers.** Derivation per link now written into Deploy §2. Two parts worth flagging: **cannon count should be deliberately set *short* of "enough to cover everything" by a designed margin — the under-supply fraction IS the difficulty dial** (a fully-supplied fort has no allocation decision left in it); and **wall demand is a function of the player's chosen command granularity** (perimeter scales as √area, so one big courtyard is cheap perimeter and four small ones are expensive), which is why the wall budget can never be a flat number.
- **The bracket for the sizing session: floor set by allocation, ceiling set by legibility — and the ceiling is the dangerous one.** The Why §6 names legibility-under-load as the single point of failure, and raising ship count loads it directly; it also worsens the known 64×48-board-larger-than-screen problem (Fight §5). **So the sizing session is run against legibility, not difficulty: the right number is the smallest one that makes coverage a genuine allocation problem.**
- **What survives numbers-free** (kept in §2): slots-not-purchases; slots grow across the campaign *and within a battle* by Fight performance (matters *more* at higher counts); unfilled slots roll over; per-archetype type limit as a **fraction** of slots rather than a flat cap; carousel/frame/swap-icon/trash/recover; type change costs a sortie; invalid guns auto-trash visibly.
- **Deliberately NOT invented:** any replacement formula. A fabricated slot formula is worse than an acknowledged hole — it would look settled, get built on, and quietly mis-set the wall budget and all three timers. §2 states the derivation *order* instead, which was the thing actually missing.
- **Consequence surfaced:** the thin-early-game flag is **sharpened, not fixed.** If the mature game needs a crowd for coverage to be a decision, the early game — which cannot open with a crowd, since Introduce→Isolate→Combine forbids it — is a stretch where the core tension structurally does not exist. Proposed answer (needs a Campaign ruling): one new order field per early battle, so allocation arrives with the crowd that creates it.

**2 · THE GROUP OUTLINE (Jack's render spec).** *Each cannon has a colour outline; when two are placed adjacent and form a group, the outline goes around all of them; the single cannon's AoR should also change.* Written up as the canonical grouping render — per-cannon outline around its own 2×2, resolving into **one unbroken perimeter tracing the union of every footprint** the instant a cell-edge is shared. A group is not a label or a menu state, it is a **shape**. Composes exactly as the adjacency rule does (bridging cannon collapses three into one; a bridging tower does the same, grayed or not; a loss redraws the perimeter). **The AoR re-forming at the same instant is the second signal channel** — perimeter + coverage circle moving together makes the grouping event impossible to miss without either channel shouting, and teaches the adjacency rule by demonstration rather than tooltip. **This supersedes my JOIN/FUSE/NEW text labels** — the outline is strictly better: diegetic, no reading, carries the *shape* of the consequence rather than a word for it, and works identically in the Fight where text would be noise. The pre-commit ghost preview becomes almost free (it's just the outline shown early). Canonical spec → **Cannons §3** (owns grouping mechanics); preview → Deploy §4.

**3 · WALLS-BEFORE-CANNONS IS RIGHT — my framing was wrong.** Jack: *"Building walls have always been built before cannons have been placed. You know where the DMZ is, you know where the enemy will be and where it will want to go when you are building the walls. This should be enough information for you to build your walls when you know which cannons you will have."* Accepted — I had treated "you author your command structure before you know the fleet" as a problem when it is a **designed ordering**. The Build-time information set is genuinely sufficient: DMZ line, spawn points (always visible, exempt from both fogs), terrain constraints, therefore where an attacker can come from and where it wants to get to — **plus your own cannon slate**, which is settled before Build opens. You are not guessing, you are *reading the ground*. What you don't know is the fleet's **mind** (which approach it commits to, what it learned, what it's loaded to punish) — exactly the knowledge the Fight teaches and the next Deploy spends. The Build↔Deploy seam (**enclosure geometry IS command granularity**) survives intact as a *feature*; the hand-wringing around it is gone, and the Mini-Games drill is now framed as teaching the highest-value invisible thing in Build, not rescuing the player from an ambush.
- **New requirement this creates (owned by Build):** **Build must display the cannon slate** — slot count and available archetypes — on screen during Build, not only in Deploy. A wall plan seating four guns is a different plan from one seating seven, and the courtyard decision can't be made without knowing which you're building for.

**4 · FRAGILE GROUND IS NOT CURED — corrected.** Jack: *"the fragile ground IS NOT cured. If a cannon is moved, then the fragile ground and DMZ can keep moving."* My §3 claim (lifted from an old GDD decision line, "fragile under cannon = disappears, even if cannon moves") is out. Corrected to **held suppression**: a gun holds the fragile grid stable and pins the DMZ **only while it stands there**; move it or lose it and **both resume**. Better design in two ways beyond being the ruling: it makes the forward gun an **ongoing garrison commitment** rather than a one-time free upgrade (you don't buy ground, you *occupy* it), and — the part I should have caught — **permanent terrain-curing is already the Pioneer's signature** (Ships, the land-lineage deep cut: bridges/stabilises fragile ground, including ground your cannons can't stand on). Giving a cannon the same power would have flattened an enemy's entire identity. Knock-on: **relocation now costs three things at once** — nurture, coverage during the change, and **ground** — so the move tax is no longer carrying the weight alone, and the territorial release is the better disincentive because it's diegetic and visible rather than an accounting penalty. The forward gun's real cost is that it is **pinned by its own job.**

**5 · ALL THREE TIMERS → ONE DEDICATED SESSION, RAMPART AS TOUCHSTONE.** Jack: *"The whole build, deploy, and fight timers all need to be revisited... The original Rampart got the timing right — especially the build phase. This should be its own design session."* Deploy §11 rewritten from "here are three models, A recommended" to a **deferral**: it keeps the contradiction on record (**20→30s** on explicit human factors — 5–8s recognition + 3–6s/cannon — versus **12–15s** normalised later by a consistency sweep that never re-derived the number; at 7 slots the stated model gives 26–50s, so 12–15s is a table artifact and is **void**), states *why* it can't be fixed alone (all three clocks are the tail of the ships→cannons→wall→timers chain, each a different slice of it), records current values as all-open (Build 25→20s +10s sortie 1 / 22s boss; Deploy disputed; Fight 90s — every one set under the old ship counts and old targeting model), keeps the three candidate models as **inputs rather than a recommendation**, and adds **Rampart as the calibration touchstone** — the existence proof that the band is achievable and roughly where it sits: *enough time to close a ring under real pressure, never enough to make it pretty.* Red line unchanged and now doubly important: **if a sortie is ever lost because the player couldn't finish stancing their groups in time, the timer is mistuned for that board.**

**6 · Working agreement amended:** added a locked bullet — **always name the docs to upload for the next piece of work, every turn** (Jack has them all to hand; the constraint is my token budget, not his access), with the corollary to **parse only what's needed** (grep/slice, not whole-file reads). Applied this turn: Ships/Victory/Build read only in the specific sections required (pool sizing, Pioneer, Build timer band).

### cont.12b — Jack's five rulings on Deploy v1.1.0 → Deploy v1.2.0, Build v1.2.0, Cannons v2.1.0

**1 · THE CANNON SLATE WIDGET → owned by BUILD (`Rivenkeep_Build.html` §5, v1.2.0).** Jack: *"The Build Phase should have a widget that displays how many cannons you will have to deploy in the next deploy phase. The second plus sorties, you will see how many cannons you currently have."* Specified with the two readings Jack named, because Build occurs in exactly two situations: **Sortie 1 = a forecast** (nothing is standing, so the slate reads the slot count + available archetypes you *will* have to place — you are building for a fort that doesn't exist yet, and this is the only thing telling you its size); **Sortie 2+ = current holdings** (what is standing and already seated, plus any slots opened by last Fight's performance — the question shifts from "how big a courtyard do I need" to "do my seats still fit, and where does the new gun go"). Kept deliberately thin: a count and the available types, **not** a loadout screen — picking and siting guns stays in Deploy. Written as a **requirement, not a convenience**: a wall plan seating four guns is a different plan from one seating seven, and one-big-courtyard vs two-small is a decision about *command structure* (shared courtyard = one commanded group), so without the slate the highest-value Build decision is being made blind for no reason. Build companion list gained Deploy + Fight.

**2 · POLARITY CORRECTED — it is a placement BONUS, not a move tax.** Jack: *"The move tax is really the opposite. It is a bonus for placing the cannons in the right place in the previous sortie. This is intended to control the player from just being able to freely move the cannons. There is a cost."* I had this backwards and it distorted the whole cluster. Corrected in Deploy §3 (heading, body, the locked-boundaries table) and in Cannons §8. **The friction is intentional design, not a side-effect** — the reasoning now written down: without a cost, guns become units you shuffle every sortie, coverage becomes something you *redraw* rather than *commit to*, and the "Deploy is the plan you live with" premise dissolves. **A gun you can move for free is not sited, it is parked.** Correct reading of the cluster: *holding position is rewarded; moving is permitted and consequential.* Nothing prevents answering a lesson — you just don't collect the good-placement bonus on a gun you had to move, and you hand back the ground it was holding. **My earlier red line ("if players stop re-siting, cut the tax to zero") is WITHDRAWN** — it was arguing against the mechanic's purpose. Only the *magnitude* stays open. Side benefit: the incentive is now visibly right — the player who read the board correctly in sortie 1 is quietly ahead of the player still finding out, which is how a game about reading ground should reward reading ground.

**3 · DEFAULT AoR SIMPLIFIED — "somewhere out there, differentiated from the other AoRs."** Jack's rule replaces my derivation, and it is better. Deploy §6 rewritten: **outward facing** (into the contested ground, the DMZ side — *not* aimed at a corridor, spawn, or predicted lane), **differentiated** (if another group already covers where this would land, push it off — groups **spread rather than stack**), plus radius from cannon count, two sanity clamps (a gun always covers itself; the launch-zone dead hole may not swallow most of the zone), deterministic grid-index tie-break for replay exactness. **What I removed and why it was wrong:** the corridor-derivation made the default an *opinion about the fleet*, which is the player's job; and the seam-overlap bias had the game **teaching the overlap technique by performing it** — worse than not teaching it, since overlap-vs-spread is one of the genuine coverage decisions. **The dumb default closes the "good default eats the decision" risk by construction** — a default that knows only "outward, and not where the others are" cannot eat a decision it has no information about. The old warn box is retired and replaced with what the default knows (your fort's shape, your other zones) versus what it never will (which approach the flagship commits to, what arrives first, what a wave punishes, what it learned last sortie — all four being exactly what the Fight teaches and the next Deploy spends). So: **defaulted fort = playable, read fort = better, permanently, by construction rather than by tuning.**

**4 · FUSION IS INTENTIONAL, AND UNDOABLE — the fusion-undo rule.** Jack: *"The other side of the accidental fuse is an intentional one... If a player puts down a cannon in a location that does fuse 2 groups, removing the fusion cannon should set the AoR back to the previous two groups' AoR. If the player picks up a different cannon, we can forget the previous 2 AoRs."* Reframed the section from "the accidental fuse and the preview that prevents it" to **"Fusion — intentional, flagged, and undoable."** Fusion is a real play (two medium zones become one large one: more barrels, bigger AoR, one tower buffing all of it), so the job is to make it **unmistakable and reversible**, not to prevent it. Unmistakable = the outline + the AoR change, two channels at once. Reversible = the memory rule, exactly as Jack specified: **remove that same bridging cannon → the previous groups return with their previous AoRs restored** (not the spread-default, not blank — the exact coverage you had built, so trying a fusion is *free*, which is what makes it something players will experiment with); **pick up any other cannon → the memory is discarded** (once you've started rearranging around the fused shape, the old zones aren't the plan you'd want back). Added two scoping rules the spec needed: **one level, no stack** (this makes a single "let me see what that looks like" free, it is not general undo), and **Deploy-scoped** (the Fight has no placement, so lock-in discards it). Why the bridging-cannon hinge is right: it ties the undo to the *gesture that caused it*, so no button, prompt, or manual is needed — removing the gun you just placed obviously means "not that," picking up a different gun obviously means "I'm doing something else." It also collapses the accidental and experimental cases into **one rule**: the accident is now cheap to notice (the outline moved) and cheap to reverse — a better outcome than trying to design the accident out.

**5 · EARLY BATTLES SIMPLIFIED — confirmed as a goal; the ECONOMY IS TABLED.** Jack: *"We do want to simplify the first couple of battles so that the player is not overwhelmed. The whole economy of cannons has been tabled for another session."* Deploy §2 retitled **TABLED — own session · derivation only**, keeping the derivation chain, the open input, and the numbers-free structural shapes, and nothing else. The old "thin early Deploy" *warning* is upgraded to a **confirmed design goal**: an early Deploy with two guns, one group and one domain is not a broken phase, it is a small one, **on purpose**. The rebuilt economy is what makes this matter — if coverage only becomes an allocation decision once there is a crowd to allocate against, the early game structurally lacks the core tension, which is fine *provided it is designed as an on-ramp rather than happening by accident*. The proposed shape (one order field per early battle: placement → AoR nudge → domain → fire-control → tower stack) now belongs to the tabled economy session + Campaign's toolkit teaching order, not to this doc.

*(Jack's sixth bullet arrived empty — nothing assumed or inferred for it.)*

### Versions after cont.12
Deploy **v1.2.0** · Build **v1.2.0** · Cannons & Towers **v2.1.0** · Journal cont.12b. Unchanged: Why v2.0.5, Build v1.1.1, Fight v1.2.1, Fleet Memory v2.0.4, Ships v2.0.1, Campaign v2.0.1, Victory v2.0.5, Shape Catalog v1.0.0, GDD v6.7.0, Removed v1.3.0.

**NEXT (revised after Jack's rulings):** **#0 fleet sizing** is now the blocking item — cannon slots, wall budget and all three phase timers are downstream of it, so terrain (#3) and the Stonwryt economy (#4) are no longer the obvious next picks. Then **#0b the three-timer session** (Rampart-calibrated). Jack's pick. #6 **mini-games** is now fully unblocked (all three phases have owning docs, and Deploy §4 just handed it a specific drill to build: teaching that courtyard geometry decides command granularity). Also newly opened by this session, both small and owned elsewhere: the **Deploy twin of the ≥2-solutions law** (Campaign/Build) and the **one-order-field-per-early-battle teaching ramp** (Campaign).

## SESSION: 2026-09-02 (cont. 13) — FLEET SIZING + CANNON ECONOMY, greenfield (queue #0 → DONE)
Jack: "#0 fleet sizing + cannon economy." Uploaded journal + Ships + Fleet Memory + Victory + Why + Cannons + Build + Deploy + Fight + Campaign + Mini-Games.

### Jack's two framing rulings, taken first
**1 · Doc architecture — no new doc, but the derivation needed an owner.** Jack's lean (numbers live with whoever owns each system) was adopted. The correction: the *derivation itself* had no owner and was sitting in Deploy §2, a doc that owns neither ships nor walls. It moved to **Victory §3**, which already owned the pool. Caveat logged for later: when the full numbers layer arrives (resolve magnitudes, falloff shape, ammo, cognition-creep rate, air density), a single tuning-values doc will earn its place — probably reviving `Rivenkeep_Balance_Analysis.html`. A doc created now for one derivation would just be a wrapper competing with the owners.

**2 · GREENFIELD — Jack's instruction, and it is now written into Victory §3 as a register.** *"We are throwing away all of the numbers associated with ships, troops, bombers, cannons. How they interact. How many and how much time. None of the old stuff should survive the massive redesign we did on the ships."* Recorded as an explicit **voided-numbers register** covering counts (pool sizes, spawn rates, sortie counts, troops per transport, bombers per carrier, slot formulas, type caps), interactions (hull HP/hits-to-kill, reload and rate of fire, movement speeds, AoR radius and area scaling, falloff floors and the Coordination increment, proximity fire, cannon recoil, troop stack multipliers, command-confusion batching tiers, troop A* cost weights, ammo loads) and times (all three phase timers, sortie length, transit, crawl, switch). Rule stated: where a *shape* was designed independently of its magnitude, the shape survives and only the number is void; where the number *was* the design, it is gone. Two legacy figures (2 guns at the opening, cap of 12) reappear in the derived results and are **explicitly given no evidential weight** — coincidence, not corroboration.

### The model — contacts vs hulls, and the correction that mattered
**The sizing unit is a CONTACT, not a hull** — one coherent object of attention, one coverage decision. A formation holding shape counts once whatever its hull count; a dispersed or picket formation counts once per hull; a formation that *breaks* mid-approach converts from one to many. Troop stack = 1, bomber cloud = 1, bomber stream = 1 per element, flagship always its own.

This was written on intuition in the first pass and is now **empirically backed**: group tracking capacity is ~4 groups and is *independent of how many items compose each group*; it degrades as intra-group spacing rises; and it degrades when common fate is disrupted. All three halves of the rule are measured, not assumed — including the breaking-formation case, which is therefore an authorable tactic (a wave that fragments under fire buys itself tracking load at the player's expense).

**THE LOAD-BEARING DISTINCTION: contacts are the attention budget; hulls are the statistical substrate.** Contacts are capped hard and low by human tracking. Hulls — the bodies resolve, fear propagation, contagion, batching and cascades run through — can be several times that. A wave of *2 contacts of 4 hulls each* is two objects for the eye and eight bodies for the network.

**MY ERROR, CORRECTED (Jack's ruling #2, "bring the resolve layer in earlier — it is the heart of the game").** The first pass computed the resolve layer's population floor in *hulls*, compared it against a *contact* count, and concluded resolve could not come online until the mid-War. Two different quantities; the conclusion was wrong and is withdrawn. **Resolve is online from Campaign 1 at full strength** — no staging needed. What it actually constrains is *early formation authoring*: opening waves arrive as loose clumps (6–8 hulls in 2 contacts), never as sparse singletons, since a singleton pair is both a thinner read and a dead resolve network. Loose-and-clumped is also the Cognition tell for a shallow fleet, so this costs nothing. Fixed in Fleet Memory §7 (the box was rewritten from `.s warn` to `.s pillar`).

### The ceiling — corrected in kind, not just in value
Tracking capacity is a **single global pool**, not an allowance per bearing, so the first pass's "≤4 per approach, ≈12 board" was wrong in kind. Corrected:
- **6 simultaneous contacts as the design target, 8 as the hard ceiling.** Range grounded in measured limits: 3–5 items ordinarily, ~4 size-independent groups, rising toward **8 when objects move slowly** and collapsing toward 1 when fast. Rivenkeep sits at the top of that range on three design facts — its contacts are slow (~1 grid/s), visually differentiated by lineage rather than identical, and **pre-learned** (deterministic battle, wave already met, so the player predicts rather than tracks). Against that, the Fight piles on load the laboratory task lacks (two fogs, health, ammo read, live verbs), which is why the target is 6 and not 8.
- **≤3 simultaneously live approaches** — pan cost on a board larger than the screen. Bonus: at most two can be off-viewport, so Fight §10's off-screen-cue problem is a two-indicator problem, not open-ended.
- **16–24 simultaneous hulls.** Anchored on Rampart's hard maximum of **16 ships in play at once** — but read carefully: that is a *population* figure on a single screen with manual crosshair targeting, and Rampart never asks you to read sixteen ships' intent. So it licenses hull count, not contact count. Our board is ~4 phone viewports and we never hand-target a hull.

### THE CALIBRATION — k₁ derived twice (Jack's ruling #1: "DO NOT GUESS ON NUMBERS. Have fact back you up")
Four quantities were being guessed independently. Each is now pinned to a source:
| Quantity | Value | Source |
|---|---|---|
| Baseline hull, hits to kill | **3** (roster band 2–6) | Rampart's shipped values: 2 / 3–4 / 5 for gunship / lander / command ship, "dark" variants +1. Its hard end was famously punishing, so 3 is baseline rather than 5. |
| Sea speed, baseline | **≈1 grid/s** | Derived from our own targets: a ~25-grid approach must fit a ~45 s sortie and still leave time to engage and withdraw. Also what puts contacts in the slow regime the tracking ceiling assumes. |
| Single-cannon AoR radius | **4 grids**, r(n) = 4√n | Pinned at the top end: a 4-gun group gets r = 8, spanning the readable height of a phone viewport — the largest zone inspectable without panning. AoR is *doctrine, not gun range* (real coastal artillery outranges this whole board), so legibility is the correct pin. |
| Reload | **= projectile flight time**, ≈4 s at mid-AoR | Rampart's actual rule: one ball in flight per cannon, distant shots arc higher and take longer, so building near the water bought more shots. **Not a free parameter.** |

**k₁, two independent routes:**
- **Route 1 (top-down, from the locked star thresholds).** ★★★ Ships Destroyed = 90%+, ★★ = 60% (Victory §2, GDD-inherited, not up for revision). Survivors re-emerge and are shot at again, so cumulative kills over N sorties ≈ 1 − (1−S)^N. At N = 3: 90% needs **S ≈ 0.55**, 60% needs **S ≈ 0.25**. A late wave is ~20 hulls → excellent play accounts for ~11 per passage. A late fort is 12 guns in 3 groups of 4 → 3·k₁·4^1.5 = 24k₁ = 11 → **k₁ ≈ 0.46**.
- **Route 2 (bottom-up, from geometry + the pins).** r = 8 → mean chord ~20 grids → 20 s in zone at 1 grid/s → 5 shots per gun at a 4 s reload → 4 guns × 5 = 20 shots → ×0.55 mean hit probability = 11 hits → ÷3 hits per hull = **3.7 hulls**. TKP(4) = 3.7 → **k₁ = 0.46**.
- **Agreement to two significant figures → k₁ = 0.45.** The routes share Rampart as a *source* (hull HP in one, the reload rule in the other) but **no single figure appears in both**, so this is the first number in the game with a real cross-check under it. Where the routes would disagree is where the model is wrong.

**TKP(n) = 0.45 · n^1.5** — barrels scale n, radius and therefore time-in-zone scale √n. A 4-gun group is ~8× a lone gun, not 4×.

### S IS NOT A DIFFICULTY LEVER — it is a consequence (Jack's ruling #3: "Don't understand this at all")
The flag was badly explained, and it dissolves anyway. What I was worried about: Campaign §3 states there are exactly **two** orthogonal difficulty families — board-combinatorial (terrain, weather, pieces, triage) and enemy-cognitive (how well the fleet thinks). If the game *also* got harder by giving the player fewer guns relative to the threat, that would be a third escalation track, it would be neither board nor enemy, and — the actual problem — it would be **invisible**: the player would feel "harder" with no readable cause, breaking the law that the player always understands why they lost.

**It dissolves because S turned out to be derived, not chosen.** The star thresholds are locked, so S is locked: ~0.55 under perfect allocation, ~0.25 for a player who accepts the default zones. Nothing escalates by squeezing the defender. What the five named difficulty levels move is the **slot grant**, and a gun count is fully visible, so that is a legible handicap setting of the ordinary kind. Two consequences worth keeping:
- **The fort is never meant to clear the sea.** Even perfect play lets ~45% of arrivals through a passage. Correct — victory is enclosure, the wall is the health bar, and a fort sized to sink everything has no allocation decision in it.
- **The S gap (0.25 → 0.55) IS the skill gradient the leaderboard measures.** Same board, same fleet, same guns; the difference is whether you read the ground.

### Jack's ruling #4 — accepted, no change
On the choreography law now having three screws (contacts, approaches, cognition): *"I don't see the problem. We are rebuilding all of the numbers and tuning knobs."* Agreed — kept as written. Campaign §4 additionally records a **fourth screw that is not a screw**: hull count. A campaign may add hulls freely provided they arrive inside formations that already exist, since that raises statistical richness at zero legibility cost. Hulls only become a screw when they arrive *dispersed*, at which point they are contacts and count as such.

### What falls out (all now in the docs)
| Stage | Approaches | Contacts | Hulls | Guns start → cap |
|---|---|---|---|---|
| Cam 1–6 | 1 | 2 | 6–8 | 2 → 4 |
| Cam 7–22 | 2 | 4 | 12–16 | 5 → 8 |
| Cam 23–32 | 3 | 6 | 16–24 | 9 → 12 |
| Hard ceiling — never authored above | 3 | **8** | 24 | 12 |

- **Slots derived, not indexed.** Solve TKP(n) = S × arriving hulls, **round down**, and let in-battle earned slots walk the fort upward toward a supply level it never reaches. That gives "slots grow within a battle by Fight performance" an actual job. The old `min(2+floor(cam/6),7)` / `min(start+sorties+floor(ships/5),12)` were indexed on campaign number and pool size — both the wrong inputs.
- **Cap of 12 now has a reason:** 3 approaches × 4 guns, and at 4 guns r = 8 = the readable viewport height, past which a zone cannot be inspected without panning and placement stops mattering because the circle covers everything.
- **Pool, spawn rate, sortie count — derived in that order.** Pool ≈ 10–14 hulls early, 34–44 late. Spawn rate = whatever holds an approach *at* its contact count, not above it. Sortie count stays emergent.
- **Wall budget:** perimeter ≈ 10·√(g·k). Second commanded group ≈ **+40% wall**, third ≈ **+75%** — the price tag on the Build↔Deploy seam, and the counterweight that pays for super-linear group throughput.
- **Type limit:** the fraction rule `max(2, ⌈slots/3⌉)` is canonical. **Contradiction resolved:** three incompatible rules were in circulation — the fraction rule, an archived "no cannon type limit," and `floor(totalStars/unlock_threshold), cap 5`. The latter two are struck; the fraction rule is the only one that scales with a derived slot count.

### A parked idea validated by the benchmark
**AoR-distance reload is no longer a proposal — it is what the model already implies.** Rampart shipped exactly this (one ball in flight per cannon; distant shots arc higher and take longer; building near the water bought more shots). So reload = flight time is a *consequence* of the throughput model rather than an addition to it, and Jack's projectile-arc answer to the legibility question is the diegetic display of it. Recorded in Cannon §5. Un-parked.

### VERSION SINGLE-SOURCING (Jack's request) — done across all 10 module docs
Three stale footers were found (Build footer v1.1.1 vs meta v1.2.0; Deploy v1.0.0 vs v1.2.0; Cannons v2.0.7 vs v2.1.0) — pre-existing drift from cont.12/12b, caused by hand-editing the same number in two or three places. **Fixed structurally rather than by hand:** each doc now declares `--doc-version:"vX.Y.Z"` once in its `:root`, with a `.ver::after{content:var(--doc-version)}` rule, and every *current-version* mention (meta, footer, changelog head, in-body "new" pills) renders `<span class="ver"></span>`. Script-free, so the module docs stay script-free per the house rule. **Bumping a doc is now a one-character edit in one place, and the footer can no longer drift from the meta.** Historical changelog stamps stay literals on purpose — they record the state at that session.

### Verified this pass
All 10 docs: div / section / ul / table tags balanced, zero dangling internal anchors, `.ver` rule present, exactly one current-version literal (the `--doc-version` declaration itself), script-free. Stale-number sweep clean — no surviving `S ≈ 0.7`, `k₁ ≈ 0.5`, `≈12 board`, or per-approach contact language anywhere in the set.

### Versions after cont.13
Why **v2.1.0** · Build **v1.3.0** · Deploy **v1.3.0** · Cannons & Towers **v2.2.0** · Ships **v2.1.0** · Fleet Memory **v2.1.0** · Campaign **v2.1.0** · Victory **v2.1.0** · Fight **v1.3.0**. Unchanged: Mini-Games v0.1.0, Shape Catalog v1.0.0, GDD v6.7.0, Removed v1.3.0.

### Honest status — what would move these numbers
- **The AoR area-scaling rule is the single most load-bearing assumption.** TKP ∝ n^1.5 depends on area scaling linearly with gun count, which Cannon §3 itself marks "exact scaling TBD." A different scaling changes the exponent and every gun count with it.
- **The reference sortie count of 3.** S is derived at N = 3, but sortie count is emergent (2–5), so S is really a band and a player who habitually reaches 5 sorties needs a lower per-passage rate for the same star. **The star thresholds may need a sortie-count normalisation** — flagged, not solved; belongs with Victory §2's adaptive thresholds.
- **Mean hit probability of 0.55 rides on falloff numbers that are themselves void.** When the falloff is rebuilt, k₁'s bottom-up route must be re-run. The top-down route is unaffected, which is the point of having two.
- **Tracking capacity is a skill function.** The mini-games are the instrument for raising it, which makes them load-bearing against The Why's tension #3 rather than an onboarding nicety. Test to hold: at the widest wave the campaign fields, a player should be able to say what each approach is doing. If not, the fleet is too big — the fix is a smaller fleet, never a denser HUD.

**NEXT:** **#0b, the three-timer session** (now unblocked and carrying derived inputs — see the queue). Then the remaining greenfield number-sets, which #0 has un-blocked but not filled: the **falloff rebuild** (edge floor, Coordination increment, and therefore mean P(hit)), **AoR area scaling** (fixes TKP's exponent), **ammo loads per lineage**, **resolve magnitudes**, **troop/bomber counts and cadences**, and the **batching tiers** re-derived against the new hull population. Also newly opened: the **sortie-count normalisation** for the star thresholds.

---

## SESSION: 2026-09-02 (cont. 14) — sizing hardened: k₁ derived, board size derived, sortie count derived, scoring ruled
Jack raised the effort level explicitly: *"I really want to dive into the numbers and make sure that they are solid. All of the number explanations should be written into the docs. They are important. ANY NUMBER is open to recalculation after the redesign that we started about a week ago."* Every derivation below is now written into the owning doc, not just summarised here.

### Jack's rulings, and what each one changed

**1 · AoR SCALING IS LINEAR IN AREA — and this closed the chain's largest open assumption.** *"Except for lone wolves, scaling AoR is linear. That is the easiest thing for humans to understand. This is not for realism, this is minor piece that a human must understand right away."* Ruled: each gun contributes one equal slice of zone (1 gun → base, 2 → 2×, 3 → 3×, 4 → 4×). Written into **Cannon §3** with the reasoning, because it is a small rule the player must absorb on first sight or every later coverage decision is guesswork. The alternative — linear *radius* — was rejected in the doc as unpredictable and badly non-uniform (the 4th gun would add ~7× the coverage of the 1st, which nobody eyeballs). Consequences now recorded: **radius ∝ √n** (so r₁ = 4 grids puts a 4-gun group at r = 8, a 16-grid zone), and **throughput ∝ n^1.5 rather than n²**. cont.13 had flagged AoR area-scaling as *the* most load-bearing unknown in the whole numeric chain; it is now settled, and the doc records what n² would have meant (TKP(1) = 0.23 not 0.45, TKP(2) = 0.92 not 1.27 — small groups far weaker, consolidation pressure much stronger). Linear area is both the simpler mental model and the gentler consolidation curve.

**2 · EIGHT CONTACTS IS THE DESTINATION, NOT THE DANGER LINE.** *"I understand that tracking 8 targets may be difficult, but that is war. I am hoping that when more targets are on the battlefield, the player has learned the mental skill to handle this."* The cont.13 ceiling (6 target / 8 hard cap) was too defensive. Revised in **Victory §3** and **The Why §6**: the late campaign **targets 8**, the ramp runs 2 → 8, and the ceiling is treated as a **trained quantity** rather than a constant — raised by determinism (a pre-learned wave is predicted, not tracked) and by the **mini-games**, which are now explicitly the instrument. This is the strongest argument yet that the mini-games are a pillar: *a player who cannot hold eight slow, familiar, differentiated contacts cannot play the late War*, so the ladder that gets them there is load-bearing against tension #3.
- **The law that makes 8 safe (new):** **at most 4 contacts may be decision-bearing at once.** Total may reach 8; the number simultaneously *asking something* of the player stays ≤4 (the measured group-tracking figure, and what the Fight §5 salience budget already implied). Above the tracking edge a player rightly stops tracking and starts **sampling** — which is what a commander does — and that only works if the board never punishes a reasonable sampling pattern. Red line: if a board punishes a player for not watching a contact that gave no reason to be watched, the board failed. Sibling to the ≥2-solutions and threat-spacing laws, owned by board/wave authoring.
- **The coupling that makes the load worth carrying:** the player already cannot cover every approach with guns, and now cannot watch every approach with attention. Same problem at two scales, solved by the same act. So raising the contact count **deepens** the game instead of merely loading it — the difference between depth and noise, which is the entire subject of tension #3.

**3 · WHY A FORMATION IS NOT JUST ONE BIG SHIP — Jack answered his own challenge, and it is the justification hull count needed.** *"The question is, if we have 6+ targets, why not just create a single ship. The answer is that the target is made up of different types of ships. You may have 4 ships escorting a transport ship. Or 6 ships protecting an aircraft carrier. The second answer is that each of these ships has its own 'mind.' One might retreat, and then others follow."* Written up as its own section in **Ships §9**:
- **Internal composition makes a formation a destructible STRUCTURE, not a health bar.** The player isn't choosing whether to shoot it, but *what inside it* to shoot — kill the payload and the escorts guard nothing (no land wave, no bomber launch); kill the escorts and the payload advanced the whole time; kill the anchor and coordination collapses into a field promotion. A single big hull poses one question ("shoot it or don't") and can only be made harder by adding HP — the exact treadmill the design refuses. **So pressure is always added as structure, never as health.**
- **Every hull has its own mind, so the formation is a coalition that can FAIL.** Resolve is a per-ship network; a big ship cannot waver, be bluffed, or be broken — only killed. And the fear grid / motion signature are only rich because there are several hulls to read the signature across.

**4 · FRAGMENTATION elevated to an authorable tactic (Jack: "I love this").** Because group tracking degrades when common fate is disrupted, a formation that **breaks mid-approach converts from one contact into one per hull**, at the worst moment for the player. Written into **Ships §9** as two cases that feel completely different: **involuntary** (a rout cascade — the attention cost is the price of your own success, and mostly ignorable because they're fleeing, though retreating hulls still take fire and still count) and **voluntary** (a deliberate late-War scatter that spends mutual support and splash-resistance to buy the player four extra things to track — a real tactic with a real cost, executable only by a deep fleet, and the cleanest possible expression of "harder because smarter, not bigger"). Both bounded by the ≤4-decision-bearing law: a scatter that pushes a board past its budget is an authoring failure, not a clever wave.

**5 · THE CAMERA IS PART OF THE GAME — canonised, with performance as a design bound.** *"Understand that the player will be able to zoom in and out. This zoom and pan SHOULD ALWAYS BE PERFORMANT. The phone size is part of the game. A commander does not always have a full picture when targeting an AoR. On the flip side, an overview does make it harder to target AoRs."* New section in **Fight §5** (and in Victory §3's board work):
- **Zoomed IN** (gun scale, ~24×16 grids) buys command — precise AoR nudging, readable gun health, a legible gradient — and costs you the battle (other bearings off-screen).
- **Zoomed OUT** (board scale) buys the read — every contact and its motion signature, AoR extents, both fogs, the fear shape, the fort's saturation as a battle-health gauge — and costs precision (a 2×2 gun renders ~9 pt: visible as a mark, too small to command well).
- **Why this is a mechanic, not a compromise:** the scarce resource is where the player is looking, and the camera turns that from metaphor into a literal choice made several times a sortie. It also folds the camera into the *plan* — a crawl scheduled in Deploy must be executed zoomed in, so the player knows in advance they'll be briefly blind elsewhere and can schedule it into an affordable gap. **That blindness is the real cost of the command**, more diegetic than any cooldown, and part of why verb costs never needed to be punitive.
- **PERFORMANCE AS A DESIGN BOUND:** because zoom/pan carry information needed continuously, in real time, on a decision timer, any stutter is *a read the player has lost*. Requirement: **smooth at the widest wave the campaign fields, on the oldest supported device** — and if a board's entity count can't hold that, **the board is too big or the wave is too wide**; the fix is a smaller board or narrower wave, never a coarser camera or a dropped render layer. This caps board size and wave width as surely as legibility does. Implementation → SDD; the bound lives in Fight because the Fight spends it.

**6 · BOARD SIZE — derived for the first time, and 64×48 is too small.** Jack: *"Right now, I am completely open to changing the size of the battlefield, but I was thinking it might be able to get bigger."* His instinct was right, and by more than a little. Three independent requirements each set a minimum and they agree — full derivation in **Victory §3**:
- **Approach depth ≈ 39 grids per live sea bearing.** Safe launch zone ≈5 (one reload cycle of untouchable acceleration at 1 grid/s vs a 4 s reload, so no spawn-camping) + reading band ≈18 (read formation shape and heading, decide, and *complete* a costed verb — an 8-grid crawl at 1 grid/tick is ~8 s, so read+decide+execute ≈18 s ≈18 grids) + engagement band ≈16 (one full 4-gun AoR diameter, so a contact crosses a whole zone rather than clipping its rim).
- **The fear grid gives the same number independently.** The grid stays ~10×10 whatever the board size, so on a 128-wide board a cell is ~12.8 grids. For fear *navigation* to be visible — skirting a hot cell, probing a cooling one, committing through a cold one — a contact must cross 2–3 cells: **26–38 grids.** Same answer, reached from the enemy's side. And the direction is favourable: **a bigger board makes each fear cell bigger and fear behaviour MORE legible**, one of very few places where scale helps legibility. Recorded in **Fleet Memory §3**.
- **Fort core ≈ 50×35.** The ≥2-near-equal-solutions law needs castles at genuinely different spacings (some pairs 8–12 grids apart so one ring takes several, others 25+ so taking both is expensive). Below that spread, every castle set is a keystone set and triage collapses to one answer.
- **→ RECOMMENDED 128×80** (width 40 + 50 + 38; height 40 + 35 + slack) = **3.3× the area of 64×48**, the smallest board supporting the design's own stated maximum of three live approaches at full reading depth around a fort with real triage variety.
- **It still fits a phone, and the arithmetic is in the doc.** 80 grids into ~360 pt of landscape height = **4.5 pt/grid**, so 128 wide renders ~576 pt and sits inside a landscape viewport. What matters is that *the tracking read happens at contact scale, not gun scale*: a 4-hull formation spans ~6 grids ≈ **27 pt** (trackable); a 4-gun AoR spans 16 grids ≈ **72 pt** (unmistakable); a 2×2 cannon ≈ **9 pt** (a mark, not a shape — which is the ruled tradeoff, and correct: the overview reads the battle, it doesn't command it).
- **Derived upper bound:** a contact needs ~20 pt to be trackable, so at 6 grids/contact the floor is 3.33 pt/grid → board **height caps at ~108 grids** on a phone. 80 sits well inside; 128 *tall* would not. Width is bounded by pan tolerance, not legibility.
- **Costs, stated honestly:** it does NOT inflate the Build job (wall demand follows perimeter, and perimeter follows the fort core, not board area — recorded in **Build §5**); it DOES inflate authoring 3.3× per board across 190 battles and 10 theaters (lands on the battle generator, not the design); it inflates panning (answered by the zoom ruling, not by shrinking); and it raises in-view entity count, which is what makes the performance bound hard rather than nice. **Middle option offered: 96×64** (2× area, ~32-grid approaches, ~32-grid core) — under the derived depth and core figures, so it buys most of the reading room with slightly compressed triage variety. Defensible; 64×48 is not.

**7 · SORTIES 3–10, deviation −1 to +2, and "10 is not necessarily more difficult than 3."** Jack's range, and the clause about difficulty is only true if the range comes from something other than pressure. It does, and the mechanism is now in **Victory §3** and **Build §5**:
- **Sortie count is a CONSTRUCTION SCHEDULE, not a difficulty dial.** A battle ends when the required castles are enclosed at the end of a Build phase, so sortie count is first and mostly how many Build phases it takes to lay and hold that much wall: `sorties ≈ ⌈new wall cells ÷ (pieces per Build × mean piece size)⌉ + rebuild-tax sorties + 1 securing sortie`. That gives **3 early** (≈9 cells ÷ ~3 pieces = 1 wall Build, +1 tax, +1 securing) and **7–10 late** (≈90 cells ÷ ~8.5 pieces = 3 wall Builds, +3–5 tax, +1). **So the 3–10 range falls out of the requirement ladder** — a ten-sortie battle is a bigger construction job, not a fiercer fight. This number could never be settled before the wall budget was.
- **The −1/+2 deviation is where skill lives, and only there.** Skill doesn't change the wall you owe; it changes the **rebuild tax**. Deliberately a tight band: enclosure is the win condition, so letting skill swing battle length wildly would make the star levers incomparable between players on the same board.
- **THE FADING FLEET — why a long battle isn't the front half again.** Pool ≈ **2.5× the peak wave**, deliberately not enough to sustain a full-strength wave for ten sorties. Sunk stays sunk, survivors return damaged, injections run out; around sortie 6–7 the pool thins and later waves arrive smaller and more battered. **A long battle is one you are winning slowly.** Tension moves from the sea to the clock and to your own condition — a different and legitimate late-battle tension, and it protects the anti-treadmill rule at battle scale: nothing gets bigger as a battle runs long.

**8 · THE NEVER-EMERGED SHIPS — gut-checked, and there is a real trap.** Jack: *"There is a cap on the number of ships. If a battle is won, and 10 ships never emerged, can we consider them kills — ships that were never in the battle. Gut check me on this."* Full ruling in **Victory §3** (`#accounted`).
- **THE TRAP: as a flat rule, this hands ★★★ to the fastest turtle.** A battle is won the moment required castles are enclosed at the end of any Build phase — nothing requires fighting first. On a board where the ring closes in one or two Builds, a player who rushes a minimal enclosure wins with most of the pool never emerged, and under a flat rule scores **★★★ on the ships lever for having sunk almost nothing.** That inverts the star system (highest ship score to whoever avoided the fleet best), collapses the three levers toward one dominant strategy, and turns the 0★ pacifist easter egg into the optimal line. It is the enclosure-dominance failure (The Why §6, tension #4) arriving through the *scoring* rather than the mechanics. **A flat rule cannot distinguish "they never came because I broke them" from "they never came because I left early."**
- **THE RULING: score by CAUSE — the lever becomes SHIPS ACCOUNTED FOR.** Sunk = 1.0. **Routed** (fled with resolve broken) = 1.0 — you removed it by breaking it, which is the skill the resolve network exists to reward, and you already pay by forfeiting the sink. Normal end-of-sortie withdrawal = 0 (it's coming back). **Unemerged reserve = 1.0 only if the battle ended in a fleet RETREAT**, because a Retreat *is* the fleet declining to commit them. **Unemerged reserve = 0 on an enclosure victory while the fleet was still committing** — the clause that closes the exploit.
- **Why the Retreat gate can't be gamed:** a Retreat requires the resolve network to have degraded across sorties (losses, dead/weak anchors, repeated rout cascades) until a re-formed wave instantly cascades. It is only reachable by fighting well, repeatedly — so the credit is gated behind exactly the play it rewards, by a mechanical state rather than a heuristic.
- **Thresholds and denominator unchanged** (any / 60% / 90% / 100%, over the capped deterministic pool), so leaderboard comparability is untouched. Lever renamed in Victory §2 as well.
- **THE SECOND BRAKE, which was already there — the three levers police each other.** Worked table now in the doc: fast minimal enclosure = ★ ships / ★★★ cannons / ★ area → ★★, Battle Score ≈145. Long poor grind = ★★★ / ★ / ★ → ★★, ≈155. Read-the-ground repel-heavy = ★★ / ★★★ / ★★★ → **★★★, ≈255.** The intended play wins on both stars and score with no special rule. **So the cont.13 flag that the star thresholds need a sortie-count normalisation is WITHDRAWN** — within-lever saturation is real, but cross-lever tension absorbs it, and a normalisation would have fixed a problem the inherited 3-lever design had already solved. That the levers police each other across a 3-to-10 sortie range is a genuine strength of the GDD scoring and worth not breaking.

### Docs written this pass
Victory **v2.2.0** (owner: ceiling ruling, board-size derivation, sortie-count derivation, Ships Accounted For, calibration updated, honest status rewritten) · Cannons **v2.3.0** (§3 linear-area ruling + consequences; §5 throughput reconciled) · Ships **v2.2.0** (§9 formation-vs-big-ship + fragmentation) · Fight **v1.4.0** (§5 camera + performance bound; §10 ceiling to 8) · Why **v2.2.0** (§6 tension #3 reframed as trained) · Campaign **v2.2.0** (§4 four-dial ramp incl. sorties) · Build **v1.4.0** (§5 wall demand sets battle length; board-growth note) · Deploy **v1.4.0** (§2 reconciled; both upstream flags closed) · Fleet Memory **v2.2.0** (§3 fear-cell scale on a bigger board).

### Verified
All 10 docs: div / section / table / ul tags balanced, zero dangling internal anchors, every `class="s X"` variant has a CSS rule (added `.s.law` + `h4` to Victory, `h4` to Ships and Build), exactly one current-version literal per file (the `--doc-version` declaration), script-free. Stale sweep clean: no surviving `64×48` outside the deliberate supersession notes, no `8 as a hard ceiling`, no `exact scaling TBD`, and `Ships Destroyed` remains only where it correctly records the pre-rename history.

### Honest status — two flags closed, five open
**Closed:** AoR area scaling (ruled linear → exponent 1.5 settled) · the sortie-count normalisation (withdrawn; the levers self-police).
**Open, and stated as targets:**
- **The rebuild tax is the last missing input to sortie count.** The schedule arithmetic is solid on wall cells and pieces-per-Build, estimated on the tax, because wall damage per sortie is itself void. Bracket and both ends firm; middle values will move.
- **Mean hit probability of 0.55 rides on falloff numbers that are void.** When the falloff is rebuilt, k₁'s bottom-up route must be re-run; the top-down route is unaffected, which is the entire reason for having two.
- **The ≤4-decision-bearing law is unmeasured.** No study covers a subject tracking enemy objects *and* conducting their own groups. 3 groups against 8 contacts across 3 bearings, with a camera that shows one bearing at command zoom, is the untested composite — **the number most likely to come back from prototype different.**
- **128×80 is derived but unplayed.** Three requirements agree and the overview arithmetic says it fits — but "fits" and "reads well while a wave is landing" are different claims. If it doesn't read, the fix is the board, not the camera.
- **Tracking capacity is a skill function.** Test to hold: at the widest wave the campaign fields, a player should be able to say what each approach is doing. If not, the wave is too wide.

**NEXT — the remaining greenfield number-sets, in dependency order:**
1. **#0b the three-timer session** (Build / Deploy / Fight, Rampart-calibrated). Now carrying derived inputs: 8–9 pieces for a late sortie 1, 3–4 s per piece, 5–8 s recognition → sortie 1 wants ≈35–45 s, so 25→20 s is short and Deploy's 12–15 s is void. Docs: journal + Build + Deploy + Victory + Fight. **Sonnet-tier, medium.**
2. **The falloff rebuild** — edge floor, Coordination increment, and therefore mean P(hit), which feeds back into k₁'s cross-check. Docs: journal + Cannons + Victory. **Opus-tier, medium** (it is a real design choice about how much reliability coordination buys, not just a number).
3. **The rebuild tax** — wall damage per sortie, which closes sortie count. Docs: journal + Build + Ships + Victory. **Opus-tier, medium.**
4. **Ammo loads per lineage**, **resolve magnitudes**, **troop/bomber counts and cadences**, and the **batching tiers** re-derived against the new hull population (6→24). Docs: journal + Ships + Fleet Memory. **Opus-tier, high** — this is the biggest remaining block.
5. **BOARD SIZE DECISION** is Jack's to make before #0b ideally, since a 128×80 board changes pan distance during Build and therefore the Build clock. 128×80 recommended, 96×64 the compromise.

---

## SESSION: 2026-09-02 (cont. 15) — WIN CONDITION CORRECTED; formation persistence, purpose collapse, the queue
Jack, opening: *"No, no, no. Victory is not enclosing castles. Victory is beating back the attack and maintaining the number of castles enclosed. That is why there is a last stand."* This was a foundational correction, not a detail — a great deal from cont.13/14 was derived on top of the wrong condition and has been rebuilt.

### 1 · THE CORRECTION, and what it invalidated
**Victory = beat back the attack AND maintain the required enclosure count.** Enclosing does not end the battle; the *fleet* ends the battle. The Last Stand is the final unopposed window to reach or restore the required count, and to push past it for the Area lever — which is why it is the only phase inheriting 100% of banked time rather than 50%.

**The tell that should have caught this several passes earlier:** if enclosing ended the battle, a *last* stand would have nothing to be last of. Recorded in Victory §2 as a warn box, because the lesson generalises — an inherited mechanic that makes no sense under the stated rules is evidence the stated rules are wrong.

**What it invalidated:**
- **Sortie count as a construction schedule (cont.14).** Wrong in kind: laying wall no longer ends the battle, so it cannot set the battle's length. Section retained in Victory as an explicit supersession note rather than deleted, since the *wall clock* survives in a new role.
- **The fast-turtle exploit that shaped the Ships Accounted For ruling (cont.14).** It no longer exists, because you cannot win by enclosing at all. The ruling is re-derived below.
- **Assorted "victory is enclosure" asides** in Cannons §5, Deploy §2 and Victory §3 — all corrected to "a single passage is not the battle."

**What it produced — the battle is now a RACE between two independent clocks** (Victory §2, Build §5, Campaign §4):
- **The fleet's clock** = how long the battle lasts = queue ÷ elimination rate.
- **The wall's clock** = how long you need = Build phases the requirement demands, plus every re-plug forced on you.
- **Board-authoring law, and it is checkable:** sorties provided must exceed Build phases demanded, with margin for a lost ring. Too tight = unwinnable; too loose = the back half is an unopposed construction exercise. Sibling to the ≥2-solutions law.
- **The decision this creates, every sortie:** how much of the phase to spend securing the requirement versus how much to spend breaking the fleet — knowing that breaking the fleet faster shortens the battle and buys Last Stand time, while building faster secures the requirement and leaves the fleet intact. That is a far better problem than "when do I stop," and it is the sharpest justification yet for the Build cannon slate.

### 2 · FLEET DEFEAT — the two ways an attack is beaten back (new Victory §4a)
Jack: *"The ships' defeat comes when there are no more ships, or, maybe, when the ships no longer have a purpose to come out — like when we had 4 aircraft carriers with 6 screen ships and all 4 carriers were sunk. The screen ships have no purpose. That is why they retreat. This is all about the resolve."*
- **A · ANNIHILATION** — the queue is empty and nothing is left afloat. Rarest, cleanest ★★★! path.
- **B · PURPOSE COLLAPSE** — the elegant one, and it grounds resolve in something *structural* rather than only in fear. Hulls split into **purpose-bearing (cores)** — transports, carriers, bombards/breachers, the flagship: the ships that can actually accomplish something — and **purpose-serving (screens)** — Bulwarks, Quartermasters, escorting raiders, which exist only to get a core to where it can do its job. Sink every core and the screens have nothing to escort and no way to win, so their resolve has nothing holding it up and the fleet declines to commit. **The attack is beaten back with ships still afloat.**
- **Why B is the best thing in the victory model:** it makes fleet-scale **decapitation** the primary strategic line, and it gives every back-line-targeting tool in the defender kit a reason that runs all the way to the win condition — the Marksman, the back-line target personality, the fight-through-the-screen problem, the flagship's screening behaviour. All of it now points at one thing: **find what the fleet is for, and kill that.** A player who sinks four carriers has won more decisively than one who sank sixteen escorts, and the game now agrees.
- **C · STALEMATE RETREAT** — kept valid-but-costly (the no-forced-playstyle law forbids closing it off). Slow, pays for its time in castle degradation ticks, and scores nothing under the credit rule below. Same shape as the already-designed "outlast the magazine" option.

### 3 · THE QUEUE — what comes out, and how many sorties there are (new Victory §4b)
Jack: *"Which ships come out per sortie is based on how many target groups are allowed for that battle and how many targets are in the queue."* This replaces the cont.14 derivation wholesale, and it is better because battle length becomes a property of **the fleet** rather than of the player's construction job.
- **C = target groups allowed this battle** — the contact budget, 2→8 (the legibility number; hard cap on a sortie's width).
- **Q = formations in the queue** — the battle's total roster, capped and fixed in order (the depth behind the width).
- A sortie fields **min(C, formations remaining)**, **survivors first**; fresh formations fill the remaining slots. So the queue drains only by what the player *finished*.
- **sorties ≈ Q ÷ formations eliminated per sortie**

| Stage | C (groups/sortie) | Hulls/formation | Q (queue) | Pool (hulls) | Eliminated/sortie | Sorties |
|---|---|---|---|---|---|---|
| Cam 1–6 | 2 | ≈4 | 4–5 | 15–20 | ≈1.5 | **3** |
| Cam 7–22 | 4–6 | ≈3 | 10–14 | 30–45 | ≈2 | **5–6** |
| Cam 23–32 | 6–8 | ≈3 | 15–20 | 45–60 | ≈2–2.5 | **7–10** |

**The reconciliation is worth noting:** the pool figures came from the cont.14 sizing pass (≈2.5× peak wave) and Jack's 3–10 sortie range came from his own judgement, independently. 45–60 hulls at ~3 hulls/formation = 15–20 formations; 15–20 formations at ~2 eliminated/sortie = 7–10 sorties. **They agree without either being fitted to the other.**

**Direction flipped, and it is now right:** repelling ends a sortie early but leaves the formation alive, so it banks time without draining the queue. Grinding a magazine kills more but banks nothing. Neither dominates — one buys Last Stand time, the other buys queue depth — and that tradeoff is now the central rhythm of the battle rather than a side effect. Skill moves the elimination rate within Jack's tight −1/+2 band, bounded above by gun throughput and below by the stalemate drain.

### 4 · FORMATION PERSISTENCE AND RECONSTITUTION (new Ships §9) — the mechanic that makes the contact model bite
Jack: *"The target (formation) of ships should persist between sorties. Let's say I have 4 screen ships and 1 troop ship in a formation. If the player kills 3 screen ships, the next sortie will have to look back for 3 more screen ships for the troop transport. If the troop transport is sunk and 2 screen ships remain, they can be reallocated to another screen, but they are probably damaged and soon sunk."*

A formation is a **persistent entity with role slots** — one **core** plus **screen slots** — and it carries its losses forward. Reconstitution happens between sorties, while the player builds:

| What happened | What the fleet does | What it costs the fleet |
|---|---|---|
| Screens dead, core alive | **Refill from the queue** — fresh hulls in the emptied slots | **Queue depth** — every replacement is a slot the queue can't spend elsewhere |
| Screens dead, queue dry | **Goes out under-screened** — visibly thin, soft centre reachable | The core becomes killable |
| **Core sunk** | **Formation dissolves** → survivors become **orphans**, reallocated to the most under-screened formations | **Permanent** — that purpose is gone, not delayed |
| Orphans with nowhere to go | Form a **coreless residual** — a formation with no purpose | The beginning of the fleet's end |

**Orphans keep their damage** and do not heal — Jack's phrasing is the design target: *probably damaged and soon sunk*. A real reinforcement, and a poor one.

**The decision this creates is the deepest in the Fight**, and neither option is strictly better. **Kill the screens:** easier (they're the hulls presented to you), drains queue depth, eventually strips a core naked — but the formation returns at strength next sortie. **Kill the core:** harder (screened, back-line, fight through), but **permanent** — a purpose removed forever, plus damaged orphans that are cheap kills next sortie, plus one step toward purpose collapse and the win. **Damage is temporary; purpose is permanent.** So the screen is not padding — it is a formation buying time for its core with hulls the queue must replace.

**Second-order effect, and it is a gift to the Fight's read:** because refills are fresh and orphans are damaged, a late-battle fleet becomes visibly *patchwork* — some formations at strength, some limping on borrowed hulls, some coreless and unwilling. That is the fading fleet rendered as **composition** rather than as numbers, readable at a glance from formation shape and motion.

### 5 · RESOLVE IS QUEUE-WIDE, and PURPOSE is a fourth input (Fleet Memory §7)
Jack: *"...BUT that is for the whole queue of ships, not just one sortie."*
- The resolve network spans **the whole fleet, reserves included.** Resolve damage **accumulates across the battle** rather than resetting per sortie — it is the closest thing in the game to a progress bar, and correctly one that is never shown. Repels are the deposits; the fleet Retreat is the withdrawal, which is why repels were always called the currency. And **reserves can be demoralised before they ever arrive**, which is the fading fleet expressed in nerve rather than hull count.
- **Purpose is now a fourth resolve input** alongside own-experience, peer contagion and the anchor broadcast. It gives resolve **a cause the player can attack directly** (reason about what the fleet is *for* and remove it — a strategic act rather than accumulated chip damage) and **a structural spine the player can see** (which hulls are cores, which are screens, which formations still have one). Reading it is unchanged in kind — no bar, still the motion signature — with one new top-end read: a coreless residual moves like hulls with nowhere to be, and that shape becomes the recognisable sign of the battle's end approaching.

### 6 · SHIPS ACCOUNTED FOR — re-derived (Victory §3)
The cont.14 objection was that a flat "unmet ships count" rule let a player win by enclosing early and bank ★★★ for sinking nothing. **That exploit no longer exists**, because enclosing cannot win. So unemerged reserves can only exist when the fleet stopped coming — which is exactly the achievement Jack's original question pointed at. The objection dissolves; the principle survives: **score by cause, never by absence.**

**The rule:** sunk = 1.0 · **routed = 1.0** · normal end-of-sortie withdrawal = 0 · **unemerged reserves × the fraction of purpose-bearing hulls destroyed.**

That proportional discriminator does all the work and replaces the retreat-type test: sank all four carriers → reserves count in full; turtled and the fleet lost heart with carriers intact → reserves count nothing; sank two of four → half credit, no threshold to cliff-edge on. **It needs no engine test for which kind of retreat happened, cannot be gamed by turtling, needs no special case for the stalemate path, and points the scoring at the same target the win condition points at.** A design where the optimal line and the winning line are the same line does not have to argue with its players. Thresholds (any/60%/90%/100%) and denominator (the capped deterministic pool) unchanged, so leaderboard comparability is untouched.

**Three-lever check, with the corrected win condition:** Turtle = ★/★★★/★★ → ★★, ≈180 · Grind = ★★★/★/★ → ★★, ≈155 · **Decapitate = ★★★/★★★/★★★ → ★★★, ≈285.** Both degenerate extremes land on ★★ and a middling score; the intended line wins on stars and score together with no special rule. Sortie-count normalisation stays withdrawn, now for a stronger reason: the levers don't merely absorb the sortie range, they actively point at the same strategy the win condition does.

### 7 · TENSION #4 IS NOW ANSWERED STRUCTURALLY (The Why §6)
The turtle risk was previously held in check by *balance* — the Build puzzle's difficulty and breakthrough threats — which is always one bad number from failing. Under the correct win condition it is held in check by **the shape of the win itself**: enclosing cannot win, and beating back the attack requires destroying the fleet's cores, so **a player who never fights cannot win by building.** The turtle line stays available (no forced playstyle) but is *structurally* inferior: many sorties of castle degradation, and unemerged reserves credited only in proportion to cores destroyed.
**General lesson recorded, because it will apply again:** the strongest fix for a dominance risk is **a win condition that does not admit it**, not a cost that discourages it.

### 8 · BOARD 128×80 CONFIRMED — and the ratio is doing a second job
Jack: *"128x80 is acceptable. Remember, this is a video play back ratio with banner information."* Recorded in Victory §3: **128×80 is exactly 16:10**, a standard video ratio. Fitted to the 9:16 replay export (1080×1920 with branding panels), a 16:10 board renders **1080×675**, leaving 1245 px of vertical frame for banner panels — generous, enough for a real title treatment rather than a cramped strip. So the board's shape is simultaneously what the design needs and what the share format wants.
**Why not 16:9 (128×72), which needs no letterboxing?** Because 72 is *below* the derived minimum: 40 grids of approach + a 35-grid fort core = 75 floor, 80 = floor plus slack. 72 would force either a compressed fort core (costing triage variety) or a shallow approach (costing reading time). The game sets the proportions; letterboxing 16:10 into 16:9 is thin bars and costs nothing.

### Docs written this pass
Victory **v2.3.0** (§2 win condition rewritten; §4a fleet defeat; §4b the queue; sortie section superseded with its useful remainder carried forward; Ships Accounted For re-derived; board ratio confirmed) · Ships **v2.3.0** (§9 formation persistence + reconstitution) · Fleet Memory **v2.3.0** (§7 queue-wide resolve + purpose as a fourth input) · Fight **v1.5.0** (§8 reading the battle's ending corrected — the read is now of the enemy, not your own walls; plus the race) · Build **v1.5.0** (§5 wall demand is a deadline inside the battle, not the battle's length) · Campaign **v2.3.0** (§4 queue-depth dial added, sorties dial corrected, new board-authoring law coupling the triage ladder to queue depth) · The Why **v2.3.0** (§6 tension #4 answered structurally) · Cannons **v2.3.0** and Deploy **v1.4.0** (stale "victory is enclosure" asides corrected).

### Verified
All 10 docs: div / section / table / ul / h4 tags balanced, zero dangling internal anchors, every `class="s X"` variant has a CSS rule, exactly one current-version literal per file (the `--doc-version` declaration), script-free. Targeted sweep for the superseded win condition run across the whole set — the only surviving mentions are the deliberate supersession notes.

### Open, and honestly ranked
1. **The elimination rate is the new soft term.** Sortie count is now queue ÷ elimination rate, and the rate depends on how formations actually die under persistence — which needs the falloff and hull HP settled, and needs a rule for *when a formation counts as eliminated* (all hulls dead? core dead? core dead and orphans absorbed?). **That last one is a real design question, not a number**, and it is the first thing I would pick up next.
2. **Core/screen composition per lineage is unspecified.** The core/screen split is defined by role, but which lineages fill which slots, in what ratios, and how many screen slots a given core type carries — none of that exists yet. It is the direct input to queue depth.
3. **The rebuild tax** still sets the wall clock's re-plug term and therefore the race's margin.
4. **The ≤4-decision-bearing law** remains unmeasured, and formation persistence adds to the load it must carry (reading *composition*, not just position).
5. **128×80 is derived and confirmed but unplayed.**

**NEXT — my recommendation, revised by this session:** the formation-composition and elimination-rule work (open items 1 and 2) now sits *ahead* of the three-timer session, because it feeds queue depth, which feeds sortie count, which feeds the race, which is what the timers have to fit inside. Docs: journal + Ships + Victory + Fleet Memory. **Opus-tier, high effort** — it is genuine design (what a formation is made of, and what it means for one to be finished), not arithmetic.
Then: #0b three timers (Sonnet, medium) · the falloff rebuild (Opus, medium) · the rebuild tax (Opus, medium) · then ammo / resolve magnitudes / troop & bomber counts / batching tiers (Opus, high).

---

## SESSION: 2026-09-02 (cont. 16) — capture pass: targeting/screening, formation shape, purpose-collapse constraints
Jack deferred all four open items and the timer work to their own sessions, and while doing so gave substantive design content that is now written into the docs. **This was a capture pass, not a design pass** — no work done on the deferred items.

### What Jack ruled, and where it landed

**1 · NEAREST-CENTRE TARGETING, and the reason screens work → Cannons §5 (v2.4.0).** *"The cannons should fire on the ships that are closest to their center AoR because that is the highest probability of a hit. That is why a screen works. All of the cannons fire independently, so they may choose to fire at a ship that is farther from its center."*
The targeting rule itself was already in the doc; **what was missing was its consequence, and it turns out to be the mechanical explanation for formation screening.** Now written up:
- **Screening is emergent, not scripted.** No rule says "escorts absorb damage." It falls out of two things already present: accuracy falls off from the AoR centre, and crews shoot the highest-probability target. A screen works because the screening hulls **occupy the high-probability positions** (forward, nearer your centre) while the core sits behind them at the chancy fringe. The fleet is not blocking your shots — it is **arranging itself so that your own targeting preference protects what it wants protected.** That is the fleet playing your model, the same idea as baiting the fear grid, one layer down. Emergent rather than authored is the best possible provenance for a mechanic this important.
- **It is probabilistic, not absolute.** Because every cannon fires *independently*, some barrels reach past the screen every volley. Screening buys the core **time and odds, never immunity** — which is what keeps core-hunting a live option rather than a locked door.
- **The lever this hands the player, with no new mechanic:** if the high-probability position is whatever is nearest the AoR centre, then **where you centre the zone decides which hull is most likely to be shot.** Centre forward over the water the screen crosses first → strip escorts efficiently. Centre **deeper**, on ground the core will occupy → your barrels reach for the core, at the price of covering less of the approach and letting the screen through comparatively untouched. A legible, costed answer to "how do I get at the thing I actually want," expressed entirely in AoR placement the player already does in Deploy and can pay to crawl in the Fight.

**2 · A SCREEN CAN COVER 2–3 CORES → Ships §9 (v2.4.0).** *"You could have 2 or 3 payload ships in a screen. Let's say they are troop ships and there might be 6 ships protecting them to get in."* A formation is not necessarily one core plus escorts. A shared screen is an **economy of scale for the fleet** and a **concentration of value** for the player — breaking a heavy screen once reaches several cores, so the reward scales with what is behind it. It also makes screen thickness a **readable signal**: six hulls around one transport is a fleet protecting something it cannot afford to lose; six around three is a cheaper prize per hull killed.

**3 · PURPOSE COLLAPSE IS A PRESSURE, NOT A KILL SWITCH → Victory §4a + Ships §9.** Two constraints, and together they fix a real risk the last session introduced.
- *"You shouldn't be able to kill the payload ship and the battle ends. Those screen ships can do damage too and they might be out for revenge."* Orphaned screens stay on the board, stay armed, stay dangerous. And the **revenge** reading is an interesting inversion: losing its purpose may make a hull briefly **more** committed rather than less — a fanatical spike before the collapse — which sits naturally on the existing intensity spectrum (fanatical = won't rout, drives into kill-zones) rather than needing a new state. *Open: whether revenge is a real transient state or simply the absence of a rally.*
- *"Kill enough screen ships and the payload ships may not come out to battle."* A core will not risk an unescorted run, so stripping the escort is a **second, symmetric route** to beating the attack back.
- **Why this matters more than it looks:** cont.15 left core-hunting looking like a single dominant line, which was the honest risk in that pass. These two rulings convert it into **two opposite legitimate lines** — kill the cores so the screens lose their *reason*, or kill the screens so the cores lose their *nerve*. They suit different boards and different fleets, and they are answered by **different defender tools**: deep-centred zones and back-line personalities for the first, forward coverage and area weapons for the second. That is the no-forced-playstyle law holding at the level of the fleet's structure, which is where it was most exposed.

### Deferred by Jack — each to its own session
All four cont.15 open items, plus the timers. Recorded here in **dependency order**, which is the order they should be picked up:

| # | Session | Why it sits here | Docs | Model |
|---|---|---|---|---|
| 1 | ✅ **DONE (cont.17)** — **Formation composition** — which lineages fill core vs screen slots, ratios, how many screen slots a core type carries, multi-core shapes | Feeds queue depth, which feeds sortie count, which feeds the race. Upstream of everything below. | journal + Ships + Victory + Fleet Memory | Opus, high |
| 2 | ✅ **DONE (cont.17)** — **The elimination rule** — when does a formation count as finished? (all hulls dead / core dead / core dead + orphans absorbed) Plus the revenge state and the sortie-refusal threshold | A real design question, not a number. Sets the elimination rate, and therefore sortie count. Needs #1 first. | journal + Ships + Victory + Fleet Memory | Opus, high |
| 3 | ✅ **DONE (cont.18)** — **The falloff rebuild** — edge floor, Coordination increment, mean P(hit) | Feeds k₁'s bottom-up cross-check, and now also feeds *how much* a screen leaks (cont.16), so it is load-bearing on screening too. | journal + Cannons + Victory | Opus, medium |
| 4 | **The rebuild tax** — wall damage per sortie | Sets the wall clock's re-plug term and therefore the race's margin. | journal + Build + Ships + Victory | Opus, medium |
| 5 | **The three phase timers, INCLUDING their lengths** (Jack: *"Even what the timer lengths are should change. That should be a session down the way."*) | Must fit inside the race, which is not settled until #1–#4 are. Moved from "next" to last of the numeric set. | journal + Build + Deploy + Victory + Fight | Sonnet, medium |
| 6 | **Ammo / resolve magnitudes / troop & bomber counts / batching tiers** re-derived against the 6→24 hull population | The largest remaining block; wants #1–#3 settled. | journal + Ships + Fleet Memory | Opus, high |
| — | **The ≤4-decision-bearing law** | Unmeasured, and formation persistence adds to the load it must carry (the player now reads *composition*, not just position). Not a session — a prototype question. | — | — |

**Note the reordering:** the three-timer session was "next" as recently as cont.14. It is now **fifth**, because timer lengths have to fit inside a battle whose length is set by the fleet, and the fleet's length is not settled until formation composition and the elimination rule are. Tuning timers before then would mean tuning them against a battle length that is going to move.

### Docs written
Cannons & Towers **v2.4.0** · Ships **v2.4.0** · Victory **v2.4.0**. All three verified: tags balanced, zero dangling anchors, every `class="s X"` variant has a CSS rule, one current-version literal per file, script-free.

---

## SESSION: 2026-09-03 (cont.17) — Formation composition + the elimination rule; both dependency-table items closed

Picked up items **#1 and #2** of the cont.16 dependency table, in the required order. Both greenfield per Victory §3 — no legacy number inherited. Jack ruled on eleven points mid-session; all are now canon above and written into the docs.

### What got designed
- **Three formation kinds** — convoy / **wolfpack** / solo. The core/screen binary broke on the lineages that never escort anything (Corsair, Reaver, Recon picket, Sowing Line); forcing them into "one core plus escorts" needed an invented lead hull, and letting them sail coreless destroyed the coreless-residual read. Jack confirmed the wolfpack as **an attack wave, not an escort**. Purpose-bearing still means cores only, so purpose collapse is untouched.
- **Shields vs riders** — the screen-slot split, with only shields counting toward refusal. Falls out of the cont.16 targeting rule: a screen protects by occupying the position nearest your AoR centre, which a rider does not do. Free deception: a rider-heavy formation looks thick and is not, and it stays fair because the tells already exist.
- **Slot counts derived, not chosen** — one shield slot ≈ one TKP-hull, off Victory §3's TKP(4)=3.7. The axis system already carries the modifier, so no new dial. Shared screens scale sub-linearly for a geometric reason and reproduce Jack's own figure.
- **The screen as a live allocation** — four Jack rulings that turn the screen from a diagram into a behaviour: tightness reads the fleet's confidence in its map (a **fourth belief register**, and baitable), a screen can be a forward **picket line whose job is to draw fire**, escorts reallocate under fire so focus-fire summons a better hull rather than opening a hole, and escort-speed movement is a lost-core tell.
- **Shape reads purpose, expanded** on Jack's note — four independent reads off one glance (geometry / thickness / tightness / quality), an eight-shape table indexed by what each carries plus how each degrades, and two authoring laws.
- **Bomber escort screens** — the grammar goes airborne. The separate HP pool is the load-bearing detail.
- **The elimination rule** — last core slot empty (convoy) / last hull dead or **errand void** (wolfpack). Both rejected alternatives are recorded with reasons. The **two clocks** split (Q shortens, pool weakens) is the cleanest statement of the two routes yet, and it corrected cont.15's refill accounting.
- **Queue composition** — Q = 5 / 11 / 17 with full rosters, and the elimination rate **decomposes** into convoy and wolfpack terms that reconcile with Jack's 3–10 sortie range at all three stages without being fitted to it. That is the strongest verification in the pass.
- **The orphan fork** — Jack asked for revenge and retreat to be balanced; the resolve network already holds the arbiter, so the player's own prior pressure decides which they get, deterministically and with nothing to tune. A surgical kill is more dangerous than a worn-down one.
- **Sortie refusal** — threshold derived from the same unit, with intensity moving it, which makes the **intensity dial structural on the win condition**. The tell was fixed from an absence to a presence: refusing cores loiter visibly in the never-fogged launch zone.
- **The sniper chain** (Jack) — Marksman ignores screens, pays in rate of fire, is confused by a wolfpack. This closed the loop the section was missing: every element answers the one before it and nothing dominates. **The best structural result of the session.**
- **The flag no longer sails first** (Jack) — a marker on a hull with a job, in an ordinary convoy. Removed a queue exception rather than adding one.

### Corrections to previously-locked material
| What | Was | Now | Why |
|---|---|---|---|
| Flag contact cost | "always its own contact" (Victory §3 + Ships §9) | label while screened; its own contact only once separable | The old rule ate the whole C=2 budget every sortie, so no payload could ever arrive. Common fate is the measured criterion. |
| Flag deployment | deploys first, back station, broadcast dormant until assembly | sails inside its convoy, does that convoy's job | Jack's ruling. Assembly window survives, relocated to convoys forming up at the launch zone. |
| Refill cost | "a refill costs a formation-slot the queue can never spend elsewhere" (cont.15) | refills draw hulls from the reserve — screens are paid for in **pool**, not queue depth | Otherwise Q drains two ways and `sorties ≈ Q ÷ elimination rate` stops being true. Jack's intended effect is preserved. |

### Open CALL-OUTS for Jack (written into the docs, not held back)
1. **Does the flag's "slightly buffed" durability+speed survive?** It was justified by the old lone-arrival opening. "Just like any other ship" argues it should go, which would also remove a flat roster asymmetry. Left in place, flagged in Ships §4.
2. **Escort-flight cap (1 per 2 bombers, max 3)** is a derived starting point, not a settled number — an unarmed escort is entity count and flak-time producing no threat, so too generous a cap makes air *slow* rather than dangerous. Belongs with air-density.
3. **The wolfpack is a third noun in a grammar that had two.** Errand-void is the payoff that earns it, but it is the biggest addition of the session and deserves a challenge.
4. **Core count (~10 late) is the softest number here** — it is fitted to a feel target (about one core per sortie of good hunting), where everything else in the composition derives from TKP. If it is wrong, the whole decapitation route's length is wrong.
5. **Shape-reading at overview zoom is unverified.** Nothing establishes that *column* is distinguishable from *picket line* at ~27 pt. The most load-bearing perceptual claim in the section; likely fix is a silhouette or motion cue, not a geometry change.
6. **Sub-linear shared screens may make bundling dominant** if the flexibility costs (one bearing, slowest speed, no feint, Splasher food) do not bite in practice. If they don't, the correction is to make the *contact* cost non-linear rather than to flatten the screen curve.

### Coupling handed forward — the falloff rebuild (table item #3)
Not solved here, per Jack. What is hostage to it: the **slot counts** (4/3/2/1) and the shared-screen numbers, because the shield ≈ TKP-hull unit rides on mean P(hit) ≈ 0.55, which rides on void falloff figures. What is **not** hostage: the three structures, role assignment, sub-linear shared screens, surplus release, exposure × value as the derivation method, the elimination rule, errand-void, the two clocks, the orphan fork, and refusal-at-half-screen. Shape survives; magnitude is void.

**One constraint the falloff rebuild now inherits from this session:** the edge floor decides whether a deep-centred zone can reach a screened core at all. Too low and screens are effectively immune, which kills the primary strategic line; too high and cores are cheap, which kills the screen's reason to exist. The bracket to hold — **a deep-centred 4-gun zone should account for roughly one screened core per two passages at perfect allocation.**

### Docs written
Ships **v2.5.0** (§4 flag deployment + call-out; §8 bomber escort screens; §9 rebuilt — three kinds, shields/riders, 16-lineage role table, derived slot table, live-allocation rulings, shared-screen curve, expanded shape grammar, orphan fork, sniper chain, flag contact correction) · Victory **v2.5.0** (§3 flag contact row corrected; §4a sortie refusal + intensity table + the presence-not-absence tell; §4b the elimination rule, two clocks, queue composition rosters, rate decomposition, sortie composition law) · Fleet Memory **v2.4.0** (§7 purpose is removed never inverted, the orphan fork's resolve arbitration, escort tightness as a fourth belief register). Tag balance verified on all three.

⚠ **NOT written — Cannons & Towers.** The Marksman changes (ignores screens, slower rate of fire, dwells with no core in zone) are Cannon-doc canon and that doc was not in this session. **It is the first thing to write next**, and it pairs naturally with table item #3 (the falloff rebuild), which also lives in that doc.

### Next
Table item **#3 — the falloff rebuild** (edge floor, Coordination increment, mean P(hit)), carrying the Marksman edits and the edge-floor bracket above. Docs: journal + Cannons + Victory. **Opus, medium.** Item #4 (rebuild tax) after it, then #5 (the three phase timers).

---

## SESSION: 2026-09-03 (cont.18) — The falloff rebuild (item #3); core count re-derived; flag buff resolved

Three Jack rulings opened the session, then item #3. The Cannons doc came in, so the cont.17 Marksman debt was paid in the same pass.

### Jack's three rulings
1. **The first flagship IS buffed** — "it is the captain of the team, so there is a reason why. If it fails, the battle promotion on the next sortie does not have the buff." Resolves the cont.17 call-out in the *opposite* direction from my recommendation, and for a better reason than the one I was arguing against: the buff is who the ship is, not a consequence of the old lone-arrival opening. Written into Ships §4.
2. **"Core count at ~10 late is the softest number." → "Then make it harder."** Plus the standing rule now in the panel: *when Jack sights a number it is only a suggestion to the current state* — if a derivation says it should move, move it.
3. **Proceed to item #3** after reading.

### The falloff rebuild — what it produced
- **F is derived, not chosen.** `F = 28% + 12% × coordination`, by inverting the two supply ratios the locked star thresholds already fix. Mixed 28% · pure 40% · Lone Wolf 64% · two LW 88%. The old 25%/+15% were close, and that closeness is recorded as coincidence per the standing rule.
- **Mean P(hit) = 0.69 coordinated / 0.52 default**, superseding ≈0.55. Two formulae now carry it: path-mean `1 − (1−F)/2` for a diametral transit (what throughput uses, because the engagement band was sized to guarantee it) and area-mean `1 − ⅔(1−F)` for default play, which clips the zone instead of crossing it.
- **⚠ Found a real error in previously-locked work.** The bottom-up k₁ route used a 20-grid chord across a radius-8 zone — geometrically impossible, max 16. It was load-bearing: 20 shots × 0.55 = 11 hits = TKP(4) 3.7. So "two independent routes agree" rested on an impossibility.
- **Fixing it strengthened the result.** Correct chord 16 → 16 shots → required mean P rises to 0.69 → which is precisely what a 38–40% floor produces. The mean stopped being an input to route 2 and became its **output**, and **k₁ = 0.46 held**. The cross-check is now stronger than the version that was wrong: route 1 pins k₁ from the stars, route 2 pins the edge floor from k₁, and the falloff numbers are no longer free parameters. This is the best possible outcome of an audit — the constant survived and the derivation got tighter.
- **The screen leak, quantified — and the missing rule found.** "Fire at the highest-probability target," read literally, is an argmax and leaks *nothing*, which would make the screen perfect cover and contradict Jack's own ruling. The rule had to be **probability-proportional selection**, and once it is, the leak computes: 10% of barrels reach a core behind a forward-centred zone (≈1 core per 5 passages), ≈35% behind a deep-centred one (≈1 per passage). That straddles the cont.17 bracket from both sides, so the screen is real *and* the core is reachable. **The cont.16 coupling is closed.**
- **The Marksman, specified** (the cont.17 debt). Absolute screen-ignore, ×1.5 reload, dwells with no core in zone. Its honest output (≈0.36 cores/passage) is *lower* than a deep-centred group's, and that is correct — four barrels beat one. Its value is that it kills cores **without trading away an approach**. That is a better claim than "the sniper is the best core-killer," and it is what completes the four-link counter-chain.

### Core count — 10 → 14 late
Re-derived from throughput rather than feel. The old figure made decapitation land exactly at the end of a *short* battle, so hunting cores won the battle and the banking together. At ≈1.4 core-kills/sortie, 14 cores = 10 sorties, so **pure decapitation now buys the long battle** — it still wins, it no longer wins best — and the 7-sortie battle requires **mixing** routes. The two lines became complements rather than alternatives, at the level of arithmetic instead of only at the level of tools. That is a stronger version of the cont.17 result and it came from Jack refusing to let a soft number stay soft.

Paid for without growing the pool: shields fell. Emergent and not designed in — **a late fleet commits more purpose behind thinner escorts**, so it is more desperate and more brittle at once, and because refusal is measured in shields, **the nerve route opens as the battle goes long.**

Also fell out: **decapitation is not available in Cam 1–6** (2–4 guns cannot deep-centre and still hold an approach) and debuts at 5–8 guns. Introduce → Isolate → Combine applied to the win condition. Handed to Campaign §4.

### Numbers that moved
| Quantity | Was | Now | Cause |
|---|---|---|---|
| Edge floor F | 25% + 15%×coord (chosen) | **28% + 12%×coord (derived)** | Inverted from the two supply ratios |
| Mean P(hit) | ≈0.55 (assumed) | **0.69 / 0.52** | Output of the rebuild |
| Bottom-up chord | 20 grids (impossible) | **16 grids** | Geometry |
| k₁ | 0.46 | **0.46 — unchanged** | Survived the audit |
| Late cores | 10 (fitted to feel) | **14 (derived)** | Jack: make it harder |
| Q | 5 / 11 / 17 | **5 / 10 / 15** | Cores packed into convoys |
| Elimination rate (late) | ≈2–2.5 | **≈1.5–2.1** | A convoy dies only on its *last* core |
| Sorties | 3–10 | **3–10 — unchanged** | Jack's range; the derived terms moved around it |

### Still soft
- **Lone Wolf coordination = 3 is set, not derived.** The other three rungs invert from supply ratios; this one has no anchor, because no shipped game gives a sniper-vs-battery precision ratio to borrow. It is the last chosen number in the falloff chain.
- **The multi-target case could quietly inflate k₁.** With several contacts in one zone, probability-proportional selection raises the per-shot hit rate (there is always a near-centre option) while spreading hits across more hulls. Throughput should be roughly conserved, but "roughly" is doing work — prototype must confirm.
- **The deep-centre figure (≈0.8 cores/passage) is the shakiest number in the leak model.** It depends on when the core arrives at the zone centre relative to its escort, which is formation-geometry-dependent and was estimated rather than derived.
- **≈1.4 core-kills/sortie carries the whole core-count derivation.** It assumes one group hunting and two covering. A player who commits two groups to hunting gets there faster and should — that is the allocation decision working — but it means 14 is calibrated against an assumed doctrine, not a physical limit.

### Docs written
Cannons & Towers **v2.6.0** (§4 falloff rebuild + the derivation box + the chord correction + the revised Coordination table; §5 the probability-proportional selection rule, the leak table, the full Marksman spec, the counter-chain law; §9 Marksman archetype row) · Victory **v2.6.0** (§3 calibration row, route 2 corrected with its own warning box, the soft-flag closed; §4b core count raised with derivation, rosters at 4/9/14 and Q 5/10/15, rate decomposition re-run, the early-decapitation law) · Ships **v2.6.0** (§4 flag buff RESOLVED; §9 the core-density consequences) · journal cont.18. Tag balance and anchors verified on all four.

### Next
Table item **#4 — the rebuild tax** (wall damage per sortie), which is the last missing input to the wall clock and therefore to the race in §2. Docs: journal + Build + Ships + Victory. **Opus, medium.** Then #5 (the three phase timers), which is now genuinely unblocked — the fleet's clock is fully derived.

Two smaller debts worth picking up opportunistically: the **Campaign §4** note that decapitation debuts at 5–8 guns, and the **Lone Wolf coordination = 3** anchor if any real-game precedent turns up.

---

## SESSION: 2026-09-03 (cont.20) — The translation law: real numbers are inputs, not authorities

Jack accepted the cont.19 research and corrected how it must be used: *"Remember that we have to couch it in terms of the game. In the real world, humans die. In the game, bits die. The game has to feel real and always just barely overwhelming."*

### What was wrong with cont.19, precisely
Nothing in the arithmetic. The error was one of **completeness** — I treated a real-world figure as the end of a derivation when it is the beginning of one. The sniper number is the clearest case: 1.5 rounds per kill is not a statement about marksmanship, it is a statement about **survival**. A sniper fires once because a second shot reveals his position and kills him. Import 67% hit probability and you have taken the arithmetic and thrown away the reason it holds.

That matters because **our Marksman has no equivalent stake.** Cannons are static, ammunition is effectively unlimited, and a hull that dies comes back as queue depth. So the number arrived in a world with none of the pressure that produced it.

### The two-step rule, now in the panel
Derivation from the real world is step one. Step two is the **translation check**: what was actually scarce in the real case, what is scarce *here* instead, and which way the asymmetry pushes. The third question has a consistent answer worth stating as a bias: **because bits die cheaply, historically-calibrated pressure feels slacker in-game than it did in life, so err toward the harsher end of the evidence.** Where a real range exists and the design must pick, pick against the player. That reverses the cont.19 instinct of taking midpoints — midpoints are the right estimator for a *quantity*, the wrong one for a *pressure*.

### The felt target, named — and it turns out to already be canon
"Always just barely overwhelming" is now the design's stated target for load, and writing it down revealed it was already the hidden through-line under a whole set of separate rulings: eight contacts as *the destination, not the danger line*; ≤4 decision-bearing as a cap to sit against rather than a budget to underspend; S ≈ 0.55 meaning the fort permanently leaks 45% under perfect play; difficulty rising by the requirement squeezing freedom. **The unifying law: sit at the top of every legible band, never the middle.** That is a better articulation of the design's spine than anything in the panel before it, and it is Jack's phrase, not a synthesis I imposed.

With a test attached: at the widest wave the campaign fields, a player should be able to say what every approach is doing **and have no attention left over while doing it.** Slack means the band is underspent.

And with the red line held: **"barely" is doing the work.** Overwhelming is the target, unfair is a failure, and the existing protections are what separate them — no board punishes a reasonable sampling pattern, every loss is attributable, no board is winnable only by placing fast. Overwhelmed-and-reading is the goal; overwhelmed-and-guessing is a bug.

### Numbers this puts back on the table
No value was changed this session — the law was written first, deliberately, so the re-pricing happens against a stated principle rather than a mood. But three numbers are now flagged as **translated too gently**, and each has its harsher end already recorded in the docs:

| Number | Current | Harsher end already on record | Why it is a candidate |
|---|---|---|---|
| Marksman reload | ×1.5 (≈6 s) | Real deliberate aimed fire has been recorded at just over 3 rpm against a mechanical 15–30 for trained riflemen | The reload — not the accuracy floor — is the true translation of sniper doctrine. It is where "a second shot gets you killed" becomes a game cost, so it is the number that should carry the weight. |
| Lone Wolf floor | 34% (midpoint of 1.3–1.7 rounds/kill) | The *range*, not the midpoint | A midpoint is right for a quantity and wrong for a pressure. Worth re-reading once the reload is settled, since the two trade against each other. |
| Contacts, late | 6–8 target | 8 as the standing late-campaign figure | Jack already ruled "eight is the destination." The ramp should arrive at 8 and *stay* there, not treat 8 as an occasional peak. |

Not moved yet because item #4 (the rebuild tax) is upstream of the felt-load question and will move the timers, and re-pricing twice is worse than re-pricing once.

### ✅ CLOSED (cont.20b) — the two laws are now in The Why
Both are written into **Why §4** as full guiding-principle pillars, not supporting bullets, because they rule choices in and out:
- **The felt target — real, and always just barely overwhelming.** Includes the list of rulings it was already the through-line under (contacts, decision-bearing cap, the 45% permanent supply shortfall, the wall, timers), the sharpened test (say what every approach is doing *and* have no attention left over), and the red line ("overwhelmed-and-reading is the goal; overwhelmed-and-guessing is a bug"). Explicitly read against §6: the design chooses to live at the boundary of its own single point of failure, which is why §6 is a *permanent* risk rather than a solved one.
- **Real numbers are inputs, not authorities — the translation step.** The three questions, the sniper worked example, and the directional bias (choose against the player). Plus the method note that a midpoint is right for a quantity and wrong for a pressure.
- **Also added** as a §4 supporting law: *every number is derived, never arbitrarily set*, with the four-tier source hierarchy and the teeth — a soft number is not one to note, it is one to re-derive.

The closing line of the second pillar is the one worth keeping in view: **real-world anchors are the discipline that stops the felt target becoming a mood, and the translation step is the discipline that stops the anchors becoming a costume.**

**Campaign v2.4.0 (cont.20c) closes the last two owed cross-references — and fixed two inherited errors while doing it.**
- **§3** — the felt target now governs the ramp: aim at the *top* of every band, arrive at the ceiling as late as possible and then *hold* it, and treat leftover headroom in the final campaigns as slack rather than safety. Explicitly does NOT license raising a measured ceiling.
- **§4** — the decapitation debut staged as Introduce → Isolate → Combine applied to the **win condition itself** (Cam 1–6 annihilation/wall-clock only at 2–4 guns → Cam 7–22 decapitation debuts at 5–8 → Cam 23–32 routes must be combined). Flagged the risk: this is the win condition shifting under the player rather than the enemy's mind, so the first huntable core needs a loud tell.
- **⚠ Corrected: queue depth** in the contact-ramp table was still 4–5 / 10–14 / 15–20 → now **4 / 9 / 11**.
- **⚠ Corrected: mean formation size was stated to FALL across the ramp (4→3 hulls). It rises — 4.3 / 4.6 / 5.3.** The old claim's *conclusion* survives by a better route: the late War feels sharper not because formations shrink but because **the hull cap binds before the contact cap**, splitting late sorties into narrow-heavy payload sorties (3–4 contacts) and wide-thin preparation sorties (6–8), so the 8-contact destination is reached precisely when no payload is out to anchor attention.

### Docs written
Journal panel (the two new LOCKED laws, ahead of the derive-everything rule) · Cannons & Towers **v2.8.0**, Ships **v2.8.0**, Victory **v2.8.0** — each real-world anchor now carries its translation note, so no future reader inherits an imported figure without the reason it held. · **The Why v2.4.0** (cont.20b) — both laws promoted to §4 guiding principles plus the derive-everything supporting law.

### Next
Unchanged: table item **#4 — the rebuild tax**. Docs: **journal + Build + Ships + Victory** (The Why and Campaign are both current as of cont.20b/20c). **Opus, medium.** Per the translation law, the anchors to hunt are historical siege breaching rates and Rampart's own wall-damage-per-wave behaviour — and then the step-two question: in a world where a wall is rebuilt every phase and pieces are a drawn hand, what is actually scarce?

---

## SESSION: 2026-09-03 (cont.19) — Both soft numbers derived; two more errors found in settled work

Jack rejected the two "still soft" items from cont.18 outright: *"Every number should be derived, never arbitrarily set"* and *"We need to do the best we can to have real numbers backing our claims. We know facts about humans, game play, wars, and everything else in this game."* Both numbers are now derived from real evidence, and finding that evidence broke two things that were already canon.

### The two numbers

**Lone Wolf floor.** Anchored on US sniper performance in Vietnam — one kill per 1.3–1.7 rounds expended, which is directly our quantity (shots per hit against a designated target). Midpoint 1.5 → P(hit) 0.67 → F = 34% → coordination **0.5**, down from a set 3. I deliberately refused the companion figure (~200,000 rounds per body for infantry on full auto): it is suppression, not aim, so a "1.5 versus 200,000 precision ratio" would be exactly the fake grounding Jack is asking me to avoid.

Two things came out of it that matter more than the value. **The old 2.3 was the best-case sniper used as the baseline** — 1.3 rounds/kill maps to coordination 2.15. That is now a recorded error pattern in the panel, because it is what a "feels right" number usually turns out to be. And **the real data says a sniper's edge is selection, not precision** — 67% single-shot is a good crew, not a magic one. That independently confirms, from Vietnam, the conclusion cont.18 reached from TKP arithmetic alone: the Marksman's value is reach, not throughput. Two routes, no shared quantity, same answer. So "precision baked in" is redefined — a Lone Wolf is **focused, not accurate**, and the tightening is the zone not growing.

**Core-kills per sortie.** The assumption was removable, which is the best kind of fix. The number of hunting groups is not a doctrine I get to assume — it is **forced by the approach limit**: at most 3 live approaches, a late fort of 3 groups, so any group diverted to deep-centred hunting uncovers a bearing outright and buys a degradation tick. Sustainable h=1 → 1.2/sortie; h=2 is a 1–2 sortie burst, not a doctrine. So 1.2 sustained, ≈1.5 with bursts, both terms derived.

### Two more errors in settled work
| What | Was | Now | How it surfaced |
|---|---|---|---|
| Shared-screen curve | shields ∝ cores^0.5, from my ring-circumference argument | **cores^0.775**, from the 1943 convoy OR finding (merchants 32→54, escorts 6→9) | Looking for real escort ratios to check my geometry |
| "Two Lone Wolves grouped → ~90%" | highest floor in the game | **no coordination gain at all; 34%** | §9 already defined Lone Wolf as "penalty when grouped" — both were canon and they were opposite |

The escort-curve correction is the more interesting one. My √x reasoning treated a screen as a ring, and a ring's perimeter really does grow that slowly — but **a real screen is ring plus depth plus detached picket stations, and stations answer bearings, which do not thin out as the formation grows.** That is the same reason Jack ruled in cont.17 that a screen need not be a ring. The two findings arrived from opposite directions and agreed, which is the strongest signal yet that the picket-line ruling was right.

It also cost Jack's own example: six hulls now matches the **two**-core case exactly and undershoots three (which wants nine). Per the suggestions rule, the curve wins and the example moves.

### The genuinely new structural result
Chasing real escort ratios collided three separately-derived limits — 16–24 hulls (Rampart), 6–8 contacts (tracking research), 5–12 hull convoys (convoy history). Eight contacts of real convoys is 60+ hulls, triple the cap.

**That is not a contradiction to patch. It is "a wave may arrive wide and simple, or narrow and clever — never both" becoming physical**, enforced by the hull cap with nothing authored. Payload sorties run 3–4 contacts and 19–24 hulls; preparation sorties run 6–8 contacts and 16–22 hulls. So the 2→8 ramp stands and **8 contacts is reached on preparation sorties** — precisely when the player most needs to read wide, because there is no payload to anchor attention on. And the two sortie kinds became **legible from the wave's silhouette**: wide and thin means no core came out, so the refusal tell and the wave's shape are one signal.

### Also: 14 cores now means pure decapitation cannot finish
14 ÷ 1.2–1.5 = 9.3–11.7 sorties against a cap of 10. Stronger than cont.18's "buys the long battle." Purpose collapse stays a real route — cores plus refusals plus errand-voids closes inside 7–8 sorties — but core-hunting alone no longer does. The boundary is recorded because it is the actual choice: **12 cores finishes exactly at the cap, 14 requires help.** 14 per Jack.

Q fell to **4 / 9 / 11** as a consequence, superseding both 5/11/17 and the original 15–20 late. That bracket was a derived intermediate (pool ÷ an assumed 3 hulls per formation), never a design target, and **Jack's 3–10 sortie range is unchanged at all three stages** — which is the point of the standing rule.

### Provenance audit — where every number in the fleet/fort chain now comes from
| Number | Source |
|---|---|
| Star thresholds (90% / 60%) | Locked design |
| S ≈ 0.55 / 0.25 | Inverted from the thresholds |
| k₁ = 0.46 | Two routes off S, cross-checked |
| Edge floor F = 28% + 12%×coord | Inverted from the two S values |
| Mean P(hit) 0.69 / 0.52 | Output of F |
| Screen leak 10% / 35% | Probability-proportional selection + F |
| Lone Wolf F = 34% | Vietnam sniper rounds-per-kill |
| Shields per core (×0.775) | 1943 convoy operations research |
| Escort-scaled vs not | Four real naval formation doctrines |
| Hulls 16–24, hits-to-kill 3, reload rule | Rampart, shipped |
| Contacts 2→8, ≤4 decision-bearing | Attentive/group tracking literature |
| Core-kills/sortie 1.2–1.5 | Approach limit + leak fraction |
| Board 128×80 | Three independent minima, agreeing |
| **Sorties 3–10** | **Jack — the one remaining judgement call** |

That last row is the right place for the single preference to live: it is a statement about how long a battle should *feel*, and nothing outside the design can answer it.

### Docs written
Cannons & Towers **v2.7.0** (§4 the Lone Wolf derivation box, the two-LW contradiction resolved, revised Coordination table; §5 Marksman reload derived to a kill-time target, output revised to 0.30) · Ships **v2.7.0** (§9 escort curve re-derived at 0.775 with the historical anchor, plus the four-doctrine table for what is and is not escort-scaled) · Victory **v2.7.0** (§4b rosters rebuilt on the real curve, Q = 4/9/11 with the supersede note, core-kill rate derived from the coverage law, the 14-cores consequence, the wide-or-heavy sortie law, rate decomposition re-run, provenance note) · journal cont.19.

### Next
Unchanged: table item **#4 — the rebuild tax** (wall damage per sortie), the last missing input to the wall clock and therefore to the race. Docs: journal + Build + Ships + Victory. **Opus, medium.** Real anchors to look for, per the standing rule: historical siege breaching rates, and Rampart's own wall-damage-per-wave behaviour.

---

---

## ARCHIVE — historical log (pre-2026-08 redesign; preserved for provenance)
*Current canon lives in the module docs + the panel & canon above. Much of the Apr–May 2026 detail below was superseded by the 2026-08 module-doc redesign (cognition-not-stats, the Flutter stack, resolve/intensity, the seed model, the Build extraction). Kept intact so nothing is lost.*

### Coding (not started — design-first)
No code yet: design-first, no hurry to release. Stack = Flutter + Dart + Flame (iOS + Android), IntelliJ. The earlier Swift/SpriteKit phase-by-phase checklist is retired with that stack; a fresh build/architecture plan belongs in the SDD (`Rivenkeep_SDD.html`) once the design is locked.

### v5.0.0 restructure & Critical-Analysis passes (complete)
The v5.0.0 restructure (single-source-of-truth per concept, 10 Parts, cross-references-as-links) and every Critical-Analysis pass (v2, v3, v4 — ~90+ items) are complete. Forward-looking items noted at the time and still live: a map editor tool (laptop app, later); a community map editor + endless/community mode (post-launch); **PvP** as a separate attacker-vs-defender game (out of scope for v1); phased content rollout (Phase 1 = 3 theaters / 50 maps, then full); an App Store listing strategy before submission. The mechanics decisions from this era are superseded by the current canon (module docs).

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

### ▲ REVISIONS — Cannons & Tower doc v1.3.0
- **Archetypes: 16 are OPTIONS → pair to 6–8** (was "→8"). More than 6–8 = undue confusion for little gain. Table columns standardized to **Primary role / Signature quirk / Honest weakness**. **Multi-target PREFERRED over multi-shot** — cut Scatter & Volley (multi-shot); added **Sweeper** (line multi-target) & **Saturation** (wide-weak multi-target). Multi-target family now Splasher/Chain/Sweeper/Saturation → keep only 1–2. Three Lone Wolves unchanged (Piercer, Marksman, Disabler).
- **Grouping adjacency:** cannons that touch **side-by-side (orthogonal)** form a group. **Pure diagonal does NOT group** until a 3rd cannon touches both → then all 3 become one group. Same rule for towers.
- **One active tower per group:** if two towers touch the same group, **last-moved wins**; the other(s) **gray out with an icon**. Move the winner away and a grayed tower takes over. No stacking.
- **Lone Wolf grouping + falloff:** two Lone Wolves CAN group but **AoR size stays the same** (doesn't grow). LW falloff is tighter: **100% centre → 60% edge** (one LW), **90% edge** (two LW grouped) — vs 25% edge for normal cannons. LW = precision/reliability (small hard-edged circle) vs normal = big soft-edged zone.
- **AoR is ALWAYS A CIRCLE → spatial tension (3rd tension axis).** Few big circles leave scalloped gaps along a straight coast + waste coverage seaward; a **line of small overlapping circles** hugs the shore as a clean defensive wall. Tension now runs on 3 axes: domain (one big group = 1 domain), direction (1 zone = 1 approach), shape (circles tile a line better when small).
- **Fight verbs now 3 command-verbs + Abilities:** (A) re-task AoR, (B) switch domain, (C) **FIRE CONTROL — hold / weapons-free** (NEW). Fire-control motivated by the **"crazy Ivan"**: a ship jukes evasively when hit, so your FIRST volley is cleanest → **hold until the ship reaches the high-% centre, then alpha-strike before it evades.** This ties falloff + crazy-Ivan + hold into ONE commander decision (timing, not aiming) and makes falloff something you actively play. Cancel→immediate fire; AoR-move + domain-switch stack. **Abilities = cannon-focused Stonwryt boosts only** (buff guns, not walls/economy), occasional by cost. **HONEST FLAG logged in doc:** verb load is near the "watch & nudge" ceiling — mitigate by setting domain + fire-control in Deploy; if the Fight feels busy, demote a verb to a Deploy standing order; do NOT add a 4th live verb.
- **FOG OF WAR resolution (PROPOSED, needs prototyping — ties to Ships doc):** a group that can't see a contact fires **speculative/blind into its AoR at a heavy penalty**; a **blind hit REVEALS** the ship, penalty drops, group **concentrates** at normal falloff (blind bombardment → contact → focus fire). **Spotter** (passive fog-lift) and the new **Flare tower** (active illumination pulse over the AoR) reveal pre-emptively. Fog blunts the **Marksman** (can't pick unseen priority) until a reveal; **hold-fire in fog** = don't burn ammo blind, wait for a reveal then strike. Fog makes information the scarce resource. Open tuning: blind-penalty severity, reveal duration, and no blind fire in the very early game.
- **Flare tower ADDED** (11th tower candidate): fires flares over the AoR to illuminate ships hidden in fog — the *active* fog-reveal vs Spotter's *passive* lift. Towers now **11 → pair to ~6**.
- **Mini-games = full "CANDY CRUSH" casual layer:** **generatively/procedurally harder** (endless, since a player may live here); **NOT leaderboard-ranked so RNG is fine** (unlike deterministic battles); the **main early Stonwryt earner** and home for **more frequent (rewarded) ads** — earn up front so battles carry fewer ads; also the **practice sandbox**; and **user-generated boards** with **creator rewards** + best community boards **promoted into the game**. UGC flagged as a big separate later milestone (needs builder tool + sharing/discovery + moderation — reuse on-device content moderation).
- **Failure timing:** first LOSS tuned to land around the **5th–8th sortie** of play (after a few easy wins) — teach early that failure is a normal, fun learning tool ("fail several times, inch closer, then it clicks").
- Doc version: Cannons & Tower **v1.3.0**.

### ▲ REVISIONS — Cannons & Tower doc v1.4.0
- **VERB BUDGET protected: Abilities REMOVED from the Fight → parked to Future.** Fight is now **3 command-verbs only** (re-task AoR, switch domain, fire-control). Two of the three (domain + fire-control) are normally set in Deploy, so live play is mostly AoR re-tasking. **Hard rule: do NOT add a 4th live verb.** (Abilities = cannon-focused Stonwryt boosts, revisit only if the Fight proves it has room.)
- **UGC mini-game boards → Future** (way down the road; idea held, not scoped). Removed from the mini-games section, recorded in Future.
- **Tower touches exactly ONE group.** If a tower touches **two** groups they **FUSE into one big group** — the tower is a bridge, like a bridging cannon. This holds **even if the tower is grayed out** (physical touch merges groups; active/inactive only decides whose buff applies).
- **Pieces are 2×2; grouping needs only ONE cell-edge of side contact** (footprints may sit offset — not both edge-cells, not a full aligned edge). Corner-only (pure diagonal) still doesn't group until bridged.
- **Default targeting = highest hit probability:** with several targets in the AoR, cannons prefer the one nearest **centre** (high %) over an edge target. Special personality archetypes (Marksman = highest-value, Interdictor = nearest-wall, Finisher = lowest-HP) OVERRIDE this default. Reinforces hold-fire (a centred ship is both the high-% shot and the preferred one).
- **Battery bonus (pure same-type group):** edge accuracy rises 25% → **~40%** (tune). Accuracy ladder: mixed group ~25% edge → pure group ~40% → Lone Wolf 60% (solo) / 90% (pair). Concrete payoff of the Battery tag; weighed against giving up domain-mix coverage.
- **Large-group advantage:** one tower buffs the WHOLE group, so the single 2×2 tower slot pays off across every cannon — another reason to consolidate (counterweighted by the circle/shape spatial tension).
- **Fog of war refinements:** every shot **thins the fog a little**; a **hit OR a near-miss reveals** a ship; a **ship that fires reveals itself** for a duration (muzzle flash). Net effect: fog burns off as the engagement heats up — an opening-moments condition, not a permanent blindfold. Spotter (passive) + Flare (active pulse) still pre-empt it. Still a proposal pending fog-theater prototyping.
- Doc version: Cannons & Tower **v1.4.0**.

### ▲ REVISIONS — Cannons & Tower doc v1.5.0 (elegance pass — "generating functions")
- **Accuracy ladder → ONE stat, "Coordination."** The four hand-set edge values are now one generating rule: **F (edge floor) = 25% + 15% × coordination, soft-capped <100%.** Mixed group 0→~25%; pure same-type ~1→~40%; Lone Wolf (precision baked in) ~2.3→~60%; two Lone Wolves ~4.3→~90%. Collapses the Battery bonus + pure-group bonus + lone-wolf falloff into ONE mechanic (exceptions become the same line at different inputs); a bigger battery raises its own floor for free. **Render it as a GROWING BRIGHT CORE, not a higher edge number** — same math, but the high-accuracy centre visibly bulges outward, which is both more elegant AND more legible (directly addresses the "can players perceive the probability?" risk).
- **Towers → ONE AMPLIFIER PER SUBSYSTEM.** Gave towers the generating structure cannons already had (archetype × domain). Six subsystem axes, one tower each, zero overlap: **Coverage** (Spotter/grow AoR), **Output** (Powder Store OR Magazine OR Sights — pick one), **Sustain** (Stonewright Post OR Bulwark OR Decoy Mast), **Tempo** (Forge OR Rally Flag), **Reveal** (Flare; Spotter passive), **Control** (Jammer). Pair-down = keep the AXES fixed, pick the best EXPRESSION per axis against the ships, and DROP any axis no enemy stresses. Towers are now a system, not an 11-item list.
- **Domain switch = validation target (not changed yet).** Recorded as the key open question: the switch carries heavy rules-weight (restartable/stackable/cancelable/countdown) for a mostly set-in-Deploy lever. The **ships/troops/bombers must justify it** with enough telegraphed "switch moments" (bomber run = archetype). The Ships session is the validation pass; if we can't invent enough switch-moments, the mechanic sheds rules to match real usage.
- Doc version: Cannons & Tower **v1.5.0**.

### ▲ REVISIONS — Cannons & Tower doc v1.6.0
- **Multiple towers per group, one active — priority stack for RESILIENCE.** A group may hold several towers; only #1 is active, the rest are grayed backups. Order set in Deploy by **last-tap** (placing or tapping a tower makes it #1, pushes old #1 → #2, etc.). Because towers are destructible + enemy-prioritized, backups are **insurance**: kill the active tower → next **auto-promotes**. Cost = fort space + barrels. Only one buff applies at a time (no stacking). Supersedes the old "one tower per group, last-moved wins, others gray out." (Tower-bridges-two-groups-merges rule unchanged.)
- **Manual live tower-switch = PARKED variant.** Shipping behaviour = auto-promote on destruction only (no live verb). IF we later add tap-to-swap-active mid-Fight, it costs a **warm-up window where NEITHER buff applies** (mirrors domain reload — adaptation keeps a price). Parked to avoid a 4th live verb; revisit after M4.
- Doc version: Cannons & Tower **v1.6.0**.

### ▲ REVISIONS — Cannons & Tower doc v1.7.0
- **Domain-switch cancel now REVERSES (not instant).** Cancelling a domain switch counts the meter **back up** to loaded before the guns fire (the pulled ammo must be re-seated). 8-count: cancel at 6-remaining → climbs 6→8 then fires original; cancel at 2 → climbs 2→…→8. Bailing late is expensive → a switch is a real commitment. **AoR-move cancel stays INSTANT** (aiming is free to abandon) — deliberate asymmetry: aim vs ammo.
- **Third-domain rule (Land→Sea then want Air):** re-selecting your **original** domain = **reverse** (cancel); picking any **different** domain = **restart a fresh full count** to the new one (partial work spent). Simple rule: *your own domain = reverse, a different domain = restart.* Honest flag in doc: reverse+restart can balloon silent time if you flip-flop (intended — enforces set-in-Deploy — but the countdown UI must make the cost legible before tuning down).
- **Camouflage tower = another SUSTAIN expression.** A tower that hides the group so the enemy can't target it → survivability. Correctly collapses into the Sustain axis (with Stonewright/repair, Bulwark/armour, Decoy/draw-fire). Good demonstration of the subsystem framework absorbing a new idea instead of adding an axis.
- **Mini-Games section REMOVED from the cannon doc → belongs in the GDD (and probably its own doc).** Determinism & Mastery-Loop section also REMOVED → GDD. The cannon doc is now purely defender mechanics. Content preserved below + in earlier revision blocks so nothing is lost.
- Doc version: Cannons & Tower **v1.7.0**.

#### MOVED-OUT CONTENT (transplant to GDD / own doc) — captured so it isn't lost
**Mini-games (the "Candy Crush" casual layer):** several per skill on a climbing ladder; **generatively/procedurally harder** (a player may live here); **NOT leaderboard-ranked so RNG is fine**; the **main early Stonwryt earner** + home for **more frequent rewarded ads** (earn up front → battles carry fewer ads); also the **practice sandbox**; deepen by combining phases until the top of the ladder **IS Campaign 1 Battle 1** ("wait, this is easy," no cliff); teach transferable mechanics only. FUTURE: user-generated boards (creator rewards, best promoted in) — way down the road, own builder+sharing+moderation project.
**Determinism & the Mastery Loop:** Fight skill = reading + adapting, not reflexes. Deterministic crises → loop: *plan → watch tested → get hit → learn why → fold into next Deploy → win.* First LOSS tuned to ~**5th–8th sortie** (after a few easy wins; teach that failure is a fun learning tool). Failure CHEAP — never drains permanent Stonwryts/upgrades, only that-run consumables; instant retry; identical crisis rewards the learner. **Post-battle AI debrief** = the coach ("east group sat idle while west fell at tick 40 — pre-task west"). A perfectly-planned battle needs ~zero Fight input; 3-lever star system rewards plan quality (turtle / perfect-defence / annihilation).

### ▲ REVISIONS — Cannons & Tower doc v1.8.0 + GDD v6.2.5
- **Third-domain switch = LONGER PATH rule (replaces the earlier "restart" idea).** Mid-reload, picking a third domain travels whichever path is farther — keep counting DOWN to 0, or reverse UP to 8 — then the new domain loads at the end. Example (8-count): at 6-left → down-path 6 > up-path 2 → continue down to 0, load Air; at 3-left → up-path 5 > down-path 3 → climb back to 8 first. Makes a third-domain change always the most expensive move (can't shortcut indecision) and reuses the same meter animation (no new UI primitive). Re-selecting the ORIGINAL domain is still the plain reverse (cancel). Caveat logged: meter travelling up vs down for the same "switch to Air" tap must be visually legible or it reads as arbitrary.
- **GDD v6.2.5:** added a prominent gold "⚑ Module Docs & To-Develop" callout at the top of Game Overview. It (1) points to the Cannon & Tower module as current source of truth for the defender combat model — noting it SUPERSEDES the GDD's old "Tap a ship to focus fire" targeting; (2) flags **Mini-Games as TO DEVELOP / needs its own doc** — "almost its own app" — and notes it REVERSES the GDD's stale "no mini-games outside core mechanics" line; (3) flags **Determinism & Mastery Loop as TO INTEGRATE**, full text preserved in this journal's MOVED-OUT CONTENT.
- **KNOWN GDD DRIFT (future reconciliation session):** the GDD (v6.2.5) still contains pre-cannon-redesign content that contradicts the module — e.g. per-ship "tap to focus fire" targeting (old model), and "no mini-games." The callout flags this; a full GDD reconciliation pass is a future task. Also: GDD has a pre-existing div imbalance (315/316) unrelated to the callout — cosmetic, browsers tolerate it; leave unless doing a full GDD cleanup.
- **Cross-refs synced:** cannon doc meta now reads "Module of the GDD (v6.2.5)."
- Doc versions: Cannons & Tower **v1.8.0**, GDD **v6.2.5**.

### ▲ REVISIONS — Cannons & Tower doc v1.9.0
- **Domain-switch UI concept recorded:** a two-ended **slider between Land/Sea/Air icons** (each a colour+icon), a marker that travels between them, a tray filling with the loading domain's colour; cancel slides back; a third-domain pick relabels the end the marker heads toward (far end of the longer path). This makes the up-vs-down "longer path" travel read as purposeful, not arbitrary — resolves the legibility caveat.
- **NEW SECTION §8 "Cannon Health, Nurture & Veterans"** — folded in from the GDD's combat design (see migration review below), reconciled to the new model: HP degrades effectiveness on an inverted-logistic curve (damaged cannon → less Coordination + firepower); between sorties, surviving/**enclosed**/held-position cannons are nurtured above 100% up to a 200% veteran cap; veterans carry **within a campaign** (reset between campaigns). Ties HP to the Coordination stat (one currency), and rewards enclosure a THIRD time (protection + victory + veteran growth). Distinct from permanent per-archetype Stonwryt mastery. Sections renumbered (Archetypes 9, Towers 10, Future 11, Open 12); nav gains "Health."
- Doc version: Cannons & Tower **v1.9.0**.

### GDD → CANNON DOC — MIGRATION REVIEW (answering "what should move / what did we forget")
**FOLDED IN NOW (v1.9.0):** the Cannon Health / Nurture / Veteran system (the big missing defender mechanic).
**SHOULD MIGRATE during the GDD reconciliation session (after ships/troops/mini-games):**
1. **Cannon slot economy** — starting/max cannon counts (formulas), earning slots by Fight performance (≥50% / clean-sweep bonuses), slot rollover. Defender progression within a battle.
2. **Cannon type deployment limits** — per-battle cap per type (production-capacity lore) that FORCES diversity ("can't fill all slots with one type"). Pairs perfectly with the 8×3 matrix / anti-dominant-archetype goal. (Also captured as a forgotten-idea below.)
3. **Cannon placement rules** — 2×2 footprint (matches), previous-sortie persistence, trashing/recovery, invalid-position destruction. NOTE CONFLICT: GDD forbids cannons on fragile grids; new doc said "no placement constraints, all cannons play all boards." Resolve which stands.
4. **Base-unit balance framework** — all balance from 4 base numbers (Wall HP 100, Std Cannon dmg 25, Warship dmg 15, tick 4t=2s); eDPS = (dmg/reload)×accuracy. The method to balance the archetypes later.
5. **Old cannon roster as a spec reference** for the new archetypes: Standard, Scatter(→multi-shot, we deprioritized), Long(range→cut), Fire(→Burner), Mortar(lob→now universal), Chain(→Chain), Healing(→now the Stonewright/Sustain TOWER, good consolidation), Lightning(→glass-cannon/Piercer flavour, "takes 2× damage" vulnerability idea), Mirror(bounce/Crystal-theater trick), Doom(→heavy/Marksman-ish 2×2 alpha). Use these when speccing the 6–8 finalists.

**CONFLICTS — the new doc SUPERSEDES the GDD (flag in reconciliation):**
- **Control model:** GDD's "three firing modes" (auto-fire nearest / hold-fire on a point / **touch-lock tap-a-ship**) is the OLD per-ship targeting. The new **AoR + domain + fire-control** model replaces it entirely. (Callout already flags "tap to focus fire" as superseded.)
- **Range:** GDD lists range stats (grids) BUT already reframes range as "arrival speed, not reach — cannons never fall short, all in range hit" — which is basically our "AoR = the reach." New doc removed range entirely; keep it removed.

**GOOD IDEAS WE'D FORGOTTEN (surfaced for later consideration):**
- **Cannon HP nurture / veterans** — DONE (folded in v1.9.0).
- **HP→effectiveness degradation curve** (inverted logistic) — DONE (in the new §8).
- **Deployment-limit diversity** — strong pairing with the matrix; migrate (see #2). Prevents spamming one archetype without a hard rule.
- **Crazy Ivan already defined in the GDD** — near-miss/hit within 1 grid triggers it, slight delay, lateral juke, **lighter ships more prone**. CONSISTENT with our fire-control motivation AND our fog "near-miss reveals" refinement (GDD near-miss = within 1 grid). Keep aligned when writing the Ships doc.
- **Shot trajectory / arrival timing** — GDD has arc height = travel time (high arc = slower arrival; "cannons never fall short"). We removed range, but *arrival timing* is a distinct, still-usable texture (different archetypes' shells land at different delays) that could add depth to the hold-fire/alpha-strike decision. Consider for the archetype spec.
- **Ship stacking** (multiple ships share a grid, hidden count, splash hits all) — enemy mechanic for the SHIPS session; interacts with our multi-target archetypes + fog hidden-count.
- **No-cannon desperate option** (Fight with zero cannons is valid) — small freedom worth keeping.
- **Healing Cannon → Stonewright/Sustain tower** — the new subsystem framework already absorbed this; note it as a resolved consolidation.

**RECONCILIATION PLAN (user):** after ships + troops + mini-games docs are done, reconcile the GDD — mostly REMOVE the superseded combat sections and replace with LINKS to the module docs. GDD callout (v6.2.5) already flags the drift and the to-develop items.

### ▲ REVISIONS — Cannons & Tower doc v1.9.1
- **Fragile-grid placement rule LOCKED (kept from GDD).** A cannon's 2×2 footprint cannot sit on a fragile grid (ice, crust, crag, bog, fissure, fract) — too heavy for the ground. Framed to resolve the earlier apparent contradiction: this restricts *where on a board* a cannon sits (terrain property), NOT *which cannons* can play a board — no cannon type is ever locked out. It is the ONLY placement constraint. (Resolves the conflict flagged in the migration review.)
- Doc version: Cannons & Tower **v1.9.1**. **Defender design considered essentially complete — ready to move on to the Ships (bestiary) session.**

### ★ TOUCHSTONE — "Edge of Tomorrow" (Live/Die/Repeat)
User's north star for the game's soul: **each loop we learn from the past.** This IS the determinism thesis — the world resets identically every loop, death is cheap, and the only thing that carries across loops is the player's *knowledge*. The player doesn't get stronger; they get smarter about an unchanging puzzle (Cage learning the fixed sequence). Maps directly to: deterministic crises → fail → learn the pattern → fold into next Deploy → win. Failure is the core verb, not a punishment. Use this as the emotional touchstone when writing the mastery-loop content in the GDD.

### GROK CONTROL MOCKUP — feedback (for the domain-switch UI, still "not final")
Grok generated a "CANNON CONFIG" mockup of the domain switch. Verdict:
- **KEEP:** the three domain **icons** (mountain = Land, wave = Sea, raptor = Air) — strong, readable domain identity beyond colour; adopt as the domain visual language. Also keep the CURRENT / TARGET state labels, the per-domain colour, and the 8→0 numerals + fill on the track. (Palette note: our doc tags use Land = green #8bc34a, Sea = cyan #4fc3f7, Air = purple #ce93d8; Grok used Land = amber, Sea = grey, Air = blue — reconcile to our palette or revisit.)
- **DROP:** the "NOT TARGET" label (idle domains should just dim), and the "STABLE/LAND" shield + "LOCK/AIR" side buttons (invent a stability state + manual lock we don't have — clutter).
- **⚠ SIGNAL:** Grok's caption ("switched to Air early… 5,4,3,2,1,0 becomes AIR") used the SIMPLE "just keep counting down" model and did NOT represent our late-switch **reverse (longer-path)** behaviour. An intelligent system asked to visualise the rule defaulted to the simpler one and dropped the reversal — a yellow flag that the longer-path rule may be too clever to read. NOT changing it now, but **"longer-path vs. just-continue-the-count" is a top item to settle in the M4 prototype.** (For an *early* switch, both models agree; only the late-switch reversal differs.)

**DESIGN PHILOSOPHY (user, explicit):** prefers "too much that can be edited down" over "too little and unimaginative." The design phase is for dreaming big and exploring; parked ideas are kept because they may inspire others. If the game never ships, that's OK — the design is fun in itself. North star for this phase = **elegance: everything feels natural and fits together** (evaluate for coherence/fit, not scope). Assistant should be in explore-mode and save scope-scolding for explicit pair-down asks. Design's recurring signature to preserve: the same principle expressed across many layers (coverage-vs-concentration; lob→enclose→victory; falloff+crazy-Ivan+hold). **190 boards plan:** define board 1 + board 190 (hardest), interpolate between — treat difficulty as a small vector of parameters (AoR scaling, falloff, threat tempo, approaches, fog density, domain pressure); campaign = a path through that space; theaters = regions; bosses = spikes. (Future session.)

---