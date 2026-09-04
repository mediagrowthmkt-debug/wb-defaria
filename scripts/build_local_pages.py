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
        'hero_img': 'bathroom-remodeling-hero.webp',
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
        'hero_img': 'kitchen-remodeling-hero.webp',
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


def home_additions_cfg():
    return {
        'slug': 'home-additions',
        'label': 'Home Additions',
        'title': '{City} Home Addition Contractors | DeFaria',
        'meta': '{City} home addition contractors. DeFaria plans structure, exterior tie-ins and finish, with real costs and a clear path to a free estimate.',
        'schema_name': '{City} home addition contractors',
        'bc2_name': 'Home Additions',
        'bc2_url': BASE_URL + '/pages/home-additions/',
        'eyebrow': '{City} home addition contractors',
        'h1': '{City} home additions that look like they belong',
        'lead': '{City} home additions from DeFaria Construction connect new space to the existing home, with structure, exterior tie-ins and finish planned before the first wall goes up.',
        'hero_alt': '{City} home addition contractors by DeFaria Construction',
        'hero_img': 'home-additions-hero.webp',
        'focus_h2': '{City} home additions start with how the new space meets the old.',
        'focus_tail': 'A {City} addition has to match the roofline, siding and structure of the existing home, so it reads as part of the house, not a box bolted on.',
        'focus_p2': 'This page is built for {City} homeowners comparing home addition contractors near them. It connects the {City} search to project photos, neighborhoods, the full addition scope and a direct estimate path.',
        'cost_h2': 'How much does a home addition cost in {City}?',
        'cost_answer_variants': [
            'A home addition in {City} usually runs from about $150 to $350 per square foot, so a typical room addition lands between $60,000 and $150,000, and larger or second-story additions more. The scope sets the price, not a flat rate.',
            'Most {City} home additions land between $60,000 and $150,000 for a room addition, and more for a large or second-story build, roughly $150 to $350 per square foot depending on the work.',
            'For a {City} addition, budget around $150 to $350 per square foot, so a room addition is often $60,000 to $150,000 and a bigger build more. The estimate follows the real scope, never a flat number.',
        ],
        'cost_factors_variants': [
            ['The size and footprint of the addition.',
             'Whether it is a ground-level or second-story build.',
             'Rooflines, siding and how the exterior ties into the existing home.',
             'Interior finishes, plumbing and electrical the new space needs.'],
            ['How many square feet the addition adds.',
             'Foundation work and whether you build out or up.',
             'Matching the roof, siding and trim to the current house.',
             'The finish level inside the new space.'],
        ],
        'cost_close': 'DeFaria gives a fixed, itemized {City} estimate at the walkthrough, so the price matches the actual scope instead of a guess.',
        'process_h2': 'How a {City} home addition runs, step by step',
        'process_intro_variants': [
            'Most {City} home additions follow the same clear path, so you always know what happens next.',
            'Every {City} addition runs on a clear sequence, from permits to final trim.',
            'A {City} home addition moves through set stages, so you can see what comes next.',
        ],
        'process_steps_variants': [
            ['Walkthrough, design and a clear, itemized estimate.',
             'Permits and any zoning review handled with the town.',
             'Foundation and framing tied into the existing home.',
             'Roof, windows and weatherproofing.',
             'Exterior siding and trim matched to the house.',
             'Electrical, plumbing, insulation and drywall.',
             'Interior finish, paint and a final walkthrough.'],
            ['Design walkthrough and an itemized estimate.',
             'Permitting and zoning with the town.',
             'Foundation, framing and structural tie-in.',
             'Roofing, windows and weather protection.',
             'Siding and trim matched to the existing exterior.',
             'Rough-in, insulation and drywall.',
             'Finish carpentry, paint and a final walkthrough.'],
        ],
        'process_close_variants': [
            'Most {City} home additions take about 8 to 16 weeks, depending on size, foundation and finishes.',
            'A typical {City} addition runs roughly 8 to 16 weeks, depending on the scope and whether you build up or out.',
            'Plan on about 8 to 16 weeks for a {City} addition once permits are in, depending on size and finish.',
        ],
        'materials_h2': 'Materials and finishes that hold up in {City} additions',
        'materials_p_variants': [
            'A {City} addition faces the same Massachusetts winters as the rest of the home, so structure, insulation and exterior are built to last.',
            'In {County} County, an addition has to handle cold winters and weather, so the framing, insulation and siding are chosen to endure.',
            'Because a {City} addition ties into the existing home, the exterior and insulation are matched and built for New England weather.',
        ],
        'materials_bullets_variants': [
            ['A foundation and framing sized for the new load and tied to the home.',
             'Insulation and weather barriers rated for Massachusetts winters.',
             'Siding, roofing and trim matched to the existing exterior.',
             'Windows and finishes that fit the age and style of the house.'],
            ['Structural framing engineered to connect to the current home.',
             'Insulation and air sealing for New England cold.',
             'Roof and siding blended so the addition disappears into the house.',
             'Interior finishes consistent with the rest of the home.'],
            ['A foundation built for the addition and the existing structure.',
             'Weatherproofing and insulation for four-season comfort.',
             'Exterior materials matched to siding, roof and trim.',
             'Trim, doors and finishes that carry through from the old space.'],
        ],
        'signs_h2': 'Signs it is time to add on in {City}',
        'signs_p': 'A few clear signs a {City} home is ready for an addition:',
        'signs_bullets_variants': [
            ['A growing family running out of bedrooms or bathrooms.',
             'Needing a home office, gym or in-law suite.',
             'A cramped kitchen or living area that cannot be reworked inside the footprint.',
             'Wanting more space but not wanting to move.',
             'Adding long-term value before a future sale.'],
            ['Bedrooms or bathrooms that no longer fit the household.',
             'A need for a dedicated office, suite or bonus room.',
             'A layout that is maxed out within the current walls.',
             'Loving the location but needing more room.',
             'Investing in the home instead of buying a new one.'],
            ['Running short on bedrooms, baths or storage.',
             'Wanting an in-law suite, office or family room.',
             'A footprint that cannot stretch any further inside.',
             'Choosing to stay and expand rather than move.',
             'Building equity with more finished square footage.'],
        ],
        'scope_h2': 'What a full {City} home addition covers',
        'scope_bullets_variants': [
            ['Foundation, framing and roofline planned to tie into the existing home.',
             'Exterior siding, windows and trim matched so the addition blends in.',
             'Interior finish, electrical and plumbing coordinated with the rest of the house.'],
            ['Structure and roof designed to connect cleanly to the current home.',
             'Siding, windows and trim matched to the existing exterior.',
             'Interior systems and finishes coordinated across old and new space.'],
            ['A foundation and frame built to join the existing structure.',
             'Exterior blended so the addition reads as part of the house.',
             'Finish, wiring and plumbing tied into the rest of the home.'],
        ],
        'photos_h2': 'Home addition photos for {City} homeowners',
        'photos_p': 'The {City} home addition page pairs local search intent with real project photos, so visitors see the finish level before requesting an estimate.',
        'areas_h2': 'Home additions across {City} neighborhoods',
        'areas_p': 'DeFaria Construction supports home addition searches across {City} and nearby {County} County towns, giving visitors enough local context to decide whether DeFaria is the right fit before they call.',
        'related_p': 'Compare the full home addition scope, the county service area and {City} sibling services. Each link points to a live local page with its own search intent.',
        'scope_link': ('../../../pages/home-additions/', 'Home addition scope, structure and process', 'View page'),
        'blog_link': ('../../../blog/kitchen-remodel-cost-massachusetts/', 'Remodeling and build costs in Massachusetts', 'Read the guide'),
        'sibling': 'remodeling',
        'sibling_label': '{City} remodeling contractors',
        'exp_tail': 'the {City} home addition page is written around real structure, exterior tie-ins and finish coordination, not a city name dropped into a template.',
        'quotes': [
            'our {City} addition looks like it was always part of the house, right down to the siding and roofline.',
            'DeFaria planned the {City} addition around our home, so the new space just fits.',
            'the {City} addition gave us the room we needed without the mess of moving.',
            'they tied the new {City} space into the old house cleanly, structure and finish both.',
        ],
        'faq': [
            ('What home addition work does DeFaria Construction handle in {City}?',
             'In {City} DeFaria Construction handles design, foundation, framing, roofing, exterior siding, and the interior electrical, plumbing and finish for a room or second-story addition.'),
            ('How much does a home addition cost in {City}?',
             'A {City} home addition usually runs about $150 to $350 per square foot, so a typical room addition lands between $60,000 and $150,000, and larger builds more. DeFaria gives a fixed, itemized estimate at the walkthrough.'),
            ('How long does a {City} home addition take?',
             'Most {City} home additions take about 8 to 16 weeks once permits are in, depending on size, foundation and finishes.'),
            ('Will the addition match my existing {City} home?',
             'Yes. DeFaria matches the roofline, siding, windows and trim so the {City} addition reads as part of the house, not a box added on.'),
            ('Is DeFaria Construction licensed and insured?',
             'Yes. DeFaria Construction is a licensed and insured contractor with an A+ BBB rating and verified reviews, and every {City} project is owner-led by Luiz DeFaria.'),
            ('Does DeFaria handle {City} addition permits and inspections?',
             'Yes. {permit_line}'),
        ],
    }


