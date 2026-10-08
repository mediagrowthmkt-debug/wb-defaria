#!/usr/bin/env python3
"""Gera blog/<slug>/index.html a partir de blog/_drafts/<slug>.md + .brief.json,
no mesmo modelo dos artigos publicados (template = small-bathroom-remodel-ideas-north-shore)."""
import json, re, sys, html
from pathlib import Path
sys.path.insert(0, "/Users/bruno/clientes_convidados/clientes/07_mediagrowth/scripts/_lib")
from mg_md import to_html_body, inline

W = Path(__file__).resolve().parent.parent
TPL = (W / "blog/small-bathroom-remodel-ideas-north-shore/index.html").read_text()
BASE = "https://www.defariaconstruction.com"

CFG = {
 "bathroom-remodel-cost-massachusetts": dict(
   eyebrow="Bathroom Remodeling · Cost Guide", card_label="Bathroom · Cost Guide", service="Bathroom remodeling", service_url="/pages/bathroom-remodeling/", crumb="Bathroom Remodel Cost",
   lead="Typical 2026 price ranges on the North Shore, where the money goes, and the hidden items that blow a bathroom budget.",
   hero="images/pages/bathroom-remodeling-detail.webp", hero_alt="Bathroom remodel by DeFaria Construction with fluted vanity and tile accent wall", hero_wh=(1200, 1000),
   fig="images/pages/bathroom-remodeling-after.webp", fig_wh=(1200, 674),
   fig_alt="Finished bathroom remodel by DeFaria Construction on the North Shore",
   keep=[("../small-bathroom-remodel-ideas-north-shore/", "7 small bathroom remodel ideas that add value in North Shore homes"),
         ("../kitchen-remodel-ideas-north-shore/", "14 kitchen remodel ideas that actually work in North Shore homes"),
         ("../kitchen-remodel-cost-massachusetts/", "How much does a kitchen remodel cost in Massachusetts? (2026 breakdown)")]),
 "kitchen-remodel-ideas-north-shore": dict(
   eyebrow="Kitchen Remodeling · Ideas", card_label="Kitchen · Ideas", service="Kitchen remodeling", service_url="/pages/kitchen-remodeling/", crumb="Kitchen Remodel Ideas",
   lead="Fourteen kitchen ideas that fit real North Shore galleys, colonials and capes, what each costs and when it is worth it.",
   hero="images/pages/kitchen-remodeling-detail.webp", hero_alt="Kitchen remodel with large island by DeFaria Construction", hero_wh=(1400, 1050),
   fig="images/pages/kitchen-remodeling-after-img-9226.webp", fig_wh=(1600, 1200),
   fig_alt="Finished kitchen remodel by DeFaria Construction on the North Shore",
   keep=[("../kitchen-remodel-cost-massachusetts/", "How much does a kitchen remodel cost in Massachusetts? (2026 breakdown)"),
         ("../bathroom-remodel-cost-massachusetts/", "How much does a bathroom remodel cost in Massachusetts? (2026 guide)"),
         ("../small-bathroom-remodel-ideas-north-shore/", "7 small bathroom remodel ideas that add value in North Shore homes")]),
 "basement-finishing-cost-massachusetts": dict(
   eyebrow="Basement Finishing · Cost Guide", card_label="Basement · Cost Guide", service="Basement finishing", service_url="/pages/finish-basements/", crumb="Basement Finishing Cost",
   lead="Typical 2026 ranges in Essex and Middlesex County, a line-by-line budget, and the moisture, egress and bathroom costs that move the number.",
   hero="images/pages/finish-basements-after.webp", hero_alt="Finished basement home gym by DeFaria Construction", hero_wh=(1600, 1200),
   fig="images/pages/basement-built-in-shelves.webp", fig_wh=(1200, 900),
   fig_alt="Finished basement with built-in shelving and bench by DeFaria Construction",
   keep=[("../bathroom-remodel-cost-massachusetts/", "How much does a bathroom remodel cost in Massachusetts? (2026 guide)"),
         ("../kitchen-remodel-cost-massachusetts/", "How much does a kitchen remodel cost in Massachusetts? (2026 breakdown)"),
         ("../when-to-book-deck-builder-massachusetts/", "When to book a deck builder in Massachusetts")]),
}

