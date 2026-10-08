# -*- coding: utf-8 -*-
# Overrides por pagina (servico, cidade) para a otimizacao de recuperacao de posicao (Kevin, 2026-09-27).
# Motivo: rank tracking Serper 27/09 mostrou quedas nessas paginas; varias keywords colidem com
# cidades homonimas (Carlisle PA, Lincoln NE, Middleton WI/ID, Essex NJ/County) e ha canibalizacao
# (ipswich x essex comercial; boxford comercial x boxford remodeling).
# Chaves opcionais: title, meta, h1, eyebrow, lead, hero_alt, schema_name, local (secao unica de
# contexto local, HTML controlado), faq_extra (lista de (pergunta, resposta)).
# Conteudo: so fatos publicos (geografia, codigos de MA) + dados reais do cities-data.json.
# Nada de preco, prazo, projeto ou avaliacao inventados.

PAGE_OVERRIDES = {

    # ------------------------------------------------------------------ COMMERCIAL
    ('commercial-projects', 'north-reading'): {
        'title': 'North Reading Commercial Remodeling, MA | Free Estimate',
        'meta': 'North Reading commercial remodeling in Massachusetts: office, retail and restaurant buildouts on Route 28 and Route 62, owner-led by DeFaria.',
        'h1': 'North Reading commercial remodeling for offices, shops and restaurants in Massachusetts',
        'eyebrow': 'North Reading, MA commercial contractor',
        'lead': 'North Reading commercial remodeling from DeFaria Construction covers office, retail and restaurant buildouts in North Reading, Massachusetts, scheduled around your hours and priced with a fixed, itemized estimate.',
        'schema_name': 'North Reading, MA commercial remodeling contractors',
        'local': {
            'eyebrow': 'North Reading business corridors',
            'h2': 'Commercial remodeling along the Route 28 and Route 62 corridors in North Reading',
            'theme': 'commercial space along a local corridor',
            'paras': [
                'Most commercial space in North Reading, Massachusetts sits on Main Street (Route 28) and the Route 62 corridor, with smaller professional offices around North Reading Center. These are working storefronts, medical and professional suites and food service spaces that share parking lots and walls with neighboring tenants, so a remodel has to be planned around access, noise and the hours the plaza is open.',
                'A tenant fit-out or renovation in North Reading is permitted through the Town of North Reading Building Department under the Massachusetts State Building Code (780 CMR). When the work touches a public entrance, restroom or path of travel, the Massachusetts Architectural Access Board rules (521 CMR) come into play, and a restaurant or food counter adds a local Board of Health review. DeFaria maps those approvals at the walkthrough so the schedule reflects them from day one.',
                'If you own the building instead of leasing a suite, the same planning covers shell work: storefront glazing, lighting and HVAC changes and interior demising walls are sequenced so the other tenants keep operating.',
            ],
            'bullets': [
                'Tenant fit-outs for retail, office and medical suites',
                'Restaurant and food counter remodels with Board of Health coordination',
                'Accessibility upgrades to entrances, restrooms and paths of travel',
                'Phased, early or after-hours work when the business stays open',
            ],
        },
        'faq_extra': [
            ('Do I need a permit for a commercial remodel in North Reading, MA?',
             'In most cases, yes. Structural, electrical, plumbing and mechanical work and most interior buildouts are permitted through the Town of North Reading Building Department under the Massachusetts State Building Code. DeFaria prepares the scope and coordinates the permit before work starts.'),
            ('Can DeFaria remodel a tenant space in a shared North Reading plaza?',
             'Yes. DeFaria plans the work around the landlord rules, shared parking and neighboring tenants, and can phase noisy work outside business hours when needed.'),
        ],
    },

    ('commercial-projects', 'lynnfield'): {
        'title': 'Lynnfield Commercial Remodeling, MA | Licensed & Insured',
        'meta': 'Lynnfield commercial remodeling in Massachusetts for Route 1, MarketStreet and Lynnfield Center businesses. Licensed, insured, owner-led. Free estimate.',
        'h1': 'Lynnfield commercial remodeling for Route 1, MarketStreet and Lynnfield Center businesses',
        'eyebrow': 'Lynnfield, MA commercial contractor',
        'lead': 'Lynnfield commercial remodeling from DeFaria Construction serves offices, shops and restaurants in Lynnfield, Massachusetts, with a schedule built around your customers and a fixed, itemized estimate.',
        'schema_name': 'Lynnfield, MA commercial remodeling contractors',
        'local': {
            'eyebrow': 'Where Lynnfield businesses operate',
            'h2': 'Lynnfield commercial projects: Route 1, MarketStreet and the town center',
            'theme': 'finished commercial interior',
            'paras': [
                'Commercial work in Lynnfield, Massachusetts clusters in three very different settings. South Lynnfield along Route 1 is high-traffic retail and restaurant space. MarketStreet Lynnfield, off Route 128 at Walnut Street, is a managed lifestyle center where tenants work inside the landlord construction rules. Lynnfield Center holds smaller professional offices and service businesses close to homes.',
                'Each setting changes the plan. In a managed center, drawings usually go through landlord review before the town permit, and deliveries and loud work follow set hours. On Route 1, customer parking and road access decide when materials can arrive. Near Lynnfield Center, neighbors and quieter streets shape the work day. DeFaria builds the schedule around whichever of those applies.',
                'Permits for Lynnfield commercial remodeling run through the Town of Lynnfield Building Department under the Massachusetts State Building Code, with accessibility work reviewed against 521 CMR.',
            ],
            'bullets': [
                'Retail and restaurant remodels on the Route 1 corridor',
                'Tenant improvements that follow landlord construction rules',
                'Professional office and service suites near Lynnfield Center',
                'Accessibility, lighting and finish upgrades for customer-facing spaces',
            ],
        },
        'faq_extra': [
            ('Does DeFaria work on tenant spaces in managed centers like MarketStreet Lynnfield?',
             'Yes. For a tenant space in a managed center, DeFaria works within the landlord approval process, work hours and delivery rules, then coordinates the town permit.'),
            ('Who issues commercial building permits in Lynnfield, MA?',
             'The Town of Lynnfield Building Department, under the Massachusetts State Building Code. DeFaria prepares the scope and handles that step as part of the project.'),
        ],
    },

    ('commercial-projects', 'lincoln'): {
        'title': 'Lincoln Commercial Remodeling, Massachusetts | DeFaria',
        'meta': 'Lincoln commercial remodeling in Lincoln, Massachusetts (Middlesex County): offices, shops and community spaces near Lincoln Station. Free estimate.',
        'h1': 'Lincoln commercial remodeling in Lincoln, Massachusetts, planned around your business',
        'eyebrow': 'Lincoln, MA (Middlesex County)',
        'lead': 'Lincoln commercial remodeling from DeFaria Construction serves offices, shops and community spaces in Lincoln, Massachusetts, the Middlesex County town west of Boston, with a clear scope and a fixed, itemized estimate.',
        'schema_name': 'Lincoln, MA commercial remodeling contractors',
        'local': {
            'eyebrow': 'Lincoln, Massachusetts',
            'h2': 'Commercial remodeling in Lincoln, MA: small-scale spaces in a conservation town',
            'theme': 'small commercial interior',
            'paras': [
                'This page is about Lincoln, Massachusetts, not Lincoln, Nebraska or any other Lincoln. Lincoln, MA is a mostly residential, conservation-minded town, so commercial remodeling here is usually small in scale: the shops and offices around Lincoln Station near the commuter rail stop, professional offices along Route 2 and Route 117, and nonprofit or community-facing spaces.',
                'Small spaces leave little room for error. A remodel often has to fit new restrooms, lighting and HVAC into an older footprint while meeting the Massachusetts State Building Code and the accessibility rules in 521 CMR. Permits go through the Town of Lincoln Building & Engineering Department, and properties near wetlands may also need Conservation Commission review before exterior work starts.',
                'DeFaria Construction is based in Lynn, MA and works across Middlesex and Essex County, so a Lincoln project gets a local contractor who knows how these towns review commercial work.',
            ],
            'bullets': [
                'Office and retail refreshes near Lincoln Station',
                'Restroom and entrance accessibility upgrades',
                'Lighting, HVAC and finish updates in older buildings',
                'Community and nonprofit space renovations',
            ],
        },
        'faq_extra': [
            ('Is this page for Lincoln, Massachusetts or Lincoln, Nebraska?',
             'Lincoln, Massachusetts, the Middlesex County town west of Boston. DeFaria Construction is based in Lynn, MA and works across Middlesex and Essex County in Massachusetts only.'),
            ('Who reviews commercial permits in Lincoln, MA?',
             'The Town of Lincoln Building & Engineering Department, under the Massachusetts State Building Code. Work near wetlands can also need Conservation Commission review.'),
        ],
    },

    ('commercial-projects', 'middleton'): {
        'title': 'Middleton Commercial Remodeling, Massachusetts | DeFaria',
        'meta': 'Middleton commercial remodeling in Middleton, Massachusetts (Essex County): retail, office and restaurant work on Route 114 and Route 62. Free estimate.',
        'h1': 'Middleton commercial remodeling for Middleton, Massachusetts businesses',
        'eyebrow': 'Middleton, MA (Essex County)',
        'lead': 'Middleton commercial remodeling from DeFaria Construction covers retail, office and restaurant spaces in Middleton, Massachusetts, planned around your operation with a fixed, itemized estimate.',
        'schema_name': 'Middleton, MA commercial remodeling contractors',
        'local': {
            'eyebrow': 'Middleton, Massachusetts',
            'h2': 'Commercial remodeling on Middleton\'s Route 114 and Route 62 corridors',
            'theme': 'commercial storefront interior',
            'paras': [
                'This page covers Middleton, Massachusetts in Essex County, not Middleton, Wisconsin or Middleton, Idaho. In Middleton, MA most businesses sit on South Main Street (Route 114) and along Route 62 near Middleton Center: plazas with retail and restaurants, service businesses, and professional offices close to the Danvers and North Reading lines.',
                'A plaza tenant space is a shared building, so a remodel has to respect common walls, fire separations and parking used by other tenants. Food service adds grease, ventilation and Board of Health review. Permits and inspections run through the Town of Middleton Office of the Inspector of Buildings, and DeFaria lines those up before demolition so the space is not left open longer than needed.',
            ],
            'bullets': [
                'Plaza retail and restaurant remodels on Route 114',
                'Office and service suite fit-outs near Middleton Center',
                'Fire separation, accessibility and code updates',
                'Work phased around customer hours and shared parking',
            ],
        },
        'faq_extra': [
            ('Is this page for Middleton, Massachusetts?',
             'Yes. It covers Middleton, MA in Essex County. DeFaria Construction is based in Lynn, MA and works in Massachusetts only, not in Middleton, Wisconsin or Idaho.'),
            ('Who inspects commercial remodeling work in Middleton, MA?',
             'The Town of Middleton Office of the Inspector of Buildings handles permits and inspections. DeFaria coordinates that step as part of the project.'),
        ],
    },

    ('commercial-projects', 'carlisle'): {
        'title': 'Carlisle Commercial Remodeling, Massachusetts | DeFaria',
        'meta': 'Carlisle commercial remodeling in Carlisle, Massachusetts (Middlesex County): small offices, shops and town center spaces on septic and well. Free estimate.',
        'h1': 'Carlisle commercial remodeling for businesses in Carlisle, Massachusetts',
        'eyebrow': 'Carlisle, MA (Middlesex County)',
        'lead': 'Carlisle commercial remodeling from DeFaria Construction serves offices, shops and service spaces in Carlisle, Massachusetts, with the site, septic and permit questions answered before the estimate.',
        'schema_name': 'Carlisle, MA commercial remodeling contractors',
        'local': {
            'eyebrow': 'Carlisle, Massachusetts',
            'h2': 'Commercial remodeling in Carlisle, MA: a small town center on septic and well',
            'theme': 'small office interior',
            'paras': [
                'This page is for Carlisle, Massachusetts in Middlesex County, not Carlisle, Pennsylvania. Carlisle, MA is a rural town with a small commercial center, so commercial remodeling here usually means small offices, shops and service businesses rather than large tenant buildouts.',
                'Carlisle has no town water or sewer. Buildings rely on private wells and on-site septic systems, so a remodel that adds restrooms, a kitchenette or food service can depend on septic capacity under Massachusetts Title 5 and a Board of Health review. Exterior changes in the town center may also need historic review. DeFaria checks those limits at the walkthrough, before layout and budget are set.',
                'Building permits run through the Town of Carlisle Building Department under the Massachusetts State Building Code, and DeFaria coordinates the inspections as part of the job.',
            ],
            'bullets': [
                'Office and retail refreshes in the town center',
                'Restroom and plumbing changes checked against septic capacity',
                'Accessibility, lighting and HVAC updates',
                'Exterior work planned around historic review when it applies',
            ],
        },
        'faq_extra': [
            ('Is this page for Carlisle, Massachusetts or Carlisle, Pennsylvania?',
             'Carlisle, Massachusetts in Middlesex County. DeFaria Construction is based in Lynn, MA and works in Massachusetts only.'),
            ('Does septic capacity affect a commercial remodel in Carlisle, MA?',
             'It can. Carlisle has no town sewer, so adding restrooms or food service may require the septic system to support the new use under Title 5. DeFaria checks this early so it does not surprise the budget.'),
        ],
    },

    ('commercial-projects', 'essex'): {
        'title': 'Essex Commercial Remodeling, Town of Essex MA | DeFaria',
        'meta': 'Essex commercial remodeling in the town of Essex, Massachusetts: shops, restaurants and marine businesses on Route 133 and the Essex River. Free estimate.',
        'h1': 'Essex commercial remodeling for shops and restaurants in the town of Essex, MA',
        'eyebrow': 'Essex, MA (the town on Cape Ann)',
        'lead': 'Essex commercial remodeling from DeFaria Construction serves the antique shops, restaurants and marine businesses of Essex, Massachusetts, with work planned around the season and a fixed, itemized estimate.',
        'schema_name': 'Essex, MA commercial remodeling contractors',
        'local': {
            'eyebrow': 'The town of Essex, Massachusetts',
            'h2': 'Commercial remodeling on Route 133 and along the Essex River',
            'theme': 'restaurant and retail interior',
            'paras': [
                'This page is for the town of Essex, Massachusetts, the small Cape Ann community between Ipswich and Gloucester. It is not about Essex County as a whole, Essex, New Jersey or Essex, Vermont. Commercial life in Essex runs along Main Street (Route 133) and the Essex River: antique shops, seafood restaurants, boatyards and marine businesses in buildings tied to the town\'s shipbuilding past.',
                'That mix shapes every remodel. Restaurants need ventilation, grease handling and Board of Health review. Older timber-framed buildings need structure checked before walls come out. Sites near the river and salt marsh can fall under flood zone rules and Conservation Commission review. And because many Essex businesses are busiest in summer, DeFaria plans the heavy work for the off-season whenever the scope allows.',
                'Permits run through the Town of Essex Building Department. If your business is in the neighboring town, see our <a href="../ipswich/" style="text-decoration:underline">Ipswich commercial remodeling</a> page instead.',
            ],
            'bullets': [
                'Restaurant and seafood kitchen remodels with Board of Health coordination',
                'Antique shop and retail storefront renovations on Route 133',
                'Structural checks in older timber-framed buildings',
                'Off-season scheduling for seasonal businesses',
            ],
        },
        'faq_extra': [
            ('Is this page for the town of Essex or for Essex County?',
             'The town of Essex, Massachusetts, on Cape Ann. DeFaria Construction also works across Essex County, and each nearby town, such as Ipswich and Gloucester, has its own page.'),
            ('Can DeFaria remodel a seasonal Essex restaurant in the off-season?',
             'Yes. When the scope allows, DeFaria schedules demolition and heavy work for the slower months so a seasonal Essex business opens on time.'),
        ],
    },

    ('commercial-projects', 'ipswich'): {
        'title': 'Ipswich Commercial Remodeling, MA | Licensed Contractor',
        'meta': 'Ipswich commercial remodeling in Ipswich, Massachusetts: downtown shops, restaurants and offices in historic buildings. Owner-led by DeFaria. Free estimate.',
        'h1': 'Ipswich commercial remodeling for downtown shops, restaurants and offices in Ipswich, MA',
        'eyebrow': 'Ipswich, MA commercial contractor',
        'lead': 'Ipswich commercial remodeling from DeFaria Construction serves businesses in Ipswich, Massachusetts, from downtown storefronts to restaurants and offices in historic buildings, with a fixed, itemized estimate.',
        'schema_name': 'Ipswich, MA commercial remodeling contractors',
        'local': {
            'eyebrow': 'Downtown Ipswich',
            'h2': 'Commercial remodeling in downtown Ipswich and along Routes 1A and 133',
            'theme': 'storefront and office interior',
            'paras': [
                'Ipswich commercial remodeling centers on downtown Ipswich, along Market Street and Central Street near the Ipswich River, and on the Route 1A and Route 133 corridors. Many of these businesses operate inside buildings from the 1700s and 1800s, in a town known for one of the country\'s largest concentrations of First Period architecture.',
                'Historic buildings change the job. Old framing, uneven floors and past alterations are opened carefully and documented before new work is designed, exterior changes to historic properties can require Ipswich Historical Commission review, and new restrooms or entrances must meet the Massachusetts accessibility rules in 521 CMR. Restaurants and takeout counters add Board of Health review. DeFaria plans all of this with the Town of Ipswich Building Department before demolition.',
                'This page is only for Ipswich. For businesses in the neighboring town, see <a href="../essex/" style="text-decoration:underline">Essex commercial remodeling</a>.',
            ],
            'bullets': [
                'Downtown storefront and office renovations',
                'Restaurant and takeout counter remodels',
                'Careful work inside First Period and 19th-century buildings',
                'Accessibility upgrades to entrances and restrooms',
            ],
        },
        'faq_extra': [
            ('Does DeFaria remodel commercial space inside historic Ipswich buildings?',
             'Yes. DeFaria opens older framing carefully, plans around historic review when exterior changes are involved, and coordinates permits with the Town of Ipswich Building Department.'),
            ('Do Ipswich restaurant remodels need extra approvals?',
             'Usually, yes. Beyond the building permit, food service work in Ipswich typically needs Board of Health review for kitchens, ventilation and grease handling. DeFaria plans for it in the schedule.'),
        ],
    },

    ('commercial-projects', 'boxford'): {
        'title': 'Boxford Commercial Remodeling, MA | Offices & Retail',
        'meta': 'Boxford commercial remodeling in Boxford, Massachusetts: offices, shops and mixed-use buildings on well and septic. Licensed, owner-led. Free estimate.',
        'h1': 'Boxford commercial remodeling for offices, shops and mixed-use buildings in Boxford, MA',
        'eyebrow': 'Boxford, MA commercial contractor',
        'lead': 'Boxford commercial remodeling from DeFaria Construction serves offices, shops and mixed-use buildings in Boxford, Massachusetts, a business-focused service that is separate from our home remodeling work.',
        'schema_name': 'Boxford, MA commercial remodeling contractors',
        'local': {
            'eyebrow': 'Commercial, not residential',
            'h2': 'Boxford commercial remodeling: business spaces in a residential town',
            'theme': 'office and retail interior',
            'paras': [
                'Boxford, Massachusetts is mostly residential, with limited commercial zoning, so Boxford commercial remodeling usually means smaller projects: professional offices, shops and service businesses in the village centers, mixed-use buildings, and community-facing spaces. This page is only about those business spaces. If you are remodeling a house, see our <a href="../../remodeling/boxford/" style="text-decoration:underline">Boxford home remodeling</a> page.',
                'Like most of Boxford, commercial buildings typically rely on private wells and septic systems, so adding restrooms or a kitchenette can depend on septic capacity under Title 5 and a Board of Health review. Public spaces also need the accessibility rules in 521 CMR. Permits run through the Town of Boxford Building Department, and DeFaria coordinates them before work starts.',
            ],
            'bullets': [
                'Professional office and service suite remodels',
                'Retail and mixed-use building renovations',
                'Restroom and plumbing changes checked against septic capacity',
                'Accessibility and code upgrades for public-facing spaces',
            ],
        },
        'faq_extra': [
            ('What is the difference between this page and Boxford home remodeling?',
             'This page covers commercial spaces in Boxford: offices, shops and mixed-use buildings. Remodeling a house in Boxford is covered on the Boxford home remodeling page.'),
            ('Does septic capacity matter for a Boxford commercial remodel?',
             'It can. Most Boxford buildings are on private septic, so new restrooms or food service may need the system to support the added use. DeFaria checks this before the estimate is final.'),
        ],
    },

    # ------------------------------------------------------------------ HOME ADDITIONS
    ('home-additions', 'carlisle'): {
        'title': 'Carlisle Home Addition Builders, Massachusetts | DeFaria',
        'meta': 'Carlisle home addition builders in Carlisle, Massachusetts: additions on two-acre lots with septic, well and setbacks planned first. Free estimate.',
        'h1': 'Carlisle home addition builders for farmhouses and estates in Carlisle, Massachusetts',
        'eyebrow': 'Carlisle, MA (Middlesex County)',
        'lead': 'Carlisle home addition work from DeFaria Construction is planned for Carlisle, Massachusetts lots, where septic capacity, well location and setbacks decide the size and shape of the addition before design starts.',
        'schema_name': 'Carlisle, MA home addition contractors',
        'local': {
            'eyebrow': 'Carlisle, Massachusetts',
            'h2': 'What shapes a home addition in Carlisle, MA: septic, well and setbacks',
            'theme': 'addition on a wooded lot',
            'paras': [
                'This page is for Carlisle, Massachusetts, not Carlisle, Pennsylvania. Carlisle, MA homes sit on large wooded parcels with no town water or sewer, which changes how an addition is planned.',
                'Every home here runs on a private well and an on-site septic system. Under Massachusetts Title 5, septic design is tied to the number of bedrooms, so an addition that adds a bedroom can require a septic review or upgrade through the Board of Health before a building permit is issued. The well and the septic leach field also limit where new foundations can go, and wetlands on many wooded lots can bring in the Conservation Commission.',
                'Design is the other half. Historic farmhouses and newer estates each need rooflines, siding and window proportions carried into the addition so it reads as part of the original house. DeFaria checks the site limits first, then designs the addition around them, and coordinates the permit with the Town of Carlisle Building Department.',
            ],
            'bullets': [
                'Septic and bedroom-count check under Title 5 before design',
                'Foundation placement planned around well, leach field and setbacks',
                'Conservation Commission review when wetlands are nearby',
                'Rooflines and exterior matched to farmhouse or estate style',
            ],
        },
        'faq_extra': [
            ('Does adding a bedroom in Carlisle, MA affect my septic system?',
             'It can. Carlisle homes use private septic systems, and Title 5 ties septic design to bedroom count, so a bedroom addition may need Board of Health review or a septic upgrade. DeFaria checks this first.'),
            ('Is this page for Carlisle, Massachusetts?',
             'Yes. It covers Carlisle, MA in Middlesex County. DeFaria Construction works in Massachusetts only, not in Carlisle, Pennsylvania.'),
        ],
    },

    ('home-additions', 'essex'): {
        'title': 'Essex Home Addition Builder in Essex, MA | DeFaria',
        'meta': 'Essex home addition builder in the town of Essex, Massachusetts: additions for antique and waterfront homes, with flood and septic rules planned first.',
        'h1': 'Essex home additions from a local home addition builder in Essex, MA',
        'eyebrow': 'Essex, MA (the town on Cape Ann)',
        'lead': 'Essex home addition projects from DeFaria Construction add space to antique Capes, Colonials and waterfront homes in Essex, Massachusetts, with flood, septic and design questions answered before the estimate.',
        'schema_name': 'Essex, MA home addition contractors',
        'local': {
            'eyebrow': 'The town of Essex, Massachusetts',
            'h2': 'Planning a home addition in Essex, MA near the river and the marsh',
            'theme': 'addition on a New England home',
            'paras': [
                'This page is for the town of Essex, Massachusetts on Cape Ann, not Essex County, New Jersey or other places named Essex. Homes in Essex range from antique Colonials, Federals and Capes tied to the town\'s shipbuilding past to newer waterfront houses near the Essex River and Conomo Point.',
                'Those settings bring specific rules. Lots near the river and salt marsh can sit in a FEMA flood zone, which affects foundation height and construction, and work near wetlands needs Conservation Commission review. Many Essex homes use septic systems, and under Title 5 a bedroom addition can require a septic review with the Board of Health. DeFaria confirms all of this before designing, so the addition is sized to what the lot allows.',
                'On antique homes, the addition has to respect the original massing: a lower connector, matching roof pitch and trim that fits the period. Permits run through the Town of Essex Building Department.',
                'Choosing a home addition builder in Essex comes down to a few questions worth asking any contractor: who will actually run the job day to day, how the addition will be tied into the existing roof and foundation, how flood, wetland and septic approvals will be handled, and how the price is broken down. At DeFaria Construction the project is owner-led by Luiz DeFaria, the estimate is itemized, and those approvals are planned before construction instead of discovered during it.',
            ],
            'bullets': [
                'Flood zone and Conservation Commission checks near the river and marsh',
                'Septic and bedroom-count review under Title 5',
                'Additions scaled to antique Capes, Colonials and Federals',
                'Waterfront additions built for coastal weather',
            ],
        },
        'faq_extra': [
            ('Do I need Conservation Commission approval for an addition in Essex, MA?',
             'If the work is near the Essex River, the salt marsh or other wetlands, often yes. DeFaria checks the lot early and plans the approval into the schedule.'),
            ('Is DeFaria a home addition builder in the town of Essex or Essex County?',
             'Both. This page covers the town of Essex, MA, and DeFaria Construction also builds additions across Essex County towns such as Ipswich, Hamilton and Gloucester.'),
        ],
    },

    ('home-additions', 'tewksbury'): {
        'title': 'Tewksbury Home Addition Contractors, MA | Free Estimate',
        'meta': 'Tewksbury home addition contractors in Tewksbury, Massachusetts: second stories, primary suites and bump-outs for capes, ranches and colonials.',
        'h1': 'Tewksbury home addition contractors for capes, ranches and colonials',
        'eyebrow': 'Tewksbury, MA home additions',
        'lead': 'Tewksbury home addition projects from DeFaria Construction add second stories, primary suites and bump-outs to Tewksbury, Massachusetts homes, with structure and zoning checked before design.',
        'schema_name': 'Tewksbury, MA home addition contractors',
        'local': {
            'eyebrow': 'Addition types in Tewksbury',
            'h2': 'Which home addition fits a Tewksbury cape, ranch or colonial?',
            'theme': 'second-story addition',
            'paras': [
                'Tewksbury homes fall into a few clear groups: colonial-era and farm homes near Tewksbury Center, mid-century capes and ranches across North and South Tewksbury, and newer colonial subdivisions around neighborhoods like Indian Ridge. Each points to a different kind of addition.',
                'A ranch often gains the most from a second story or a rear primary suite, but the existing foundation and walls have to be checked to carry the new load. A cape usually grows with a full or partial dormer that turns cramped upstairs rooms into real bedrooms. A newer colonial tends to get a family room or kitchen bump-out, or a suite over the garage. Older center-of-town homes need the addition matched to their original rooflines.',
                'Before design, DeFaria confirms zoning setbacks and lot coverage and coordinates the permit with the Town of Tewksbury Building Department, so the addition you plan is one the lot allows.',
            ],
            'bullets': [
                'Second-story additions on ranches, with structure checked first',
                'Dormers that turn cape upstairs into full bedrooms',
                'Kitchen and family room bump-outs on colonials',
                'Primary suites over garages or at the rear of the home',
            ],
        },
        'faq_extra': [
            ('What is the most common home addition in Tewksbury, MA?',
             'It depends on the house. Ranches often add a second story or rear suite, capes usually add dormers, and newer colonials often add a bump-out or a suite over the garage. DeFaria recommends the option after seeing the structure and lot.'),
            ('Do Tewksbury additions need zoning review?',
             'Every addition is checked against Tewksbury setbacks and lot rules. If a lot is nonconforming, zoning relief may be needed before the building permit. DeFaria checks this before design.'),
        ],
    },

    ('home-additions', 'ipswich'): {
        'title': 'Home Additions Ipswich, MA | Licensed Builder | DeFaria',
        'meta': 'Home additions in Ipswich, MA for First Period, Colonial and coastal homes, with historic, flood and septic rules planned first. Licensed. Free estimate.',
        'h1': 'Home additions Ipswich, MA families can grow into, built to respect historic homes',
        'eyebrow': 'Ipswich, MA home additions',
        'lead': 'Home additions Ipswich homeowners plan with DeFaria Construction are designed around First Period, Colonial and coastal homes in Ipswich, Massachusetts, with the historic, flood and septic questions answered before design.',
        'schema_name': 'Ipswich, MA home addition contractors',
        'local': {
            'eyebrow': 'Ipswich, Massachusetts',
            'h2': 'Adding on to a First Period or coastal home in Ipswich',
            'theme': 'addition on a historic home',
            'paras': [
                'Ipswich holds one of the country\'s largest concentrations of First Period houses, plus Georgian and Federal homes around Meeting House Green, High Street and the East End. An addition on one of these homes has to stay smaller and subordinate to the original, often with a connector, matching roof pitch and trim, and some Ipswich homes carry preservation restrictions that set what can change.',
                'On Great Neck and Little Neck the questions are different: coastal lots can sit in a FEMA flood zone, and work near wetlands needs Conservation Commission review. Where a home uses septic, Title 5 ties the system to bedroom count, so a bedroom addition can require a Board of Health review.',
                'DeFaria sorts out those limits first, then designs the addition and coordinates the permit with the Town of Ipswich Building Department.',
            ],
            'bullets': [
                'Additions kept subordinate to First Period and Colonial homes',
                'Preservation restriction and historic review checked early',
                'Flood zone and wetlands planning for Great Neck and Little Neck',
                'Septic and bedroom-count review when it applies',
            ],
        },
        'faq_extra': [
            ('Can I build an addition on a historic home in Ipswich?',
             'Usually, yes, with care. The addition is designed to stay subordinate to the original house, and if the home has a preservation restriction or needs historic review, DeFaria plans that step before design is final.'),
            ('Do coastal Ipswich homes have extra rules for additions?',
             'Often. Homes on Great Neck and Little Neck can be in a flood zone or near wetlands, which affects foundations and may need Conservation Commission review.'),
        ],
    },

    # ------------------------------------------------------------------ KITCHEN
    ('kitchen-remodeling', 'carlisle'): {
        'title': 'Modern Kitchen Remodeling in Carlisle, MA | DeFaria',
        'meta': 'Modern kitchen remodeling in Carlisle, MA: flat-panel cabinets, quartz, integrated appliances and layered lighting for farmhouses and estates.',
        'h1': 'Modern kitchen remodeling in Carlisle, MA with clean lines and a layout that works',
        'eyebrow': 'Carlisle, MA kitchen remodeling',
        'lead': 'Modern kitchen remodeling in Carlisle, MA from DeFaria Construction brings clean lines, integrated storage and better light to Carlisle farmhouses and estates, with scope and budget set before demolition.',
        'schema_name': 'Carlisle, MA kitchen remodeling contractors',
        'local': {
            'eyebrow': 'Modern kitchens in Carlisle',
            'h2': 'What a modern kitchen looks like in a Carlisle, MA home',
            'theme': 'modern kitchen',
            'paras': [
                'A modern kitchen is less about a trend and more about clean lines and less visual clutter: flat-panel or slim shaker cabinets, quartz or stone counters with simple edges, integrated or panel-ready appliances, hidden storage and layered lighting under cabinets and over the island.',
                'In Carlisle, Massachusetts that style often goes into historic farmhouses or large contemporary homes on wooded lots. In a farmhouse the goal is usually a modern kitchen that still respects beams, wide trim and window placement. In a contemporary estate it is often a bigger island, a pantry wall and a direct line to the patio or yard.',
                'Carlisle homes run on private wells, so many kitchens also need space for water filtration or treatment equipment, planned into the sink base or a nearby cabinet from the start. Electrical service is reviewed early too, since induction cooktops and wall ovens can need upgraded circuits.',
            ],
            'bullets': [
                'Flat-panel or slim shaker cabinetry with integrated pulls',
                'Quartz or stone counters and a working island',
                'Panel-ready appliances and induction-ready electrical',
                'Room for well water filtration in the cabinet plan',
            ],
        },
        'faq_extra': [
            ('Can a modern kitchen work in a Carlisle farmhouse?',
             'Yes. DeFaria keeps the elements that give the house its character, like beams, trim and window placement, and brings in clean-lined cabinets, counters and lighting around them.'),
            ('Does well water affect a Carlisle kitchen remodel?',
             'It can. Many Carlisle homes on private wells use filtration or treatment equipment, so DeFaria plans cabinet space and plumbing for it before the layout is final.'),
        ],
    },

    # ------------------------------------------------------------------ REMODELING
    ('remodeling', 'pepperell'): {
        'title': 'Pepperell Remodeling Contractors, MA | Free Estimate',
        'meta': 'Pepperell remodeling contractors in Pepperell, Massachusetts: interior remodels for Colonial, Victorian and mill village homes. Owner-led. Free estimate.',
        'h1': 'Pepperell remodeling contractors for Colonial, Victorian and mill village homes',
        'eyebrow': 'Pepperell, MA remodeling',
        'lead': 'Pepperell remodeling from DeFaria Construction updates kitchens, baths and whole floors in Pepperell, Massachusetts homes, from East Pepperell mill houses to Victorians near the center.',
        'schema_name': 'Pepperell, MA remodeling contractors',
        'local': {
            'eyebrow': 'Pepperell homes',
            'h2': 'Remodeling older Pepperell homes: what we check behind the walls',
            'theme': 'remodeled interior',
            'paras': [
                'Pepperell mixes older Colonial and Victorian-era homes near Pepperell Center, worker housing in the East Pepperell mill village along the Nashua River, and newer houses on semi-rural lots. The older homes are where a remodel needs the most planning.',
                'Houses built before 1978 can have lead paint, so work that disturbs painted surfaces follows lead-safe work practices. Victorian and mill-era homes often have balloon framing that needs fire blocking when walls are open, older wiring that may need replacement, and floors that have settled over a century. DeFaria opens up and checks these conditions at the start, so they are priced honestly instead of discovered halfway through.',
                'Permits and inspections run through the Town of Pepperell Building Department, and DeFaria coordinates them as part of the project.',
            ],
            'bullets': [
                'Lead-safe work practices in homes built before 1978',
                'Fire blocking and framing repair in balloon-framed walls',
                'Wiring and plumbing updates while walls are open',
                'Leveling and subfloor repair in older floors',
            ],
        },
        'faq_extra': [
            ('Do older Pepperell homes need lead-safe remodeling?',
             'If the home was built before 1978 and the work disturbs painted surfaces, lead-safe practices apply. DeFaria plans for this in older Pepperell homes.'),
            ('What does DeFaria remodel in Pepperell, MA?',
             'Kitchens, bathrooms, whole floors and interior layouts, room by room or whole-home, with the older-home conditions checked before the estimate is final.'),
        ],
    },

    ('remodeling', 'boxford'): {
        'title': 'Boxford Remodeling Contractors, MA | Homes & Interiors',
        'meta': 'Boxford remodeling contractors for homes in Boxford, Massachusetts: kitchens, baths and whole-home interior remodels for Colonials. Free estimate.',
        'h1': 'Boxford remodeling contractors for homes that finally work',
        'eyebrow': 'Boxford, MA home remodeling',
        'lead': 'Boxford remodeling from DeFaria Construction turns dated rooms in Boxford, Massachusetts homes into finished spaces, with a clear scope, honest sequencing and careful finish work.',
        'schema_name': 'Boxford, MA home remodeling contractors',
        'local': {
            'eyebrow': 'Home remodeling in Boxford',
            'h2': 'Home remodeling for Boxford Colonials on large wooded lots',
            'theme': 'remodeled home interior',
            'paras': [
                'This page is about remodeling houses in Boxford, Massachusetts: kitchens, bathrooms and whole-home interior projects in historic Colonials and newer single-family homes across East Boxford, West Boxford and the village centers.',
                'Large wooded and conservation lots mean long driveways, well and septic systems and sometimes wetlands nearby, which affect deliveries, dumpster placement and any work that adds bathrooms. DeFaria checks those conditions at the walkthrough. If you need work on a business space instead, see <a href="../../commercial-projects/boxford/" style="text-decoration:underline">Boxford commercial remodeling</a>.',
            ],
            'bullets': [
                'Kitchen, bath and whole-floor remodels in Boxford homes',
                'Site access planned for long driveways and wooded lots',
                'Added bathrooms checked against septic capacity',
            ],
        },
        'faq_extra': [
            ('Does DeFaria also remodel commercial spaces in Boxford?',
             'Yes, and that work has its own page: Boxford commercial remodeling. This page covers home remodeling only.'),
        ],
    },
}


