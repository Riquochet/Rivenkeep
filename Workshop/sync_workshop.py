#!/usr/bin/env python3
"""sync_workshop.py -- sort Claude's working folder into WORK PRODUCT (kept in this repo) and WORKING DEBRIS (kept
outside it, on this Mac only).

    python3 sync_workshop.py --src SCRATCHPAD --mode copy            # refresh both sides from a live scratchpad
    python3 sync_workshop.py --src Workshop/scratchpad --mode move   # partition a mirror in place
    python3 sync_workshop.py --src ... --dry [--manifest DIR]        # print the sizes (and write keep.txt / leave.txt)

KEEP  = the Book, Plain Words and Notes sources; the specs, lexicons and grain data; the translation units, glosses and
        their reports; the research notes and guides; the current page builders and the language tools; the leaf-hand
        font and the drawings the builders use.
LEAVE = browser profiles, screenshots, temporary copies, built pages (the finished ones live in ../Docs), backups,
        superseded drafts and builders, downloaded books and articles, caches, symlinks.

The keep side goes to Workshop/scratchpad (this folder). The leave side goes to ~/code/Rivenkeep_Workshop/scratchpad.
Rules are checked in this order: KEEP_PATHS / KEEP_MOVES / KEEP_LINKS, then every LEAVE rule, then the KEEP list.
To keep a new kind of file, add a rule. Leaving a file is always recoverable; publishing one is not.
"""
import argparse
import fnmatch
import os
import re
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
KEEP_ROOT = os.path.join(HERE, 'scratchpad')
LEAVE_ROOT = os.path.expanduser('~/code/Rivenkeep_Workshop/scratchpad')

# --------------------------------------------------------------------------- what is never kept
LEAVE_DIRS = ['tmp', 'tmp*', 'shots', 'shots*', 'out', 'audio', '__pycache__', 'node_modules', '_src', 'src', 'xcheck*', 'xchk',
              'chk*', '*chk', 'cdp-*', 'chrome-prof*', 'prof*', '*backup*', 'groot', 'before', 'after', 'gn_wf8',
              'decode', 'sheet', 'v2out', '_final', '_edit', '_s[0-9]*', '_g[0-9]*', '_plain*', '_notes_v3', 'venv', 'npm-cache',
              'ed2', 'edit', 'plain_parts', 'tools_old', 'w01chk', 'gi_test']
LEAVE_FILES = ['.DS_Store', '*.pyc', '*_before_verify.json', '*_view.txt', '_wf12_manifest_*', '*_draft.md', 'panes_v300.json',
               'Singleton*', 'old_p*.html', 'published_*.html']
# downloaded books and articles (other people's text)
LEAVE_FILES += ['chekhov_letters.txt', 'hod.txt', 'iliad_butler.txt', 'odyssey_butler.txt', 'njal.txt']
LEAVE_FILES += ['*_prev.md',          # previous drafts that sit beside the current ones
                'test_p5.svg',        # a test render that nothing references
                'S10_VI-1_2.*']       # an exact copy of S10_VI-1 (.gn2, .svg)
# exact paths (relative to the scratchpad) that a KEEP rule below would take but that are not work product
LEAVE_PATHS = [
    # v1.3-era page builders and checkers (replaced by build_story_html.py / check_story.py and build_panes.py)
    'wf13/book/build_legends_html.py', 'wf13/book/check_legends_html.py', 'wf13/book/native_html.py', 'wf13/book/check_tabs3.py',
    'wf13/orig/build_original.py', 'wf13/orig/check_original.py', 'wf13/orig/bookparse.py', 'wf13/orig/units.py', 'wf13/orig/cmp_tok.py',
    # screenshot, preview, measuring and test-drive scripts (cdp.mjs stays: the kept reader checks run through it)
    'wf13/book/shot.py', 'wf13/book/shot_tabs.py', 'wf13/book/t_ax.mjs', 'wf13/book/t_dbg.mjs', 'wf13/book/t_il.mjs',
    'wf13/book/t_note.mjs', 'wf13/book/t_place.mjs', 'wf13/notes_build/shot.py',
    'wf13/orig/measure_iframe.py', 'wf13/orig/preview_panes.py', 'wf13/orig/shoot.sh', 'wf13/orig/shoot_page.py',
    'wf13/orig/shoot_phone.py', 'wf13/orig/units_probe.py',
    'wf8/tongues_build/shoot.py', 'wf8/tongues_build/shoot_part.py', 'wf8/tongues_build/shoot_part_old.py',
    'wf8/tongues_build/shoot_v030.py', 'wf8/tongues_build/perf.py',
    # one-off patch scripts whose input (old_p2.html, old_p3.html) is on the leave side
    'wf8/tongues_build/edit_p2.py', 'wf8/tongues_build/edit_p3.py',
    # dumps of single runs that nothing reads
    'wf13/orig/build_report.txt', 'wf13/orig/check_out.txt', 'wf13/orig/jobs.txt', 'wf13/orig/jobs3.txt',
    # drafts of the Plain Words v1.1.0 (A and B), superseded
    'wf7/book/modern_a_v110.md', 'wf7/book/modern_b_v110.md',
]
# regexes on the relative path: svg3 drawings that no page sets (the 'not set' list of panes_check.json)
LEAVE_RE = [
    r'wf13/orig/svg3/VI-2-(vaelress|senneir|naelthar|leavaren|esthaer|rhenvael|ralensaen)(_r(0[1-9]|1[01]|13|14))?\.svg$',
    r'wf13/orig/svg3/VI-2-(eirlenth|neivaere)(_r(0[1-9]|1[01]|15|16))?\.svg$',
]

