#!/usr/bin/env python3
"""Rebuild the index of a manual as links to its sections.

Usage: build_index.py MANUAL.md TERMS.txt

TERMS.txt: one entry per line, "Display ; search 1 ; search 2 ...". Without search terms the
display text (without backticks) is searched. "Display => see Other" makes a cross reference.
Lines starting with # are comments.

Search rules: a search term that starts with "|" or is written in capitals (CAT, BDOS, CP/M ...)
matches case-sensitively and exactly; other terms match case-insensitively as whole words - in
the German manual with up to 3 more letters (inflections), in the English one with "s"/"es".

For each entry the script lists up to MAX_LINKS sections, the ones with the highest score
(hits in the section text, plus HEAD_BONUS when the heading contains the term), in document
order. The title block, the index (INDEX_HEADINGS) and the table of contents are not searched.
The part from the first letter group under the index heading to the next "---" line is
replaced; the note paragraph under the heading is kept. Run it again after every change of the
manual.
"""
import re, sys, unicodedata

MAX_LINKS = 4
HEAD_BONUS = 10
INDEX_HEADINGS = ('Stichwortverzeichnis', 'Index')
TOC_HEADINGS = ('Inhaltsverzeichnis', 'Contents')

def slug(h):
    h = h.strip().lower()
    h = re.sub(r'[^\w\- ]', '', h)
    return h.replace(' ', '-')

def sections(text):
    """[(level, heading, anchor, body)] for all headings outside code blocks."""
    out, inblock, cur, seen = [], False, None, {}
    for line in text.split('\n'):
        if line.startswith('```'):
            inblock = not inblock
        m = None if inblock else re.match(r'^(#{1,6}) (.+)$', line)
        if m:
            s = slug(m[2]); n = seen.get(s, 0); seen[s] = n + 1
            cur = [len(m[1]), m[2], s if n == 0 else f'{s}-{n}', []]
            out.append(cur)
        elif cur:
            cur[3].append(line)
    return [(l, h, a, '\n'.join(b)) for l, h, a, b in out]

SUFFIX = r'\w{0,3}'      # German: inflections; set to (?:s|es)? for English in main()

def pattern(term):
    t = term.replace('`', '').strip()
    exact = t.startswith('|') or not re.search(r'[a-zäöüß]', t)
    esc = re.escape(t)
    if exact:
        return re.compile(r'(?<![\w|])' + esc + r'(?![\w]|\.\w|,\d)')
    return re.compile(r'(?<!\w)' + esc + SUFFIX + r'(?!\w)', re.I)

def sort_key(display):
    t = display.replace('`', '').lstrip('|').strip('"')
    t = unicodedata.normalize('NFKD', t)
    return ''.join(c for c in t if not unicodedata.combining(c)).lower()

def main(manual, terms_file):
    global SUFFIX
    text = open(manual, encoding='utf-8').read()
    if '\n## Index\n' in text:
        SUFFIX = r'(?:s|es)?'
    secs = sections(text)
    # skip the TOC, the index and the index's letter groups
    usable, skip_level = [], None
    for lvl, h, a, body in secs:
        if lvl == 1:                       # the title block
            continue
        if skip_level is not None and lvl > skip_level:
            continue
        skip_level = None
        if h.strip() in INDEX_HEADINGS + TOC_HEADINGS:
            skip_level = lvl
            continue
        usable.append((lvl, h, a, body))
    entries = []
    for line in open(terms_file, encoding='utf-8'):
        line = line.rstrip('\n')
        if not line.strip() or line.startswith('#'):
            continue
        if '=>' in line:
            d, ref = (x.strip() for x in line.split('=>', 1))
            entries.append((d, ref)); continue
        parts = [p.strip() for p in line.split(';') if p.strip()]
        display, searches = parts[0], parts[1:] or [parts[0]]
        pats = [pattern(s) for s in searches]
        scored = []
        for i, (lvl, h, a, body) in enumerate(usable):
            in_head = any(p.search(h.replace('`', '')) for p in pats)
            hits = sum(len(p.findall(body)) for p in pats)
            if in_head or hits:
                scored.append((-(hits + (HEAD_BONUS if in_head else 0)), i, i, h, a))
        scored.sort()
        best = sorted(scored[:MAX_LINKS], key=lambda x: x[2])   # in document order
        if not best:
            print('no hit:', display, file=sys.stderr); continue
        links = ', '.join(f'[{h}](#{a})' for _, _, _, h, a in best)
        entries.append((display, links))
    groups = {}
    for d, v in entries:
        c = sort_key(d)[:1].upper()
        groups.setdefault(c if 'A' <= c <= 'Z' else '#', []).append((d, v))
    special = 'Sonderzeichen / Zahlen' if 'Stichwortverzeichnis' in text else 'Special Characters / Numbers'
    out = []
    for g in sorted(k for k in groups if k != '#') + (['#'] if '#' in groups else []):
        out.append(f'### {special if g == "#" else g}\n')
        for d, v in sorted(groups[g], key=lambda e: (sort_key(e[0]), e[0])):
            out.append(f'- {d} – {v}')
        out.append('')
    # replace from the first letter group after the index heading up to the next '---'
    hpos = max(text.find(f'\n## {h}\n') for h in INDEX_HEADINGS)
    start = text.index('\n### ', hpos)
    end = text.index('\n---\n', start)
    text = text[:start] + '\n' + '\n'.join(out) + text[end:]
    open(manual, 'w', encoding='utf-8').write(text)
    print(f'{len(entries)} entries written', file=sys.stderr)

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
