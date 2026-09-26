# RIVENKEEP — STORY BIBLE & MYTHCRAFT GUIDE

*Research for the rewrite of the Legend of Rivenkeep. Compiled 2026-09-25. Nothing in this file changes the simulation; every story surface proposed here is cosmetic and sits off the sim path.*

**Canon conventions used throughout (Jack's rulings):**
- The enemy people are the **Mystaeri**. Never "Mystborn", which was dropped as trademarked (journal 2026-05-07). Jack's message used "Mystborn" out of habit; this file corrects it everywhere.
- The defenders were the **Shorelanders**, reborn as the **Rivenmen**. Jack wrote "shore men" informally. That spelling is noted under naming (B7) as a possible Mystaeri name *for* them, but it is not canon.
- Rhyna's husband is **Halvard** (Old Norse *Hallvarðr*: *hallr* "rock, stone" + *varðr* "guardian", so "rock-guardian"). He is **Elder Halvard** and she is **Elderess Rhyna**. They are Aetherbonded, the tales always name them together, and they always act together. A real-world note: St. Hallvard is the patron saint of Oslo, and the name is common in Norway. That association is harmless.
- "Ender's Game" is the reference Jack meant ("Endor's game"): the less advanced ships are sent first.

---

## READ THIS FIRST — THE TEN FINDINGS THAT MATTER MOST

1. **The story's spine is already in the source, but nobody has stated it.** The **Aetherbond** (two Shorelanders made one) and the **Ael'thar** (two peoples made one front, "harm to one was harm to both") are the same idea. One people perfected it inside marriage. The other offered it across a border. The first people did not recognise the gift. Rhyna and Halvard are therefore the living image of the bond the Shorelanders refused. This is why the husband matters, and it is the thematic key to the whole rewrite (B8).
2. **The Ael'thar murder is a crime against guest-right** in the strict Homeric sense of *xenia*. A kneeling suppliant came with a gift and was killed by his host. The Odyssey treats this as the gravest of wrongs, the kind that brings down the wrath of the powers. The legend should name the crime in those terms (B2.2).
3. **The mechanics already tell the story. The prose does not yet.** "Mystwood remembers" *is* the fleet's Contact memory. The Aetherbond's shared pain *is* the resolve network's contagion. The flagship ("the standard bearer", "the captain of the team", Ships §4) *is* the carrier of the carved orders. The prior review verified this fit (verified_brief, market-meta-narrative-5), and no authoritative document yet connects them (C4).
4. **The Ender's Game ordering has a ready-made mechanical home:** the Campaign doc's cognition ramp (naive fleets in Cam 1–~8, sharper in ~9–22, anticipating in ~23–32). The fiction can explain it without breaking determinism. The armada came in **tides**. The first tide was grown fast and carved in anger, with crude single orders. Wreck-wood drifts home, as the Aelvaren once did. The groves read each wreck and grow the next tide wiser (C2).
5. **Carved orders read from sunk or routed ships are the missing "after-the-fact explanation".** The prior review found that legibility has to be earned through tells plus explanation after the fact, and that the fleet's next-sortie plan (Fleet Memory §5, §12) is named but never specified. A post-battle **Reading** is the diegetic surface for both. In it, Seren (and later Rhyna and Halvard) translates the carving the fleet actually followed. The translation starts as fragments, echoing the emissary's "Stop… Sky… Dying…", and grows fluent over the war (C3).
6. **The fleet's deception can be made true to the lore.** Mystwood cannot lie ("no word could be twisted"). The late fleet does not lie *in* the wood. It carves true orders to *deceive* ("Show them fear where you are strong"). The tragedy is that the wood-folk learned deceit from the stone-folk. This supplies the fleet-baits-you direction the review found missing, and it lands where the Mimic debuts (Cam 27–31) (C2).
7. **There are serious internal contradictions** (A12). The biggest: the Coastal city fell "by sunset" and also "endured three months". The Leviathan (the *Coastal* Mystarch) destroyed the *Crystal* spire during the Fall, which also breaks the Ender's Game ordering. Rivenkeep predates the harbour-cities, yet the Coastal city is where "the first walls had been laid". The ships are called crewed in one place and autonomous in another. "Stone does not translate" collides with a "Myststone that remembers all". The 20-soldier roster includes admirals and generals, but the legend says the Shorelands had no navy and that their generals were slain.
8. **The 20-soldier roster (330 campaign-card quotes) belongs to the old identity and a different world.** It uses modern ranks (Pvt., LtCol., RAdm.), real-world names (Tomás Reyes, Priya Chakravarti, Yuki Tanaka), meta-game vocabulary ("heptominoes", "Wall Rack", "Campaign 26", "4% completion rate") and real-world allusions (the Minotaur; a near-quote of Yeats). Its "Hale" and "Voss" do not match the legend's Private Hale and Corporal Voss, and Sergeant Kael does not exist in it (A9).
9. **The prose is awkward for four measurable reasons** (B1). There are 60 em-dashes in 4,288 words. The narrator explains instead of showing. Modern and bureaucratic diction intrudes ("leverage", "henchmen", "profusely", "Neutralized", "cynosure", "sequel"). Abstract coinages carry the doctrine in the narrator's own voice ("ordination tendrils that predated this mortal life").
10. **The Odyssey structure fixes the "one long awkward chronicle" problem.** Turn the legend into a *book of tales told at Rivenkeep's hearth between sorties*. Each tale has a named teller: Halvard and Rhyna, a True Man, Seren, and the Wood itself. Each tale can be unlocked on its own, and none has to be a complete start-to-finish narrative (B8, C5).

---

# PART A — THE STORY AS IT EXISTS (COMPLETE EXTRACTION)

## A1. Where the lore lives

| Source | What it holds | Status |
|---|---|---|
| `Rivenkeep_GDD.html` / `.txt` lines 177–258 | The Legend of Rivenkeep, ch. I–X (4,288 words), XI The Whispers, XII Battle Messages | Only home of the legend; GDD is otherwise the OLD identity |
| GDD "Campaign Names, Soldiers & Quotes" (script data in GDD.html: `SOLDIERS`, `CAMPAIGN_NAMES`, `Q`) | 20-soldier roster, 33 campaign names, 330 campaign-card quotes (10 per campaign, rotate daily) | Not visible in the .txt extraction; extracted from HTML for this file (Appendix) |
| GDD Theaters (lines ~390–600) | 10 theaters: introduction campaign, land, problem, fragile grid, "enemy vehicles" per theater | Old identity |
| GDD Boss / Campaign / archive (`GDD_Removed` lines 408–482, 1165–1244) | Ten Mystarchs: theater, mechanic, HP, stealth | Archived; set-pieces are "a later design pass" |
| GDD Last Garrison | Pvt. Reyes line | Live |
| GDD AI §4–5 (lines 3186–3196) | "Ask the Stonewright" / "Ask the Emissary" personas; dynamic battle messages; interstitials; boss intros | Live (future feature) |
| GDD Challenges (lines ~1485–2066) | "Rhyna's Blessing", "Stonewright Legacy", "Pentomino/Wall Whisperer", badges | Live |
| GDD App Store shot list (line 3497) | Lore screen, "We remember our home too." "Discover the legend" | Live |
| `RIVENKEEP_JOURNAL.md` lines 235–248, 1823–1892 | NARRATIVE design ledger: every narrative decision and superseded variant | History |
| `Rivenkeep_AI_Image_Prompts.md` | Visual lore: "dark organic Mystwood hulls that look grown not built", "pale grey-green" / "torn grey-green sails", "crimson pennant flags" on castle keeps | Art direction |
| Module docs (Sep 2026) | Almost no lore. Stonewright Post tower; Stonewrights haul guns between sorties; flagship = standard bearer; lineage names; "Leviathan" as a lineage | ACTIVE identity |
| `verified_brief.md` findings market-meta-narrative-5, -6, -9 | Verified critique of lore delivery, doctrine voice, name collisions | Review |

## A2. The Legend, chapter by chapter (faithful beat list; all quoted lines verbatim)

**Epigraph / title cry (GDD 178–179).** "IN MEMORY OF OUR HOME, OUR FAMILIES, OUR GOD, OUR FREEDOMS, OUR PEACE." It is inscribed on the banner "that once fluttered above the last unbroken wall" and heads every tale of that place. The wind speaks it "through the high ridges where Rivenkeep still stands." The tale is framed as what "the old chroniclers would have set it down in runes upon enduring granite." It is an homage to Captain Moroni's Title of Liberty (Book of Mormon, Alma 46:12–13; journal 2026-04-09: "Captain Moroni / Title of Liberty inspired"). The journal describes the cry as a chiasmus.

**I. The Shorelands and the Stonewrights (180–186).**
- "In the elder days", the realm of the **Shorelands** stood on the **eastern coasts**: mountains and high hills tumbling to the sea. Its people, the **Shorelanders**, were builders and carvers of stone, not seafarers. They paved "vast roads like veins" and raised **ten great harbour-cities** about natural havens:
  1. the **eldest Coastal city**, "where the first walls had been laid";
  2. the **River city**, "where waters met the tide";
  3. the **Swamp settlement**;
  4. the **Forest keep**;
  5. the **Mountain stronghold**;
  6. the **Volcanic forge**;
  7. the **Desert citadel**;
  8. the **Frozen outpost**;
  9. the **Sky tower**;
  10. the **Crystal spire** "that caught the sun like a blade of ice".

  "Ten cities, ten harbours, ten kindreds who called themselves one nation."
- **The Stonewrights** were an ancient guild of master-builders and holy elders, "keepers of the religion and guardians of absolute truth". Every fortress, temple and monument was their labour. **Creed:** "Build, do not destroy. Protect, do not attack." No Stonewright bore a weapon; "mortar and chisel were their only arms." Women bore the title **Elderess** and "stood equal in all things to their husbands in the craft."
- "Not all Shorelanders were Stonewrights, yet all Stonewrights were Shorelanders." Children were *called* in infancy from any household, most from Stonewright blood. Being called was an honour, and no parent objected.
- **The Aetherbond** was the ordained pairing of infants, husband and wife, chosen at birth by the guild's **seers**. The union was "designed by God, with ordination tendrils that predated this mortal life." Both families raised the pair, and the **Theoliths** taught them: "great husband-and-wife Stonewrights called to the teaching for a season." These were "Covenants of Completion." Pairs lived, worked and worshipped as one, with wordless movement and coordination always in sync. Their work was "not doubled but multiplied twelvefold." "Every great wall and soaring temple was the work of such pairs."
- No Aetherbond ever fell apart. The pain and thought of one were felt by the other. "Separation, God did not permit." **The Aetherbonded died together.** The longest separation was rumoured to be **eight days**, which most held a fancy; in truth it was hours, and many died in the same moment. "Birth united them; death could not separate them."
- **The Stonwryt** was the guild's most ancient symbol: "a vow sealed in living rock, earned by toil and skill". It was carved into the foundation of every great work as a master's promise that the wall would hold, and it could not be bought, only earned. The **Stonwryt coin** was named after it: partly gold, partly fine-hewn black stone, minted only by "the finest craftsmen couples of the guild in workshops no outsider had ever entered." It was "trust, sealed in stone."
- The Shorelanders feared the open sea. Brave souls who neared the everlasting **fog-bank** turned back with wild stories. Sailors called it **the Mistlands**. The Stonewrights recorded its "blackish veil" in their oldest archives "as wonderings".

**II. The Mystaeri and the Living Mist (187–191).**
- The fog was "a living barrier — ancient, deliberate, and breathing", woven by the **Mystaeri**. Beyond it lay "measureless flat forestlands that stretched to the world's far edge." The Mystaeri were "older than the builders by many centuries" and "lived twice and half again as long as any Shorelander." They raised the mist to cloak their realm.
- They lived in kinship with the **Mystwood**, "the vast and dreaming forests". The trees exhale the mist, and the mist sustains trees and folk. It filters the sun into "a gentler radiance". The Mystaeri are "not creatures of darkness" but are woven to the twilight; the unfiltered sun withers them "as it withers a deep-forest fern dragged into open desert." Without the mist the wood sickens, and without both the Mystaeri perish: "newborns growing frailer, their eldest dwindling." "The mist was not a wall... It was the air they breathed."
- The Mystaeri could see out through the veil and marked every Shoreland hull that brushed it. The Shorelanders saw only grey. "Each brush was a cut, every trespass counted as a wound."
- **Mystwood is "their tongue of truth."** A covenant carved in living Mystwood "would interpret the writer's intent and render meaning clear to any who touched it", bridging the dialects of the Mystaeri **thunder-tongue** so that "no word could be twisted and no promise misheard." They trust only wood for anything sacred or binding. Kinds of Mystwood include "twisted boughs for ceremony, pale saplings for song, silver-barked elders for council." **The Mystholders** were "tall and dark-trunked, growing in solemn ranks at the fog's outermost edge", "the living pillars of the barrier itself, the anchors that bound the mist to mortal earth." Their timber was "harder than oak, lighter than iron, proof against rot". These alone the Shorelanders found and coveted.

**III. The Pride of the Shorelands (192–195).**
- In "the high summer of their pride", with rich cities and heavy trade, the Stonewrights' counsel seemed "a voice from humbler days." **For two generations the Trade Council** sent expeditions to fell Mystholders "for the buttresses of fortresses, bridge-beams, and all manner of decadence and wealth." The fog thinned "like a dying enchantment", and the Council named it fortune.
- The Stonewright elders warned: "These trees grow in strange soil. The carvings we find beside them bear a tongue we cannot read. Where wisdom is absent, let restraint be our guide." But "commerce had become king, and the Stonewrights were reckoned relics."
- The Mystaeri "carved warnings upon the stone", believing stone would translate as Mystwood does. "But stone has no intelligence. Stone does not translate." The warnings arrived "beautiful and mute". Some were locked in Stonewright archives; others were sold as curiosities, "holy pleas reduced to ornament on the walls of harbour-houses."
- The harvest ceased "not by wisdom but by the fickleness of men": the trees grew scarce and cheaper substitutes appeared. "The forebears had not known what they destroyed. Their children would not know. The Shorelanders of the final days remembered nothing at all." By the time "the first dark sails appeared", the wheel of pride had turned: the people had begun to humble themselves, seek Stonewright counsel and mend temples. "But humility came too late."

**IV. The Emissary and the Ael'thar (196–204).**
- **The Ael'thar** was the holiest Mystaeri rite of fellowship, "a binding of gift, blood, and kinship across any divide." The supplicant (1) kneels and gifts a prized possession; (2) rises and takes the back of the other's neck gently with the right hand; (3) draws their heads together until the foreheads touch in silence; (4) with the left hand opens a shallow cut on the other's right arm; (5) releases the neck and cuts his own left arm; (6) the two turn and press their bleeding arms together, shoulder to shoulder, "a promise of united front, that harm to one was harm to both."
- **A single emissary** sailed through the dying mist to the **outermost Shoreland outpost**. He chose it because Mystwood was set about its doorways, walls and furniture, which he took for reverence. It was "the trappings of a rich man's vanity."
- **The outpost commander** was "a young nobleman's son — arrogant, quick to anger". He held the post by "his father's leverage in the Trade Council" and had been banished to the edge for his temper. He "had never known battle. He had never known patience." His "henchmen" served him.
- The emissary was "tall and pale, clad in woven mist-cloth". He spoke the thunder-tongue, "sharp syllables that rolled like storm-wind through ancient branches", and had learned fragments of Shoreland speech by listening across the veil. His words: **"Stop… Sky… Dying…"**. They were "the right words, spoken truly, but words without sentences are only sounds."
- He knelt and set down **petrified Mystwood**, "the most sacred of all Mystwood, wood that time itself had forgotten". Even a sliver is the most treasured gift a Mystaeri can give, and it speaks truth "slowly, requiring long contact". The commander "saw only a strange dark stone and kicked it aside. His henchmen chuckled."
- The emissary took the neck and the foreheads met. The blade touched the commander's arm, and the commander recoiled in terror, so the cut went deeper than intended. Bleeding and screaming, he called his men to seize the stranger and "ordered the killing blow. His henchmen obeyed."
- To hide the deed, the body was thrown on the emissary's small Mystwood vessel and set ablaze. "The old wood raged in its grief, fire leaping higher than any natural flame — as though the wood itself was screaming." The garrison shoved it off. The commander's report read: **"Unknown intruder. Hostile intent. Neutralized. Vessel burned and released."**
- "But Mystwood remembers." The vessel, **the Aelvaren**, "proud to be the Bearer of the Binding", "turned against the current and sailed itself home." Through secret channels it beached "before the Mystaeri council-hall." The Mystaeri "saw their holiest peace... answered with murder and flame. They did not know it was ignorance. They saw only an act of war."

**V. The Fleet (205–208).**
- The Mystaeri children weakened. The elders who counselled patience were "dying of the very wound for which they counselled patience." "When the bones of the emissary washed ashore, something broke." The young had grown up under a vanishing sky. The elders pleaded, "send another, learn their words," but their voices were too few. **The young put it to council, and the vote was carried "by the weight of anger and grief."**
- **The fleet was grown, not built,** from sacred Mystwood. "Battle orders were carved into the living wood." Hulls came from breathing trunks, keels from root-systems, and masts from "saplings trained by decades of windsong." There were Warships, Fire Ships, Transports ("to pour warriors through every breach"), Mortar Ships and Torpedo Boats, and **ten colossal Mystarchs**: "the sovereign commanders of the entire armada, the final exalted expressions of the eldest Mystholders themselves. The last living pillars of the barrier, now grown into moving thrones of war — one for each Shoreland harbour-city." "The ships obeyed the orders carved within them as a hand obeys the mind, for the wood of the hull and the wood of the command were one."
- "The growing took decades." Those who cried for war grew old and were forgotten. "The armada was built and sailed generations before it would arrive." When it broke through, "few Mystaeri remained: only scattered souls tending the last groves." "The war was a doom set in motion by the dead, crewed by the living, against a people who had never known they were the foe."

**VI. The Fall and the Flight to Rivenkeep (209–212).**
- The armada came without warning. The Shorelands had "no standing navy, no war fleet, no defensive doctrine"; their walls were "built for ceremony and weather, not for bombardment." "At dawn the fleet fell upon the Coastal harbour. By sunset it was ash." No envoy they could understand came, "only the harsh thunder of a tongue born in ancient forests." City by city the havens fell: **the Coastal city endured three months; the Volcanic forge five; the Crystal spire**, "raised by seven generations of Stonewrights, collapsed in a single night when the Mystaeri ghost fleet unleashed the Leviathan Mystarch." "The Stonewrights... did not fight. They simply walked."
- The survivors fled into the mountains to **Rivenkeep**, "more myth than memory... the castle that had never fallen", long abandoned for the lowlands.
- They found "a shadow": broken gates and crumbled walls. "What man could not destroy, time had withered... forgetting had done what no enemy ever could." "Some shook. Some wept. Some fell and would not rise. For the first time, the Shorelanders began to fracture."

**VII. The Captain and the Title of Liberty (213–223).**
- **The Captain** was "no general, no politician, no nobleman, no Stonewright", only the captain of a small company, his **True Men**: "soldiers who kept their oaths, who built what they promised, who fought only when the cause was just." He found them one by one and bound them by trust. He was humble and waited for a greater leader, but "the generals were slain, the politicians forgotten, the nobles scattered, and the Stonewrights despaired." At the gates some cried for surrender, some for flight, some to hide. "The True Men looked to their Captain. The Captain looked at the wall."
- He climbed it alone, tore his cloak, raised it on a pike, and wrote in his own hand: **"In memory of our home, our families, our God, our freedoms, our peace."** The True Men answered first, then the soldiers, then the refugees, and the people "chose to unite — not by command". The humble captain "had become the cynosure."
- The banner called the Stonewrights too. They had watched ten cities die, and "the faith that had sustained them through twelve generations" faced the truth "that walls built for peace must sometimes be defended with blood." The challenge: **"Your walls are falling. Will you build, or will you watch and die?"**
- **Elderess Rhyna**: "it was said that her ancestor-grandfather and mother had laid the capstone of Rivenkeep's inner gate in the age before the harbour-cities". She bowed, lifted her chisel, and cried: **"The mortar cries out from the ground. Rise, Stonewrights! Lay stone upon stone. Stand every wall to the very end."**
- **Her husband (unnamed in the source; now Halvard)** raised his chisel beside hers: **"Rise! Rise! Rise!"** The guild took up the shout, "until the walls of Rivenkeep itself seemed to tremble".
- The Stonewrights would not take up arms ("they never would"), but they would build between volleys and mend breaches "with the speed and precision that only Aetherbonded pairs could achieve." "Not the sword, but the stone. Not the killing, but the keeping."

**VIII. The Anointing (224–227).**
- In Rivenkeep's deepest vaults Rhyna found the **Rite of the Cornerstone**, "the most ancient ceremony of the guild, the rite by which the first Stonewrights had consecrated the leaders of Rivenkeep to build Rivenkeep itself". Its texts held "the secrets of building for battle."
- "Elderess Rhyna and her husband together" performed it for the Captain before all, in the shadow of the Title of Liberty. The **three oils** were "oil of cedar for endurance, oil of granite-bloom for strength, and oil of myrrh for the burden of command." They gave him **the ceremonial staff**: "a rod of polished wood capped with the finest polished ashlar, borne by every overseer of a great Stonewright work since the founding." It named him **Commander of Rivenkeep**.
- He stayed humble. He did not carry the staff into battle or wear the oils after that day, and he led from the wall, "mortar upon his hands and a soldier's plain cloak upon his back." "In his own heart he was still only the Captain."

**IX. The Rivenmen (228–231).**
- "The Commander fought. The Stonewrights built." From that union a people was remade. They renamed the land **Rivenkeep**, "all of it, from the high ridge to the farthest fallen harbour," and vowed on the banner to reclaim every stone. The eldest still murmured "the Shorelands", a name "to return to, perhaps, when the last wall stood and the last Mystarch lay broken." Until then they were **the Rivenmen**, "the people of the riven stone, the keepers of the keep that would not fall."
- In quiet hours the Stonewrights began to decipher "the enemy's gentle Mystwood tongue". Only after the final Mystarch fell did Rhyna find **a sliver of living Mystwood**, "still green, still aware." When she touched it: **"We remember our home too."**

**X. Culmination of Myth (232–233).** "Thus ends the legend. There is no sequel, no easy healing. Only the weight of inherited sorrow". The sea whispers on, and the torn cloak flies. "Somewhere, across the thinning fog, a seasoned young Mystaeri engraves the words of his youth, 'In the memory of our home, our families...' into the **Myststone** that remembers all."

## A3. XI — The Whispers (verbatim, GDD 234–242)

Frame: "Every wall the player places is laid by Stonewright hands. Every cannon is positioned by the Commander's orders. Build, then Deploy, then Fight — the sacred union of Commander and Stonewrights". The truth came "in whispers" as the Stonewrights "learned to read the Mystwood tablets". "Twenty voices tell the story: soldiers (Private Hale, Corporal Voss, Sergeant Kael), the True Men, and the Stonewrights (Elderess Rhyna and her apprentice Seren)."

| Campaigns | Whispers (verbatim) | Emotional beat (journal: confidence→humility→fear→resolve→defiance) |
|---|---|---|
| 1–6 | "They picked the wrong fortress." / "Twelve generations of Stonewright walls. Let them try." | confidence |
| 7–14 | "Rhyna says they tried to write in our tongue. The sounds were close, but the symbols wrong." / "Stone does not speak as they believed." | humility |
| 15–22 | "Rhyna held the petrified wood for an hour. She said she could hear a voice — faint, like water over stone." / "The Ael'thar. Blood to blood. A frightened boy gave back fire." | fear / guilt |
| 23–31 | "The fleet cannot be recalled. The wood obeys the wood." / "Our forebears were proud. Their response was rage. Both are true. Build the wall." | resolve |
| 32 + Boss Finale | "We do not fight because we are right. We fight because our children are behind these walls." Then the living sliver: "We remember our home too." | defiance → recognition |

## A4. XII — Battle Messages (verbatim, GDD 243–257)

System: each of the 190 battlefields has a flavour theme tied to its theater, campaign stage and narrative position. At battle start (first Build, below the phase bar) one message shows for **3 seconds**, drawn at random from a pool of **5–8 per battlefield**, and it is different on every replay. The messages are stored in the battlefield data file.

- *Coastal, Campaign 3 ("The Walls Will Hold"):* "The salt air stings. The walls don't care." · "Grandfather built this harbor wall. I'll be damned if I let it fall." · "Two ships on the horizon. Standard formation. This will be easy." · "The Commander says hold the coast. We hold the coast." · "Fresh mortar, fresh stones. The wall stands renewed."
- *Frozen, Campaign 24 ("The Reckoning"):* "Ice in the mortar. Ice in my bones. The wall still holds." · "They sent the Leviathan against the Frozen pass. We sent it back." · "Voss asked why we fight for ice and stone. I said it's not the ice I'm fighting for." · "The wind carries their drums. Let it carry our cannons' answer."
- *Future dynamic lines (GDD AI §5):* "Three castles held against the Leviathan — the Stonewrights will sing of the east wall" · boss intro: "You fled the Sandworm last time, Commander. It remembers."

## A5. The narrative ledger in the journal (decisions and superseded variants)

Canon decisions (journal 235–248, 1823–1892), by date:
- **2026-04-09:** narrative added ("Captain Moroni / Title of Liberty inspired"; "No cutscenes, just evolving flavor text"; arc confidence→humility→fear→resolve→defiance). "Inspired by Title of Liberty + Ender's Game moral ambiguity." The Commander is he/his, a specific person. Harm was accidental, "4 generations removed". The fleet was "launched 2 generations ago, can't be recalled — Ships follow carved instructions. Autonomous war machines following ancient orders." The Mystaeri are "slightly more villainous: chose warships over words. Had centuries to learn Shoreland language... Disproportionate response." The Shorelanders are "defending, not attacking. Commander reclaims defensive positions, pushes fleet back from Rivenkeep's approaches." "Mystwood intelligence: wood is alive, remembers, can navigate. This is why it made great ships." The Mystaeri language moved from "cracking rock and grinding gravel" to "thunder rolling through a forest canopy. Elvish but abrupt." Ael'thar replaced **Rak'thol**; Elderess Rhyna replaced **Kiera** ("stone-derived name").
- **2026-05-07:** Mystaeri replaced Mystborn (trademark). Men of Shoreland are Shorelanders, renamed Rivenmen after the unity. Aetherbond + Theoliths ("12x coordination. Die together"). Stonwryt has a dual meaning. Elderess is the title for women Stonewrights. The Ael'thar ritual was revised to its current form. The fleet is grown, with orders in Mystwood (not stone). **Seren** is Rhyna's apprentice ("replaces Hale as translator. Private Hale remains as soldier/discoverer"). "Final poetic rewrite... Silmarillion-inspired compression."
- **2026-05-23:** Mystarchs (the 10 bosses renamed, "grown from eldest Mystholders"). Aelvaren named ("Bearer of the Binding").
- Other: "Ask the Garrison" was renamed "Ask the Emissary" (to avoid a collision with Last Garrison). There are 8 easter eggs, including "Rhyna's Blessing". "20 soldiers = narrative quote-givers".

Superseded variants a rewriter must *not* resurrect by accident:
| Element | Current (GDD) | Superseded |
|---|---|---|
| Tagline | "In memory of our home, our families, our God, our freedoms, our peace." | "In memory of our homes, our families, our freedom, and our peace." (04-09) |
| Title of Liberty challenge | "Your walls are falling. Will you build, or will you watch and die?" | "Will you build for your people, or will you watch them die?" (journal 05-07, listed as "refined": **conflicts with the GDD**) |
| Rhyna's cry | "...Stand every wall to the very end." | "...Lay stone upon stone until the last wall stands." (04-09); also "We do not fight. But we will build faster than they can destroy." (04-09, no longer in the legend) |
| Harvest distance | legend: 2 generations of harvest, then children and grandchildren who forgot | journal: "4 generations ago" |
| Mystaeri lifespan | legend: "twice and half again" (2.5×) | journal canon row: "Live 1.5x longer" |
| Translator | Seren | Hale |
| Emissary's rite | Ael'thar | Rak'thol |

## A6. Complete named inventory

**Persons**
| Name | Who | Source |
|---|---|---|
| The Captain / the Commander (Commander of Rivenkeep) | Unnamed humble captain of the True Men, writer of the Title of Liberty, anointed Commander; the player's role ("Every cannon is positioned by the Commander's orders") | Legend VII–IX, XI |
| Elderess Rhyna | Stonewright elder; descendant of the pair who laid the inner-gate capstone; cries "Rise, Stonewrights!"; finds the Rite; reads the petrified wood; touches the living sliver | VII–IX, XI |
| Elder **Halvard** (new) | Rhyna's Aetherbonded husband ("Her husband" in source); answers "Rise! Rise! Rise!"; co-performs the Rite | VII, VIII; Jack 2026-09-25 |
| Rhyna's "ancestor-grandfather and mother" | Laid the capstone of Rivenkeep's inner gate "in the age before the harbour-cities" | VII |
| Seren | Stonewright apprentice to Rhyna (now to both); translator | XI; journal 05-07 |
| Private Hale | Soldier voice, "soldier/discoverer" | XI; journal |
| Corporal Voss | Soldier voice ("Voss asked why we fight for ice and stone") | XI; XII |
| Sergeant Kael | Soldier voice (no lines anywhere) | XI |
| The True Men | The Captain's oath-keeping company (none named) | VII, XI |
| The emissary | Unnamed Mystaeri, tall, pale, mist-cloth; murdered at the outpost | IV |
| The young commander of the outpost | Unnamed nobleman's son, banished; ordered the killing | IV |
| His father | Trade Council member with "leverage" | IV |
| The henchmen | The garrison who killed the emissary | IV |
| "A seasoned young Mystaeri" | Engraver in the coda | X |
| Pvt. Tomás Reyes and 19 others | The 20-soldier roster (A9) | GDD script |

**Peoples, orders and bodies:** Shorelanders (later Rivenmen) · the Stonewrights (guild) · Elderesses / (Elders) · the Theoliths · the guild's seers · the Aetherbonded · the Trade Council · the True Men · the Mystaeri · the Mystaeri council (at the council-hall) · the "younger generation" war faction vs. the patient elders · sailors of the Shoreland coasts.

**Places:** the Shorelands (eastern coasts) · the ten harbour-cities (A7) · the paved roads · the outermost Shoreland outpost · the Mistlands / the fog-bank / the veil · the Mystaeri realm ("measureless flat forestlands... to the world's far edge") · the Mystwood · the fog's outermost edge (Mystholder ranks) · the Mystaeri council-hall · "secret channels" (the Aelvaren's route) · the last groves · Rivenkeep (the Keep, "the castle that had never fallen", in the mountains, "high ridges") · Rivenkeep's inner gate, ancient courtyard, deepest vaults, halls · "Rivenkeep" as the renamed whole land · harbour-houses (where warnings hung as ornament) · the Stonewright archives · the Frozen pass (battle message).

