# RIVENKEEP · CONLANG AND SCRIPT CRAFT

> **Imported to `Docs/Research/` on 2026-09-27** as a source behind `Rivenkeep_Tongues.html`, which is canonical where the two differ. Scripts, renderers and file paths mentioned below belong to the design workspace and are deliberately not in the repo, which is documents only.


*Research for wf6: the two tongues and the two hands. 2026-09-27. Workflow input, not a Book leaf and not a repo doc.*

**Why this exists.** Jack asked (2026-09-27) that the line *"Untold. Halyna cannot yet hold this deep."* be replaced by real Shoreland or Mystaeri writing. The player cannot read it until an achievement "translates" it. He pictured the Mystaeri hand as something like the alien writing in *Arrival* and Shoreland as an ancient, Celtic-feeling tongue, and he wants both to be **real**: a language written by rule and read back by rule. His standing rule is that names and designs must be **original**. Influence is fine, but nothing may be exactly traceable to another work.

This file covers the craft research and the boundaries on originality. It does not design either language. It ends with a **DO-NOT-COPY** list and a **DO** list for the two scripts, plus a few decisions only Jack can make.

**Confidence key.** **[H]** means several sources agree, or the fact is standard reference knowledge. **[M]** means one secondary source, or my own inference from sources. **[L]** means a judgement call or a proposal. Source numbers `[S#]` refer to the list at the end. `[C#]` refers to our own canon files.

---

## 0 · THE SHORT ANSWER

1. **Stone writes what is said; wood writes what is meant.** This is the design thesis, and the canon already holds it. "Stone carried nothing" (Legend III). What is carved in living wood "is not heard. It is known ... whatever tongue the carver spoke" (II.2, [C1]). So the Shoreland **course-hand** is an *alphabet*: it records sound, is cut straight in stone, and runs in lines. The Mystaeri **grain** is *semasiographic*: it records meaning, is grown in rings, and is taken in whole. Real writing scholarship draws exactly this line, between *glottographic* and *semasiographic* systems (Sampson) [S30] [H].
2. **Take Arrival's idea, not its look.** The idea is Chiang's: a script that carries meaning rather than sound and is grasped whole [S1] [H]. The look belongs to Vermette and Bertrand: one inky, smoky circle with tendrils and blots, where stroke weight carries tone. They designed about 100 of these and 71 reached the screen [S1] [S3] [H]. Ours can be the opposite on every visible axis. Many rings instead of one. Crisp knife-cuts instead of ink. Marks *across* the rings instead of blots *off* the rim. And a script with a direction, heart to bark, where Arrival's has none. **Arrival's writing is timeless; ours is made of time**, one ring per growing.
3. **Almost every rule the grain needs is already real wood anatomy** [S39] [S40] [H]:
   - the pith and its eccentricity;
   - heartwood, sapwood and bark (three bands, the three movements);
   - rays running from pith to bark (links);
   - knots (the Knot);
   - radial checks ("where bark splits");
   - fire scars (*Burn*);
   - frost rings;
   - the double pith of stems that grew together (the Joined Tide).

   Building from anatomy is also the originality defence. It is nature, not anyone's glyph set.
4. **The course-hand's originality comes from its medium too.** Runes avoid horizontal strokes because a cut along a stave's grain is hard to see and can split the wood [S8] [H]. Stone has no grain. So a stone hand can use horizontals freely, and that alone separates it from runes and Cirth. The rest of the look comes from masonry:
   - letters **stand on** a mortar line (the bed joint);
   - words are **stones** parted by head-joints;
   - successive lines **break the joint**, as a mason staggers a course.
5. **Ogham is the right spirit and the wrong letters.** Ogham letters are counts of one to five parallel scores on either side of a stem, or across it, with vowels as notches, read up the edge of a stone [S6] [S7] [H]. Do not use tallies. Do not put strokes either side of a central line. Do not notch the line for vowels.
6. **The Celtic "feel" comes from typology** [S24–S29] [H], and none of it needs a Celtic word:
   - initial mutation (lenition and nasalisation);
   - verb-first order;
   - conjugated prepositions, and no verb "to have";
   - two verbs "to be";
   - verbal nouns in place of infinitives;
   - broad/slender consonant harmony;
   - counting in twenties.
7. **The Sindarin trap.** Tolkien *deliberately* modelled Sindarin's sound changes on Welsh [S20] [H]. A fantasy tongue with Welsh-style mutation is therefore, by default, "another Sindarin". Lean on the features Sindarin does not showcase: the Irish-type broad/slender harmony, verb-first syntax with verbal nouns, and conjugated prepositions. Avoid its signatures: plurals by vowel change (*adan/edain*), and an article *i* that causes soft mutation.
8. **Be naturalistic the way Tolkien, Peterson and Rosenfelder are.** Build an older stage, apply regular sound changes, and let irregularity fall out of the history [S18] [S21] [S23] [H]. The real model for our two registers is **Primitive Irish in Ogham becoming Old Irish**. Endings were lost, and the mutations those endings had caused stayed behind as grammar. The Ogham genitive *MAQQI* 'of the son' became Old Irish *maicc* [S29] [H]. That gives us **the first builders' hand** (long old forms, which the living Rivenmen cannot sound) and **Seren's hand** (short forms carrying mutation marks) for free.
9. **Reverse-engineer from the names we already have**, as Peterson built Dothraki out of the fragments already in Martin's books [S22] [H]. Our names already fix a good deal (§1). For example, the thunder-break always falls **after the first syllable**, and every Mystaeri compound is **modifier + head**.
10. **Make the non-linear script decodable** with the four things every successful two-dimensional notation has [S34] [S35] [M]:
    - a small closed set of primitives;
    - positional rules that carry roles;
    - explicit links that bind arguments;
    - one canonical way to read it out in a line.

    Then test the round trip: text to drawing, and back to the same text.
11. **Render both hands as generated SVG paths, not a font.** Seed the generator from the text, so the same leaf is the same drawing for every player. That is the Book's own law of determinism [C1 §1]. Draw each cut as two flat facets, one lit and one shaded, which is the V-cut of a real letter-cutter [S41] [H]. It needs no filters, and it themes with CSS tokens.
12. **Assume players will decode it.** Tunic's players broke its script [S44] [H]. So each locked leaf must either be a truthful encoding or not be shown at all. Never show pseudo-text. Jack needs to decide whether that includes the first spread's wood leaf, which holds the ending (§7).

---

## 1 · WHAT THE CANON ALREADY COMMITS US TO

This is the Peterson step: treat the existing names as data the language must explain [S22]. Everything here comes from [C1]–[C4] and should be treated as fixed.

### 1a · The Mystaeri thunder-tongue: what the names imply

The data are the roots *ael, thar, varen, saen, vael, seth* (pl. *sethen*), *thae, lea, ralen, nael, rhen, eir, nei, ress, lenth* and *-ear*, and the names built from them: *Aelvaren, Sethvaren, Saenvael, Naelsaen, Thaesaen, Leavaren, Vaelress, Ralensaen, Rhenvael, Esthaer, Senneir, Eirlenth, Naelthar, Neivaere, Naelear, Rhenear*, and the six Tides.