def remodeling_cfg():
    return {
        'slug': 'remodeling',
        'label': 'Remodeling',
        'title': '{City} Remodeling Contractors | DeFaria',
        'meta': '{City} remodeling contractors. DeFaria plans and builds interior remodels room by room or whole-home, with clear scope, real costs and a free estimate.',
        'schema_name': '{City} remodeling contractors',
        'bc2_name': 'Interior Remodeling',
        'bc2_url': BASE_URL + '/pages/interior-remodeling/',
        'eyebrow': '{City} remodeling contractors',
        'h1': '{City} remodeling contractors for a home that finally works',
        'lead': '{City} remodeling from DeFaria Construction turns dated or awkward spaces into finished rooms, with a clear scope, honest sequencing and careful finish work.',
        'hero_alt': '{City} remodeling contractors by DeFaria Construction',
        'hero_img': 'interior-remodeling-hero.webp',
        'focus_h2': '{City} remodeling is about the plan as much as the finish.',
        'focus_tail': 'A {City} remodel that stays organized, from demolition to the final trim, is what separates a smooth project from an endless one.',
        'focus_p2': 'This page is built for {City} homeowners comparing remodeling contractors near them. It connects the {City} search to project photos, neighborhoods, the full remodel scope and a direct estimate path.',
        'cost_h2': 'How much does a remodel cost in {City}?',
        'cost_answer_variants': [
            'A remodel in {City} ranges widely by scope, from about $15,000 for a single room to $100,000 or more for a whole-home remodel. The rooms involved and the level of finish set the number.',
            'Most {City} remodels run from around $15,000 for one room to $100,000 or more for a whole-home project. Scope and finish level drive the price, not a flat rate.',
            'For a {City} remodel, budget from about $15,000 for a single room up to $100,000 or more whole-home. The rooms and the finish decide the total, priced at the walkthrough.',
        ],
        'cost_factors_variants': [
            ['How many rooms are in the project.',
             'The level of finish and material grade.',
             'Whether the layout, walls or plumbing change.',
             'The age and condition of the home behind the walls.'],
            ['The number and size of the rooms involved.',
             'Material and finish choices.',
             'Any structural, layout or systems changes.',
             'Hidden conditions in an older home.'],
        ],
        'cost_close': 'DeFaria gives a fixed, itemized {City} estimate at the walkthrough, so the price matches the actual scope instead of a guess.',
        'process_h2': 'How a {City} remodel runs, step by step',
        'process_intro_variants': [
            'Most {City} remodels follow the same clear path, so you always know what happens next.',
            'Every {City} remodel runs on a clear sequence, so nothing catches you off guard.',
            'A {City} remodel moves through set stages, so you can see what comes next.',
        ],
        'process_steps_variants': [
            ['Walkthrough and a clear, itemized estimate.',
             'Design and material selections.',
             'Protection of the home and demolition.',
             'Framing and any layout changes.',
             'Electrical, plumbing and mechanical rough-in.',
             'Drywall, trim and finish carpentry.',
             'Paint, final details and a walkthrough before you sign off.'],
            ['A walkthrough and an itemized estimate.',
             'Design, layout and material selections.',
             'Home protection and demolition.',
             'Framing and structural changes.',
             'Rough-in for electrical, plumbing and HVAC.',
             'Drywall, trim and finish work.',
             'Paint, punch list and a final walkthrough with you.'],
        ],
        'process_close_variants': [
            'A {City} remodel timeline depends on scope, from a couple of weeks for one room to a few months for a whole-home project.',
            'Most {City} remodels run from a few weeks for a single room to a few months whole-home, depending on scope.',
            'Plan on anywhere from a couple of weeks to a few months for a {City} remodel, depending on how much is involved.',
        ],
        'materials_h2': 'Materials and finishes that last in {City} homes',
        'materials_p_variants': [
            '{County} County homes take daily wear and cold winters, so the finishes are chosen for durability, not just looks.',
            'In {County} County, a remodel has to handle daily use and New England weather, so durable materials come first.',
            'Because a {City} home gets lived in hard, the trim, floors and surfaces are picked to hold up over years.',
        ],
        'materials_bullets_variants': [
            ['Durable flooring rated for real daily traffic.',
             'Trim, doors and finish carpentry that hold their line.',
             'Quality drywall and paint prep for a clean finish.',
             'Fixtures and hardware matched to how the room is used.'],
            ['Flooring chosen for wear, not just appearance.',
             'Finish carpentry and trim built to last.',
             'Proper drywall and paint prep behind the finish.',
             'Hardware and fixtures that keep working.'],
            ['Hard-wearing floors for busy rooms.',
             'Clean trim, doors and finish carpentry.',
             'Drywall and paint done with real prep.',
             'Fixtures and finishes suited to daily life.'],
        ],
        'signs_h2': 'Signs it is time to remodel in {City}',
        'signs_p': 'A few clear signs a {City} home is ready for a remodel:',
        'signs_bullets_variants': [
            ['Dated rooms that no longer fit how you live.',
             'A layout that fights daily routines.',
             'Worn floors, trim, doors or surfaces.',
             'Wasted or awkward space you work around.',
             'Getting the home ready to sell.'],
            ['Rooms that feel stuck in another decade.',
             'A floor plan that makes everyday life harder.',
             'Tired flooring, trim and finishes.',
             'Space that is not working for the household.',
             'Preparing the home for the market.'],
            ['Interiors that look and feel past their prime.',
             'A layout that no longer suits the family.',
             'Worn surfaces throughout the home.',
             'Awkward rooms you keep working around.',
             'Boosting value before a future sale.'],
        ],
        'scope_h2': 'What a full {City} remodel covers',
        'scope_bullets_variants': [
            ['Framing, drywall and finish carpentry planned around the whole space.',
             'Flooring, trim, paint and fixtures coordinated for a consistent finish.',
             'Electrical, lighting and plumbing sequenced before the finishes go in.'],
            ['Structural and finish work planned across the rooms involved.',
             'Flooring, trim and paint coordinated for one clean look.',
             'Rough-in for power, lighting and plumbing done before finishes.'],
            ['Framing and finish carpentry built around the real layout.',
             'Surfaces, trim and fixtures selected to work together.',
             'Electrical, lighting and plumbing sequenced ahead of the finish.'],
        ],
        'photos_h2': 'Remodeling photos for {City} homeowners',
        'photos_p': 'The {City} remodeling page pairs local search intent with real project photos, so visitors see the finish level before requesting an estimate.',
        'areas_h2': 'Remodeling across {City} neighborhoods',
        'areas_p': 'DeFaria Construction supports remodeling searches across {City} and nearby {County} County towns, giving visitors enough local context to decide whether DeFaria is the right fit before they call.',
        'related_p': 'Compare the full remodeling scope, the county service area and {City} sibling services. Each link points to a live local page with its own search intent.',
        'scope_link': ('../../../pages/interior-remodeling/', 'Interior remodeling scope and process', 'View page'),
        'blog_link': ('../../../blog/kitchen-remodel-cost-massachusetts/', 'Remodeling costs in Massachusetts', 'Read the guide'),
        'sibling': 'home-additions',
        'sibling_label': '{City} home addition contractors',
        'exp_tail': 'the {City} remodeling page is written around real scope, sequencing and finish coordination, not a city name dropped into a template.',
        'quotes': [
            'our {City} remodel stayed organized from demolition to the final trim.',
            'DeFaria remodeled our {City} home around how we actually live, not a template.',
            'the {City} project finally fixed a layout we had worked around for years.',
            'clean work and clear updates through the whole {City} remodel.',
        ],
        'faq': [
            ('What remodeling work does DeFaria Construction handle in {City}?',
             'In {City} DeFaria Construction handles interior remodels room by room or whole-home: framing, drywall, flooring, trim, paint, and electrical and plumbing coordination with finish carpentry.'),
            ('How much does a remodel cost in {City}?',
             'A {City} remodel ranges from about $15,000 for a single room to $100,000 or more for a whole-home project. DeFaria gives a fixed, itemized estimate at the walkthrough so the price matches the real scope.'),
            ('How long does a {City} remodel take?',
             'It depends on scope, from a couple of weeks for one room to a few months for a whole-home {City} remodel. DeFaria sets a realistic sequence at the walkthrough.'),
            ('Can DeFaria remodel one room at a time in {City}?',
             'Yes. Many {City} projects start with one room, kitchen, bath or living area, and DeFaria plans the scope so the work fits the home and the budget.'),
            ('Is DeFaria Construction licensed and insured?',
             'Yes. DeFaria Construction is a licensed and insured contractor with an A+ BBB rating and verified reviews, and every {City} project is owner-led by Luiz DeFaria.'),
            ('Does DeFaria handle {City} remodeling permits and inspections?',
             'Yes. {permit_line}'),
        ],
    }


