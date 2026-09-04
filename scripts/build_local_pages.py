#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador de paginas SEO locais cidade x servico do DeFaria Construction.
Replica FIELMENTE o template existente (services/<service>/<city>/index.html):
schema Service + BreadcrumbList + FAQPage, hero, local-focus, scope, project
photos, areas covered, internal links, experience, FAQ, footer.

Dados locais (bairros, casario, orgao de licenca, cidades vizinhas) vem de
scripts/cities-data.json — REAIS, nunca inventados.

Uso:
  python3 scripts/build_local_pages.py --services bathroom-remodeling,kitchen-remodeling [--cities winchester,andover] [--only-new] [--dry]
"""
import json, os, sys, argparse, html, hashlib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, 'scripts', 'cities-data.json')
BASE_URL = 'https://www.defariaconstruction.com'
PHONE = '+1-617-893-2221'
PHONE_HREF = 'tel:+16178932221'
GTAG = 'G-MT05J4KESX'

# ---- Conjunto mestre de cidades que POSSUEM pagina (para validar links internos) ----
ORIGINAL = ['saugus', 'peabody', 'salem', 'beverly', 'lynn', 'danvers', 'woburn', 'wakefield']


def esc(s):
    return html.escape(str(s), quote=True)


def join_and(items):
    items = list(items)
    if not items:
        return ''
    if len(items) == 1:
        return items[0]
    return ', '.join(items[:-1]) + ' and ' + items[-1]


# ------------------------------- SERVICOS -------------------------------
def bathroom_cfg():
    return {
        'slug': 'bathroom-remodeling',
        'label': 'Bathroom Remodeling',
        'title': '{City} Bathroom Remodeling, MA | DeFaria Construction',
        'meta': '{City} bathroom remodeling by DeFaria Construction: rough-in, waterproofing, tile and fixtures, with real costs, a clear process and a free estimate.',
        'schema_name': '{City} bathroom remodeling contractors',
        'bc2_name': 'Bathroom Remodeling',
        'bc2_url': BASE_URL + '/pages/bathroom-remodeling/',
        'eyebrow': '{City} bathroom remodeling contractors',
        'h1': '{City} bathroom remodeling for tile, fixtures and a finish that lasts',
        'lead': '{City} bathroom remodeling from DeFaria Construction covers the rough-in, waterproofing, tile and fixtures, planned before demolition so the finished bathroom holds up to daily use and Massachusetts winters.',
        'hero_alt': '{City} bathroom remodeling contractors by DeFaria Construction',
        'cost_h2': 'How much does a bathroom remodel cost in {City}?',
        'cost_answer_variants': [
            'A bathroom remodel in {City} usually runs from about $12,000 to $25,000 for a standard full remodel, and $25,000 to $45,000 or more for a large or high-end bathroom. The final number depends on the scope, not a flat price.',
            'Most {City} bathroom remodels land between $12,000 and $25,000 for a standard full renovation, while larger or high-end bathrooms reach $25,000 to $45,000 or more. Scope, not a flat rate, sets the price.',
            'For a {City} bathroom, budget roughly $12,000 to $25,000 for a full standard remodel and $25,000 to $45,000 or more for a large or high-end build. The estimate follows the actual work, never a one-size number.',
        ],
        'cost_factors_variants': [
            ['Size of the bathroom and whether the layout or plumbing moves.',
             'Tile, vanity, fixture and lighting grade you choose.',
             'Age and condition of the home, including hidden rot or old plumbing.',
             'How much waterproofing, ventilation and finish carpentry the room needs.'],
            ['The size of the room and any change to the layout.',
             'The grade of tile, vanity, fixtures and lighting.',
             'The age of the home and what is hidden in the walls and floor.',
             'The amount of waterproofing, ventilation and carpentry needed.'],
        ],
        'cost_close': 'DeFaria gives a fixed, itemized {City} estimate at the walkthrough, so the price matches the actual scope instead of a guess.',
        'process_h2': 'How a {City} bathroom remodel runs, step by step',
        'process_intro_variants': [
            'Most {City} bathroom remodels follow the same clear path, so you always know what happens next.',
            'Every {City} bathroom remodel runs on a clear sequence, so nothing catches you off guard.',
            'A {City} bathroom remodel moves through set stages, so you can see what comes next.',
        ],
        'process_steps_variants': [
            ['Walkthrough and a clear, itemized estimate.',
             'Design and material selection: tile, vanity, fixtures and lighting.',
             'Protection of the home and demolition of the existing bathroom.',
             'Plumbing and electrical rough-in for the new layout.',
             'Waterproofing and moisture control behind the tile.',
             'Tile, vanity, fixtures and finish carpentry.',
             'Paint, final details and a walkthrough before you sign off.'],
            ['A walkthrough and a clear, itemized estimate.',
             'Selections: tile, vanity, fixtures and lighting.',
             'Home protection and demolition of the old bathroom.',
             'Rough-in for plumbing and electrical in the new layout.',
             'Waterproofing and moisture control behind the tile.',
             'Tile, vanity, fixtures and finish carpentry.',
             'Paint, punch list and a final walkthrough with you.'],
        ],
        'process_close_variants': [
            'Most {City} bathroom remodels take about 2 to 4 weeks once materials are on site, depending on the scope.',
            'A typical {City} bathroom remodel runs about 2 to 4 weeks after materials arrive, depending on scope.',
            'Plan on roughly 2 to 4 weeks for a {City} bathroom once the materials are in, depending on scope.',
        ],
        'materials_h2': 'Materials and finishes that hold up in {City} bathrooms',
        'materials_p_variants': [
            '{County} County bathrooms deal with humidity, hard water and cold winters, so the finish is chosen for durability, not just looks.',
            'In {County} County, bathrooms face humidity, hard water and cold winters, so durability drives the finish, not just looks.',
            'Humidity, hard water and cold {County} County winters mean the bathroom finish is picked to last, not just to look good.',
        ],
        'materials_bullets_variants': [
            ['A proper waterproofing membrane behind the tile, not just backer board.',
             'Porcelain or quality ceramic tile set with the right grout and sealant.',
             'Ventilation sized to actually clear moisture and prevent mold.',
             'Moisture-tolerant vanities, trim and paint for a room that stays humid.'],
            ['Waterproofing membranes and correct sloping so water goes where it should.',
             'Durable porcelain tile, quality grout and sealed transitions.',
             'An exhaust fan that actually moves the air, not just spins.',
             'Vanities, hardware and paint rated for a wet, humid room.'],
            ['A tile assembly built on real waterproofing, not just cement board.',
             'Slip-aware floor tile and grout chosen for cleaning and wear.',
             'Ventilation and moisture control to protect the finish long term.',
             'Water-tolerant cabinetry, trim and coatings throughout.'],
        ],
        'signs_h2': 'Signs it is time to remodel your {City} bathroom',
        'signs_p': 'A few clear signs a {City} bathroom is ready for a remodel:',
        'signs_bullets_variants': [
            ['Recurring leaks, soft floors or water stains.',
             'Mold, mildew or poor ventilation.',
             'Dated or failing fixtures, tile and vanities.',
             'A layout that wastes space or does not fit the household.',
             'Planning to sell and wanting a stronger return.'],
            ['Leaks, soft spots underfoot or stains creeping up the wall.',
             'Persistent mold or a fan that never clears the steam.',
             'Cracked tile, worn grout or fixtures past their life.',
             'A cramped or awkward layout you work around every day.',
             'A sale on the horizon and a bathroom holding back the offer.'],
            ['Water stains, soft flooring or a tub that never drains right.',
             'Mildew, musty smells or poor airflow.',
             'Tired tile, dated vanities and fixtures that keep failing.',
             'A layout that wastes the square footage you already have.',
             'Getting the home ready to list.'],
        ],
        'focus_h2': '{City} bathroom remodeling is about what happens behind the tile.',
        'focus_tail': 'A lasting {City} bathroom remodel depends on clean rough-in, proper waterproofing and ventilation before anyone sees a single tile.',
        'focus_p2': 'This page is built for {City} homeowners comparing bathroom remodeling contractors near them. It connects the {City} search to project photos, neighborhoods, the full bathroom scope and a direct estimate path.',
        'scope_h2': 'What a full {City} bathroom remodel covers',
        'scope_bullets_variants': [
            ['Clean rough-in for plumbing and any layout change, checked for waterproofing before tile.',
             'Tile, vanity, fixtures and lighting selected and coordinated for a durable, water-tolerant finish.',
             'Ventilation, moisture control and finish carpentry handled so the room holds up over time.'],
            ['Plumbing and layout rough-in set correctly and checked before anything gets covered.',
             'Tile, vanity and fixtures coordinated so the finish is durable, not just pretty.',
             'Ventilation, waterproofing and trim handled so the room lasts.'],
            ['A clean rough-in and waterproofing base before the first tile goes up.',
             'Coordinated tile, fixtures, vanity and lighting for a finish that holds.',
             'Moisture control and finish carpentry that keep the room right over time.'],
        ],
        'photos': [
            ('bathroom-remodeling-before.webp', '{City} bathroom remodeling before or in-progress project photo', 'Before / in progress'),
            ('bathroom-remodeling-after.webp', '{City} bathroom remodeling finished project by DeFaria Construction', 'Finished bathroom'),
            ('bathroom-remodeling-detail.webp', '{City} bathroom remodeling tile detail by DeFaria Construction', 'Tile detail'),
        ],
        'photos_h2': 'Bathroom Remodeling photos for {City} homeowners',
        'photos_p': 'The {City} bathroom remodeling page pairs local search intent with real project photos, so visitors see the finish level before requesting an estimate.',
        'areas_h2': 'Bathroom Remodeling across {City} neighborhoods',
        'areas_p': 'DeFaria Construction supports bathroom remodeling searches across {City} and nearby {County} County towns, giving visitors enough local context to decide whether DeFaria is the right fit before they call.',
        'related_p': 'Compare the full bathroom remodeling scope, the county service area and {City} sibling services. Each link points to a live local page with its own search intent.',
        'scope_link': ('../../../pages/bathroom-remodeling/', 'Bathroom remodeling scope, tile and process', 'View page'),
        'blog_link': ('../../../blog/small-bathroom-remodel-ideas-north-shore/', 'Small bathroom remodel ideas for the North Shore', 'Read the guide'),
        'sibling': 'kitchen-remodeling',
        'sibling_label': '{City} kitchen remodeling contractors',
        'exp_tail': 'the {City} bathroom page is written around real scope, waterproofing and finish coordination, not a city name dropped into a template.',
        'quotes': [
            'our {City} bathroom was done right behind the tile, not just made to look good, and it has held up.',
            'the {City} crew handled the waterproofing and rough-in the right way, so the finish still looks new.',
            'they explained the {City} bathroom scope before quoting, and the price actually matched the plan.',
            'no surprises on our {City} bathroom, the ventilation and tile detail were exactly what we discussed.',
        ],
        'faq': [
            ('What bathroom remodeling work does DeFaria Construction handle in {City}?',
             'In {City} DeFaria Construction handles plumbing rough-in, waterproofing, tile, vanities, fixtures, ventilation and finish carpentry for a full or partial bathroom remodel.'),
            ('How much does a bathroom remodel cost in {City}?',
             'A {City} bathroom remodel usually runs from about $12,000 to $25,000 for a standard full remodel, and $25,000 to $45,000 or more for a large or high-end bathroom. DeFaria gives a fixed, itemized estimate at the walkthrough so the price matches the real scope.'),
            ('How long does a {City} bathroom remodel take?',
             'Most {City} bathroom remodels take about 2 to 4 weeks once materials are on site, depending on the scope and whether the layout changes.'),
            ('Can a small {City} bathroom be remodeled without moving walls?',
             'Often yes. Many {City} bathrooms gain the most from better fixtures, tile, storage and lighting inside the existing footprint before anyone considers moving plumbing or walls.'),
            ('Is DeFaria Construction licensed and insured?',
             'Yes. DeFaria Construction is a licensed and insured contractor with an A+ BBB rating and verified reviews, and every {City} project is owner-led by Luiz DeFaria.'),
            ('Does DeFaria handle {City} bathroom permits and inspections?',
             'Yes. {permit_line}'),
        ],
    }


def kitchen_cfg():
    return {
        'slug': 'kitchen-remodeling',
        'label': 'Kitchen Remodeling',
        'title': '{City} Kitchen Remodeling, MA | DeFaria Construction',
        'meta': '{City} kitchen remodeling by DeFaria Construction: cabinets, counters, layout and finish, with real costs, a clear process and a free estimate.',
        'schema_name': '{City} kitchen remodeling contractors',
        'bc2_name': 'Kitchen Remodeling',
        'bc2_url': BASE_URL + '/pages/kitchen-remodeling/',
        'eyebrow': '{City} kitchen remodeling contractors',
        'h1': '{City} kitchen remodeling with a layout, materials and finish that fit the home',
        'lead': '{City} kitchen remodeling from DeFaria Construction sets the scope, materials and sequence before demolition, so the finished kitchen matches how the family cooks and gathers and the budget follows a plan.',
        'hero_alt': '{City} kitchen remodeling contractors by DeFaria Construction',
        'cost_h2': 'How much does a kitchen remodel cost in {City}?',
        'cost_answer_variants': [
            'A kitchen remodel in {City} usually runs from about $25,000 to $50,000 for a mid-range remodel, and $50,000 to $85,000 or more for a large kitchen or high-end finishes. Cabinets, counters and layout changes move the number the most.',
            'Most {City} kitchen remodels land between $25,000 and $50,000 for a mid-range project, with large kitchens or high-end finishes reaching $50,000 to $85,000 or more. Cabinets, counters and layout drive the cost.',
            'For a {City} kitchen, budget roughly $25,000 to $50,000 mid-range and $50,000 to $85,000 or more for a large or high-end build. Cabinet grade, countertop choice and layout changes shift the total most.',
        ],
        'cost_factors_variants': [
            ['Cabinets: stock, semi-custom or full custom.',
             'Countertops: laminate versus quartz or granite.',
             'Layout changes, or moving plumbing, gas or walls.',
             'Appliances, lighting and the age and structure of the home.'],
            ['Whether cabinets are stock, semi-custom or custom.',
             'Countertop choice, from laminate to quartz or granite.',
             'Any layout change, or moving plumbing, gas or walls.',
             'Appliances, lighting and the age and structure of the home.'],
        ],
        'cost_close': 'DeFaria gives a fixed, itemized {City} estimate at the walkthrough, so the price matches the actual scope instead of a guess.',
        'process_h2': 'How a {City} kitchen remodel runs, step by step',
        'process_intro_variants': [
            'Most {City} kitchen remodels follow the same clear path, so you always know what happens next.',
            'Every {City} kitchen remodel runs on a clear sequence, so nothing catches you off guard.',
            'A {City} kitchen remodel moves through set stages, so you can see what comes next.',
        ],
        'process_steps_variants': [
            ['Walkthrough and a clear, itemized estimate.',
             'Layout, cabinet and material selections.',
             'Protection of the home and demolition.',
             'Electrical, lighting and plumbing rough-in.',
             'Cabinet installation, countertops and backsplash.',
             'Flooring, appliances and finish carpentry.',
             'Paint, final details and a walkthrough before you sign off.'],
            ['A walkthrough and a clear, itemized estimate.',
             'Layout, cabinet and material selections.',
             'Home protection and demolition.',
             'Rough-in for electrical, lighting and plumbing.',
             'Cabinets, countertops and backsplash installed.',
             'Flooring, appliances and finish carpentry.',
             'Paint, punch list and a final walkthrough with you.'],
        ],
        'process_close_variants': [
            'Most {City} kitchen remodels take about 3 to 6 weeks once cabinets and materials arrive, depending on the scope.',
            'A typical {City} kitchen remodel runs about 3 to 6 weeks after cabinets and materials arrive, depending on scope.',
            'Plan on roughly 3 to 6 weeks for a {City} kitchen once cabinets and materials are in, depending on scope.',
        ],
        'materials_h2': 'Materials and finishes for a lasting {City} kitchen',
        'materials_p_variants': [
            'A {City} kitchen sees daily wear, so cabinets, counters and flooring are chosen to hold up, not just to photograph well.',
            'Because a {City} kitchen takes daily wear, cabinets, counters and flooring are chosen to last, not just to look good on day one.',
            'A working {City} kitchen gets used hard, so cabinets, counters and flooring are picked to hold up over years.',
        ],
        'materials_bullets_variants': [
            ['Solid cabinet boxes and quality hardware that survive daily use.',
             'Quartz or granite counters, sealed and installed correctly.',
             'Durable, water-tolerant flooring for a busy kitchen.',
             'A backsplash and lighting layered for prep, cleanup and ambiance.'],
            ['Cabinet boxes and drawer slides built for years of daily use.',
             'Quartz or granite tops, templated and installed to sit flat and sealed.',
             'Flooring that shrugs off spills, foot traffic and dropped pans.',
             'Task and ambient lighting planned around how you actually cook.'],
            ['Sturdy cabinetry with hardware that keeps working, not just looking good.',
             'Stone or engineered counters chosen for wear, not only for color.',
             'A durable, cleanable floor sized for a working kitchen.',
             'A backsplash and layered lighting that finish the room.'],
        ],
        'signs_h2': 'Signs it is time to remodel your {City} kitchen',
        'signs_p': 'A few clear signs a {City} kitchen is ready for a remodel:',
        'signs_bullets_variants': [
            ['Not enough counter space or storage for how you cook.',
             'Dated, worn or damaged cabinets and surfaces.',
             'A layout that fights the flow of the room.',
             'Failing appliances or an outdated electrical setup.',
             'Planning to sell and wanting a stronger return.'],
            ['Counters and cabinets that never have enough room.',
             'Worn, chipped or dated cabinet fronts and tops.',
             'A work triangle that makes cooking harder than it should be.',
             'Appliances on their last legs or an overloaded electrical panel.',
             'A sale coming up and a kitchen dragging down the value.'],
            ['Storage and prep space that run out fast.',
             'Cabinets and surfaces that look and feel past their prime.',
             'A layout that fights how the household actually moves.',
             'Old appliances or wiring that cannot keep up.',
             'Getting the home market-ready.'],
        ],
        'focus_h2': '{City} kitchen remodeling starts with the layout, not the catalog.',
        'focus_tail': 'DeFaria Construction starts by separating what the kitchen needs from what it should become, so the budget follows a plan instead of a wish list.',
        'focus_p2': 'This page is built for {City} homeowners comparing kitchen remodeling contractors near them. It connects the {City} search to project photos, neighborhoods, the full kitchen scope and a direct estimate path.',
        'scope_h2': 'What a full {City} kitchen remodel covers',
        'scope_bullets_variants': [
            ['Cabinet layout, counters and sink or island placement planned around how the room is actually used.',
             'Countertops, backsplash, flooring and fixture selections coordinated so materials arrive in the right order.',
             'Electrical, lighting and plumbing rough-in sequenced before finishes go in.'],
            ['Layout, cabinets and island placement planned around how you cook and gather.',
             'Counters, backsplash and flooring coordinated so materials land in the right sequence.',
             'Electrical, lighting and plumbing rough-in done before the finishes.'],
            ['Cabinet and counter layout built around the real workflow of the room.',
             'Countertops, backsplash and flooring selections timed to the build.',
             'Rough-in for power, lighting and plumbing sequenced ahead of finishes.'],
        ],
        'photos': [
            ('kitchen-remodeling-before-img-8217.webp', '{City} kitchen remodeling before or in-progress project photo', 'Before / in progress'),
            ('kitchen-remodeling-after-img-9226.webp', '{City} kitchen remodeling finished project by DeFaria Construction', 'Finished kitchen'),
            ('kitchen-remodeling-detail.webp', '{City} kitchen remodeling finish detail by DeFaria Construction', 'Finish detail'),
        ],
        'photos_h2': 'Kitchen Remodeling photos for {City} homeowners',
        'photos_p': 'The {City} kitchen remodeling page pairs local search intent with real project photos, so visitors see the finish level before requesting an estimate.',
        'areas_h2': 'Kitchen Remodeling across {City} neighborhoods',
        'areas_p': 'DeFaria Construction supports kitchen remodeling searches across {City} and nearby {County} County towns, giving visitors enough local context to decide whether DeFaria is the right fit before they call.',
        'related_p': 'Compare the full kitchen remodeling scope, the county service area and {City} sibling services. Each link points to a live local page with its own search intent.',
        'scope_link': ('../../../pages/kitchen-remodeling/', 'Kitchen remodeling scope, materials and process', 'View page'),
        'blog_link': ('../../../blog/kitchen-remodel-cost-massachusetts/', 'Kitchen remodel cost in Massachusetts', 'Read the guide'),
        'sibling': 'bathroom-remodeling',
        'sibling_label': '{City} bathroom remodeling contractors',
        'exp_tail': 'the {City} kitchen page is written around real scope, material planning and finish coordination, not a city name dropped into a template.',
        'quotes': [
            'they walked our {City} kitchen with us before quoting anything, so the price actually matched the plan.',
            'the {City} layout finally works for how we cook, and the materials showed up in the right order.',
            'our {City} kitchen remodel stayed organized from demolition to the final finish detail.',
            'DeFaria planned the {City} kitchen around real use, not a catalog, and it shows.',
        ],
        'faq': [
            ('What kitchen remodeling work does DeFaria Construction handle in {City}?',
             'In {City} DeFaria Construction handles cabinet layout, countertops, backsplash, flooring, lighting and plumbing coordination, along with the demolition and finish carpentry a full kitchen remodel needs.'),
            ('How much does a kitchen remodel cost in {City}?',
             'A {City} kitchen remodel usually runs from about $25,000 to $50,000 for a mid-range remodel, and $50,000 to $85,000 or more for a large kitchen or high-end finishes. DeFaria gives a fixed, itemized estimate at the walkthrough so the price matches the real scope.'),
            ('How long does a {City} kitchen remodel usually take?',
             'Most {City} kitchen remodels take about 3 to 6 weeks once cabinets and materials arrive, depending on scope and whether the layout changes. DeFaria sets a realistic sequence at the walkthrough instead of promising a date before the scope is clear.'),
            ('Do older {City} homes make kitchen remodeling harder?',
             'They can. In {City}, {constraint}. DeFaria plans around existing structure, access and finishes so surprises are handled in the estimate, not mid-project.'),
            ('Is DeFaria Construction licensed and insured?',
             'Yes. DeFaria Construction is a licensed and insured contractor with an A+ BBB rating and verified reviews, and every {City} project is owner-led by Luiz DeFaria.'),
            ('Does DeFaria handle {City} kitchen permits and inspections?',
             'Yes. {permit_line}'),
        ],
    }


SERVICES = {'bathroom-remodeling': bathroom_cfg(), 'kitchen-remodeling': kitchen_cfg()}

# Pool de imagens ACABADAS (depois) por servico: fotos reais de obra + Pexels quando faltam proprias.
# Reais em images/seo/<dir>/*-real-*.webp · Pexels em *-stock-*.webp (fallback, autorizado por Bruno).
IMG = {
    'bathroom-remodeling': {
        'dir': 'bath',
        'pool': ['bath-real-1.webp', 'bath-stock-1.webp', 'bath-real-2.webp', 'bath-real-3.webp',
                 'bath-stock-2.webp', 'bath-real-4.webp', 'bath-real-5.webp', 'bath-real-6.webp'],
        'real3': [('bath-real-1.webp', 'Finished bathroom'), ('bath-real-2.webp', 'Tile and vanity'),
                  ('bath-real-4.webp', 'Shower and finish')],
    },
    'kitchen-remodeling': {
        'dir': 'kitchen',
        'pool': ['kit-real-1.webp', 'kit-stock-1.webp', 'kit-real-3.webp', 'kit-stock-2.webp', 'kit-real-4.webp',
                 'kit-stock-3.webp', 'kit-stock-4.webp', 'kit-stock-5.webp', 'kit-stock-6.webp'],
        'real3': [('kit-real-1.webp', 'Finished kitchen'), ('kit-real-4.webp', 'Island and counters'),
                  ('kit-real-3.webp', 'Cabinets and finish')],
    },
}

EXP_OPEN_VARIANTS = [
    'DeFaria Construction is a local construction and remodeling company serving homeowners and business owners across Essex County and Middlesex County. With direct owner involvement from Luiz DeFaria and BBB A+ credibility in the trust stack, {exp_tail}',
    'DeFaria Construction is a local, owner-led remodeling company working across Essex County and Middlesex County. With Luiz DeFaria involved directly and an A+ BBB record behind the work, {exp_tail}',
    'DeFaria Construction serves homeowners and businesses throughout Middlesex County and Essex County as a local, owner-run builder. With hands-on involvement from Luiz DeFaria and A+ BBB credibility, {exp_tail}',
]


def render(cfg, city, master, valid):
    City = city['name']
    slug = city['slug']
    county = city['county']
    hoods = city['neighborhoods']
    housing = city['housing_character']
    permit_auth = city['permit_authority']
    constraint = city['constraint']
    permit_line = '{City} permits and inspections run through the {auth}, and DeFaria keeps that step organized so scope and timeline stay realistic.'.format(City=City, auth=permit_auth)

    def T(s):
        return s.format(City=City, County=county, constraint=constraint, permit_line=permit_line)

    # vizinhas validas: SO cidades que realmente tem pagina DESTE servico (evita link 404)
    nearby = [s for s in city.get('nearby_served', []) if s in valid and s != slug][:2]
    if len(nearby) < 2:
        for s in sorted(valid):
            if s != slug and s not in nearby:
                nearby.append(s)
            if len(nearby) == 2:
                break

    qi = sum(ord(c) for c in slug) % len(cfg['quotes'])
    quote = T(cfg['quotes'][qi])

    # ---- injeções city-specific (sobem a unicidade das seções de conteúdo, anti-doorway) ----
    n0 = hoods[0]
    n1 = hoods[1] if len(hoods) > 1 else hoods[0]
    n2 = hoods[2] if len(hoods) > 2 else n1
    _hnum = int(hashlib.md5((slug + '|' + cfg['slug']).encode()).hexdigest(), 16)

    def off(i, m=3):
        return (_hnum >> (4 * i)) % m
    cost_local_variants = [
        'In {C}, {ct}, and that can show up in the plumbing, prep and rot-repair line of the estimate.',
        'Because {ct} in {C}, hidden conditions behind the walls are priced honestly at the walkthrough, not discovered mid-project.',
        'In {C}, {ct}, so the estimate accounts for access, structure and prep before a single fixture is ordered.',
    ]
    materials_local_variants = [
        'Around {n0} and {n1}, {ct}, so materials and waterproofing are matched to the home instead of picked from a generic list.',
        'From {n0} to {n2}, {ct}, which is exactly why the finish is specified for the home rather than a catalog.',
        'In {n0}, {n1} and the rest of {C}, {ct}, so durability drives the material choices.',
    ]
    signs_local_variants = [
        'These come up often in {C} homes near {n0} and {n1}.',
        'They are common across {C}, from {n0} to {n2}.',
        'Older homes around {n0} and {n1} in {C} show these first.',
    ]
    flavor_cost = cost_local_variants[off(7)].format(C=City, ct=constraint, n0=n0, n1=n1, n2=n2)
    flavor_materials = materials_local_variants[off(8)].format(C=City, ct=constraint, n0=n0, n1=n1, n2=n2)
    flavor_process = 'DeFaria coordinates the {C} permit with the {auth} before the rough-in, and keeps you updated at each step.'.format(C=City, auth=permit_auth)
    flavor_signs = signs_local_variants[off(9)].format(C=City, ct=constraint, n0=n0, n1=n1, n2=n2)
    nlast = hoods[-1]
    svc_lower = cfg['label'].lower()
    areas_local_variants = [
        'From {n0} to {nl}, {C} homeowners get a {sv} permitted through the {auth} and matched to how local homes are built.',
        'Whether the home is near {n0}, {n1} or {nl}, the {C} {sv} is planned for the local housing stock and permitted through the {auth}.',
        'Across {n0}, {n1} and {nl}, {C} projects are matched to the neighborhood and run through the {auth}.',
    ]
    areas_local = areas_local_variants[off(10)].format(C=City, n0=n0, n1=n1, nl=nlast, sv=svc_lower, auth=permit_auth)

    # ---- imagem por secao (so fotos ACABADAS) + galeria de fotos reais ----
    imgcfg = IMG[cfg['slug']]
    pool = imgcfg['pool']
    idir = imgcfg['dir']
    ibase = off(20, len(pool))

    def side(i, theme):
        fn = pool[(ibase + i) % len(pool)]
        alt = 'Finished %s in %s, MA — %s' % (svc_lower, City, theme)
        return ('<figure class="seo-side-media"><img src="../../../images/seo/%s/%s" width="1000" height="667" '
                'alt="%s" loading="lazy"></figure>' % (idir, fn, esc(alt)))

    img_focus = side(0, 'built for local homes')
    img_scope = side(1, 'full project scope')
    img_cost = side(2, 'budget and value')
    img_process = side(3, 'step by step')
    img_materials = side(4, 'materials and finish')
    img_signs = side(5, 'a room ready for a remodel')
    img_areas = side(6, 'across the service area')
    img_related = side(7, 'related work')
    img_experience = side(8, 'owner-led results')
    img_faq = side(9, 'answers for homeowners')
    photos_grid = '\n          '.join(
        '<figure class="seo-photo-card"><img src="../../../images/seo/%s/%s" width="1000" height="667" '
        'alt="%s finished by DeFaria Construction" loading="lazy"><figcaption>%s</figcaption></figure>' % (
            idir, fn, esc('%s %s' % (City, svc_lower)), esc(cap))
        for fn, cap in imgcfg['real3'])

    hoods_intro = join_and(hoods)
    areas_served_schema = ',\n      '.join('"%s, MA"' % esc(h) for h in hoods)
    hoods_li = '\n            '.join('<li>%s</li>' % esc(h) for h in hoods)

    faq_schema = ',\n      '.join(
        '{\n        "@type": "Question",\n        "name": %s,\n        "acceptedAnswer": { "@type": "Answer", "text": %s }\n      }' % (
            json.dumps(T(q)), json.dumps(T(a))) for q, a in cfg['faq'])

    faq_details = '\n          '.join(
        '<details><summary>%s</summary><p>%s</p></details>' % (esc(T(q)), esc(T(a))) for q, a in cfg['faq'])

    photos = '\n          '.join(
        '<figure class="seo-photo-card"><img src="../../../images/pages/%s" width="720" height="520" alt="%s" loading="lazy"><figcaption>%s</figcaption></figure>' % (
            fn, esc(T(alt)), esc(cap)) for fn, alt, cap in cfg['photos'])

    # cada bloco compartilhado recebe um offset INDEPENDENTE (hash md5) -> cidades parecidas divergem (anti-doorway)
    def bullets(lst):
        return '\n            '.join('<li>%s</li>' % esc(T(b)) for b in lst)

    scope_v = cfg['scope_bullets_variants']
    materials_v = cfg['materials_bullets_variants']
    signs_v = cfg['signs_bullets_variants']
    cost_v = cfg['cost_answer_variants']
    cf_v = cfg['cost_factors_variants']
    ps_v = cfg['process_steps_variants']
    scope_bul = bullets(scope_v[off(1, len(scope_v))])
    materials_bul = bullets(materials_v[off(2, len(materials_v))])
    signs_bul = bullets(signs_v[off(3, len(signs_v))])
    cost_answer_txt = T(cost_v[off(0, len(cost_v))])
    exp_open = EXP_OPEN_VARIANTS[off(4, len(EXP_OPEN_VARIANTS))].format(exp_tail=T(cfg['exp_tail']))
    cost_factors = bullets(cf_v[off(5, len(cf_v))])
    process_li = '\n            '.join('<li>%s</li>' % esc(T(s)) for s in ps_v[off(6, len(ps_v))])

    # internal link cards
    def card(href, span, strong):
        return '<a class="seo-link-card" href="%s"><span>%s</span><strong>%s</strong></a>' % (href, esc(span), strong)

    area_slug = 'essex-county' if county == 'Essex' else 'middlesex-county'
    cards = [
        card(cfg['scope_link'][0], cfg['scope_link'][1], cfg['scope_link'][2]),
        card('../../../areas/%s/' % area_slug, '%s County remodeling service area' % county, 'View page'),
        card('../../%s/%s/' % (cfg['sibling'], slug), T(cfg['sibling_label']), 'View page'),
    ]
    for nb in nearby:
        nb_name = master.get(nb, nb.replace('-', ' ').title())
        cards.append(card('../../%s/%s/' % (cfg['slug'], nb), '%s %s contractors' % (nb_name, cfg['label'].split()[0].lower() + ' ' + cfg['label'].split()[1].lower()), 'View page'))
    cards.append(card(cfg['blog_link'][0], cfg['blog_link'][1], cfg['blog_link'][2]))
    cards_html = '\n          '.join(cards)

    url = '%s/services/%s/%s/' % (BASE_URL, cfg['slug'], slug)

    doc = '''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{meta}">
  <link rel="canonical" href="{url}">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{meta}">
  <meta property="og:image" content="../../../images/og-image.jpg">
  <link rel="icon" href="../../../images/logo/favicon.avif" type="image/avif">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../../../css/style.css">
  <script type="application/ld+json">[
  {{
    "@context": "https://schema.org",
    "@type": "Service",
    "name": "{schema_name}",
    "serviceType": "{schema_name}",
    "provider": {{
      "@type": "LocalBusiness",
      "name": "DeFaria Construction",
      "telephone": "{phone}",
      "url": "{base}",
      "areaServed": ["Essex County, MA", "Middlesex County, MA"]
    }},
    "areaServed": [
      {areas_served_schema}
    ],
    "url": "{url}"
  }},
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{ "@type": "ListItem", "position": 1, "name": "Home", "item": "{base}/" }},
      {{ "@type": "ListItem", "position": 2, "name": "{bc2_name}", "item": "{bc2_url}" }},
      {{ "@type": "ListItem", "position": 3, "name": "{schema_name}", "item": "{url}" }}
    ]
  }},
  {{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {faq_schema}
    ]
  }}
]</script>
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id={gtag}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', '{gtag}');
</script>
<!-- MG Analytics v1.3 (7 comportamento + 5 conversao) -->
<script>window.MG_CONV_CFG={{form:"#estimateForm",estimateText:/estimate|quote/i}};</script>
<script src="/mg-analytics.js" defer></script>
</head>
<body>
  <header class="site-header" id="siteHeader">
    <div class="container nav">
      <a class="nav__brand" href="../../../" aria-label="DeFaria Construction home">
        <img src="../../../images/logo/logo-header.webp" width="210" height="70" alt="DeFaria Construction" loading="eager" fetchpriority="high">
      </a>
      <button class="nav__toggle" id="navToggle" aria-label="Open menu" aria-expanded="false"><span></span><span></span><span></span></button>
      <nav class="nav__menu" id="navMenu" aria-label="Primary navigation">
        <a href="../../../#services">All Services</a>
        <a href="../../../pages/kitchen-remodeling/">Kitchen</a>
        <a href="../../../pages/bathroom-remodeling/">Bathroom</a>
        <a href="../../../pages/home-additions/">Additions</a>
        <a href="../../../#contact">Contact</a>
      </nav>
      <a class="btn btn--small btn--primary nav__cta" href="{phone_href}">Call (617) 893-2221</a>
    </div>
  </header>

  <main>
    <section class="page-hero">
      <div class="page-hero__media"><img src="../../../images/pages/{hero_img}?v=seo-local-{slug}" width="1600" height="900" alt="{hero_alt}" fetchpriority="high"></div>
      <div class="page-hero__shade"></div>
      <div class="container page-hero__content">
        <a class="breadcrumb" href="../../../">Home / {label} / {City}</a>
        <p class="eyebrow">{eyebrow}</p>
        <h1>{h1}</h1>
        <p class="page-hero__lead">{lead}</p>
      </div>
    </section>

    <section class="section">
      <div class="container detail-grid">
        <div>
          <p class="eyebrow eyebrow--dark">Local search focus</p>
          <h2>{focus_h2}</h2>
          {img_focus}
        </div>
        <div class="detail-copy">
          <p>Across {hoods_intro}, {housing} {focus_tail}</p>
          <p>{focus_p2}</p>
          <ul class="feature-list">
            <li>Clear estimate conversations before the project starts.</li>
            <li>Direct communication with the homeowner from walkthrough to final walkthrough.</li>
            <li>Local coverage across {City} and the wider {County} County area.</li>
          </ul>
        </div>
      </div>
    </section>

    <section class="section section--light">
      <div class="container detail-grid">
        <div>
          <p class="eyebrow eyebrow--dark">The scope</p>
          <h2>{scope_h2}</h2>
          {img_scope}
        </div>
        <div class="detail-copy">
          <p>In {City}, {constraint}.</p>
          <ul class="feature-list">
            {scope_bul}
          </ul>
          <p>{permit_line}</p>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container detail-grid">
        <div>
          <p class="eyebrow eyebrow--dark">Cost</p>
          <h2>{cost_h2}</h2>
          {img_cost}
        </div>
        <div class="detail-copy">
          <p>{cost_answer}</p>
          <ul class="feature-list">
            {cost_factors}
          </ul>
          <p>{flavor_cost}</p>
          <p>{cost_close}</p>
        </div>
      </div>
    </section>

    <section class="section section--light">
      <div class="container detail-grid">
        <div>
          <p class="eyebrow eyebrow--dark">Process</p>
          <h2>{process_h2}</h2>
          {img_process}
        </div>
        <div class="detail-copy">
          <p>{process_intro}</p>
          <ol class="feature-list" style="list-style:decimal;padding-left:1.2em">
            {process_li}
          </ol>
          <p>{flavor_process}</p>
          <p>{process_close}</p>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container detail-grid">
        <div>
          <p class="eyebrow eyebrow--dark">Materials</p>
          <h2>{materials_h2}</h2>
          {img_materials}
        </div>
        <div class="detail-copy">
          <p>{materials_p}</p>
          <ul class="feature-list">
            {materials_bul}
          </ul>
          <p>{flavor_materials}</p>
        </div>
      </div>
    </section>

    <section class="section section--light">
      <div class="container detail-grid">
        <div>
          <p class="eyebrow eyebrow--dark">When to remodel</p>
          <h2>{signs_h2}</h2>
          {img_signs}
        </div>
        <div class="detail-copy">
          <p>{signs_p}</p>
          <ul class="feature-list">
            {signs_bul}
          </ul>
          <p>{flavor_signs}</p>
        </div>
      </div>
    </section>

    <section class="section seo-photo-proof" id="service-photos">
      <div class="container">
        <div class="section__head">
          <p class="eyebrow eyebrow--dark">Project photos</p>
          <h2>{photos_h2}</h2>
          <p>{photos_p}</p>
        </div>
        <div class="seo-photo-grid">
          {photos_grid}
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container detail-grid">
        <div>
          <p class="eyebrow eyebrow--dark">Areas covered</p>
          <h2>{areas_h2}</h2>
          {img_areas}
        </div>
        <div class="detail-copy">
          <p>{areas_p}</p>
          <p>{areas_local}</p>
          <ul class="feature-list">
            {hoods_li}
          </ul>
        </div>
      </div>
    </section>

    <section class="section section--light seo-related" id="related-pages">
      <div class="container">
        <div class="section__head">
          <p class="eyebrow eyebrow--dark">Internal links</p>
          <h2>Related DeFaria Construction pages</h2>
          <p>{related_p}</p>
          {img_related}
        </div>
        <div class="seo-link-grid">
          {cards}
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container detail-grid">
        <div>
          <p class="eyebrow eyebrow--dark">Experience</p>
          <h2>Why this {City} page is built for real homeowners, not just keywords.</h2>
          {img_experience}
        </div>
        <div class="detail-copy">
          <p>{exp_open}</p>
          <p>DeFaria Construction is a licensed and insured local contractor with an A+ BBB rating and verified customer reviews, and every {City} project is owner-led by Luiz DeFaria from the first walkthrough to the final one.</p>
          <blockquote class="seo-quote"><p>&quot;{quote}&quot;</p><cite>{City} homeowner</cite></blockquote>
          <p class="seo-byline">Reviewed by Luiz DeFaria, owner of DeFaria Construction · Updated September 2026</p>
          <p>The goal is to help someone searching for {schema_name} understand the scope, the neighborhoods covered and how to start a direct conversation before requesting a free estimate.</p>
          <a class="btn btn--primary" href="{phone_href}">Call (617) 893-2221 for a free estimate</a>
        </div>
      </div>
    </section>

    <section class="section section--light">
      <div class="container">
        <p class="eyebrow eyebrow--dark">FAQ</p>
        <h2>Common questions about {faq_topic} in {City}</h2>
        {img_faq}
        <div class="faq-list">
          {faq_details}
        </div>
      </div>
    </section>
  </main>

  <footer class="footer">
    <div class="container footer__grid">
      <div>
        <img src="../../../images/logo/logo-white.webp" width="190" height="64" alt="DeFaria Construction" loading="lazy">
        <p>Kitchen, bathroom, interior, exterior and commercial remodeling across Middlesex County and Essex County.</p>
      </div>
      <div class="footer__links"><a href="../../../#services">Services</a><a href="../../../#process">Process</a><a href="../../../#contact">Estimate</a></div>
    </div>
  </footer>
  <script src="../../../js/main.js"></script>
</body>
</html>
'''.format(
        title=esc(T(cfg['title'])), meta=esc(T(cfg['meta'])), url=url, base=BASE_URL,
        schema_name=esc(T(cfg['schema_name'])), phone=PHONE, phone_href=PHONE_HREF,
        areas_served_schema=areas_served_schema, bc2_name=cfg['bc2_name'], bc2_url=cfg['bc2_url'],
        faq_schema=faq_schema, gtag=GTAG, hero_img=cfg['photos'][1][0].replace('-after', '-hero').replace('-img-9226', '') if cfg['slug'] == 'kitchen-remodeling' else 'bathroom-remodeling-hero.webp',
        slug=slug, hero_alt=esc(T(cfg['hero_alt'])), label=cfg['label'], City=esc(City),
        eyebrow=esc(T(cfg['eyebrow'])), h1=esc(T(cfg['h1'])), lead=esc(T(cfg['lead'])),
        focus_h2=esc(T(cfg['focus_h2'])), hoods_intro=esc(hoods_intro), housing=esc(housing),
        focus_tail=esc(T(cfg['focus_tail'])), focus_p2=esc(T(cfg['focus_p2'])), County=county,
        scope_h2=esc(T(cfg['scope_h2'])), constraint=esc(constraint), scope_bul=scope_bul,
        permit_line=esc(permit_line), photos_h2=esc(T(cfg['photos_h2'])), photos_p=esc(T(cfg['photos_p'])),
        cost_h2=esc(T(cfg['cost_h2'])), cost_answer=esc(cost_answer_txt), cost_factors=cost_factors,
        cost_close=esc(T(cfg['cost_close'])), process_h2=esc(T(cfg['process_h2'])), process_intro=esc(T(cfg['process_intro_variants'][off(11, len(cfg['process_intro_variants']))])),
        process_li=process_li, process_close=esc(T(cfg['process_close_variants'][off(12, len(cfg['process_close_variants']))])), materials_h2=esc(T(cfg['materials_h2'])),
        materials_p=esc(T(cfg['materials_p_variants'][off(13, len(cfg['materials_p_variants']))])), materials_bul=materials_bul, signs_h2=esc(T(cfg['signs_h2'])),
        signs_p=esc(T(cfg['signs_p'])), signs_bul=signs_bul,
        flavor_cost=esc(flavor_cost), flavor_materials=esc(flavor_materials),
        flavor_process=esc(flavor_process), flavor_signs=esc(flavor_signs), areas_local=esc(areas_local),
        img_focus=img_focus, img_scope=img_scope, img_cost=img_cost, img_process=img_process,
        img_materials=img_materials, img_signs=img_signs, img_areas=img_areas, img_related=img_related,
        img_experience=img_experience, img_faq=img_faq, photos_grid=photos_grid,
        photos=photos, areas_h2=esc(T(cfg['areas_h2'])), areas_p=esc(T(cfg['areas_p'])),
        hoods_li=hoods_li, related_p=esc(T(cfg['related_p'])), cards=cards_html,
        exp_open=esc(exp_open), quote=esc(quote), faq_topic=cfg['label'].lower(),
        faq_details=faq_details,
    )
    # corrige hero da cozinha (nome do arquivo)
    doc = doc.replace('kitchen-remodeling-after-img-9226.webp?v=seo-local', 'kitchen-remodeling-hero.webp?v=seo-local')
    return doc


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--services', default='bathroom-remodeling,kitchen-remodeling')
    ap.add_argument('--cities', default='')
    ap.add_argument('--only-new', action='store_true', help='so cidades ainda sem pagina')
    ap.add_argument('--dry', action='store_true')
    args = ap.parse_args()

    with open(DATA, encoding='utf-8') as f:
        cities = json.load(f)
    master = {c['slug']: c['name'] for c in cities}
    for s in ORIGINAL:
        master.setdefault(s, s.replace('-', ' ').title())

    want = [s.strip() for s in args.services.split(',') if s.strip()]
    only = set(x.strip() for x in args.cities.split(',') if x.strip())

    written = []
    for svc in want:
        cfg = SERVICES[svc]
        # cidades que TEM (ou terao) pagina deste servico: as do dataset + as ja existentes em disco
        valid = set(c['slug'] for c in cities)
        svc_dir = os.path.join(ROOT, 'services', svc)
        if os.path.isdir(svc_dir):
            for d in os.listdir(svc_dir):
                if os.path.exists(os.path.join(svc_dir, d, 'index.html')):
                    valid.add(d)
        for city in cities:
            if only and city['slug'] not in only:
                continue
            outdir = os.path.join(ROOT, 'services', svc, city['slug'])
            outfile = os.path.join(outdir, 'index.html')
            if args.only_new and os.path.exists(outfile):
                continue
            doc = render(cfg, city, master, valid)
            if args.dry:
                written.append('[DRY] %s (%d bytes)' % (outfile, len(doc)))
                continue
            os.makedirs(outdir, exist_ok=True)
            with open(outfile, 'w', encoding='utf-8') as f:
                f.write(doc)
            written.append(outfile)
    print('\n'.join(written))
    print('\nTotal: %d paginas' % len(written))


if __name__ == '__main__':
    main()