- **Consonants: seven, and no oral stops.** Every root uses only *v, th, s, l, r, rh, n*, sometimes doubled (*ss, nn*). There is **no p, t, k, b, d, g, and also no m, f, h, w or y** in any Mystaeri root. That phonaesthetic is rare and striking: fricatives, liquids and a nasal, "wind in branches". [H as data; the reading is L]
- **Vowels: front and open only.** The vowels are *a, e, i* and the diphthongs *ae, ea, ei*, with **no o and no u** (the only *o*-root, *orn*, was removed in the originality pass [C4]). So Shoreland can own the back rounded vowels, and the two tongues will sound unlike each other at once. [H as data]
- **The thunder-break is syllabic, not morphemic.** It falls **after the first syllable** every time. *Ra'lenthae* and *Ra'lensaen* settle it: the break comes inside the root *ralen* (*ra.len*), not at the root boundary (*ralen'thae*). The rest agree: *Ael'thar, Lea'thae, Es'thaer, Sen'neir, Nei'vaere, Rhen'ear*. [H as data]
  - **What it can be:** a glottal catch with a fall in pitch on the first syllable, somewhat like the Danish *stød*. That gives every word of two or more syllables one "knock". Speech then sounds like drumming, which the canon already says: "knocking and knocking out of the grey; the soldiers on our wall call it the drums" (III.1, [C1]). [L]
  - **The carved form drops it** ("the thunder is for the moment, the softness for always", II.2). So each grain sign has a **soft reading**, its unbroken name.
  - This is the one fantasy apostrophe that means something. Crafting Languages argues an apostrophe earns its place only when it marks a real break or sound [S38] [M].
- **Compounds are consistently modifier + head,** that is, left-branching:
  - *Nael-saen* 'mist-heart', *Thae-saen* 'tide-heart', *Rhen-vael* 'stone-grain', *Eir-lenth* 'long-winter';
  - *Lea-varen* 'new-growth bearer' and *Seth-varen* 'carving-bearer' (object + agent);
  - *Vael-ress* 'grain-rot', every Tide name (*Lea-thae* 'green-tide', and so on), and *Ael-ralen* 'bond-roots'.

  That points to a **head-final** language: noun-final, verb-final, with postpositions. This is the natural contrast with a verb-first Shoreland. [M]
- **-en is a plural:** *seth / sethen*, and *ralen* 'roots' is plausibly *\*ral* + *-en*. *Varen* 'bearer' is then either a homophonous agent suffix *-en* or a lexicalised form. That kind of natural homophony is fine (English *-s* is both a plural and a verb ending). [M]
- **Dialects exist.** "Each deep of the forest speaks it its own way" (II.2). The grain is valid **across** them, which is exactly what makes it semasiographic: it is tied to no single spoken language [S30]. [H as canon]
- **An irregularity already explained by history** (a worked example, [L]). The ending "those of" has two spellings, *-aer* and *-ear* [C4].
  - Suppose older *-aer* became *-ear* by **metathesis**, a common real sound change.
  - Then *Naelear* and *Rhenear* are the living forms.
  - The Rivenmen's exonym *Mystaeri*, "they named the senders the Mystaeri, the mist-folk", would be an *early borrowing* that kept the old *-aer* and added a Shoreland plural *-i*. Loanwords often keep a shape the source language later lost.
  - The eldest Throne, *Esthaer*, can be read either as *es + thaer* or as a relic *-aer*.

  This is the Tolkien move: the irregularity *is* the history.

### 1b · The grain: what the canon already specifies

- **The Law of the Rings** [C3 §2]: "A sapling-hull holds one sign. A hull of forty rings holds a phrase ... a sentence ... a judgement." The Book of Knowings adds that each Tide "cut the same root and added to it, as a tree adds a ring, so that the eldest carvings are the youngest ones grown old" [C1 appendix]. **Ring count equals complexity, and the root sits at the heart.** [H]
- **Ten root signs, each already given a shape** [C1 appendix; C2 §9a]:

  | Root sign | Shape |
  |---|---|
  | the Wave | one stroke curling forward |
  | the Lone Stroke | a short cut running ahead of a long one |
  | the Bar Before | a bar laid across a stroke |
  | the Spark | a cut ending in a star-notch |
  | the Mute Square | a closed square: *how they cut the word for stone* |
  | the Two Mouths | two strokes side by side, one hollow |
  | the Turned Stern | a stroke that hooks back on itself |
  | the Breath | a gap left open between two cuts |
  | the Knot | a stroke that stops in a knot of the grain |
  | the Smoothed Cut | filled and smoothed, felt and not seen |

  There is also ***Burn***, cut in the Fall.
- **Seren can read the root by eye; only the Bonded can know the rest** [C1]. The script must make the root **visually separable**, at the heart and bigger than the rest, while leaving the other rings legible *to the player's rules* and not to Seren's eye. That irony is worth keeping: the player can eventually decode by rule what Seren never could.
- **Three movements parted by a grain-rule** (`<!-- RING -->`) in every whole wood leaf [C1 §delivery]. These map to the heart band, the middle band and the bark band.
- **A Throne's groan closes a pale ring in its bark** [C2 T-rules]. The rings are already a visible counter in play.
- **The carvings' English already carries a lexicon of metaphor** [C2]. A *bough* is a hull. *Root* is the hull that goes first ("As root to water, go"). *Thin wood* is a cheap hull. *Wood is ash* means sunk. *Stone* is the wall and the Rivenmen. A gun is *a flash* or *speaks*. The grain's lexicon should be built from these metaphors, which is Peterson's "lexicon from culture" [S21].

### 1c · Shoreland: what the names imply

- **Names:** Rhyna, Halvard, Halyna, Seren, Tarnel, Kael, Voss, Hale, Brenn, Marl, and the pair-names Aldwena and Idrenna.
  - Together they give **stops** (*t, d, k, b*), plus *m, h, w*, *rh* and *y*, and the vowel *o*. They sit at the opposite pole from the Mystaeri inventory, which is good. [H as data]
  - *Rh-* word-initially and *y* as a vowel already give a light Welsh colour. Keep it light (§4d).
- **The sealing-name:** *Halyna* = *Hal(vard)* + *(Rh)yna*. The second name loses its initial *Rh*. That is exactly what **compound lenition** would do. In Welsh and Irish the second element of a compound lenites, and Welsh *rh* softens to *r* [S24]. In a cluster after *l*, the weakened *r* can then drop. [L: a proposal that turns Jack's blend into grammar]
- **English words in the Book are Seren's translations.** These include Stonewright, Stonwryt, Theolith, the Aetherbond, and the haven names: Eldhythe, Tidesmeet, Carnhold, Holtward, Fenholm, Emberhythe, Rimewatch, Glasspire, Sandreach and Highreach.
  - The tongue should supply a Shoreland original behind each one, cut in the course-hand on maps and capstones. The Book keeps its English.
  - Many real names work like this; *Dublin*, for instance, is Irish *Dubh Linn*, 'black pool'. [M]
- **Name clash to handle quietly:** *Seren* is the ordinary Welsh word for "star". Jack's name stands. But the lexicon **must not** make *seren* mean "star": that would be a lifted word. Give it an etymology of its own (§4d). [H that it is Welsh; L the remedy]
- **The old register** has a physical home. It appears in:
  - the Stonwryt cut under capstones;
  - the Rite of the Cornerstone's slate leaves, and the small-hand leaf about the hearth-custom at the bottom of the chest (I.4);
  - the Epilogue's inscription, which is `MIXED`: "stone letters on wood that became stone" [C1].

  So **the two hands must meet on one surface**: straight courses of stone letters laid across a ring-face. The design should make that one image look inevitable.

---

## 2 · ARRIVAL'S HEPTAPOD WRITING: TAKE THE IDEA, AVOID THE LOOK

### 2a · Facts

- **Source text.** In Ted Chiang's "Story of Your Life" (1998), *Heptapod B* is a semasiographic script with no spoken form. Its units are *semagrams* (not logograms, since they stand for no spoken words). They are arranged in two dimensions, not in rows. Meaning is inflected through the curvature, thickness and undulation of strokes and through the relative size and orientation of the parts. In Chiang, the orientation of strokes separates subject from object. A writer must know the whole sentence's layout before making the first stroke [S1] [H].
- **The spoken language, Heptapod A, is unrelated to the writing** [S1] [H]. Our case is different in a useful way. The grain has **soft readings** in the thunder-tongue (§1a), and it is **valid across dialects**.
- **Film design.**
  - Production designer **Patrice Vermette** worked out what each part meant.
  - Artist **Martine Bertrand** conceived the look: forms that are "inky and smoky", "tendrilled circles" [S1] [S3] [S5].
  - About **100** logograms were designed and **71** used on screen [S1] [H].
  - The team's research looked at Asian, Arabic and North African writing [S3] [M].
  - The film's own devices: **stroke weight carries tone**, where a thicker swirl means urgency and a thinner one quiet; a small **hook turns a statement into a question** [S3] [M].
  - Stephen and Christopher Wolfram split each logogram into **12 sections** and looked for repeats, and published the notebook code [S1] [S2] [S4] [H].
  - Linguist **Jessica Coon** annotated the characters as if analysing them for real [S1] [H].
- **The look in one sentence:** one closed ring of black ink on a pale, fogged glass, with smoky density variations, blots and tendrils coming off it, no start and no finish, made in a single gesture. [H, from the film and sources]

### 2b · What we take and what we leave

| Arrival | The grain |
|---|---|
| One ring per sentence | **Many concentric growth rings** per carving; one ring per growing |
| Ink, smoke, soft gradients, blots | **Crisp incised cuts** in a wood surface, lit and shaded facets, no gradients |
| Meaning attached around and outside the rim (tendrils, hooks) | Meaning carried by **marks that cross the rings inward of the bark**; nothing leaves the bark edge |
| No direction: the circle has no start or end | **Directional:** heart = beginning, bark = end; the root at the heart sets the reading axis |
| Stroke weight = tone and urgency | Weight carries **nothing**. Class is carried by *line quality*: straight for stone-world things, curved for wood-world things (§5c) |
| A hook makes a question | Questions come from structure, e.g. a mark ending **open** at the next ring (the Knowing's "Look, then go") [L] |
| Segmented into 12 around one circle | **No fixed sector count**; angle is either free (relations run by rays) or tied to the game's bearings (§5c) |
| Timeless, simultaneous | **Made of time:** rings are growings, and the Law of the Rings is literal |
| Written in one gesture | **Grown and cut over years**; a later carving literally contains its earlier form (§5c) |

**What we may keep openly, because it is an idea and not a design:** meaning over sound; being taken in whole; a writer who must hold the whole before cutting. The canon's version of the last point is "known whole, as memory". In Arrival the medium is the writing's *shape*. In ours it is *touch*. Mystwood gives its meaning to the palm. [L]

---

## 3 · STROKE AND STEM SCRIPTS: OGHAM, RUNES, TENGWAR, CIRTH, AND GAME HANDS

### 3a · Ogham (the spirit we want)

- **What it is.** Ogham dates from roughly the 4th to the 6th centuries AD, with about 400 orthodox stone inscriptions, mostly in Munster. They are in Primitive Irish, later Old Irish [S6] [H].
- **How it is built.**
  - Four ***aicmí*** ('families') of five letters each. The first family is scores to the right of the stem, the second to the left, the third crossing it at a slant, and the fourth (the vowels) short notches across the stem [S6] [S7] [H].
  - The stem (*druim*) is usually **the edge (arris) of the stone**. The inscription reads **bottom to top** [S6] [H].
  - Five extra letters, the ***forfeda***, were added later, mostly in the manuscript tradition. **Feather marks** sometimes mark where a text begins [S6] [H].
- **The tree-names are later.** Each letter's link to a tree comes from medieval scholarship (*Auraicept na n-Éces*, *In Lebor Ogaim*, *Bríatharogam*) and postdates the stones [S6] [H]. Ogham's association with trees is therefore *not* ancient. It is a later scholarly layer, and the "tree alphabet" idea is a well-worn trope we should not echo.
- **What we take:** strokes grouped on a line; a hand made for **edges and courses of stone**; systematic families of letters. [L]
- **What reads as a copy:**
  - letters that are **counts of one to five parallel strokes**;
  - strokes either side of, or through, a **central** line;
  - **vowels as notches on the line**;
  - feather marks;
  - reading **up** an edge;
  - five-letter families named after their first letter;
  - letter names that are trees. [H]

### 3b · Runes

- **Facts.** The Elder Futhark has 24 runes in three **ættir** of eight. The oldest full row is on the Kylver Stone, about AD 400. Runes are angular because, cut **along** a stave's grain, a horizontal stroke is less legible and can split the wood, so they have **no horizontal strokes**. The Younger Futhark cut the row to 16. Bind-runes (ligatures) were used inconsistently [S8] [H].
- **What we take:** the lesson that **the medium shapes the letters**, which is also the core of neography practice: incision gives straight lines because curves are hard to cut [S37] [H].
- **What reads as a copy:**
  - any letter identical to a Futhark rune (ᚠ ᚢ ᚦ ᚨ ᚱ ᚲ ᚷ ᚹ ᚺ ᚾ ᛁ ᛃ ᛇ ᛈ ᛉ ᛊ ᛏ ᛒ ᛖ ᛗ ᛚ ᛜ ᛞ ᛟ);
  - tall staves with branches;
  - a row named after its first letters;
  - bind-rune monograms as a look. [H]

### 3c · Tolkien's Tengwar and Cirth

- **Tengwar** are *featural*. A **stem** (*telco*), long or short and raised or lowered, combines with one or two **bows** (*lúva*). The letters fill a grid of **series** (place of articulation) by **grades** (manner). Vowels are ***tehtar***, marks above or below the consonant. The script has "modes" for different languages. It lives in the Private Use Area under the ConScript registry [S9] [H].
- **Cirth** are made of **a stem plus branches** on one or both sides, designed for carving. In the Angerthas Daeron, **adding a stroke to a branch marks voicing**, **moving the branch marks a spirant**, and **branches on both sides add voice and nasality**. The singular *certh* comes from an Elvish root meaning 'cleave, cut' [S10] [H].
- **The principle is general and usable:** a featural design, where related sounds get related shapes. Hangul, Pitman shorthand and Canadian syllabics all use it. [H]
- **What reads as a copy:**
  - stem-and-bow letters with vowel marks above;
  - a Cirth-like stem where **the number or side of the branches** encodes voicing and nasality in Daeron's pattern;
  - anything that looks like the Angerthas;
  - any script name built on a Tolkien root. [H]

### 3d · Game scripts to steer clear of

| Script | Its signature | Distance we keep |
|---|---|---|
| **Trunic** (*Tunic*, 2022) | A phonetic cipher of English. A **horizontal line runs through the middle** of each glyph; **hexagon edges are vowels** and **radial lines consonants**; a small circle at the bottom reverses the order; the line joins the characters of a word [S11] [H] | Our line is a **bed at the foot** of the letters, never through their middle. No hexagon lattice. Not a cipher of English |
| **Nomai** (*Outer Wilds*) | **Branching spirals**; each spiral is one speaker; a conversation is a tree of spirals [S12] [H] | No spirals, no branching vines, no colour per speaker |
| **Circular Gallifreyan** (Sherman, 2011) | A **circle per word inside a circle per sentence**, with letters as arcs and dots on the circle, read **anticlockwise from the bottom** [S13] [H] | No discs within discs, no dots on rings. We read **clockwise from the root's axis**, heart outward |
| **Dovahzul** (*Skyrim*) | **Claw-scratch** triplets with a dot or hook for the dewclaw, cuneiform-inspired [S14] [H] | Our cuts are chisel-straight and bedded on a line; no triple slashes |
| **Sheikah** (*Zelda*) | Angular glyphs, **each boxed in a square**, a cipher of Latin letters [S15] [H] | No boxed letters; a whole *word* is the stone, not a letter |
| **Kryptonian** (*Man of Steel*, Schreyer) | Glyphs set inside the **shield shape**; every glyph has a **closed cell** to show its orientation [S16] [M] | We take the *lesson* (a built-in orientation cue, i.e. the root's axis) and not the frame |
| **The Elden Ring** emblem | **Overlapping, interlocking ring arcs**, each a Great Rune, with a golden glow, in a world of a great tree [S17] [M] | Our rings are **complete, concentric, eccentric growth lines**; nothing interlocks; no gold light; no staff line through them |
| **Heaven's Vault** "Ancient" | Chinese-inspired compound glyphs in a line, built from "atoms" [S35] [H] | We take the method (atoms compound), not the look |

---

## 4 · HOW NATURALISTIC LANGUAGES ARE BUILT, AND THE CELTIC FEEL

### 4a · Tolkien

- **Language first, then the world for it.** Tolkien's own famous phrasing is "The 'stories' were made rather to provide a world for the languages." He held that a language needs its own history, a history of its speakers, and a mythology [S18] [H].
- **Proto-roots and regular sound changes.** In the 1930s *Etymologies* he built proto-roots (Primitive Quendian, Common Eldarin) and derived the daughter languages from them by regular sound change [S18] [H].
- **Constant revision.** He worked in three long periods on about fifteen languages and dialects, and never finished [S18] [H].
- **Real models for aesthetics.** Quenya's morphology draws on Finnish; Sindarin's sound changes on Welsh, chosen to fit the "Celtic" feel of its speakers' legends [S18] [S20] [H].
- **Phonaesthetics.** *A Secret Vice* (1931) argues that making languages and making myth are "related functions", and it muses on the fit of sound to meaning [S19] [H].

**For us:** the names are "given first" by Jack, and the tongues must be fitted under them. We should also let the history show in exceptions, as with *-aer* and *-ear* (§1a). [L]

### 4b · Peterson and Rosenfelder

- **Peterson** (*The Art of Language Invention*, 2015) covers sounds, words, evolution and writing. He builds a **proto-language and evolves the daughter from it**: he sketched High Valyrian's verb system *and its ancestor's* [S21] [H].
- **For Dothraki** he took the handful of words already in Martin's books (*khal, khaleesi, arakh*) and built a consistent language that could have produced them. For example, *-eesi* was made a regular feminine ending after the fact [S22] [H].
- **Rosenfelder** (*The Language Construction Kit*) gives the order of work: sounds, then lexicon, then grammar, then script, then texts. Working backwards from a text breeds inconsistency. He also offers a Sound Change Applier, so the history can be computed rather than hand-applied [S23] [H].

**The shared practices:**

1. **Phonology and phonotactics first.** Choose the inventory, the syllable shapes and the frequencies, and keep a *frequency skew*: some sounds common, some rare. Real languages are never uniform. [H]
2. **Don't relex English.** Build words by *semantic field* and by the culture's metaphors. Let one word cover two English words and one English word need two native words. Let polysemy happen [S23] [H].
3. **Derive; don't list.** Most vocabulary should come from a few hundred roots through productive affixes and compounds. Heaven's Vault's "atoms" are the game version of this [S35] [H].
4. **Irregularity lives in the frequent words** (*be, go, have, give*), because those are the ones old enough to have been worn down. Generate it with sound changes, never by fiat. [H]
5. **Idioms and set phrases** make a language feel lived-in. Keep a small phrasebook of what people actually *say*: greetings, oaths, the hearth-formula "We remember". [M]

### 4c · Celtic typology as *feel* (the features, not the words)

| Feature | The real thing (for reference only) | A Shoreland version (proposal, [L]) |
|---|---|---|
| **Initial mutation** | Welsh has three mutations. Soft: p→b, t→d, c→g, b→f, d→dd, g→∅, m→f, ll→l, rh→r. Nasal: p→mh, t→nh, c→ngh, b→m, d→n, g→ng. Aspirate: p→ph, t→th, c→ch. So *tad* 'father' gives *ei dad* 'his father', *ei thad* 'her father', *fy nhad* 'my father' [S24] [H]. Irish has lenition (written with *h*: b→bh) and eclipsis (a prefixed letter: b→mb, c→gc, t→dt). So *a bhád* 'his boat', *a bád* 'her boat', *a mbád* 'their boat': **the mutation alone carries the meaning** [S25] [H] | Two mutations, **softening** and **nasalising**, with *our own* outcomes and *our own* triggers: possessives, the object after a verb-noun, the second element of a compound (§1c). Show the mutation in the script with a mark that **keeps the base letter visible** (§6c) |
| **Where mutations came from** | They were once automatic sound effects. Once the final syllables that caused them were lost, they became grammar: Ogham *MAQQI* 'of the son' → Old Irish *maicc* [S29] [H] | The **old register** keeps the long endings and writes no mutation. The **living** hand has lost the endings and writes the mutations. That gives two registers from one history, and a real reason the Rivenmen cannot read the first builders |
| **Verb-first order** | The Celtic languages are rigidly VSO [S28] [H] | VSO in statements. A fronting particle for emphasis, like the canon's "one said, and the other finished", can create a cleft |
| **Two verbs "to be"** | Irish has the substantive *bí/tá* (state, location) and the copula *is* (identity, class) [S28] [H] | A **state-verb** ("the wall stands broken") and an **identity-particle** ("it is a wall"). This gives Halyna's paired lines a grammatical shape |
| **No verb "to have"** | Irish *tá ... agam* 'is ... at me' = "I have"; *agam, agat, aige, aici* ... are a preposition fused with a pronoun [S27] [H] | **Conjugated prepositions** built on our own prepositions. Possession is "*at*" a person; knowledge is "*in the hands of*" a person. So Seren's line becomes something like "not yet in their hands is the deep of this", which keeps the canon's own verb *hold* [L] |
| **Feelings are on you** | The Irish idiom type: "sorrow is on me" [H] | Make it masonry: feelings **are laid on** a person, as a course is laid ("grief is laid on me") |
| **Verbal nouns instead of infinitives** | Irish *tá mé ag scríobh* 'I am at writing'; Welsh *dw i'n darllen* 'I am reading' (periphrastic, with a verbal noun) [H] | Progressive = the state-verb + "at" + a verbal noun: "*is the Keep at mending*" |
| **Broad/slender harmony** | Irish spelling rule *caol le caol agus leathan le leathan*: a consonant is flanked by vowels of the same class (e, i slender; a, o, u broad), which shows whether it is palatalised or velarised [S26] [H] | **Vowel harmony by class across a whole word-stone**: a word is broad or slender. The script shows the class *once per word*, not by spelling extra vowels (§6c) |
| **Counting in twenties** | The traditional Welsh and Irish count by scores, e.g. Welsh *deugain* 40 = 'two twenties' [H] | Count in scores. It also suits masonry: a mason's tally |

### 4d · Keeping Shoreland off other people's languages

- **No real Celtic words with their real meanings.** Check every Shoreland root against Welsh (Geiriadur Prifysgol Cymru), Irish (teanglann.ie; eDIL for Old Irish), Scottish Gaelic, Breton, Cornish and Manx. Welsh *seren* 'star' is the live case (§1c). [H method]
- **Don't look Welsh or Irish on the page.** Welsh spelling in full (*ll, dd, ff, w* and *y* as vowels, *ch* all together) reads as Welsh at a glance. Irish digraphs and eclipses (*bh, mh, gc, dt, bhf, ao, aoi*) read as Irish. Keep *rh* and vowel *y*, which Jack's names use, and choose our own romanisation for the rest. [M]
- **Not another Sindarin** [S20] [H]:
  - no plural by vowel change as the main plural (*adan → edain*, *orod → ered*);
  - no article *i* that triggers soft mutation;
  - no Sindarin or Quenya roots. For our semantic fields the dangerous ones are *sarn, gond* 'stone', *ondo, galadh, orn, eryn, taur, hîth* 'mist', *mith, nen, duin, dor, ost, barad, aran*, and the endings *-ion, -iel, -dor*. The name map's check against Eldamo and Parf Edhellen stays the gate [C4].
- **Personal names can keep their surface and gain new meaning.** Halvard is glossed in the canon from Old Norse "rock-guardian" [C3]. The tongue may give it a Shoreland etymology instead, so that the Norse gloss becomes a folk comparison. That is Jack's call; a single name is not a lift either way. [L]

### 4e · The Mystaeri contrast (to keep the tongues unlike each other)

| | Shoreland | Mystaeri |
|---|---|---|
| Consonants | stops, *m, h, w* | seven continuants; stops only as the thunder-knock (§1a) |
| Vowels | back vowels; broad/slender harmony | front vowels and *ae, ea, ei* only |
| Word order | verb-first; prepositions | head-final; postpositions; modifier + head compounds |
| Grammar | fusional mutation | agglutinative compounding |
| Stress and rhythm | musical, initial stress | one knock after the first syllable |
| Script | the course-hand: an alphabet, straight, linear | the grain: semasiographic, curved, ringed |

---

## 5 · SEMASIOGRAPHIC WRITING, AND HOW TO MAKE A NON-LINEAR SCRIPT DECODABLE

### 5a · Real systems

- **Sampson's distinction.** *Glottographic* writing records a spoken language; *semasiographic* writing records ideas, tied to no one language. Many scholars keep the word "writing" for the first kind only [S30] [H].
  - **Blissymbolics** is the standard modern example. It composes meanings from a small set of shapes and is used in augmentative communication [S30] [H].
  - **Caution:** the famous "Yukaghir love letter" on birch bark, often cited as complex semasiography, was shown by DeFrancis to be something else and arguably not communication at all [S30] [H]. Don't lean on it.
- **Notations are everyday semasiography, and they are 2-D and rule-decodable** [H]:
  - **mathematics**, where position carries operation (exponents, fractions);
  - **music**, where the vertical is pitch, the horizontal is time, and stacking means simultaneity;
  - **chemical structure diagrams**, which are graphs with a **canonical linear form**, such as a systematic name.

  The last is the closest model for the grain: a drawing with many valid layouts and *one* canonical reading.
- **Read by touch.**
  - The **lukasa** of the Luba (in present-day DR Congo) is a wooden memory board of beads, shells and carved signs. Court historians, the *bana balute* or "men of memory", **read it with the fingertip** while reciting genealogies and histories [S31] [H]. This is a real precedent for "Mystwood is known by touch", **for influence only**. It is a living cultural object, so we take no forms from it.
  - The **khipu** of the Inca records in knots. Its decimal *positional* system is deciphered; about a third of khipu are not decimal and may carry narrative (Urton) [S32] [H]. It proves knots can carry structure, which suits the Knot.
  - **Rongorongo**, carved on wooden tablets, reads in *reverse boustrophedon*, turning the tablet at each line [S33] [H]. It shows that *handling the object* can be part of reading it.
- **A conscript that solves our exact problem.** Alex Fink and Sai's **UNLWS** (2010) is unspeakable and fully 2-D. Glyphs are predicates, and **lines join glyphs to show which arguments share a referent**. There is no reading order [S34] [H]. This is the rule-engine the grain should imitate *functionally*: our **rays** do the job of UNLWS lines. UNLWS looks like nothing we plan (it is a pen-drawn network), so the risk of a look-alike is low. [M]

### 5b · Games

- **Heaven's Vault** (inkle, 2019).
  - "Ancient" builds words from atoms, compounds them, and has a real grammar and about 3,000 words [S35] [H].
  - The player picks glosses per word. The game narrows wrong options and never fails the player, since every plausible translation feeds the story. A fatigue meter stops brute force [S35] [H].
  - Inkle framed it as making players *feel* like translators, the "Guitar Hero of linguistics" [S35] [M].
- **Chants of Sennaar** (Rundisc, 2023). Each floor of the tower has its own glyph language, over 100 glyphs in all. A notebook fills glyph by glyph and confirms guesses from context [S36] [H].
- **Tunic** (2022). The manual and signs are in an undeclared phonetic cipher that the game never teaches, and players cracked it [S11] [S44] [H]. **The lesson: whatever we encode, some player will read.**
- **Outer Wilds.** The Nomai spirals are translated by a tool the player carries [S12] [H]. Rivenkeep's version is the Knowing ladder.

### 5c · Rules for a decodable grain (a proposal for the design step, [L])

**Surface.** A cross-section, or "round", of Mystwood contains:

- a **pith** (the heart point), slightly off-centre;
- growth rings, each drawn as an **earlywood/latewood pair**, so rings read as rings and not as circles;
- **heartwood** (dark), then **sapwood** (light), then a rough **bark** band.

**Reading.**

1. **Heart → bark** is the order of knowing. The **three bands are the three movements**, and the heartwood/sapwood boundary is the Book's grain-rule.
2. **The root sign sits at the heart** and is the largest mark. Its direction (where the Wave curls, which way the Lone Stroke runs ahead) is **the axis**. All angles are read **clockwise from the root's axis**. That is the orientation cue Kryptonian's closed cell provides [S16], built from our own material.
3. **One marked ring is one clause, or one knowing.** Unmarked rings between marked rings are **time**: *n* empty rings means "after *n*", which matches "when the second falls" and "the fourth time, mean it". The count is exact, so it is meaning. The *width* of each ring is not meaning; it is seeded and bounded variation.
4. **Marks cut across rings.** A mark spanning rings *i* to *j* has scope over those clauses (an order that "holds until").

**Line quality is a classifier,** like an Egyptian determinative:

- **straight-edged marks are stone-world things**: the wall, the gun, the Rivenmen. The canon's Mute Square, "how they cut the word for stone", is the seed;
- **curved or organic marks are wood-world things**: hull (*bough*), root, mist, water, fire.

**Primitives to start from.** Keep the inventory **small and closed**: about 40–80 marks. For scale, Arrival designed about 100 and used 71 [S1]; Kryptonian had about 300 words [S16]; Heaven's Vault about 3,000 [S35].

| Primitive | Meaning |
|---|---|
| **cut** (across rings) | an act |
| **enclosure** (the square is the only straight one) | a thing |
| **notch** along a mark | a count |
| **hollow** (an outline cut) | shown, not meant: the Two Mouths, deceit |
| **smoothed** (relief only, no cut shadow) | hidden: the Smoothed Cut |
| **knot** (the rings bulge around it, as real grain flows around a branch) | hold or wait: the Knot |
| **check** (a radial split from the bark inward) | fail or turn aside: "where bark splits" |
| **fire scar** (a charred wedge the later rings heal over) | *Burn* |
| **fork** (a mark that splits) | a branch in the plan: if/then (the Last Tide) |
| **ray** (a hair-line through several rings) | **the same one as**: argument binding, as with UNLWS lines. "The west waited for the east" is a ray from a west-mark to an east-mark |
| **a ray running inward** | memory: the Tide of Remembering, "the memory that runs back through the roots" |

**Carvings grow literally.** Each carving's inner rings **are exactly** the carving it "grows from" in the Admiral's line tables [C2 §16]. So E2-02 *The Sounding* is E1-03 *Go Until Struck* with more rings added. That is the canon ("a Rivenman who has read the young wood can read the root of the old"), made visible and exact.

**Tides as growth forms.**

| Tide | Form |
|---|---|
| Hasty | a sapling round: pith plus one sign |
| Second | one more marked ring (a phrase: two signs) |
| Remembering | inward rays appear |
| Joined | **several piths inside shared outer rings**. Stems that grow together really do this. It is the dark mirror of the Aetherbond, two made one, drawn and never explained |
| Deceit | hollow and smoothed marks appear |
| Last | forks appear |
| Thrones | a full bark band carrying the Throne's **name-sign**, and a pale ring closing in the bark at each groan (canon) |

**One drawing, one reading. One reading, one drawing (up to noise).** Define the quantisation so that noise can never cross a threshold: a mark can never drift into the next ring, and an angle can never cross into a neighbouring bearing. The fan-built Nomai "scriptorium" makes the same promise for its spirals ("every drawing has exactly one reading") [S12] [M]. That is the standard to meet.

**Canonical linearisation.** Read heart → bark, ring by ring. Within a ring, read clockwise from the axis. Rays read as "(the same)". This gives the gloss order, the alt text and the round-trip test.

**Angle (a choice for the designer).** Either (a) angle is free, with only rays carrying relations, or (b) angle is **bearing**, so that the round is a map of the roads, with "three roads, one hour" drawn as three marks at three bearings joined by a ray. Option (b) is more iconic and ties directly to the sim's bearings. **I recommend (b)**, with the root axis as the fleet's heading. [L]

**Soft readings.** Every primitive and fixed compound has an unbroken thunder-tongue name, e.g. the Mute Square is soft-read *rhen*. This fulfils "carve Aelthar whole and soft". The **carved** names in the canon are these soft readings.

---

## 6 · RENDERING BOTH HANDS AS CLEAN SVG

All of this is generator guidance. The generators live in `scratchpad/wf6`; the repo receives only the HTML output (Jack's rule: documents only).

### 6a · Shared practice [H unless marked]

- **Generate paths; don't ship a font.** The Docs need no font loading and no Private Use Area code points. If the game engine later wants live text, register a PUA block in the manner of the **UCSUR** (the successor of the ConScript registry, which is how Tengwar, Cirth and sitelen pona have been handled) [S43] [S9]. **Never use the Ogham block (U+1680–169F)** [S6]: it is someone else's script.
- **Deterministic.** Seed a small PRNG (e.g. mulberry32 over an FNV-1a hash) from the leaf ID and the text. Never use an unseeded random. The same leaf gives the same drawing for everyone, which is the Book's law [C1 §1].
- **Coordinates.** Use one `viewBox` per figure (e.g. `0 0 1000 1000` for a round, and a unit em-box such as `0 0 100 140` for a letter, with the bed at y = 120). Round to one decimal. Set `width="100%"` and let the height follow, so the figure fits a phone gutter. Check that the smallest mark is still at least about 6 px at 340 px wide.
- **Reuse.** Put each course-hand letter in `<defs><symbol id="ch-…">`, placed with `<use href x y>`. Grain marks are unique per round, so draw them inline.
- **Theming.** Draw with `fill="currentColor"` or CSS variables. Use two facet tokens, `--cut-lit` and `--cut-shade`, over a surface token. Redefine them for dark mode as the Docs already do. `color-mix()` suits the ring hairlines. Never hard-code colours. Stone ink leans yellow and wood ink leans green (N7 [C1]).
- **The cut itself: two flat facets, no filters.** A V-cut letter is two walls meeting at about 90°. Under a raking light one wall is lit and one is in shadow [S41] [H].
  - Build each stroke from its centre-line P→Q with half-width *w*.
  - Make two quads: {P, Q, Q + n·w, P + n·w} and the mirror quad on −n.
  - Shade each facet by the sign of **n · L**, for one fixed light direction L (from the top left).
  - This reads as carved at any size and stays crisp in print.
  - Avoid `feTurbulence` or `feDiffuseLighting` per mark. If the page wants wood or stone texture, use one filtered background rect at most.
- **Ends of strokes.**
  - *Course-hand:* **square where the stroke meets the bed** (bedded), **tapered at the free end** (where the chisel lifts). This rule is ours and gives each letter a built-in "up".
  - *Grain:* knife-cuts, **tapered at both ends**, curves allowed.
- **Arcs.** SVG cannot draw a full circle with a single `A` command, because the start and end points coincide. Use two arcs, a `<circle>`, or better for rings, a sampled closed curve [S42] [H].
- **Accessibility.** Use `role="img"` with `<title>` and `<desc>`. For a **locked** leaf, the title says what it is ("A carving in the grain, not yet known" / "A leaf in the course-hand, not yet read") and **does not leak the English**, so everyone gets the same leaf. Once earned, the title carries the translation. Any "grow the rings" reveal animation must honour `prefers-reduced-motion`.
- **Validation (run in the scratchpad before export):**
  - round-trip every text (encode, decode, compare);
  - no two meanings give the same drawing;
  - every gap is above its minimum;
  - no ring crosses another;
  - no mark leaves its ring span;
  - the page size budget holds.

### 6b · The grain round

- **Rings.** Use r_k(θ) = R_k + e·(k/K)·cos(θ − φ) + Σ_{m=2..4} a_{k,m}·sin(mθ + ψ_m).
  - The *e* term offsets the pith (real reaction wood makes a leaning trunk's pith eccentric).
  - The *a* terms stay small and correlated between neighbouring rings.
  - Enforce R_{k+1} − R_k > 2·max|Δnoise| so rings never touch.
  - Sample 96–144 points and close with Catmull-Rom → cubic Bézier.
  - Draw each ring as a thin latewood line plus a pale earlywood band.
- **Marks follow the wood.** Place a mark by evaluating r_i(θ) and r_j(θ), so it is cut into *this* round's real ring geometry and does not float on an ideal grid.
- **Knots deform the rings:** r += A·exp(−((θ − θ_k)/σ)²)·exp(−((R − R_k)/s)²).
- **The Smoothed Cut** gets only a 1-unit lit edge and a 1-unit shaded edge, offset, with no fill contrast. It is "felt, not seen" and reads only on a second look.
- **Fire scars** are a dark wedge through the outer rings, with the later rings curling over its lips as callus.
- **Rays** are hair-lines at 0.5–0.8 of the ring line's weight, drawn from ring to ring along the sampled radii.
- **Bark.** Draw it as a rough band (a jittered outer contour). No mark may cross it outward: that is the rule that keeps us off Arrival's rim-tendrils.
- **Budget.** A round of 12 rings × 120 points plus marks comes to about 15–30 KB inline, so all 46+1 carvings on one page is fine.

### 6c · The course-hand line

- **The bed (mortar line)** is a thin horizontal band under the letters. Letters **stand on it**; nothing hangs below it except, optionally, the mutation bite. That keeps it clear of Trunic's through-line [S11] and of the hanging headline of Devanagari or Tibetan.
- **Words are stones.**
  - Draw a faint ashlar outline, or none, and use a fixed **head-joint** gap between words.
  - In multi-line text, adjacent lines **break the joint**: if a head-joint falls within *t* of a joint on the line below, widen that line's joints evenly until it doesn't (justification by mortar).
  - Reading is unaffected, since a joint is a word break whatever its width. The page looks like a wall.
- **Letter geometry.**
  - **Squat proportions** (wider than tall, like a course of stone) keep it off runes and Cirth, which are tall staves.
  - Use a small lattice of endpoints for consistency.
  - Allow horizontals and diagonals (stone has no grain); allow no curves at all.
  - Make related sounds share shapes in *our own* scheme (§8).
- **Mutation mark.** A small **"bite"**, a nick in the bed under the letter's foot, marks softening. A second form marks nasalising. The base letter always stays intact, as the dot of lenition in Gaelic type keeps the consonant readable [H]. A reader can always find the dictionary form.
- **Broad/slender.** Mark the class **once per word-stone**, e.g. the stone's first bed-segment sits a hair lower for slender words. Don't spell harmony vowels.
- **Ink form.** Seren writes the Book in ink, so give the course-hand a **book-hand**: the same skeleton, drawn with a flat pen on a ruled bed. A real parallel is the split between inscriptional capitals and pen hands. Stone rendering (facets) is for capstones and the Epilogue's inscription; the book-hand is for leaves. [L]
- **The old register (the first builders' hand)** differs from the living hand in four ways:
  - **scriptio continua**: no head-joints;
  - taller courses;
  - the **old long endings**, with no mutation bites;
  - **two or three archaic letters for sounds that have since merged**, like the Ogham letter kept after its sound merged [S6] [M].

  A living Rivenman can see every letter and still cannot *sound* the words. That is the reason for "cannot read until earned", and it is real.
- **The Stonwryt** is a **ligature** of the master-pair's sealing-name, sharing one bed and shared uprights. It is our own ligature law, not bind-rune style.
- **The Epilogue's `MIXED` inscription:** straight courses of stone letters laid across a petrified round, with the rings running *under* the bed. Both hands on one surface.

---

## 7 · THE CONCEIT IN PLAY: LOCKED LEAVES, TABS, AND WHAT MUST BE TRUE

- **The locked wood leaf is already described by the canon.** The Epilogue's facing leaf "stood empty ... with the grain drawn on it and one line" [C1].
  - So a locked wood leaf shows **the grain** of its carving (Mystaeri), plus **Seren's one line in the course-hand** (Shoreland), which means *"Untold. Halyna cannot yet hold this deep."*
  - Both hands appear on the first spread from the first minute. That answers Jack's request exactly.
- **The Knowing ladder maps cleanly onto glossing:**

  | Canon stage | What the leaf shows |
  |---|---|
  | **Blank** | the grain, unglossed |
  | **Fragments** | the marks already known get English glosses beside them; the rest stay **[ ]** ("the shape only") |
  | **Whole** | the telling in English, with the round kept above it. "The Book never removes a word" |

  The root sign is glossed first, as the canon requires ("until then only its root sign shows").
- **Locked stone leaves** show Seren's text in the course-hand book-hand. **Old-register** pieces (the Rite's slate leaves, the hearth-custom leaf, the Stonwryt) stay old-hand until a specific achievement.
- **Tabs (Jack's second note).** Earned leaves toggle **Book | Modern**. A locked leaf shows its original hand under *either* tab, because there is nothing yet to translate. Optionally add a third view, **Original**, for earned leaves: the facing-page bilingual edition, as in classical text series. It lets decoders check their work. [L]
- **Truth or nothing.** Players decode (Tunic [S44]), so every shown line must be a **truthful encoding**. Scope decides the cost [L]:

  | Tier | Content | Lexicon needed |
  |---|---|---|
  | 1 (must) | Seren's *Untold* line; the 46 carvings and *Burn*; leaf titles; all names; the Stonwryt; the Epilogue inscription | ~300–500 roots |
  | 2 (should) | the **first paragraph** of each locked stone leaf; the rest of the leaf is shown folded, not faked | ~1,000 |
  | 3 (only if Jack wants it) | whole leaves in Shoreland. The Book is ~33k words | Heaven's-Vault scale, ~3,000 |

- **Spoilers.** A truthful grain on the first spread's facing leaf would let a decoder read the Epilogue on minute one. Options:
  - (a) encode it truthfully (the reward for decoders);
  - (b) show that leaf's grain **unmarked**, rings only, until late: "the wood has not yet given its carving";
  - (c) encode only its root.

  This is **Jack's call**. I lean to (b): truthful and still a secret.

---

## 8 · DO-NOT-COPY

**From Arrival** [S1] [S3]:
- one ring per sentence;
- ink, smoke or blot textures;
- tendrils or hooks off the outer edge;
- black on pale fogged glass;
- **stroke weight as tone or urgency**;
- a hook meaning a question;
- twelve fixed sectors;
- a directionless circle drawn in one gesture;
- any heptapod term (*semagram* is a general word; *logogram* in their sense is theirs).

**From other ring and circle hands** [S12] [S13] [S17]:
- Nomai spirals and branching vines;
- Gallifreyan circles within circles, dots and arcs on rings, reading anticlockwise from the bottom;
- Elden Ring interlocking arcs, a staff line through rings, or golden glow;
- magic circles: text round the rim, inscribed polygons or stars.

**From Ogham** [S6] [S7]:
- tallies of one to five parallel scores;
- strokes either side of, or through, a central line;
- vowels as notches on the line;
- five-letter families named after their first letter;
- tree names for letters;
- feather marks;
- reading up an edge;
- the Ogham Unicode block.

**From runes** [S8]:
- any Futhark shape;
- tall staves with branches;
- bind-rune monograms;
- a row named from its first letters;
- ættir of eight.

**From Tolkien** [S9] [S10] [S20]:
- stem-and-bow letters;
- *tehtar* vowel marks;
- a series-by-grade table;
- Cirth branch-count voicing on Daeron's pattern;
- *certh*-derived or any Elvish-rooted script names;
- Sindarin's vowel-change plurals and the lenition triggered by the article *i*;
- Sindarin and Quenya roots, especially for stone, tree, mist, silver, water and land;
- the endings *-ion, -iel, -dor*.

**From other game hands** [S11] [S14] [S15] [S16] [S35] [S36]:
- Trunic: a line through the middle, hexagon edges and radials, and a circle below;
- Dovahzul claw-triplets;
- Sheikah boxed ciphers;
- Kryptonian's shield frame;
- Hangul-style syllable blocks;
- letters hanging from a headline;
- Heaven's Vault's glyph style;
- Chants of Sennaar's balloon pictograms.

**From real languages:**
- real Welsh, Irish, Gaelic, Breton, Cornish or Manx words with their meanings (*seren* 'star' is the live case);
- whole Welsh or Irish spelling systems;
- mutation tables copied exactly from Welsh or Irish.

**From the lukasa** [S31]: any of its forms. It is a living cultural object; take the idea of reading by touch only.

**Decoration without meaning:** apostrophes that mark nothing (ours mark the knock); pseudo-text anywhere a player might decode it.

---

## 9 · DO

### 9a · The grain (Mystaeri, semasiographic)

1. Build it from **real wood anatomy**: pith, heartwood, sapwood, bark, earlywood and latewood, rays, knots, checks, fire scars, frost rings, double piths.
2. **Heart = beginning, bark = end**, and the three bands are the three movements.
3. **The root sign at the heart**, the largest mark, sets the axis. Read clockwise from it.
4. Carry meaning by **marks that cross the rings**. Nothing leaves the bark.
5. **Line quality classifies:** straight for stone-world things, curved for wood-world things. Keep weight meaningless.
6. **Empty rings are time; ring widths are noise.** Seed the noise and quantise the meaning.
7. **Rays bind referents**; an inward ray is memory.
8. **Later carvings contain their earlier forms ring for ring**, following the Admiral's "grows from" chains.
9. Give each Tide a growth form: sapling, phrase, memory, **joined piths**, hollow and smoothed, fork, throne.
10. Realise the ten root signs *exactly as Seren describes them*, and draw *Burn* as a fire scar.
11. Give every sign a **soft reading** in the thunder-tongue.
12. Specify **one canonical linearisation**, and run a round-trip test on all 46+1 carvings.

### 9b · The course-hand (Shoreland, alphabet)

1. **Straight strokes only; horizontals welcome** (stone has no grain); squat letters.
2. Letters **stand on the mortar line**. Words are **stones** parted by head-joints, and lines **break the joint**.
3. Strokes are **square at the bed and tapered at the lift**; render them as V-cut facets.
4. Use a **featural scheme of our own**, with related sounds in related shapes. Check each letter by overlay against the Latin capitals, the Futhark, Ogham, Cirth, Trunic and Dovahzul.
5. A **mutation bite** that keeps the base letter visible; **harmony class marked once per word**.
6. **A book-hand for Seren's ink** and a **cut-hand for stone**.
7. **The old register:** no word gaps, taller courses, long pre-loss endings, no mutation marks, and two or three archaic letters for sounds that merged.
8. **The Stonwryt** as a sealing-name ligature on a shared bed.
9. Make it **compatible with the grain on one surface** (the Epilogue).

### 9c · The two tongues

1. **Reverse-engineer from existing names first** (§1), and treat every canon name as a fixed point.
2. Work **old stage → sound changes → living stage** for both tongues. For Shoreland, let **lost endings leave mutations**; for Mystaeri, let **-aer become -ear**.
3. **Keep the tongues opposite** (§4e): stops against continuants, back vowels against front, verb-first against head-final, fusional against agglutinative.
4. **Build the lexicon from the cultures' metaphors.**
   - Shoreland: **to tell a tale = to lay a course**, and trust is "sealed in stone".
   - Mystaeri: **to know = to hold** (the Untold line's own verb), a hull is a bough, and a scout is a root.
5. **Put irregularity in the frequent words, via history.** Keep a small **phrasebook** of what people actually say.
6. **Audit every root and whole word:** Tolkien lexicons (Eldamo, Parf Edhellen), Celtic dictionaries, and an exact-string web search against the major franchises, as the name map did [C4].

---

## 10 · FOR JACK (DECISIONS ONLY HE CAN MAKE)

1. **Spoilers on the first spread.** Should the facing leaf's grain be (a) truthful, (b) rings only until late, or (c) root only? I recommend (b). (§7)
2. **Scope.** Tier 1 alone, Tier 1–2, or whole leaves in Shoreland (Tier 3)? (§7)
3. ***Seren*** is Welsh for "star". Keep the name with a Shoreland etymology of its own (recommended), or accept the echo? (§1c, §4d)
4. ***Halvard's* gloss.** Keep "rock-guardian" from Old Norse, or give it a Shoreland etymology? (§4d)
5. **An Original tab** for earned leaves (a facing-page bilingual view), or only Book | Modern? (§7)

---

## SOURCES

**Arrival**
- [S1] Heptapod languages, Wikipedia. https://en.wikipedia.org/wiki/Heptapod_languages
- [S2] "How Science and Nerdery Combined to Create ARRIVAL's Clever Logograms", Nerdist (archive). https://archive.nerdist.com/arrival-logograms-science-nerdery-creation/
- [S3] "The Secrets Behind The Alien Language In Arrival", SlashFilm. https://www.slashfilm.com/903056/the-secrets-behind-the-alien-language-in-arrival/
- [S4] Wolfram Blog, "Analyzing and Translating an Alien Language: Arrival, Logograms and the Wolfram Language". https://blog.wolfram.com/2017/01/31/analyzing-and-translating-an-alien-language-arrival-logograms-and-the-wolfram-language/ · notebooks: https://github.com/WolframResearch/Arrival-Movie-Live-Coding
- [S5] Rama's Screen, "Patrice Vermette and Martine Bertrand on ARRIVAL Production Design And Logograms". https://www.ramascreen.com/patrice-vermette-and-martine-bertrand-on-arrival-production-design-and-logograms/

**Stroke and stem scripts**
- [S6] Ogham, Wikipedia. https://en.wikipedia.org/wiki/Ogham
- [S7] Ogham in 3D, Dublin Institute for Advanced Studies. https://ogham.celt.dias.ie/version2013/menu.php?lang=en&menuitem=03
- [S8] Runes, Wikipedia. https://en.wikipedia.org/wiki/Runes
- [S9] Tengwar, Wikipedia. https://en.wikipedia.org/wiki/Tengwar
- [S10] Cirth, Wikipedia. https://en.wikipedia.org/wiki/Cirth

**Game and fan scripts**
- [S11] Tunic Script, Tunic Wiki. https://tunic.fandom.com/wiki/Tunic_Script
- [S12] Nomai writing: https://github.com/Rytting/nomai-scriptorium · https://yanwittmann.de/projects/ow-written-nomai-lang
- [S13] Sherman's Gallifreyan, Omniglot. https://www.omniglot.com/conscripts/shermansgallifreyan.htm
- [S14] Dovahzul, Omniglot. https://www.omniglot.com/conscripts/dovahzul.htm
- [S15] Sheikah, Omniglot. https://www.omniglot.com/conscripts/sheikah.htm
- [S16] Kryptonian (Schreyer): https://www.supermanhomepage.com/movies/movies.php?topic=mos-kryptonian · https://www.rcinet.ca/en/2013/07/08/canadian-professor-created-kryptonian-language-for-man-of-steel/
- [S17] The Elden Ring (concept), Elden Ring Wiki. https://eldenring.fandom.com/wiki/Elden_Ring_(concept)

**Tolkien, Peterson, Rosenfelder**
- [S18] Languages constructed by Tolkien, Wikipedia. https://en.wikipedia.org/wiki/Languages_constructed_by_Tolkien
- [S19] A Secret Vice, Tolkien Gateway. https://tolkiengateway.net/wiki/A_Secret_Vice
- [S20] Sindarin, Wikipedia. https://en.wikipedia.org/wiki/Sindarin
- [S21] *The Art of Language Invention* (Peterson): review, The Fantasy Inn, https://thefantasyinn.com/2017/12/15/the-art-of-language-invention-by-david-j-peterson/ · review, Superlinguo, https://www.superlinguo.com/post/130226474983/the-art-of-language-invention-david-j-peterson · https://artoflanguageinvention.com/
- [S22] Dothraki language, Wikipedia, https://en.wikipedia.org/wiki/Dothraki_language · TED Ideas, https://ideas.ted.com/meet-the-person-who-created-dothraki-and-valyrian-for-game-of-thrones-and-learn-how-khaleesi-should-have-been-said/
- [S23] Mark Rosenfelder, *The Language Construction Kit*. https://www.zompist.com/kit.html

**Celtic typology**
- [S24] Welsh mutation, Wikipedia. https://en.wikipedia.org/wiki/Welsh_mutation
- [S25] Irish initial mutations, Wikipedia. https://en.wikipedia.org/wiki/Irish_initial_mutations
- [S26] Irish orthography, Wikipedia. https://en.wikipedia.org/wiki/Irish_orthography
- [S27] Irish prepositional pronouns: https://daltai.com/grammar/prepositional-pronouns/ · https://www.hofshi.net/Ceachtanna_MeanRang/IrishPrepositionalPronounChart.pdf
- [S28] The Irish copula and substantive verb: https://www.celtic-languages.org/Guide_to_Irish_to_be,_the_substantive_verb_b%C3%AD,_t%C3%A1_&_the_copula_is · Rouveret, "VSO Word Order in the Celtic Languages": https://onlinelibrary.wiley.com/doi/abs/10.1002/9781118358733.wbsyncom092
- [S29] Primitive Irish, Wikipedia. https://en.wikipedia.org/wiki/Primitive_Irish

**Semasiography and touch-read records**
- [S30] Sampson, writing systems: https://www.grsampson.net/AWsy.html · https://languagesindanger.eu/book-of-knowledge/writing/ · Unger and DeFrancis critique: https://link.springer.com/chapter/10.1007/978-94-011-1162-1_4
- [S31] Lukasa, Wikipedia, https://en.wikipedia.org/wiki/Lukasa · Smarthistory, https://smarthistory.org/lukasa-memory-board-luba-peoples/
- [S32] Quipu, Wikipedia. https://en.wikipedia.org/wiki/Quipu
- [S33] Rongorongo, Wikipedia. https://en.wikipedia.org/wiki/Rongorongo
- [S34] UNLWS: https://github.com/saizai/unlws · https://hugocisneros.com/notes/unker_non_linear_writing_system/

**Games that teach a language**
- [S35] Heaven's Vault: https://www.gamedeveloper.com/design/how-inkle-developed-its-own-ancient-language-for-i-heaven-s-vault-i- · https://kestrel-text.com/2019/05/26/designing-a-lost-language-for-heavens-vault-egx-2019/ · https://en.wikipedia.org/wiki/Heaven's_Vault
- [S36] Chants of Sennaar: https://www.axios.com/2023/09/08/chants-of-sennaar-rundisc-interview · https://en.wikipedia.org/wiki/Chants_of_Sennaar

**Script craft, wood and stone, rendering**
- [S37] "How to Create a Script", Neography. https://neography.info/how-to-create-a-script/
- [S38] "Fantasy Apostrophe", Crafting Languages. https://craftinglanguages.substack.com/p/fantasy-apostrophe
- [S39] USDA Forest Products Laboratory, Wood Handbook, structure of wood: https://www.fpl.fs.usda.gov/documnts/fplgtr/fplgtr190/chapter_03.pdf · https://www.fpl.fs.usda.gov/documnts/fplgtr/fplgtr113/ch02.pdf
- [S40] Dendropyrochronology (fire scars), Wikipedia, https://en.wikipedia.org/wiki/Dendropyrochronology · Payette et al. 2010, frost rings, https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2009GL041849
- [S41] Simon Burns Cox, stone letter carving (the V-cut), https://www.simonburnscox.co.uk/2017/10/14/stone-letter-carving-techniques/ · Letter cutting, Wikipedia, https://en.wikipedia.org/wiki/Letter_cutting
- [S42] MDN, SVG paths, https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorials/SVG_from_scratch/Paths · MDN, vector-effect, https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/vector-effect
- [S43] Under-ConScript Unicode Registry, https://www.kreativekorp.com/ucsur/ · ConScript Unicode Registry, Wikipedia, https://en.wikipedia.org/wiki/ConScript_Unicode_Registry
- [S44] PC Gamer on decoding Tunic's language. https://www.pcgamer.com/im-still-riding-the-high-of-unlocking-tunics-secret-language/

**Canon (ours)**
- [C1] `wf5/legends_v11_final.md`: the Book v1.1.0, including II.2, I.4, the Epilogue, the Book of Knowings, and How the Legends Enter the Game.
- [C2] `wf5/admiral_v03.md`: §9a root signs, §14–16 the carvings and their growth chains, the Throne rules.
- [C3] `Docs/Research/Rivenkeep_Fiction_Hooks.md`: §2 the Law of the Rings, §6 the lines, §9 the lexicon.
- [C4] `Docs/Research/Rivenkeep_Name_Map.md`: renames and the audit method.