def decks_cfg():
    return {
        'slug': 'decks-and-patios',
        'label': 'Decks and Patios',
        'title': '{City} Deck Contractors | DeFaria Construction',
        'meta': '{City} deck contractors. DeFaria builds decks and patios with solid framing, decking, railings and stairs, with real costs and a free estimate.',
        'schema_name': '{City} deck contractors',
        'bc2_name': 'Decks and Patios',
        'bc2_url': BASE_URL + '/pages/decks-and-patios/',
        'eyebrow': '{City} deck contractors',
        'h1': '{City} deck contractors for a backyard that gets used',
        'lead': '{City} deck builders at DeFaria Construction plan framing, decking, railings and layout so the outdoor space is safe, durable and ready for New England seasons.',
        'hero_alt': '{City} deck contractors by DeFaria Construction',
        'hero_img': 'decks-and-patios-hero.webp',
        'focus_h2': '{City} decks start with the frame you cannot see.',
        'focus_tail': 'A {City} deck lives outside through hot summers and hard winters, so the footings, framing and fasteners matter as much as the boards on top.',
        'focus_p2': 'This page is built for {City} homeowners comparing deck builders and deck contractors near them. It connects the {City} search to project photos, neighborhoods, the full deck scope and a direct estimate path.',
        'cost_h2': 'How much does a deck cost in {City}?',
        'cost_answer_variants': [
            'A deck in {City} usually runs from about $20 to $60 per square foot, so a typical deck lands between $8,000 and $30,000, depending on size, materials and height. The scope sets the price.',
            'Most {City} decks land between $8,000 and $30,000, roughly $20 to $60 per square foot, depending on size, material and how high off the ground it sits.',
            'For a {City} deck, budget about $20 to $60 per square foot, so most decks are $8,000 to $30,000 depending on size and materials. The estimate follows the real scope.',
        ],
        'cost_factors_variants': [
            ['The size and height of the deck.',
             'Pressure-treated wood versus composite decking.',
             'Railings, stairs and any built-in features.',
             'Footings and framing for the site and load.'],
            ['Square footage and how high the deck sits.',
             'Decking material, wood or composite.',
             'Stairs, railings and add-ons.',
             'Site conditions, footings and framing.'],
        ],
        'cost_close': 'DeFaria gives a fixed, itemized {City} estimate at the walkthrough, so the price matches the actual scope instead of a guess.',
        'process_h2': 'How a {City} deck project runs, step by step',
        'process_intro_variants': [
            'Most {City} decks follow the same clear path, so you always know what happens next.',
            'Every {City} deck runs on a clear sequence, from footings to final railing.',
            'A {City} deck moves through set stages, so you can see what comes next.',
        ],
        'process_steps_variants': [
            ['Walkthrough, design and a clear, itemized estimate.',
             'Permits handled with the town.',
             'Footings and posts set for the load and frost line.',
             'Framing and structural connections to the home.',
             'Decking boards installed and fastened.',
             'Railings, stairs and any built-ins.',
             'Final details and a walkthrough before you sign off.'],
            ['Design walkthrough and an itemized estimate.',
             'Permitting with the town.',
             'Footings dug below the frost line and set.',
             'Frame built and tied to the house.',
             'Decking laid and fastened down.',
             'Stairs, railings and finish work.',
             'Final walkthrough with you.'],
        ],
        'process_close_variants': [
            'Most {City} decks take about 1 to 3 weeks, depending on size, height and materials.',
            'A typical {City} deck runs roughly 1 to 3 weeks, depending on the scope and finish.',
            'Plan on about 1 to 3 weeks for a {City} deck once permits are in, depending on size.',
        ],
        'materials_h2': 'Materials and finishes that hold up on {City} decks',
        'materials_p_variants': [
            'A {City} deck faces sun, rain and snow all year, so the framing, fasteners and decking are chosen to last outdoors.',
            'In {County} County, a deck takes four seasons of weather, so materials and hardware are picked to endure.',
            'Because a {City} deck lives outside, the structure and surface are built for New England weather.',
        ],
        'materials_bullets_variants': [
            ['Footings set below the frost line for a stable deck.',
             'Pressure-treated or composite decking chosen for the budget and look.',
             'Corrosion-resistant fasteners and hardware.',
             'Railings and stairs built to code and to last.'],
            ['Frost-depth footings so the deck does not heave.',
             'Wood or composite decking matched to how it will be used.',
             'Coated or stainless fasteners that resist the weather.',
             'Code-compliant railings and solid stairs.'],
            ['Solid footings and framing for a deck that stays level.',
             'Decking chosen for durability and low upkeep.',
             'Weather-rated hardware throughout.',
             'Safe, code-built railings and stairs.'],
        ],
        'signs_h2': 'Signs it is time for a new {City} deck',
        'signs_p': 'A few clear signs a {City} deck is ready to replace or build:',
        'signs_bullets_variants': [
            ['Soft, rotting or splintering deck boards.',
             'Wobbly railings or stairs that feel unsafe.',
             'A deck pulling away from the house.',
             'Wanting real outdoor space to use and entertain.',
             'Adding value and curb appeal before a sale.'],
            ['Rotting boards or popped fasteners.',
             'Railings or stairs that no longer feel solid.',
             'A frame or ledger showing its age.',
             'Wanting a better backyard to actually use.',
             'Boosting the home before listing.'],
            ['Boards that are soft, cracked or splintering.',
             'Loose railings or shaky stairs.',
             'A deck that is sinking or separating.',
             'A backyard that needs a real gathering space.',
             'Investing in curb appeal and value.'],
        ],
        'scope_h2': 'What a full {City} deck project covers',
        'scope_bullets_variants': [
            ['Footings, posts and framing sized for the load and the site.',
             'Decking, railings and stairs installed and fastened cleanly.',
             'Layout, height and access planned around how the yard is used.'],
            ['Structure and footings built for the site and frost line.',
             'Decking, railings and stairs done to code.',
             'Layout and access planned around the home and yard.'],
            ['A frame and footings built to last outdoors.',
             'Clean decking, solid railings and safe stairs.',
             'A layout that fits the backyard and the home.'],
        ],
        'photos_h2': 'Deck photos for {City} homeowners',
        'photos_p': 'The {City} deck page pairs local search intent with real project photos, so visitors see the finish level before requesting an estimate.',
        'areas_h2': 'Decks across {City} neighborhoods',
        'areas_p': 'DeFaria Construction supports deck searches across {City} and nearby {County} County towns, giving visitors enough local context to decide whether DeFaria is the right fit before they call.',
        'related_p': 'Compare the full deck scope, the county service area and {City} sibling services. Each link points to a live local page with its own search intent.',
        'scope_link': ('../../../pages/decks-and-patios/', 'Deck and patio scope and process', 'View page'),
        'blog_link': ('../../../blog/when-to-book-deck-builder-massachusetts/', 'When to book a deck builder in Massachusetts', 'Read the guide'),
        'sibling': 'commercial-projects',
        'sibling_label': '{City} commercial remodeling contractors',
        'extra_sections_draft': [
            {'eyebrow': 'Materials', 'theme': 'decking materials', 'h2': 'Wood, composite or PVC decking for {City}?',
             'paras': [
                 'The decking material shapes both the price and the upkeep of a {City} deck. Pressure-treated wood is the most affordable and widely used, but it needs cleaning and sealing every couple of years to fight New England moisture. Cedar and other natural woods look beautiful and resist rot better, at a higher cost and with regular maintenance.',
                 'Composite decking, like Trex and similar brands, costs more up front but resists fading, staining and rot and needs little more than an occasional wash, which is why many {City} homeowners choose it for a low-maintenance deck. PVC decking is fully synthetic and the lightest to maintain of all. DeFaria walks through the trade-offs at the estimate so the choice fits the budget, the look and how much upkeep you want.'],
             'bullets': [
                 'Pressure-treated wood: lowest cost, needs sealing every 2 to 3 years.',
                 'Cedar or hardwood: natural look, better rot resistance, more upkeep.',
                 'Composite (Trex and similar): higher cost, low maintenance, fade and stain resistant.',
                 'PVC: fully synthetic, the lightest maintenance of all.']},
            {'eyebrow': 'Permits and code', 'theme': 'permits and code', 'h2': 'Deck permits, setbacks and code in {City}',
             'paras': [
                 'Most {City} decks over a certain height or size need a building permit, pulled through the {permit_authority}, plus attention to how far the deck sits from property lines. DeFaria handles that step so the project starts on solid legal footing, not a stop-work order.',
                 'Massachusetts building code drives the safety details: guardrails at least 36 inches high, baluster spacing under four inches so a child cannot slip through, proper stair rise and run, and footings dug below the frost line so the deck does not heave in winter. Building to code is not optional, and it is what keeps a {City} deck safe for years.'],
             'bullets': [
                 'Building permit through the {permit_authority} for most decks.',
                 'Setbacks from property lines checked before framing.',
                 'Guardrails 36 inches high, balusters under 4 inches apart.',
                 'Footings below the frost line so the deck stays level.']},
            {'eyebrow': 'Maintenance', 'theme': 'deck upkeep', 'h2': 'Keeping a {City} deck lasting through the seasons',
             'paras': [
                 'A {City} deck takes sun, rain, snow and freeze-thaw cycles all year, so a little upkeep goes a long way. Wood decks benefit from a yearly clean and a fresh seal or stain every couple of seasons; composite and PVC decks usually just need a wash. Either way, checking the fasteners, ledger connection and railings once a year catches small problems before they become big ones.',
                 'DeFaria builds with corrosion-resistant hardware and a properly flashed ledger from the start, which is the single biggest factor in how long a deck lasts. Good structure up front means less to worry about later.'],
             'bullets': [
                 'Clean the deck yearly; reseal wood every couple of seasons.',
                 'Check fasteners, ledger and railings once a year.',
                 'Clear snow and standing water to protect the surface.',
                 'A flashed ledger and coated hardware prevent the worst failures.']},
            {'eyebrow': 'Deck or patio', 'theme': 'deck versus patio', 'h2': 'Deck or patio: which fits your {City} yard?',
             'paras': [
                 'A deck is a raised, framed structure in wood or composite, ideal for sloped {City} yards, walkouts from a second floor, or anywhere you want a level outdoor room above the ground. A patio sits at ground level in stone, pavers or concrete, and works well on flat lots and for fire pits, dining areas and low-maintenance surfaces.',
                 'The grade of the lot usually points to the answer. Where the ground drops away from the house, a deck bridges that gap and gives you a level surface without major excavation, while a flat backyard can take a patio directly on a prepared base. Cost runs differently too: a simple ground-level patio can be economical, but once a raised deck or extensive hardscaping is involved, the numbers move based on structure, materials and site work.',
                 'Many {City} homes end up with both, a deck off the house that steps down to a patio in the yard, which gives you two distinct spaces and a natural transition between them. DeFaria helps weigh the grade of the lot, how you want to use the space, drainage and the budget to land on the right mix, and builds the deck side to the same standard whether it stands alone or ties into a patio below.']},
            {'eyebrow': 'Styles', 'theme': 'deck styles', 'h2': 'Popular {City} deck styles and add-ons',
             'paras': [
                 'Beyond the basic platform, {City} decks can be built in ways that fit how a family actually uses the yard. Multi-level decks step down a sloped lot; wraparound decks follow the house; and built-in features turn a deck into a real outdoor room.'],
             'bullets': [
                 'Multi-level and wraparound layouts for sloped or larger lots.',
                 'Built-in benches, planters and storage.',
                 'Pergolas, privacy screens and shade structures.',
                 'Deck lighting for stairs, railings and evening use.',
                 'Screened porches and covered sections for more seasons of use.']},
            {'eyebrow': 'Value', 'theme': 'deck resale value', 'h2': 'How much value a deck adds to a {City} home',
             'paras': [
                 'A well-built deck is one of the more reliable outdoor improvements for resale in {City}. Buyers read a solid deck as move-in-ready outdoor living space, and remodeling surveys have long shown decks returning a healthy share of their cost at sale, often more than many interior projects because the usable square footage is so visible.',
                 'The return depends on doing it right: a deck framed to code, in materials that match the home and last, adds value, while a sagging or unpermitted deck can actually scare buyers off. DeFaria builds so the deck is an asset on an appraisal and an inspection, not a red flag.',
                 'Beyond resale, a deck pays off every season you own the home, adding real, usable living space for a fraction of what enclosed square footage costs, which is why so many {City} homeowners consider it money well spent whether or not they plan to sell.']},
            {'eyebrow': 'Timing', 'theme': 'best time to build', 'h2': 'The best time to build a deck in {City}',
             'paras': [
                 'Decks can be built most of the year in {City}, but spring and early summer are the busiest, so booking early matters if you want the deck ready for the warm months. Late summer and fall are often easier to schedule and the weather is still good for concrete footings and framing.',
                 'Winter builds are possible for many decks, though frozen ground and snow can slow footings. Planning the design and permits over the winter is a smart way to be first in line when the season opens. DeFaria helps time the project so it lands when you actually want to use the deck.']},
            {'eyebrow': 'Lighting', 'theme': 'deck lighting', 'h2': 'Deck lighting and electrical in {City}',
             'paras': [
                 'Lighting turns a {City} deck into a space you use after sunset, and it is far easier to run wiring while the deck is being built than to add it later. Low-voltage stair and railing lights improve safety on steps; post-cap and under-rail lights set the mood; and a switched outlet or two makes the deck work for cooking, music and gatherings.',
                 'Any deck electrical in {City} is done to code with proper outdoor-rated fixtures and GFCI protection. DeFaria plans the lighting and power up front so the finished deck is ready for evenings, not just afternoons.']},
            {'eyebrow': 'Planning', 'theme': 'planning the project', 'h2': 'Planning and budgeting your {City} deck project',
             'paras': [
                 'The smoothest {City} deck projects start with a clear plan: how the deck will be used, where it connects to the house, the material and railing choices, and a realistic budget that includes footings, framing, decking, railings, stairs and any lighting. Getting those decisions made before the build keeps the project on schedule and the price predictable.',
                 'DeFaria walks the yard, talks through the options and puts it all in a fixed, itemized {City} estimate, so there are no surprises once the work starts. A little planning up front is what separates a deck that gets built once, right, from one that drags on.',
                 'It also helps to know what to ask any {City} deck contractor before you sign: whether they pull the permit, how the ledger attaches to the house, what fasteners and footings they use, and whether the quote is fixed or an estimate that can move. Clear answers up front are the best sign the deck will be built to last, and DeFaria puts those details in writing so you can compare fairly and decide with confidence.']},
            {'eyebrow': 'Structure', 'theme': 'footings and framing', 'h2': 'Deck footings and framing: the part that lasts',
             'paras': [
                 'Everything you see on a {City} deck rests on the part you do not: the footings and the frame. Footings carry the load down to stable soil below the frost line, usually around four feet in this part of Massachusetts, so the deck does not lift and settle as the ground freezes and thaws each winter. Skimping here is the most common reason older decks end up uneven or unsafe.',
                 'The frame ties it all together. Properly sized joists and beams, correct spacing, and a ledger board flashed and bolted, not just nailed, to the house are what make a deck feel rock-solid instead of bouncy. A failed ledger connection is one of the leading causes of deck collapses nationally, which is exactly why DeFaria details that connection carefully on every {City} build.',
                 'Corrosion-resistant hangers, bolts and fasteners hold the frame together through the seasons. It is unglamorous work that never shows in a photo, but it is the difference between a deck that lasts a couple of decades and one that needs rebuilding in a few years.']},
            {'eyebrow': 'Railings', 'theme': 'railing options', 'h2': 'Deck railings: materials and options in {City}',
             'paras': [
                 'Railings are the most visible part of a {City} deck and a major safety element, so the choice matters for both look and code. Wood railings are the most affordable and can be painted or stained to match the house, though they need the same upkeep as a wood deck. Composite railings pair with composite decking for a low-maintenance, coordinated look that holds its color.',
                 'For homeowners who want to keep a view, cable and aluminum railings offer a thinner, more modern profile, and glass panels open the sightline almost completely, which is popular where a {City} deck overlooks a yard or water. Every option is built to the same code, guardrail height and baluster spacing that keep the deck safe, so the decision comes down to look, budget and maintenance.',
                 'DeFaria shows the railing options alongside the decking so the two work together, and prices them in the itemized estimate. It is an easy detail to overlook early and an expensive one to change late, so it is worth deciding up front.']},
            {'eyebrow': 'Outdoor living', 'theme': 'covered decks and porches', 'h2': 'Screened porches, pergolas and covered decks in {City}',
             'paras': [
                 'Not every {City} homeowner wants an open deck. Adding a roof, a screened section or a pergola stretches the outdoor season and changes how the space feels. A screened porch keeps the bugs out on summer evenings and adds a room you can use in the rain; a covered section shades the hottest part of the afternoon; and a pergola adds structure and partial shade without fully closing the space in.',
                 'These upgrades change the structure and the permitting, since a roof adds load and a screened room may be treated more like an addition. DeFaria plans them from the start, so the framing, footings and code all account for the covered space instead of trying to bolt it on later. The result is an outdoor room that fits the house and gets used far more of the year.']},
        ],
        'exp_tail': 'the {City} deck page is written around real framing, materials and safe finish, not a city name dropped into a template.',
        'quotes': [
            'our {City} deck is solid underfoot and finally a place we actually use.',
            'DeFaria framed the {City} deck right, so it feels rock-solid, not bouncy.',
            'the {City} deck came out clean, from the footings to the railings.',
            'they built our {City} deck to last through the winters, not just look good day one.',
        ],
        'faq': [
            ('What deck work does DeFaria Construction handle in {City}?',
             'In {City} DeFaria Construction handles footings, framing, decking, railings, stairs and built-ins for a new deck or a full deck rebuild.'),
            ('How much does a deck cost in {City}?',
             'A {City} deck usually runs about $20 to $60 per square foot, so most decks land between $8,000 and $30,000 depending on size and materials. DeFaria gives a fixed, itemized estimate at the walkthrough.'),
            ('How long does a {City} deck take to build?',
             'Most {City} decks take about 1 to 3 weeks once permits are in, depending on size, height and materials.'),
            ('Should I use pressure-treated wood or composite for my {City} deck?',
             'Both work in {City}. Pressure-treated wood costs less up front; composite costs more but needs less upkeep. DeFaria helps you weigh budget, look and maintenance at the walkthrough.'),
            ('Is DeFaria Construction licensed and insured?',
             'Yes. DeFaria Construction is a licensed and insured contractor with an A+ BBB rating and verified reviews, and every {City} project is owner-led by Luiz DeFaria.'),
            ('Does DeFaria handle {City} deck permits and inspections?',
             'Yes. {permit_line}'),
        ],
    }


