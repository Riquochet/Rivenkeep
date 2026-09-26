# Making a Computer Fleet Feel Like a Human Commander

Research for Rivenkeep: how the Mystaeri fleet can feel intentional, coordinated, deceptive and adaptive while staying deterministic, blind, readable and fair.

Prepared 2026-09-25 for Jack's stratagem and Fight-control work.

---

## 0. How to read this

**What was asked.** How shipped games and game-AI practitioners make a computer opponent feel like a human commander, covering 13 named sources. Then 12 to 20 principles for Rivenkeep: a deterministic, blind Mystaeri fleet. Its commander picks a stratagem between sorties, and its formations carry that stratagem out using their own local judgment.

**Confidence tags** (they appear after each claim):

- **[V]**: verified this session against the primary source (the paper, slides or official page).
- **[S]**: verified this session against a reputable secondary source (a Game Developer article, AI and Games, Game Studies, a patent report, an official wiki).
- **[M]**: from memory and not re-checked this session. Probably right, but check it before quoting it in a design doc.
- **[U]**: uncertain or disputed. A claim is marked [U] when one source says it and no other confirmed it.

**On quoting.** I paraphrase almost everything. Where a talk's own terms matter (such as "structured unpredictability"), I use them as names, not as quotations.

**Vocabulary used below.** These terms come from the current Fleet Memory and Ships docs. **LOS / Contact / Effect** are the three knowledge channels. The **fear grid** is the Effect channel. **Resolve** is read through motion. The **Flagship** is field-promoted when it dies. **Convoy / Wolfpack / Solo** are the formation kinds. The **Build/Deploy "bait window"** falls between sorties. **Mystarchs** are the bosses. **Stratagem** is the new layer Jack asked for. It is the thing the current docs call the "next-sortie plan" but never define.

---

## 1. Case studies

Each entry covers the same four things: the technique, why it reads as human, what Rivenkeep should take from it, and the citation.

### 1.1 F.E.A.R.: planning soldiers, squad "barks", and complexity that isn't there (Monolith, 2005)

**Technique.**
- **Individuals.** Each soldier runs a tiny three-state machine (Goto, Animate, UseSmartObject). A STRIPS-style planner searches with A* for a sequence of actions that meets the soldier's current goal. [V]
- **Squads.** A separate, informal layer sits above the soldiers. A global coordinator periodically regroups soldiers into squads by proximity. [V]
- **Four simple squad behaviours:**
  - get-to-cover while one soldier suppresses;
  - advance-cover;
  - orderly-advance in single file, the last man facing backwards;
  - search in covering pairs. [V]
- **How a squad behaviour runs:**
  1. It looks for soldiers who can fill its slots.
  2. It sends them orders.
  3. Each soldier weighs the order against his own goals. A grenade can make fleeing outrank obeying.
  4. The squad behaviour watches whether the orders succeed or fail. [V]

**The key admissions (paper, pp. 14–16).**
- F.E.A.R. had **no complex squad behaviours at all**. Apparent flanking, coordinated strikes and retreats emerged from simple squad orders meeting individual planning. A soldier sent to the only valid cover he knows of may take a back route and come out on the player's side. That looks like a flank. [V]
- **Dialogue is chosen after the fact.** Once the squad layer has decided what will happen, it looks at the situation from above and picks a matching line. Players on forums praised soldiers who "actually do what they're told". Orkin notes that it is smoke and mirrors. [V]
- **Voicing an intention can be enough without implementing it.** The last survivor calls for reinforcements. There is no reinforcement system, but the next enemies the player meets get read as the reinforcements. [V]
- **Prefer two-voice exchanges to announcements.** When a soldier is hit, a squadmate asks his status and he answers. When they search, one asks and another reports. [V]
- **Use dialogue to explain inaction.** A soldier who fails to reposition says he has nowhere to go, so he reads as trapped rather than stupid. [V]
- Orkin also says it is the separation between individual planning and squad planning that matters, more than any particular algorithm. [V]

**Why it reads as human.** Orders are spoken out loud, other soldiers acknowledge them, and actions visibly follow. Players credit the squad with a shared plan. Individuals can also refuse an order (by fleeing), and that makes them feel like people rather than puppets.

**Rivenkeep takeaways.**
1. Split the commander (the stratagem) from the formations (local execution). Let formations weigh the order against their own resolve and fear, and let them refuse it visibly.
2. Barks are an output-only view of decisions that have already been made. They are chosen after the decision, so they never feed back into the simulation, and determinism is untouched.
3. Voice intentions and explain hesitation.

**Citation.** Jeff Orkin, "Three States and a Plan: The A.I. of F.E.A.R.", GDC 2006. Paper: https://www.gamedevs.org/uploads/three-states-plan-ai-of-fear.pdf. Vault: https://gdcvault.com/play/1013282/Three-States-and-a-Plan. The squad-behaviour design cites Evans & Barnet, "Social Activities: Implementing Wittgenstein", GDC 2002. [V]

---

### 1.2 Halo: readable enemies, "tougher = smarter", and no dice (Bungie, 2001–2007)

**Halo: Combat Evolved (the GDC 2002 talk).** The slides were read in full.

**Split of responsibility:**
- **Design** owns a roughly 3-minute scope: racial personalities and strategic purpose.
- **Code** owns a roughly 30-second scope: intelligent decisions and instant reactions. [V]

**Design goals:** intelligible, interactive, unpredictable. [V] The player should be:
- *impressed*: the AI reacts to the player with surprise, anger or awe;
- able to *fool* it: it has limited knowledge and predictable reactions;
- able to *thwart* it: it has a breaking point, after which it flees in terror, goes berserk, retreats or turns defensive. [V]

**What they deliberately discarded:**
- **Randomness.** Unpredictability was meant to come from reactive AI: an unpredictable player creates unpredictable situations, which produce unpredictable reactions. They also used "analog" reactions, where position and timing vary continuously. [V] This is almost exactly Jack's principle 1.
- **Hidden states.** Instead, inform the player through language, posture, gesture, visible focus of attention, dialogue and animation, all serving "communication of intent". [V]
- **A complete world model.** Instead, individual knowledge: "no cheating" senses, selective memory, persistent state, and an AI that can be fooled. [V] The senses listed are vision, hearing, touch and "ESP". I read ESP as a designer-controlled knowledge channel. [U]

**Races as learnable personalities.**
- Grunts flee easily.
- Elites seek cover when hurt.
- Jackals carry shields. [V]
- Grunts panic when their Elite leader dies. [S]

**Combat dialogue.** Lines are selected from decisions and stimuli, with nearby characters able to reply. The talk gives 57 events, 166 dialogue types, 12 speaking characters and 5,147 recorded lines, all "used for flavor only". [V]

**The famous playtest.** The talk's playtest slide compares a weak-enemy build with a tough-enemy build (the same AI with more health). [V]

| Playtest build | Rated "very intelligent" | Rated "not intelligent" | Rated difficulty "about right" |
|---|---|---|---|
| Weak enemies | 8% | 20% | 52% |
| Tough enemies (more health) | 43% | 0% | 92% |

The slide labels the finding both ways: smarter = tougher, and tougher = smarter.

**Things to avoid:** subtlety, looking broken, insufficient challenge. **Things to refine:** communication, animations, engagement distances. [V]

**Halo 2 (Isla, GDC 2005).** The first shipped use of behaviour trees in a commercial game, aimed at a scalable, directable brain with a clear player experience. [S]

**Halo 3 (Isla, GDC 2008), the "Objectives" system.**
- Designers author a tree of **tasks**. Each task has a priority, activation and exhaustion conditions (for example, a death count), a capacity limit, and filters (for example, snipers only, or vehicles only). [S]
- **Squads** trickle down the tree and fill the highest-priority open tasks. When a task is exhausted they fall to the next, and when a higher task opens they are pulled back up. [S]
- The designer is "the coach calling plays". The squads play them autonomously. [S]
- Encounters progress from initial position to fall-back to last stand. A leader's death "breaks" its followers. [S]

**Why it reads as human.** Bungie says it plainly: the AI must be intelligible, or it might as well not be there. Hierarchy (leaders and followers) and a breaking point read as a society. Toughness buys the AI enough screen time to be seen thinking.

