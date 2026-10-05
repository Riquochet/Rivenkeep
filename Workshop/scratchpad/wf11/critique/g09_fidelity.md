# g09 · Fidelity critique: V.7 The Mirror in the Grain · Book Six heading and Argument · VI.1 The Homecomings

**Read against:** R6b V.7 and VI.1 entries, with §0, 0.1 and 0.7; R6a's III.1 plants; outline §8 V.7 and VI.1; reckoning §1.3, §2.8 and §2.9; `book_v2.md` l.2087–2433; `voice_v3.md`; `craft.md`; and the sibling drafts that V.7 and VI.1 must lock to: g01 (foreword and Contents), g02 (I.2), g03 (I.5), g04 (II.3), g05 (III.1–2), g07 (IV.5), g08 (V.5), g10 (VI.3), g11 (Epilogue and Knowings) and w02 (VI.2). I also read the v2 builder (`wf10/book/build_story_html.py`) for the markup.

**Counter** (`count_v3.py`, each leaf cut out alone):
- **V.7:** 1,295 against a ceiling of 1,300. Headnote 30, dateline 5. Two *-eth*, two *do*-negations, mean sentence 11.2, 46% under ten words. The one sentence over 30 is a false join with the Part III carving. All four semicolons are in fixed matter.
- **VI.1:** 1,059 against 1,100. Headnote 41, dateline 8. Two *-eth*, one *do*-negation, mean 8.9, 61% under ten words, which the litany exception allows.
- Both leaves are under their ceilings. Neither reaches voice §7's aim of 5–10% under: V.7 is 0.4% under and VI.1 is 3.7% under. The additions below must therefore be paid for in V.7 (see fix 17).