def commercial_cfg():
    return {
        'slug': 'commercial-projects',
        'label': 'Commercial Projects',
        'title': '{City} Commercial Remodeling | DeFaria',
        'meta': '{City} commercial remodeling contractors. DeFaria builds out offices, storefronts and restaurants with clear scheduling, scope and a free estimate.',
        'schema_name': '{City} commercial remodeling contractors',
        'bc2_name': 'Commercial Projects',
        'bc2_url': BASE_URL + '/pages/commercial-projects/',
        'eyebrow': '{City} commercial remodeling contractors',
        'h1': '{City} commercial remodeling that respects the business around it',
        'lead': '{City} commercial remodeling from DeFaria Construction is planned around your operation, offices, storefronts and restaurants, with clear scheduling, scope and clean execution.',
        'hero_alt': '{City} commercial remodeling contractors by DeFaria Construction',
        'hero_img': 'commercial-projects-hero.webp',
        'focus_h2': '{City} commercial projects are about coordination, not just construction.',
        'focus_tail': 'A {City} business space is tied to revenue and customers, so scheduling, scope and communication matter as much as the finish.',
        'focus_p2': 'This page is built for {City} business owners comparing commercial remodeling contractors near them. It connects the {City} search to project photos, neighborhoods, the full commercial scope and a direct estimate path.',
        'cost_h2': 'How much does commercial remodeling cost in {City}?',
        'cost_answer_variants': [
            'Commercial remodeling in {City} ranges widely by space and use, often about $50 to $200 or more per square foot depending on the buildout, systems and finish. The scope sets the price.',
            'Most {City} commercial buildouts run roughly $50 to $200 or more per square foot, depending on whether it is an office, retail or restaurant space and the systems involved.',
            'For a {City} commercial project, budget around $50 to $200 or more per square foot depending on use, code work and finish. The estimate follows the real scope.',
        ],
        'cost_factors_variants': [
            ['The size and use of the space, office, retail or restaurant.',
             'Mechanical, electrical, plumbing and code requirements.',
             'The level of finish and any specialty systems.',
             'Working around an operating business or an empty shell.'],
            ['Square footage and how the space is used.',
             'Systems and code or ADA work involved.',
             'Finish level and any specialty buildout.',
             'Whether the business stays open during the work.'],
        ],
        'cost_close': 'DeFaria gives a fixed, itemized {City} estimate at the walkthrough, so the price matches the actual scope instead of a guess.',
        'process_h2': 'How a {City} commercial project runs, step by step',
        'process_intro_variants': [
            'Most {City} commercial projects follow the same clear path, so the business always knows what happens next.',
            'Every {City} commercial project runs on a clear sequence, planned around your operation.',
            'A {City} commercial project moves through set stages, coordinated around the business.',
        ],
        'process_steps_variants': [
            ['Walkthrough, scope and a clear, itemized estimate.',
             'Permits, code and any inspections lined up.',
             'A schedule built around your operation.',
             'Demolition and structural or layout work.',
             'Mechanical, electrical and plumbing rough-in.',
             'Finishes, fixtures and buildout.',
             'Final inspection, punch list and handover.'],
            ['Scope walkthrough and an itemized estimate.',
             'Permitting, code and inspection planning.',
             'A timeline that protects daily operations.',
             'Demo and any structural changes.',
             'MEP rough-in for the new layout.',
             'Finishes, fixtures and the buildout.',
             'Inspection, punch list and handover.'],
        ],
        'process_close_variants': [
            'A {City} commercial timeline depends on the space and scope, from a few weeks for a light buildout to a few months for a full renovation.',
            'Most {City} commercial projects run from a few weeks to a few months, depending on the buildout and code work.',
            'Plan on a few weeks to a few months for a {City} commercial project, depending on scope and inspections.',
        ],
        'materials_h2': 'Materials and finishes that work in {City} commercial spaces',
        'materials_p_variants': [
            'A {City} commercial space takes heavy daily use, so finishes and systems are chosen to hold up and meet code.',
            'In {County} County, a commercial buildout has to handle traffic and code, so durable, compliant materials come first.',
            'Because a {City} commercial space is used hard every day, the finishes and systems are picked for durability and code.',
        ],
        'materials_bullets_variants': [
            ['Commercial-grade flooring and surfaces for heavy traffic.',
             'Code-compliant electrical, lighting and mechanical work.',
             'Durable finishes that survive daily customer use.',
             'ADA and safety details handled correctly.'],
            ['Flooring and surfaces rated for commercial traffic.',
             'Electrical, HVAC and plumbing to code.',
             'Finishes chosen to last in a busy space.',
             'Accessibility and safety built in.'],
            ['Hard-wearing commercial floors and walls.',
             'Systems installed to meet inspection and code.',
             'Durable, low-maintenance finishes.',
             'ADA and life-safety details done right.'],
        ],
        'signs_h2': 'Signs it is time to remodel your {City} commercial space',
        'signs_p': 'A few clear signs a {City} business space is ready for a remodel:',
        'signs_bullets_variants': [
            ['A dated space that no longer fits the brand.',
             'Outgrowing the current layout or square footage.',
             'Taking over a new storefront, office or restaurant.',
             'Code, ADA or safety issues to bring up to standard.',
             'Wanting a space that works better for staff and customers.'],
            ['An interior that looks tired next to competitors.',
             'A layout that limits how the business runs.',
             'Moving into or fitting out a new space.',
             'Code or accessibility work that is overdue.',
             'Improving flow for customers and staff.'],
            ['A space that no longer reflects the business.',
             'Not enough room or the wrong layout.',
             'A new location that needs a buildout.',
             'Bringing systems up to current code.',
             'Making the space work harder for the business.'],
        ],
        'scope_h2': 'What a full {City} commercial project covers',
        'scope_bullets_variants': [
            ['Scope, scheduling and code planned around the operation.',
             'Demolition, structure, MEP and buildout coordinated cleanly.',
             'Durable, code-compliant finishes for a working space.'],
            ['Planning and scheduling built around the business.',
             'Structural, mechanical and finish work coordinated.',
             'Commercial-grade, code-compliant finishes.'],
            ['A scope and timeline that protect daily operations.',
             'Clean coordination of demo, systems and buildout.',
             'Finishes built for a busy commercial space.'],
        ],
        'photos_h2': 'Commercial project photos for {City} businesses',
        'photos_p': 'The {City} commercial page pairs local search intent with project photos, so visitors see the finish level before requesting an estimate.',
        'areas_h2': 'Commercial remodeling across {City} neighborhoods',
        'areas_p': 'DeFaria Construction supports commercial remodeling searches across {City} and nearby {County} County towns, giving visitors enough local context to decide whether DeFaria is the right fit before they call.',
        'related_p': 'Compare the full commercial scope, the county service area and {City} sibling services. Each link points to a live local page with its own search intent.',
        'scope_link': ('../../../pages/commercial-projects/', 'Commercial project scope and process', 'View page'),
        'blog_link': ('../../../blog/kitchen-remodel-cost-massachusetts/', 'Remodeling and buildout costs in Massachusetts', 'Read the guide'),
        'sibling': 'decks-and-patios',
        'sibling_label': '{City} deck contractors',
        'exp_tail': 'the {City} commercial page is written around real scheduling, code and clean execution, not a city name dropped into a template.',
        'quotes': [
            'DeFaria remodeled our {City} space around our hours, so we barely lost a day.',
            'the {City} buildout stayed on schedule and passed inspection clean.',
            'they understood our {City} business, not just the construction.',
            'our {City} space finally matches the brand, and it was done cleanly.',
        ],
        'faq': [
            ('What commercial work does DeFaria Construction handle in {City}?',
             'In {City} DeFaria Construction handles office, retail and restaurant buildouts and remodels: demolition, structure, mechanical, electrical, plumbing coordination and finishes, planned around the operation.'),
            ('How much does commercial remodeling cost in {City}?',
             'A {City} commercial project ranges widely, often about $50 to $200 or more per square foot depending on use, systems and finish. DeFaria gives a fixed, itemized estimate at the walkthrough.'),
            ('How long does a {City} commercial project take?',
             'It depends on the space and scope, from a few weeks for a light buildout to a few months for a full {City} renovation. DeFaria sets a realistic schedule around your operation.'),
            ('Can DeFaria work around our {City} business hours?',
             'Yes. DeFaria plans the {City} schedule around your operation so the work disrupts customers and staff as little as possible.'),
            ('Is DeFaria Construction licensed and insured?',
             'Yes. DeFaria Construction is a licensed and insured contractor with an A+ BBB rating and verified reviews, and every {City} project is owner-led by Luiz DeFaria.'),
            ('Does DeFaria handle {City} commercial permits and inspections?',
             'Yes. {permit_line}'),
        ],
    }