**Rivenkeep takeaways.**
1. **The Halo 3 task tree is almost a spec for "commander picks a stratagem, formations fill its roles".** A stratagem is a small tree of prioritised tasks with capacities and exhaustion conditions. Formations fill the tasks by fit, and they fall back when a task is exhausted.
2. **Durability is a readability lever, not only a difficulty lever.** Keep the formation carrying the idea alive long enough to show it.
3. **Discard randomness and discard hidden states.** Both are already in Jack's vision, and Halo is the strongest precedent for them.

**Citations.**
- Chris Butcher & Jaime Griesemer, "The Illusion of Intelligence: The Integration of AI and Level Design in Halo", GDC 2002. Slides: https://www.jmeiners.com/shamans/papers/ai/the_illusion_of_intelligence.pdf. Vault: https://gdcvault.com/play/1022590/Creating-the-Illusion-of-Intelligence [V]
- Damian Isla, "Handling Complexity in the Halo 2 AI", GDC 2005: https://www.gamedeveloper.com/programming/gdc-2005-proceeding-handling-complexity-in-the-i-halo-2-i-ai [S]
- Damian Isla, "Building a Better Battle: HALO 3 AI Objectives", GDC 2008. https://gdcvault.com/play/497/Building-a-Better-Battle-HALO. Slides: https://web.cs.wpi.edu/~rich/courses/imgd4000-d09/lectures/halo3.pdf. Notes: https://aarmstrong.org/journal/2008/03/02/gdc08-notes-building-a-better-battle-halo-3-ai-objectives [S]

---

### 1.3 Left 4 Dead: the AI Director and "structured unpredictability" (Valve, 2008)

**Technique.**
- **The intensity score.** Each survivor has an emotional-intensity value. It rises with damage taken, incapacitation, being pulled off ledges, and nearby infected dying (inversely with distance). It decays toward zero, but not while infected are actively engaging. [V]
- **The pacing cycle.** The Director tracks the maximum intensity across all four survivors and runs a cycle: [V]
  1. **Build Up**: full threat population until intensity crosses a peak threshold.
  2. **Sustain Peak**: 3–5 s more.
  3. **Peak Fade**: the fight in progress plays out.
  4. **Relax**: major threats withdraw.
- **Structured unpredictability.** Population is "not purely random, nor deterministically uniform". It is a superposition of population functions, each with designer-set randomness. [V]
  - Mobs arrive at random 90–180 s intervals on Normal. [V]
  - 75% of mobs spawn behind the team, because threats ahead are already engaged. [V]
  - Boss events (Tank, Witch, Nothing) are shuffled and dealt along the route with no immediate repeats. [V]
- **Why procedural at all.** Players memorise static placements, which kills suspense and turns co-op into a race. [V]
- **Companion talk.** Elan Ruskin's GDC 2012 talk covers the dialogue system: fuzzy pattern-matching of hundreds of world facts against thousands of lines, so characters "remember history". [S]

**Why it reads as human.** Valve modelled the pacing on Counter-Strike rounds between human teams. The enemy seems to know when to press and when to let you breathe, which is what a human game-master does.

**Rivenkeep takeaways.**
1. **A pacing layer is valuable, but it must be deterministic and must never inform the commander.** Valve used live randomness. Rivenkeep can get the same "unmemorisable yet structured" feel from a per-battle seed plus the player's own inputs.
2. **The "no immediate repeats" deal is a cheap human-feel rule for stratagem selection.** People vary their plays.
3. Mob-from-behind is a reminder that the best threats come from where attention isn't.

**Citations.**
- Michael Booth, "The AI Systems of Left 4 Dead", AIIDE 2009 keynote (Valve). https://steamcdn-a.akamaihd.net/apps/valve/2009/ai_systems_of_l4d_mike_booth.pdf [V]
- Elan Ruskin, "AI-driven Dynamic Dialog through Fuzzy Pattern Matching", GDC 2012. https://gdcvault.com/play/1015528/AI-driven-Dynamic-Dialog-through [S]

---

### 1.4 XCOM: Enemy Unknown and XCOM 2: pods, the reveal, and named enemy commanders (Firaxis, 2012 and 2016–17)

**Technique.**
- **Pods.** Aliens deploy in pods (UFOpaedia gives groups of 2–8, varying by version and mod) that activate together when any member is spotted. [S]
- **Patrols.** Unrevealed pods may hold still or patrol as a group, and a patrol gives an audio cue between turns. [S]
- **The "scamper".** On reveal, a pod gets a free move, usually into cover, but cannot attack that turn. [S]
  - The community rationale: without it, aliens would stand in the open and the game would be trivial. [S]
  - I did not find Firaxis's own statement of the reason. Alex Cheng presented XCOM: EU's AI on the GDC 2013 "AI Postmortems" panel, but I could not read its contents this session. [U]
- **XCOM 2 pod leaders.** Pods have a leader that followers follow. XCOM 2's AI behaviour trees are exposed in data files that mods edit. [M]
- **The Chosen (War of the Chosen, 2017).**
  - Three named enemy commanders: the Assassin (stealth and melee), the Hunter (a long-range tracking rifle) and the Warlock (psionics). [S]
  - Each has randomised strengths and weaknesses, taunts the player, and gains abilities over the campaign until it can assault the player's base. [S]

**Why it reads as human.**
- The reveal plus the scamper reads as the enemy shouting "Contact!" and diving for cover, the same frame a human squad would react in.
- Pods make encounters countable, and managing activations becomes the player's strategic skill.
- The Chosen add rivalry and recognisable personalities who "remember" you.

**Rivenkeep takeaways.**
1. A formation is a pod: it activates, reacts and breaks as a unit, which keeps the attention cost low.
2. **Give the first moment of contact a visible, fixed reaction (a scamper).** For example, a formation spotted by the keep closes up and signals, so the player learns the fleet has noticed them.
3. Mystarchs should work like Chosen: named, a known repertoire, a published weakness, and taunts delivered as signals or story lines.

**Citations.**
- GDC 2013, "AI Postmortems: Assassin's Creed III, XCOM: Enemy Unknown, and Warframe": https://www.gdcvault.com/play/1018058/AI-Postmortems-Assassin-s-Creed [S for existence only]
- UFOpaedia, "Tactical AI": https://www.ufopaedia.org/index.php/Tactical_AI [S]
- War of the Chosen overview: https://en.wikipedia.org/wiki/XCOM_2:_War_of_the_Chosen [S]

---

### 1.5 Total War: morale, rout and collapse (Creative Assembly, 2000 onward)

**Technique.**
- **Morale states.** Each unit has morale (later "leadership") that moves through named states: eager, steady, shaken, wavering, routing. In later titles, units routed repeatedly become shattered and cannot rally. [S]
- **What drains it.** Casualties, being alone, flank and rear attacks, being surrounded, and the general's death. A routing unit drains nearby allies, which can cause a chain rout. [S]
- **The tell.** The unit's banner flashes while it wavers and turns white when it routs. [S]
- **Shogun and Sun Tzu.** Shogun: Total War (2000) was marketed as having battle AI built on Sun Tzu's *The Art of War*. [S] One secondary source claims "220+ rules" and behaviours such as feigned retreats. [U]

**Why it reads as human.** Armies don't fight to the last man. They break, and the break spreads socially. The player wins by making the enemy believe it has lost (flanking, killing the general), which is a psychological victory rather than arithmetic.

**Rivenkeep takeaways.**
1. Resolve already exists in the design. The research says to **show it through a few discrete, big states** (a banner or pennant, plus motion) and make it **contagious**. Total War shows morale on the banner itself; it isn't only inferred from motion.
2. Killing the Flagship should produce a visible command shock (Halo 3 leaders, Total War generals).

**Citations.**
- Total War Wiki, "Morale": https://totalwar.fandom.com/wiki/Morale [S]
- "About Shogun: Total War": https://wiki.totalwar.com/w/About_Shogun:_Total_War.html [S]

---

### 1.6 StarCraft and RTS AI: build orders as recognisable, scoutable strategies