**Rites and customs:** the Aetherbond (Covenants of Completion) · the calling of infants · the Theoliths' teaching · the Stonwryt vow carved in every foundation · the Ael'thar (six steps) · the Rite of the Cornerstone (consecration of a great work and its overseer: three oils and the staff) · the council vote · the Stonewright creed · the Title of Liberty.

**Objects and materials:** the Title of Liberty (the Captain's torn cloak on a pike, written in his hand) · the Stonwryt (vow-stone) and the Stonwryt coin (gold + black stone) · chisels and mortar · Mystwood (kinds: ceremony boughs, song saplings, silver-barked council elders, Mystholders) · petrified Mystwood (the emissary's gift) · living Mystwood sliver · the Aelvaren (the emissary's Mystwood vessel) · the Mystaeri warnings carved on stone · the "Mystwood tablets" (XI) · carvings beside the Mystholders (III) · mist-cloth · the emissary's blade · the three oils (cedar, granite-bloom, myrrh) · the ceremonial staff (polished wood, ashlar cap) · the texts of the Rite of the Cornerstone · the Myststone (X) · the fleet: Warships, Fire Ships, Transports, Mortar Ships, Torpedo Boats, the ten Mystarchs · "their drums" (XII).

**Events, in order:** the founding of Rivenkeep (the first Stonewrights, the Rite) → the age of the harbour-cities → the fog seen as the Mistlands → the two-generation Mystholder harvest → the mute warnings → the harvest ends by fickleness → the emissary and the broken Ael'thar → the Aelvaren's voyage home → the council vote → the decades of growing → the armada sails → the Shorelanders forget; pride turns to humility → the Fall of the ten havens → the flight to Rivenkeep → the fracture → the Title of Liberty → the cry of the Stonewrights → the Anointing → the siege (the game) → the Rivenmen named → the deciphering → the last Mystarch falls → the living sliver speaks → the coda.

**Numbers and motifs:** 10 (cities, kindreds, harbours, Mystarchs) · 12 (twelvefold work, twelve generations of faith, "Twelve generations of Stonewright walls") · 7 (generations to raise the Crystal spire) · 8 days (longest bonded separation, rumour) · 2 generations of harvest · 3 months (Coastal) · 5 months (Volcanic) · 1 night (Crystal) · 2.5× Mystaeri lifespan · 3 oils · "Rise!" ×3 · the three-word emissary speech. Recurring images: fog/veil/breath, wound/cut, blood, fire that screams, wood that remembers, stone that is mute, the torn cloak, the capstone and gate.

## A7. The ten harbour-cities ↔ the ten theaters ↔ the ten Mystarchs

| # | Legend city (label only) | Theater (GDD) | Intro Cam | Terrain problem | GDD "enemy vehicles" (old) | Mystarch | Mystarch mechanic (archived) | HP |
|---|---|---|---|---|---|---|---|---|
| 1 | eldest **Coastal city** ("first walls") | Coastal Fortress | 1 | none (baseline) | galleons, rowboats, rope-netted transports, fire barges | **Leviathan** | Submerges every 2 sorties; resurfaces near a castle; tidal wave pushes walls 1 grid | 8,000 |
| 2 | **River city** ("waters met the tide") | River Crossing | 3 | split territory | gunboats, canoes, barges, tar-pot boats | **Hydra** | 3 heads, each 1/3 HP; dives; regenerates 5%/sortie if undamaged | 9,000 |
| 3 | **Swamp settlement** | Swamp Ruins | 5 | bog grids rot walls | mossy swamp boats, reed skimmers, disease barges | **Plague Herald** | Poison cloud DoT on walls; dissolves into water; spawns plague mini-troops | 8,000 |
| 4 | **Forest keep** | Deep Forest | 7 | fog + DMZ advance; densest trees | war wagons, ranger scouts, horse-drawn log transports, fire carts | **Ancient Treant** | Roots grow through walls 1 grid/sortie; hides as a tree; spawns trees | 14,000 |
| 5 | **Mountain stronghold** | Mountain Pass | 9 | troop map: cliff-climbing | armoured wagons, mule carts, siege trains, wheeled catapults | **Colossus** | Boulder throw; climbs for range; cave stealth; vulnerable while throwing | 12,000 |
| 6 | **Volcanic forge** | Volcanic Isle | 11 | shrinking island, crust heat | obsidian barges, magma skimmers, fire barges | **Magma Titan** | Lava breath cone; lava trail; armour weakens below 50% | 10,000 |
| 7 | **Desert citadel** | Desert Canyon | 13 | wind drift, sand fog, fissures | sand skiffs, dune runners, camel caravans, trebuchets | **Sandworm** | Burrows, charges in a line, erupts under a castle | 6,000 |
| 8 | **Frozen outpost** | Frozen Citadel | 15 | ice, DMZ, blizzard, wind | icebreakers, sled cavalry, runner transports, frost catapults | **Frost Wyrm** | Ice breath freezes walls (no repair next Build); blizzard stealth; makes ice grids | 7,000 |
| 9 | **Sky tower** | Sky Bastion | 17 | isolated shrinking islands | propeller barges, glider raiders, chain-hung carriers, dirigibles | **Storm King** | Flies; thundercloud stealth; lightning hits highest-HP cannon; cannons at ½ range | 5,000 |
| 10 | **Crystal spire** ("caught the sun like a blade of ice") | Crystal Depths (an *underground cavern*) | 19 | shot bounce, collapse, dark | crystal golems, gem crawlers, prism cannons | **Crystal Lich** | Bouncing beam; becomes a crystal; reflective shields | 9,000 |

The Boss Finale uses the 4 starting castles; "the emotional weight comes from familiarity." Bosses are "rare promoted flagships" on the Bulwark / Leviathan / Herald / Mimic / Chirurgeon chassis (Ships §4). Death animations: "Leviathan sinks into the sea, Colossus crumbles, Sandworm explodes from the ground." The live Campaign doc keeps all ten names.

## A8. The fleet as the ACTIVE docs define it (lore-relevant facts only)

- **Lineages** (Ships): canonical Bombard, Recon, Runner, Skyfall, Quartermaster, Bulwark, Sower, Reaver; expansion Provocateur, Breacher, Corsair, **Leviathan**, Wraith, Mimic, **Herald** (boss-only), Chirurgeon-Fleet; troops (Sapper, Aegis, Linebreaker, …); bombers launched by Skyfall. "Ship names are working handles... not final flavour." The old legend roster maps as follows: Warship→Bombard, Scout→Recon, Transport→Runner, Carrier→Skyfall, Fire Ship→Sower/Breacher, Hospital→Chirurgeon-Fleet, Artillery Barge→Leviathan, Torpedo Boat→Corsair (Campaign §5). **Mortar Ships** and **Torpedo Boats** in the legend are old names.
- **The flagship** "is the standard bearer"; "the captain of the team"; "a normal-looking hull wearing a flag icon" that "sails inside a convoy" and "has a job of its own." Only the first flag is buffed ("a better-built hull with a better crew because the fleet chose it for the job"). When it is killed, the most command-capable survivor is **field-promoted** (no buff, "a lieutenant standing in"), and "the fleet takes on its personality." A Herald boss "re-anchors on the standard, not a successor."
- **Resolve** is a per-ship network: fleeing hulls drag neighbours into a rout cascade, and steady clusters stiffen waverers. It is read only by the **motion signature** (Committed / Steady / Wavering / Breaking / Gone), never by a bar.
- **Memory** (Fleet Memory): three channels, LOS / Contact / Effect (the fear grid). The fleet computes a **next-sortie plan** during Build/Deploy "from its (last-observed, possibly stale) knowledge"; "Same memory → same plan."
- **Retreat and return:** survivors "retreat to spawn and re-emerge first, in order, a cognition-tick smarter" (Victory §4). **Ammo** is "the sortie's diegetic clock." **Purpose collapse:** orphaned screens may be "out for revenge" (journal cont.16).
- **Cognition ramp** (Campaign §4): naive in Cam 1–~8, tightening in ~9–22, sharp and anticipating in ~23–32; "felt not seen" but "subtle in magnitude, legible in kind." Mimic, "the fleet baiting back", debuts in Cam 27–31.
- **Defender lore hooks:** the **Stonewright** tower (repair; "fits the backstory"; taught first). The Deploy relocation penalty's in-world reason: "the Stonewrights spend the between-sortie hours hauling instead of improving." There is a Camouflage tower, and a Decoy Mast option.

## A9. The voices: the 20-soldier roster, campaign names and the Last Garrison line

The roster (GDD script `SOLDIERS`): "Soldiers range from terrified privates to supremely arrogant admirals — the rank determines the tone." Each campaign card shows 10 of their quotes, rotating daily (330 total, 33 campaigns; full text in the Appendix).

| # | Rank | Name | Tone |
|---|---|---|---|
| 1 | Pvt. | Tomás Reyes | Terrified, wide-eyed, apologetic |
| 2 | PFC | Lena Marsh | Nervous but trying to be brave |
| 3 | Cpl. | Dex Holt | Scrappy, gallows humor, sarcastic |
| 4 | Sgt. | Ama Okafor | Practical, gruff, motherly |
| 5 | SSgt. | Viktor Reznik | Dry veteran, matter-of-fact |
| 6 | MSgt. | Corinne DuPont | World-weary wisdom, seen it all |
| 7 | SgtMaj. | Elias Brant | Commanding NCO, earned respect |
| 8 | 2Lt. | Priya Chakravarti | Eager, bookish, quotes regulations |
| 9 | 1Lt. | James Hale | Growing confidence, earnest |
| 10 | Cpt. | Nadia Sorel | Decisive, sharp, no-nonsense |
| 11 | Maj. | Rowan Kettridge | Strategic thinker, chess analogies |
| 12 | LtCol. | Yuki Tanaka | Calculating, precise, data-driven |
| 13 | Col. | Emeric Thane | Authoritative, experienced, blunt |
| 14 | BGen. | Aldara Voss | Broad perspective, inspiring |
| 15 | MGen. | Obi Adeyemi | Political awareness, diplomatic |
| 16 | LtGen. | Sable Morrow | Philosophical, poetic, haunted |
| 17 | Gen. | Dren Calloway | Legendary, mythic, speaks in absolutes |
| 18 | RAdm. | Helena Voss | Naval tradition, formal, precise |
| 19 | VAdm. | Kira Nohlan | Grand strategist, cold clarity |
| 20 | Adm. | Marcus Sterling | Supreme arrogance, absolute authority |

**Campaign names (33):** 1 First Watch · 2 Shifting Ground · 3 Iron Tide · 4 Crooked Pieces · 5 Storm Warning · 6 The Long Wall · 7 Fire and Stone · 8 Broken Geometry · 9 Fog and Fury · 10 Divided Kingdom · 11 Wolves at the Gate · 12 Thunder and Ash · 13 The Widening Gyre · 14 The Architect's Nightmare · 15 Thin Line · 16 Tempest Reign · 17 The Crucible · 18 Blood Weather · 19 The Sprawl · 20 Siege of Fire Mountain · 21 The Gauntlet · 22 Shattered Compass · 23 The Reckoning · 24 Tides of Ruin · 25 The Noose Tightens · 26 Labyrinth of War · 27 Empire of Walls · 28 The Anvil · 29 Edge of Ruin · 30 The Last Geometry · 31 The Last Bastion · 32 Full Stack · 33 End Times.

**Last Garrison:** Pvt. Reyes: "The castle is falling! EVERYONE TO THE CANNONS!"

**Register audit of the 330 quotes:**
- Meta-game words: pentomino, hexomino, heptomino, Wall Rack, "Campaign 26", "Full Stack. All five layers", "4% completion rate", "8.3%", "ERROR: INSUFFICIENT DATA".
- Modern idiom and anachronism: Tuesday, Wednesday, "summer home", "movie", "metal", "Field Manual 7", "three continents", "before breakfast".
- Real-world allusion: the Minotaur (C26); a near-quote of Yeats, "The gyre widens. The center cannot hold" (C13; the campaign name "The Widening Gyre" is also Yeats).
- Obsolete mechanics: Sappers, hospital ships/medics, friendly fire, siege ships, lightning, rams.
- Theology in a jokey voice: "God gave us pentominoes to teach humility."

Several quotes are nonetheless strong and in keeping with the world. They could survive a recast with minor edits: "Every fortress begins with a single stone. And a prayer." · "Put the stone down, pick another stone up. That's the whole war, kid." · "Every castle you claim is a promise you must keep." · "Tempests pass. Fortresses endure." · "Hammer falls. Fortress holds. Repeat until one breaks." · "They bring medics now. That means they plan to stay." (recast as healers).

## A10. Other lore-bearing surfaces

- **Personas:** "Ask the Stonewright" (building help) and "Ask the Emissary" (rules and lore voice; "herald and lore-keeper"). *The persona shares its title with the murdered emissary* (verified_brief -9).
- **Codex / lore screen / interstitials:** a searchable FAQ and codex exist; there is a lore screen (store shot 10: "We remember our home too." / "Discover the legend"). "Campaign & war interstitials. Short lore beats between campaigns." "Lore integration (progressive revelation)" is scheduled for Phase 5.
- **Achievements and easter eggs:** **Rhyna's Blessing** (all 10 castles enclosed at once; "Blessed" badge) · **Stonewright Legacy** (50,000 pieces; "Stonewright" badge) · Pentomino Whisperer · Wall Whisperer · **Pacifist** (win with 0 ships destroyed and 0 cannons surviving). The Pacifist egg echoes the creed.
- **Economy flavour:** "Assign Stonewrights" button, a stone-chiseling sound, the Stonwryt counter with a stone-mason icon, the ω symbol on harvested interior blocks. The currency name **Stonwryt** is a homophone of **Stonewright** (verified_brief -9).
- **Visual lore (image prompts):** "dark organic Mystwood hulls that look grown not built", "pale grey-green" / "torn grey-green sails", castle keeps with "crimson pennant flags". The Map View is a "WWII command table" and the World View is a 2.5D diorama.

## A11. Name collisions

| Collision | Where | Suggested resolution |
|---|---|---|
| **Leviathan** = SEA 12 lineage *and* the Coastal Mystarch | Ships §6 / Campaign §2 | Give the Mystarch its Mystaeri true name (B7), with "the Leviathan" as the Rivenmen's fear-name only if the lineage is renamed; or rename the lineage (e.g., "Dreadhull") |
| **Herald** = SEA 15 lineage *and* "Plague Herald" Mystarch | Ships §6 / GDD | As above |
| **Stonwryt / Stonewright** | GDD economy | Keep Stonwryt as the lore object; UI currency gets another name ("seals", "marks") (verified_brief -9) |
| **Emissary** persona vs murdered emissary | GDD AI §4 | Rename the persona "Seren" or "the Archivist" |
| **Hale / Voss** in two incompatible forms | Legend vs roster | Pick one set (A12 #14) |
| **Rivenkeep** = fortress *and* the whole renamed land | Legend IX | Deliberate, but say so once in the tale ("they gave the name of the Keep to all the land") |
| **Commander** = the Captain *and* the outpost's "young commander" | Legend IV vs VII | Call the nobleman's son "the warden of the outpost" or "the lordling"; reserve "Commander" for the Captain |

## A12. Inconsistencies (numbered; severity; fix options)

| # | Sev. | Inconsistency | Evidence | Fix options |
|---|---|---|---|---|
| 1 | **High** | Coastal city falls **in a day** and **endures three months** | VI: "At dawn the fleet fell upon the Coastal harbour. By sunset it was ash." then "The Coastal city endured three months." | The harbour (port) burned in a day; the city behind it held three months. Say so. |
| 2 | **High** | **Leviathan** (Coastal Mystarch) destroys the **Crystal** spire; Mystarchs appear in the Fall, which breaks the Ender's Game ordering (the greatest ships should come last) and the Boss Finale placement | VI; Campaign §2; Ships §4 | Remove the named Mystarch from the Fall. At most "a shadow in the fog greater than any hull" is glimpsed. The Mystarchs are the **last tide**, arriving after the Fall to sit enthroned in the ten fallen havens ("one for each Shoreland harbour-city"). |
| 3 | **High** | **Rivenkeep predates the cities**, yet the **Coastal city is where "the first walls had been laid"** | I vs VII ("in the age before the harbour-cities"); VIII (the first Stonewrights consecrated Rivenkeep's leaders "to build Rivenkeep itself") | Make Rivenkeep the first work (the Rite supports this); the Coastal city is "the eldest of the *havens*". |
| 4 | **High** | **Crewed or autonomous?** | V: "crewed by the living"; V: "few Mystaeri remained"; journal: "Autonomous war machines following ancient orders" | See C2. Recommended: the fleet is wood-driven and obeys the carvings. A few young Mystaeri sail only in the flag-hulls (the "better crew" of Ships §4) and in the Mystarchs. Troops need a fiction (#5). |
| 5 | **High** | **Who are the troops** if the Mystaeri are nearly extinct? | V: Transports "pour warriors"; Ships §7 troop lineages | Options: (a) the last young Mystaeri, few and fanatical; (b) wood-grown "root-warriors" (Mystwood that walks), which fits "Mystwood is alive"; (c) both, with the living ones rare and marked. (b) keeps the tragedy clean, since no Mystaeri families are slaughtered by the thousand, and it honours the "near-extinct" premise. |
| 6 | **High** | "**Stone does not translate**" vs a "**Myststone that remembers all**" | III vs X | Either delete "Myststone" (the coda engraves in Mystwood), or make it deliberate: the last Mystaeri *learned to carve in stone*, the builders' medium. That is a haunting reversal, but it must be explained. |
| 7 | **High** | The **roster contradicts the world**: admirals when there is "no standing navy"; generals when "the generals were slain"; modern ranks; no Kael | VI, VII vs `SOLDIERS` | Recast the roster (C7): in-world ranks, Shoreland names, True Men and wall-wardens. |
| 8 | Med | **What the Stonewrights read:** warnings carved *on stone* (III), "Mystwood tablets" (XI), "the enemy's gentle Mystwood tongue" (IX), carvings found beside the Mystholders (III), and the Whisper "they tried to write in our tongue. The sounds were close, but the symbols wrong" (contradicts III, where the warnings are in their own tongue and trust stone to translate) | III, IX, XI | Define three corpora: **the Mute Stones** (warnings in Mystaeri script on stone, in the archives and harbour-houses); **the Wreck-wood** (carved orders from sunk hulls, the siege's new source); **the Petrified Gift** (the emissary's wood, slow truth). The "wrong symbols" whisper becomes: "they carved in their own letters, trusting the stone to carry the meaning." |
| 9 | Med | **Thunder-tongue vs "gentle" Mystwood tongue** | II, IV vs IX | Make it deliberate: the Mystaeri *speak* in thunder, and the wood *renders* it gently. Two registers of one language (B7). |
| 10 | Med | **Generations** do not add up: 2 generations of harvest, then 2–3 of forgetting (legend); "4 generations" (journal); "fleet launched 2 generations ago"; "growing took decades" | III, V; journal | Fix one chronology (proposal, Shoreland generations of ~25 years): harvest years 0–50; emissary ~year 45; council vote ~year 50; growing ~50–90; first tide sails ~year 90; the Fall ~year 120 (the "final days", ~3 generations after the harvest began, so no one living remembers); the siege follows. Mystaeri at 2.5× lifespan means some who voted could still be alive, which is useful for a "Last Carver". |
| 11 | Med | **Lifespan** 2.5× vs 1.5× | II vs journal | Pick one. 2.5× makes the "dead set the doom" line harder; 1.5× makes it easier. |
| 12 | Med | **The petrified gift's journey:** kicked aside at the outpost generations ago, yet Rhyna holds it | IV vs XI | Needs a tale. It lay in the outpost's dust and then passed as a curiosity through the harbour-houses to the Stonewright archives, like the mute warnings. It survived the Fall in a Stonewright's pack on the walk to Rivenkeep. A natural "wanderings of an object" tale (B8, Tale 7b). |
| 13 | Med | **"The fleet cannot be recalled"** vs the win condition (the fleet routs and turns back) | XI vs Victory §4 | "Recalled" means by a voice, since no one living can call it home. It can still be *turned*: the wood knows fear (the Aelvaren "raged in its grief"). "It cannot be called home. It can be made to go home." |
| 14 | Med | **Hale / Voss / Kael** do not match the roster | XI vs `SOLDIERS` (1Lt. James Hale; BGen. Aldara Voss; RAdm. Helena Voss; no Kael) | Keep the legend's Private Hale, Corporal Voss, Sergeant Kael as the core soldier voices; fold the roster into them. |
| 15 | Med | **Campaign names in XII examples** do not match `CAMPAIGN_NAMES` | Cam 3 "The Walls Will Hold" vs "Iron Tide"; Cam 24 "The Reckoning" vs "Tides of Ruin" (Reckoning is 23) | Regenerate; in-world campaign names are proposed as Tale titles (C5). |
| 16 | Med | **A Leviathan in a Frozen Campaign 24 message** ("They sent the Leviathan against the Frozen pass") while bosses appear only in the Finale | XII vs Campaign §2 | Replace it, or allow that the *lineage* Leviathan (a capital hull) appears there. If so, the naming collision gets worse (A11). |
| 17 | Med | **The theater "enemy vehicles"** (wagons, mule carts, camel caravans, dirigibles, crystal golems) vs a fleet grown from Mystwood with grey-green sails | GDD theater cards vs V, image prompts | Every enemy is grown Mystwood, skinned for its theater: root-hulls that crawl on land, bladder-sails that ride the sky-currents, hulls that swim lava in a skin of wet bark. No horses, camels or propellers. |
| 18 | Med | **Theater vs city mismatches:** "Crystal *spire*" that caught the sun vs "Crystal *Depths*", an underground cavern; "Volcanic *forge*" vs "Volcanic *Isle*"; "Frozen *outpost*" vs "Frozen *Citadel*"; "Sky *tower*" vs floating islands; non-harbour cities (Mountain, Desert, Sky) called "harbour-cities" | I vs GDD theaters | The spire fell into the depths: the Crystal Depths are the spire's own cellars, laid open when it collapsed ("collapsed in a single night"), which suits the "collapse" DMZ. Call the set "the ten havens" (a haven need not be a sea harbour: a river-haven, a sky-haven). |
| 19 | Med | **Where are the battles?** Rivenkeep is "in the mountains", "high ridges", yet battles are fought on ten theaters, including the Coastal harbour | VI, X vs GDD | Two readings: (a) each battle is a sortie *out* from Rivenkeep to hold and retake the fallen havens ("vowed... to reclaim every stone"); this is a **nostos** frame (B2.2), recommended. (b) The theaters are "Rivenkeep's approaches" (journal 04-09). (a) fits "one Mystarch for each harbour-city". |
| 20 | Low | **The coda's engraver** is "seasoned young", "the words of his youth" | X | Unclear who or when. Either the **Last Carver** (C2) or remove. |
| 21 | Low | "Bones of the emissary **washed ashore**" vs the Aelvaren "**beached before the council-hall**" | V vs IV | Unify: the Aelvaren beached, and the bones were in it. |
| 22 | Low | "**Ghost fleet**" appears once and is never explained | VI | Either establish it (hulls with no crew, hence "ghost") or drop it. It fits #4. |
| 23 | Low | **The Mystarchs** were made "from the last living pillars of the barrier". Growing them would itself have **finished killing the fog** | V | Not a contradiction but an *unexploited tragedy*: the Mystaeri spent their own sky on vengeance. Say it. |
| 24 | Low | Rhyna's "**ancestor-grandfather and mother**" is an unclear kinship | VII | "Her foremother and forefather, Aetherbonded" (and Halvard's line too: the ancestor pair could be *both* of theirs). |
| 25 | Low | Rhyna is said to "lead" the Stonewrights (journal) but the legend never says so; there is no male title "Elder" | journal vs I, VII | Rhyna and Halvard lead together as Elder and Elderess. |
| 26 | Low | The legend's ship roster is old (Mortar Ships, Torpedo Boats) | V vs Campaign §5 | Refresh when the roster is locked, or keep the tale's list deliberately archaic (the Rivenmen's own names for hull-kinds). |
| 27 | Low | "The Commander" (the player) and "the Commander's torn cloak" | VII–X | Keep the Captain **unnamed**, which is recommended since the player is the Commander. The Odyssey withholds its hero's name at the opening and uses epithets; do the same. |
| 28 | Low | Doctrine in the narrator's voice ("Their union was designed by God") | I | verified_brief -6: move belief into the characters' voices ("they held that God had joined them") if broader reach matters. This is Jack's call. |

---

# PART B — MYTHCRAFT GUIDE: "LIKE TOLKIEN, LIKE THE ODYSSEY" (WITHOUT COPYING EITHER)

*Rule zero: take their methods, never their sentences. Do not quote or closely paraphrase any line of Tolkien or of any Homer translation (translations are copyrighted even though Homer is not). Do not borrow their invented names or words (no Elvish or Dwarvish roots, no "Minas-", "-ost", "Gondo-"), and do not imitate their famous openings. Everything in the example sections below was written for this document.*

## B1. What is awkward now (diagnosis with evidence)

The story elements are sound. The *telling* stumbles in eight repeatable ways:

| # | Problem | Evidence from the legend | Rule |
|---|---|---|---|
| 1 | **The narrator explains instead of showing** | "It was a sacred ritual beyond all measure." · "It is the sorrowful heart of the myth" · "These unions were not mere marriage" | Show the act; let the reader feel its weight. Cut every sentence that tells the reader how to feel. |
| 2 | **Modern, bureaucratic or colloquial diction** | "leverage in the Trade Council", "decadence", "henchmen chuckled", "bleeding profusely", "tentatively reached", "cynosure", "Neutralized", "a fancy", "no sequel" | Use plain old words (B3 lists). A modern word is allowed only inside a character's mouth, and only when the lie or the pettiness is the point. |
| 3 | **Abstract coinages carrying doctrine** | "ordination tendrils that predated this mortal life", "Covenants of Completion", "guardians of absolute truth" | Replace abstraction with an image or a custom: *what did the seers do?* Did they read the cradle-stones, lay the infants in one cradle, cut one mark in two foundation stones? |
| 4 | **Em-dash dependence** | 60 em-dashes in 4,288 words (about 1 per 70 words); many sentences hinge on a dash-aside | At most one dash per paragraph. Mythic prose runs on *and*, *but*, *for*, *so*, *then*, not on asides. |
| 5 | **Fragments and restarts** | "A land of mountains and high hills that tumbled down to meet the restless sea." (a fragment) · "wonderings, pondering, in the deep watches of the night" | Whole sentences. Parataxis is not fragmentation. |
| 6 | **Everything at one volume** | Every paragraph is intense; there is no quiet before the murder or the cry | Vary the register: annal (cool, dated, brief) → tale (scene, dialogue) → lay (song) → reading (fragment). Quiet makes the loud moments land. |
| 7 | **One omniscient chronicle trying to hold everything** | Twelve chapters in a single voice, from the cosmology to the battle-message spec | Break it into **tales with tellers** (B8). Each tale may be partial, biased, or contradicted by another, and that is a feature. |
| 8 | **Meta-leaks** | "Thus ends the legend. There is no sequel", "XII. Battle Messages" inside the legend, "the player" in XI | Keep all design talk outside the tales. |

## B2. What to take from each master

### B2.1 Tolkien's high mythic register (the *Silmarillion* mode, not *The Hobbit*)

1. **Annalistic narration.** Events are set down as an annal would record them: by years, ages and reigns, reported rather than dramatised, and then suddenly one scene is dramatised in full. Most of the legend should be *told at a distance*; only a few moments are *shown up close* (the Ael'thar, the cloak on the wall, the reading of the sliver). Distance is what makes it feel old.
2. **"And"-chains (parataxis).** Clauses are joined by *and* rather than subordinated with *because*, *although* or *which*. The effect is scriptural and inevitable: things happen *and* then other things happen, and the reader supplies the causality. Use *for* ("for the wood remembers") as the main causal word.
3. **Measured archaism.** A little goes a long way. Allowed: inversion now and then ("Great was the grief of the groves"), *ere*, *thereafter*, *wrought*, *kin*, *doom* (meaning fate or judgement), *wise* (meaning manner, as in "in no wise"), *save* (meaning except). Avoid: *thee/thou/thy* in narration (use them only if a people's speech is established to use them), *-eth* verbs, *verily*, *forsooth*. Never mix a high archaism and a modern word in one sentence.
4. **Concrete imagery.** Tolkien's mythic prose is full of *things*: light, trees, stone, water, stars, particular colours and metals. Every abstraction should be pinned to a noun the reader can see: the black bark of the Mystholders, the grey-green sails, the ashlar cap of the staff, the crimson pennants, mortar in the Captain's knuckles.
5. **Names and genealogies.** People are placed by their line ("X son of Y, of the house of Z"); places are named, renamed, and named again in other tongues. A genealogy is itself a kind of story, and the reader trusts a world that remembers its dead. Give Rhyna and Halvard a line, and give the ten havens names (B7).
6. **Songs and lays embedded in prose.** A tale pauses for a few lines of verse "as it is sung" and then resumes, sometimes noting that the song and the tale disagree. This lets the rewrite hold Jack's best lines (the cry, the banner) as *songs the Rivenmen sing*, not as narration.
7. **The long defeat.** Victories are real but local and costly, and the tide of the world runs toward loss. Each triumph is shadowed by what it cost or what it cannot undo. The legend already has this ("humility came too late"); keep it as the ground note.
8. **Eucatastrophe.** Tolkien's own term (from his essay on fairy-stories) is the sudden, unlooked-for turn toward good, at the very edge of ruin, that does not deny sorrow. The **living sliver of green Mystwood** is exactly this: hope where none was looked for. Stage it as a turn, not as a footnote.
9. **Tales attributed to tellers and books.** The mythology presents itself as *transmitted*: set down in an old book, told by a named loremaster, translated, sometimes in variant versions. It is never presented as the author's truth. This is the fix for doctrine-in-the-narrator's-voice (A12 #28): belief is reported as what the Stonewrights held and wrote.
10. **Many names for one thing.** A person or place carries an exonym, an endonym and an epithet. Here, "Mystholders" is the Shoreland word, and the Mystaeri have their own word, revealed late (C10).

### B2.2 The Odyssey's structure

1. **Tales within tales, told at a hearth or feast.** The hero's own wanderings are told in the first person, at a king's table, long after they happened. A bard sings earlier deeds at the same feast and the hero weeps to hear them. The listeners interrupt, and the telling is itself an event. **For Rivenkeep:** the tales are told at Rivenkeep's hearth *between sorties*, in the Build/Deploy hours. The teller is present, the listeners are soldiers and refugees, and sometimes the teller weeps.
2. **In medias res.** The poem opens deep in the story and reaches back. **For Rivenkeep:** the game opens with the siege already on. The first tale the player hears should be the cloak on the wall, not the elder days. Cosmology arrives later, as memory.
3. **Epithets.** Short fixed tags recur whenever a name returns. They are formulaic and they help the listener. **For Rivenkeep:** give each principal a fixed epithet and repeat it without variation (bank in B4).
4. **Catalogues.** A list sung in full is a monument: of ships, of heroes, of the dead seen in the underworld. **For Rivenkeep:** the catalogue of the ten havens (their founding, their fall, how long each held) is the natural "Book of the Havens". A catalogue of the tides of the fleet is its Mystaeri mirror.
5. **Nostos (homecoming).** The whole poem is the long road home and the reclaiming of a house held by others. **For Rivenkeep, doubly:** the Rivenmen vow to reclaim every haven ("a name to return to, perhaps, when the last wall stood"), and **the Mystaeri line, "We remember our home too," is their nostos.** Their home is the thing *they* can never go back to. Two homecomings, one of them impossible.
6. **Xenia (guest-friendship) and its violation.** The poem's moral law is the law of the guest. The host must receive the stranger who comes to his door, feed him, and give gifts; the guest must honour the house. The worst villains violate it: the monster who eats his guests, and the suitors who devour a host's house. Such violation draws the wrath of the powers.
   - **The Ael'thar murder is a xenia crime in its purest form.** A lone stranger comes *through the sea to a threshold*, kneels, and offers the most precious gift his people know. The host kicks the gift into the dust, *laughs* (the henchmen "chuckled"), and kills the suppliant at his own door. Then he burns the guest's ship to hide it and *lies to his own people* in his report. The Mystaeri response, a war of generations, is the wrath that follows. **Name it in the text as the breaking of guest-right,** a law older than either people ("there is no older law among any people"). The tragedy deepens because the Shorelanders, a people of houses and doors, broke the law of the door.
   - **The resonance of the self-sailing ship:** in the Odyssey, a people's ships sail themselves home by knowledge of the way, and one such ship is turned to stone as it comes into harbour. Rivenkeep already has both halves: the **Aelvaren sails itself home**, and **petrified Mystwood is wood turned to stone**. This is a resonance to *know*, not to reproduce. The rewrite should not stage a ship turned to stone. (If Jack wanted a deliberate echo, the petrified gift's origin could be "the heartwood of a ship that came home too late", but that is optional and should be his decision.)
7. **Recognition by a token.** The hero is known by a scar, a bow, or a secret of the marriage-bed. **For Rivenkeep:** the half-made Ael'thar left **one scar**, on the outpost warden's right arm. It is the only mark the rite ever made on a Shorelander. The token could return (an heirloom account, a descendant, a skeleton in the outpost's ruin with a scarred arm bone). Also: an Aetherbonded pair is recognised because each knows what the other is thinking. That is a recognition test no impostor can pass, and it is a tool for a Mimic-era tale.
8. **The bard inside the story.** A singer at the feast performs the same material the poem is made of. **For Rivenkeep:** Seren, or a True Man who sings, is the in-world bard, so the lays can be attributed.

### B2.3 How the two combine

**Tolkien gives the voice; the Odyssey gives the frame.** Each individual tale is told in the grave, annalistic, concrete Silmarillion register, and the collection is arranged Odyssey-fashion: told at a hearth by named tellers, out of chronological order, with songs, catalogues and epithets, and centred on homecoming and the broken law of the guest.

## B3. Rules of the register (the working checklist)

**Sentences**
- The default is a medium-long sentence of two or three clauses joined by *and / but / for / so*. After every three or four such sentences, drop one very short sentence. The short sentence carries the blow ("His men obeyed." is good in the current text; keep that instinct).
- At most one em-dash per paragraph; prefer commas, semicolons and *and*.
- Put the verb early. Avoid stacked prepositional phrases and "the X of the Y of the Z".
- Rhetorical repetition (anaphora) is allowed at climaxes, and **only** there ("They had never known battle. He had never known patience." is a good example).

**Words.** Prefer these, and avoid their counterparts:

| Prefer | Avoid |
|---|---|
| kin, folk, host, guest, doom, lore, craft, hold, haven, hythe, ward, mark, oath, the wise | leverage, commerce (in narration), decadence, henchmen, profusely, tentatively, cynosure, neutralized, intel, strategy, logistics |
| wrought, hewn, laid, set, raised, felled | constructed, utilized, implemented |
| the grey sails, the black pillars, the torn cloak | abstract nouns in *-ity*, *-tion*, *-ness* doing the work of images |
| "they held that…", "it is said that…", "the Stonewrights write that…" | the narrator asserting doctrine as fact |

**Voices**
- **Narration (the tales):** high register, as above.
- **The Stonewrights speaking:** grave, craft-metaphor, antiphonal when the pair speaks (one begins, the other completes, B9).
- **Soldiers (battle messages, campaign cards):** plain, concrete, sometimes funny, never modern. Tolkien's plain-spoken characters and the Odyssey's swineherd show the model: common speech that is still of its world. Humour comes from character, not from anachronism.
- **The Mystaeri (readings of the wood):** short imperatives and images, no articles in the early readings, rhythm like a carved line (C3).

**Content**
- Keep every piece of design vocabulary (sortie, AoR, Build, heptomino, campaign numbers) out of all in-world text, except "sortie", which is a real old military word and may appear in soldiers' mouths.
- Keep faith in characters' mouths and books (B2.1 #9). The source is Jack's; the framing choice is his (A12 #28).
- Every tale must be readable alone, in about 250–600 words, and understandable without the others. That is the Odyssey's episodic principle and the practical constraint of a codex.

## B4. Epithet bank (original; fix one per figure and repeat it)

| Figure | Fixed epithet (primary) | Alternates (for songs only) |
|---|---|---|
| The Captain / Commander | **the Captain of the Torn Cloak** | he who would not carry the staff; the mortar-handed |
| Elder Halvard | **Halvard Stone-Warden** (from his name's meaning) | the gate-keeper of the high ridge |
| Elderess Rhyna | **Rhyna of the Inner Gate** (her line's capstone) | the chisel-lifter |
| Halvard and Rhyna together | **the Bonded of the Keep** | the two who are one |
| Seren | **Seren Reader-of-Wood** | the patient hand |
| The True Men | **the oath-keepers** | the few who built what they promised |
| The Mystaeri | **the long-lived**, **the mist-folk** | the thunder-tongued |
| The emissary | **the Kneeling Guest** | the bearer of the gift |
| The outpost's warden | **the warden who laughed** | the lordling of the outpost |
| The Aelvaren | **the Bearer of the Binding** (source) | the ship that went home alone |
| The Mystholders | **the black pillars of the fog** | the anchors of the sky |
| The fleet | **the grown fleet**, **the grey-sailed** | the doom of the dead |
| The Mystarchs | **the thrones that walk the sea** | the last pillars |
| Rivenkeep | **the Keep that was Forgotten** (before), **the riven hold** (after) | the castle that had never fallen |
| The sea at the fog's edge | **the grey-walled sea** | — |

## B5. Before → after (rewriting Jack's own lines; same content, new register)

1. **Before:** "The Stonewrights recorded its blackish veil in their oldest archives as wonderings, pondering, in the deep watches of the night, what hidden truths it guarded."
   **After:** "In the oldest archives of the Stonewrights the fog is written down only as a question, asked in the night-watches and never answered."
2. **Before:** "He had been given his post not by merit but by his father's leverage in the Trade Council, and when his rash temper proved dangerous in civilized company, he was banished to the outermost edge of the realm where he could do no further damage."
   **After:** "He held the outpost by his father's name and not his own; for his temper had made him unwelcome in the cities, and the Trade Council had sent him to the last edge of the land, where there was no one left for him to wound."
3. **Before:** "Their union was designed by God, with ordination tendrils that predated this mortal life."
   **After:** "The Stonewrights held that God had joined each pair before either drew breath, and that the seers did not choose but only read what was already written."
4. **Before:** "His report was a coward's lie: 'Unknown intruder. Hostile intent. Neutralized. Vessel burned and released.'"
   **After:** "And he sent word to the cities in the cold speech of clerks: *A stranger came armed and was slain. His boat was burned and put to sea.* No word of the gift was written, nor of the kneeling." (Here the flat official register is deliberate: the lie *sounds* different from the tale.)
5. **Before:** "Thus ends the legend. There is no sequel, no easy healing. Only the weight of inherited sorrow, as it has since the world was young."
   **After:** "Here the tale ends, but not the grief of it; for grief is an inheritance, and it is paid out to the children."

## B6. Original example sentences in the target register (15)

*All written for this guide. The names Orlen and Ysa are placeholders.*

1. *(Annal opening)* In the years when the ten havens were young and their stones still smelled of the quarry, the grey came up against the Shorelands every morning and went back every evening, and no one asked what lay behind it.
2. *(And-chain, the Bond)* And Halvard set his hand upon the gate, and Rhyna set hers beside it, and neither spoke, for the bonded have no need of speech; and the stone, which had been cold for nine lives of men, grew warm beneath their palms.
3. *(Genealogy)* Rhyna was the daughter of Orlen and Ysa, who were bonded in one cradle, and her foremothers had laid the capstone of the inner gate; and Halvard was of the quarry-wardens of the high ridge, whose names are cut in the lintel of the western stair.
4. *(Concrete image)* The Mystholders stood in their ranks at the fog's edge like the pillars of a hall whose roof was the mist itself, black of bark and straight as a plumb-line; and where one was felled the bare sky showed through, as daylight shows through a rent in a sail.
5. *(Xenia named)* He came with his hands open and his gift before him, and knelt on the salt-stones of the outpost as a guest kneels at a hearth; and there is no older law among any people than this, that one who kneels at your door is under your roof.
6. *(The long defeat)* So the counsel of the Stonewrights was heeded at last, but it was heeded in the years of ash, when there was nothing left to save by it.
7. *(Mystaeri council, from the wood's side)* *Grow until the shore is silent,* the council carved into the heartwood; and the wood, which cannot unlearn what is carved in it, grew.
8. *(The tides, the Ender's Game ordering)* The first ships that came against Rivenkeep were the first that had been grown, green and hasty, carved by angry hands in a single season; they came each alone, as hounds come that are loosed before the hunter, and they broke upon the new walls. But wood remembers, and the wreck-wood went home on the tide.
9. *(Epithets in action)* Then Halvard Stone-Warden took up the chisel, and Rhyna of the Inner Gate took up the mallet, and the oath-keepers on the wall saw the two tools lifted as one, and took heart.
10. *(Embedded lay; an original quatrain)*
    > *Stone upon stone, and the stone remembers;*
    > *hand upon hand, and the hand holds true;*
    > *two at the gate when the grey fleet gathers,*
    > *two at the gate, and the gate stands through.*
11. *(Attribution to a teller)* This is the tale as Seren Reader-of-Wood set it down from the carvings of the sunken hulls; and where the carving was broken she has said so, and has not mended it with guesses.
12. *(Mystaeri point of view: what the wood can and cannot know)* In the groves beyond the fog the Mystaeri laid their hands on the charred keel of the Aelvaren and read there the whole of it, the gift refused, the blade that slipped, the fire; but they did not read the warden's fear, for fear leaves no mark on wood.
13. *(Catalogue)* First fell the eldest haven by the sea, whose harbour burned between a dawn and a dusk though its walls held three months after; and then the city where the river meets the tide; and then the fen-town on its sinking stones, that had been sinking since its founding and now went under all at once.
14. *(Eucatastrophe)* And the sliver was green. Of all the things the Rivenmen had searched for in the long years of the siege, no one had searched for that; and Rhyna wept, and Halvard did not, for she was weeping for them both.
15. *(Measured number, lore as dispute)* Eight days, men say, is the longest that ever the bonded lived apart after one had died; but the Stonewrights say it was hours, and they should know, for they keep the count.

## B7. Naming kit

**Shoreland / Rivenmen (stone, craft, Northern-European).** Existing names: Rhyna, Halvard, Seren, Hale, Voss, Kael, Rivenkeep. The rule: English or Norse-sounding roots that *mean* something in craft or stone; compounds for places (as Tolkien used Old English for one of his peoples, choose one real-language palette and hold it). Useful roots: *hythe* (landing), *holm* (islet), *holt* (wood), *carn* (cairn), *mere* (lake), *rime* (frost), *ward* (guard), *stane / stan* (stone), *reach*, *mark*. Personal names should be short: two syllables, often ending in *-a, -en, -ard, -el, -wyn*.

*Working names for the ten havens (proposals for Jack's approval; each with a fixed epithet):*

| Label | Working name | Epithet |
|---|---|---|
| Coastal city | **Eldhythe** | the Eldest Haven, whose harbour burned in a day |
| River city | **Tidesmeet** | where the river meets the tide |
| Swamp settlement | **Fenholm** | the town that was always sinking |
| Forest keep | **Holtward** | the keep under the canopy |
| Mountain stronghold | **Carnhold** | the stronghold of the cairns |
| Volcanic forge | **Emberhythe** | the forge on the burning shore |
| Desert citadel | **Sandreach** | the citadel carved in the canyon wall |
| Frozen outpost | **Rimewatch** | the watch on the frozen mere |
| Sky tower | **Highreach** | the tower of the floating stones |
| Crystal spire | **Glasspire** | the spire that fell into its own cellars |

**Mystaeri (the thunder-tongue and the wood-tongue).** Existing words: *Ael'thar* (the rite), *Aelvaren* ("Bearer of the Binding"). Everything "Myst-" (Mystaeri, Mystwood, Mystholder, Mystarch, Myststone) is best read as **Shoreland exonyms**, the builders' names for the mist-folk's things. That is realistic and opens a reveal (C10).

- *Proposed mini-lexicon, derived from the existing words:* **ael** = bond, joining · **thar** = blood · **varen** = bearer · **'** (the apostrophe) = the *thunder-break*, the hard crack in the spoken word that the wood-writing smooths away. So *Ael'thar* is "bond-blood" spoken; written in wood it becomes a soft, unbroken word.
- *The two registers resolve A12 #9.* **Spoken:** hard stops (k, t, d), apostrophe breaks, short words ("thunder"). **Carved:** vowel-rich, flowing, unbroken ("gentle"). One language, two faces.
- *Phonology:* ae, ei, ea; th, v, l, r, s, n; the apostrophe only in spoken forms; no z, x or q; avoid Sindarin-looking endings (-ion, -iel, -dor).
- *Mystarch true names:* give each Mystarch a spoken name and a carved name; the Rivenmen keep their beast-names as fear-names, provided the lineage collisions are resolved (A11).
- *Jack's "shore men":* a candidate for what the Mystaeri call the Shorelanders, as a translated epithet that surfaces in the readings: **"the stone-deaf"** or **"the shore-men who do not hear"**. It is a Mystaeri word, not canon, and depends on Jack.

## B8. The architecture of the collection: a Book of Tales told at the hearth

**The thematic spine (state it in the first tale, and let every tale bear on it):**
- **Two made one.** The Aetherbond (two Shorelanders made one) and the Ael'thar (two peoples made one front) are one idea, seen from two sides of the fog. The Shorelanders perfected it at home and could not recognise it at their own door. Rhyna and Halvard are the image of what was refused; the fleet, coordinating without words, is a dark mirror of the bond.
- **The wood cannot lie; the stone cannot speak.** Each people trusted a medium the other could not read.
- **Two homecomings.** The Rivenmen fight to go home. The Mystaeri remember a home they can never return to.
- **The long defeat, on both sides.** The Shorelanders' pride and the Mystaeri's rage are both true ("Both are true. Build the wall.").
- **The broken law of the guest** is the first cause of the war.

**The tellers (every tale is attributed):**
| Teller | Book | Register |
|---|---|---|
| **Halvard and Rhyna** (antiphonal, often one tale in two voices) | *The Book of the Cornerstone*: the Stonewright annals | annal + tale |
| **A True Man** (a named oath-keeper; could be Sergeant Kael) | *The Tales of the Wall*: soldiers' tales of the Captain | tale, plain-spoken narrator |
| **Seren Reader-of-Wood** | *The Readings*: translations of wreck-carvings | fragment → fluent (C3) |
| **The Wood itself** (the petrified gift, then the living sliver) | *The Telling of the Wood* | the Mystaeri side, first person plural |
| **Sung (anonymous)** | *The Lays of the Riven Stone* | verse |

**Proposed tale list (each 250–600 words, standalone). The source chapter each absorbs is shown in the last column.**

| # | Tale | Teller | Form | Absorbs |
|---|---|---|---|---|
| 1 | **The Torn Cloak** (open in medias res) | a True Man | tale | VII (the Captain, the banner) |
| 2 | **The Cry of the Bonded** | Halvard and Rhyna | tale + lay | VII (Rise, Stonewrights!) |
| 3 | **Of the Keep that was Forgotten** | Halvard and Rhyna | annal | VI (Rivenkeep found in ruin) |
| 4 | **The Rite of the Cornerstone** | Halvard and Rhyna | tale | VIII |
| 5 | **The Book of the Havens** (catalogue of founding and fall) | Halvard and Rhyna | catalogue | I (cities), VI (the Fall) |
| 6 | **Of the Bonded and the Theoliths** | Rhyna, then Halvard | annal | I (Aetherbond, Theoliths, the eight days) |
| 7 | **The Kneeling Guest** (the broken Ael'thar) | Seren, from the wreck-carvings + the petrified wood | tale | IV |
| 7b | **The Wanderings of the Gift** (how the petrified wood came to Rivenkeep) | Rhyna | tale | new (A12 #12) |
| 8 | **The Voyage of the Aelvaren** | the Wood | telling | IV (the ship goes home) |
| 9 | **The Felling of the Black Pillars** | Halvard (with the archive warnings) | annal | III (pride, harvest) |
| 10 | **The Mute Stones** (the warnings that stone could not carry) | Seren | reading | III |
| 11 | **The Council of the Fading** (the vote of the young) | the Wood | telling | V |
| 12 | **The Growing of the Tides** (the Ender's Game ordering) | the Wood / Seren | telling + catalogue | V (fleet grown) + new |
| 13 | **Of the Stonwryt** (the vow in the foundation) | Halvard | annal | I (Stonwryt) |
| 14 | **Of the Mistlands and the Wood that Speaks** | the Wood | telling | II |
| 15 | **The Naming of the Rivenmen** | a True Man | tale | IX |
| 16 | **The Thrones that Walk the Sea** (the Mystarchs in the havens) | Seren | reading | V (Mystarchs) + A12 #2 |
| 17 | **The Reading of the Green Wood** (eucatastrophe) | Halvard and Rhyna | tale | IX (the sliver) |
| 18 | **The Last Carver** (coda, optional) | the Wood | telling | X (the engraver) |

Chronological order is not play order. The Odyssey starts late and reaches back, and the play order in C5 does the same.

## B9. Halvard: integration checklist

Every passage where Rhyna acts alone in the source must be reworked so the pair acts together. Aetherbonded pairs "lived, worked, and worshipped as one" and felt each other's pain and thought.
1. **VII, ancestry:** "her ancestor-grandfather and mother laid the capstone" should become the capstone laid by an Aetherbonded pair from whom *both* descend, or one line each (Rhyna of the capstone, Halvard of the quarry-wardens).
2. **VII, the cry:** make it an **antiphon**. Rhyna calls: "The mortar cries out from the ground." Halvard answers: "Rise, Stonewrights!" Rhyna: "Lay stone upon stone." Halvard: "Stand every wall to the very end." Then both: "Rise! Rise! Rise!" Jack's words are kept exactly and redistributed. The call-and-response *is* the bonded's way of speaking.
3. **VIII, the Rite found:** "Halvard and Rhyna found". Note the Aetherbond's shared thought: one found the vault, the other knew where to look.
4. **VIII, the Anointing:** already "together"; name him.
5. **IX / XI, the petrified wood:** "Rhyna held the petrified wood for an hour" becomes both hands on it; or Rhyna reads while Halvard *feels* her reading; he hears the voice through her.
6. **IX / XI, the living sliver:** both touch it. "We remember our home too" is heard by both at once.
7. **XI:** "Rhyna says…" becomes "The Bonded say…" or "Halvard says, and Rhyna finishes…".
8. **Seren** is "their apprentice".
9. **Easter egg "Rhyna's Blessing"** becomes **"The Blessing of the Bonded"** (or "Halvard and Rhyna's Blessing").
10. **The Aetherbonded die together.** An optional last tale: the Bonded of the Keep die in the same hour, perhaps the night the sliver is replanted. It is the one death in the legend that is not a defeat.
11. **Mechanical echoes (optional, from verified_brief -6):** the dual piece draw as "the pair"; a Stonewright Post drawn as two figures; the "twelvefold" multiplier as the in-world reason Stonewrights rebuild so fast between volleys.

---

# PART C — WEAVING THE STORY INTO PLAY

## C1. Principles (from Jack's vision and the verified review)

1. **Cosmetic and off the sim path, always.** No tale, reading or message changes any number, spawn or behaviour. The sim stays deterministic ("if two people play EXACTLY the same, they would get the same outcome").
2. **Low-load moments only.** The Why sets an attention budget of ≤4 decision-bearing contacts and ≤3 live approaches. Lore must not compete with play. Tales go on the debrief, between campaigns, at battle load, and at the Last Stand's end (verified_brief -5), never in a live Fight and never in timed Build.
3. **No forced playstyle.** No tale or reading may be unlockable only through one trick (e.g., only by feinting). Every unlock is reachable by the blunt route as well. Honouring the creed ("Protect, do not attack") is welcome only as a *bonus* flavour, never as a gate.
4. **Legibility is earned, not declared.** The story's biggest job is to be the *after-the-fact explanation* of the fleet's mind (C3). It must be truthful: a reading reports what the fleet actually followed, generated from the sim's own record.
5. **The fleet should feel like another mind.** Jack's vision #2: "working together but also independent... they recognize the strategy and they can counter it." The fiction supplies the commander the fleet lacks: the carved orders, the standard-bearer, the Mystarchs and, optionally, the Last Carver.

## C2. The Tides: the Ender's Game ordering as fiction for the cognition ramp and the stratagem ladder

**The premise, in one paragraph.** The war-council did not grow one armada; it set the groves growing and **sent each ship as soon as it was ready**. The first ships were the youngest wood and the hastiest carving: made in one season by angry hands, each hull alone with a single order. They sailed first and arrived first. Behind them the groves kept growing, slower and deeper, and **the wood remembers**. Every wreck that drifts home, as the Aelvaren once did, is read by the groves, and the next ships are carved with the lesson. So the Rivenmen meet a fleet that begins as a mob and becomes an army. **No living hand recalls it and no living hand needs to guide it: "The wood obeys the wood."** This explains three things at once:
- the cognition ramp (Campaign §4);
- survivors retreating and "re-emerging... a cognition-tick smarter" (Victory §4): the hull has *felt* the wall;
- why the fleet cannot be recalled but can be turned (A12 #13).

**The stratagem ladder's story scaffold.** Jack asked for 6–8 stratagems per game period, overlapping, with simple ones building into complex ones. The carvings are those stratagems. A simple carved order is a *glyph*. Glyphs compose into *phrases*, phrases into *sentences*, sentences into *conditions*, and conditions into *deceits*, exactly as simple stratagems compound into late ones. The number of periods is not fixed at five; this scaffold uses the GDD's six stage groups.

| Stage (GDD) | Campaigns | Tide | Grown / carved by | Carving grammar | On the board (cognition ramp) | What the Readings can show |
|---|---|---|---|---|---|---|
| Introduction | 1–6 | **The Hasty Tide** | young wood, one season, the council's anger | **single glyphs**: "Burn." "To the shore." "Break the wall." "Follow the standard." | naive: short sight, fast forgetting, trusts stale fixes; one approach; ships "not organized" (Jack) | fragments only; Seren can read one sign in three |
| Pairs | 7–16 | **The Second Tide** | wood of a generation; the first wreck-lessons | **phrases (two signs)**: "Around the loud stone." "Screen the bearer." "Strike, then run." | pairs and screens appear; decapitation becomes discoverable (5–8 guns); Provocateur and Corsair debut | short phrases, with gaps |
| Triples | 17–26 | **The Tide of Remembering** | the groves reading many wrecks | **sentences, with a memory clause**: "Where the stone fell silent, look before you trust." "Go where they have not yet built." | verification over trust; longer sight; Wraith (fog) debuts | whole sentences, with doubtful words marked |
| Quads | 27–31 | **The Tide that Learned Deceit** | the groves, having read the Rivenmen's feints | **true orders to deceive** (the wood still cannot lie): "Show fear where you are strong." "Let them see the bearer where it is not." | anticipation; Mimic, "the fleet baiting back", debuts | fluent; Seren's horror that they learned it from us |
| Full Stack | 32 | **The Last Tide** | everything the wood has learned | **conditions nested in sequences**: whole battle-plans carved in the flag-hull | at the top of every legible band | fluent, and sometimes signed (the Last Carver) |
| End Times | Boss Finale | **The Thrones** (Mystarchs) | the eldest Mystholders, the last pillars of the sky | **judgements**, not orders: each Mystarch carries the grief of one haven and the name of the wrong it avenges | set-pieces, fanatical top of the resolve dial | the true name of the Mystarch and of the haven it holds |

**The tragedy inside the ladder.** The Mystaeri spent their own sky to make the Thrones (A12 #23). The wood that could not lie learned deceit from its enemy (Quads). This is the long defeat for *both* peoples: the war makes each side more like the other.

**The optional commander: "the Last Carver".** Jack's vision #2 asks that the enemy feel "like there is another human running" it, and the prior review found the fleet has "good soldiers but no commander". In the fiction, late in the war a living Mystaeri, one of the few young who still tend the groves, begins to sail with the fleet and **re-carve orders in the field**. Mechanically this changes nothing; the sharp late cognition is already in the ramp. In the story, the player's sense that "someone is answering me" is *true*. The coda's "seasoned young Mystaeri" (X) becomes him: young by his people's span, seasoned by the war. He may be the voice of "We remember our home too." It works as a late reveal in the Ender's Game spirit (the other side was a person all along). This is optional and needs Jack's decision.

## C3. The Reading: carved orders as the after-the-fact explanation

**What it is.** On the debrief after each battle, and optionally after a sortie, a single line appears: *the carving read from the flag-hull, or from wreck-wood of the formation that hurt you most*, in Seren's translation. It is generated deterministically from what the fleet *actually did* (the stratagem or next-sortie plan the sim executed; Fleet Memory §5, §12). It is therefore a truthful, retrospective tell: the player learns *what the mind was doing* in the fiction's own voice.

**Fidelity rises with the war.** This mirrors the emissary's broken words, since now the Shorelanders are the ones fumbling with fragments:
- **Hasty Tide (1–6):** "…shore… fire… first…" *Seren: "Three signs, and I am not sure of the third."*
- **Second Tide (7–16):** "Around the loud stone." *Seren: "They went where our guns were not. The wood says they were told to."*
- **Tide of Remembering (17–26):** "Where the stone fell silent, look before you trust." *Seren: "They remember the gun you moved. They came to see whether it was still there."*
- **Tide that Learned Deceit (27–31):** "Show them fear in the east." *Seren: "The wood does not lie. It was told to make us believe a lie, and it obeyed."*
- **Last Tide (32):** "When the bearer falls, the second takes the standard; when the second falls, go home." *Seren: "They have carved their own defeat into the plan. They know us now."*
- **Thrones (Finale):** the Mystarch's true name, the haven it holds, and the wrong it carries.

**Design rules for the Reading:**
- It is always true. It is never a hint about the *next* battle, only an explanation of this one; that protects the "earned, not declared" law.
- It names the stratagem in fiction terms. The codex can show the plain-language gloss beside it ("the fleet avoided your firing zones").
- It never grades the player and never nags. It is the enemy's side of the story.
- Readings collect in the codex as **the Readings of Seren**, one per stratagem, filling the Mystaeri half of the tales (C6).

**The fleet's mind, named in the fiction (so Readings and tales use one vocabulary):**

| Mechanic | Fiction |
|---|---|
| LOS channel (sight) | *the wood's sight through the mist* |
| Contact channel (memory of exposed guns) | **the wood remembers where it was struck** |
| Effect channel (fear grid, "haze") | **the dread of the wood** / Mystaeri fear |
| Next-sortie plan | **the carving for the morrow** (made in the Build/Deploy hours, "both minds think at once") |
| Flagship | **the Standard-Bearer**, the hull that carries the carving; "the captain of the team" |
| Field promotion | *the standard passes*: the wood carries the carving to the next hull, but the new bearer is "a lieutenant standing in" |
| Resolve network / contagion | **the bond of the fleet**: the pain of one hull is felt by its neighbours, a dark mirror of the Aetherbond |
| Motion signature (Committed / Wavering / Routing) | *the lean of the hulls*: the wood leans toward the shore, or away |
| Rout / retreat | **the wood goes home**, turned but never recalled |
| Survivors return a tick smarter | *the wood that felt the wall* |
| Ammo as diegetic clock | *the fleet has spent its fire* |
| Purpose collapse ("out for revenge") | *the orphaned hulls*: the carving lost, only the grief left |

## C4. Tales unlocked by campaign (play order ≠ chronological order)

| Unlock | Tale(s) (from B8) | Why here |
|---|---|---|
| First launch / tutorial | 1 The Torn Cloak | In medias res: the player *is* the Captain |
| Cam 1 complete | 2 The Cry of the Bonded | the Stonewrights join; Build explained in fiction |
| Cam 2–3 | 3 Of the Keep that was Forgotten · 13 Of the Stonwryt | the place and its vows |
| Cam 4–6 (end of the Hasty Tide) | 4 The Rite of the Cornerstone · 12a *The Growing of the Tides, part one* | "these ships are young and wild; there will be others" |
| Cam 7–10 | 6 Of the Bonded and the Theoliths · 5 *The Book of the Havens, part one* | a second approach, a second voice; the catalogue begins |
| Cam 11–16 | 9 The Felling of the Black Pillars · 10 The Mute Stones | humility: *we* did this |
| Cam 17–22 | 7 The Kneeling Guest · 7b The Wanderings of the Gift · 8 The Voyage of the Aelvaren | fear and guilt: the broken law of the guest |
| Cam 23–26 | 11 The Council of the Fading · 12b *The Growing of the Tides, part two* | resolve: "Both are true. Build the wall." |
| Cam 27–31 | 14 Of the Mistlands and the Wood that Speaks · 5 *The Book of the Havens, part two* | the enemy understood as a people, just as they learn to lie |
| Cam 32 | 15 The Naming of the Rivenmen | defiance |
| Each Mystarch defeated | 16 *The Thrones that Walk the Sea*, one entry per haven | nostos: each haven retaken |
| All ten Mystarchs | 17 The Reading of the Green Wood · (18 The Last Carver) | eucatastrophe and coda |

## C5. The Mystaeri side of each tale, unlocked by Readings

Each Rivenkeep tale has a **counter-telling** from the wood. It unlocks when the player has earned the Readings of the stratagems that belong to it. For example, "The Kneeling Guest" (the Stonewright telling) pairs with the Aelvaren's own telling, which unlocks after the Readings of the Tide of Remembering.

- **Unlock rules must be deterministic and playstyle-neutral:** a Reading is earned when its stratagem is *met and survived*, however the player survived it. It is never earned only by a specific counter.
- **Sinking or routing** a flag-hull both yield wreck-wood. (Routed hulls leave carvings behind in the flotsam, or the Reading is taken from the carving the fleet shouted across the water; either way both routes count.)
- **An optional creed echo:** turning a fleet back (a battle Retreat) rather than annihilating it adds a *line* of warmth to the Reading ("They went home. The wood was glad of it."). It never adds a reward.
- **The name reveal:** as counter-tellings unlock, the codex swaps the Shoreland exonym for the Mystaeri endonym ("Mystholders" becomes their own name, "the Mystaeri" becomes their own name). Understanding shows as a change of language. The Readings get more fluent at the same rate.

## C6. The 3-second battle messages, reworked

**Placement.** Show the message at **battle load or briefing, before the clock starts**, or during the 3-2-1 Map-to-World transition, rather than during timed Build (verified_brief -5). Keep the 3-second length and the 5–8 random pool.

**Voices.** A recast in-world roster (C7). Plain speech, never modern, no design vocabulary.

**The hint discipline (important for determinism and fairness).** A message may foreshadow the battle's stratagem, which makes it a *tell* in Jack's sense ("they recognize the strategy and they can counter it"). Because selection is random, **either every message in a battlefield's pool carries the same hint in different voices, or none does.** Otherwise two players get unequal information from the same seed.

**Examples (original):**
- *Coastal, Hasty Tide:* "Eight sails, and not one keeping station with another. Whoever sent these sent them in a hurry." (tell: uncoordinated) · "The Captain says the young ones hit the newest stone first. So make the newest stone the strongest." · "Salt in the mortar again. Salt holds, if you let it."
- *River, Second Tide:* "They came in pairs this morning. The front one takes the shot; the back one takes the ground." (tell: screening)
- *Forest, Tide of Remembering:* "The gun we moved last night — Voss swears the grey sails came looking for it." (tell: memory of exposed guns)
- *Frozen, Tide of Remembering:* "The lookouts counted the hulls twice. The second count was shorter. Something is sitting in the rime." (tell: Wraith)
- *Desert, Tide that Learned Deceit:* "They are frightened of the east wall. Too frightened. Kael doesn't like it." (tell: feigned fear)
- *Any, Last Tide:* "Halvard says they carve a morrow now, as we do. Then let us build a morrow they did not carve for."

**AI-dynamic lines** (GDD AI §5) keep the same register and the same hint discipline, and remain cached and cosmetic.

## C7. The voices, recast (proposal)

- **Keep the legend's core:** **Private Hale** (the discoverer), **Corporal Voss** (the questioner: "why we fight for ice and stone"), **Sergeant Kael** (the sceptic; currently has no lines, so give him the Desert line above). Add **Seren**, **the Bonded of the Keep** and **the Captain** (who speaks rarely, like the Odyssey's hero among strangers).
- **Recast the 20-soldier roster into the world:** keep the *tonal spread* (terrified to arrogant); replace the ranks with in-world ones and the names with the Shoreland palette (B7).
  - No admirals, since there was no navy. The arrogant top of the old roster becomes a **Trade Council lord** who fled to the Keep, still proud: a living remnant of the pride that caused the war. That is dramatically useful.
  - No generals, since they were slain. The old "legendary" voice becomes an **old Theolith**.
  - Possible in-world ranks: *wall-hand, shieldman, file-leader, wall-warden, captain of the gate, oath-keeper (True Man), mason, Theolith, Elder/Elderess*.
- **The 330 campaign-card quotes:** keep the tonal ladder and rewrite them in register, stripping meta and modern references (A9 audit). A few survive nearly intact (A9).
- **Pvt. Reyes' Last Garrison cry** survives in spirit, recast: "The keep is falling! Every hand to the guns!"

## C8. The Whispers, restructured

- **Move them** from the first Build to the **debrief and between-campaign interstitials** (verified_brief -5).
- **Split them into three strands per band:** a **Hearth-word** (the Bonded or a True Man), a **Reading** (Seren, C3), and, from Cam 17, a **Wood-word** (the Mystaeri side).
- **Keep Jack's lines. They are good.** Rework them only for Halvard and consistency (A12 #8, #13):
  - "Rhyna says they tried to write in our tongue…" becomes "The Bonded say they carved in their own letters, and trusted the stone to carry the meaning. Stone carries nothing."
  - "The fleet cannot be recalled. The wood obeys the wood." becomes "No voice can call it home. But it can be sent home. The wood knows fear."
  - Keep as they are: "They picked the wrong fortress." · "The Ael'thar. Blood to blood. A frightened boy gave back fire." · "Our forebears were proud. Their response was rage. Both are true. Build the wall." · "We do not fight because we are right. We fight because our children are behind these walls." · "We remember our home too."

## C9. The Mystarchs as story set-pieces

- **Each Mystarch holds one fallen haven** ("one for each Shoreland harbour-city"). The Finale is ten homecomings: the nostos frame (A12 #19).
- **Each gets:** a true name (spoken and carved; B7), the haven it holds, **the grief it carries** (each haven's fall is a wrong the Mystaeri remember), and a Reading on its defeat.
- **Boss intro lines** in register, e.g.: "It has sat in Eldhythe since the harbour burned. It has had a long time to learn the streets." Or, in the dynamic memory-aware style: "The Throne of the Fen remembers you, Captain. It remembers that you ran."
- **Thematic fit for set-pieces:** a set-piece should *mean* its haven. The Ancient Treant at the Forest keep is literally a Mystholder walking home. The Crystal Lich sits in Glasspire's cellars under the spire that fell. The Hydra's regrowth is the Mystwood's regrowth, and the Rivenmen must keep pressing or the wood heals.

## C10. Other surfaces

- **Codex / lore screen:** the Book of Tales (B8) with its teller-attributions, and the Readings of Seren. The exonym-to-endonym swap (C5) is the codex's progress bar.
- **Persona rename:** "Ask the Emissary" becomes **"Ask Seren"** or **"the Archivist"**. "Ask the Stonewright" can become **"Ask the Bonded"** (verified_brief -9).
- **Currency:** keep *Stonwryt* as the lore object (the vow in the foundation, B8 Tale 13); give the UI currency a non-homophone name (verified_brief -9).
- **Towers:** the Stonewright tower in the fiction is a bonded pair at work; the twelvefold multiplier is the in-world reason repair is so fast.
- **The Fight's order slow-down** (Jack's ruling: time ramps from 1 hour per second to 18 seconds per game-hour while an order is given, then back): optionally name it in the fiction, e.g. **"the Captain's long breath"**, from the hearth-tales' idea that "for the Captain, an hour could last as long as a day." It is purely a label, with no mechanical meaning. It is low priority and needs Jack's call.
- **Store and trailer:** end on the hook, not on the creed; keep "We remember our home too" out of store screenshots (verified_brief -6).

## C11. Open questions for Jack

1. **Where are the battles fought?** At the ten fallen havens (the nostos frame, recommended) or at Rivenkeep's approaches? (A12 #19)
2. **Are the ships crewed, and who are the troops?** Wood-driven hulls, with root-warriors and a few young Mystaeri on the flag-hulls, is recommended. (A12 #4–5)
3. **Remove the Leviathan from the Fall** so the Mystarchs arrive last, as the Thrones? (A12 #2)
4. **The coda:** keep the Mystaeri engraver? Is he the Last Carver? Does he carve in wood or, deliberately, in stone? (A12 #6, #20; C2)
5. **Lifespan** 2.5× or 1.5×, and **which chronology**? (A12 #10–11)
6. **The soldier roster:** recast into the world, as recommended, or keep the modern ranks as a deliberate layer? (A12 #7)
7. **The faith voice:** narrator or characters? (A12 #28)
8. **The Captain:** stays unnamed (recommended)?
9. **The Title of Liberty challenge:** the GDD wording or the journal wording? (A5)
10. **Name collisions:** rename the Leviathan and Herald lineages, or the Mystarchs? (A11)
11. **Working names** for the ten havens (B7): accept, edit, or keep the labels?
12. **"Shore men"** as the Mystaeri's name for the Shorelanders: yes or no?

---

# APPENDIX — THE 330 CAMPAIGN-CARD QUOTES (VERBATIM, FROM GDD SCRIPT DATA)

*Source: `Rivenkeep_GDD.html`, `const Q` / `SOLDIERS` / `CAMPAIGN_NAMES`. Ten per campaign, rotating daily on the campaign card. Kept for the recast (C7); see the register audit in A9.*

**C1 — First Watch**

- Pvt. Tomás Reyes: "I d-don't even know which end of the wall goes up."
- Cpl. Dex Holt: "First day on the job. Try not to die on it."
- Sgt. Ama Okafor: "Put the stone down, pick another stone up. That's the whole war, kid."
- MSgt. Corinne DuPont: "Every fortress begins with a single stone. And a prayer."
- 2Lt. Priya Chakravarti: "The enemy gives you one free lesson. Don't waste it."
- 1Lt. James Hale: "Field Manual says 'enclose and hold.' Simple on paper."
- Maj. Rowan Kettridge: "Think of the board like a chess opening. Control the center."
- BGen. Aldara Voss: "A single wall, placed well, outperforms a fortress placed poorly."
- Gen. Dren Calloway: "The first battle teaches you what the last battle costs."
- Adm. Marcus Sterling: "Begin. That is the only order that matters."

**C2 — Shifting Ground**

- Pvt. Tomás Reyes: "The ground just... moved? Is that normal?!"
- PFC Lena Marsh: "They said the terrain would be different. They didn't say it would fight back."
- Sgt. Ama Okafor: "Watch where the land drops off. That's where you'll lose people."
- SSgt. Viktor Reznik: "I've fought on every surface this continent offers. Mud is the worst."
- SgtMaj. Elias Brant: "The terrain doesn't take sides. Learn its moods or it'll bury you."
- Cpt. Nadia Sorel: "Work WITH the ground, not against it. Saves time. Saves lives."
- LtCol. Yuki Tanaka: "Elevation data suggests a 23% advantage for high-ground cannons."
- Col. Emeric Thane: "The land fights for no one. But it punishes the ignorant."
- LtGen. Sable Morrow: "In my experience, commanders who ignore terrain don't become generals."
- Adm. Marcus Sterling: "The ground is mine. The enemy merely walks on it."

**C3 — Iron Tide**

- Pvt. Tomás Reyes: "There's... there's so many of them. Are those all ships?"
- Cpl. Dex Holt: "Siege ships. Great. Because regular enemies weren't enough."
- Sgt. Ama Okafor: "New enemy types just mean new ways to rebuild after they break through."
- MSgt. Corinne DuPont: "Sappers don't knock. They just appear inside your walls."
- 2Lt. Priya Chakravarti: "Every new enemy is a puzzle. Solve it once, own it forever."
- 1Lt. James Hale: "The tactical manual lists 14 enemy variants. I've memorized 12."
- Maj. Rowan Kettridge: "Advanced enemies require advanced responses. Adapt your cannon mix."
- BGen. Aldara Voss: "They come in numbers. We answer with walls."
- RAdm. Helena Voss: "I have seen every monster the sea can vomit forth. None have impressed me."
- Adm. Marcus Sterling: "Send them all. I'll need the target practice."

**C4 — Crooked Pieces**

- Pvt. Tomás Reyes: "This piece has SEVEN blocks?! Where does it even GO?"
- PFC Lena Marsh: "I keep rotating it and it still doesn't fit. I think it's broken."
- Cpl. Dex Holt: "The perfect block never comes. So stop waiting for it."
- SSgt. Viktor Reznik: "You get what you get. Complaining doesn't change the shape."
- SgtMaj. Elias Brant: "I've placed ten thousand pieces in my career. Every one taught me something."
- Cpt. Nadia Sorel: "Piece complexity isn't the enemy. Your expectations are."
- LtCol. Yuki Tanaka: "Statistically, a well-managed Wall Rack mitigates 78% of bad draws."
- MGen. Obi Adeyemi: "God gave us pentominoes to teach humility. Heptominoes to teach despair."
- Gen. Dren Calloway: "The shapes are not random. They are a language. Learn to read them."
- Adm. Marcus Sterling: "I could build a fortress from heptominoes blindfolded. And I have."

**C5 — Storm Warning**

- Pvt. Tomás Reyes: "It's raining sideways and my walls are on fire. Is this normal?!"
- PFC Lena Marsh: "Wind? In a SIEGE? Who designed this battlefield?"
- Sgt. Ama Okafor: "Keep your head down in a storm. The walls won't build themselves, but panicking won't help."
- MSgt. Corinne DuPont: "Weather is just terrain that moves. Treat it the same."
- 2Lt. Priya Chakravarti: "A true commander reads the wind before placing the first stone."
- Maj. Rowan Kettridge: "Meteorological data integrated into placement algorithms. Adjust for drift."
- Col. Emeric Thane: "When the sky turns, the clever commander has already built."
- LtGen. Sable Morrow: "I have fought in monsoons, sandstorms, and volcanic ash. The trick is the same: prepare early."
- RAdm. Helena Voss: "Wind and war respect no walls. Build them anyway."
- Adm. Marcus Sterling: "I once held a fortress through a hurricane. The enemy surrendered. The weather did not."

**C6 — The Long Wall**

- Pvt. Tomás Reyes: "Wait, we have to protect MORE castles now?! I can barely protect one!"
- Cpl. Dex Holt: "More territory, more problems. At least the pay is the... oh wait, there's no pay."
- Sgt. Ama Okafor: "Every castle you add to your line stretches your walls thinner. Choose carefully."
- MSgt. Corinne DuPont: "More castles, more souls to protect. That is the burden we carry."
- 1Lt. James Hale: "Resource allocation across multiple defense points requires triage discipline."
- Maj. Rowan Kettridge: "Two castles means two fronts. Three means three. The math is simple. The execution is not."
- BGen. Aldara Voss: "Hold the land or lose the crown. There is no middle ground."
- LtGen. Sable Morrow: "The art of war is the art of choosing what NOT to defend."
- RAdm. Helena Voss: "A commander who tries to hold everything holds nothing."
- Adm. Marcus Sterling: "All of it is mine. Every castle, every wall, every grain of sand."

**C7 — Fire and Stone**

- PFC Lena Marsh: "The ground is shaking AND there are siege ships?! Pick ONE disaster!"
- Cpl. Dex Holt: "Terrain plus enemies. Classic combo. Classic nightmare."
- SSgt. Viktor Reznik: "Two problems at once? Welcome to Tuesday."
- SgtMaj. Elias Brant: "When the terrain and the enemy conspire, the builder must outthink both."
- 2Lt. Priya Chakravarti: "The first layer pair reveals whether a commander can multitask under fire."
- Cpt. Nadia Sorel: "Terrain is your first ally. Enemies are your second teacher."
- LtCol. Yuki Tanaka: "Dual-threat analysis shows terrain-enemy overlap increases casualties by 40%."
- BGen. Aldara Voss: "Fire and stone. The two oldest weapons. Respect both."
- Gen. Dren Calloway: "Two forces against you means two opportunities to exploit their conflict."
- Adm. Marcus Sterling: "I do not acknowledge difficulty. Only outcomes."

**C8 — Broken Geometry**

- Pvt. Tomás Reyes: "The pieces don't fit AND the lava is coming?! I quit! I don't quit. But I WANT to."
- Cpl. Dex Holt: "Pentominoes on shifting ground. Whoever planned this has a sick sense of humor."
- SSgt. Viktor Reznik: "Bad pieces on bad terrain. Just pick the least terrible option and commit."
- SgtMaj. Elias Brant: "The land shifts. The pieces twist. Adapt or fall — that's the whole lesson."
- 1Lt. James Hale: "Spatial analysis under terrain modification requires 3D mental modeling."
- Maj. Rowan Kettridge: "Hard pieces on hard terrain is where you separate builders from commanders."
- Col. Emeric Thane: "Broken geometry is still geometry. Find the pattern."
- MGen. Obi Adeyemi: "I have seen masters build cathedrals from heptominoes on ice. It can be done."
- RAdm. Helena Voss: "The impossible is merely the untried."
- Adm. Marcus Sterling: "Geometry bends to my will. Not the reverse."

**C9 — Fog and Fury**

- Pvt. Tomás Reyes: "I can't SEE them and the WIND is pushing my walls! Help!"
- PFC Lena Marsh: "Fog plus wind drift. My two least favorite words in one campaign."
- Sgt. Ama Okafor: "You can't fight what you can't see. But you CAN build where you can't see."
- MSgt. Corinne DuPont: "Weather in a warzone is God's way of telling you to plan better."
- 2Lt. Priya Chakravarti: "You cannot fight what you cannot see — but you can prepare."
- Cpt. Nadia Sorel: "Fog and fury go together like fire and powder."
- Col. Emeric Thane: "Atmospheric interference reduces targeting efficiency. Compensate with volume."
- MGen. Obi Adeyemi: "The fog hides the enemy. But it hides us too. Use that."
- RAdm. Helena Voss: "I have fought blind. I have fought in gales. I have never fought without purpose."
- Adm. Marcus Sterling: "The fog parts for me. Or I burn it away. Either works."

**C10 — Divided Kingdom**

- Pvt. Tomás Reyes: "They want me to hold the WHOLE territory?! In THIS weather?!"
- Cpl. Dex Holt: "Castles, castles everywhere, and not a wall to spare."
- SSgt. Viktor Reznik: "Big territory plus bad weather. Just keep your head down and build fast."
- SgtMaj. Elias Brant: "A divided kingdom falls to the enemy that strikes the seams."
- 1Lt. James Hale: "Territorial defense requires concentric ring strategy per Field Manual 7."
- Maj. Rowan Kettridge: "Expansion campaigns teach what contraction campaigns punish."
- BGen. Aldara Voss: "Hold everything or hold nothing. The map decides."
- LtGen. Sable Morrow: "A commander's first duty is to know which castles to sacrifice."
- RAdm. Helena Voss: "I do not divide my kingdom. I EXPAND my empire."
- Adm. Marcus Sterling: "The crown sits on the head that defends ALL the castles. Mine."

**C11 — Wolves at the Gate**

- Pvt. Tomás Reyes: "SAPPERS IN THE WALLS AND OUR OWN CANNONS ARE HITTING US?!"
- PFC Lena Marsh: "Friendly fire is NOT friendly! Whose bright idea was this?!"
- Cpl. Dex Holt: "Watch where you're shooting. Actually, watch where THEY'RE shooting too."
- SSgt. Viktor Reznik: "Sappers and hard pieces in the same campaign. Thanks for nothing, command."
- 2Lt. Priya Chakravarti: "Wolves at the gate require wolves behind the wall. Arm up."
- Cpt. Nadia Sorel: "Friendly fire isn't. Remember that."
- Col. Emeric Thane: "Collateral damage analysis: 24% of wall damage is self-inflicted at this tier."
- MGen. Obi Adeyemi: "Sappers in the walls. Fire in the sky. Welcome to real war."
- RAdm. Helena Voss: "The enemy brings sappers because they respect your walls. Take the compliment."
- Adm. Marcus Sterling: "My cannons hit what I tell them to hit. If your wall is in the way, move it."

**C12 — Thunder and Ash**

- Pvt. Tomás Reyes: "Lightning, rams, AND my walls are crumbling in the rain?!"
- Cpl. Dex Holt: "Battle in a thunderstorm. At least the explosions match the weather."
- Sgt. Ama Okafor: "Hunker down, rebuild fast, and pray the wind shifts."
- MSgt. Corinne DuPont: "Bad weather makes bad enemies worse. That's just math."
- 2Lt. Priya Chakravarti: "Thunder and ash — the universe's way of testing your resolve."
- Maj. Rowan Kettridge: "Adverse conditions amplify enemy effectiveness by 35%. Plan accordingly."
- Col. Emeric Thane: "Bad weather never stopped a cannonball."
- MGen. Obi Adeyemi: "I have fought in worse. Every time I say that, it gets worse."
- RAdm. Helena Voss: "The storm is my ally. My enemies fear it. I do not."
- Adm. Marcus Sterling: "I once ordered a hurricane to wait. It didn't. I won anyway."

**C13 — The Widening Gyre**

- PFC Lena Marsh: "Every time I think I've enclosed enough, they add another castle!"
- Cpl. Dex Holt: "More territory, more enemies. The universe is consistent in its cruelty."
- SSgt. Viktor Reznik: "Defending everything with advanced enemies pressing in. Sure. Fine. This is fine."
- SgtMaj. Elias Brant: "Every castle you claim is a promise you must keep."
- 2Lt. Priya Chakravarti: "The widening gyre asks: how thin can you spread before you break?"
- Cpt. Nadia Sorel: "Hold what matters. Let the rest burn if you must."
- LtCol. Yuki Tanaka: "Multi-castle defense under advanced siege: survivability drops 12% per castle."
- MGen. Obi Adeyemi: "The gyre widens. The center cannot hold. But WE can."
- RAdm. Helena Voss: "I have never lost a castle I chose to keep."
- Adm. Marcus Sterling: "They think more castles weaken me. More castles give me more to fight FOR."

**C14 — The Architect's Nightmare**

- Pvt. Tomás Reyes: "These pieces have TOO MANY BLOCKS and the WIND keeps moving them!"
- Cpl. Dex Holt: "Pentominoes in a gale. Architecture's cruelest joke."
- Sgt. Ama Okafor: "Ugly pieces plus ugly weather. Just find a spot and commit."
- MSgt. Corinne DuPont: "The architect's nightmare is the builder's daily commute."
- 1Lt. James Hale: "The architect's nightmare is a spatial optimization problem. Solve it."
- Maj. Rowan Kettridge: "Piece complexity under weather modification is the ultimate Build test."
- BGen. Aldara Voss: "God gave us pentominoes to teach humility. He was right."
- LtGen. Sable Morrow: "I once watched a master builder cry at a hexomino in a crosswind. Tears and all, she placed it perfectly."
- RAdm. Helena Voss: "Nightmares end. Fortresses remain."
- Adm. Marcus Sterling: "There is no nightmare. Only a puzzle I haven't solved yet."

**C15 — Thin Line**

- Pvt. Tomás Reyes: "One spare castle. ONE. And the pieces are getting worse!"
- PFC Lena Marsh: "If I mess up ONE wall section, it's over. No pressure!"
- Sgt. Ama Okafor: "Thin margins mean thick walls. Build smart."
- MSgt. Corinne DuPont: "One castle margin. One. The math doesn't lie."
- 2Lt. Priya Chakravarti: "One spare castle. One margin of error. One chance."
- Maj. Rowan Kettridge: "Zero-margin campaigns reveal the difference between skill and luck."
- Col. Emeric Thane: "Thin lines hold when every block is placed with intention."
- MGen. Obi Adeyemi: "I have walked the thin line a thousand times. I am still walking."
- RAdm. Helena Voss: "The thin line doesn't scare me. Thick lines make lazy commanders."
- Adm. Marcus Sterling: "One spare? I don't NEED a spare. I don't lose castles."

**C16 — Tempest Reign**

- Pvt. Tomás Reyes: "The wind just blew my wall into the OCEAN!"
- Cpl. Dex Holt: "Tempest plus territory expansion. Who writes these mission orders?"
- SSgt. Viktor Reznik: "Wind pushes your walls. Enemies push your patience. Build anyway."
- SgtMaj. Elias Brant: "A tempest obeys no commander. But a commander can read the tempest."
- 1Lt. James Hale: "Meteorological drift plus multi-castle defense is a dual-variable optimization."
- Maj. Rowan Kettridge: "Tempest campaigns are won in the first three sorties. After that, you're surviving."
- BGen. Aldara Voss: "Wind and war respect no walls. Build them anyway."
- LtGen. Sable Morrow: "I remember Tempest Reign. I still hear the wind sometimes."
- RAdm. Helena Voss: "Tempests pass. Fortresses endure. That is the lesson."
- Adm. Marcus Sterling: "I command the tempest. Not literally. But close enough."

**C17 — The Crucible**

- Pvt. Tomás Reyes: "Three layers?! THREE?! We barely survived two!"
- PFC Lena Marsh: "Oh good, everything at once. Excellent. Wonderful. I hate this."
- Sgt. Ama Okafor: "Three threats means three things to watch. Triple your attention, not your panic."
- MSgt. Corinne DuPont: "The crucible burns away everything except skill. What's left is you."
- 2Lt. Priya Chakravarti: "Three forces conspire. The commander who survives earns the name."
- Cpt. Nadia Sorel: "The crucible doesn't break you. It reveals what you're made of."
- LtCol. Yuki Tanaka: "Triple-layer analysis requires parallel processing. Prioritize by casualty potential."
- MGen. Obi Adeyemi: "The crucible is where good commanders become great ones. Or ashes."
- RAdm. Helena Voss: "I have walked through the crucible. I came out forged."
- Adm. Marcus Sterling: "Three layers? Amusing. I've handled five before breakfast."

**C18 — Blood Weather**

- Pvt. Tomás Reyes: "RAIN OF IRON?! There's actual IRON falling from the SKY?!"
- Cpl. Dex Holt: "Blood weather. Sounds metal. Feels worse."
- SSgt. Viktor Reznik: "When it rains fire and enemies, you build faster or you don't build at all."
- MSgt. Corinne DuPont: "Blood weather is just weather with consequences. All weather has consequences."
- 2Lt. Priya Chakravarti: "Rain of iron. Wind of ruin. And still we build."
- Maj. Rowan Kettridge: "Triple-threat storms require a dedicated rebuild cadence. 8 blocks per tick minimum."
- BGen. Aldara Voss: "The weather bleeds. The enemy roars. And the builder keeps building."
- LtGen. Sable Morrow: "Blood weather tests everything at once. There is no partial credit."
- RAdm. Helena Voss: "I have built in blood weather. The walls held. I held."
- Adm. Marcus Sterling: "Let it rain iron. My walls are made of something stronger."

**C19 — The Sprawl**

- Pvt. Tomás Reyes: "The map is HUGE and I have to protect ALL of it?!"
- PFC Lena Marsh: "So many castles... so few walls... so much screaming..."
- Sgt. Ama Okafor: "When the territory sprawls, focus on chokepoints. Let the edges go."
- SgtMaj. Elias Brant: "Defend everything, defend nothing. Choose wisely, Commander."
- 1Lt. James Hale: "Sprawl analysis: fortress density drops below viable threshold at castle 6."
- Maj. Rowan Kettridge: "The sprawl rewards economy of motion. Every piece must serve two purposes."
- BGen. Aldara Voss: "A sprawling territory is a generous trap. Don't fall for it."
- LtGen. Sable Morrow: "I have commanded sprawling defenses on three continents. The secret? Triage."
- RAdm. Helena Voss: "The sprawl is not a problem. It is a canvas."
- Adm. Marcus Sterling: "My empire sprawls because I CHOOSE it to sprawl."

**C20 — Siege of Fire Mountain**

- Pvt. Tomás Reyes: "The volcano is ACTIVE?! Who puts a fortress on an ACTIVE VOLCANO?!"
- Cpl. Dex Holt: "Siege of Fire Mountain. Sounds like a movie. Feels like a funeral."
- SSgt. Viktor Reznik: "Lava, wind, and enemies. Prioritize the one that kills you fastest."
- SgtMaj. Elias Brant: "The mountain does not care who wins. That makes it the most honest enemy."
- 2Lt. Priya Chakravarti: "Fire Mountain has broken better commanders than you. Prove me wrong."
- Cpt. Nadia Sorel: "The mountain tests everything: terrain, combat, morale. Pass or burn."
- Col. Emeric Thane: "Volcanic siege parameters exceed standard deviation by 340%. Recalculate."
- MGen. Obi Adeyemi: "I was at Fire Mountain. Seventeen days. Still have the burns."
- RAdm. Helena Voss: "The mountain does not care. I do. That is the difference."
- Adm. Marcus Sterling: "I conquered Fire Mountain. Then I built a SUMMER HOME on it."

**C21 — The Gauntlet**

- Pvt. Tomás Reyes: "How many layers is this?! I've lost count!"
- Cpl. Dex Holt: "The gauntlet. Where the game stops being fun and starts being personal."
- Sgt. Ama Okafor: "Three layers deep, pieces getting worse. Just focus on the next wall."
- MSgt. Corinne DuPont: "By now you know the shapes. Now learn the cost of each."
- 1Lt. James Hale: "Hexomino integration under triple-threat conditions. The final exam."
- Maj. Rowan Kettridge: "The gauntlet is where theory meets practice. Practice always wins."
- Col. Emeric Thane: "The gauntlet doesn't test your building. It tests your priorities."
- MGen. Obi Adeyemi: "I ran the gauntlet once. I still dream about hexominoes."
- RAdm. Helena Voss: "The gauntlet is a gift. It shows you what you're capable of."
- Adm. Marcus Sterling: "Gauntlets are for soldiers. Admirals send soldiers through gauntlets."

**C22 — Shattered Compass**

- Pvt. Tomás Reyes: "My compass literally broke. The wind smashed it."
- PFC Lena Marsh: "Which way is north?! Does it even MATTER anymore?!"
- Sgt. Ama Okafor: "When the compass breaks, follow the walls. They know where they need to be."
- SgtMaj. Elias Brant: "North means nothing when the ground itself is moving."
- 2Lt. Priya Chakravarti: "A shattered compass forces you to navigate by instinct. Good."
- Maj. Rowan Kettridge: "Gyroscopic disorientation under combat stress. Compensate with landmark navigation."
- BGen. Aldara Voss: "The compass lies. The walls don't. Trust the walls."
- LtGen. Sable Morrow: "I have fought without a compass, without maps, without hope. Walls still went up."
- RAdm. Helena Voss: "Direction is a luxury. Determination is a necessity."
- Adm. Marcus Sterling: "I don't need a compass. The enemy always knows where I am. Follow the craters."

**C23 — The Reckoning**

- Pvt. Tomás Reyes: "S-seven castles. I can barely count to seven right now."
- Cpl. Dex Holt: "The reckoning. When all your bad habits come home to roost."
- SSgt. Viktor Reznik: "Seven castles, one spare. Don't waste it on sentiment."
- SgtMaj. Elias Brant: "The reckoning asks a simple question: were you paying attention?"
- 2Lt. Priya Chakravarti: "Seven castles. One spare. Count your walls, Commander."
- Cpt. Nadia Sorel: "At seven castles, triage becomes an art form. Master it."
- LtCol. Yuki Tanaka: "Defense sustainability at 7-castle threshold requires 94% wall integrity minimum."
- MGen. Obi Adeyemi: "The reckoning is where I learned that 'good enough' walls are not."
- RAdm. Helena Voss: "The reckoning comes for everyone. I was ready. Are you?"
- Adm. Marcus Sterling: "Seven castles is a Wednesday. I've held twelve."

**C24 — Tides of Ruin**

- Pvt. Tomás Reyes: "They have MEDICS now?! The enemies have MEDICS?!"
- PFC Lena Marsh: "Ships that heal other ships. That's just unfair!"
- Sgt. Ama Okafor: "Hospital ships in the fleet means they're planning a long siege. Dig in."
- MSgt. Corinne DuPont: "They bring medics now. That means they plan to stay."
- 2Lt. Priya Chakravarti: "A fleet with medics is a fleet that expects to take hits. Oblige them."
- Maj. Rowan Kettridge: "Hospital ship targeting priority analysis: eliminate before DPS threshold exceeds repair rate."
- Col. Emeric Thane: "When the enemy starts healing, start killing faster."
- MGen. Obi Adeyemi: "Tides of ruin wash both ways. Their medics slow the tide. Your cannons stop it."
- RAdm. Helena Voss: "Tides rise and fall. Fortresses remain."
- Adm. Marcus Sterling: "Let them bring medics. I'll destroy the medics first. Then the rest."

**C25 — The Noose Tightens**

- Pvt. Tomás Reyes: "I can't breathe. The margin is zero. There's no room for error. I can't breathe."
- Cpl. Dex Holt: "The noose tightens. And we're the ones wearing it."
- SSgt. Viktor Reznik: "Fewer margins mean every piece placement is a life-or-death decision."
- SgtMaj. Elias Brant: "Fewer margins. Harder choices. This is where legends break."
- 2Lt. Priya Chakravarti: "The noose tightens — but a tightened noose can also be a garrote if you flip it."
- Cpt. Nadia Sorel: "Precision becomes survival at this tier. There is no 'close enough.'"
- Col. Emeric Thane: "Margin analysis at tier 25: sub-2% error tolerance. Surgical precision required."
- MGen. Obi Adeyemi: "I have seen the noose tighten on better commanders than me. I adapted. They didn't."
- RAdm. Helena Voss: "The noose tightens? Good. I work better under pressure."
- Adm. Marcus Sterling: "The noose is for the weak. I AM the noose."

**C26 — Labyrinth of War**

- Pvt. Tomás Reyes: "It's a maze of walls and enemies and I can't find my way out!"
- Cpl. Dex Holt: "Labyrinth of war. Even the Minotaur would get lost in here."
- Sgt. Ama Okafor: "In a labyrinth, the only strategy is forward. Just keep building."
- MSgt. Corinne DuPont: "Every wall is a question. Every cannon is an answer."
- 1Lt. James Hale: "Labyrinth mapping requires iterative wall-path optimization. Cross-reference enclosures."
- Maj. Rowan Kettridge: "The labyrinth of war has no center. Only edges. Defend the edges."
- BGen. Aldara Voss: "A labyrinth is just a fortress someone else designed. Redesign it."
- LtGen. Sable Morrow: "I walked the labyrinth at Campaign 26. Three times. Won twice."
- RAdm. Helena Voss: "The labyrinth has no exit. Good. Neither do I."
- Adm. Marcus Sterling: "I do not navigate labyrinths. I REDESIGN them."

**C27 — Empire of Walls**

- Pvt. Tomás Reyes: "Eight castles. Eight. My hands are shaking too hard to count higher."
- PFC Lena Marsh: "Empire of walls. More like empire of anxiety."
- Sgt. Ama Okafor: "Eight castles demand eight miracles per sortie. Start praying. Then building."
- MSgt. Corinne DuPont: "At eight castles, you're not building a fortress. You're building a nation."
- 2Lt. Priya Chakravarti: "An empire of walls requires an emperor's will. Find yours."
- Maj. Rowan Kettridge: "Eight-castle defense: the Build phase becomes a 26-second chess game."
- BGen. Aldara Voss: "Empires are built by those who refuse to let any part fall."
- LtGen. Sable Morrow: "I held eight castles at Campaign 27. My hair was brown when I started."
- RAdm. Helena Voss: "The empire stands because I WILL it to stand."
- Adm. Marcus Sterling: "Eight castles? I built my career on ten."

**C28 — The Anvil**

- Pvt. Tomás Reyes: "Hammer... falls... fortress... please hold... please..."
- Cpl. Dex Holt: "The anvil. We're the metal and the enemy is the hammer. Fun."
- SSgt. Viktor Reznik: "Hit, rebuild, hit, rebuild. The rhythm of the anvil."
- SgtMaj. Elias Brant: "Hammer falls. Fortress holds. Repeat until one breaks."
- 2Lt. Priya Chakravarti: "The anvil forges or shatters. Which one you become is up to you."
- Cpt. Nadia Sorel: "The anvil campaign has a 4% completion rate. Be in the 4%."
- LtCol. Yuki Tanaka: "Structural stress testing at campaign 28 exceeds design parameters by 200%."
- MGen. Obi Adeyemi: "The anvil doesn't care how good you are. It only cares how many times you can rebuild."
- RAdm. Helena Voss: "I am the anvil. The enemy is the one being shaped."
- Adm. Marcus Sterling: "Hammers break on my walls. I've collected seventeen of them."

**C29 — Edge of Ruin**

- Pvt. Tomás Reyes: "Nine c-castles, one spare. ONE. And they're sending EVERYTHING."
- PFC Lena Marsh: "Edge of ruin. I can see the edge. It's very close."
- Sgt. Ama Okafor: "One spare among nine. Don't get attached to it."
- MSgt. Corinne DuPont: "Nine castles, one spare. The math is merciless."
- 2Lt. Priya Chakravarti: "The edge of ruin is where you discover what you're willing to sacrifice."
- Maj. Rowan Kettridge: "Survival probability at 9/10 castles with full layer stack: 8.3%. Noted."
- BGen. Aldara Voss: "The edge of ruin is not the end. It's where the view gets clear."
- LtGen. Sable Morrow: "I stood at the edge of ruin once. I took one step back. Then I built a wall."
- RAdm. Helena Voss: "Ruin is for those who stop building."
- Adm. Marcus Sterling: "There is no edge. There is only territory I haven't claimed yet."

**C30 — The Last Geometry**

- Pvt. Tomás Reyes: "Seven blocks per piece. SEVEN. My brain has left my body."
- Cpl. Dex Holt: "Heptominoes. I'd rather fight the boss with my bare hands."
- Sgt. Ama Okafor: "The last geometry. After this, there are no more shapes to fear. Small comfort."
- MSgt. Corinne DuPont: "Heptominoes. I have seen veterans weep. I have joined them."
- 1Lt. James Hale: "Heptomino integration efficiency: 12% optimal placement rate under combat conditions."
- Maj. Rowan Kettridge: "The last geometry is where the piece pool becomes your primary enemy."
- Col. Emeric Thane: "Heptominoes don't fit because they weren't meant to. Place them anyway."
- MGen. Obi Adeyemi: "The last geometry broke my best engineer. She rebuilt. The pieces didn't change. She did."
- RAdm. Helena Voss: "The last geometry is not the last challenge. It is the last lesson before the real one."
- Adm. Marcus Sterling: "Heptominoes? I use those as DECORATIONS."

**C31 — The Last Bastion**

- Pvt. Tomás Reyes: "This is it. The last bastion. If we lose this, we lose EVERYTHING."
- PFC Lena Marsh: "I'm not ready. Nobody's ready. But here we are."
- Sgt. Ama Okafor: "The last bastion. Everything you've learned, every wall you've placed — it comes down to this."
- SgtMaj. Elias Brant: "If you are reading this, you are among the finest. Prove it."
- 2Lt. Priya Chakravarti: "The last bastion is not a place. It's a state of mind."
- Cpt. Nadia Sorel: "Last bastion protocols: maximum efficiency, zero waste, absolute focus."
- Col. Emeric Thane: "The last bastion doesn't ask if you're ready. It asks if you're worthy."
- MGen. Obi Adeyemi: "I defended the last bastion. Barely. The scars remind me every morning."
- RAdm. Helena Voss: "The last bastion falls only when the last commander falls. I am still standing."
- Adm. Marcus Sterling: "'Last' bastion? There are no last bastions. Only first chapters in the NEXT war."

**C32 — Full Stack**

- Pvt. Tomás Reyes: "ALL of it. Everything. At once. I think I'm going to be sick."
- Cpl. Dex Holt: "Full stack. All five layers. This is where legends are born or buried."
- Sgt. Ama Okafor: "Full stack means no tricks left. Just skill. Just walls. Just you."
- MSgt. Corinne DuPont: "Everything. All at once. All of it yours to hold. Or lose."
- 2Lt. Priya Chakravarti: "The full stack is the final exam, the graduation, and the funeral — all at once."
- Maj. Rowan Kettridge: "Full-stack analysis: all five layers simultaneously. Computing optimal strategy... ERROR: INSUFFICIENT DATA."
- BGen. Aldara Voss: "Every mechanic. Every enemy. Every piece. Every castle. This is the complete game."
- LtGen. Sable Morrow: "I reached Full Stack once. Took me fourteen months. Worth every second."
- RAdm. Helena Voss: "The full stack is not a campaign. It is a coronation. Win it, and you are a Commander."
- Adm. Marcus Sterling: "Full stack. The only challenge worthy of my attention."

**C33 — End Times**

- Pvt. Tomás Reyes: "B-b-boss. That's a boss. That thing is ENORMOUS."
- PFC Lena Marsh: "End times. I can see why they call it that."
- Sgt. Ama Okafor: "Bosses. Real bosses. Not the 'tough enemy' kind. The 'oh god it's eating my castle' kind."
- SgtMaj. Elias Brant: "They saved their worst for last. So did we."
- 2Lt. Priya Chakravarti: "End times don't mean the end. They mean the beginning of the real fight."
- Cpt. Nadia Sorel: "Boss mechanics require phase-specific targeting and enclosure-priority shifts."
- Col. Emeric Thane: "The boss is not the enemy. The boss is the final question. Your fortress is the answer."
- MGen. Obi Adeyemi: "End times. I've seen them. I survived them. I don't talk about them."
- RAdm. Helena Voss: "The end is just another wall to build. Build it."
- Adm. Marcus Sterling: "End times? I call it TUESDAY."
