# Research Corpus: Real Military Stratagems for the Mystaeri Fleet

Research input for the Rivenkeep fleet-stratagem ladder (2026-09-25). This is a derivation corpus, not a design decision. It follows Jack's law: ideas and numbers come from the real world wherever there is evidence.

What it covers: all Thirty-Six Stratagems, Sun Tzu's core principles, and 26 naval, amphibious and siege case studies. It then describes how real militaries moved from crude first contact to sophisticated doctrine, and ends with a candidate tier ladder of about 55 fleet stratagems, arranged so simple ones build into complex ones.

---

## 0. How to read this corpus

### 0.1 The constraints every "fleet expression" below obeys

The constraints come from the Fleet Memory and Ships docs and from Jack's vision:

- **The fleet is blind.** A ship acts only on what it has perceived through the three channels:
  - **LOS**: live vision, gated by occluders and distance.
  - **Contact**: hard facts that persist and change only when something contradicts them.
  - **Effect**: the soft ~10x10 fear grid.

  It never reads the true cannon roster, AoR radii, loaded domains, HP or fire-control stances. "Targets the key battery" always means "targets the battery it has a Contact for".
- **The fleet is deterministic.** Fleet behaviour is a pure function of the seed plus each unit's observation history. A stratagem is therefore a finite-state plan with four parts:
  1. **Preconditions** over perceived state.
  2. **Role assignment**: which hulls play which part.
  3. **Phases stamped in sim ticks.** One game-hour is one tick. A siege day is 18 ticks, so the 3-day siege is 54 ticks.
  4. **Branch or abort conditions**, triggered by observed events.

  No wall-clock time and no unseeded randomness are involved.
- **"One second earlier or later" matters.** Most stratagems below have a **hinge tick**: a moment when the defender's action or silence decides which branch the fleet takes. For example, if a battery fires before the bait crosses a line, the bait has exposed it; if the battery holds, the bait passes. The Fight's time ramp-down on orders (to 18 real seconds per game-hour) turns these hinges into deliberate decisions rather than reflexes.
- **Strategy, not skill.** Every counter listed is a defender lever: hold-fire and fire-control timing, AoR re-task, domain switch, Deploy relocation, walls, bait and ghost structures, Reveal towers (Flare/Spotter), Camouflage, and the cannon types (Piercer, Finisher, Marksman, Splasher, Chain, Sweeper, Saturation, Overwatch, Frost, Jammer, Disabler, Interdictor, Suppressor, Breaker). No counter requires aim or click speed.
- **Legibility is a hard constraint.** Every stratagem must carry a **tell**: on-screen behaviour the player learns to recognise. Many tells below come straight from history, such as Hastings' too-orderly "rout", smoke before a landing, or dust and settling over a mine gallery.
- **Unit vocabulary.** Fleet roles use the Ships-doc lineages:
  - Sea hulls: Bombard (warship), Recon, Runner (troop transport), Bulwark (screen), Sower (smoke/mines/fire), Reaver (hunts cannons on confirmed fixes), Quartermaster (support).
  - Air: Skyfall (bomber carrier).
  - Late lineages: Provocateur, Breacher, Corsair, Wraith, Mimic, Herald, Leviathan.
  - Flagship: the propagation hub and resolve anchor.

  "Raiders" means Reaver, Corsair or Wraith.

### 0.2 Entry fields

Each entry has these fields:

- **Mechanism**: how the stratagem actually works, in one or two sentences.
- **Needs**: the preconditions for it to work.
- **Counters**: the classic historical answers, which usually map onto a defender lever.
- **Fleet expression**: how a blind, deterministic fleet of ships, transports, bombers and raiders attacking a walled coastal fort with static cannons could do it. This includes the tell.
- **Tier**: a suggested period (T1 to T6, see 0.3), plus "builds from" and "builds into" where a simple stratagem grows into a complex one.
- **Fit**: how well it suits this game. *Strong* means it works as-is. *Adapted* means it needs reinterpretation. *Conditional* means it depends on a mechanic the game may not have.

### 0.3 Tiers: an information ladder, not just a difficulty ladder

Across history, the sophistication of a stratagem tracks how much it needs to know about the enemy. That fits a blind fleet naturally, because each tier needs one more channel of knowledge than the tier before it.

| Tier | Working name | What the fleet needs to know | Historical echo |
|---|---|---|---|
| **T1** | First Contact (unorganized raiders) | Nothing. Per-ship rules only, with no shared plan. | Vikings 787 to 793, Sea Peoples, U-boats in 1939 |
| **T2** | Probing Fleets | LOS and simple group roles (screen, probe, demonstration) | Carhampton 840, the Mongol 1274 probe of Japan, Dieppe |
| **T3** | Ordered Squadrons | The Contact ledger and two-group timed plans | Wolfpack homing, Trafalgar |
| **T4** | Cunning Fleets | A model of the defender's *reactions*, taken from earlier sorties of the same battle | Q-ship decay, WATU, Jutland |
| **T5** | Grand Designs | Multi-group, multi-domain synchronisation through the flagship | Cannae, Kalka, Midway, Lepanto |
| **T6** | Campaign Chains | Chains across several sorties and switching stratagem when the current one is countered | Fortitude, Agrippa, the Viking arc |

Tiers overlap. A T1 behaviour such as "swarm the breach" never disappears; later fleets do it only when their better estimator says the breach is real.

---

## 1. The Thirty-Six Stratagems (三十六計)

The text is a late-imperial Chinese compilation of 36 proverbs arranged in six chapters of six. It resurfaced in 1941. The phrase "of the 36 stratagems, retreat is best" already appears in the *Book of Southern Qi* (6th century), alluding to the general Tan Daoji.

Most of the proverbs summarise a story. The stories come from Warring States history, the Three Kingdoms period, or the novel *Romance of the Three Kingdoms*; entries flag the novel where it applies. The chapters run from stratagems for when you are winning (1) to stratagems for when you are losing (6).

### Chapter 1: Winning Stratagems (勝戰計 shèng zhàn jì), used when you hold the advantage

**#1 瞞天過海 Mán tiān guò hǎi. "Deceive the heavens to cross the sea."**
- *Mechanism:* Hide an extraordinary action inside something the enemy has come to see as routine. In the traditional story, the Tang emperor feared the sea crossing to Goguryeo, so he was feasted in a "seaside house" that was really a ship already under way.
- *Needs:* A pattern repeated often enough that the enemy stops watching it.
- *Counters:* Treat routine as suspect, and audit what "always happens".
- *Fleet expression:* Conditioning. For two or three sorties, transports (Runners) always idle at the same far fringe cell and leave at the same tick. The player learns to ignore them and aims AoRs elsewhere. On sortie N, the idle position becomes the landing approach at that same departure tick.
  - The precondition is perceived: the fleet's fear grid shows that fringe stayed COLD.
  - *Tell:* The idle group rides lower in the water (it carries troops), or its idle tick shifts by one.
- *Tier:* T6. Builds from Hang at the Fringe (T1). *Fit:* Strong.

**#2 圍魏救趙 Wéi Wèi jiù Zhào. "Besiege Wei to rescue Zhao."**
- *Mechanism:* When Wei besieged Zhao's capital, Sun Bin of Qi marched on Wei's own capital instead. Wei's army had to abandon the siege and was ambushed on its way home (Guiling, 353 BC). The principle: threaten what the enemy must defend, and he leaves off what he is attacking.
- *Needs:* Knowledge of something the enemy values more than his current objective.
- *Counters:* Refuse the bait if the threat is hollow. Keep a reserve that is not committed to the main action.
- *Fleet expression:* The player's fire is concentrated on the fleet's transports, so the Effect channel shows those hulls taking heavy fire. At that moment a Bombard group threatens a castle, or a contacted open breach, in another sector. The aim is to force the player into a costly AoR re-task or fire-control switch that takes pressure off the transports.
  - *Hinge:* The player either keeps firing on the transports and lets the threat develop, or pays the re-task.
- *Tier:* T3. *Fit:* Strong.

**#3 借刀殺人 Jiè dāo shā rén. "Kill with a borrowed knife."**
- *Mechanism:* Let a third party, or the enemy's own tools, do the damage.
- *Needs:* A force that is neither yours nor spent at your cost, such as terrain, weather, an ally, or the enemy's own weapons.
- *Counters:* Recognise the manipulation and deny the third party its opening.
- *Fleet expression:* The only honest versions are environmental or reflexive:
  - A fireship set adrift on a seeded current or wind, so physics does the killing.
  - If the game has friendly fire, a hull that parks beside a wall section so the player's Splasher damages the player's own wall.
  - Burning debris from a sunk Sower drifting into the fort.
- *Tier:* T4. *Fit:* Conditional (needs currents or wind, or friendly splash).

**#4 以逸待勞 Yǐ yì dài láo. "Wait at leisure while the enemy exhausts himself."**
- *Mechanism:* This comes from Sun Tzu ch. 7. Arrive rested at the place of battle, let the enemy march, spend and tire, then strike when he is spent.
- *Needs:* The enemy must have a consumable: ammunition, heat, reload time, repair capacity, or the timer.
- *Counters:* Don't spend into empty water. Practise fire discipline.
- *Fleet expression:*
  - *Crude (T1):* Loiter in cold fringe cells and let the defender's early shots miss or fall on screens.
  - *Refined (T2 to T4):* The fleet can see muzzle flashes, so LOS logs each battery's firing cadence as Contact. The assault is timed to land in the observed reload window of the batteries covering the approach, or after a burst of long-range fire has been spent on Bulwarks.
  - *Tell:* The fleet holds just outside the fear haze until your guns go quiet, then moves on the silence.
- *Tier:* T1 (crude) builds to T4 (cadence-timed). *Fit:* Strong. It pairs directly with the player's hold-fire lever.

**#5 趁火打劫 Chèn huǒ dǎ jié. "Loot a burning house."**
- *Mechanism:* Strike an enemy who is already in internal disorder: a breach, a fire, a collapsed command.
- *Needs:* Visible evidence of disorder.
- *Counters:* Hide disorder. Plant false disorder, for example a ghost breach that is really a kill-zone.
- *Fleet expression:* This is the most basic T1 behaviour. Any hull with a Contact for a breach, or a cell that has just gone cold because a gun died, diverts to pour in. It is individual and uncoordinated, just like the early Viking and Sea Peoples raiders.
  - *Counter:* The player's existing ghost-breach and hidden-breach bait layer.
  - *Later form (T3 and up):* Only pile in after verification, meaning a second observer confirms the breach is not HOT.
- *Tier:* T1. Builds into Run the Batteries (T2), Wolfpack Convergence (T3) and Cannae (T5). *Fit:* Strong.

**#6 聲東擊西 Shēng dōng jī xī. "Make a sound in the east, strike in the west."**
- *Mechanism:* A short, noisy feint draws attention and forces to one place while the blow falls somewhere else.
- *Needs:* The enemy must react to the noise, and the real strike needs to be timed inside that reaction.
- *Counters:* Stay in depth, hold reserves, and don't commit your whole stance to the first threat.
- *Fleet expression:* A Bombard or Provocateur group makes a loud, fire-drawing demonstration on flank A, starting at tick t. Transports aim to land on flank B at t + Δ, where Δ is roughly the time a player needs to re-task toward A.
  - *Hinge:* If the player re-tasks within the window, B is uncovered. If the player holds, the feint wastes itself.
  - *Tell:* The demonstrating hulls don't close. They make lateral motion without fore-aft commitment, which is the Ships-doc motion grammar.
- *Tier:* T2. Builds into #8 (T4) and Fortitude (T6). *Fit:* Strong.

### Chapter 2: Enemy-Dealing Stratagems (敵戰計 dí zhàn jì), used against an equal enemy

**#7 無中生有 Wú zhōng shēng yǒu. "Create something from nothing."**
- *Mechanism:* The model is Zhang Xun at the siege of Yongqiu in 756. He lowered straw dummies from the walls at night; the besiegers shot them full of arrows, which he harvested. After several nights the enemy stopped reacting to "dummies". Then he lowered 500 real men, who raided and routed the enemy camp. So: repeat a false signal until the enemy discounts it, then make it real.
- *Needs:* An enemy who learns, and who learns the wrong lesson.
- *Counters:* Never fully discount a repeated signal. Verify it cheaply each time.
- *Fleet expression:* Mimic decoys, or empty hulls, run the same night approach toward the harbour mouth over several sorties. The player learns they are harmless and stops spending fire on them.
  - On a later sortie the same silhouettes carry troops.
  - The precondition is perceived: the fear grid shows that the approach stayed COLD on the earlier runs.
  - *Tell:* The real ones cast a wake, or turn one tick later.
- *Tier:* T4. *Fit:* Strong. It is the canonical "they recognise the strategy" moment.

**#8 明修棧道，暗渡陳倉 Míng xiū zhàn dào, àn dù Chéncāng. "Openly repair the gallery roads, secretly march through Chencang."**
- *Mechanism:* In 206 BC Han Xin loudly rebuilt the burned mountain roads, while his army took a hidden route through Chencang. The difference from #6 is that the visible effort is a credible, sustained operation that could succeed on its own, not a short feint.
- *Needs:* A visible effort that is expensive enough to be believed, and a hidden route.
- *Counters:* Ask what the visible effort cannot achieve by itself, and watch the "impossible" approaches.
- *Fleet expression:* Over a whole sortie, Sowers clear mines and Bombards methodically reduce wall section A. It is a real siege that would breach A in about two sorties. Meanwhile a Wraith group uses a LOS-occluded approach, behind a headland, smoke, or the wall's own shadow, to reach section B.
  - *Tell:* A's attackers never bring transports.
- *Tier:* T4. Builds from #6. *Fit:* Strong.