def md_html(md):
    links = []
    def stash(m):
        links.append('<a href="%s">%s</a>' % (html.escape(m.group(2)), inline(m.group(1))))
        return "\x01%d\x01" % (len(links) - 1)
    md = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", stash, md)
    out = to_html_body(md)
    return re.sub(r"\x01(\d+)\x01", lambda m: links[int(m.group(1))], out)

def build(slug, date="2026-10-05", upd="October 2026"):
    c = CFG[slug]; b = json.loads((W / f"blog/_drafts/{slug}.brief.json").read_text())
    md = (W / f"blog/_drafts/{slug}.md").read_text()
    lines = md.splitlines()
    h1 = lines[0].lstrip("# ").strip(); md = "\n".join(lines[1:])
    body, rest = re.split(r"^## FAQ\s*$", md, maxsplit=1, flags=re.M)
    cta_m = re.search(r"^## (.+)$", rest, flags=re.M)
    cta_title = cta_m.group(1).strip(); cta_md = rest[cta_m.end():].strip()
    # figura depois do 2º parágrafo de abertura (antes do 1º H2)
    bh = md_html(body)
    fig = (f'<figure class="article-figure">\n              <img src="../../{c["fig"]}?v=20261005-defaria" alt="{c["fig_alt"]}" '
           f'width="{c["fig_wh"][0]}" height="{c["fig_wh"][1]}" loading="lazy">\n'
           f'              <figcaption>A finished project by DeFaria Construction. Real project photo, not a stock image.</figcaption>\n            </figure>')
    bh = bh.replace("<h2>", fig + "\n<h2>", 1)
    faq_html = "".join(f'\n              <div class="faq-item">\n                <h3>{html.escape(f["q"])}</h3>\n                <p>{html.escape(f["a"])}</p>\n              </div>' for f in b["faq"])
    keep = "".join(f'\n              <li><a href="{u}">{t}</a></li>' for u, t in c["keep"])
    cta_paras = [p for p in cta_md.split("\n\n") if p.strip()]
    cta_txt = "\n".join(f"              <p>{md_html(p).replace('<p>','').replace('</p>','')}</p>" for p in cta_paras)
    url = f"{BASE}/blog/{slug}/"; img = f"{BASE}/{c['hero']}"
    ld = {"@context": "https://schema.org", "@graph": [
      {"@type": "Article", "headline": h1, "description": b["metaDescription"], "image": img,
       "datePublished": date, "dateModified": date,
       "mainEntityOfPage": {"@type": "WebPage", "@id": url},
       "author": {"@type": "Person", "name": "Luiz DeFaria", "jobTitle": "Owner, DeFaria Construction",
                  "description": "Owner of DeFaria Carpentry, Inc., a BBB Accredited (A+) remodeling contractor serving Middlesex and Essex County. Owner-led estimating and project management across the North Shore.",
                  "worksFor": {"@type": "Organization", "name": "DeFaria Construction"}},
       "publisher": {"@type": "Organization", "name": "DeFaria Construction",
                     "logo": {"@type": "ImageObject", "url": f"{BASE}/images/logo/logo-header.webp"}}},
      {"@type": "HomeAndConstructionBusiness", "@id": BASE + "/#business", "name": "DeFaria Construction",
       "url": BASE + "/", "telephone": "+1-617-893-2221", "image": f"{BASE}/images/logo/logo-header.webp",
       "address": {"@type": "PostalAddress", "streetAddress": "24 Fiske Ave", "addressLocality": "Lynn", "addressRegion": "MA", "postalCode": "01902", "addressCountry": "US"},
       "areaServed": ["Essex County, MA", "Middlesex County, MA"]},
      {"@type": "Service", "name": c["service"], "serviceType": c["service"],
       "provider": {"@id": BASE + "/#business"}, "areaServed": ["Essex County, MA", "Middlesex County, MA"], "url": BASE + c["service_url"]},
      {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": f["q"], "acceptedAnswer": {"@type": "Answer", "text": f["a"]}} for f in b["faq"]]},
      {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE + "/"},
        {"@type": "ListItem", "position": 2, "name": "Blog", "item": BASE + "/blog/"},
        {"@type": "ListItem", "position": 3, "name": c["crumb"], "item": url}]}]}
    t = TPL
    head_end = t.index("<!-- Google tag (gtag.js) -->")
    mt, md_ = html.escape(b["metaTitle"]), html.escape(b["metaDescription"])
    head = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{mt}</title>
  <meta name="description" content="{md_}">
  <link rel="canonical" href="{url}">
  <meta name="robots" content="index, follow">
  <meta property="og:type" content="article">
  <meta property="og:title" content="{mt}">
  <meta property="og:description" content="{md_}">
  <meta property="og:image" content="{img}">
  <meta property="og:url" content="{url}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{mt}">
  <meta name="twitter:description" content="{md_}">
  <meta name="twitter:image" content="{img}">
  <link rel="icon" href="../../images/logo/favicon.avif" type="image/avif">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../../css/style.css">
  <link rel="stylesheet" href="../blog.css">

  <script type="application/ld+json">
{json.dumps(ld, indent=2, ensure_ascii=False)}
  </script>