# --------------------------------------------------------------------------- what is kept: (directory, extensions or None = any, depth, names or None)
KEEP = [
    # the course-hand drawings the page builders inline, and the first specs
    ('wf6', None, 0, ['mystaeri_spec.md']),
    ('wf6/grain', {'.json'}, 0, None),
    ('wf6/svg', {'.svg', '.md'}, 0, None),
    # the language foundation
    ('wf7', {'.md', '.py', '.tsv'}, 0, None),
    ('wf7/ancestor', {'.md', '.py'}, 0, None),
    ('wf7/orrowen', {'.py', '.json', '.md'}, 0, None),
    ('wf7/fonts', {'.woff2', '.fea', '.py'}, 0, None),
    ('wf7/coverage', {'.json', '.py'}, 0, None),
    ('wf7/grain2', {'.json', '.txt', '.md'}, 0, None),
    ('wf7/lex', {'.py', '.md', '.tsv'}, 0, None),
    ('wf7/book', {'.md'}, 0, None),
    ('wf7/pilot_IV4', {'.gn2', '.txt', '.md', '.tokens'}, 0, None),
    # the Tier 3 translation (the v1.3 telling), its Tongues-page builder, and the grain drawings it used
    ('wf8', {'.md', '.tsv', '.py'}, 0, None),
    ('wf8/units', {'.md'}, 0, None),
    ('wf8/additions', {'.tsv', '.md'}, 0, None),
    ('wf8/backtrans', {'.md'}, 0, None),
    ('wf8/blind', {'.txt', '.gn2', '.md'}, 0, None),
    ('wf8/grain3/data', {'.json'}, 0, None),
    ('wf8/grain3/texts', {'.gn2'}, 0, None),
    ('wf8/grain3/svg', {'.svg'}, 0, None),
    ('wf8/grain3/work', {'.py'}, 0, None),
    ('wf8/tongues_build', {'.py', '.css'}, 0, None),
    ('wf8/tongues_build', {'.html'}, 0, ['p0.html', 'p[1-4].html', 'p_*.html']),
    # the design of the epic: the outline, the timeline, the cast, the puzzle
    ('wf9', {'.md'}, 0, None),
    # the v3 Book, Plain Words and Notes sources, the voice and craft guides, the research, the register test
    ('wf11', {'.md', '.py'}, 0, None),
    ('wf11/_tools_v3', {'.py'}, 0, None),
    ('wf11/research', {'.md', '.py', '.json', '.txt'}, 0, None),
    ('wf11/samples', {'.md'}, 0, None),
    ('wf11/calib/A', {'.md'}, 0, None), ('wf11/calib/B', {'.md'}, 0, None), ('wf11/calib/C', {'.md'}, 0, None),
    ('wf11/drafts', {'.md'}, 0, None),
    ('wf11/plain', {'.md'}, 0, None),
    ('wf11/critique', {'.md'}, 0, ['book_*.md', 'plain_whole*.md', 'g[0-9][0-9]_*.md', 'w0[0-9]_*.md']),
    # the v3 translation into Orrowen and the grain, and its reports
    ('wf12', {'.md', '.tsv'}, 0, None),
    ('wf12/units', {'.md'}, 0, None),
    ('wf12/additions', {'.tsv', '.md'}, 0, None),
    ('wf12/backtrans', {'.md'}, 0, None),
    ('wf12/blind', {'.txt', '.gn2', '.md'}, 0, None),
    ('wf12/merge', {'.py', '.md'}, 0, None),
    ('wf12/base', {'.tsv', '.md', '.py'}, 0, None),
    # v3.1: Plain Words for newcomers, the glosses, and the current page builders (page, panes, Notes)
    ('wf13', {'.md', '.py', '.sh'}, 0, None),
    ('wf13', {'.json'}, 0, ['common_words.json']),
    ('wf13', {'.txt'}, 0, ['_s03_glosses.txt']),
    ('wf13/gloss', {'.json'}, 0, None),
    ('wf13/gloss_in', {'.json'}, 0, None),
    ('wf13/plain', {'.md'}, 0, None),
    ('wf13/critique', {'.md'}, 0, None),
    ('wf13/book', {'.py', '.css', '.mjs'}, 0, None),
    ('wf13/orig', {'.py', '.css', '.json', '.md', '.txt', '.sh'}, 0, None),
    ('wf13/orig', {'.log'}, 0, ['make_grain3.log']),
    ('wf13/orig/gn', {'.gn2'}, 0, None),
    ('wf13/orig/svg', {'.svg'}, 0, None),
    ('wf13/orig/svg3', {'.svg'}, 0, None),
    ('wf13/notes_build', {'.py', '.md'}, 0, None),
    ('wf13/fid', {'.py', '.md'}, 0, None),
    ('wf13/fid', {'.txt'}, 0, ['*_out.txt']),
]
# single files kept although they sit in a folder or under a name the rules above leave (checked BEFORE every leave rule)
KEEP_PATHS = [
    # the frozen blind readings (the '*_draft.md' glob is aimed at wf11/wf13 drafts)
    'wf8/blind/S01_draft.md', 'wf8/blind/S03_draft.md', 'wf8/blind/S04_draft.md', 'wf8/blind/W06_draft.md', 'wf8/blind/W07_draft.md',
    # the checkers the kept reports name (wf12/fidelity_report.md, wf13/check_report.md)
    'wf12/tmp/FID/fid_text.py', 'wf12/tmp/FID/fid_frame.py', 'wf12/tmp/FID/fid_orig.py', 'wf12/tmp/FID/spot.py',
    'wf13/tmp/chk/web_contract.py', 'wf13/tmp/chk/gloss_static.py',
    'wf13/tmp/reader/il.mjs', 'wf13/tmp/reader/plain.mjs', 'wf13/tmp/reader/gaps.mjs', 'wf13/tmp/reader/blot.mjs',
    'wf13/tmp/reader/fw_place.mjs', 'wf13/tmp/reader/place.mjs', 'wf13/tmp/reader/t_place2.mjs',
    # the 45 first marks, which the First Tongue page lists among the engine's files
    'wf7/ancestor/first_marks.svg',
]
# files kept under another name: (folder now, working folder they belong in, names). The tools find their siblings through HERE.
KEEP_MOVES = [
    ('wf7/bt_IV4/lexdry/ancestor', 'wf7/ancestor',
     ['laws.py', 'formations.py', 'first_marks.py', 'first_marks.json', 'predict.py', 'check.py', 'extract.py', 'descent.py',
      'descent.html', 'gen_reserve.py', 'gen_reserve2.py', 'reserve.json', 'o_lex_raw.json', 's_lex_raw.json', 'common_english.txt']),
    ('wf7/bt_IV4/lexdry/orrowen', 'wf7/orrowen', ['wordstones.json']),
    ('wf7/bt_IV4/lexdry/lex', 'wf7/lex',
     ['base.py', 'sys_curated.py', 'extract_lemmas.py', 'lemmas.tsv', 'names.tsv', 'compounds.tsv', 'lemma_overrides.tsv']),
    ('wf7/bt_IV4/lexdry/lex/en_map', 'wf7/lex/en_map', ['*.txt']),
]
# the two symlinks the page builders open: kept, and written RELATIVE to their target (which is itself kept)
KEEP_LINKS = {
    'wf13/orig/lexicon_orrowen.tsv': 'wf12/lexicon_orrowen_full.tsv',
    'wf13/orig/orrowen_v2.md': 'wf7/orrowen_v2.md',
}