**#9 隔岸觀火 Gé àn guān huǒ. "Watch the fire burning across the river."**
- *Mechanism:* When enemies are falling out among themselves, stand back and let the fire burn; intervening would unite them. In 207, Cao Cao withdrew rather than press the Yuan brothers, who then fled to Gongsun Kang and were killed by him.
- *Needs:* The enemy is degrading on its own.
- *Counters:* Resolve the internal problem fast, or fake one.
- *Fleet expression:* With one defender there is no feud to wait on. The honest version is to stand off while something already set in motion keeps hurting the fort: a Sower's persistent fire on a wall, a mine gallery (see siege craft) working toward collapse, or the player's own repair backlog.
  - *Tell:* The fleet stops attacking and simply watches while a fire burns.
- *Tier:* T2. Overlaps with #4. *Fit:* Adapted.

**#10 笑裏藏刀 Xiào lǐ cáng dāo. "Hide a knife behind a smile."**
- *Mechanism:* Appear harmless or friendly, win access, then strike. The WWI Q-ship is the purest naval form (see 3.14).
- *Needs:* The enemy must have a rule that treats "harmless-looking" as safe to approach, or not worth a shot.
- *Counters:* Treat every approach by its capability rather than its look, and keep standoff distance.
- *Fleet expression:* A Q-hull with a Quartermaster or Runner silhouette, apparently soft, sails into the player's close zone. If the player ignores it because it is "not a threat", it unmasks guns at the wall or on a contacted battery.
  - *Tell:* Its draft or gunports are subtly different under a Flare.
  - *Decay:* Once the player learns the tell, it stops working, just as the real Q-ships did.
- *Tier:* T3. *Fit:* Strong.

**#11 李代桃僵 Lǐ dài táo jiāng. "Sacrifice the plum tree to preserve the peach tree."**
- *Mechanism:* Accept a planned, smaller loss to protect what matters.
- *Needs:* A clear value ranking and cheap assets to spend.
- *Counters:* Shoot what matters, not what is presented. Back-line targeting.
- *Fleet expression:*
  - *T1:* The cheapest hulls simply lead.
  - *T2:* Deliberate screens. Bulwarks move into HOT cells so that transports travel in their cold shadow.
  - The Midway torpedo squadrons (3.16) show the accidental form: sacrifice that draws the defence away.
  - *Tell:* Hulls press into your fire without firing back.
- *Tier:* T1 builds to T2, then Break the Line (T3) and Lepanto (T5). *Fit:* Strong.

**#12 順手牽羊 Shùn shǒu qiān yáng. "Lead away a goat in passing."**
- *Mechanism:* While executing the main plan, seize small opportunities that cost no deviation.
- *Needs:* An opportunity inside the path.
- *Counters:* Don't leave loose "goats" (exposed small assets) along predictable paths.
- *Fleet expression:* Raiders on transit fire at any structure that enters their LOS, but never alter course for it. This is the T1 raider personality: the Lindisfarne logic of taking portable wealth and moving on.
- *Tier:* T1. *Fit:* Strong.

### Chapter 3: Attacking Stratagems (攻戰計 gōng zhàn jì)

**#13 打草驚蛇 Dǎ cǎo jīng shé. "Beat the grass to startle the snake."**
- *Mechanism:* Make a deliberate disturbance to provoke a hidden enemy into revealing himself. In modern doctrine this is reconnaissance by fire.
- *Needs:* The hidden enemy must be inclined to react.
- *Counters:* Hold fire. Don't be startled.
- *Fleet expression:* This is the signalling game's own core.
  - *T1:* The crude form is to advance until something fires.
  - *T2:* Ships fire speculatively into suspected cells: shadows, walls, fear-grid edges. Any muzzle flash writes a Contact.
  - *Counter:* The player's defining verb, hold-fire. A battery that stays silent never enters the fear grid.
  - *Hinge:* The tick at which the probing shell lands near a hidden gun.
- *Tier:* T1 builds to T2, then #17, the AF Ruse (T4) and the Double Agent (T6). *Fit:* Strong. This is the spine of the whole ladder.

**#14 借屍還魂 Jiè shī huán hún. "Borrow a corpse to resurrect the soul."**
- *Mechanism:* Put something dead or discarded to new use: an old institution, a fallen name, a wreck.
- *Needs:* Leftovers.
- *Counters:* Clear the leftovers.
- *Fleet expression:*
  - The resolve network's field promotion is literally this: a survivor picks up the dead flagship's standard.
  - Wrecks as hard cover, occluders or blockships. The Zeebrugge and Port Arthur blockships show the blockship use.
  - Damaged hulls from the previous sortie, which persist, re-used as the Bulwark line.
  - *Tell:* Hulls cluster behind a wreck.
- *Tier:* T3. *Fit:* Strong, if wrecks persist as occluders.

**#15 調虎離山 Diào hǔ lí shān. "Lure the tiger down the mountain."**
- *Mechanism:* Never fight a tiger on its mountain. Draw it off its strong ground, then take the ground or kill it on the plain.
- *Needs:* Something that tempts the tiger off.
- *Counters:* Stay on the mountain.
- *Fleet expression:* The fort's cannons are static, so the "mountain" is the defender's stance: its AoR aim, loaded domain, and hidden status. The fleet shows a strong air threat (a Skyfall launch) to induce a sea-to-air domain switch on the key battery, then attacks by sea. Or it shows a flank threat to pull an AoR re-task away from the harbour mouth.
  - *Tell:* The threat is shown well before it is delivered.
- *Tier:* T3. *Fit:* Adapted. Luring maps onto stance, not position.

**#16 欲擒故縱 Yù qín gù zòng. "To capture, first let it go."**
- *Mechanism:* In the traditional story, Zhuge Liang captured and released Meng Huo seven times. Don't corner a desperate enemy; let pressure off, and he loosens and exposes himself.
- *Needs:* Patience, and an enemy who relaxes.
- *Counters:* Don't relax when pressure lifts.
- *Fleet expression:* An information-ecology stratagem. The fleet deliberately leaves a known, contacted battery alive. If it killed that battery, the player would rebuild it somewhere unknown in Deploy. A known gun can be avoided or timed around; an unknown one cannot.
  - *Tell:* Your exposed gun is conspicuously ignored.
- *Tier:* T4. *Fit:* Strong, and subtle. It rewards players who notice.

**#17 拋磚引玉 Pāo zhuān yǐn yù. "Toss out a brick to lure a jade."**
- *Mechanism:* Offer something cheap to draw out something precious.
- *Needs:* The enemy must mistake the brick for something worth jade.
- *Counters:* Price targets before you spend on them.
- *Fleet expression:* A cheap hull enters the likely kill-zone of a special cannon: the Marksman, Piercer charge, or Saturation strike. It draws that cannon's expensive shot and cooldown, and writes that cannon's position to Contact.
  - *Tell:* One lonely, cheap hull heads exactly where your best gun looks.
- *Tier:* T2. Builds from #13. *Fit:* Strong.

