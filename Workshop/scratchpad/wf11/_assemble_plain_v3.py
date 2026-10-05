#!/usr/bin/env python3
"""Assemble plain_v3.md from the Plain group files, in book_v3.md's order.

Each file is cut into sections at its structural lines (a '#'/'##'/'###' heading or a top-level '---' rule).
The Book's skeleton (its sequence of headings and rules) is then walked, and for each heading the Plain
section with the identical heading line is emitted; each rule is emitted as a rule.
"""
import os, re, sys

WF = os.path.dirname(os.path.abspath(__file__))
BOOK = os.path.join(WF, 'book_v3.md')
OUT = os.path.join(WF, 'plain_v3.md')
GROUPS = ['g01', 'g02', 'g03', 'g04', 'g05', 'g06', 'g07', 'g08', 'g09', 'g10', 'g11', 'w01', 'w02']

STRUCT = re.compile(r'^(#{1,3} .*|---)\s*$')


def strip_header(text):
    lines = text.split('\n')
    if lines and lines[0].startswith('<!-- PLAIN WORDS'):
        assert lines[0].rstrip().endswith('-->'), 'multi-line PLAIN WORDS header'
        lines = lines[1:]
    return '\n'.join(lines)


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

    sections, where = {}, {}
    for g in GROUPS:
        raw = strip_header(open(os.path.join(WF, 'plain', g + '.md'), encoding='utf-8').read())
        for key, body in cut(raw):
            if key is None:
                if any(x.strip() for x in body):
                    sys.exit(f'{g}: text before the first heading')
                continue
            if key == '---':
                if any(x.strip() for x in body):
                    sys.exit(f'{g}: text under a rule with no heading')
                continue
            if key in sections:
                sys.exit(f'duplicate Plain section {key!r} in {g} and {where[key]}')
            sections[key], where[key] = trim(body), g

    # The Contents repeats each Book's Argument word for word, as in book_v3.md and plain_v2.md.
    # Take each Argument from the Plain's own Book heading, so the two never drift.
    synced = []
    contents = sections.get('## CONTENTS')
    if contents:
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
        # every tale line in the Contents names a '###' heading of the Book
        for ln in contents:
            if ln.startswith('- '):
                title = ' · '.join(ln[2:].split(' · ')[:2])
                if '### ' + title not in skeleton and '### ' + ln[2:].split(' · ')[0] not in skeleton:
                    print('Contents line names no tale heading:', ln)

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
    print('wrote', OUT)
    print('book sections:', sum(1 for k in skeleton if k != '---'), ' rules:', skeleton.count('---'))
    print('missing in Plain:', missing)
    print('Plain sections not in Book:', extra)
    for name, old, new in synced:
        print(f'Contents Argument synced to the heading: {name}\n    was: {old}\n    now: {new}')
    for k in skeleton:
        if k and k != '---':
            print(f'  {where.get(k, "--"):4} {k}')


if __name__ == '__main__':
    main()
