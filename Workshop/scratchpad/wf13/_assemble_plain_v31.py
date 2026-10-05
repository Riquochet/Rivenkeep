#!/usr/bin/env python3
"""Assemble plain_v31_draft.md from the wf13 Plain group files, in book_v3.md's order.

Same method as wf11/_assemble_plain_v3.py:
  * the one-line '<!-- PLAIN WORDS ... -->' header of each group file is dropped;
  * everything from a group's '## WRITER'S NOTES' heading to its end is cut out and collected in plain_notes.md;
  * the rest is cut into sections at its structural lines (a '#'/'##'/'###' heading or a top-level '---' rule);
  * the Book's skeleton (its sequence of headings and rules) is walked, and for each heading the Plain section with
    the identical heading line is emitted; each rule is emitted as a rule;
  * each Contents Argument is set word for word to the Argument under that Book's own Plain heading (g01's notes
    expect this: only Book One's Contents Argument is g01's own);
  * every '###' tale of the Book must have its line in the Contents, in the Book's order.
"""
import os, re, sys

WF13 = os.path.dirname(os.path.abspath(__file__))
WF11 = os.path.join(os.path.dirname(WF13), 'wf11')
BOOK = os.path.join(WF11, 'book_v3.md')
OUT = os.path.join(WF13, 'plain_v31_draft.md')
NOTES = os.path.join(WF13, 'plain_notes.md')
GROUPS = ['g01', 'g02', 'g03', 'g04', 'g05', 'g06', 'g07', 'g08', 'g09', 'g10', 'g11', 'w01', 'w02']

STRUCT = re.compile(r'^(#{1,3} .*|---)\s*$')
NOTES_HEAD = re.compile(r"^## WRITER'S NOTES\s*$")


def split_group(text):
    """Return (header comment or None, body text, notes lines)."""
    lines = text.split('\n')
    header = None
    if lines and lines[0].startswith('<!-- PLAIN WORDS'):
        assert lines[0].rstrip().endswith('-->'), 'multi-line PLAIN WORDS header'
        header, lines = lines[0].rstrip(), lines[1:]
    idx = [i for i, ln in enumerate(lines) if NOTES_HEAD.match(ln)]
    assert len(idx) <= 1, 'more than one WRITER\'S NOTES heading'
    if idx:
        body, notes = lines[:idx[0]], lines[idx[0] + 1:]
    else:
        body, notes = lines, []
    return header, '\n'.join(body), notes


def cut(text):
    """Return a list of (key, body_lines). key is the heading line, or '---' for a rule, or None for preamble."""
    out, key, body = [], None, []
    for ln in text.split('\n'):
        if STRUCT.match(ln):
            if key is not None or any(x.strip() for x in body):
                out.append((key, body))
            key, body = ln.rstrip(), []
        else:
            body.append(ln)
    if key is not None or any(x.strip() for x in body):
        out.append((key, body))
    return out


def trim(lines):
    while lines and not lines[0].strip():
        lines = lines[1:]
    while lines and not lines[-1].strip():
        lines = lines[:-1]
    return lines