**Clean on the locks:**
- no custom of burning, and no echo of one (Harl's *I did not burn it.* is his own temper, as R6a §0.1 and voice §4 require);
- Brenn does not appear;
- no ▒▒▒▒ name is needed (*the warden's door* is the common noun, as in the IV.3 sample);
- every pair-name takes a plural verb, and there is no singular *they*;
- no Christian mark (the prayer reads *God*, per craft rule 21; g11 relies on this exact wording);
- the three carvings are verbatim;
- no song is quoted;
- *We remember* is verbatim every time;
- the native key `legend_stonwryt_enrella chip` is kept, and v2 gave VI.1 no native block and no FACING LEAF marker;
- datelines agree with the reckoning (Cam 25, 29 and 32, and the year of the homecomings).

The fixes follow, most serious first.

---

## Markup and the Book's frame

**1. VI.1, the ten haven heads (l.189, 199, 205, 215, 221, 227, 235, 241, 265, 271). Split each into two paragraphs.**
- **What:** each head is now one paragraph, `**Eldhythe.** *Voss, for Corlen.*`. Make it two, as v2 had them (l.2321–2323) and as g05 III.1 still has them: `**Eldhythe.**`, a blank line, then `*Voss, for Corlen.*`. This costs no words.
- **Why:** the builder turns a bold-only paragraph into a part head (`h4.part`) and the fully italic line after it into the who-line. A merged head is neither, so all ten heads print as plain body prose, and the litany loses its shape.

**2. Book Six Argument (l.173). Make it agree with the Contents.**
- **What:** g01's Contents (l.65) gives *What came home, and what was sent.* g09 gives *How the havens came home, and the war went home.* g01 l.403 asks every Book head to use the Contents' line. Either adopt g01's line here or have g01 change. I recommend g01's: it spoils nothing, and *what was sent* is paid in VI.3.
- **Why:** the reader would see two different Arguments for one Book.

**3. V.7, Halyna's four pairs of halves (l.68/70, 122/124, 151/153, 159/161). Wrap each pair in markers.**
- **What:** put `<!-- HALYNA -->` before the first half and `<!-- HALYNA END -->` after the second, around those two paragraphs only. The brief's markup list asks for exactly this, and markers are not counted.
- **Why:**
  - v2 marked each pair with a cue, *One of them said, and the other finished:*, and the builder (l.482–484) inks the next two paragraphs a/b only after such a cue. g09 rightly cut the cues (voice §4: no tag on every line), so all four pairs would now print in one ink. That breaks the foreword's two inks (g01 l.114) and *Ye cannot tell*.
  - Do not wrap {{Idrenna}}'s prayer (l.49/51). The builder keeps another pair's halves in the leaf's own ink.
  - **For the orchestrator:** g01's *"A tale told from one side of a wall," / "is half a tale."* and g08's Count VI halves have the same gap. One ruling should cover the whole Book.

**4. V.7, the native caption (l.42). Restore v2 word for word.**
- **What:** the caption reads *as Seren looked on it by the last of the light*. v2 (l.2130) reads *looked upon it*. Put *upon* back.
- **Why:** voice §1.7 puts every `::: native` block outside the dial, and g11 keeps v2's native English verbatim. The *upon → on* rule applies to prose, not to fixed matter.

## The logic of the scenes, and their payoffs

**5. V.7 Part I, the gate-song (l.59). Fix who stays silent.**
- **What:** the draft has *No one took the first voice. The line began in silence, and the rest came in at the comma, as though it had been sung.* But in I.2 (g02 l.82) Enno and Della *took the first voice between them, the one to the comma and the other the rest*, and the guild came in after them. Both are dead, so both halves must be silent. As written, someone comes in at the comma and sings Della's half, and only Enno's half is missing.
- **Fix** (+2 words): *No one took the first voice, before the comma or after it. The guild came in on the second line, as though the first had been sung.*
- **Why:**
  - It keeps R6b's must-survive, *the first voice silent upon the comma*.
  - It locks to I.2.
  - It lets the Epilogue answer it: there {{Orvenna}} take both halves, *Ormund to the comma and Penna the rest* (g11 l.21).

**6. VI.1, the north lamp (l.263 and l.279). Give the child a lamp of its own.**
- **What:** Hesk's mother's lamp is the one he lit on the north wall (III.1 g05 l.59; III.2 l.155, *Every dusk since, I have lit it on the north wall*). VI.1 has him carry that lamp to Rimewatch, where it is found burning on the ice. So *At the Keep that night the north lamp was dark. Then a child lit it* has the child light a lamp that is lying on the mere.
- **Fix** (+5 words): *At the Keep that night no lamp burned on the north wall. Then a child set one there, and lit it, and said, "Someone has to keep a light."*
- In the roll (l.279), write *At Hesk's a lamp was lit on the north wall, and no answer came down.* This still pays V.5 Count VI (g08, *Hesk answered from the north wall, where his lamp was lit*).
- Keep the child's line verbatim. It is Hesk's own line from III.2 (g05 l.157), now in a child's mouth.

**7. V.7 Part II, the glass and the battery (l.128 and l.132). Give Hale the battery too.**
- **What:** only the glass is offered to Hale. The outline (Part II scene 10) and R6b II.13 have the Captain offer Pellow's glass *and the battery with it*, and both go to Ruan.
- **Fix** (+4 words): *…and held out the glass to Hale, and the battery with it.* … *So they went to Ruan of the spire, his file-leader. He put the glass to his eye…*
- **Why:**
  - *"I am not a True Man … I run."* answers a True Man's post, not a glass.
  - Ruan's taking the battery is what makes him a True Man. That gives V.5 Count VI and VI.1 their fourteen names, and it lets *Ruan, for Pellow* speak as a True Man at Glasspire.
  - The writer's notes do not list this drop, so it was lost, not folded.

**8. V.7 Part I, the house of one door (l.11). Put the mark back under its first stone.**
- **What:** II.3 (g04 l.86) plants it: *cut their mark under its first stone, for they could not wait for the last.* R6b I.1 keeps it (*with their mark beneath its first stone*). g09 lost it. Without it, Della cutting their mark under the *last* stone of the breach does not pay II.3's *could not wait for the last*. Also, *Enno set the chisel, and Della struck.*, told of the drum-night, does not say what they were cutting.
- **Fix** (+6 words): *Their mark lay under its first stone. Enno had set the chisel, and Della struck. One course high it stood, and higher it stood never.*

**9. V.7 Part II, Pellow's battery (l.106). Say the hunters came to it first.**
- **What:** the outline's ★★ beat is that the hunters came to Pellow's battery *first, for his was the battery nearest the grey* (v2: *to his the hunters came first of all*). g09 cut the Captain's place at the north end (a fold the notes record), so *Pellow's was the farthest* now has nothing to be farthest from. *first* was also lost, unrecorded.
- **Fix** (+5 to +7 words): *Pellow's was the farthest, and the nearest the grey. To his they came first, and it met them alone.*
- Optional: the outline's *(keep)* clause *and would not leave it*, after *to every gun that had spoken* (l.104, +5). It is why silence could not have saved a gun that had already spoken.

**10. VI.1, the sworn wants (l.185, and Lanner's *as I sware I would*, l.267). Make the oaths true in III.1, or soften them here.**
- **What:** *ten of us had sworn what each would do … I held all ten* needs ten wants in III.1. g05 III.1 gives six: Corlen, Marl, Garvel, Harl, Hesk and Lanner (g05 l.238). Tamm, Aske, Ulden and Pellow give a habit but no want. Lanner's want reads *I mean to climb them again*, not an oath.
- **Fix, preferred** (in g05; craft §2.3 says *ten men, each with one picture and one want*): one clause of want each, which VI.1 already pays:
  - Tamm sets his stones on the bank;
  - Aske keeps every axe off the trees;
  - Ulden sleeps under his own roof of stone;
  - Pellow looks on his spire again.
  
  Lanner's *I mean to* becomes *I swear to*.
- **Fallback, if g05 will not change:** VI.1 reads *At this hearth each of us had told his haven. Oath-keeper am I. I held all ten.*, which plays on *tell*, and Lanner says *as I said I would*.

**11. V.7 Part I, Stannard at dusk (l.47) against V.5 Count IV. Fix the clash in one of the two tales.**
- **What:** g08 Count IV has *At dusk I walked the wall to count. Enno of the guild I found in the east breach.* V.7 has *At dusk Stannard carried Enno the whole mile*, so at dusk Enno lies in two places.
- **Fix:** change one word in g08 (*Ere dusk I walked the wall*). This keeps V.7's dusk, which follows Seren looking *by the last light*. If g08 is locked, V.7 says *At nightfall Stannard carried…*

## Small fidelity points, one or two words each

**12. V.7 l.13. Echo I.2 word for word.** Change *Into this ward they had come hand in hand, where I came in alone.* to *Into that courtyard they had come hand in hand…* This pays I.2's ★ line *I came into that courtyard alone.* (g02 l.23) exactly.

**13. V.7 l.74. Put back the moment of knowing.** *Its first part I knew* reads as if Seren already knew it. v2 and the outline (scene 10) have *that night, for the first time, I knew the first part of it*, and that dawning is the climb to *I will not write what I thought* (R6b says keep that chain whole). Fix (+1 word): *That night I knew its first part: ael, the joining, as in Ael'thar…*

**14. V.7 l.84, and the dateline (l.3). Mark the year that passes before Part II.**
- **What:** Part I carries *short night* (summer) and Part III carries *snow to the knee* (winter). Part II, a year after Part I, carries no season, and with the part datelines gone only the leaf dateline dates it.
- **Fix** (+1 word): *On a grey spring morning a fleet ran at the wall…* Alternatively, restore v2's gulls back on the shingle (+8).
- **The dateline:** to match the samples' form (*The first winter, …*), write *The fourth summer, the fifth spring, the sixth winter.* That is 8 words, inside the cap.

**15. VI.1 headnote (l.179). Say that Seren was at the fires.**
- **What:** v2's *I was at every one of those fires, and set each down beside it* is gone. Without it, no one is shown setting the havens down, and it is unclear why Kael counts *my leaves*. Separately, *each at his own haven's fire* is untrue of Kael at Rimewatch.
- **Fix** (+5 words; the headnote goes from 41 to 46, inside the cap of 50): *Laid by the True Men at each haven's fire, on the night its Throne fell; I set each down beside it.* The rest of the headnote stands.

**16. VI.1 and VI.2, the Throne names. No change in g09; w02 should change.**
- **What:** VI.1's *the Bearer of Branches* and *the Grain That Rots* match the Book of Knowings (g11). VI.2 (w02 l.257 and l.259) has *bearer of new branches* and *the rotting grain*. VI.2 now cuts its Shore lines and names no haven, so these English names are the only bridge between the facing leaves.
- **Fix:** ask w02 to match VI.1 and g11. w02's own notes raise this.

## Budget

**17. V.7 must stay at or under 1,300 once fixes 5–14 are in.**
- **Cost:** fixes 5, 7, 8, 9, 13 and 14 together add about 20–25 words.
- **Trims that cost no element:**
  - l.100: *The Captain heard Hale out, and went along the wall* becomes *The Captain went along the wall* (−4).
  - l.55: *bound a strip of his cloak on a pike* becomes *bound a strip on a pike* (−3). Craft §3.6 has the strip told whole once at Jory and given only a clause after that.
  - l.120: *Then I understood: the wood lieth not.* becomes *The wood lieth not.* (−3).
  - l.86: *the youngest of the True Men* (−6). III.1 holds it (g05 l.67).
- **If more is needed:** VI.1 has room. Its l.279 *for a count is no count till it be named* repeats V.5 Count VI word for word (craft rule 22), and cutting it saves 9.

## Folded on purpose (accepted; listed so nothing is lost by accident)

**V.7:**
- *Hold the stone, Seren.*, once (craft §3.6);
- the hood, three times (craft §3.6 supersedes R6b 0.7 and (d));
- the fisher's wife, cut (craft rule 12);
- the lamplighter and the boots, each as a clause;
- the Stonwryt law, cut (outline: must-not-carry);
- *for it was the wall-masters who had sent them apart*;
- Lanner sinking the bearer (it lives in V.5 Count IV);
- Pellow's father and the great glass (III.1 carries it, and VI.2 pays it);
- the list of deceits;
- *A mind that carves how it will go home is a mind that wants to go home* (outline ★★). It is folded into the boots and *we saw the enemy hope*. It is a gloss by craft rule 14, so the fold is accepted.
- *and it was no runner's fault* (outline scene 4). The writer cut it, and it can come back for 6 words. **Orchestrator's call.** It is the one kindness to Hale at the grave.

**VI.1:**
- the epithets in the haven heads (III.1 keeps them);
- *I did not understand it then. I think I do now.* (I.5 only, craft §3.6);
- the hood at Rimewatch;
- the ground still warm, and the long table;
- the outline's [may] staff at Glasspire.

## Seeds and payoffs that cross tales, checked against the sibling drafts

Holding:
- **The foreword** (g01): *Ye cannot tell*, Enrella's jest and *Orvenna never raise their voices*.
- **I.2** (g02): hand in hand, and the first voice (once fix 5 is made).
- **I.4** (g03): *The one set the chisel, and the other struck.*
- **I.5** (g03): Ebba's *Perhaps*; *Every haven … is Rivenkeep*; *Tomorrow we go down*; the hearth's first wait for Ebba. VI.1 makes the second wait, within craft §3.3's allowance.
- **II.3** (g04): *seldom apart, and never far*; the jest; the house; *a mile apart, and each knew*.
- **III.1 and III.2** (g05):
  - Corlen's *I will steer it in* and *the sea had not finished*;
  - Tamm's stones and line;
  - Marl's course-stone;
  - *These were trees once*;
  - Garvel's not-a-gun;
  - Harl's *I told him to burn it*;
  - Ulden's ear and roof;
  - Hesk's lamp and *The ice held*;
  - Lanner's whistle;
  - Pellow's *Look close*;
  - Kael's *The Captain found me on a road*.
- **IV.4** (w01): *Ael'thar*, and the gift *slow … and true*. This last is a light lock for *the wood cannot lie*, but enough.
- **IV.5** (g07): the three grey stones *under no roof but the rain*.
- **V.2** (g08): the *Burn* plank.
- **V.5** (g08):
  - Corlen under the cairns, and Voss's finger;
  - Count IV has no *One*;
  - *Ruan of the spire hath his glass*;
  - *fourteen names, and twelve*.
- **VI.3** (g10): the sending answers *a morrow they did not carve for*, unsaid.
- **The Epilogue and the Knowings** (g11):
  - rely on V.7 for the prayer told whole and for *Rhenear* and the young hand;
  - rely on VI.1 for Voss's stones, the *Burn* plank on the crust and the north-lamp child.
  
  All of these are present in g09.

Needing the action above: fix 5 (I.2 and the Epilogue), fix 6 (III.1, III.2 and V.5), fix 7 (V.5 and VI.1), fix 8 (II.3), fix 10 (III.1), fix 11 (V.5) and fix 16 (VI.2).
