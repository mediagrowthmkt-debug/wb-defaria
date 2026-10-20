# -*- coding: utf-8 -*-
"""Cidades da onda 1 de pintura interna e built-ins (Kevin 2026-10-20).

Escolha: volume real do Google Ads Keyword Planner (geo Massachusetts, termos 'painters <cidade> ma'),
seo/2026-10/servicos-internos-inverno/vol_termos_cidade.json. Fora por conflito com cliente MG:
Wolf (interior-renovation em Andover, Beverly, Danvers, Lynn, Melrose, North Andover, Peabody, Reading,
Salem, Saugus, Wakefield) e Innov (built-ins em Lynnfield, North Reading, Reading, Wakefield, Woburn).
EXTRA_CITIES so valem para estes dois servicos (nao entram no cities-data.json, pra nao gerar
banheiro/cozinha nessas cidades sem querer).
"""

WAVE1 = ['burlington', 'arlington', 'lexington', 'wilmington', 'chelmsford', 'concord', 'weston',
         'gloucester', 'winchester', 'marblehead']

EXTRA_CITIES = [
    {"name": "Burlington", "slug": "burlington", "county": "Middlesex",
     "neighborhoods": ["Burlington Center", "Mill Pond", "Fox Hill", "the Simonds Park area"],
     "housing_character": "Burlington grew fast after the 1950s, so most homes are mid-century Capes, ranches, split-levels and garrison Colonials, with newer Colonials on the edges of town.",
     "permit_authority": "Town of Burlington Building Department",
     "constraint": "most homes are 1950s and 1960s Capes, ranches and split-levels with original plaster, early drywall and builder-grade trim",
     "nearby_served": ["lexington", "wilmington", "winchester"]},
    {"name": "Arlington", "slug": "arlington", "county": "Middlesex",
     "neighborhoods": ["Arlington Center", "East Arlington", "Arlington Heights", "Morningside", "Jason Heights", "Turkey Hill"],
     "housing_character": "Arlington is full of early 1900s two-family homes, Victorians, bungalows and Colonials, many with original plaster walls and detailed wood trim.",
     "permit_authority": "Town of Arlington Inspectional Services",
     "constraint": "early 1900s two-family homes and Victorians still have horsehair plaster, layers of old paint and original wood trim",
     "nearby_served": ["lexington", "winchester"]},
    {"name": "Chelmsford", "slug": "chelmsford", "county": "Middlesex",
     "neighborhoods": ["Chelmsford Center", "North Chelmsford", "South Chelmsford", "East Chelmsford", "West Chelmsford"],
     "housing_character": "Chelmsford mixes older homes around the town center and North Chelmsford mill village with large post-war neighborhoods of Capes, ranches, split-levels and Colonials.",
     "permit_authority": "Town of Chelmsford Building Department",
     "constraint": "post-war Capes, split-levels and Colonials sit next to much older homes near the center and the North Chelmsford mill village",
     "nearby_served": ["concord", "burlington"]},
    {"name": "Concord", "slug": "concord", "county": "Middlesex",
     "neighborhoods": ["Concord Center", "West Concord", "Nine Acre Corner", "Monument Square", "Thoreau Depot"],
     "housing_character": "Concord has some of the oldest houses in Massachusetts, from 18th-century Colonials and Federal homes near Concord Center to 20th-century Capes and Colonials in West Concord.",
     "permit_authority": "Town of Concord Building Division",
     "constraint": "18th- and 19th-century houses near Concord Center carry original plaster, wide pine trim and many layers of old paint",
     "nearby_served": ["lexington", "weston", "chelmsford"]},
    {"name": "Marblehead", "slug": "marblehead", "county": "Essex",
     "neighborhoods": ["Old Town", "Marblehead Neck", "Clifton", "Devereux", "Peach's Point"],
     "housing_character": "Marblehead ranges from tightly packed 18th-century homes in Old Town to shingle-style and waterfront houses on Marblehead Neck and later Colonials in Clifton and Devereux.",
     "permit_authority": "Town of Marblehead Building Department",
     "constraint": "18th-century Old Town houses and salt-air waterfront homes have narrow stairs, old plaster and trim that takes careful prep",
     "nearby_served": ["gloucester", "winchester"]},
]
