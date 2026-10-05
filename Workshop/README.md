# Rivenkeep Workshop

The work product behind the Legends and the Tongues docs: the sources the finished pages in `../Docs` were built from, the tools that built them, and the records of how the work was done. The finished pages live in `../Docs`; nothing here is needed to read them.

`scratchpad/` mirrors the working folder Claude used (`wf4` to `wf13` are successive stages of the work, `wf13` the newest). The scripts have the working folder's path (`/private/tmp/claude-501/.../scratchpad`) written into them, so to reuse them, copy `scratchpad/` back to that path.

## What is here

| Folder | What it holds |
|---|---|
| `wf6`, `wf7` | The first language work: the Mystaeri spec, the course-hand drawings, the Orrowen and First Tongue tools (`orr_analyze.py`, `grain_validate.py`, `render_grain2.py`, the leaf-hand and its font `GarlFlenn.woff2`), the lexicon builder and its inputs, the v1.3 Book source (`wf7/book/legends_v13.md`) |
| `wf8` | The Tier 3 translation of the v1.3 telling (units, additions, blind readings, back-translations), the grain renderer v3, and the Tongues page parts and builder |
| `wf9` | The design of the epic: the outline, the Reckoning (timeline), the cast and the puzzle pieces |
| `wf11` | The v3 Book, Plain Words and Notes sources, the voice and craft guides, the research on how great tellers build a tale, the register test, and the critics' verdicts |
| `wf12` | The v3 translation into Orrowen and the grain: units, additions, blind back-translations, the merge tools and reports, the merged lexicon, grain spec and concept map |
| `wf13` | Plain Words v3.1 (the lore primer, the 13 writers' files, the editor's log), the word-by-word glosses, and the current builders for the story page, its panes and the Notes page |

## Known quirks

- Several builders read the house look from `../Docs/Rivenkeep_Legends.html`, so that page must stay in the repo.
- The Tongues page builder (`wf8/tongues_build/build.py`) can no longer run: more than fifty of its inputs were lost before they were backed up. `../Docs/Rivenkeep_Tongues.html` is the only complete copy and is edited in place; the parts here are history.
- `wf13/extract_rom.py` and `wf13/check_gloss.py` write to or read the working folder's path directly. Don't run `extract_rom.py`: it rewrites `wf13/gloss_in/`.
- `wf13/orig/lexicon_orrowen.tsv` and `orrowen_v2.md` are relative symlinks to files elsewhere in this folder.
- The root `.gitignore` ignores `*.log`; `scratchpad/wf13/orig/.gitignore` lets the one log the builders need (`make_grain3.log`) through.

## What is not here

Browser profiles, screenshots, temporary copies, built pages, backups, superseded drafts and builders, and downloaded books and articles (other people's text) stay out of the repo. They are on the author's Mac only, in `~/code/Rivenkeep_Workshop/`.

## Keeping it up to date

`sync_workshop.py` holds the rules that decide what is work product. From a live working folder:

```
python3 Workshop/sync_workshop.py --src <scratchpad> --mode copy
```

It copies work product here and the rest to the private folder. Add `--dry` to see the sizes first. Check `git status` before committing, and add with `git add Workshop`, not `git add -A`.