def main():
    book = open(BOOK, encoding='utf-8').read()
    skeleton = [k for k, _ in cut(book)]
    assert skeleton[0] is not None

    sections, where, notes_out, problems = {}, {}, [], []
    for g in GROUPS:
        raw = open(os.path.join(WF13, 'plain', g + '.md'), encoding='utf-8').read()
        header, body, notes = split_group(raw)
        heads = []
        for key, sbody in cut(body):
            if key is None:
                if any(x.strip() for x in sbody):
                    sys.exit(f'{g}: text before the first heading')
                continue
            if key == '---':
                if any(x.strip() for x in sbody):
                    sys.exit(f'{g}: text under a rule with no heading')
                continue
            if key in sections:
                sys.exit(f'duplicate Plain section {key!r} in {g} and {where[key]}')
            sections[key], where[key] = trim(sbody), g
            heads.append(key.lstrip('# ').strip())
        notes_out.append((g, header, heads, trim(notes)))

    # Contents: each Book's Argument copied from the Plain's own Book heading.
    synced = []
    contents = sections.get('## CONTENTS')
    assert contents, 'no Contents'
    for i, ln in enumerate(contents):
        m = re.match(r'^\*\*((?:BOOK|EPILOGUE|APPENDIX)[^*]*)\*\*$', ln)
        if not m:
            continue
        head = '## ' + m.group(1)
        arg = next((x for x in sections.get(head, []) if x.strip()), None)
        j = next(j for j in range(i + 1, len(contents)) if contents[j].strip())
        if arg and arg.startswith('*') and contents[j] != arg:
            synced.append((m.group(1), contents[j], arg))
            contents[j] = arg

    # Contents must list every tale, in the Book's order, and nothing else.
    tales = [k[4:] for k in skeleton if k and k.startswith('### ')]
    listed = []
    for ln in contents:
        if ln.startswith('- '):
            parts = ln[2:].split(' · ')
            title = ' · '.join(parts[:2]) if re.match(r'^[IVX]+\.\d+$', parts[0]) else parts[0]
            listed.append(title)
    contents_missing = [t for t in tales if t not in listed]
    contents_extra = [t for t in listed if t not in tales]
    contents_order_ok = [t for t in listed if t in tales] == tales

    parts, used, missing = [], set(), []
    for key in skeleton:
        if key == '---':
            parts.append('---')
            continue
        if key not in sections:
            missing.append(key)
            parts.append(key)
            continue
        used.add(key)
        body = sections[key]
        parts.append(key + ('\n\n' + '\n'.join(body) if body else ''))
    extra = [k for k in sections if k not in used]

    open(OUT, 'w', encoding='utf-8').write('\n\n'.join(parts) + '\n')

    # Notes file: every group's WRITER'S NOTES, as written, in the Book's order of groups.
    order = {k: i for i, k in enumerate(skeleton)}
    first = {g: min((order.get(k, 10**6) for k, w in where.items() if w == g), default=10**6) for g in GROUPS}
    nl = ['# The Plain, v3.1: writer\'s notes', '',
          '*The \'## WRITER\'S NOTES\' sections of the wf13 Plain group files (plain/g01.md to g11.md, w01.md, w02.md), '
          'cut from `plain_v31_draft.md` when it was assembled and kept here whole, group by group in the Book\'s order. '
          'Each group\'s one-line PLAIN WORDS header is quoted above its notes.*', '']
    for g, header, heads, notes in sorted(notes_out, key=lambda x: first[x[0]]):
        nl += ['---', '', f'## {g} · ' + ' · '.join(h for h in heads), '']
        if header:
            nl += ['> ' + re.sub(r'^<!--\s*|\s*-->$', '', header), '']
        nl += (notes if notes else ['*(no writer\'s notes in this group)*']) + ['']
    open(NOTES, 'w', encoding='utf-8').write('\n'.join(nl).rstrip('\n') + '\n')

    print('wrote', OUT)
    print('wrote', NOTES)
    print('book sections:', sum(1 for k in skeleton if k != '---'), ' rules:', skeleton.count('---'))
    print('missing in Plain:', missing)
    print('Plain sections not in Book:', extra)
    print('groups without notes:', [g for g, _, _, n in notes_out if not n])
    print('tales in Book:', len(tales), ' tale lines in Contents:', len(listed),
          ' missing:', contents_missing, ' extra:', contents_extra, ' order ok:', contents_order_ok)
    for name, old, new in synced:
        print(f'Contents Argument synced to the heading: {name}\n    was: {old}\n    now: {new}')
    for k in skeleton:
        if k and k != '---':
            print(f'  {where.get(k, "--"):4} {k}')
    if missing or extra or contents_missing or contents_extra or not contents_order_ok:
        sys.exit(1)


if __name__ == '__main__':
    main()