**Technique.**
- **Build orders as a vocabulary.** Human RTS play is organised around named build orders: rush, timing attack, fast expand, tech to air. They are learnable, scoutable and counterable, which makes them a shared vocabulary between opponents. [M]
- **They can be recognised from partial information.** Weber & Mateas (2009) showed that strategies can be predicted from replay features with machine learning. A player's strategy is recognisable from limited observation. [S]
- **SC2's built-in AI.**
  - It lets you pick the AI's opening build. The names I recall are Full Rush, Timing Attack, Aggressive Push, Economic Focus and Straight to Air. [M/U on the exact names; the dropdown's existence is S]
  - The top levels are labelled openly as cheats: Cheater 1 (Vision), Cheater 2 (Resources), Cheater 3 (Insane). [M]
- **Age of Empires II.**
  - AIs are defined by a `.ai` file plus a `.per` ("personality") script of rules and **strategic numbers**. [S]
  - Personalities differ in strategy bias. For example, rushers barely fish and boomers fish heavily. [S]
- **AlphaStar (DeepMind, 2019).**
  - It reached Grandmaster in the top 0.15% of European players. [S]
  - It was trained in a **league** of main agents plus "exploiter" agents whose only job is to find the main agents' weaknesses. [S]
  - Its APM was capped, in consultation with professionals, so the contest was about decisions rather than mechanical speed. [S]
  - Critics noted that burst APM within the cap could still be superhuman. [S] The January 2019 exhibition agent saw the whole map, while the Nature version used a camera-like view. [M]

**Why it reads as human.** A build order is a plan with a name, a timing and a tell (what the scout sees). You recognise it ("he's going air"), you counter it, and the opponent adapts. That is exactly Jack's principle 2.

