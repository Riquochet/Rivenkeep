# Rivenkeep

A single-player iOS fortress-defense game — Swift + SpriteKit — that modernizes the classic *Rampart* **Build → Deploy → Fight** loop into a deep, replayable campaign. You wall in castles to claim territory, deploy cannons, and defend against escalating fleets and landing troops across 190 battles, 10 theaters, and a boss finale.

**Studio:** Riquochet Studios

## The one design pillar: determinism

Every battle is **identical for every player on every run** — same maps, spawns, and enemy behavior. That is what makes the puzzle learnable, the leaderboards fair, and replays shareable, and it dictates the entire architecture: a pure-Swift deterministic simulation core (seeded RNG, fixed tick) kept strictly separate from the SpriteKit render layer. AI features (below) enhance the experience *around* the game but never touch the simulation.

## Documents

| File | What it is | Internal version |
|------|------------|------------------|
| `Rivenkeep_GDD.html` | **Game Design Document** — the source of truth. Every system, economy, monetization stream, UI, challenge, leaderboard, backend, and the AI-Enhanced Experience layer. | v6.2.4 |
| `Rivenkeep_SDD.html` | **Software Design Document & Build Plan** — architecture, asset pipeline, milestones M0–M12, testing strategy, and ready-to-paste Windsurf/Claude prompts. An interactive checklist (progress saves locally in the browser). | v1.0.2 |
| `Rivenkeep_Critical_Analysis_Definitive.html` | Live issue tracker — 62 resolved, 16 open. | re: GDD v6.2.4 |
| `Rivenkeep_Balance_Analysis.html` | Numbers-first balance audit vs. game-balance theory + Rampart (cannon cost curve, TTK/timer math, difficulty scaling, economy). 3 P0 / 4 P1 / 5 P2 findings. | — |
| `RIVENKEEP_JOURNAL.md` | Cross-session decision history + changelog + handoff. | — |

> Open the `.html` files in any browser. The SDD checklist persists your check-offs via the browser's local storage.

## Versioning

Versions are tracked **inside each document** (title/footer + the SDD changelog) and via **git history** — filenames stay stable so diffs remain meaningful. Do not put version numbers in filenames.

## Tech stack (planned)

Swift 5.9+ · SpriteKit (render) · GameplayKit (`GKGridGraph` weighted A*, `GKStateMachine`, seeded `GKMersenneTwisterRandomSource`) · CloudKit (save sync) · GameKit (leaderboards) · Firebase (analytics, Remote Config, Crashlytics) · StoreKit 2 · Apple Foundation Models (on-device AI: moderation, debrief, tutor, flavor — never the simulation). Built with Xcode; authored with the Windsurf Claude plugin.

## Where to start

1. Read `Rivenkeep_GDD.html` for *what* the game is.
2. Read `Rivenkeep_SDD.html` for *how* to build it, in order, starting at milestone **M0**.
3. `RIVENKEEP_JOURNAL.md` has the full decision history if you need context on a past choice.

## Status

Design phase complete. The SDD is the active build plan; implementation begins at M0 (foundations + the deterministic tick loop).