# Secoes locais adicionais (H2 extras) nas paginas onde o lider da SERP cobre mais subtopicos.
_MORE_SECTIONS = {
    ('home-additions', 'carlisle'): [
        {
            'eyebrow': 'Size and zoning',
            'h2': 'How big can a home addition be on a Carlisle, MA lot?',
            'theme': 'addition sized to the lot',
            'paras': [
                'In Carlisle the lot itself sets the ceiling. Most homes sit on parcels of two acres or more, which sounds like plenty of room, but the buildable area is smaller than it looks: setbacks from the property lines, the septic system and its reserve area, the well and its protective radius, and any wetland buffer all come off the top.',
                'That is why DeFaria starts a Carlisle addition with the site, not the floor plan. Once the usable footprint is clear, the addition can go out, up or over the garage in the spot that costs the least in foundation and utility work. On older farmhouses that often means a rear wing or an ell, a form that has been used to add space to New England houses for centuries.',
                'Since February 2025, Massachusetts law also allows one accessory dwelling unit of up to 900 square feet by right in single-family zones, subject to local site and health rules. For Carlisle families planning space for a parent or an adult child, an attached in-law addition can now be simpler to approve, though the septic and well questions still apply.',
            ],
            'bullets': [
                'Buildable area mapped after setbacks, septic reserve, well and wetlands',
                'Rear wings and ells that suit historic farmhouses',
                'Attached in-law suites under the 2025 Massachusetts ADU law',
                'Second-story options when the footprint cannot grow',
            ],
        },
        {
            'eyebrow': 'Before construction',
            'h2': 'The order of approvals for a Carlisle home addition',
            'theme': 'planned addition',
            'paras': [
                'A Carlisle addition moves through its approvals in a set order, and knowing it up front keeps the schedule honest. First comes the site check: septic design flow, well location, setbacks and any wetlands. If a bedroom is being added, the Board of Health reviews the septic under Title 5, and a system upgrade may be part of the scope. If the work falls inside a wetland buffer, the Conservation Commission reviews it next.',
                'Only then is the design finished and the building permit filed with the Town of Carlisle Building Department. Construction follows the same sequence as any DeFaria addition: foundation, framing and roof tie-in, weather-tight shell, rough-in, insulation and finishes, with inspections at each stage. Planning the approvals first means the crew is not waiting on paperwork once work begins.',
                'Budget follows the same logic. On a Carlisle lot, the items that move the price most are usually the ones outside the new rooms: foundation depth and ledge, the length of the utility runs from the house, any septic upgrade, tree clearing and driveway access for equipment. DeFaria lists those separately in the estimate, so you can see what the site costs and what the addition itself costs before you commit.',
            ],
            'bullets': [
                'Site check: septic, well, setbacks and wetlands',
                'Board of Health septic review when bedrooms are added',
                'Conservation Commission review inside wetland buffers',
                'Building permit and staged inspections through construction',
            ],
        },
    ],

    ('home-additions', 'ipswich'): [
        {
            'eyebrow': 'Old-house details',
            'h2': 'Matching an Ipswich addition to the original house',
            'theme': 'addition matched to a historic home',
            'paras': [
                'The additions that look right in Ipswich are the ones that follow the original house: the same roof pitch, clapboard exposure and trim depth, windows with similar proportions, and a scale that stays below the main block. A slightly narrower connector between old and new keeps the historic house readable and makes the transition between old framing and new framing easier to build.',
                'Inside, the goal is the reverse: new rooms should feel open and comfortable while meeting today\'s code for insulation, egress and structure, even where they meet low ceilings and wide-board floors in the older part of the house.',
            ],
            'bullets': [
                'Roof pitch, clapboard exposure and trim matched to the original',
                'Connectors that keep the historic house readable',
                'New framing, insulation and egress built to current code',
            ],
        },
        {
            'eyebrow': 'In-law space',
            'h2': 'In-law suites and ADU additions in Ipswich',
            'theme': 'in-law suite addition',
            'paras': [
                'Since February 2025, Massachusetts law allows one accessory dwelling unit of up to 900 square feet by right in single-family zones, subject to local site, health and historic rules. For Ipswich families, that opens the door to an attached in-law suite or a small apartment added to the house, as long as the lot, the septic system where there is one, and any historic review allow it.',
                'DeFaria plans an ADU addition like any other addition in Ipswich, with the extra details a second living unit needs: its own entrance, a kitchenette, fire separation where required and utilities sized for two households.',
            ],
            'bullets': [
                'Attached ADUs up to 900 square feet under the 2025 state law',
                'Separate entrance, kitchenette and fire separation',
                'Septic and historic questions checked first',
            ],
        },
        {
            'eyebrow': 'Step by step',
            'h2': 'From walkthrough to permit: an Ipswich addition in order',
            'theme': 'addition under planning',
            'paras': [
                'Every Ipswich addition starts with a walkthrough of the house and the lot. From there DeFaria checks the things that decide what is possible: preservation restrictions or historic review, flood zone and wetlands on coastal lots, septic capacity when bedrooms are added, and zoning setbacks.',
                'With those answered, the design is finalized, the permit is filed with the Town of Ipswich Building Department, and construction runs through foundation, framing and roof tie-in, the weather-tight shell, rough-in, insulation and finishes, with inspections along the way.',
            ],
            'bullets': [
                'Walkthrough of the house and the lot',
                'Historic, flood, septic and zoning checks',
                'Final design and permit filing',
                'Staged construction with inspections',
            ],
        },
    ],

    ('kitchen-remodeling', 'carlisle'): [
        {
            'eyebrow': 'Layouts',
            'h2': 'Modern kitchen layouts that work in Carlisle homes',
            'theme': 'modern kitchen layout',
            'paras': [
                'The layout matters more than the finish. Most modern kitchens are built around work zones instead of the old triangle alone: a prep zone between the sink and the cooktop, a cooking zone with landing space on both sides, a cleanup zone with the dishwasher next to the sink, and a storage zone close to the pantry and refrigerator.',
                'Clearances make a kitchen comfortable. Kitchen design guidelines from the National Kitchen and Bath Association call for work aisles of about 42 inches for one cook and about 48 inches when two people cook together. In a Carlisle farmhouse, where walls and chimneys sit where they have for generations, the layout is fitted around them; in a contemporary estate there is usually room for a large island with seating on one side and a tall pantry wall that hides small appliances.',
                'Opening a wall to connect the kitchen to a family room is a common request in Carlisle. If the wall is load-bearing, it needs a properly sized beam and a permit, and DeFaria checks that before the layout is promised.',
                'Before the walkthrough, it helps to know a few things: who cooks and how often, whether you want seating at the island or a separate table, which appliances you plan to keep, and what bothers you most about the current kitchen, whether that is storage, light, traffic through the room or the lack of counter space. With those answers, DeFaria can compare two or three layout options for your Carlisle home, show what each one changes in plumbing, electrical and structure, and price the one that fits how you live instead of a generic plan.',
            ],
            'bullets': [
                'Prep, cooking, cleanup and storage zones',
                'Work aisles of about 42 inches, 48 inches for two cooks',
                'Islands with seating and tall pantry walls',
                'Load-bearing walls checked before they are opened',
            ],
        },
        {
            'eyebrow': 'Materials compared',
            'h2': 'Choosing materials for a modern kitchen in Carlisle, MA',
            'theme': 'modern kitchen materials',
            'paras': [
                'Cabinets set the style. Flat-panel doors give the cleanest modern look; a slim shaker is a softer version that fits many older Carlisle homes. Painted finishes show a crisp color, while wood or wood-veneer doors bring warmth that pairs well with beams and wide-plank floors.',
                'Counters are the next big choice. Quartz is engineered, consistent in color and low maintenance. Quartzite and granite are natural stone, harder and more varied, and they need periodic sealing. For a modern kitchen, a simple eased edge and a full-height backsplash in the same stone or in large-format tile keep the look calm.',
                'Lighting finishes the design: ambient light from recessed fixtures, task light under the upper cabinets and over the island, and accent light inside glass cabinets or on open shelves. Warm color temperatures around 2700K to 3000K usually feel right in a home kitchen.',
            ],
            'bullets': [
                'Flat-panel or slim shaker doors, painted or wood',
                'Quartz for low maintenance, quartzite or granite for natural stone',
                'Full-height backsplash in stone or large-format tile',
                'Layered ambient, task and accent lighting',
            ],
        },
        {
            'eyebrow': 'Appliances and ventilation',
            'h2': 'Appliances, ventilation and power for a modern Carlisle kitchen',
            'theme': 'modern kitchen appliances',
            'paras': [
                'Modern kitchens hide as much as they show. Panel-ready refrigerators and dishwashers disappear behind cabinet doors, wall ovens and a speed oven stack in a tall cabinet, and a drawer microwave keeps the counters clear. Each of these needs its own dedicated circuit, so the electrical plan is drawn with the cabinet plan, not after it.',
                'Induction cooktops are a popular choice in modern kitchens because they heat quickly, stay cooler to the touch and are easy to clean. They also need a dedicated high-amperage circuit, and in older Carlisle homes that can mean checking whether the main electrical service has room for it.',
                'Ventilation deserves the same attention. A hood that is ducted to the outside removes heat, grease and moisture far better than a recirculating one. Under the building code adopted in Massachusetts, a kitchen exhaust system rated above 400 cubic feet per minute generally needs a makeup air provision, so larger hoods are planned with that in mind from the start.',
                'Storage finishes the modern look: deep drawers instead of base cabinet doors, a pull-out for trash and recycling next to the sink, organized spice and utensil inserts, and an appliance garage that keeps the coffee maker and mixer out of sight. Charging drawers and outlets inside the island keep phones and small devices off the counter, which helps the room stay as clean-lined in daily use as it looks on the day it is finished.',
            ],
            'bullets': [
                'Panel-ready and integrated appliances on dedicated circuits',
                'Induction cooktops with the electrical service checked first',
                'Ducted range hoods, with makeup air for larger systems',
                'Deep drawers, pull-outs and an appliance garage',
            ],
        },
    ],

    ('remodeling', 'boxford'): [
        {
            'eyebrow': 'Historic Colonials',
            'h2': 'Remodeling a historic Colonial in Boxford',
            'theme': 'remodeled Colonial interior',
            'paras': [
                'Many Boxford homes are historic Colonials, and remodeling them means planning for what is behind the plaster. Homes built before 1978 can have lead paint, so work that disturbs painted surfaces follows lead-safe practices. Older framing may need sistering or leveling, and walls that are opened are a good moment to add insulation and air sealing, which can qualify for Mass Save incentives.',
                'The best Boxford remodels keep the character that makes these houses worth owning, such as wide-board floors, original trim and window placement, while updating kitchens, baths and layouts for how families live now.',
            ],
            'bullets': [
                'Lead-safe practices in homes built before 1978',
                'Framing repair, leveling and insulation while walls are open',
                'Original trim and floors kept where they can be',
            ],
        },
        {
            'eyebrow': 'Well and septic',
            'h2': 'Adding a bathroom or bedroom to a Boxford home on septic',
            'theme': 'remodeled bathroom',
            'paras': [
                'Most Boxford homes use a private well and a septic system. Under Massachusetts Title 5, the septic system is designed around the number of bedrooms, so a remodel that turns an office or attic into a bedroom can trigger a Board of Health review. A new bathroom adds fixtures and water use, so the system and the plumbing layout are checked before the design is final.',
                'Well water can also shape the remodel: filtration or treatment equipment needs space, and older well pumps and pressure tanks are worth checking when a bathroom or kitchen is added. DeFaria covers those questions at the walkthrough so the estimate reflects them.',
            ],
            'bullets': [
                'Bedroom count checked against the septic design',
                'Plumbing and septic reviewed before new bathrooms',
                'Space planned for well water treatment equipment',
            ],
        },
    ],
}