**Rivenkeep takeaways.**
1. **Stratagems should be the fleet's build orders.** Each is named, with a recognisable opening shape, a timing and a counter.
2. **A human-feel AI is a repertoire plus a style bias** (AoE2's personalities), not one optimal policy.
3. **If the fleet ever cheats, label it.** SC2's "Cheater" levels are an honest precedent. Better still, don't cheat.
4. AlphaStar's APM cap is the RTS version of "strategy, not skill". The Fight's slow-time ramp is the player-side equivalent.

**Citations.**
- Ben G. Weber & Michael Mateas, "A Data Mining Approach to Strategy Prediction", IEEE CIG 2009. [S]
- O. Vinyals et al., "Grandmaster level in StarCraft II using multi-agent reinforcement learning", *Nature* 575:350–354, 2019. https://www.nature.com/articles/s41586-019-1724-z [S]
- AoE2 AI scripting reference: https://airef.github.io/ [S]
- Age of Empires Wiki, "Artificial intelligence": https://ageofempires.fandom.com/wiki/Artificial_intelligence [S]

---

### 1.7 Chess engines and human style

**Technique.**
- **Style shows in how an agent errs.** Strong engines are recognisably inhuman. Maia (McIlroy-Young, Sen, Kleinberg, Anderson, KDD 2020) retrained an AlphaZero-style network on human games. It predicts human moves at a given rating far better than engines, and it predicts when a human will blunder. [S]
- **Anti-cheating relies on the same fact.** Ken Regan's statistical work on cheat detection rests on human error patterns being skill-dependent and characteristic. [M]
- **Chessmaster personalities.** Chessmaster shipped many named personalities. The grandmaster and Josh Waitzkin personalities used opening books built only from moves those players actually played. [S] Engine "personality" settings (aggression, material versus position, randomness) are widely reported, but I did not verify their exact parameters. [U]
- **Kasparov on AlphaZero.** He wrote that AlphaZero's play felt dynamic and closer to his own style than traditional engines did (*Science* editorial, 2018). [M]

**Why it reads as human.** In chess you see every move and never see the plan, yet strong players still recognise styles. Style comes from consistent preferences (the opening repertoire, attacking versus positional) and characteristic mistakes.

**Rivenkeep takeaways.**
1. **Show the moves, hide the plan.** Every formation's tactical move is visible; the stratagem is inferred from them.
2. **Human-likeness comes from systematic, skill-appropriate errors, not noise.** Early Mystaeri should err like green captains (overcommitting, fixating), not like dice.
3. **A Mystarch's repertoire is its opening book.**

**Citations.**
- R. McIlroy-Young et al., "Aligning Superhuman AI with Human Behavior: Chess as a Model System", KDD 2020. https://arxiv.org/abs/2006.01855 [S]
- Chessmaster 10th Edition personalities FAQ: https://gamefaqs.gamespot.com/pc/921361-chessmaster-10th-edition/faqs/38373 [S]

---

### 1.8 Advance Wars and Fire Emblem: commander identity and enemy-phase predictability

**Advance Wars.**
- Every Commanding Officer (CO) has asymmetric rules. For example, Max has strong direct-fire units and weak indirect ones. Each CO also has a CO Power that charges as damage is dealt and taken. [S]
- Both sides' power meters are on screen, so the player can see an enemy power coming and bait it or play around it. [M]
- The personality mostly reads through rules and dialogue. I found no evidence that each CO has a distinct AI decision policy. [U]

**Fire Emblem.**
- Enemy AI is authored per unit and per map: stationary guards, units that attack only when you enter range, chargers, bosses that hold the throne. [M]
- ROM-hacking documentation of the GBA games shows primary and secondary AI bytes per unit, including "act 100% / 80% / 50%" variants. [S]
- Later titles show the enemy's threat range as a danger zone. [M]
- Veterans learn that enemies prefer targets they can damage heavily or kill. [M]

**Why it reads as human.** A named commander with known strengths is a person you prepare for ("it's Max, so bring indirects"). Fire Emblem's enemies are not clever, but they are consistent, so the player's plans feel like outwitting someone.

**Rivenkeep takeaways.**
1. **A Mystarch's identity should come with a visible "power meter" for its signature stratagem.** For example, horn-calls counting toward its big move. This is a telegraph that can be baited.
2. **Per-formation "standing orders" are cheap.** Formations can be guards, chargers or probers. They are consistent, and the player can learn them.

**Citations.**
- Wars Wiki, "Commanding Officer": https://warswiki.org/wiki/Commanding_Officer [S]
- FE Universe, "[FE7] The Official AI Documentation Thread": https://feuniverse.us/t/fe7-the-official-ai-documentation-thread/348 [S; community reverse-engineering]

---

### 1.9 Into the Breach: telegraphing and determinism (Subset Games, 2018)

**Technique (from the GDC 2019 slides, read directly).**
- **The core constraint of the combat design:**
  - all enemy attacks are shown;
  - there is no hit or miss chance;
  - the game is completely deterministic during the player's turn. [V]
- **Consequences they list:**
  - threat changes from "the enemy might hurt me" to "the enemy will do exactly this unless I intervene";
  - play becomes defensive;
  - manipulating enemies (pushing them into each other) is more fun than killing them. [V]
- **UI-guided design.** The iconography forced three attack types (artillery, melee, projectile), orthogonal aiming and static enemy designs. The target and attack type are shown for every enemy. [V]
- **A lesson learned.** The Power Grid mechanic inserted randomness into a deterministic design and annoyed players. [V]
- **Related precedent.** Slay the Spire (2019) shows each enemy's next intent (attack and how much, block, buff) as an icon. [M]

**Why it reads as human.** It doesn't, and that is instructive. Full telegraphing makes the enemy a puzzle, not a mind. Into the Breach is the pole Jack does not want at the fleet level ("I don't want the player to know exactly what the ships are doing at first"). It is the right pole at the tactical level, where you want to know what this formation will do in the next few seconds.

**Rivenkeep takeaways.**
1. **Telegraph tactics, conceal strategy.** Show what a formation is about to do (heading, wind-up, target lock). Let the player infer why, meaning the stratagem.
2. **Randomness grafted onto a deterministic design annoys players.** Don't.
3. **Manipulating the fleet is more fun than killing it.** The bait patterns are the Rivenkeep version of Into the Breach's pushes.

**Citations.**
- Matthew Davis (with Justin Ma), "Into the Breach Design Postmortem", GDC 2019. https://gdcvault.com/play/1026333/-Into-the-Breach-Design. Slides: https://media.gdcvault.com/gdc2019/presentations/Into%20the%20Breach%20Postmortem%20Final.pdf [V]

---

### 1.10 Alien: Isolation: two brains, unlockable behaviours, and the perception of cheating (Creative Assembly, 2014)

**Technique.**
- **Two layers:**
  - A **Director** (the "macro" AI) always knows where both the player and the alien are.
  - The **alien** (the "micro" AI, a behaviour tree of roughly 100+ nodes) hunts using only its senses: sight, sound, and touch.
  - The Director hands the alien only rough-area hints, never the exact position. [S]
- **The menace gauge.** It tracks proximity, line of sight and motion-tracker pressure. After a sustained peak, the Director sends the alien backstage into the vents. After a long lull, it nudges the alien closer. [S]
- **Unlockable behaviour.** Some behaviour-tree branches start locked and unlock as the player uses tactics:
  - repeated locker-hiding unlocks locker searches;
  - flamethrower use unlocks a sub-tree for handling it, then ambush and flanking responses. [S]
  - This produces the illusion of learning without true learning. [S]

**The reception study (Švelch, 2020).**
- Players split into two camps. [S]
  - *Experientialists* accepted the manipulation for the sake of mystery.
  - *Simulationists* demanded autonomous, consistent rules.
- Simulationists called three things cheating: telepathy (the alien seems to know where you are), teleportation, and tethering (it never strays far, like rubber-banding). [S]
- All three are side effects of the Director's hints. [S]

**Why it reads as human.**
- The alien seems to learn your habits because its new behaviours are gated by your habits.
- The Director makes it feel malevolently timed.
- Even minimal truth-leakage from the omniscient layer reads as ESP to a large share of players.

**Rivenkeep takeaways.**
1. **Keep two brains, with a hard wall.** The pacing Director may change what arrives and when (the queue, reserves, relax sorties). It must **never** pass true player state to the commander. The critique already found blindness leaks (troop A* reading true wall HP). Švelch's study says players will notice and call it cheating.
2. **Unlock-on-habit is the cleanest deterministic way to make the fleet seem to learn.** The unlock condition is a pure function of what the fleet observed.

**Citations.**
- Tommy Thompson, "The Perfect Organism: The AI of Alien: Isolation", Game Developer, 2017. https://www.gamedeveloper.com/design/the-perfect-organism-the-ai-of-alien-isolation [S]
- Tommy Thompson, "Revisiting the AI of Alien: Isolation", AI and Games, 2020. https://www.aiandgames.com/p/revisiting-alien-isolation [S]
- Jaroslav Švelch, "Should the Monster Play Fair?: Reception of Artificial Intelligence in *Alien: Isolation*", *Game Studies* 20(2), 2020. https://gamestudies.org/2002/articles/jaroslav_svelch [S]

---

### 1.11 Poker and opponent modelling

**Technique.**
- **Poki.** The University of Alberta program builds a statistical model of each opponent's tendencies and adjusts to exploit the patterns it sees. [S]
- **Bayes' Bluff.** It formalises this: keep a prior over the opponent's strategy, update it with a posterior from observed play, then play a response to that distribution. [S]
- **Game theory.** An unexploitable strategy must mix, which includes bluffing. A pure best response to a model is itself exploitable. That is why "safe exploitation" became a research topic. [M]

**Why it reads as human.** Humans read other humans: "he always bets big on a draw". An opponent that notices your habit and punishes it feels like a person. Its tendency to over-read you (to over-fit) is also very human, and it gives you something to exploit.

**Rivenkeep takeaways.**
1. **The commander should model the defender, not the board.** Keep a small, discrete, deterministic profile of the player's habits, built only from what the fleet observed. For example: holds fire late; favours the north coast; encloses guns; opens with an alpha. Then choose a stratagem as a biased best response.
2. **Over-fitting is the feature.** Once the player sees what the fleet thinks of them, they can feed it false habits. This is the Fleet Memory "bait window", raised to the level of strategy.
3. **Bluffs need a mixing rule.** A deterministic fleet can still "mix", driven by the battle seed and the observed history. The same play still gives the same bluff.

**Citations.**
- D. Billings, A. Davidson, J. Schaeffer, D. Szafron, "The challenge of poker", *Artificial Intelligence* 134(1–2):201–240, 2002. [S]
- F. Southey, M. Bowling, et al., "Bayes' Bluff: Opponent Modelling in Poker", UAI 2005. https://arxiv.org/abs/1207.1411 [S]

---

### 1.12 The "illusion of intelligence" and believability

**Butcher & Griesemer (GDC 2002).** See 1.2. This is the canonical talk that made "illusion of intelligence" a working principle: design for the player's perception of mind, not for the mind itself. [V]

**Joseph Bates (CMU Oz Project), "The Role of Emotion in Believable Agents".** *Communications of the ACM* 37(7), 1994. [M]
- Drawing on Disney's *Illusion of Life*, believability comes from clearly expressed internal state and intention, not from realism or competence.
- Characters should show what they feel and think before they act.

**BotPrize (Philip Hingston, 2008–2012).** A Turing test for Unreal Tournament 2004 bots. [S]
- In 2012 MirrorBot scored 52.2% "humanness" and UT^2 scored 51.9%. The humans averaged 41.4%.
- The bots were judged more human than the humans.
- MirrorBot's trick was human-inspired mirroring behaviour.
- Commentary on the winners stressed human-like imperfection and reacting to others, not raw skill. [S/M]

**Soren Johnson, "Playing to Lose: AI and Civilization" (GDC 2008).**
- The central distinction is "good" AI versus "fun" AI. [S]
- A strategy AI's job is to be a compelling opponent, not to minimise the player's win rate. [S]
- Civilization IV also shows AI leaders' attitudes with itemised reasons in diplomacy. [M] That is transparency about the AI's state of mind.

**Sid Meier, "The Psychology of Game Design (Everything You Know Is Wrong)" (GDC 2010 keynote).**
- Perceived fairness beats mathematical fairness. [S]
- Players felt 2:1 odds should nearly always win, and didn't read 2:1 and 20:10 as the same. [S]
- Design for the player's psychology, not the simulation's truth. [S]

**Rivenkeep takeaways.**
1. Perception is the product.
2. Show internal state before action (the believability rule).
3. Imperfection and reacting to the player make an agent seem human.
4. Fairness must also be perceived: honest odds are not enough if they look unfair.

**Citations.**
- P. Hingston, "A Turing Test for Computer Game Bots", *IEEE Trans. Computational Intelligence and AI in Games* 1(3), 2009. [M for volume and issue]
- UT Austin news on BotPrize 2012: https://news.utexas.edu/2012/09/26/artificially-intelligent-game-bots-pass-the-turing-test-on-turings-centenary/ [S]
- Soren Johnson: https://www.designer-notes.com/playing-to-lose-ai-and-civilization-gdc-2008/ [S]
- Sid Meier: https://gdcvault.com/play/1012186/The-Psychology-of-Game-Design [S]

---

### 1.13 Other directly relevant precedents

**Metal Gear Solid V: The Phantom Pain (2015): the "Revenge" / enemy-preparedness system.** [S]
- The game tracks how the player infiltrates:
  - frequent headshots lead to helmets;
  - repeated night operations lead to night-vision goggles;
  - heavy use of one method leads to more guards and better kit against it.
- It raises the share of soldiers equipped against your habit.
- Levels fall if you stop the habit, or if you send dispatch missions that disrupt the enemy's supply.
- Mission briefings tell you about the new countermeasures. [M]
- **Rivenkeep lesson.** Adapt to the player's most-used method, announce the adaptation, and always leave a counter-counter.
- Konami support, "Enemy Preparedness": https://eu-support.konami.com/hc/en-gb/articles/9667929703191-The-Phantom-Pain-Enemy-Preparedness. Wiki: https://metalgear.fandom.com/wiki/Revenge_System_(enemy_preparedness)

**Middle-earth: Shadow of Mordor (2014): the Nemesis System.** [S]
- Orc captains remember encounters with the player, get promoted (for example, after killing the player), change behaviour, and refer to the past.
- It is patented as US 10,926,179, granted 23 February 2021.
- **Rivenkeep lesson.** Remembered history, voiced back to the player, is the fastest route to "a person is running the enemy". Rivenkeep forgets on replay, so apply this within a battle or across the campaign's story layer, not across retries.
- https://www.patentarcade.com/2021/02/warner-brothers-granted-patent-for-nemesis-system-from-middle-earth-video-games.html

**The Last of Us (2013): the Combat Coordinator.** [S]
- Human enemies are given roles: Flanker, Approacher, OpportunisticShooter, StayUpAndAimer.
- A flanker is valid only if it has a path to the player that avoids the "combat vector".
- NPCs share the player's position with nearby allies.
- Players widely report enemies calling out when the player is out of ammo and rushing. I could not confirm this in the chapter. [U]
- **Rivenkeep lesson.** Roles within a formation (lead, screen, flanker, reserve) are what make coordination legible.
- Travis McIntosh, "Human Enemy AI in The Last of Us", *Game AI Pro 2*, ch. 34, 2015. https://www.gameaipro.com/GameAIPro2/GameAIPro2_Chapter34_Human_Enemy_AI_in_The_Last_of_Us.pdf

**Plants vs. Zombies (2009): one new thing at a time.** [S]
- New mechanics and enemies arrive gradually across levels.
- Each level starts slowly and builds to waves and a final wave.
- **Rivenkeep lesson.** This is the teaching half of Jack's Ender's Game ramp.
- George Fan, "How I Got My Mom to Play Through Plants vs. Zombies", GDC 2012. https://www.gdcvault.com/play/1015541/How-I-Got-My-Mom

**Frozen Synapse (Mode 7, 2011): deterministic simultaneous turns.**
- Players plan with unlimited time. Then about 5 s of simulation resolves. [S]
- Because the resolution is deterministic, you can plan hypothetical enemy moves and preview the outcome. [M]
- **Rivenkeep lesson.** Determinism plus a thinking pause turns timing into a considered choice. That is the Fight slow-time ramp, reached from a different direction.
- https://en.wikipedia.org/wiki/Frozen_Synapse

**Bad North (Plausible Concept, 2018): Viking boats landing on island shores.** [S]
- Boats emerge from the mist and sail straight in, so the landing point can be predicted.
- A beached boat occupies its spot.
- **Rivenkeep lesson.** This is the closest genre neighbour for "ships landing on a defended shore". The heading telegraph gives readable threat direction.
- https://www.badnorth.com/

**Age-of-sail signalling (historical; a thematic source for naval "barks").** [M]
- Fleets communicated by flag hoists (for example, Popham's telegraphic code). A receiving ship acknowledged with the **answering pennant**.
- Nelson's Trafalgar memorandum (9 October 1805) is the classic statement of mission command. It says that if signals can't be seen or understood, a captain who lays his ship alongside an enemy can't go far wrong.
- **Rivenkeep lesson.** This gives a period-true grammar for Mystaeri barks (a signal, then an acknowledgement, then the action). It also gives a period-true model of "commander's intent plus captains' judgment".

---

## 2. Cross-cutting patterns

| Pattern | What it does for "human feel" | Strongest sources |
|---|---|---|
| **Two layers of brain** (strategic or pacing versus local) | A plan exists above the units, while each unit still acts for itself | F.E.A.R. squads/individuals; Halo 3-min/30-s scopes; Halo 3 Objectives; Alien: Isolation Director/alien; TLOU coordinator |
| **Coordination made audible** | Players credit the enemy with a shared plan only if they see or hear it | F.E.A.R. squad dialogue; Halo combat dialogue; Valve dynamic dialog; naval signalling |
| **Named, repeatable strategies** | Recognition leads to counterplay, which leads to the other side adapting: a relationship | StarCraft builds; AoE2 `.per` personalities; Chessmaster opening books; Advance Wars COs |
| **Consistent personality** | You prepare for *someone* | Halo races; XCOM Chosen; Mystarchs (Rivenkeep); Civ leaders |
| **Morale and breaking points** | Armies that break like people, not HP bars | Total War; Halo "thwarted" goals; Halo 3 leaders |
| **Visible memory and adaptation** | "It learned from me", together with "I can use that" | MGSV Revenge; Nemesis; Alien: Isolation unlocks; poker modelling |
| **Telegraph the near future** | Fairness and planning | Into the Breach; Slay the Spire; Advance Wars power meters; Bad North boat headings |
| **No hidden cheating** | Trust. Leaks are noticed and resented | Halo "no cheating" knowledge model; Švelch on Alien: Isolation; SC2's honest "Cheater" labels |
| **Pacing** | The enemy seems to know when to press and when to breathe | L4D Director; Alien: Isolation menace gauge |
| **Human-like error** | Imperfection that is characteristic, not random | Maia; BotPrize; Johnson's "fun AI" |
| **Determinism and no dice** | Outcomes the player owns | Halo's discarded randomness; Into the Breach; Frozen Synapse; the Power Grid lesson |

---

## 3. Design principles for Rivenkeep's deterministic, blind Mystaeri fleet

Each principle below states the rule, the evidence behind it, how it would apply in Rivenkeep, and a prototype test. They are grouped by which part of Jack's vision they serve, numbered 1–7 (see the list in section 7).

### A. Architecture: coordinated yet independent (vision 2)

**P1. Two brains, one wall.**
- **Rule.** Split the enemy into two layers:
  - a **Tide Director**: pacing, authored and seeded. It owns the queue, reserve release and "relax" sorties.
  - a **Mystaeri Commander**: blind. It chooses the stratagem and knows only what LOS, Contact and Effect have delivered.
- **The wall.** The Director may change **what arrives and when**. It may never change **what the fleet knows**. No hints, no nudges, no "rough area" leaks.
- **Evidence.** Alien: Isolation's Director/alien split works. Its hint channel, though, is exactly what simulationist players called telepathy (Švelch). L4D shows how much a pacing layer adds.
- **Test.** The *counterfactual invariance test*: change any player state the fleet has not observed (move a hidden gun, add an enclosed wall). The fleet's decisions must be identical, tick for tick, until the first tick at which that state enters a channel. Run it automatically in CI over saved battles.

**P2. Three clocks of decision: stratagem per sortie, judgment per beat, reflex per tick.**
- **Rule.** Each layer decides on its own cadence:
  - **Commander.** Chooses and commits to a stratagem at sortie boundaries, during Build/Deploy (the bait window). It may also switch at no more than one or two authored "branch points" inside a sortie. An example branch is "if the probe is repulsed, switch to plan B".
  - **Formations.** Re-evaluate their local task on a fixed cadence in sim ticks (for example, every 3 ticks, meaning 3 game-hours, meaning 3 s at normal speed).
  - **Hulls.** React every tick.
- **Evidence.** Halo's 3-minute design scope versus 30-second code scope. Halo 3's task tree re-assigned squads continuously while the designer's "play" held.
- **Why it matters.** Humans commit to a plan and adapt between rounds. Commitment is itself a human tell, and it is what makes a stratagem recognisable and counterable. A fleet that re-plans every tick reads as twitchy and machine-like.
- **Test.** Log every stratagem change with its trigger. Target: at most one unforced change per sortie.

**P3. Orders are intent, not scripts. Formations may refuse, visibly.**
- **Rule.** A stratagem is a small **task tree**, in the style of Halo 3 Objectives:
  - roles such as *probe, pin, screen, strike, reserve, exploit*;
  - each role with a priority, a capacity, filters (which lineages or shapes may fill it) and exhaustion conditions.
- **How formations take part.** They fill roles by fit and distance. Each formation weighs its assigned role against its own resolve and fear, as F.E.A.R.'s soldiers weigh orders against their own goals. A Wavering formation ordered to *strike* may take *screen* instead, or break off.
- **Show the refusal.** Show it (P5), don't hide it. A captain who balks is one of the most human things the player can see.
- **Evidence.** F.E.A.R. (orders versus goals; squad behaviours that can fail). Halo 3 (tasks, capacities, fall-back). The TLOU Combat Coordinator (roles and valid-flanker tests). Nelson's memorandum (mission command).
- **Test.** In playtest replays, count how often a formation deviates from its role, and whether players can say why. Too rare looks robotic; too common looks like chaos. Tune toward "about one visible deviation per sortie, always with a tell".

**P4. Make the coordination visible: signal, answer, act.**
- **Rule.** Every stratagem and role change gets a **bark** in the period naval grammar:
  - the Flagship's **horn or signal hoist** (the order);
  - the formation's **answering pennant or horn** (the acknowledgement);
  - then the manoeuvre.
  - Add the defenders' **lookout line** in the story's voice, so the player learns the signal language. An example: "Horns on the grey water. They are closing their ranks."
- **Rules for barks:**
  - Barks are chosen after the decision, from the decision.
  - They are output-only, so determinism is unaffected.
  - Prefer exchanges (flag and answer, lookout and captain) to single announcements.
- **Evidence.** Orkin (squad dialogue chosen after decisions; two-voice exchanges; no point coordinating if the player can't see it). Halo combat dialogue. Valve's fuzzy-matched dialog. Age-of-sail answering pennants.
- **Test.** Can a playtester name what the fleet is about to do from signals alone, three sorties into a campaign? This also serves Jack's story goal: signals are where the myth voice lives in the Fight.

**P5. Voice intentions and explain hesitation, even when there is no mechanism behind it.**
- **Rule.** Use barks for:
  - intent ("the flag calls the reserve");
  - distress ("a pinned formation signals for relief");
  - inaction ("a formation that holds signals it has no clear water").
- **Evidence.** Orkin's reinforcement call and his "nowhere to go" line. A hesitating AI with an explanation reads as trapped. The same AI without one reads as broken. Halo also lists "looking broken" as a thing to avoid.
- **Rivenkeep application.** This is the cheapest fix for the critique that resolve and propagation are invisible. The mechanism already exists; it just has no voice.

### B. Readability: the player recognises and counters (vision 2, vision 3)

**P6. Telegraph tactics, conceal strategy.**
- **Rule.** At formation level, the next few seconds must be readable: heading line, wind-up, target lock, closing up or spreading out, the Bad North boat telegraph. At fleet level, the **stratagem is never labelled live**. The player infers it from the shapes the formations make together.
- **Evidence.** Into the Breach shows that full telegraphing makes a fair puzzle but not a mind. Chess shows every move and hides the plan, and still reads as a person. Jack: "I don't want the player to know exactly what the ships are doing at first, but they recognize the strategy and they can counter it."
- **Test.** After a sortie, ask playtesters to pick the stratagem from a list of three. Target: chance-level in the first encounter, and above 70% by the third encounter of the same stratagem.

**P7. Name it afterwards: the debrief is the debugger.**
- **Rule.** The Build/Deploy phase shows a short **after-action chart**:
  - the stratagem the Mystaeri attempted, under its in-world name, written as a chronicle entry;
  - what the fleet believed: its Contact ledger, its fear grid, and its profile of you (P13);
  - which formation broke from the plan, and why.
- **Collection.** Stratagems the player has witnessed go into a **Book of Tides** codex, which is also a story collection.
- **Evidence.** Halo discarded hidden states. Chess learning runs on annotation. The critique noted that the promised debug loop has no debugger.
- **Why it matters.** This is the single highest-leverage change for learnability. Determinism only turns into mastery if the player can see the rule that produced the outcome.
- **Test.** After a debrief, can the player state one thing they will change to exploit the fleet's belief?

**P8. One headline per formation. Big tells, few registers.**
- **Rule.** Each formation shows **one** dominant tell at a time: its role, or its morale state, or its wind-up. Reserve fine detail for the debrief and for slow time.
- **Evidence.**
  - Halo's "things to avoid" list begins with subtlety.
  - XCOM's pods make encounters countable.
  - The critique counts about 15 reading registers per formation in an 18 s band, on shapes about 27 pt wide.
- **Note on the Fight slow-time ramp.** It gives extra reading time only while an order is being placed. Passive reading still happens at full speed, so it doesn't remove the need for big tells.
- **Test.** Can a phone playtester, at arm's length, say what each formation is doing in one word?

**P9. Let the formation carrying the idea live long enough to be seen thinking.**
- **Rule.**
  - Budget durability and screening so that the formation expressing a stratagem survives through its tell.
  - A probe should survive long enough to report; a feint long enough to draw fire.
  - Early "unorganised" sorties can die fast. From the Early-Mid tier on, key roles get protection.
- **Evidence.** In Halo's playtest, tougher enemies were rated "very intelligent" by 43% of testers against 8% for weaker ones, with the same AI.

### C. Determinism and "strategy, not skill" (vision 1, vision 3, vision 7)

**P10. No dice after the seed. Every divergence traces to a player action.**
- **Rule.**
  - A battle's only source of variety besides the player is its fixed seed. Authored "shuffle-bag" variety (such as no immediate repeat of a stratagem) is derived from that seed.
  - Every decision input is a quantised function of observed state.
  - All maths is integer or fixed-point: LOS, bearings, the fear grid. Platform trig can differ between iOS and Android and break determinism.
  - Iteration order is stable.
- **Evidence.**
  - Halo discarded randomness in favour of reactive unpredictability.
  - Into the Breach: the Power Grid's randomness annoyed players.
  - L4D's "structured unpredictability" gets the unmemorisable feel without needing live randomness.
- **Test.** Record and replay: the same input log gives a byte-identical state hash at every sortie boundary, on both iOS and Android.

**P11. Time belongs to the player, not the fleet. The slow-time ramp is presentation only.**
- **Rule (Jack's ruling).** Starting an order ramps wall-clock speed down from 1 tick per second (1 siege hour = 1 s; 1 day = 18 s) to 1 tick per 18 s. The ramp eases in and out, never snaps.
- **What that requires of the fleet:**
  - Orders are stamped in ticks.
  - The fleet's decision cadence (P2) is defined only in ticks, so slowing the wall clock never gives the fleet "more thinking".
  - Nothing in the simulation may read wall-clock time.
- **Keep the tells animating in slow time.** Slow time exists so the player can read tells and choose the tick deliberately. "A second earlier or later" becomes a considered choice of tick, not a reflex.
- **Evidence.** AlphaStar's APM caps kept the contest about decisions. Frozen Synapse and Into the Breach pair deterministic resolution with unlimited planning time.
- **Test.**
  - The same order stamped at tick T gives the same outcome whether it was placed at full speed or in slow time.
  - An automated test injects orders with randomised wall-clock delays but fixed tick stamps, and asserts identical state hashes.
- **Possible extension (flagged, not a ruling).** A press-and-hold "spyglass" on a formation that uses the same ramp, if playtests show live reading is still too fast.

### D. The stratagem book: from simple to complex (vision 4, vision 5 "they get better")

**P12. Stratagems are the fleet's build orders. Complex ones are compositions of simple ones.**
- **Rule.** Author a small set of **primitive verbs**. Candidates: land, probe, mass, pin, screen, feint, envelop, reserve, exploit, withdraw. Late stratagems are **sentences** built from verbs the player already knows, reusing the same signals and shapes.
- **Evidence.** F.E.A.R. had no complex squad behaviours: they emerged from simple ones. StarCraft builds chain an opening, a timing and a transition. Halo 3 task trees compose.
- **Why it matters.** Recognition transfers. Early learning pays off late ("you know the words, now read the sentence"), and it meets Jack's point that a simple stratagem should build into a complex one.
- **Test.** Each late stratagem must be describable as a combination of earlier ones in one sentence. If it needs a new tell, it needs a new primitive, and that primitive must be introduced alone first.

**P13. Introduce one new idea at a time: the Ender's Game ramp.**
- **Rule.** Jack's example is that the less advanced ships were sent out first. Early Mystaeri sorties are **unorganised**: no signals, no roles, every formation for itself. Each later period unlocks one capability:
  - signals;
  - then roles;
  - then two-verb stratagems;
  - then a player profile;
  - then feints;
  - then Mystarch repertoires.
- **Mechanism.** Unlocks are gated deterministically by battle, tier and the fleet's observations, in the style of Alien: Isolation's unlockable branches.
- **Evidence.** Plants vs. Zombies (new things gradually; slow starts building to waves). Alien: Isolation (behaviours unlocked by player habits).
- **Story tie-in.** Each capability unlock can be a tale in the collection. For example: the first unbanded raiders; the day the horns were first heard; the first Mystarch.

**P14. Commanders have repertoires, not policies.**
- **Rule.** A Mystarch (and each Flagship lineage) is:
  - a **weighted preference over the stratagem book** (its opening book);
  - one **signature stratagem** with a visible build-up, like Advance Wars' power meter, for example a count of horn calls;
  - one **published weakness**;
  - a **temperament**, which sets how fast it abandons a failing plan.
- **Field promotion.** When a Flagship is promoted in the field, the new commander's repertoire takes over. Announce it with a distinct signal.
- **Evidence.** AoE2's `.per` personalities. Chessmaster opening books. Advance Wars COs. Halo races. XCOM's Chosen.
- **Test.** Can players tell two Mystarchs apart from play alone within one battle?

### E. Adaptation and deception (vision 2 "they get better", "they can counter it")

**P15. Model the defender, visibly, and let the model be baited.**
- **Rule.** The Commander keeps a **defender profile** of 4 to 6 discrete traits, updated only from observations. Examples: *guards the north / south*; *holds fire until close*; *encloses guns*; *opens with an alpha*; *punishes screens first*. It picks stratagems as a biased best response to that profile.
- **Show the profile in the debrief (P7).** Then the player can deliberately teach the fleet a false habit and punish its over-fit.
- **Evidence.** Poki and Bayes' Bluff (model plus response). MGSV (adapt to the most-used method). Fleet Memory's existing bait window.
- **Why it matters.** This lifts baiting from single volleys to the level of strategy, which is where Jack's "recognise the strategy and counter it" lives.

**P16. Every adaptation opens a counter-counter.**
- **Rule.** No adaptation is a pure nerf of the player. Each one commits the fleet to something and leaves an exploitable gap.
  - Massing against your north battery thins the south.
  - Answering your alpha with dispersed wolfpacks leaves them without payload.
- **Announce adaptations in-world.** For example, the lookouts report "they have learned our chain".
- **Evidence.** MGSV adaptation is reversible and announced. Poker says a best response is itself exploitable. Alien: Isolation unlocks new behaviour but never omniscience.
- **Test.** For every adaptation rule, the design doc must name its counter in one line.

**P17. Deceive fairly: a feint needs a cost, a cause and a tell.**
- **Cost.** Feints and other deceptions spend fleet tempo or hulls, so they are gambles, not free.
- **Cause.** They are chosen *because of* a player habit the fleet observed. The player baited the bait.
- **Tell.** They have a readable tell that an attentive player can catch. The feint formation might lack payload, ride high, or skip its answering pennant.
- **Timing.** Feints appear only after the player has learned the honest version of the same shape (P13).
- **Evidence.** Poker bluffing. StarCraft fakes (from memory). Shogun's feigned retreats (claimed, [U]). Into the Breach's lesson that the fair version beats the surprising one.

### F. Humanity: error, morale, pacing (vision 2)

**P18. Err like a commander, not like a die.**
- **Rule.** Give each tier and personality **systematic, deterministic biases** in place of noise:
  - *recency* (over-weighting the last hit);
  - *sunk cost* (reinforcing a failing assault);
  - *fixation* (Reaver-style target lock);
  - *overcommitment* (throwing the reserve early);
  - *caution* (withdrawing at the first alpha).
- **Scaling.** Green early captains show strong, crude biases. Late Mystarchs show subtler ones.
- **Evidence.** Maia (human errors are predictable and skill-dependent). BotPrize (human-like imperfection). Johnson ("fun" AI, not optimal AI). Halo's goal that the player can fool the AI through its predictable reactions.
- **Why it matters.** A bias the player can name is a lever the player can pull.

**P19. Morale is the most human signal. Make it few, big, and contagious.**
- **Rule.**
  - Resolve reads in **three or four named states**, each with a clear tell: pennant colour or shape plus motion.
  - Breaking **spreads** to nearby formations.
  - Killing the Flagship causes a visible **command shock**: signals stop, formations hesitate, and then a new flag is raised.
- **Fanatical fleets and bosses** ignore fear, not strategy. They keep running stratagems and still have a breaking point, just a higher one. The critique noted that fanatical fleets currently switch the mind off in the highest-stakes battles.
- **Evidence.** Total War (states, banner tells, flanks, general's death, chain rout). Halo (breaking points; Grunts flee when the leader dies). Halo 3 (leaders' deaths break followers).

**P20. Pace like a Director, deterministically, across sorties.**
- **Rule.** The Tide Director shapes a battle as build-up, then peak, then relax, across its 3–10 sorties. It controls:
  - which stratagem tier is available;
  - when reserves are released;
  - when a lighter "breather" sortie comes.
- **Inputs.** Authored battle data, the seed, and aggregate outcomes such as keep damage or hulls lost. It never touches Commander knowledge (P1).
- **Avoid rubber-banding.** Pacing may ease or sharpen the shape of the challenge. It must never cancel the result of a good play.
- **Evidence.** The L4D Director. Alien: Isolation's menace gauge, and Švelch's "tethering" complaint as the failure mode.

---

## 4. Applying the principles to Jack's stratagem ladder

Jack asked for a lot more than 6–8 stratagems: 6–8 per period, across Early, Early-Mid, Mid, Late-Mid and Late (and more periods if needed), with overlap and simple stratagems growing into complex ones. The research suggests building the ladder along two axes:

- **Capability tiers.** What the Mystaeri *can* do, unlocked per P13. This is the "they get better" story.
- **Stratagem families.** Chains that reuse one signal and one shape, per P12.

**Capability tiers (illustrative; names are placeholders).**

| Period | What the fleet can do | Human analogue | Player learns |
|---|---|---|---|
| **Early**: the unbanded | No signals, no roles. Each formation picks its own beach. Crude biases (charge the nearest noise). | Green raiders | Guns, walls, "they avoid where it hurts" |
| **Early-Mid**: first horns | Flagship signals exist. One-verb stratagems (Mass, Probe, Screen). Formations acknowledge. | A captain in charge | Reading signals; the first named stratagems |
| **Mid**: the line | Roles within a stratagem; two-verb stratagems (Probe-then-Mass, Pin-and-Envelop). Defender profile with 1–2 traits. | A drilled squadron | Recognising combinations; the debrief |
| **Late-Mid**: the feint | Feints with tells; timed reserves; profile with 3–4 traits; adaptations announced. | A cunning admiral | Baiting the fleet's model of you |
| **Late**: the Mystarchs | Personal repertoires, signature stratagems with visible build-up, multi-phase sentences, counter-adaptation. | A rival commander | Out-thinking a person |
| *(optional)* **Legend** | Mystarch pairs coordinating across theatres (a boss duo) | Allied admirals | Reading two minds |

**One family climbing the ladder (illustrative).** Suppose the family is built on the verb *Probe*, with one signal: a single long horn plus a lone fast formation.

1. **Early.** *Landfall*: no probe. Everyone sails for the nearest beach.
2. **Early-Mid.** *Sounding*: one Recon formation probes, and the rest follow the quiet water it reports.
3. **Mid.** *Sounding and Mass*: the main body holds until the probe reports, then masses at the weakest coast.
4. **Late-Mid.** *False Sounding*: a probe at A draws your alpha and reveals your guns, while the main body is already committed to B. The tell is that the probe carries no payload.
5. **Late.** *Twin Tides*: a False Sounding, plus a pin on your strongest battery, plus a reserve timed to your observed alpha habit. A Mystarch's signature.

Each rung reuses the horn and the lone formation, so a Late player who sees a lone fast ship and one long horn thinks, "which Sounding is this?" That is recognition turning into counterplay, as Jack describes.

---

## 5. Determinism and Fight-control checklist

These are drawn from P1, P2, P10 and P11.

- [ ] The simulation reads no wall-clock time. The slow-time ramp changes presentation speed only.
- [ ] Every player order is stamped with an integer tick. Order resolution depends only on (state, tick, order).
- [ ] Commander decisions happen only at sortie boundaries and authored branch points. Formation cadence is N ticks. Both are defined in ticks.
- [ ] All geometry and belief maths is integer or fixed-point. Iteration order is stable. There are no platform trig calls in the simulation.
- [ ] The only PRNG is seeded per battle. Its draws are consumed in a fixed order independent of the player's actions. Otherwise, one extra tap would shift every later "random" choice. Draw per decision site and decision index, not from a shared global stream.
- [ ] The counterfactual invariance test (P1) runs in CI.
- [ ] The cross-device replay hash test (P10) runs in CI.
- [ ] Barks, signals and lookout lines are derived from decisions and never read back by the simulation.
- [ ] Audit for blindness leaks: troop A* and every "reads your X" Cognition apex must use believed state, not true state. The critique found several.
- [ ] The Director has write access to the queue and pacing only, and no read path to Commander knowledge (or the reverse).

---

## 6. Traps to avoid (what not to copy)

1. **Director hints to the enemy** (Alien: Isolation). Even soft hints read as ESP to simulation-minded players.
2. **Randomness as personality.** Noise reads as dumb, not human (Halo, Into the Breach's Power Grid, Maia).
3. **Hidden machinery with no tell.** If a system can't be perceived or debriefed, it costs build time and adds nothing to the experience (Halo "discarded hidden states"; the critique of propagation and contagion).
4. **Adaptation that only punishes.** Without a counter-counter, adaptation reads as the game cheating (MGSV's reversibility is the fix).
5. **Optimal play.** A fleet tuned to minimise the player's win rate is neither fun nor human (Johnson).
6. **Subtle tells on a phone** (Halo's first "thing to avoid").
7. **Bosses that switch the mind off.** Fanatics should ignore fear, never strategy.
8. **Re-planning every tick.** Humans commit. Twitchy re-planning reads as a machine and can't be learned.
9. **Labels on live strategy.** Naming the stratagem while it unfolds turns the fleet into Into the Breach (a puzzle). Name it afterwards.

---

## 7. How the principles map to Jack's vision

1. Deterministic, a second earlier or later matters: P10, P11, P2.
2. Feels like a human running the enemy, coordinated yet independent, readable, counterable: P1, P3, P4, P5, P6, P7, P14, P15, P17, P18, P19.
3. Strategy, not skill: P11, P6, P8.
4. Many stratagems across periods, simple growing into complex: P12, P13, section 4.
5. Story woven into play; the fleet gets better (Ender's Game): P13 (capability tales), P4 (signal and lookout voice), P7 (the Book of Tides chronicle).
6. Halvard and Rhyna: lore, outside this research. The signal grammar in P4 (order, then answer, then act) gives the Rivenmen side a natural place for their names in lookout lines and chronicles.
7. Fight live-control ramp: P11 and section 5.

---

## 8. Source list

Tags are as in section 0.

- Orkin, J. "Three States and a Plan: The A.I. of F.E.A.R." GDC 2006. https://www.gamedevs.org/uploads/three-states-plan-ai-of-fear.pdf [V]
- Butcher, C. & Griesemer, J. "The Illusion of Intelligence: The Integration of AI and Level Design in Halo." GDC 2002. https://www.jmeiners.com/shamans/papers/ai/the_illusion_of_intelligence.pdf [V]
- Isla, D. "Handling Complexity in the Halo 2 AI." GDC 2005. https://www.gamedeveloper.com/programming/gdc-2005-proceeding-handling-complexity-in-the-i-halo-2-i-ai [S]
- Isla, D. "Building a Better Battle: HALO 3 AI Objectives." GDC 2008. https://gdcvault.com/play/497/Building-a-Better-Battle-HALO [S]
- Booth, M. "The AI Systems of Left 4 Dead." AIIDE 2009. https://steamcdn-a.akamaihd.net/apps/valve/2009/ai_systems_of_l4d_mike_booth.pdf [V]
- Ruskin, E. "AI-driven Dynamic Dialog through Fuzzy Pattern Matching." GDC 2012. https://gdcvault.com/play/1015528/AI-driven-Dynamic-Dialog-through [S]
- Cheng, A. et al. "AI Postmortems: Assassin's Creed III, XCOM: Enemy Unknown, and Warframe." GDC 2013. https://www.gdcvault.com/play/1018058/AI-Postmortems-Assassin-s-Creed [existence S; contents not read]
- UFOpaedia, "Tactical AI" (XCOM). https://www.ufopaedia.org/index.php/Tactical_AI [S]
- Wikipedia, "XCOM 2: War of the Chosen." https://en.wikipedia.org/wiki/XCOM_2:_War_of_the_Chosen [S]
- Total War Wiki, "Morale." https://totalwar.fandom.com/wiki/Morale ; "About Shogun: Total War." https://wiki.totalwar.com/w/About_Shogun:_Total_War.html [S]
- Weber, B. & Mateas, M. "A Data Mining Approach to Strategy Prediction." IEEE CIG 2009. [S]
- Vinyals, O. et al. "Grandmaster level in StarCraft II using multi-agent reinforcement learning." *Nature* 575, 2019. https://www.nature.com/articles/s41586-019-1724-z [S]
- AoE2 AI Scripting Encyclopedia. https://airef.github.io/ [S]
- McIlroy-Young, R., Sen, S., Kleinberg, J., Anderson, A. "Aligning Superhuman AI with Human Behavior: Chess as a Model System." KDD 2020. https://arxiv.org/abs/2006.01855 [S]
- Chessmaster 10th Edition AI Personalities FAQ. https://gamefaqs.gamespot.com/pc/921361-chessmaster-10th-edition/faqs/38373 [S]
- Wars Wiki, "Commanding Officer." https://warswiki.org/wiki/Commanding_Officer [S]
- FE Universe, "[FE7] The Official AI Documentation Thread." https://feuniverse.us/t/fe7-the-official-ai-documentation-thread/348 [S]
- Davis, M. (with Ma, J.) "Into the Breach Design Postmortem." GDC 2019. https://media.gdcvault.com/gdc2019/presentations/Into%20the%20Breach%20Postmortem%20Final.pdf [V]
- Thompson, T. "The Perfect Organism: The AI of Alien: Isolation." Game Developer, 2017. https://www.gamedeveloper.com/design/the-perfect-organism-the-ai-of-alien-isolation [S]
- Thompson, T. "Revisiting the AI of Alien: Isolation." AI and Games, 2020. https://www.aiandgames.com/p/revisiting-alien-isolation [S]
- Švelch, J. "Should the Monster Play Fair?" *Game Studies* 20(2), 2020. https://gamestudies.org/2002/articles/jaroslav_svelch [S]
- Billings, D. et al. "The challenge of poker." *Artificial Intelligence* 134, 2002. [S]
- Southey, F. et al. "Bayes' Bluff: Opponent Modelling in Poker." UAI 2005. https://arxiv.org/abs/1207.1411 [S]
- Hingston, P. "A Turing Test for Computer Game Bots." IEEE TCIAIG, 2009. [M] BotPrize 2012 results: https://news.utexas.edu/2012/09/26/artificially-intelligent-game-bots-pass-the-turing-test-on-turings-centenary/ [S]
- Bates, J. "The Role of Emotion in Believable Agents." *CACM* 37(7), 1994. [M]
- Johnson, S. "Playing to Lose: AI and Civilization." GDC 2008. https://www.designer-notes.com/playing-to-lose-ai-and-civilization-gdc-2008/ [S]
- Meier, S. "The Psychology of Game Design (Everything You Know Is Wrong)." GDC 2010. https://gdcvault.com/play/1012186/The-Psychology-of-Game-Design [S]
- Konami, "The Phantom Pain: Enemy Preparedness." https://eu-support.konami.com/hc/en-gb/articles/9667929703191-The-Phantom-Pain-Enemy-Preparedness [S]
- US Patent 10,926,179 (Nemesis System), granted 2021-02-23. https://www.patentarcade.com/2021/02/warner-brothers-granted-patent-for-nemesis-system-from-middle-earth-video-games.html [S]
- McIntosh, T. "Human Enemy AI in The Last of Us." *Game AI Pro 2*, ch. 34, 2015. https://www.gameaipro.com/GameAIPro2/GameAIPro2_Chapter34_Human_Enemy_AI_in_The_Last_of_Us.pdf [S via summary]
- Fan, G. "How I Got My Mom to Play Through Plants vs. Zombies." GDC 2012. https://www.gdcvault.com/play/1015541/How-I-Got-My-Mom [S]
- Frozen Synapse (Mode 7, 2011). https://en.wikipedia.org/wiki/Frozen_Synapse [S; the determinism detail is M]
- Bad North (Plausible Concept, 2018). https://www.badnorth.com/ [S]
- Nelson, H. Trafalgar memorandum, 9 Oct 1805 (public domain) [M]
