#!/usr/bin/env python3
"""Build static reading copies without modifying the canonical Markdown sources."""
from pathlib import Path
from html import escape
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://pgvozdev1973.github.io/'
DOI = 'https://doi.org/10.5281/zenodo.22849217'
REPO = 'https://github.com/PGvozdev1973/PGvozdev1973.github.io'
DATE = '2026-10-29'
STYLE = '''html{color-scheme:light dark}body{max-width:48rem;margin:auto;padding:1.5rem;font:1.1rem/1.65 Georgia,serif}a{color:#3068ae}nav,aside,footer{font:1rem/1.6 system-ui,sans-serif}nav{display:flex;gap:1rem;flex-wrap:wrap}h1{font-size:1.9rem;line-height:1.2}pre{font:inherit;white-space:pre-wrap;overflow-wrap:anywhere}li{margin:.4rem 0}a:focus-visible{outline:3px solid;outline-offset:3px}@media(prefers-color-scheme:dark){a{color:#a8c9ff}}'''
generated = []

def page(path, title, body, lang='en'):
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(f'''<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)} — Peter Gvozdev</title>
<meta name="description" content="{escape(title, quote=True)}. Canonical version 5.15, Peter Gvozdev. Static reading edition.">
<meta name="author" content="Peter Gvozdev">
<meta name="robots" content="index,follow">
<meta name="citation_author" content="Gvozdev, Peter">
<meta name="citation_title" content="Meta-Symbiotic Theory: Constitutional Architecture for Relational Intelligence">
<meta name="citation_publication_date" content="2026/09/16">
<meta name="citation_doi" content="10.5281/zenodo.22849217">
<link rel="canonical" href="{BASE}{path}">
<style>{STYLE}</style></head><body>
<nav aria-label="Reading navigation"><a href="/">MST home</a><a href="/read/">Reading index</a><a href="{DOI}">Authoritative edition on Zenodo</a></nav>
<main><h1>{escape(title)}</h1>{body}</main>
<footer><p>Peter Gvozdev · v5.15 · 16 September 2026 · CC BY-ND 4.0. The Zenodo PDF remains authoritative.</p></footer>
</body></html>
''', encoding='utf-8')
    generated.append(path)

def reading(path, title, text, lang='en', navigation=''):
    page(path, title, navigation + '<article aria-label="Manuscript text"><pre id="canonical-text">' + escape(text) + '</pre></article>' + navigation, lang)

sources = [('mst-summary', 'MST — Canonical summary', 'en'),
           ('mst-v5.15-en', 'MST v5.15 — Full English text', 'en'),
           ('mst-v5.15-bg', 'MST v5.15 — Bulgarian translation', 'bg')]
texts = {}
for stem, title, lang in sources:
    raw = (ROOT / (stem + '.md')).read_bytes()
    text = raw.decode('utf-8')
    texts[stem] = text
    (ROOT / (stem + '.txt')).write_bytes(raw)
    reading(stem + '.html', title, text, lang)

# Smaller, sequential excerpts cover the entire English source, exactly once.
text = texts['mst-v5.15-en']
chapters = list(re.finditer(r'^## Chapter ([IVX]+) — (.+)$', text, re.M))
assert len(chapters) == 24, 'Review chapter boundaries before regenerating a different edition'
afterword = text.index('# Afterword —')
boundaries = [0] + [m.start() for m in chapters] + [afterword, len(text)]
titles = ['Opening material and practical architecture'] + [m.group(0)[3:] for m in chapters] + ['Afterword, coda and appendices']
chunks = [text[a:b] for a, b in zip(boundaries, boundaries[1:])]
assert ''.join(chunks) == text
paths = [f'read/section-{i:02}.html' for i in range(len(chunks))]
for i, (path, title, chunk) in enumerate(zip(paths, titles, chunks)):
    links = []
    if i:
        links.append(f'<a rel="prev" href="/{paths[i-1]}">Previous section</a>')
    if i + 1 < len(chunks):
        links.append(f'<a rel="next" href="/{paths[i+1]}">Next section</a>')
    navigation = '<nav aria-label="Section navigation">' + ' '.join(links) + '</nav>'
    reading(path, 'MST v5.15 — ' + title, chunk, navigation=navigation)

formats = ''.join(f'<li><a href="/{stem}.html">{escape(title)}</a> · <a href="/{stem}.txt" download>Download text</a> · <a href="/{stem}.md">Markdown</a></li>' for stem, title, _ in sources)
contents = ''.join(f'<li><a href="/{path}">{escape(title)}</a></li>' for path, title in zip(paths, titles))
page('read/index.html', 'Read Meta-Symbiotic Theory', f'''<p>Canonical version 5.15 by Peter Gvozdev. Choose the complete text or a smaller section.</p>
<h2>Complete editions</h2><ul>{formats}</ul>
<h2>English text by section</h2><ol>{contents}</ol>
<h2>Alternative access</h2><p>If this website cannot be opened in your reading tool, try the <a href="{REPO}/blob/main/mst-v5.15-en.md">English text on GitHub</a>, the <a href="https://raw.githubusercontent.com/PGvozdev1973/PGvozdev1973.github.io/main/mst-v5.15-en.md">raw text on GitHub</a>, or the <a href="{DOI}">authoritative Zenodo record</a>. You can also download a text file above and attach it directly to your conversation.</p>''')

# Preserve historical lastmod dates for existing pages; add only generated HTML.
ns = 'http://www.sitemaps.org/schemas/sitemap/0.9'
ET.register_namespace('', ns)
tree = ET.parse(ROOT / 'sitemap.xml')
root = tree.getroot()
known = {u.find(f'{{{ns}}}loc').text: u for u in root}
for path in [''] + generated:
    url = BASE + path
    node = known.get(url)
    if node is None:
        node = ET.SubElement(root, f'{{{ns}}}url')
        ET.SubElement(node, f'{{{ns}}}loc').text = url
    modified = node.find(f'{{{ns}}}lastmod')
    if modified is None:
        modified = ET.SubElement(node, f'{{{ns}}}lastmod')
    modified.text = DATE
ET.indent(tree, space='  ')
tree.write(ROOT / 'sitemap.xml', encoding='UTF-8', xml_declaration=True)
print(f'Built {len(generated)} HTML pages and 3 exact text copies; {len(chunks)} sections cover the complete English manuscript.')
