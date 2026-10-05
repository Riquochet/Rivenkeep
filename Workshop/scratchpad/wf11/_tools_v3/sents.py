import sys, re
sys.path.insert(0, '_tools_v3')
from count_v3 import proper_parts, sentences, words
raw = open(sys.argv[1]).read()
part = sys.argv[2]
book, plain = raw.split('<!-- PLAIN WORDS', 1) if '<!-- PLAIN WORDS' in raw else (raw, None)
if part == 'plain':
    plain = plain.split('-->', 1)[1]
    h, p = proper_parts(plain, False)
else:
    h, p = proper_parts(book, True)
for s in sentences(p):
    n = len(words(s))
    flag = '  <10' if n < 10 else ('  >30' if n > 30 else '')
    print(f"{n:3d}{flag} | {s[:110]}")
