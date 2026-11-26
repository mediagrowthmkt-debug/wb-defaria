"""Artigo a/an antes de cidade com som de vogal (Kevin 26-11-26). Só texto visível, JSON-LD, meta description/og e alt."""
import re
VOG=r'(Andover|Acton|Ipswich|Amesbury|Arlington|Ayer|Essex|Everett|Ashland|Easton|Abington|Auburn|Agawam|Athol|Attleboro|Avon|Uxbridge)'
ART=re.compile(r'(?<![\w/.-])([Aa]) (?='+VOG+r'\b)')
def fix_text(s):
    return ART.sub(lambda m: ('An' if m.group(1)=='A' else 'an')+' ', s)
def fix_articles_html(h):
    # só fora de tags (texto visível) e dentro de <script ld+json>; nunca em atributos/URLs
    out=[];i=0
    for m in re.finditer(r'<script\b[^>]*>.*?</script>|<style\b.*?</style>|<[^>]+>',h,re.S):
        out.append(fix_text(h[i:m.start()]))
        t=m.group(0)
        if t.startswith('<script') and 'application/ld+json' in t[:80]: t=fix_text(t)
        elif t.startswith('<meta') and re.search(r'name="description"|property="og:|name="twitter:',t): t=re.sub(r'content="([^"]*)"',lambda c:'content="'+fix_text(c.group(1))+'"',t)
        elif t.startswith('<img'): t=re.sub(r'alt="([^"]*)"',lambda c:'alt="'+fix_text(c.group(1))+'"',t)
        out.append(t); i=m.end()
    out.append(fix_text(h[i:])); return ''.join(out)