def rel_parts(rel):
    return rel.split('/')


def keep_rule(rel):
    parts = rel_parts(rel)
    d = '/'.join(parts[:-1])
    name = parts[-1]
    ext = os.path.splitext(name)[1].lower()
    for prefix, exts, depth, names in KEEP:
        if d != prefix:
            continue
        if names is not None and not any(fnmatch.fnmatch(name, g) for g in names):
            continue
        if exts is not None and ext not in exts:
            continue
        return True
    return False


def dest_of(rel):
    """where a kept file lives on the keep side: itself, or the working folder KEEP_MOVES names for it"""
    d, name = os.path.split(rel)
    for src, dst, names in KEEP_MOVES:
        if d == src and any(fnmatch.fnmatch(name, g) for g in names):
            return dst + '/' + name
    return rel


def is_leave(rel, islink):
    if islink:
        return True
    if rel in LEAVE_PATHS or any(re.match(p, rel) for p in LEAVE_RE):
        return True
    parts = rel_parts(rel)
    name = parts[-1]
    for d in parts[:-1]:
        if any(fnmatch.fnmatch(d, g) for g in LEAVE_DIRS):
            return True
    if any(fnmatch.fnmatch(name, g) for g in LEAVE_FILES):
        return True
    return False


def classify(rel, islink=False):
    """-> 'keep' | 'leave'"""
    if islink:
        return 'keep' if rel in KEEP_LINKS else 'leave'
    if rel in KEEP_PATHS or dest_of(rel) != rel:
        return 'keep'
    if is_leave(rel, islink):
        return 'leave'
    if keep_rule(rel):
        return 'keep'
    return 'leave'