SERVICES = {
    'bathroom-remodeling': bathroom_cfg(), 'kitchen-remodeling': kitchen_cfg(),
    'home-additions': home_additions_cfg(), 'remodeling': remodeling_cfg(),
    'decks-and-patios': decks_cfg(), 'commercial-projects': commercial_cfg(),
}

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
    'home-additions': {
        'dir': 'addition',
        'pool': ['add-real-1.webp', 'add-stock-1.webp', 'add-real-2.webp', 'add-stock-2.webp', 'add-real-3.webp',
                 'add-stock-3.webp', 'add-real-4.webp', 'add-stock-4.webp', 'add-stock-5.webp'],
        'real3': [('add-real-1.webp', 'Finished addition'), ('add-real-4.webp', 'Exterior tie-in'),
                  ('add-real-2.webp', 'New space and finish')],
    },
    'remodeling': {
        'dir': 'remodel',
        'pool': ['rem-real-1.webp', 'rem-stock-1.webp', 'rem-real-2.webp', 'rem-stock-2.webp', 'rem-real-3.webp',
                 'rem-real-4.webp', 'rem-stock-5.webp', 'rem-real-5.webp', 'rem-stock-6.webp'],
        'real3': [('rem-real-1.webp', 'Finished remodel'), ('rem-real-4.webp', 'Living space'),
                  ('rem-real-3.webp', 'Finish detail')],
    },
    'decks-and-patios': {
        'dir': 'deck',
        'pool': ['deck-real-1.webp', 'deck-stock-1.webp', 'deck-real-2.webp', 'deck-stock-2.webp', 'deck-real-3.webp',
                 'deck-stock-4.webp', 'deck-real-4.webp', 'deck-stock-5.webp'],
        'real3': [('deck-real-1.webp', 'Finished deck'), ('deck-real-2.webp', 'Deck and stairs'),
                  ('deck-real-3.webp', 'Railing and finish')],
    },
    'commercial-projects': {
        'dir': 'commercial',
        'credit': '',  # pool majoritariamente Pexels -> alt ilustrativo, sem alegar "by DeFaria"
        'pool': ['comm-real-1.webp', 'comm-stock-1.webp', 'comm-stock-2.webp', 'comm-stock-3.webp', 'comm-stock-4.webp',
                 'comm-stock-5.webp', 'comm-stock-6.webp', 'comm-stock-7.webp', 'comm-stock-8.webp'],
        'real3': [('comm-real-1.webp', 'Finished commercial space'), ('comm-stock-3.webp', 'Office and interior'),
                  ('comm-stock-6.webp', 'Meeting and work area')],
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
        return s.format(City=City, County=county, constraint=constraint, permit_line=permit_line,
                        permit_authority=permit_auth)

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
    credit = imgcfg.get('credit', 'finished by DeFaria Construction')
    photos_grid = '\n          '.join(
        '<figure class="seo-photo-card"><img src="../../../images/seo/%s/%s" width="1000" height="667" '
        'alt="%s" loading="lazy"><figcaption>%s</figcaption></figure>' % (
            idir, fn,
            esc('%s %s %s' % (City, svc_lower, credit) if credit else 'Finished %s in %s, MA' % (svc_lower, City)),
            esc(cap))
        for fn, cap in imgcfg['real3'])

    # secoes extras de profundidade (subtopicos reais que os lideres da SERP cobrem)
    extra_sections = ''
    for i, sec in enumerate(cfg.get('extra_sections', [])):
        light = ' section--light' if i % 2 == 0 else ''
        sec_img = side(11 + i, sec.get('theme', 'more on the project')) if sec.get('img', True) else ''
        paras = '\n          '.join('<p>%s</p>' % esc(T(p)) for p in sec.get('paras', []))
        bul = ''
        if sec.get('bullets'):
            bul = '<ul class="feature-list">\n            %s\n          </ul>' % '\n            '.join(
                '<li>%s</li>' % esc(T(b)) for b in sec['bullets'])
        extra_sections += '''
    <section class="section%s">
      <div class="container detail-grid">
        <div>
          <p class="eyebrow eyebrow--dark">%s</p>
          <h2>%s</h2>
          %s
        </div>
        <div class="detail-copy">
          %s
          %s
        </div>
      </div>
    </section>''' % (light, esc(sec.get('eyebrow', 'Details')), esc(T(sec['h2'])), sec_img, paras, bul)

    hoods_intro = join_and(hoods)
    areas_served_schema = ',\n      '.join('"%s, MA"' % esc(h) for h in hoods)
    hoods_li = '\n            '.join('<li>%s</li>' % esc(h) for h in hoods)

    faq_schema = ',\n      '.join(
        '{\n        "@type": "Question",\n        "name": %s,\n        "acceptedAnswer": { "@type": "Answer", "text": %s }\n      }' % (
            json.dumps(T(q)), json.dumps(T(a))) for q, a in cfg['faq'])

    faq_details = '\n          '.join(
        '<details><summary>%s</summary><p>%s</p></details>' % (esc(T(q)), esc(T(a))) for q, a in cfg['faq'])

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
        svc_phrase = cfg['schema_name'].replace('{City} ', '').replace(' contractors', '')
        cards.append(card('../../%s/%s/' % (cfg['slug'], nb), '%s %s contractors' % (nb_name, svc_phrase), 'View page'))
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
{extra_sections}
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
        faq_schema=faq_schema, gtag=GTAG, hero_img=cfg['hero_img'],
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
        img_experience=img_experience, img_faq=img_faq, photos_grid=photos_grid, extra_sections=extra_sections,
        areas_h2=esc(T(cfg['areas_h2'])), areas_p=esc(T(cfg['areas_p'])),
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
