#!/usr/bin/env python3
"""Counts for the v3 calibration samples (Book leaf + Plain Words twin in one file).

Tale proper = everything after the headnote, through the hearth's answer
(or 'And no one answered.'), songs included; ::: native blocks and HTML comments excluded.
Also: annal (IV.3), reading (wood leaf), -eth/-est forms, contractions, Plain/Book 4-gram overlap,
and a rough Flesch-Kincaid grade."""
import re, sys, statistics

W = r"[A-Za-z0-9’'\-]+"

def norm(t):
    t = re.sub(r'\{\{([^}]+)\}\}', r'\1', t)
    return t.replace('▒▒▒▒', 'Warden')

def words(t):
    return re.findall(W, norm(t))

def strip_native(txt):
    out, skip = [], False
    for ln in txt.split('\n'):
        s = ln.lstrip('> ').strip()
        if s.startswith(':::'):
            skip = not skip
            continue
        if not skip:
            out.append(ln)
    return '\n'.join(out)

def proper_parts(section, has_dateline=True):
    txt = re.sub(r'<!--.*?-->', '', section, flags=re.S)
    txt = strip_native(txt)
    paras = [p.strip() for p in txt.split('\n\n') if p.strip() and p.strip() != '---']
    hi = 2 if has_dateline else 1
    head = paras[hi]
    body = paras[hi + 1:]
    end = None
    for i, p in enumerate(body):
        if 'said: We remember.' in p or 'And no one answered.' in p:
            end = i
    proper = body[:end + 1] if end is not None else body
    return head, proper

def sentences(paras):
    prose = [p for p in paras if not p.startswith('>')]
    s_txt = re.sub(r'\*', '', ' '.join(prose))
    sents = [s for s in re.split(r'(?<=[.!?…])["”]?\s+', s_txt) if words(s)]
    return sents

def syllables(w):
    w = w.lower().strip("'’")
    if len(w) <= 3:
        return 1
    w = re.sub(r'(?:[^laeiouy]es|ed|[^laeiouy]e)$', '', w)
    w = re.sub(r'^y', '', w)
    return max(1, len(re.findall(r'[aeiouy]{1,2}', w)))

def fk(sents):
    ws = [w for s in sents for w in words(s)]
    syl = sum(syllables(w) for w in ws)
    return 0.39 * len(ws) / len(sents) + 11.8 * syl / len(ws) - 15.59

def grams(paras, n=4):
    ws = [w.lower().replace('’', "'") for p in paras for w in words(p)]
    return [tuple(ws[i:i + n]) for i in range(len(ws) - n + 1)]

def report(name, head, proper, label):
    pw = sum(len(words(p)) for p in proper)
    sents = sentences(proper)
    lens = [len(words(s)) for s in sents]
    third = len(lens) // 3 or 1
    th = [statistics.mean(lens[:third]), statistics.mean(lens[third:2 * third]), statistics.mean(lens[2 * third:])]
    body = ' '.join(proper)
    contr = len(re.findall(r"\b(?:\w+n['’]t|\w+['’](?:ll|re|ve|d|m)|(?:it|that|he|she|there|what|who|here|let|where)['’]s)\b", body, flags=re.I))
    ands = len(re.findall(r'\band\b', body, flags=re.I))
    eth = re.findall(r"\b(?:\w+eth|hath|doth|saith)\b", body)
    est = re.findall(r"\b\w+(?:est|edst)\b", body)
    print(f"{name} [{label}]: headnote {len(words(head))} | tale proper {pw} | sentences {len(lens)} "
          f"mean {statistics.mean(lens):.1f} median {statistics.median(lens)} | <10w {100*sum(l<10 for l in lens)/len(lens):.0f}% "
          f">30w {sum(l>30 for l in lens)} max {max(lens)} | thirds {th[0]:.1f}/{th[1]:.1f}/{th[2]:.1f} | "
          f"';'/sent {body.count(';')/len(lens):.2f} 'and'/sent {ands/len(lens):.2f} | "
          f"contractions {contr} ({1000*contr/pw:.1f}/1k) | FK {fk(sents):.1f}")
    if label == 'Book':
        print(f"    -eth forms {len(eth)}: {', '.join(eth)}")
        print(f"    -est forms: {', '.join(est) or 'none'}")
    return pw

def main():
  for path in sys.argv[1:]:
      raw = open(path, encoding='utf-8').read()
      if '<!-- PLAIN WORDS' in raw:
          book_raw, plain_raw = raw.split('<!-- PLAIN WORDS', 1)
          plain_raw = plain_raw.split('-->', 1)[1]
      else:
          book_raw, plain_raw = raw, None
      name = path.split('/')[-1]
      bh, bp = proper_parts(book_raw, True)
      report(name, bh, bp, 'Book')
      # annal and reading
      if 'So far the words of Brenn.' in book_raw:
          a = book_raw.index('So far the words of Brenn.')
          b = book_raw.index('There I stopped tonight')
          print(f"    annal (record): {len(words(book_raw[a:b]))} words")
      if '<!-- READING -->' in book_raw:
          a = book_raw.index('<!-- READING -->') + len('<!-- READING -->')
          b = book_raw.index('This is held in the grain.')
          print(f"    reading: {len(words(book_raw[a:b]))} words")
      if plain_raw:
          ph, pp = proper_parts(plain_raw, False)
          report(name, ph, pp, 'Plain')
          bg = set(grams(bp)); pg = grams(pp)
          shared = sum(1 for g in pg if g in bg)
          print(f"    Plain 4-word runs found verbatim in the Book: {100*shared/len(pg):.1f}% (target <= 20%)")
          FIXED = ('*—', '*Stop the felling', '*Stop cutting', '*Unknown intruder', '"Stop', '**IN MEMORY', '>', 'This is held in the grain.',
                   '*And no one answered', "That's all he came to say", 'That is all he came to say', '*And the hearth said', '*And everyone at the hearth said', 'This I lay', 'This we lay', 'I have laid', 'We have laid')
          free = lambda ps: [p for p in ps if not p.startswith(FIXED)]
          bpf, ppf = free(bp), free(pp)
          bg2 = set(grams(bpf)); pg2 = grams(ppf)
          sh2 = sum(1 for g in pg2 if g in bg2)
          for lab, ps in (('Book', bpf), ('Plain', ppf)):
              ss = sentences(ps); ls = [len(words(x)) for x in ss]
              print(f"    {lab} prose only (no fixed matter, no reading): sentences {len(ls)} mean {statistics.mean(ls):.1f} "
                    f"<10w {100*sum(l<10 for l in ls)/len(ls):.0f}% >30w {sum(l>30 for l in ls)}")
          print(f"    overlap, prose only: {100*sh2/len(pg2):.1f}%")


if __name__ == '__main__':
    main()