def walk(src):
    for root, dirs, files in os.walk(src, followlinks=False):
        for f in files:
            p = os.path.join(root, f)
            yield os.path.relpath(p, src).replace(os.sep, '/'), p, os.path.islink(p)
        for d in dirs:
            p = os.path.join(root, d)
            if os.path.islink(p):
                yield os.path.relpath(p, src).replace(os.sep, '/'), p, True


def put(p, dest, mode):
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    if os.path.lexists(dest):
        if os.path.islink(dest) or os.path.isfile(dest):
            os.remove(dest)
    if os.path.islink(p):
        os.symlink(os.readlink(p), dest)
        if mode == 'move':
            os.remove(p)
        return
    if mode == 'move':
        shutil.move(p, dest)
    else:
        shutil.copy2(p, dest)


def put_link(rel, p, keep_root, mode):
    """KEEP_LINKS: write the link on the keep side as a RELATIVE link to its (kept) target"""
    dest = os.path.join(keep_root, rel)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    if os.path.lexists(dest):
        os.remove(dest)
    os.symlink(os.path.relpath(os.path.join(keep_root, KEEP_LINKS[rel]), os.path.dirname(dest)), dest)
    if mode == 'move' and os.path.lexists(p) and os.path.abspath(p) != os.path.abspath(dest):
        os.remove(p)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--src', required=True)
    ap.add_argument('--mode', choices=['copy', 'move'], default='copy')
    ap.add_argument('--keep-root', default=KEEP_ROOT)
    ap.add_argument('--leave-root', default=LEAVE_ROOT)
    ap.add_argument('--dry', action='store_true')
    ap.add_argument('--manifest', help='write keep.txt and leave.txt manifests into this directory')
    a = ap.parse_args()
    src = os.path.abspath(a.src)
    skip_top = {'venv', 'npm-cache'}
    keep, leave = [], []
    for rel, p, islink in walk(src):
        if rel.split('/')[0] in skip_top:
            continue
        (keep if classify(rel, islink) == 'keep' else leave).append((rel, p, islink))
    ks = sum(os.path.getsize(p) for _, p, l in keep if not l)
    ls = sum(os.path.getsize(p) for _, p, l in leave if not l and os.path.exists(p))
    print('KEEP  %6d files %8.1f MB' % (len(keep), ks / 1048576))
    print('LEAVE %6d files %8.1f MB' % (len(leave), ls / 1048576))
    if a.manifest:
        os.makedirs(a.manifest, exist_ok=True)
        for nm, L in (('keep', keep), ('leave', leave)):
            with open(os.path.join(a.manifest, nm + '.txt'), 'w') as f:
                for rel, p, l in sorted(L):
                    sz = 0 if l or not os.path.exists(p) else os.path.getsize(p)
                    shown = dest_of(rel) if nm == 'keep' else rel
                    f.write('%10d  %s%s\n' % (sz, shown, '  -> symlink' if l else ''))
    if a.dry:
        return
    same_tree = os.path.samefile(src, a.keep_root) if os.path.exists(a.keep_root) else False
    for rel, p, l in keep:
        if l:
            put_link(rel, p, a.keep_root, a.mode)
        elif not (same_tree and a.mode == 'move' and dest_of(rel) == rel):
            put(p, os.path.join(a.keep_root, dest_of(rel)), a.mode)
    for rel, p, l in leave:
        put(p, os.path.join(a.leave_root, rel), a.mode)
    if a.mode == 'move':           # prune what the move emptied
        for root, dirs, files in os.walk(src, topdown=False):
            if root != src and not os.listdir(root):
                os.rmdir(root)


if __name__ == '__main__':
    main()