'''
    gtag_to_main = t[head_end:t.index("  <main>")]
    main = f'''  <main>
    <section class="blog-hero">
      <div class="blog-hero__media"><img src="../../{c["hero"]}?v=20261005-defaria" alt="{c["hero_alt"]}" width="{c["hero_wh"][0]}" height="{c["hero_wh"][1]}" fetchpriority="high"></div>
      <div class="blog-hero__shade"></div>
      <div class="container blog-hero__content">
        <a class="breadcrumb" href="../">Home / Blog</a>
        <p class="eyebrow">{c["eyebrow"]}</p>
        <h1>{html.escape(h1)}</h1>
        <p class="blog-hero__lead">{c["lead"]}</p>
        <p class="blog-meta">By <a href="../../#top">Luiz DeFaria</a>, Owner &middot; DeFaria Construction &middot; Updated {upd}</p>
      </div>
    </section>

    <article class="section article">
      <div class="container">
        <div class="article__wrap">
          <p class="byline">
            <img src="../../images/logo/favicon.avif" alt="DeFaria Construction" width="46" height="46">
            By <a href="../../#top">Luiz DeFaria</a>, Owner of DeFaria Construction &middot; BBB Accredited A+ &middot; Updated {upd}
          </p>

          <div class="prose">
{bh}

            <div class="faq-block">
              <h2>Frequently asked questions</h2>{faq_html}
            </div>

            <h2>Keep reading</h2>
            <ul>{keep}
            </ul>

            <div class="article-cta">
              <h2>{html.escape(cta_title)}</h2>
{cta_txt}
              <div class="article-cta__actions">
                <a class="btn btn--secondary" href="tel:+16178932221">Call (617) 893-2221</a>
                <a class="btn btn--ghost" href="../../#contact">Request Your Free Estimate</a>
              </div>
            </div>
'''
    tail = t[t.index("            <aside class=\"author-box\">"):]
    tail = tail.replace("<strong>Luiz DeFaria</strong> — Owner", "<strong>Luiz DeFaria</strong>, Owner")
    out = head + gtag_to_main + main + "\n" + tail
    d = W / f"blog/{slug}"; d.mkdir(exist_ok=True); (d / "index.html").write_text(out)
    print("ok", d / "index.html", len(out))

if __name__ == "__main__":
    for s in sys.argv[1:] or CFG: build(s)