**#18 擒賊擒王 Qín zéi qín wáng. "To catch bandits, catch their king."**
- *Mechanism:* The line is from a Du Fu poem: to shoot a man, shoot his horse first; to capture bandits, capture their king. Decapitation dissolves the organisation.
- *Needs:* You must know which node is the king.
- *Counters:* Redundancy and hidden command. Protect the head.
- *Fleet expression:* The fleet identifies the enabling structure through Contact and focuses on it. That might be the Reveal tower (the defender's eyes), a magazine, or the tower that feeds the others.
  - This needs inference ("that tower's flare preceded every hit"), so it is late.
  - *Tell:* Every group converges on one of your structures and ignores closer targets.
  - *Counter:* Camouflage, ghost towers, redundancy.
- *Tier:* T5. *Fit:* Strong.

### Chapter 4: Chaos Stratagems (混戰計 hùn zhàn jì), used in confused situations

**#19 釜底抽薪 Fǔ dǐ chōu xīn. "Remove the firewood from under the cauldron."**
- *Mechanism:* Remove the source of strength rather than fighting the strength. At Guandu in 200, Cao Cao burned Yuan Shao's grain at Wuchao. Agrippa at Actium (3.3) is the naval form.
- *Needs:* A dependency the enemy's strength relies on.
- *Counters:* Protect and disperse supply and magazines.
- *Fleet expression:* Target the fort's sustainment rather than its guns: magazines, powder, repair yards, and whatever Build economy the defender has.
  - *Tell:* Bombers or Reavers pass over live guns to hit a storehouse.
- *Tier:* T4. *Fit:* Conditional. It needs the defender to have sustainment structures.

**#20 混水摸魚 Hùn shuǐ mō yú. "Muddy the water to catch fish."**
- *Mechanism:* Create confusion and take what you want in it.
- *Needs:* A means of confusion.
- *Counters:* Clarity tools such as flares and fixed fire plans, and staying calm.
- *Fleet expression:* Sower smoke combined with a mass of small, simultaneous arrivals on several bearings. The defender cannot prioritise, and transports slip through the chaos.
  - *Tell:* Smoke comes before a surge.
  - *Counter:* Flare/Spotter, Saturation, and pre-assigned AoRs that don't need a decision.
- *Tier:* T2. *Fit:* Strong.

**#21 金蟬脫殼 Jīn chán tuō qiào. "The golden cicada sheds its shell."**
- *Mechanism:* Escape by leaving a convincing empty shell behind. In the Gallipoli evacuation of December 1915, "drip rifles" fired on water timers and weeks of conditioning "silent stunts" covered the withdrawal (3.15).
- *Needs:* A shell the enemy keeps believing in, even briefly.
- *Counters:* Probe the shell.
- *Fleet expression:* When resolve breaks, the main body withdraws while Mimic decoys, or damaged hulls left anchored, keep up a signature. The player keeps spending fire on them, and the real hulls survive to the next sortie.
  - *Tell:* The "fleet" stops manoeuvring.
- *Tier:* T4. Builds from Scatter and Run (T1). *Fit:* Strong.

**#22 關門捉賊 Guān mén zhuō zéi. "Shut the door to catch the thief."**
- *Mechanism:* Encircle and cut off the enemy's escape and relief, then destroy him. Bai Qi at Changping in 260 BC is the example.
- *Needs:* A mobile enemy element that can be cut off.
- *Counters:* Don't over-extend. Keep the exits open.
- *Fleet expression:* A static fort has no "thief" to catch. The honest versions:
  - Blockade the harbour mouth, with blockships or Sower mines, so defender boats can't sortie.
  - If the defender has mobile units such as boats or sally troops, let them come out and then close behind them.
- *Tier:* T4. *Fit:* Conditional (defender mobiles).

**#23 遠交近攻 Yuǎn jiāo jìn gōng. "Befriend the distant state, attack the neighbour."**
- *Mechanism:* Around 270 BC, Qin's policy under Fan Ju was to keep far enemies quiet while devouring near ones, one at a time.
- *Needs:* The ability to engage selectively.
- *Counters:* Mutual support, and don't stay passive while a neighbour dies.
- *Fleet expression:* Piecemeal reduction. The fleet stays outside the perceived AoR of distant batteries so they never fire and never learn anything, while it destroys the nearest sector.
  - *Tell:* The fleet hugs one sector.
  - *Counter:* Overlapping AoRs. Distant batteries that are willing to fire at long range and reveal themselves.
- *Tier:* T2. *Fit:* Strong.

**#24 假道伐虢 Jiǎ dào fá Guó. "Borrow the road to conquer Guo."**
- *Mechanism:* In 655 BC, Jin borrowed passage through Yu to attack Guo, then took Yu on the way home. The idiom it produced is "when the lips are gone, the teeth are cold".
- *Needs:* A party that lets you pass.
- *Counters:* Never let a strong force pass. Anyone allowed to pass has seen you.
- *Fleet expression:* A transit wave heads for the harbour and ignores battery X going in. The player keeps X silent to protect it. But X is inside the wave's LOS during transit, so its position goes to Contact. On the return leg, the wave strikes X.
  - *Hinge:* Firing on the transit wave reveals X now. Holding reveals it to LOS anyway if X is not occluded. Camouflage is the real counter.
- *Tier:* T4. *Fit:* Strong.

### Chapter 5: Proximate Stratagems (並戰計 bìng zhàn jì), used against allies or near equals

**#25 偷梁換柱 Tōu liáng huàn zhù. "Steal the beams and swap the pillars."**
- *Mechanism:* Covertly change the internal structure while the outside looks the same, or subvert the enemy's structure.
- *Needs:* A trusted outward form.
- *Counters:* Verify the substance, not the silhouette.
- *Fleet expression:* Between sorties, the fleet swaps which hull holds which role while keeping the same formation silhouette. The flag icon, or the "flagship position" in the convoy, is worn by a decoy while the real flag sails elsewhere. This is the Mimic-boss "Impostor".
  - *Tell:* The flag hull's behaviour doesn't match its hull.
- *Tier:* T5. *Fit:* Strong.

**#26 指桑罵槐 Zhǐ sāng mà huái. "Point at the mulberry, curse the locust tree."**
- *Mechanism:* Discipline or deter indirectly by making an example of someone else. Sima Rangju executed a late noble to steel his army.
- *Needs:* An observer who draws the lesson.
- *Counters:* Don't learn the lesson the enemy wants you to learn.
- *Fleet expression:* Deterrence by example, aimed at the player's mind. The first battery that reveals itself early is punished overwhelmingly, with all Reavers and Bombards on it. The player learns that whoever fires first dies, becomes over-cautious, and that caution cools a lane the fleet then uses.
  - *Tell:* A violent overreaction to the first gun that speaks.
- *Tier:* T3. *Fit:* Adapted. It works on the human, which is exactly Jack's "another human running the enemy".

**#27 假痴不癲 Jiǎ chī bù diān. "Feign madness but keep your balance."**
- *Mechanism:* Play the fool so the enemy drops his guard, while keeping your wits.
- *Needs:* A credible fool persona.
- *Counters:* Judge by capability, not by display.
- *Fleet expression:* A sophisticated fleet imitates T1 behaviour, blundering into cold-looking cores and "swarming" obvious breaches. This invites the player's aggressive, T1-grade answer: exposed guns and early fire. Later groups then exploit everything the player revealed.
  - This only works because the player has learned the T1 patterns, so it belongs late in the campaign.
  - *Tell:* The "blunderers" never actually die in the kill-zone. They turn one cell short.
- *Tier:* T6. *Fit:* Strong. It is the Ender's Game arc turned back on itself.

**#28 上屋抽梯 Shàng wū chōu tī. "Remove the ladder when the enemy has climbed onto the roof."**
- *Mechanism:* Lure the enemy into a position or commitment, then remove his way back.
- *Needs:* An irreversible commitment.
- *Counters:* Avoid irreversible moves on enemy invitation.
- *Fleet expression:* The ladder is the player's reversibility. The fleet induces an expensive commitment that can't be undone until Deploy: a costly re-task, a domain switch, or a hidden battery's first shot (a Contact stays until contradicted). Then it attacks where that commitment is wrong.
  - *Hinge:* The moment the player spends the costly verb.
- *Tier:* T4. *Fit:* Strong.

**#29 樹上開花 Shù shàng kāi huā. "Deck the tree with false blossoms."**
- *Mechanism:* Make a small force look large. In the novel, Zhang Fei dragged branches behind horses to raise dust at Changban. Fortitude's dummy landing craft and radio nets are the modern form (3.17).
- *Needs:* Cheap signatures.
- *Counters:* Reconnaissance that can tell real from false.
- *Fleet expression:* Mimic silhouettes, and air "phantoms" (a Taxable/Glimmer-style chaff analogue), inflate the apparent threat on a flank so the player over-commits AoR there.
  - *Tell:* The phantoms vanish under Flare or Spotter light, and never leave wrecks.
- *Tier:* T3. *Fit:* Strong.

**#30 反客為主 Fǎn kè wéi zhǔ. "Make the host and the guest exchange roles."**
- *Mechanism:* The guest gradually takes over the house. The invader becomes the entrenched power.
- *Needs:* A foothold that can be fortified.
- *Counters:* Evict the guest early.
- *Fleet expression:* Troops ashore dig in and become a static threat inside the perimeter that the defender must reduce. Historical models are the Viking fortified camps (3.7), Alexander's mole at Tyre (3.8) and the 1453 ships in the Golden Horn.
  - **This conflicts with the current rule** that troops are cleared at the end of every sortie. It works within a sortie as-is; across sorties it would need an explicit beachhead rule.
- *Tier:* T5. *Fit:* Conditional.

### Chapter 6: Defeat Stratagems (敗戰計 bài zhàn jì), used when losing

**#31 美人計 Měi rén jì. "The beauty trap."**
- *Mechanism:* Weaken the enemy through his own desire. Xi Shi was sent to King Fuchai of Wu.
- *Needs:* Something the enemy cannot resist.
- *Counters:* Discipline.
- *Fleet expression:* The "treasure ship". A slow, apparently undefended, high-value hull (a flagship-looking silhouette or a laden transport) parades through the kill-zone. It tempts the player's hidden batteries to break silence for the big prize, revealing them to waiting Reavers. The Q-ship exploited exactly the U-boat's desire for easy prey.
  - *Tell:* A prize that is too easy.
- *Tier:* T3. *Fit:* Strong.

**#32 空城計 Kōng chéng jì. "The empty fort stratagem."**
- *Mechanism:* In the novel, Zhuge Liang opened his undefended gates and played the zither on the wall. Sima Yi, sure it was an ambush, withdrew. Project calm confidence from weakness so the enemy supposes a trap.
- *Needs:* An enemy who believes you are cunning.
- *Counters:* Probe cheaply.
- *Fleet expression:* This is natively the defender's stratagem; the player's hold-fire is an empty-fort play. For the fleet, the inverse: a battered, weak group advances in immaculate formation with no hesitation. A cautious player assumes a hidden main body behind the fog and holds fire or re-tasks.
  - It is late because it exploits a player who has learned to fear the fleet's cunning.
  - *Tell:* No second wave ever appears on the fear edge.
- *Tier:* T5. *Fit:* Adapted.

**#33 反間計 Fǎn jiàn jì. "Let the enemy's own spy sow discord."**
- *Mechanism:* Turn the enemy's information channels against him. In the novel, Jiang Gan was fed a forged letter that made Cao Cao execute his own admirals. Historically, Themistocles carved messages at watering places for the Ionian Greeks serving Xerxes, hoping to cause defection or at least distrust (Herodotus 8.22). In WWII, Garbo's network fed false reports.
- *Needs:* The enemy must be using an information channel you can feed.
- *Counters:* Cross-check sources, and don't trust a single channel.
- *Fleet expression:* The player's "spies" are the Reveal towers and the player's own learned tells. The fleet behaves differently inside a Flare's light than outside it: it shows a false formation under the flare and the real one in the dark.
  - Hardest version: a hull occasionally displays a known tell falsely, so the player's pattern-reading is turned against them.
  - **Legibility risk:** a false tell must carry its own counter-tell, or this breaks the fairness law.
- *Tier:* T6. *Fit:* Adapted and risky.

**#34 苦肉計 Kǔ ròu jì. "Inflict injury on oneself to win the enemy's trust."**
- *Mechanism:* In the novel, Zhou Yu flogs Huang Gai so his "defection" to Cao Cao will be believed. Huang Gai's surrender fleet then arrives as fireships at Red Cliffs (208), which is historical.
- *Needs:* A credible wound.
- *Counters:* Distrust any gift or defection that arrives at the decisive moment.
- *Fleet expression:* A hull shows damage (burning, listing, "drifting derelict") and drifts toward the wall or the harbour boom. The player ignores it as spent or saves the shot. It detonates as a fireship, or lands troops.
  - *Tell:* The derelict is drifting against the wind or current.
- *Tier:* T4. *Fit:* Strong.

**#35 連環計 Lián huán jì. "Chain stratagems" (also "interlocking/chained ships").**
- *Mechanism:* The name puns on Red Cliffs, where Cao Cao's ships were moored close together (the novel adds that they were chained on Pang Tong's advice) and so burned together. The meta-principle is to link stratagems so the counter to one sets up the next.
- *Needs:* Multiple stratagems and sequencing.
- *Counters:* Break the first link, and see the chain.
- *Fleet expression:* The late-game capstone behaviour. A branching plan in which each stage's observed outcome selects the next stage. For example: Beat the Grass, and if the player holds, Toss a Brick; if the brick is taken, Remove the Ladder; then Cannae. All of it is deterministic on perceived state.
- *Tier:* T6. *Fit:* Strong.