for _key, _secs in _MORE_SECTIONS.items():
    _base = PAGE_OVERRIDES[_key].get('local')
    _base = [_base] if isinstance(_base, dict) else list(_base or [])
    PAGE_OVERRIDES[_key]['local'] = _base + _secs


# ------------------------------------------------------------------ BASEMENT FINISHING (Kevin 2026-10-06)
# Camada local real (so fatos publicos/gerais verificaveis). Gloucester: lider local
# 603basementsolutions com 2.672 palavras e 26 H2 -> secoes de Cape Ann pra superar.
PAGE_OVERRIDES[('basement-finishing', 'gloucester')] = {
    'local': [
        {'eyebrow': 'Cape Ann ledge', 'h2': 'Granite ledge under Gloucester basements',
         'theme': 'finished basement wall',
         'paras': [
             'Gloucester sits on Cape Ann, where granite bedrock runs close to the surface; the Lanesville quarries are part of that history. Many basements here meet ledge along one wall or under the slab, which shapes the layout more than any finish choice.',
             'Ledge matters most for egress windows, drains and a basement bathroom. Cutting rock for a window well or a drain line costs more than digging soil, so we locate ledge at the first walkthrough and plan bedrooms and plumbing where the rock allows.',
         ],
         'bullets': ['Ledge located before the layout is drawn',
                     'Egress wells placed where digging is practical',
                     'Bathroom drains routed to avoid cutting rock where possible']},
        {'eyebrow': 'Flood zones', 'h2': 'Check the flood map before finishing a Gloucester basement',
         'theme': 'dry finished basement',
         'paras': [
             'Parts of Gloucester near the harbor, the Annisquam River and low coastal streets fall inside FEMA flood zones. In a mapped flood zone, finishing a basement below the base flood elevation can be restricted, and a large renovation can count as a substantial improvement that brings the whole house under current flood rules.',
             'Before design we check the flood map for the address and confirm the requirements with the City of Gloucester Inspectional Services, so the project is planned around what the city will approve.',
         ],
         'bullets': ['FEMA flood map checked for the address',
                     'Substantial improvement rules reviewed on large projects',
                     'Flood-resistant materials used low on the walls where they make sense']},
        {'eyebrow': 'Salt air', 'h2': 'Humidity control for coastal Gloucester basements',
         'theme': 'basement living area',
         'paras': [
             'Ocean air keeps humidity high on Cape Ann for much of the year, and a cool basement is where that moisture condenses. A finished basement in Gloucester needs a dehumidification plan, not just insulation.',
             'We size a dehumidifier or a ductless heat pump for the finished space, seal the rim joist and keep foam insulation continuous so warm, damp air never reaches cold concrete.',
         ],
         'bullets': ['Dehumidifier or heat pump sized for the finished space',
                     'Continuous foam so damp air does not touch concrete',
                     'Rim joist sealed against salt-air drafts']},
        {'eyebrow': 'Village homes', 'h2': 'Old cellars in Annisquam, Lanesville and East Gloucester',
         'theme': 'basement with painted beams',
         'paras': [
             'Many 18th and 19th century homes in Annisquam, Lanesville, Rocky Neck and East Gloucester were built over shallow fieldstone cellars that were never meant to be lived in. Some can become storage, laundry or a workshop with a clean finish; others have the height for a real family room.',
             'We measure the clear height, check the stone walls for water and tell you honestly which use fits the cellar you have.',
         ]},
        {'eyebrow': 'Sump pumps', 'h2': 'Where a Gloucester sump pump can discharge',
         'theme': 'utility area in a finished basement',
         'paras': [
             'Massachusetts sewer systems generally do not allow sump pumps or roof drains to discharge into the sanitary sewer, and Gloucester is no exception. Water from a basement sump is routed outside, away from the foundation and neighboring lots.',
             'On tight harbor lots that takes planning, so we design the discharge line, the backup pump and the access panel into the finished walls from the start.',
         ]},
        {'eyebrow': 'Permits', 'h2': 'Permits through Gloucester Inspectional Services',
         'theme': 'basement finishing permit work',
         'paras': [
             'Gloucester is a city, so building, electrical and plumbing permits go through the City of Gloucester Inspectional Services rather than a town building department. Framing, insulation, rough wiring and plumbing are inspected before the walls close.',
             'If the home is in a historic area and the project changes the exterior, such as a new egress window on a street side, we check whether any additional review applies before cutting the foundation.',
         ]},
        {'eyebrow': 'Uses', 'h2': 'How Gloucester families use a finished basement',
         'theme': 'finished basement family room',
         'paras': [
             'In Gloucester we see basements finished as guest space for summer visitors, gear rooms for boats and beach equipment, home offices and workshops. Durable, water-tolerant floors and plenty of storage matter more here than in most inland towns.',
         ],
         'bullets': ['Guest suites for visiting family',
                     'Gear and mudrooms for boats, bikes and beach equipment',
                     'Home offices and studios',
                     'Workshops with good lighting and power']},
    ],
    'faq_extra': [
        ('Can I finish a basement in a Gloucester flood zone?',
         'It depends on the flood zone and the base flood elevation for the address. In some mapped zones, finishing below that elevation is restricted, and large renovations can trigger substantial improvement rules. We check the flood map and confirm with Gloucester Inspectional Services before design.'),
        ('Does ledge make a Gloucester basement more expensive?',
         'It can. Ledge mainly affects egress windows, drains and bathrooms, because cutting rock costs more than digging. We locate it at the walkthrough and plan the layout around it to keep costs down.'),
    ],
}

PAGE_OVERRIDES[('basement-finishing', 'carlisle')] = {
    'local': [
        {'eyebrow': 'Well and septic', 'h2': 'A basement bedroom in Carlisle and the septic system',
         'theme': 'finished basement guest room',
         'paras': [
             'Carlisle has no town water or sewer, so homes here run on a private well and a septic system. Under Massachusetts Title 5, a septic system is designed for a set number of bedrooms. Adding a basement bedroom can raise the bedroom count, which may require a Board of Health review or a system upgrade.',
             'Wells add their own planning: the pressure tank, filtration and the well pump controls usually live in the basement and need clear access after it is finished. We plan a utility room around them instead of boxing them in.',
         ],
         'bullets': ['Bedroom count checked against the septic design',
                     'Board of Health review planned when needed',
                     'Well equipment kept accessible in a utility room']},
    ],
    'faq_extra': [
        ('Can I add a bedroom in my Carlisle basement if I have septic?',
         'Possibly, but the septic system is designed for a set number of bedrooms under Title 5, so a new bedroom may need a Board of Health review or a system upgrade. We check this before design.'),
    ],
}