**#36 走為上策 Zǒu wéi shàng cè. "If all else fails, retreat."**
- *Mechanism:* Withdraw to preserve the force for another day.
- *Needs:* A way out.
- *Counters:* Pursuit, a closed door (#22), or a golden bridge (Sun Tzu) that turns the retreat into a rout.
- *Fleet expression:*
  - *T1:* Resolve collapse becomes a rout, with every hull running for itself. This already exists as sortie Repel and battle Retreat.
  - *T4:* An orderly, covered withdrawal (Jutland's turn-away, 3.12) that saves hulls and, crucially, carries what the fleet learned into the next sortie.
  - *Tell:* A rout scatters; a withdrawal keeps its screen facing you.
- *Tier:* T1 builds to T4. *Fit:* Strong.

---

## 2. Sun Tzu, *The Art of War*: core principles

The principles are paraphrased from the public-domain Giles translation (1910), with chapter numbers. Many of the 36 Stratagems are proverbial compressions of these principles. The ch. 7 and ch. 9 material is especially valuable: ch. 7 gives the defender's counters and ch. 9 gives a catalogue of tells.

| # | Principle (paraphrase) | Ch. | Mechanism | Fleet expression / design use |
|---|---|---|---|---|
| S1 | All warfare rests on deception. Appear unable when able, near when far. Offer bait, feign disorder, then crush. | 1 | Manipulate the enemy's estimate | The whole signalling game. Fleet deception (feints, baits, false blossoms) is the fleet sending signals too. |
| S2 | Know the enemy and yourself and you need not fear a hundred battles. | 3 | Information decides outcomes | The information ladder of tiers. The fleet's power grows with what it knows. |
| S3 | The highest skill is to break resistance without fighting. The order of preference: attack the enemy's plans, then his alliances, then his army. Besieging walled cities is the worst option. | 3 | Walls are expensive to assault | The fleet should *prefer* not to assault walls: make the defence spend, bypass, break resolve. Frontal wall assault is the T1 default and the late fleet's last resort. |
| S4 | First make yourself invincible, then wait for the enemy to become vulnerable. | 4 | Security, then opportunism | Late fleets keep their screens and reserves intact and strike only on a perceived opening (#4, #5 verified). |
| S5 | Zheng and qi: the orthodox force fixes the enemy and the extraordinary force wins. Their combinations are endless. | 5 | Fix and flank | Every two-group stratagem (#6, #8, Cannae). The orthodox group is legible; the extraordinary one is the surprise. |
| S6 | Shi, strategic momentum: like round stones rolled down a mountain, or a drawn crossbow. The skilled general gets results from the configuration, not from demanding it of individuals. | 5 | Position creates outcome | **This is Jack's Brick n Balls principle, stated 2,500 years early.** The player's plan (Deploy) creates shi, and the Fight releases it. The fleet's stratagems are likewise configurations that play themselves out. |
| S7 | Weak and strong (xu/shi): avoid strength, strike weakness. Water shapes its course to the ground. | 6 | Flow to weakness | The fear grid is literally this: AoR-avoidance is water flowing around strength. |
| S8 | Formlessness: make the enemy show his dispositions while staying formless yourself. | 6 | Information asymmetry | Hold-fire (defender) versus probing (fleet). Both sides are trying to be formless. |
| S9 | Concentrate while the enemy divides. If we are one and he is split into ten, we attack with ten to one. | 6 | Local superiority | Break the Line (Trafalgar), piecemeal reduction (#23). |
| S10 | Speed and momentum. No state has benefited from prolonged war. | 2 | Costs of duration | The siege timer. Also the stalemate valve: resolve decays when progress stops. |
| S11 | The eight maxims of manoeuvre: don't pursue a feigned flight, don't attack high ground, don't swallow bait, don't block an army going home, leave a surrounded army an outlet, don't press a desperate foe. | 7 | The canonical counters | **The player's counter list.** Each maxim answers a fleet stratagem: feigned flight, bait, and the golden bridge (let a breaking fleet go rather than making it fanatical). |
| S12 | Read the signs: birds rising mean ambush; high thin dust means chariots and low broad dust means infantry; humble words with more preparation mean an advance; soldiers leaning on spears are hungry. | 9 | **Tells** | The legibility law's ancestor. Every fleet stratagem needs a Sun Tzu ch. 9 sign. Humble words with more preparation is the #10 and #34 tell; birds rising is the #8 hidden-route tell. |
| S13 | Terrain and death ground: soldiers with no escape fight hardest. "Burn the boats." | 10–11 | Commitment raises resolve | Fanatical resolve. A fleet with its retreat cut, or a Herald fleet, fights to the last hull. The golden bridge (S11) is its counter. |
| S14 | Attack by fire: five kinds. Prepare, wait for the right wind, and follow up at once. | 12 | Fire as an amplifier | Sower fire and fireships (#34, Gravelines). The follow-up requirement means a fire attack without a timed follow-up wave is a T2 error; T4 fires with follow-up. |
| S15 | Foreknowledge comes from people, not spirits. Five kinds of spies; the converted spy is the most valuable. | 13 | Intelligence network | Recon lineages are the fleet's spies, and the Reveal towers are the player's. The converted spy is #33. |

---

## 3. Historical cases: naval, amphibious and siege

Cases are roughly chronological. Each one includes the real numbers, because Jack's law asks for them.

### 3.1 Salamis, 480 BC: false intelligence, feigned flight, and the narrows
- **What happened:**
  - Themistocles sent his slave Sicinnus to Xerxes claiming the Greeks would slip away that night. The Persians rowed all night to block the exits, arriving tired, and then attacked into the narrow strait.
  - Herodotus reports that the Corinthian squadron made sail northward as if fleeing (disputed). The Greek line initially backed water, looking fearful, drawing the Persians deeper before turning to ram.
  - In the narrows the Persian numbers fouled each other.
  - Numbers: about 371–378 Greek triremes against about 600–800 Persian (modern estimate; ancient claim 1,207).
- **Mechanism:** Deception about intent draws the enemy into terrain where his mass is a liability. Feigned withdrawal pulls him forward into it.
- **Needs:** A credible channel (a "traitor's" message), plus narrows.
- **Counters:** Refuse chokepoints. Don't act on convenient intelligence. Rest before battle.
- **Fleet expression:** Salamis is mostly the defender's lesson; the player's Rivenkeep channels are narrows. It gives the fleet two things:
  1. *Negatively:* the Cognition axis. Late fleets refuse to crowd into chokepoints and space out on approach, where T1 fleets pile in and foul each other. A literal "fouling" rule, where hulls block each other's movement in narrow cells, would make this visible.
  2. *Positively:* a fleet version of backing water. A bombard line retreats slowly under fire, drawing the player's pursuit fire (more guns revealing, more Contacts) toward range bands where Reavers wait.
- **Tier:** Chokepoint refusal is T3 Cognition. The backing-water lure is T4, building into Kalka (T5).

### 3.2 Themistocles' deceptions: long preparation and the golden bridge
- **What happened:**
  - In 483 BC Themistocles persuaded Athens to spend the Laurium silver strike on about 200 triremes. He also read the Delphic oracle's "wooden walls" as meaning ships.
  - At Artemisium he carved appeals at watering places to the Ionian Greeks serving Persia (#33).
  - After Salamis he sent a second message to Xerxes, claiming he had talked the Greeks out of destroying the Hellespont bridges. It hastened Xerxes' withdrawal, a golden bridge the enemy believed was a favour.
- **Mechanism:** Strategic preparation years ahead, information operations aimed at the enemy's alliances, and managing the enemy's exit.
- **Fleet expression:** The golden bridge is mainly a *player* lever against a breaking fleet: leave it a way out rather than making it fanatical. On the fleet side it gives #33 (messages to the defender's "allies" do not apply) and a campaign idea: a fleet that "offers" the player a stand-down, by withdrawing a flank so the player moves guns in Deploy, then returns (#1).
- **Tier:** T6 (campaign-level).

### 3.3 Actium, 31 BC: strangulation first, battle second
- **What happened:**
  - Before the battle, Agrippa seized Methone, raided along the Greek coast, and cut Antony's supply line to Egypt through the Peloponnese.
  - Antony's army and fleet were trapped at Actium, wasting away from disease (malaria) and desertion. He arrived with about 500 ships but could not man them all, and fought with about 230–250 heavy ships (quinqueremes with towers) against about 400 lighter Liburnians.
  - In the battle, Cleopatra's squadron used a breeze to break out through a gap, and Antony followed. The breakout succeeded, but the fleet collapsed.
- **Mechanism:** Win the campaign before the battle. Remove supply, let attrition do the work, then fight a weakened enemy on your terms. Light, numerous ships beat few heavy ones by manoeuvre.
- **Needs:** A sustainment dependency, time, and command of the sea lanes.
- **Counters:** Break out early, secure supply, or offer battle before starving.
- **Fleet expression:**
  - (a) Composition: many light Corsairs against the fort's slow, heavy guns means rate of target turnover beats the size of each shot.
  - (b) A blockade stratagem: raiders interdict the defender's sustainment (#19) while the main body stays out of range.
  - **Design conflict:** the stalemate valve (resolve decays without progress) would punish a waiting blockader. Either the blockade counts as "progress" when it measurably degrades the defender, or this stratagem stays inert.
- **Tier:** T5 (Agrippa's Strangulation) or T6. *Fit:* Conditional on defender sustainment.

### 3.4 Cannae, 216 BC: the double envelopment
- **What happened:**
  - Hannibal had about 50,000 men (10,000 cavalry) against Rome's about 86,000.
  - He advanced a convex crescent of Gauls and Iberians, which gave ground on purpose under Roman pressure. The Romans, in an unusually deep and compressed formation, pushed into the pocket.
  - African infantry held back on both flanks wheeled inward. Hasdrubal's cavalry routed the Roman horse, then struck the Roman rear.
  - Roman losses were about 67,500–80,000 killed or captured; Carthaginian losses about 5,700–8,000.
- **Mechanism:** A yielding centre draws the enemy's commitment inward while held-back wings close on the flanks and rear.
- **Needs:** An enemy committed to pushing the centre, flank forces that stay uncommitted until the hinge, and mobility superiority (the cavalry).
- **Counters:** Rome's own answers were:
  - The Fabian strategy: refuse the decisive battle.
  - Zama (202 BC): win the cavalry arm first. Scipio had Masinissa's horse.
  - Keep reserves and cover the flanks.
- **Fleet expression:** A static fort cannot "advance into a pocket", but the *player's fire* can.
  1. A central Bombard group engages, then slowly gives ground. The player's fire-control and re-tasks concentrate on the centre, and hidden centre batteries reveal themselves.
  2. At the hinge tick, two wing groups (raiders by sea and Skyfall bombers by air) close on the fort's flank and rear batteries, now out of the player's attention and possibly mis-tasked.
  3. Troops land behind the walls where the rear faces are weakest.
  - *Tell:* The centre retreats in good order while wing groups sit motionless at the fear edge.
  - *Counter:* Fabian hold-fire at the centre, wing-facing Overwatch, and killing the "cavalry" (air wing) early.
- **Tier:** T5. Builds from #6 (T2) and Feigned Flight (T4).

### 3.5 Hastings, 1066: feigned flight to break a shield wall
- **What happened:**
  - Harold's shield wall held Senlac ridge after a forced march from Stamford Bridge. Norman arrows shot uphill were largely stopped by shields.
  - A genuine Breton rout, with a rumour that William was dead, drew English pursuers off the hill, and they were cut down. William showed his face to rally his men.
  - William of Poitiers says the Normans then *feigned* flight twice, repeating the effect deliberately. Historians mostly accept this, though some suspect it was invented afterwards to excuse a real panic.
  - The pursuits thinned the housecarls, and fyrd militia filled the gaps.
- **Mechanism:** A real accident, recognised, is weaponised into a repeatable stratagem. Each pursuit trades the defender's discipline for exposure.
- **Needs:** A defender tempted to pursue, and attackers disciplined enough to turn around.
- **Counters:** Sun Tzu's first maxim: don't pursue a feigned flight. Keep the wall intact.
- **Fleet expression:** The defender's "pursuit" is *fire*: firing on a retreating group feels free, but it reveals batteries and burns cooldowns.
  1. A group takes damage.
  2. It "routs", with fore-aft motion away and nerve visibly broken.
  3. Hidden batteries fire on the easy targets and write Contacts.
  4. The group turns at a set cell and Reavers move on the new Contacts.
  - *Tell:* The rout is too orderly. The hulls keep spacing and don't scatter the way a real T1 rout does.
  - The Ships-doc motion grammar (fore-aft means nerve) makes this a readable forgery.
  - Also: the flagship *showing itself* to halt a real rout (William's helmet-off moment) is a legible resolve-anchor behaviour.
- **Tier:** T4 (Feigned Flight). Builds from Scatter and Run (T1) and into Kalka (T5). Note the historical accident: a real rout came first and the stratagem followed. That is exactly the "they get better" arc.

### 3.6 The Mongol feigned retreat, and the Mongol learning curve
- **What happened:**
  - Kalka River (31 May 1223): Jebe and Subutai's column of about 20,000 (traditional figure) drew a Rus'–Cuman coalition claimed at about 80,000 through a *nine-day* retreat that strung the pursuers out. At the Kalka the Mongols turned; the Cumans broke and fled, disordering the Rus', and the Mongols swept through the gap.
  - Liegnitz (1241): about 20,000 horse archers beat about 30,000 by harassment and demoralisation.
  - Battlefield control used signal flags, horns, and to a lesser degree signal arrows. The decimal organisation (units of 10, 100, 1,000 and 10,000) let sub-units execute a drill without new orders. The *nerge* great hunt was the peacetime drill for encirclement.
- **The learning curve (key for the Mystaeri arc):**
  - Early Mongol armies could not take walled cities.
  - The 1221–23 Jebe–Subutai expedition was effectively a *strategic reconnaissance in force*, 14 years before Batu's invasion of Rus' (1237–40).
  - The Mongols acquired siege craft by hiring and conscripting Chinese and Persian engineers. At Xiangyang (1273), two Muslim engineers (from Persia and Syria) built counterweight trebuchets that finally broke a 5-year siege.
  - The order was: raid, reconnoitre, hire the missing capability, conquer.
- **Mechanism:** A long feigned retreat turns the pursuer's cohesion and supply into liabilities. Organisation and signals let dispersed units act as one.
- **Needs:** Mobility superiority, a disciplined drill, and an overconfident pursuer.
- **Counters:** Don't pursue. Keep the coalition cohesive (the Cumans broke first). Fortify, since the steppe armies were weak against walls until they acquired engineers.
- **Fleet expression:** "Kalka" is the long form of Feigned Flight.
  - Over several game-hours, a fleet element yields sector after sector. The player follows with fire, re-tasks and domain switches, spending, revealing and turning the defence toward one arc.
  - At the hinge the element turns, and the rest of the fleet, which was never in the fear grid, arrives on the arc the player has abandoned.
  - The decimal-drill lesson maps to Coordination: late fleets have sub-groups that carry out their phase of a stratagem even after the flagship dies, because the plan was propagated before the Fight.
  - The engineer lesson: the siege lineages (Breacher, mining troops) should *arrive* later in the campaign as an acquired capability, not exist from board 1.
- **Tier:** Kalka is T5. The decimal drill is a T5 Coordination property. Engineer acquisition is a campaign-arc beat.

### 3.7 Viking escalation: from raid to invasion (787–878)
- **What happened:**
  1. 787/789: three ships at Portland; the reeve who met them was killed.
  2. 793: Lindisfarne. Monasteries were targeted for portable wealth, then the raiders left.
  3. The raids grew: 35 ships at Carhampton in 840.
  4. 850–51: first overwintering on Thanet, then Sheppey (854–55). The raiders stopped going home.
  5. 865: the Great Heathen Army, a coordinated host estimated from under 1,000 to over 5,000. It took horses from East Anglia (mobility ashore) and built fortified winter camps (Torksey, Repton).
  6. It conquered Northumbria, East Anglia and most of Mercia.
  7. 878: Alfred's victory at Edington, then the Treaty of Alfred and Guthrum and the Danelaw.
- **Mechanism:** The same people escalate in steps: opportunistic raids, larger raids, persistence (overwintering), a unified army with its own logistics, and finally settlement. Each step was enabled by what the earlier ones had learned about the defenders' weakness.
- **Counters:** Alfred's reforms: the burh system of fortified towns within a day's march of each other, a standing rotation of the fyrd, and ships. **Defence in depth made raids unprofitable.**
- **Fleet expression:** This is the single best real template for "the first are not organised, but they get better". The Mystaeri campaign can follow the same beats:
  - T1: individual raiders hit soft, portable targets (#12, #5).
  - T2: bigger raids that probe.
  - T3: persistence, meaning the fleet's presence and memory carry across sorties. This already exists as the within-battle ratchet.
  - T4–T5: a unified host with logistics (Quartermasters) and mobility ashore (troops that move inland).
  - T5–T6: a beachhead that becomes a "host" (#30).
  - Alfred's burhs are the player's counter-arc: layered strongpoints close enough to support each other.
- **Tier:** The whole ladder. Within a battle, sorties 1 to N could be a miniature of the same escalation.

### 3.8 Byzantine and medieval siege craft: investment, starvation, mining, and the sea
- **The real toolbox:**
  - **Investment:** encircle, cut off relief and supply. Caesar at Alesia (52 BC) built inner and outer lines of circumvallation and contravallation.
  - **Starving out:**
    - Rochester (1215): King John's engines failed against the keep, so he mined the south-east corner. The tunnel's timber props were fired with the fat of **forty pigs**, and the corner collapsed. The garrison still held out behind the keep's cross-wall; **starvation** ended it in late November after nearly two months. The rebuilt corner is round, because round towers resist mining better. The defender learned.
    - Château Gaillard (1203–04) was reduced by blockade, then mining and escalade.
  - **Mining and countermining:** tunnels under walls, props burned to collapse the wall. Defenders detected mining with bowls or barrels of water whose surface trembled (Johannes Grant at Constantinople, 1453, also used smoke, fire and Greek fire in countermines), then dug countermines to break in and fight underground.
  - **Getting around the sea barrier:**
    - Tyre (332 BC): Alexander built a mole (causeway) about 800 m to the island city over about seven months, fought off Tyrian fireships, then assaulted with ship-mounted rams once defecting Phoenician and Cypriot fleets gave him command of the sea.
    - Constantinople (1453): the chain boom closed the Golden Horn. On the night of 22 April, Mehmed II had **70–80 ships** hauled overland on greased rollers across the Galata ridge (about a mile) into the Horn, outflanking the boom and forcing the defenders to thin the land walls.
  - **Greek fire** (a defender weapon) broke the Arab naval sieges of 674–678 and 717–718.
  - The Byzantine *Strategikon* (c. 600) codified feigned retreats, ambushes and night attacks as doctrine.
- **Mechanism:** Walls beat assault, so the attacker changes the problem. He goes under the wall (mining), around it (overland ships, a mole), or through time (starvation).
- **Counters:** Countermining with water-bowl detection, round towers, stored provisions, depth (inner walls or a cross-wall), and a harbour chain.
- **Fleet expression:**
  - **Mining:** a troop or Breacher operation that runs across several sorties toward a specific wall section. A countdown holds in Contact between sorties, which fits the persistence boundary.
    - *Tell:* Dust and settling at the section: the water bowl.
    - *Counter:* Reinforce or countermine the section in Deploy.
    - It is deterministic, legible and slow, and it creates a real Deploy decision.
  - **Overland outflank:** the fleet discovers a boom or minefield through Contact and routes transports or light craft around it by a land or short-portage route. The Great Siege of Malta shows it too (3.19).
  - **Starvation:** see Actium; it is conditional.
- **Tier:** Mining is T3 (single) to T5 (combined with an assault timed to the collapse). The overland outflank is T4.

### 3.9 Red Cliffs, 208: fireships behind a false surrender
- **What happened:** Cao Cao's larger fleet, moored close together on the Yangtze, received a promised "defection" from Huang Gai. The defecting ships were fireships loaded with oil-soaked reeds, and a wind carried them in. The fire spread through the packed fleet and the camp, and Sun–Liu forces followed up.
- **Mechanism:** A false surrender (#34) delivers fire (S14) into a formation packed too densely (#35).
- **Needs:** A believable defection, the right wind, and a packed target.
- **Counters:** Disperse the formation, accept defectors only at a distance, and check the wind.
- **Fleet expression:** A "surrender" hull flies a white flag or a derelict silhouette. It shows as low-resolve: backing away, then drifting. It comes toward the harbour boom or a wooden structure, and the fleet's follow-up wave is timed to the fire.
  - *Counter:* Sink derelicts at range, and don't cluster wooden structures.
- **Tier:** T4.

### 3.10 Gravelines, 1588: fireships that burned nothing and won anyway
- **What happened:** On the night of 7–8 August (NS), the Armada lay anchored off Calais in its famous defensive crescent, waiting for Parma's army. Drake and Howard sent in **eight** fireships packed with combustibles. **None of the Spanish ships burned**, but ships cut their cables to escape, broke the crescent against Medina Sidonia's orders, and never re-formed or recovered their anchorage. The next day's battle of Gravelines was fought against a scattered fleet.
- **Mechanism:** The threat is the weapon. A fireship forces a choice between burning and breaking formation, and the formation was the fleet's whole defensive strength.
- **Needs:** An enemy that relies on a static formation, plus wind and tide toward him.
- **Counters:** Picket boats to tow fireships aside (the Spanish did deflect two), sea room, and dispersed anchoring.
- **Fleet expression:**
  - (a) *Fleet against fort:* a Sower or fireship drifts toward a wall or wooden structure. The player must either shoot it (spending fire-control, revealing a battery, pulling an AoR off its task) or let it burn. It is a forced dilemma: the "hurt" is the defender's disrupted stance, not the fire.
  - (b) *The lesson to the fleet:* anchored or holding formations, such as transports waiting to land, are vulnerable to exactly this. So late fleets hold dispersed and T1 fleets bunch.
- **Tier:** The fireship dilemma is T3–T4. Dispersed holding is a T3 Cognition property.

### 3.11 Lepanto, 1571: forward floating batteries, a flank game, and the reserve
- **What happened:**
  - The Holy League had 206 galleys and **6 galleasses**. The Ottomans had 211 galleys and 63 galliots.
  - The six Venetian galleasses, heavy gun platforms, were towed ahead of the Christian line. Their close-range fire disordered the Ottoman array at the moment of contact.
  - On the Christian left, Barbarigo hugged the shore to stop encirclement. The Ottomans (Sirocco) still slipped galleys into the shallow gap.
  - On the right, Uluç Ali's manoeuvre drew Doria south, opening a gap into the centre.
  - Santa Cruz's **reserve** plugged the gap twice: first on the left, then against Uluç Ali.
  - Result: about 117 Ottoman galleys captured and 83 sunk or destroyed. Christian dead about 7,500–10,000, Ottoman about 20,000–40,000.
- **Mechanism:** Disrupt the enemy formation *before* contact with forward heavy firepower. Use one wing's manoeuvre to open a gap. An uncommitted reserve decides where the gap appears.
- **Counters:** Screen the galleasses or go around them. Don't let a wing be drawn off. Keep your own reserve.
- **Fleet expression:**
  - A Leviathan or galleass-type heavy moves ahead of the main line to soak and disorder the defender's first fire (fire-control spent on the heavy).
  - A wing manoeuvre draws a battery's AoR off its arc (#15).
  - Most important for sophistication: **a held-back reserve that commits to whatever the Effect grid shows is the coldest opening**, perceived at the moment of commitment.
  - *Tell:* One group sits unmoving at the rear and never engages until something breaks.
  - *Counter:* Hidden batteries that stay silent until the reserve commits.
- **Tier:** The forward heavy is T3. Wing plus reserve is T5.

### 3.12 Jutland, 1916: bait squadrons, and the covered turn-away
- **What happened:**
  - Scheer planned to lure and destroy a detached part of the Grand Fleet. Hipper's five battlecruisers were the bait, about 50 miles ahead of the High Seas Fleet, with submarines pre-positioned.
  - Room 40 read the German signals, so Jellicoe sailed early.
  - Run to the South: Beatty engaged Hipper and lost *Indefatigable* and *Queen Mary*.
  - Run to the North: finding Scheer's battleships, Beatty turned and became the *counter-bait*, drawing both German forces onto Jellicoe.
  - Jellicoe deployed and **crossed the T** (about 18:15–18:30), with the Germans silhouetted against the sunset. Scheer escaped with a simultaneous **battle turn-away** (*Gefechtskehrtwendung*, 18:33), later repeated under cover of a destroyer torpedo attack and a battlecruiser charge.
  - Losses: British 14 ships (113,300 t), 6,094 dead. German 11 ships (62,300 t), 2,551 dead.
  - Beatty's flag signals repeatedly failed to reach the 5th Battle Squadron.
- **Mechanism:** Bait draws a detachment onto the main body, and bait can be counter-baited. An orderly, simultaneous withdrawal covered by a sacrificial screen escapes a trap.
- **Counters:** Signals intelligence. Know what is behind the bait. Keep formation discipline and signalling redundancy.
- **Fleet expression:**
  - (a) **Bait squadron:** a fast group engages at the edge of the player's defence, then runs along a path that pulls the player's fire and attention toward the arc where the main body will appear.
  - (b) **Covered turn-away:** when the fleet's LOS or Effect suddenly shows it has sailed into a scalding cell (the player "crossed its T" with a hidden battery reveal), every hull reverses on the same tick while screens and Sowers lay smoke and charge to cover.
    - *Tell:* A synchronised reversal. A T1 fleet instead scatters.
  - The signalling-failure lesson maps to Coordination: early multi-group fleets should mis-coordinate, with phases arriving late because propagation is slow. Late ones don't.
- **Tier:** The bait squadron is T4. The covered turn-away is T4, the orderly form of #36.

### 3.13 Trafalgar, 1805: breaking the line, and command by intent
- **What happened:**
  - Nelson had 27 ships of the line against Villeneuve's 33.
  - He rejected the rigid line-of-battle doctrine of the old Fighting Instructions (parallel lines, often indecisive). He attacked in two columns *perpendicular* to the enemy line: *Victory*'s column at the centre and Collingwood's at the rear, isolating the rear and centre.
  - The approach was bow-on under raking fire, accepted as a calculated risk given the allies' poorer gunnery. The allied van under Dumanoir took too long to turn back in the light wind.
  - Nelson's pre-battle memorandum ("the Nelson touch") gave every captain the *intent*, so they acted without signals.
  - Results: 18 allied ships lost (17 captured, 1 destroyed), no British losses. British 458 killed; allied about 4,400 killed and 7,000–8,000 captured. Nelson died, and the plan executed anyway.
- **Mechanism:** Concentrate overwhelming force on part of the enemy while the rest of his force *cannot reposition in time*. Shared intent replaces signals.
- **Counters:** Keep a mobile reserve able to turn (the van's failure), keep the line compact, and bring fire to bear on the approaching columns.
- **Fleet expression:** A fort's static batteries are the "van that can't turn". Their AoRs don't reposition mid-Fight except through the costly re-task.
  - The fleet concentrates two perpendicular columns on one wall sector, accepting losses on the approach, so that only the batteries covering that sector can respond. It overwhelms them before the player's re-tasks can arrive.
  - Command by intent maps to how the fleet handles a dead flagship: late fleets keep executing the propagated plan. This is a tension with the flagship-kill lever; see section 6.
  - *Tell:* Columns heading straight at a single sector, bow-on, ignoring fire.
  - *Counter:* Overlapping AoRs from adjacent sectors, a Chain or Splasher on the column axis, and Frost to slow the approach.
- **Tier:** Break the Line is T3. Command by intent is a T5 Coordination property.

### 3.14 Q-ships, 1915–1918: the smile with a knife, and why deceptions decay
- **What happened:**
  - Britain disguised warships as merchant tramps with hidden guns, sometimes with a "panic party" that abandoned ship theatrically. U-boats saved torpedoes by surfacing to sink small merchants with deck guns, and a surfaced U-boat was exactly what a Q-ship needed.
  - About **366 Q-ships** were used against **351 U-boats**. They sank **at least 11** (about 7% of U-boats lost to enemy action), damaged about 60, and **61 Q-ships were lost**.
  - The U-boats adapted by attacking submerged without warning, and Q-ship effectiveness collapsed. The deception had a half-life.
- **Mechanism:** Exploit the enemy's cost-saving rule (surface and use the gun on "harmless" targets) with a disguised threat.
- **Needs:** An enemy whose behaviour depends on judging targets by appearance.
- **Counters:** Change the rule and attack every target from safety. Also watch for tells: Q-ships were too well crewed and too steady.
- **Fleet expression:** The "Q-hull" of #10. More importantly, the Q-ship gives the ladder its most important dynamic, the **stratagem half-life**.
  - A deception works until the opponent learns its tell. Then it becomes a liability, since each Q-ship lost was a warship lost.
  - Late fleets therefore need stratagem *rotation*: if a stratagem's precondition fails (the player didn't bite on the Q-hull in earlier sorties), the fleet stops using it and switches (T6).
  - Reversed, the Q-ship also describes the *player's* hidden batteries. Late fleets treat every quiet sector as a possible Q (Cognition).
- **Tier:** The Q-hull is T3. Half-life rotation is T6.

### 3.15 Gallipoli and the Dardanelles, 1915: why a fleet alone cannot force a fortified narrows
- **The naval attempt (18 March 1915):**
  - The Allied battleships beat the outer forts at long range. But the minefields were covered by mobile howitzers that civilian minesweeping trawlers would not work under, and the inner forts covered the mines.
  - The night before, the Ottoman minelayer *Nusret* laid one fresh line of **20 mines**, about 100 yards apart and parallel to the shore, in Erenköy Bay, **exactly where the Allied ships had been observed turning** on earlier days.
  - *Bouvet* hit a mine at 13:54 and sank with 639 men. *Irresistible* (about 16:00) and *Ocean* (18:05) were mined and lost.
  - De Robeck concluded on 23 March that troops were required.
- **The landings (25 April):** At V Beach the collier *River Clyde*, fitted with sally ports, was run aground to land about 2,000 men, a Trojan-horse assault ship. It took heavy losses to machine guns at Sedd el Bahr.
- **The evacuation (December 1915 to January 1916):**
  - Brudenell White's plan used weeks of "silent stunts", periods of no firing, to condition the Ottomans to quiet trenches. On the last nights, drip rifles (water-timed triggers) kept up sporadic fire.
  - Commanders had feared up to 30,000 casualties. In the event **35,268 men**, 3,689 animals and 127 guns left Anzac and Suvla with **no deaths from enemy fire**.
- **Mechanisms:**
  - (1) Layered defence: mines stop ships, mobile guns stop sweepers, forts cover mines. The attacker needs combined arms.
  - (2) The defender exploited the attacker's *repeated observed pattern*.
  - (3) Conditioning by silence enabled the cicada-shell escape (#21).
- **Fleet expression:**
  - For the fleet, sweeper-before-battleship sequencing: Sowers or clearers work ahead of the Bombards, and the clearers are the soft target. This gives the player a Sweeper, Interdictor or Marksman lever.
  - The *Nusret* is the player's archetypal counter-play. Deterministic fleets repeat patterns, and the player mines or baits exactly where the fleet turns. **This is by design the player's core reward, so fleet patterns must be observable and exploitable.** Late fleets vary their turning points by seed, but deterministically.
  - The *River Clyde* is a Runner-type assault transport that grounds itself at the wall.
  - The evacuation is #21 with a #1-style conditioning lead-in.
- **Tier:** Sweeper sequencing is T3. The assault transport is T3. Conditioned evacuation is T4–T6.

### 3.16 Midway, 1942: stimulus tests, scouting, and staggered waves
- **What happened:**
  - Station HYPO (Rochefort) partly read JN-25b and suspected that "AF" meant Midway. Holmes suggested Midway send a plain-language message, by secure cable, reporting its water plant broken. Within about 24 hours the Japanese reported "AF is short of water", confirming the target.
  - Japanese reconnaissance failed. The *Tone*'s scout launched about 30 minutes late (it sighted US ships at 07:40, but carriers weren't confirmed until about 08:20). The Operation K flying-boat recon of Pearl Harbor was cancelled because US ships occupied French Frigate Shoals. The submarine picket line arrived late.
  - Nagumo, having ordered his reserve re-armed for land targets at 07:15, faced the dilemma of whether to launch against ships at once or re-arm again. He waited.
  - US torpedo squadrons attacked piecemeal and unescorted: VT-8 lost 15 of 15, VT-6 about 9–10 of 14, VT-3 10 of 12, with zero hits. But they pulled the Japanese combat air patrol down to sea level. At 10:25 SBD dive bombers arrived unopposed from altitude and wrecked three carriers in minutes.
  - The Aleutian operation (3 June) diverted Japanese strength.
- **Mechanisms:**
  - (1) Test a hypothesis by sending a stimulus and watching the reaction.
  - (2) Scouting depth decides who gets surprised.
  - (3) A dilemma between two target types, imposed on a fixed re-arming cycle.
  - (4) Staggered arrivals, accidental here: the first wave spends the defender's attention and the second hits the gap.
- **Counters:** Guard your channels (don't answer in a way that confirms the test). Scout early and redundantly. Keep an escort and CAP at more than one altitude.
- **Fleet expression:**
  - **The AF Ruse (T4):** the fleet has a hypothesis, "battery at cell X", from a coarse fear bearing. It sends a single ship across X's supposed arc at a precise tick and watches for a flash. That turns Effect into Contact.
  - **Scouting depth (T2–T3):** late fleets send Recon on multiple bearings before committing; T1 fleets don't scout.
  - **Nagumo's Dilemma (T5):** sea and air threats timed so a battery's domain-switch cooldown can't serve both.
  - **Staggered Waves (T3–T5):** the first wave draws fire-control and reveals, the second arrives at the hinge. At T1 the staggering is *accidental* (poor coordination); at T5 it is deliberate.
  - *Tell:* A small first wave that doesn't commit.
- **Tier:** T2 to T5 as noted.

### 3.17 D-Day and Operation Fortitude, 1944: the real attack disguised as the feint
- **What happened:**
  - *Fortitude South:* a notional First US Army Group (FUSAG) under Patton, the general the Germans rated most highly, "poised" at Pas-de-Calais. It was built from dummy landing craft, simulated radio traffic (Quicksilver) and double agents, especially Garbo's fictional network of 27 sub-agents.
  - *Fortitude North:* a notional Fourth Army in Scotland threatening Norway, with fake radio (Skye, from 22 March 1944) and planted football scores and wedding notices. The Germans kept 13 divisions in Norway.
  - On the night itself: Operation Taxable and Glimmer aircraft dropped Window (chaff) in precise, slowly advancing patterns to paint phantom invasion fleets on radar toward Cap d'Antifer and Boulogne, and Titanic dropped dummy paratroopers.
  - **Crucially, the deception continued after the landing.** It persuaded the Germans that Normandy was itself the feint, keeping the 15th Army at Calais for weeks, possibly into September.
- **Mechanism:** Build a complete, consistent false picture across every channel the enemy watches, including a phantom main effort. The pinnacle is making the real attack look like the diversion.
- **Needs:** Control of the enemy's information channels (air superiority denied German reconnaissance), a credible story (Patton), and consistency.
- **Counters:** Independent reconnaissance, and scepticism about too-convenient intelligence.
- **Fleet expression (T6):**
  - Over a battle, the fleet builds a consistent phantom main effort against one sector. Mimic silhouettes, air phantoms, demonstrations and mining "tells" there (#8, #29) persist across sorties.
  - When the real landing comes elsewhere, the phantom effort *keeps signalling a second, larger landing*, so the player keeps AoRs committed to the phantom sector.
  - *Legibility:* phantoms must have a counter-tell. They vanish under Flare or Spotter light, leave no wrecks, and their "radio" (propagation lines) goes nowhere. Denying them the player's Reveal (Jamming) is how they stay credible.
  - Fortitude also gives the design rule for #33: deceive through the channel the enemy trusts most.
- **Tier:** T6 (Fortitude).

### 3.18 Reconnaissance in force, and Dieppe, 1942
- **Doctrine:** US joint doctrine defines reconnaissance in force as a deliberate combat operation to discover or test the enemy's strength, dispositions and reactions, or to obtain other information. It differs from a raid: the information *is* the objective.
- **Dieppe (19 August 1942):**
  - About 10,500 personnel, mostly the 2nd Canadian Division, with 237 ships and landing craft, 74 air squadrons and 29 Churchill tanks. The aim was to test whether a defended port could be seized.
  - Surprise was lost to a chance clash with a German convoy. The preliminary heavy bombardment was cancelled. The tanks bogged on the shingle beach.
  - Of about 6,086 landed, over 3,600 became casualties. The Canadians lost 907 killed, 2,460 wounded and 1,946 captured, about 68%.
- **Lessons carried to D-Day:** Don't assault a defended port frontally (hence the Mulberry artificial harbours). Use specialist armour, heavy preliminary bombardment and integrated air support.
- **Other examples:** Jebe and Subutai's 1221–23 ride (3.6) and the Mongol 1274 attack on Japan (3.20) worked as reconnaissance in force before larger efforts.
- **Mechanism:** Pay a measured price for information that shapes the decisive effort.
- **Counters:**
  - Reveal as little as possible to a probe: hold fire, let it hit a decoy, accept acceptable damage.
  - Or annihilate it so the information never gets home.
- **Fleet expression:** The sortie structure already *is* reconnaissance in force at the battle scale. The explicit stratagem is a moderate first sortie that attacks broadly, logs every reveal as Contact, and *retreats early on purpose* (#36) to carry the knowledge home.
  - The counter is exactly the Fleet Memory rule "kill the knower before it radios": sink the probing Recon before propagation.
  - *Tell:* The fleet retreats with resolve still high.
- **Tier:** T2.

### 3.19 Great Siege of Malta, 1565: the wrong first objective, the hidden battery, the fear of relief
- **What happened:**
  - About 6,100 defenders (about 600 Knights) faced about 28,500–40,000 Ottomans.
  - The attackers first reduced the small outlying Fort St Elmo. It held about a month (27 May to 23 June) and cost the Ottomans at least 6,000 men, including half their Janissaries. The corsair Dragut, the most experienced commander, was killed directing fire from a trench.
  - The Ottomans carried about 100 small boats overland across Mount Sciberras into the Grand Harbour to avoid Fort St Angelo's guns.
  - On 15 July, a **hidden sea-level battery** at St Angelo's foot fired two salvos and sank all but one of the boats attacking Senglea, killing or drowning over 800.
  - On 7 August, a cavalry sally from Mdina hit the undefended Ottoman field hospital. The attackers, **believing relief had arrived**, abandoned an assault that was about to succeed.
  - The real relief (about 8,000 men, 7 September) routed them. Ottoman dead: 25,000–35,000.
- **Mechanisms:** Sunk-cost fixation on the first target. A hidden battery holding fire until the decisive moment. Resolve broken by a perceived rear threat.
- **Fleet expression:**
  - T1 fleets **fixate on the first contacted structure** and pay heavily for it (the St Elmo error). The player can build "St Elmos": sacrificial outworks that eat the naive fleet's time.
  - Late fleets bypass outworks.
  - The overland portage is the 1453 move again.
  - The hidden sea-level battery is the player's hold-fire at its most lethal.
  - The Mdina raid shows a *player* lever over fleet resolve: a threat to the fleet's rear or support (Quartermasters) breaks nerve out of proportion to the damage. This supports the per-ship resolve network reading "progress and danger".
- **Tier:** First-Wall Fixation is T1 (an anti-pattern). Bypassing outworks is T3.

### 3.20 The Mongol invasions of Japan, 1274 and 1281: probe, wall, mass, coordination failure
- **What happened:**
  - **1274:** about 900 ships and about 28,000–30,000 troops took Tsushima and Iki, then landed at Hakata Bay. They fought one day with bombs and massed tactics against samurai single-combat norms, then re-embarked. A storm wrecked about 200 ships, and about 13,500 did not return. It functioned as a probe.
  - **Between the invasions:** the Kamakura shogunate built the **Genkō Bōrui**, a stone wall about 2 m high (commonly cited as about 20 km along Hakata Bay, 1276), staked the river mouths, and executed Kublai's envoys.
  - **1281:** two fleets. The Eastern Route had about 900 ships and 40,000 men; the Southern Route about 3,500 ships and 100,000 men (figures disputed). They failed to rendezvous on time, which was a coordination failure.
  - The Eastern fleet **could not land at the wall** and shifted to islands. Anchored for weeks, it suffered **Japanese small-boat night raids**. A typhoon (15 August) destroyed the combined fleet.
- **Mechanism:** The attacker's first expedition teaches the defender more than the attacker. The defender fortifies the observed landing ground. The attacker's second, larger expedition fails on coordination and on having to hold anchored off a defended shore.
- **Fleet expression:** This is the closest real analogue to Rivenkeep: a sea power against a walled shore, escalating across expeditions.
  - Beats for the Mystaeri arc:
    1. The first expeditions are probes that teach the Shorelanders.
    2. The Shorelanders' wall changes the attacker's plan. The fleet should visibly **re-route landings away from wall it has contacted**, a perceived rule.
    3. Multi-fleet operations **mis-time their rendezvous** at T3–T4 and synchronise only at T5.
    4. Anchored or holding fleets suffer night raids, which is the Gravelines lesson again.
  - The 1274 "shock weapons against unfamiliar norms" (bombs frightening horses) suggests that a new lineage's first appearance should *feel* disruptive before the player learns its tell.
- **Tier:** The whole arc. Rendezvous failure is T3, rendezvous success is T5.

### 3.21 The Sea Peoples and the Battle of the Delta, c. 1175 BC: the first shoremen's victory
- **What happened:** After a generation of raids and migrations that destroyed Ugarit, overran Cyprus and helped end the Hittite state, the Sea Peoples came to Egypt. Ramesses III *let* their ships into the Nile mouths, lined both banks with archers, and closed the exits with his own ships, which grappled and capsized them. It is recorded on the walls of Medinet Habu.
- **Mechanism:** The defender chooses the kill-zone and lets the attacker enter it. The attacker's disorganised mass, including families and migrants, cannot manoeuvre in channels.
- **Fleet expression:**
  - A mythic precedent for the Shorelanders' first victories.
  - T1 Mystaeri fleets **enter channels and estuaries naively**; the player's kill-zone channel is the Delta.
  - The later Cognition lesson is the same as Salamis: refuse the channel.
- **Tier:** T1 anti-pattern.

### 3.22 Running the batteries: New Orleans (1862) and Mobile Bay (1864)
- **What happened:**
  - **New Orleans (24 April 1862):** after a failed mortar bombardment, Farragut ran his fleet past Forts Jackson and St Philip at night through a cut in the river obstruction. He took damage but didn't stop to fight. With the forts bypassed, the city fell; the forts surrendered days later.
  - **Mobile Bay (5 August 1864):** the monitor *Tecumseh* struck a mine ("torpedo") and sank. The column faltered, and Farragut pushed through the minefield under Fort Morgan's guns into the bay.
- **Mechanism:** Don't fight the fort. Pass it at speed, in a column, at night or under smoke, and take the objective behind it. The fort's power is wasted if nothing stays in its arc.
- **Needs:** A gap in the obstacles, speed, and acceptance of losses in transit.
- **Counters:** Obstacles and mines that force the attacker to slow *inside* the kill-zone. Depth, meaning inner batteries covering the objective.
- **Fleet expression:** A fast raider or transport column runs through the arc of the outer batteries on a direct line to the harbour, beach or castle, never pausing, under Sower smoke or on a seeded "night" tick.
  - *Tell:* A column in single file at top speed.
  - *Counter:* Frost (slow), Chain across the channel, Interdictor on the column, and inner batteries.
- **Tier:** T2. It builds naturally from #5 swarm.

### 3.23 Drøbak Sound (Oscarsborg), 1940: the fort that held its fire
- **What happened:** On 9 April 1940 the heavy cruiser *Blücher* led the German squadron up the Oslofjord at night to seize Oslo by surprise. Colonel Birger Eriksen held fire until she was at close range. At 04:21, 40-year-old Krupp 28 cm guns and a torpedo battery of turn-of-the-century Whitehead torpedoes (on North Kaholmen) wrecked her, and she sank at about 06:22 with roughly 650–800 dead. The delay let the King, government, parliament and gold reserve escape Oslo.
- **Mechanism:** A silent fort is not an empty fort. Holding fire to point-blank against a capital ship that assumed surprise.
- **Fleet expression:** The *player's* hold-fire in its purest form. For the fleet, the lesson is its most important Cognition behaviour: **never lead with the capital ship into a silent narrows; send a probe first.**
  - T1–T2 fleets lead with their big hull and pay.
  - T3+ fleets send a cheap "brick" first (#17).
- **Tier:** T1 anti-pattern leads to T3 correction.

### 3.24 Zeebrugge, 1918: diversion, smoke, blockships
- **What happened:** On 23 April 1918, to bottle up the Bruges U-boat base, HMS *Vindictive* assaulted the Zeebrugge Mole as a diversion to draw the defenders' fire. A submarine packed with explosives blew the viaduct to stop reinforcement, and three concrete-filled blockships steamed for the canal mouth under smoke. A wind shift thinned the smoke. Two blockships were scuttled in the channel, only partly blocking it, and within days the Germans had dredged a way past.
- **Mechanism:** A sacrificial diversion plus smoke covers the real payload (the blockships). Cutting the defender's reinforcement is part of the plan.
- **Fleet expression:** A Provocateur or Bombard diversion, Sower smoke, and a "cork" payload aimed at a structural objective such as the harbour mouth, a gate or a wall gap.
  - The wind shift says environmental conditions should be deterministic by seed and visible (a wind vane), so smoke stratagems can fail legibly.
- **Tier:** T3–T4.

### 3.25 Port Arthur (1904) and Taranto (1940): the opening strike on a fleet in harbour
- **What happened:**
  - **Port Arthur:** on 8–9 February 1904, Japanese destroyers made a surprise night torpedo attack on the Russian squadron at anchor. Later blockship attempts to seal the harbour failed.
  - **Taranto:** on 11–12 November 1940, 21 Swordfish biplanes from HMS *Illustrious* attacked the Italian fleet in harbour. Three battleships were put out of action (*Conte di Cavour* never returned to service) for the loss of 2 aircraft.
- **Mechanism:** Strike before the defender's stance is set, at the highest-value static target, using the domain he has least prepared for (air, night).
- **Fleet expression:** An opening Skyfall strike in the first ticks of a sortie on the highest-value *contacted* structure, before the player's fire-control settles. It needs Contact from previous sorties, so it is never sortie 1 of a battle.
  - *Counter:* Air-domain AoRs loaded at Deploy.
  - *Tell:* Carriers holding at the horizon at sortie start.
- **Tier:** T3–T4.

### 3.26 Nelson's dictum and Sullivan's Island, 1776: why fleets don't simply brute-force forts
- **What happened:** On 28 June 1776, nine British warships under Parker bombarded the unfinished palmetto-log Fort Sullivan (about 30 guns) at Charleston. The spongy logs absorbed shot, three frigates grounded on a shoal, and the British fleet withdrew heavily damaged. The saying attributed to Nelson, "a ship's a fool to fight a fort", records the general pattern: land guns have a stable platform, protected magazines, heated shot and unsinkable mass.
- **Design use:** This is the real-world justification for the whole stratagem ladder. At equal guns the fort should win a straight exchange. So the fleet *must* use stratagem: probing, deception, bypassing, combined arms, mining. A frontal wall-bash is a T1 behaviour, and it should lose.

---

## 4. From crude to sophisticated: how real militaries progress

The cases above show one recurring arc across very different eras. It is the evidence base for "the first are not organized, but they get better", and it parallels Ender's Game, where the earlier and less advanced ships arrive first.

### 4.1 The six recurring stages

| Stage | What it looks like | Real evidence | Fleet tier |
|---|---|---|---|
| 1. **Opportunistic raid** | Small, independent, uncoordinated. Hits soft, portable value, then leaves. No scouting. Fixates on the first target. Routs when hurt. | Portland 787/789 and Lindisfarne 793; early Sea Peoples; solo U-boats in 1939; the *Blücher* leading into silence; St Elmo fixation | T1 |
| 2. **Probing and mapping** | Bigger raids, accepting losses for information. Reconnaissance in force. | Carhampton 840 (35 ships); Jebe and Subutai 1221–23; Mongols at Japan 1274; Dieppe 1942; the Dardanelles on 18 March | T2 |
| 3. **Massing without integration** | Numbers first, with coordination failures: late rendezvous, piecemeal waves, signals lost. | Mongols at Japan 1281 (two fleets out of step); Salamis (Persian mass fouled); Midway torpedo squadrons; Beatty's lost signals at Jutland | T3 (partly failing) |
| 4. **Integration by doctrine and signals** | Shared drill; roles specialised (sweepers, engineers, screens); a scouting line with a shadower who homes the pack. | Mongol decimal drill and signal flags; Dönitz's Rudeltaktik; the Great Heathen Army's horses and camps; Nelson's memorandum | T3–T4 |
| 5. **Combined arms and operational deception** | Multi-domain synchronisation; deception across every channel the enemy watches; the campaign won before the battle. | Agrippa at Actium; Fortitude plus Overlord; Mongol engineers at Xiangyang 1273; Cannae | T5 |
| 6. **Co-evolution** | Adapting to the defender's adaptation. Retiring stratagems the enemy has learned. Chaining. | Q-ship decay; Black May 1943 and Dönitz's withdrawal; the round towers after Rochester; the wall after 1274; WATU's "Raspberry" | T6 |

### 4.2 The Atlantic as a full worked example of co-evolution
- **1917:** Britain adopted convoy late, and losses to U-boats fell sharply. This is the defender's lesson.
- **1939–40:** Individual U-boats operated. From 1940 came the wolfpack, *Rudeltaktik*: a patrol line across the convoy route; the first boat to sight **shadows and radios**, and the others converge; night **surface** attacks from inside or astern of the convoy, where ASDIC (sonar) was blind.
- **Early 1942, the Second Happy Time:** the US coast was unconvoyed and lit, with ships silhouetted against city lights. About **609 ships** were sunk for **22 U-boats**. The defender had *forgotten* the 1917 lesson.
- **1942:** In Liverpool, the Western Approaches Tactical Unit (Captain Gilbert Roberts and a team of Wrens) wargamed convoy battles on the floor. It **deduced from the pattern of sinkings** that U-boats were attacking on the surface from inside the convoy, and invented the counter-manoeuvre "Raspberry". This is exactly Jack's vision #2 on the defender's side: recognise the strategy, then counter it.
- **1943:** Escort groups, escort carriers, very-long-range aircraft closing the air gap, radar, HF/DF (direction-finding on the *shadower's radio reports*, which made the propagation node the weak point), Hedgehog and Ultra.
  - March 1943, the U-boat peak: about 120 ships sunk for 15 U-boats.
  - May 1943, Black May: **43 U-boats lost (about 25% of the operational force)** for 58 merchant ships (34 in the Atlantic).
  - On 24 May Dönitz withdrew the boats. The attacker retired the stratagem the defender had solved.

**Design reading:**
- The wolfpack is the fleet's T3 **Patrol Line and Shadower**.
- HF/DF is the player's existing "kill the knower before it radios".
- WATU is the player's own play pattern.
- Black May is what the player's mastery should feel like. It also shows that the *attacker* then has to change, which is the T6 rotation.

### 4.3 Amphibious doctrine: failure to capstone
Gallipoli (1915) failed on combined arms, and the naval attempt failed on layered defence. Between the wars, the US Marine Corps studied Gallipoli and produced the *Tentative Manual for Landing Operations* (1934). Dieppe (1942) was the paid-for probe. Then came Torch, Sicily and Salerno. D-Day (1944) combined all the lessons: artificial harbours instead of port assault, specialist armour, heavy preliminary fire, air superiority, and Fortitude.

It took about 30 years, several catastrophes and a doctrine written from the failures. That is the pace at which the Mystaeri should become sophisticated across the campaign.

### 4.4 Principles for the Mystaeri arc, drawn from the evidence
1. **Each stage is born from the failure of the one before.** Hastings' feigned flight came from a real rout, the wolfpack from Dönitz's WWI experience, D-Day from Dieppe. Each new stratagem can be introduced as the fleet's lesson from the previous era's defeat. That gives a natural hook for the tales, where each fleet-age is a story.
2. **Early is uncoordinated, not just weaker.** The Ender's Game feel comes from *coordination and information* growing, not from hit points. This matches the Ships-doc rule that difficulty is Cognition and Coordination.
3. **The defender learns too, and the attacker's sophistication is partly a response.** The wall of 1276 re-routed 1281. The round tower answered the mine. Stratagems at higher tiers should be answers to the player's own habitual counters to lower tiers. For example, #16 "let it go" is the answer to a player who rebuilds killed guns somewhere unknown.
4. **Deceptions have a half-life.** Stratagems retire once countered (Q-ships), and late fleets must rotate and chain.
5. **Sophistication needs information first.** No fleet can feint against a battery it hasn't located. The information ladder (0.3) is historically honest.
6. **Numbers without integration fail.** The two fleets of 1281, the Persian mass at Salamis and Midway's piecemeal waves show that a *larger* T3 fleet can be *easier* than a smaller T5 one. That supports "smarter, not tougher".

---

## 5. Candidate stratagem ladder (input for design, not a decision)

This ladder has about 55 fleet stratagems in six overlapping periods. It meets Jack's ask of 6–8 or more per period, with simple ones building into complex ones. The names are working labels; in-world names would come from the tales.

"Src" is the source entry in this corpus. The information column shows what the fleet must have perceived, following 0.3.

### T1: First Contact (the unorganized raiders). No shared plan, no memory needed.
| # | Working name | Src | Behaviour (one line) | Player counter | Builds into |
|---|---|---|---|---|---|
| 1.1 | Loot the Burning House | #5, Vikings | Any hull that sees a breach or a newly cold cell pours in | Ghost or hidden breach | Run the Batteries, Wolfpack, Cannae |
| 1.2 | Pilfer the Goat | #12, Lindisfarne | Raiders fire at whatever enters LOS, never deviating | Keep small assets off the paths | Beauty Trap |
| 1.3 | Beat the Grass (crude) | #13 | Advance until something fires | Hold fire | Beat the Grass (aimed), AF Ruse |
| 1.4 | Hang at the Fringe | #4 | Loiter in cold cells, drift in when fire slackens | Don't spend on fringes | Cadence Strike, Deceive the Heavens |
| 1.5 | Sacrificial Van | #11 | Cheapest hulls lead into the fire | Back-line targeting | Plum for the Peach, Break the Line |
| 1.6 | First-Wall Fixation (anti-pattern) | Malta St Elmo | Commits to the first contacted structure and grinds it | Sacrificial outworks | Befriend the Far, Strike the Near |
| 1.7 | Straggling Stream (anti-pattern) | Midway, 1281 | Groups arrive piecemeal | Defeat in detail | Staggered Waves, Nagumo's Dilemma |
| 1.8 | Scatter and Run | #36 | Resolve breaks and every hull flees alone | Golden bridge, or pursue | Covered Turn-Away, Feigned Flight, Cicada Shell |
| 1.9 | Blind Channel Entry (anti-pattern) | Delta, Salamis, *Blücher* | Enters narrows and channels, big hull first | Kill-zone channel, hold fire | Brick First, Chokepoint Refusal |

### T2: Probing Fleets. LOS and simple roles.
| # | Working name | Src | Behaviour | Counter | Builds from / into |
|---|---|---|---|---|---|
| 2.1 | Sound East, Strike West | #6 | Demonstration on A, landing on B at t+Δ | Don't re-task to noise | From 1.3; into 4.2, 6.3 |
| 2.2 | Toss a Brick | #17, Drøbak | A cheap hull enters the best gun's arc to draw the expensive shot | Price targets | From 1.3; into 4.10 |
| 2.3 | Muddy the Water | #20 | Smoke plus simultaneous multi-bearing arrivals | Flare, pre-set AoRs, Saturation | Into 3.10 |
| 2.4 | Befriend the Far, Strike the Near | #23 | Stay out of distant arcs and reduce one sector | Overlapping AoRs | From 1.6; into 3.6, 5.3 |
| 2.5 | Plum for the Peach | #11 | Bulwark screen, with transports in its cold shadow | Piercer, back-line targeting | From 1.5; into 3.6, 5.4 |
| 2.6 | Reconnaissance in Force | Dieppe, Kalka ride | A moderate sortie that retreats early with Contacts | Kill the knower, reveal little | Into 3.5, 4.10 |
| 2.7 | Run the Batteries | New Orleans, Mobile | A fast column straight past outer arcs to the objective | Frost, Chain, inner batteries | From 1.1; into 5.1 |
| 2.8 | Watch It Burn | #9 | Stand off while a fire or hazard degrades the fort | Fight the fire, or fake one | From 1.4 |
| 2.9 | Scout Before Committing | Midway | Recon on several bearings before the main body moves | Sink scouts early | Into 3.5 |

### T3: Ordered Squadrons. The Contact ledger and two-group plans.
| # | Working name | Src | Behaviour | Counter | Builds from / into |
|---|---|---|---|---|---|
| 3.1 | Besiege Wei | #2 | Threaten a castle or breach when the fleet's transports are under fire | Reserve, refuse the hollow threat | Into 5.5 |
| 3.2 | Lure the Tiger | #15 | Show air to force a domain switch, then strike by sea (or the reverse) | Don't switch on display | Into 5.5 |
| 3.3 | Q-Hull | #10, Q-ships | A soft-looking hull unmasks guns at close range | Treat by capability; read the tell under Flare | Into 6.7 (half-life) |
| 3.4 | False Blossoms | #29 | Mimics and phantoms inflate a flank | Reveal the phantoms | Into 6.3 |
| 3.5 | Patrol Line and Shadower (Wolfpack) | Atlantic | A search line; the finder shadows and propagates; the others converge | Kill the shadower before it propagates | From 2.6, 2.9; into 5.1 |
| 3.6 | Break the Line | Trafalgar | Two perpendicular columns on one sector | Overlapping arcs, Chain, Frost | From 2.4, 2.5; into 5.4 |
| 3.7 | The Treasure Ship | #31 | A tempting prize parades to break hold-fire | Discipline | From 1.2 |
| 3.8 | Make an Example | #26 | The first gun to speak is destroyed overwhelmingly | Don't learn the lesson | Into 6.2 |
| 3.9 | The Sap (mining) | Rochester, 1453 | A multi-sortie mine toward a wall section; dust tell | Countermine or reinforce in Deploy | Into 5.8 |
| 3.10 | Fireship Dilemma | Gravelines, Red Cliffs | A drifting burner forces shoot-or-burn | Picket fire at range | From 2.3; into 4.9 |
| 3.11 | Corpse Cover | #14, Zeebrugge | Wrecks used as occluders or blockships; field promotion | Clear wrecks | |
| 3.12 | Chokepoint Refusal and Brick First (Cognition) | Salamis, Drøbak | Spread out on approach; probe silent narrows first | Punish the probe anyway | From 1.9 |

### T4: Cunning Fleets. The fleet models the defender's reactions from earlier sorties.
| # | Working name | Src | Behaviour | Counter | Builds from / into |
|---|---|---|---|---|---|
| 4.1 | Something from Nothing | #7, Yongqiu | Repeat a harmless approach until ignored, then make it real | Cheap verification each time | Into 6.1 |
| 4.2 | Open Roads, Hidden March | #8 | A credible sustained siege at A masks an occluded approach to B | Ask what A can't achieve alone | From 2.1; into 6.3 |
| 4.3 | Feigned Flight | Hastings, Salamis | A too-orderly "rout" draws pursuit fire, then turns on the new Contacts | Don't pursue a feigned flight | From 1.8; into 5.2 |
| 4.4 | Remove the Ladder | #28 | Induce a costly irreversible verb, then hit where it's wrong | Don't spend on invitation | Into 6.5 |
| 4.5 | Bait Squadron | Jutland | A fast group pulls attention toward the arc of the main body's arrival | Know what's behind the bait | Into 5.2 |
| 4.6 | Covered Turn-Away | Jutland | A synchronised reversal under a smoke and screen charge | Pursue the screen, not the smoke | From 1.8 |
| 4.7 | Cicada Shell | #21, Gallipoli | Withdraw leaving decoys that keep drawing fire | Probe the shell | From 1.8 |
| 4.8 | Let It Go to Catch It | #16 | Spare a known gun so the player won't relocate it | Relocate anyway | |
| 4.9 | Wounded Derelict | #34, Red Cliffs | A "crippled" hull drifts in and detonates or lands troops | Sink derelicts at range; drift against the wind is the tell | From 3.10 |
| 4.10 | The AF Ruse | Midway | A stimulus test across a suspected arc at a precise tick | Hold fire on tests | From 2.2, 2.6; into 6.4 |
| 4.11 | Borrow the Road | #24 | A transit wave spares X going in and strikes X on the way out | Camouflage | |
| 4.12 | Remove the Firewood | #19, Actium | Hit magazines and repair capacity, not guns | Protect sustainment | Into 5.8 |
| 4.13 | Cadence Strike | #4 refined | Assault timed to observed reload windows | Stagger your fire | From 1.4 |
| 4.14 | Borrowed Knife | #3 | Currents or wind or friendly splash do the damage | Watch the environment | Conditional |

### T5: Grand Designs. Multi-group and multi-domain, synchronised through the flagship.
| # | Working name | Src | Behaviour | Counter | Builds from / into |
|---|---|---|---|---|---|
| 5.1 | Cannae | Cannae | The centre yields while sea and air wings close on flank and rear batteries | Fabian hold-fire, wing Overwatch, kill the air wing | From 1.1, 2.1, 4.3 |
| 5.2 | Kalka | Mongols | A long multi-sector feigned retreat turns the defence; the unseen main body hits the abandoned arc | Don't follow | From 4.3, 4.5 |
| 5.3 | Catch the King | #18 | Converge on the inferred enabling tower (eyes or magazine) | Camouflage, ghosts, redundancy | From 2.4 |
| 5.4 | Galleass and Reserve | Lepanto | A forward heavy disrupts, a wing draws off, the reserve commits to the coldest gap | Hold hidden guns until the reserve commits | From 3.6 |
| 5.5 | Nagumo's Dilemma | Midway | Sea and air timed against domain-switch cooldowns | Split domains at Deploy | From 3.1, 3.2 |
| 5.6 | Swap the Beams | #25 | Decoy flagship; roles swapped under the same silhouette | Read behaviour, not the icon | Into 6.4 |
| 5.7 | Guest Becomes Host | #30, Repton, Tyre | Troops dig in inside the perimeter | Evict early | Conditional (troop clearing) |
| 5.8 | Sap and Storm | Rochester, 1453 | Assault timed to a mine collapse | Countermine | From 3.9, 4.12 |
| 5.9 | The Empty Fleet | #32 | A weak group advances with perfect confidence | Probe it | |
| 5.10 | Agrippa's Strangulation | Actium | Interdict sustainment, wait, strike the weakened fort | Break out, protect supply | From 4.12; conditional |
| 5.11 | Command by Intent (Coordination) | Trafalgar, Mongol drill | Phases execute even after the flag dies | Kill the flag before the plan propagates | |

### T6: Campaign Chains. Several sorties, with rotation when countered.
| # | Working name | Src | Behaviour | Counter | Builds from |
|---|---|---|---|---|---|
| 6.1 | Deceive the Heavens | #1 | A multi-sortie conditioned routine becomes the attack | Audit the routine | 1.4, 4.1 |
| 6.2 | Feign Madness | #27 | A sophisticated fleet imitates T1 blundering to invite T1 answers | Judge capability, not display | 3.8, the whole T1 set |
| 6.3 | Fortitude | Fortitude | A phantom main effort persists after the real landing | Reveal, independent recon | 2.1, 3.4, 4.2 |
| 6.4 | The Double Agent | #33, Garbo | Behaves differently under the player's Reveal; a false tell with a counter-tell | Cross-check channels | 4.10, 5.6 |
| 6.5 | Chain Stratagems | #35 | A branching plan where each counter selects the next link | Break the first link | Any |
| 6.6 | Raid, Overwinter, Great Army | Vikings, Japan | Within one battle, sorties escalate from raid to probe to host | Alfred's burhs: depth | The whole ladder |
| 6.7 | Half-Life Rotation | Q-ships, Black May | Retire any stratagem whose precondition failed in earlier sorties and switch | Keep countering | 3.3 and all others |

### 5.1 Example build-chains (simple to complex)
- **The probe chain:** Beat the Grass (1.3), then Toss a Brick (2.2), then the AF Ruse (4.10), then the Double Agent (6.4).
- **The feint chain:** Sound East (2.1), then Open Roads (4.2), then Fortitude (6.3).
- **The lure chain:** Scatter and Run (1.8), then Feigned Flight (4.3), then Kalka (5.2), then Feign Madness (6.2).
- **The mass chain:** Loot the Burning House (1.1), then Run the Batteries (2.7), then Wolfpack (3.5), then Cannae (5.1).
- **The screen chain:** Sacrificial Van (1.5), then Plum for the Peach (2.5), then Break the Line (3.6), then Galleass and Reserve (5.4).
- **The patience chain:** Hang at the Fringe (1.4), then Cadence Strike (4.13), then Deceive the Heavens (6.1).
- **The siege chain:** First-Wall Fixation (1.6), then The Sap (3.9), then Remove the Firewood (4.12), then Sap and Storm (5.8).
- **The coordination chain:** Straggling Stream (1.7), then Scout Before Committing (2.9), then Staggered Waves, then Nagumo's Dilemma (5.5), then Chain Stratagems (6.5).

---

## 6. Design conflicts and open questions surfaced by the research

1. **Troops are cleared at every sortie end, but beachheads persist in history.** #30, 5.7 and the Viking camps need either a within-sortie form only, or an explicit "entrenched beachhead" exception.
2. **The stalemate valve works against blockade and waiting stratagems.** Actium, #4 at campaign scale and #9 would bleed the fleet's own resolve. Either measurable defender degradation counts as progress, or these stay tactical.
3. **Static cannons can't be "lured" physically.** Luring (#15, Hastings, Cannae, Kalka) must map onto the defender's *stance*: fire-control, AoR re-task, domain loaded, hidden or revealed. That works, but it means the costly verbs are what the fleet fishes for. They must be visible to the fleet (it can see where fire goes), and the player must be able to see that they are being fished.
4. **Friendly fire and currents.** #3 is only real if Splasher can hurt the player's own walls, or the sea has seeded currents and wind. The Zeebrugge wind shift argues for a visible, deterministic weather and wind state in any case.
5. **No defender sustainment means firewood stratagems are inert.** #19, Actium and starvation need magazines, repair capacity or a consumable to target.
6. **Command by intent versus the flagship-kill lever.** Trafalgar and the Mongol drill say late fleets degrade gracefully when decapitated, while Fleet Memory makes the flagship kill a major lever. One resolution is that the plan *already propagated* before the Fight continues, but no *new* adaptation happens. The lever then shifts from "stop the plan" to "freeze the fleet's learning", which is still legible.
7. **False tells versus the legibility law.** #33 and 6.4 turn the player's pattern-reading against them. That is only fair if every false tell has a counter-tell: the phantom vanishes under Flare, the derelict drifts against the wind, the fake rout keeps its spacing.
8. **Exploitable repetition is a feature.** The *Nusret* lesson means deterministic fleets repeat observable patterns, and punishing them is the player's reward. Late tiers should vary patterns *by seed*, still deterministically, rather than removing them.
9. **Hinge ticks and the order ramp-down.** Almost every T2+ stratagem has a hinge tick where the defender's action or silence picks the branch. Stamping orders in sim ticks, with the 1/18 ramp-down, makes "one second earlier or later" a considered choice. Worth confirming: branch decisions read the order's *stamped tick*, never when the player clicked.

---

## 7. Real numbers index (for Jack's law)

| Case | Figure | Possible design use |
|---|---|---|
| Salamis | about 371–378 against 600–800 triremes | Numbers are useless in narrows; roughly a 2:1 mass defeated |
| Cannae | about 50k against 86k; Roman losses 67.5–80k, Carthaginian 5.7–8k | Envelopment kill ratio of about 10:1 when it works |
| Kalka | A 9-day feigned retreat; about 20k against a claimed 80k | A long lure: phases lasting many game-hours |
| Vikings | 787/793 first raids, 850 overwintering, 865 Great Army, 878 settlement | About 90 years from raid to settlement: a campaign-arc pacing model |
| Rochester | 40 pigs; about 2 months; starvation ended it | Mining is decisive against walls but not the whole answer |
| 1453 | 70–80 ships portaged about a mile in one night | Outflanking a boom |
| Gravelines | 8 fireships; 0 ships burned; formation broken for good | The threat does the work |
| Lepanto | 6 galleasses disrupted a line of about 211 galleys | Small heavy forward elements have outsized disruptive effect |
| Trafalgar | 27 against 33; 18 allied ships lost, 0 British | Concentration against a van that can't turn |
| Jutland | Bait 50 miles ahead; losses 14 against 11 ships | Bait and counter-bait |
| Q-ships | 366 ships; 11 or more kills (about 7% of U-boats lost to enemy action); 61 lost | A deception's half-life, and its cost |
| Dardanelles | 20 mines in one line sank or crippled 3 battleships | Exploiting a repeated pattern |
| Gallipoli evacuation | 35,268 men; 0 killed by enemy fire; 30,000 casualties feared | Conditioning by silence |
| Atlantic 1942 | 609 ships for 22 U-boats | An undefended, lit shore; the naive defender |
| Atlantic, May 1943 | 43 U-boats (about 25% of the operational force) for 58 merchants | Mastery reverses the exchange; the attacker withdraws |
| Midway | Torpedo squadrons lost 34 of 41 planes with 0 hits, then SBDs hit 3 carriers in minutes | Staggered waves; the first wave draws the defence |
| Dieppe | 68% Canadian casualties | The price of reconnaissance in force |
| Malta | St Elmo held about 1 month and cost 6,000 or more; 2 salvos killed 800 or more | Outwork attrition; a hidden battery |
| Mongols at Japan | 900 ships (1274); 900 plus 3,500 (1281); wall about 2 m high | A probe, then fortification, then a mass that fails at the wall |
| Oscarsborg | 40-year-old guns sank a new heavy cruiser | A silent fort is not an empty fort |
| Taranto | 21 aircraft, 2 lost, 3 battleships disabled | An opening air strike on static targets |
| Fortitude | 13 divisions held in Norway; the 15th Army held at Calais for weeks after D-Day | A phantom main effort outlasting the real one |

---

## Sources

- Thirty-Six Stratagems: https://en.wikipedia.org/wiki/Thirty-Six_Stratagems
- Salamis: https://en.wikipedia.org/wiki/Battle_of_Salamis
- Actium: https://en.wikipedia.org/wiki/Battle_of_Actium
- Cannae: https://en.wikipedia.org/wiki/Battle_of_Cannae
- Hastings: https://en.wikipedia.org/wiki/Battle_of_Hastings
- Kalka: https://en.wikipedia.org/wiki/Battle_of_the_Kalka_River
- Mongol military tactics: https://en.wikipedia.org/wiki/Mongol_military_tactics_and_organization
- Great Heathen Army: https://en.wikipedia.org/wiki/Great_Heathen_Army
- Rochester 1215: https://www.exploring-castles.com/uk/england/rochester_castle/ and https://castlestudiestrust.org/blog/2020/05/22/kings-barons-miners-and-inedible-pigs-the-great-siege-of-rochester-in-1215-now-on-video/
- Constantinople 1453, Johannes Grant and the overland ships: https://en.wikipedia.org/wiki/Johannes_Grant, https://en.wikipedia.org/wiki/Fall_of_Constantinople and https://en.wikipedia.org/wiki/Golden_Horn
- Gravelines: https://www.rmg.co.uk/stories/topics/spanish-armada-history-causes-timeline and https://en.wikipedia.org/wiki/Spanish_Armada
- Lepanto: https://en.wikipedia.org/wiki/Battle_of_Lepanto
- Trafalgar: https://en.wikipedia.org/wiki/Battle_of_Trafalgar
- Jutland: https://en.wikipedia.org/wiki/Battle_of_Jutland
- Q-ships: https://www.westernfrontassociation.com/world-war-i-articles/2021/july/pantomime-at-sea-q-ships-in-the-first-world-war/ and https://en.wikipedia.org/wiki/U-boat_campaign
- Dardanelles naval operations: https://en.wikipedia.org/wiki/Naval_operations_in_the_Dardanelles_campaign
- Gallipoli evacuation: https://www.awm.gov.au/articles/encyclopedia/gallipoli/drip_rifle and https://www.anzac100.initiatives.qld.gov.au/remember/evacuation-of-gallipoli/index.aspx
- Wolfpacks and Black May: https://en.wikipedia.org/wiki/Wolfpack_(naval_tactic), https://en.wikipedia.org/wiki/Black_May_(World_War_II) and https://www.usni.org/magazines/naval-history-magazine/2018/april/turning-point-atlantic
- Second Happy Time: https://en.wikipedia.org/wiki/Second_Happy_Time
- Midway: https://en.wikipedia.org/wiki/Battle_of_Midway
- Operation Fortitude: https://en.wikipedia.org/wiki/Operation_Fortitude
- Dieppe Raid: https://en.wikipedia.org/wiki/Dieppe_Raid
- Great Siege of Malta: https://en.wikipedia.org/wiki/Great_Siege_of_Malta
- Mongol invasions of Japan: https://en.wikipedia.org/wiki/Mongol_invasions_of_Japan
- Battle of the Delta: https://en.wikipedia.org/wiki/Battle_of_the_Delta
- Drøbak Sound: https://en.wikipedia.org/wiki/Battle_of_Drøbak_Sound
- From general knowledge, not fetched this session: Sun Tzu (Giles translation, 1910, public domain); Red Cliffs; Tyre; Zeebrugge; Port Arthur; Taranto; Sullivan's Island; New Orleans and Mobile Bay; WATU and "Raspberry"; the 1934 USMC *Tentative Manual for Landing Operations*; the Byzantine *Strategikon*.
