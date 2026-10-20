# -*- coding: utf-8 -*-
"""Secao local unica + FAQ extra por cidade para interior-painting e custom-finish-carpentry (Kevin 2026-10-20).

So fatos gerais e verificaveis sobre o tipo de casa da cidade; nenhuma obra, cliente, nota ou preco inventado.
Carregado no fim de page_overrides.py.
"""

def _p(eyebrow, h2, theme, paras, bullets=None):
    d = {'eyebrow': eyebrow, 'h2': h2, 'theme': theme, 'paras': paras}
    if bullets:
        d['bullets'] = bullets
    return d


INTERIOR_OVERRIDES = {}

# ---------------- PINTURA INTERNA ----------------
P = 'interior-painting'
INTERIOR_OVERRIDES[(P, 'arlington')] = {
    'local': [_p('Two-family homes', 'Painting an Arlington two-family or an older Victorian', 'painted stair hall',
        ['A large share of Arlington housing is early 1900s two-family homes, plus Victorians, bungalows and Colonials near Arlington Center and the Heights. Painting one of these usually means a shared front hall and stairway, two kitchens and a lot of original trim, so the job is planned unit by unit with access agreed in advance.',
         'Almost every one of these houses was built before 1978, so sanding or scraping old paint follows lead-safe work practices. If a child under six lives in a pre-1978 rental unit, the Massachusetts Lead Law has its own deleading requirements, and a paint job does not replace that process.'],
        ['Shared halls and stairways scheduled around both units',
         'Lead-safe prep on pre-1978 walls and trim',
         'Old oil-painted trim primed before latex goes on'])],
    'faq_extra': [('Can you paint one unit of my Arlington two-family while the tenants stay?',
        'Yes. We schedule the rooms so each household keeps a working kitchen and bathroom, and shared halls are painted at agreed times.')],
}
INTERIOR_OVERRIDES[(P, 'burlington')] = {
    'local': [_p('Mid-century homes', 'Painting a mid-century Burlington ranch, Cape or split-level', 'painted living space',
        ['Most Burlington homes went up after the 1950s, so a typical repaint is a ranch, Cape or split-level with original plaster or early drywall, open stair landings and builder-grade trim. Split-levels need extra care at the half-flights, where walls are tall and the light changes from level to level.',
         'Textured or popcorn ceilings from that era should be tested before anyone scrapes them, since some older ceiling textures contained asbestos. If the test is clear, we can skim the ceiling smooth before painting; if not, it is handled before any sanding.'],
        ['One color plan across the levels of a split-level',
         'Popcorn ceilings tested before scraping',
         'Early drywall seams and nail pops fixed first'])],
    'faq_extra': [('Can you remove the popcorn ceiling before painting my Burlington home?',
        'Yes, after it is tested. Older textures can contain asbestos, so we test first, then scrape and skim smooth or plan the right abatement before painting.')],
}
INTERIOR_OVERRIDES[(P, 'chelmsford')] = {
    'local': [_p('Chelmsford homes', 'Painting in Chelmsford, from mill-village houses to post-war Colonials', 'painted family room',
        ['Chelmsford has two very different kinds of houses: older homes around Chelmsford Center and the North Chelmsford mill village, and large post-war neighborhoods of Capes, ranches, split-levels and Colonials. The older ones bring plaster and many layers of paint; the newer ones bring tired builder finishes and scuffed halls.',
         'Many Chelmsford families repaint after updating a kitchen or bath, when the new room makes the rest of the house look dated. Planning one palette for the main floor keeps the rooms connected.'],
        ['Plaster and layered paint in older center homes',
         'Washable finishes for busy family halls',
         'One palette for the whole main floor'])],
    'faq_extra': [('Do you paint the whole main floor of a Chelmsford Colonial at once?',
        'We can. Most main floors take about one to two weeks with ceilings and trim, and the rooms are done in an order that keeps the kitchen usable.')],
}
INTERIOR_OVERRIDES[(P, 'concord')] = {
    'local': [_p('Antique homes', 'Painting a Concord antique or Federal house', 'painted antique interior',
        ['Concord has some of the oldest houses in Massachusetts, and many still have original plaster, wide pine trim and paneling under decades of paint. Those surfaces need slower prep than drywall: loose plaster re-secured, cracks taped and old oil paint primed so new paint does not peel.',
         'Concord historic district reviews focus on exterior changes seen from the street, so interior colors are your choice. In an antique home we usually recommend keeping trim profiles crisp instead of filling them with more paint, and testing for lead before any sanding.'],
        ['Original plaster repaired, not covered over',
         'Lead-safe prep on antique trim and doors',
         'Trim profiles kept crisp, not filled with paint'])],
    'faq_extra': [('Do I need historic commission approval to paint inside my Concord house?',
        'Historic district review in Concord deals with exterior changes visible from the street. Interior painting is your decision, but lead-safe prep still applies in older homes.')],
}
INTERIOR_OVERRIDES[(P, 'gloucester')] = {
    'local': [_p('Cape Ann homes', 'Painting a Gloucester home in salt air', 'painted coastal room',
        ['Gloucester homes, from the harbor to Annisquam, Lanesville and Magnolia, live with salt air and humidity. Inside, that shows up as mildew in bathrooms and closets, peeling on window sashes and stains on ceilings under old roof leaks.',
         'We use mildew-resistant, bathroom-rated paint where moisture collects and seal stains before the finish coat. Many Cape Ann cottages were built for summer and later winterized, so walls often mix original boards, plaster and newer drywall that each need their own primer.'],
        ['Mildew-resistant paint in baths and closets',
         'Ceiling stains sealed before painting',
         'Mixed boards, plaster and drywall primed correctly'])],
    'faq_extra': [('What paint holds up in a Gloucester bathroom near the water?',
        'A mildew-resistant, bathroom-rated satin over a proper primer, plus an exhaust fan that actually vents outside. Paint alone cannot fix a room that never dries out.')],
}
INTERIOR_OVERRIDES[(P, 'lexington')] = {
    'local': [_p('Lexington homes', 'Painting a Lexington Colonial or mid-century modern', 'painted modern interior',
        ['Lexington mixes historic Colonials near Lexington Center with mid-century modern neighborhoods such as Five Fields, where many houses have wood paneling, tongue-and-groove ceilings and large windows. In those homes the first question is often what to paint and what to leave natural.',
         'Painting paneling or a wood ceiling is possible, but it needs cleaning, de-glossing and a bonding primer, and it is hard to undo. We often suggest testing a section first and keeping some original wood as a feature.'],
        ['Paneling and wood ceilings primed with a bonding primer',
         'Test sections before committing to paint over wood',
         'Colonial trim and plaster prepped the traditional way'])],
    'faq_extra': [('Can you paint the wood paneling in my Lexington mid-century house?',
        'Yes, with the right prep: cleaning, de-glossing, a bonding primer and two finish coats. We usually test a section first, because painted wood is hard to take back to natural.')],
}
INTERIOR_OVERRIDES[(P, 'marblehead')] = {
    'local': [_p('Old Town homes', 'Painting an Old Town Marblehead house', 'painted older interior',
        ['Old Town Marblehead is full of 18th-century houses with narrow stairs, low ceilings, uneven plaster and doors that are not square. Painting them is detailed work: walls are patched and feathered by hand, and trim is brushed carefully around old hardware and glass.',
         'On Marblehead Neck and near the water, salt air and humidity add mildew and ceiling stains to the list. In every house built before 1978, scraping or sanding old paint follows lead-safe work practices.'],
        ['Hand-feathered patches on uneven plaster',
         'Careful brush work around old hardware',
         'Mildew-resistant paint where humidity collects'])],
    'faq_extra': [('Can you paint the narrow stairway in my Old Town Marblehead house?',
        'Yes. Tight stairways get proper staging so the walls and ceiling can be reached safely, with treads and rails protected the whole time.')],
}
INTERIOR_OVERRIDES[(P, 'weston')] = {
    'local': [_p('Large homes', 'Painting a large Weston home with high ceilings', 'painted large interior',
        ['Many Weston homes are large, with two-story foyers, high ceilings, long stair halls and a lot of trim and paneling. Those rooms need proper staging, more time on ceilings and a clear plan for which rooms are done in which week.',
         'Large houses also benefit most from one consistent white for ceilings and trim and a written color schedule, so every room matches when the job is done.'],
        ['Staging for two-story foyers and stair halls',
         'Written color and sheen schedule room by room',
         'Week-by-week plan for a whole-house repaint'])],
    'faq_extra': [('How long does it take to paint the inside of a large Weston home?',
        'A typical home takes about one to two weeks; larger homes with high ceilings and a lot of trim take longer. You get a room-by-room schedule with the estimate.')],
}
INTERIOR_OVERRIDES[(P, 'wilmington')] = {
    'local': [_p('Wilmington, MA', 'Interior painting in Wilmington, Massachusetts', 'painted family home',
        ['This page is about Wilmington, Massachusetts, in Middlesex County, not Wilmington in Delaware or North Carolina. Most homes here are post-war Capes, ranches, split-levels and Colonials, with plenty of busy family rooms, halls and stairways.',
         'In Capes, the upstairs bedrooms often have sloped ceilings and knee walls where walls and ceiling meet at odd angles, which takes careful cutting in. Families with kids usually choose washable satin or eggshell in halls and mudrooms.'],
        ['Sloped ceilings and knee walls in Capes cut in by hand',
         'Washable finishes for halls and mudrooms',
         'Quick room-by-room schedule for busy families'])],
    'faq_extra': [('Do you work in Wilmington, Massachusetts?',
        'Yes. DeFaria Construction serves Wilmington, MA in Middlesex County, about a half-hour from our base in Lynn.')],
}
INTERIOR_OVERRIDES[(P, 'winchester')] = {
    'local': [_p('Victorian homes', 'Painting a Winchester Victorian or Colonial', 'painted Victorian interior',
        ['Winchester has many late-1800s Victorians and stately Colonials, especially on the West Side and near the town center. These homes have tall ceilings, deep crown, wide casings and sometimes plaster ceiling medallions, all of which take more time to prep and paint than flat drywall.',
         'Original plaster is repaired before painting, and detailed trim is cleaned, sanded and primed so the profiles stay sharp. Because the houses are older than 1978, lead-safe prep applies whenever old paint is disturbed.'],
        ['Tall ceilings and deep crown prepped and painted',
         'Plaster medallions and detailed trim kept sharp',
         'Lead-safe prep on original woodwork'])],
    'faq_extra': [('Can you repaint the detailed trim in my Winchester Victorian without losing the detail?',
        'Yes. Loose paint is removed with lead-safe methods, the profiles are sanded and primed, and the finish is brushed in thin coats so the detail stays crisp.')],
}

# ---------------- BUILT-INS / MARCENARIA FINA ----------------
C = 'custom-finish-carpentry'
INTERIOR_OVERRIDES[(C, 'arlington')] = {
    'local': [_p('Arlington homes', 'Built-ins for Arlington two-families, bungalows and Victorians', 'built-in storage',
        ['Arlington two-family homes and bungalows were built with small closets, so built-ins do a lot of work here: bookcases in living rooms, benches in narrow entries and storage under stairs and eaves.',
         'Many of these houses still have original casing and baseboard. New pieces are trimmed to match, so a built-in looks like it came with the house.'],
        ['Storage in narrow entries and under stairs',
         'Bookcases and benches scaled to smaller rooms',
         'New trim matched to original profiles'])],
    'faq_extra': [('Can you add built-in storage in a small Arlington entry?',
        'Yes. A shallow bench with hooks and cubbies, or a tall narrow cabinet, can fit where a closet will not. We measure the entry and draw it before pricing.')],
}
INTERIOR_OVERRIDES[(C, 'burlington')] = {
    'local': [_p('Mid-century homes', 'Built-ins for Burlington ranches, Capes and split-levels', 'built-in media wall',
        ['Mid-century Burlington homes tend to have small closets and a family room on the lower level of a split-level. Media walls, home office walls and mudroom benches are the most useful built-ins in that layout.',
         'Original builder-grade trim is often thin and plain, so new casing and baseboard can make an older Burlington room look finished without a full remodel.'],
        ['Media walls for split-level family rooms',
         'Home office walls with desk and shelves',
         'Upgraded casing and baseboard over builder-grade trim'])],
    'faq_extra': [('Can new trim make my Burlington ranch look less builder-grade?',
        'Yes. Wider casing, taller baseboard and crown in the main rooms change the look of a mid-century house, and it is mostly a few days of carpentry plus paint.')],
}
INTERIOR_OVERRIDES[(C, 'chelmsford')] = {
    'local': [_p('Chelmsford homes', 'Mudroom benches and built-ins for Chelmsford family homes', 'mudroom built-in',
        ['Many Chelmsford homes are post-war Colonials and split-levels where the family comes in through the garage or the side door, so a mudroom bench with cubbies and hooks is the built-in we would plan first.',
         'Older houses around Chelmsford Center and the North Chelmsford mill village add another job: matching original trim when a wall is opened or a doorway is moved.'],
        ['Mudroom benches with cubbies at the garage door',
         'Matching trim in older center and mill-village homes',
         'Window seats and bookcases for family rooms'])],
    'faq_extra': [('How much does a mudroom bench cost in Chelmsford?',
        'A mudroom bench with cubbies typically runs about $3,000 to $9,000, depending on length, upper cabinets and hooks. You get a fixed price after we measure.')],
}
INTERIOR_OVERRIDES[(C, 'concord')] = {
    'local': [_p('Antique homes', 'Finish carpentry for Concord antique and Federal houses', 'traditional built-in',
        ['Concord antiques often have wide pine floors, original casing and paneling, and walls that have moved for two centuries. New built-ins and trim have to be scribed to those surfaces and match the old profiles so they look original.',
         'Historic district review in Concord concerns exterior changes; interior carpentry is yours to plan, but we treat the old woodwork with the same care, repairing instead of replacing when it can be saved.'],
        ['Built-ins scribed to settled floors and walls',
         'Old casing and paneling repaired before replaced',
         'Profiles matched or milled to order'])],
    'faq_extra': [('Can you repair the original trim in my Concord antique instead of replacing it?',
        'Often, yes. Loose or split pieces can be re-secured, patched and refinished, and only the pieces that cannot be saved are replaced with a matching profile.')],
}
INTERIOR_OVERRIDES[(C, 'gloucester')] = {
    'local': [_p('Cape Ann homes', 'Window seats and built-ins for Gloucester homes', 'window seat built-in',
        ['Gloucester homes, from East Gloucester to Annisquam and Magnolia, often have windows with a view worth sitting at, and a window seat with drawers below is one of the most requested pieces here.',
         'Salt air and humidity mean material choices matter: stable plywood boxes, moisture-resistant panels near baths and entries, and a hard enamel finish that wipes clean.'],
        ['Window seats with storage drawers',
         'Moisture-resistant materials near the water',
         'Hard enamel finish that handles humidity'])],
    'faq_extra': [('What wood holds up for built-ins in a Gloucester house near the ocean?',
        'Stable cabinet-grade plywood boxes, poplar face frames and moisture-resistant panels, sealed and painted with a hard enamel. Solid wood that moves a lot is kept out of damp spots.')],
}
INTERIOR_OVERRIDES[(C, 'lexington')] = {
    'local': [_p('Lexington homes', 'Built-ins for Lexington Colonials and mid-century moderns', 'modern built-in',
        ['In Lexington, built-ins follow the house. Colonials near Lexington Center call for traditional bookcases with face frames and crown; mid-century modern homes in neighborhoods such as Five Fields call for clean, flat-panel pieces, often in natural wood.',
         'We draw the style with you first, so a new piece fits the architecture instead of fighting it.'],
        ['Traditional bookcases with face frames for Colonials',
         'Flat-panel, natural-wood pieces for mid-century homes',
         'Drawings approved before anything is built'])],
    'faq_extra': [('Can you build modern built-ins for my Lexington mid-century house?',
        'Yes. Flat-panel doors, simple pulls and natural wood such as white oak or walnut suit mid-century homes. Stain-grade wood costs more than paint-grade, and you see both prices in the estimate.')],
}
INTERIOR_OVERRIDES[(C, 'marblehead')] = {
    'local': [_p('Old Town homes', 'Fitting built-ins into Old Town Marblehead houses', 'compact built-in',
        ['Old Town Marblehead houses have narrow stairs, low ceilings and rooms that are rarely square, so there is little room to waste. Storage under stairs, shallow bookcases and benches built into alcoves make the most of every inch.',
         'Pieces are measured on site and built to be carried up narrow stairways, then scribed to the walls in place.'],
        ['Under-stair storage and alcove benches',
         'Pieces sized to fit narrow stairways',
         'Scribed to walls that are rarely square'])],
    'faq_extra': [('Can a built-in fit up the narrow stairs of my Old Town Marblehead house?',
        'Yes. We build in sections sized for the stairway and assemble and scribe them in the room.')],
}
INTERIOR_OVERRIDES[(C, 'weston')] = {
    'local': [_p('Large homes', 'Libraries, offices and mudrooms for Weston homes', 'library built-in',
        ['Weston homes often have room for larger pieces: full library walls, home offices with desks and cabinets, and long mudroom runs with lockers and benches. At that size, layout, lighting and outlets need to be planned before the first box is built.',
         'Stain-grade hardwood is more common in these rooms, and it changes both the price and the finishing schedule, so it is decided at the design stage.'],
        ['Full library walls and home offices',
         'Lighting and outlets planned into the drawing',
         'Paint-grade or stain-grade decided up front'])],
    'faq_extra': [('Do you build stain-grade built-ins for a Weston library or office?',
        'Yes. Oak, cherry and walnut are common choices for stained pieces. They cost more than paint-grade poplar or MDF, and both options are priced in the estimate.')],
}
INTERIOR_OVERRIDES[(C, 'wilmington')] = {
    'local': [_p('Wilmington, MA', 'Built-ins for Wilmington, Massachusetts Capes and ranches', 'knee-wall storage',
        ['This page is about Wilmington, Massachusetts, in Middlesex County, not Wilmington in Delaware or North Carolina. Many homes here are Capes with sloped upstairs ceilings and knee walls, where built-in drawers and cabinets turn dead space into storage.',
         'Ranches and split-levels gain the most from mudroom benches and basement shelving, since closets in post-war homes are small.'],
        ['Knee-wall drawers and cabinets in Cape bedrooms',
         'Mudroom benches for busy entries',
         'Basement shelving for storage'])],
    'faq_extra': [('Can you build storage into the knee walls of my Wilmington Cape?',
        'Yes. Drawers or small cabinets can be built into the knee walls of upstairs bedrooms, framed and trimmed to look like part of the room.')],
}
INTERIOR_OVERRIDES[(C, 'winchester')] = {
    'local': [_p('Victorian homes', 'Bookcases and trim for Winchester Victorians and Colonials', 'fireplace bookcases',
        ['Winchester Victorians and Colonials, especially on the West Side, often have a fireplace flanked by bare walls and tall ceilings with deep crown. Bookcases on each side of the fireplace, with face frames and crown that match the room, are the classic built-in here.',
         'Original trim in these homes is usually more detailed than anything sold today, so new pieces are built up or milled to match the existing profiles.'],
        ['Bookcases on each side of the fireplace',
         'Crown and face frames matched to the room',
         'Detailed profiles built up or milled to order'])],
    'faq_extra': [('Can you build bookcases around the fireplace in my Winchester home?',
        'Yes. A pair of built-in bookcases often runs about $4,000 to $15,000, depending on size, doors and drawers and wood. We match the crown and trim of the room.')],
}


# ---- rodada 3 (lider da SERP com 3.800 a 4.300 palavras): segunda secao local ----
INTERIOR_OVERRIDES[(P, 'burlington')]['local'] += [
    _p('Paneling and soffits', 'Painting 1960s paneling, soffits and family rooms in Burlington', 'painted family room',
       ['Many Burlington family rooms and basements from the 1960s and 1970s still have dark wood or veneer paneling, kitchen soffits over the cabinets and low ceilings with a single light. Painting changes these rooms more than any other single project, but paneling needs the right prep: cleaning, de-glossing, a bonding primer and, if the grooves bother you, filling them before the finish coats.',
        'Soffits and low ceilings look better in a flat, bright white, and the paneling can go a warm white or a soft color that makes the room feel taller. If the paneling is damaged or loose, it is often faster to remove it and hang new drywall, which our carpenters can do in the same project.',
        'Split-levels add one more detail: the half-flight stair walls are tall and visible from two levels, so we plan them as one surface with one color, and set up staging so the walls are reached safely without leaning ladders on fresh paint.'],
       ['Paneling cleaned, de-glossed and primed before paint',
        'Grooves filled when you want a smooth wall',
        'Soffits and low ceilings in a bright flat white',
        'Damaged paneling replaced with drywall when it makes sense']),
    _p('Planning the week', 'How a Burlington whole-house repaint is scheduled', 'room by room schedule',
       ['A typical Burlington ranch or Cape can have its main rooms painted in about a week, and a full interior in one to two weeks. The order matters as much as the speed: bedrooms are usually done first while the family uses the kitchen and living room, then the shared rooms, and the halls and stairway last so nothing gets bumped after it is finished.',
        'Each day ends with the rooms you need put back together. Furniture is moved to the center and covered rather than carried out of the house, and anything fragile is boxed by you before the crew starts in that room. The schedule is written into the estimate, so you know which rooms are out of use on which days.'],
       ['Bedrooms first, shared rooms next, halls and stairs last',
        'Rooms in use put back together every evening',
        'Written schedule with the estimate']),
]
INTERIOR_OVERRIDES[(P, 'burlington')]['faq_extra'] += [
    ('Can you paint the wood paneling in my Burlington family room?',
     'Yes. Paneling is cleaned, de-glossed and primed with a bonding primer, then painted with two finish coats. If you want a smooth wall, the grooves can be filled first, or the paneling can be replaced with drywall.'),
    ('How long does it take to paint a Burlington ranch?',
     'The main rooms of a typical ranch or Cape take about a week, and a full interior about one to two weeks, depending on repairs, ceilings and trim.'),
]
INTERIOR_OVERRIDES[(P, 'weston')]['local'] += [
    _p('Fine finishes', 'Paneled libraries, wainscoting and detailed millwork in Weston homes', 'detailed millwork',
       ['Weston homes often have more millwork than a typical house: paneled libraries and studies, wainscoting in dining rooms, built-in bookcases, coffered ceilings and long runs of crown. Painting these surfaces is closer to furniture finishing than wall painting. Every panel edge is sanded, every joint is caulked where it should be and left crisp where it should not, and the enamel is applied in thin coats so it levels without runs.',
        'Stained woodwork is a separate decision. Some owners want to keep a natural library or a stained staircase rail and paint around it; others want to paint it for a lighter look. Painting stained wood is permanent in practice, so we test a hidden spot and talk through the result before committing.',
        'Where the finish level is high, we also recommend a written color and sheen schedule for the whole house, with one ceiling white and one trim white, so rooms painted weeks apart still match perfectly.'],
       ['Paneling and millwork sanded, caulked and enameled in thin coats',
        'Stained wood tested before any decision to paint it',
        'One ceiling white and one trim white through the house',
        'Color and sheen schedule written room by room']),
    _p('Large-home logistics', 'Painting a large Weston house without taking over the home', 'large home logistics',
       ['A whole-house repaint in a large Weston home is planned like a small project: which wing first, where the crew sets up a paint station that is protected from floors and rugs, how furniture and art are handled, and which rooms stay untouched until the end.',
        'We usually work one zone at a time, so the rest of the house stays in normal use. Art and mirrors are taken down and labeled by room, large furniture is moved to the center of the room and covered, and floors are protected along every path the crew uses, not only inside the room being painted. At the end of each zone there is a walkthrough before the crew moves on, so touch-ups are done while the materials are still out.'],
       ['Work in zones so the rest of the house stays usable',
        'Art and mirrors labeled and stored by room',
        'Floors protected along every crew path',
        'Walkthrough at the end of each zone']),
]
INTERIOR_OVERRIDES[(P, 'weston')]['faq_extra'] += [
    ('Can you paint stained woodwork in my Weston home?',
     'Yes, with a cleaning, de-glossing and bonding primer step. Because painted wood is hard to return to a stained finish, we test a hidden spot first and agree on the result before painting.'),
    ('Do you move furniture and art before painting?',
     'Yes. Art and mirrors are taken down and labeled by room, large furniture is moved to the center and covered, and everything goes back in place at the end of each room.'),
]
INTERIOR_OVERRIDES[(P, 'winchester')]['local'] += [
    _p('Stair halls', 'Painting tall stair halls and entry halls in Winchester Victorians', 'painted stair hall',
       ['The entry and stair hall of a Winchester Victorian is often the tallest painted space in the house, with a long run of wall, a staircase with turned balusters and a ceiling that cannot be reached from a normal ladder. It is also the first room guests see, so it is worth doing right.',
        'We build proper staging over the stairs, protect the treads and the rail, and paint from the top down: ceiling, then the high walls, then the lower walls, trim and balusters by hand. Old plaster in these halls often has long settlement cracks along the stair line, which are taped and filled before painting so they do not reappear the first winter.'],
       ['Staging built over the stairs for safe access',
        'Settlement cracks along the stair line taped and filled',
        'Balusters and rail painted by hand',
        'Ceiling to floor, top down']),
]
INTERIOR_OVERRIDES[(P, 'winchester')]['faq_extra'] += [
    ('Can you paint the tall stair hall in my Winchester house?',
     'Yes. We build staging over the stairs, protect the treads and rail and paint from the ceiling down, with cracks along the stair line repaired before painting.'),
]
INTERIOR_OVERRIDES[(P, 'wilmington')]['local'] += [
    _p('Busy family homes', 'Repainting a busy Wilmington family home room by room', 'family home painting',
       ['Many Wilmington homes are full family houses with kids, pets and a lot of traffic through the halls, kitchen and stairway. Repainting them usually means choosing finishes that wash well, fixing the dings and nail pops that years of use leave behind, and scheduling so bedrooms are back in use by bedtime.',
        'Satin or a scrubbable eggshell in halls, mudrooms and kids\' rooms makes fingerprints easy to clean, and semi-gloss enamel on doors and trim stands up to bumps. We leave labeled touch-up paint for every room so small marks can be fixed in minutes later.'],
       ['Scrubbable finishes in halls and kids\' rooms',
        'Enamel on doors and trim for bumps',
        'Bedrooms back in use by the end of the day',
        'Labeled touch-up paint left for every room']),
]
INTERIOR_OVERRIDES[(P, 'wilmington')]['faq_extra'] += [
    ('What paint finish is best for kids\' rooms and halls in Wilmington?',
     'A scrubbable satin or eggshell on the walls and a semi-gloss enamel on doors and trim. Both clean up well, and we leave labeled touch-up paint for later.'),
]


# ---- rodada 4: terceira secao local nas 4 cidades com lider mais longo ----
INTERIOR_OVERRIDES[(P, 'burlington')]['local'] += [
    _p('Kitchen cabinets', 'Painting original kitchen cabinets in a Burlington home', 'painted kitchen cabinets',
       ['A lot of Burlington kitchens still have solid wood cabinets from the 1960s, 70s or 80s with a dated stain or a worn finish. When the boxes are sound and the layout works, painting them is a big change for a fraction of the cost of new cabinets, usually about $4,000 to $9,000 for a kitchen.',
        'Older cabinets often have years of grease near the range and an oil-based or lacquer finish, so cleaning and a bonding primer are the steps that decide whether the paint lasts. New hinges and pulls are easiest to change at the same time, while the doors are off. If the boxes are water damaged or the layout does not work for you, we will say so and price a kitchen remodel instead.'],
       ['Degreased and primed with a bonding primer',
        'Hard cabinet enamel for daily use',
        'Hinges and pulls swapped while the doors are off']),
]
INTERIOR_OVERRIDES[(P, 'weston')]['local'] += [
    _p('Around fine finishes', 'Painting around stone, custom cabinetry and hardwood in Weston', 'protected fine finishes',
       ['Weston interiors often include natural stone counters and fireplace surrounds, custom cabinetry, wide-plank hardwood and expensive fixtures. Painting next to them is mostly about protection: floors are covered with breathable runners along every path, stone and cabinetry are masked with tape that will not lift finishes, and light fixtures are bagged or taken down.',
        'Clean, sharp lines where paint meets stone, tile or stained wood are cut by hand. At the end of each room, the protection comes off carefully and every surface is checked before the furniture goes back.'],
       ['Breathable floor runners along every crew path',
        'Low-tack masking on stone, cabinetry and stained wood',
        'Fixtures bagged or taken down',
        'Hand-cut lines at stone and tile']),
]
INTERIOR_OVERRIDES[(P, 'winchester')]['local'] += [
    _p('Original woodwork', 'Original woodwork in Winchester homes: paint, strip or keep it stained?', 'original woodwork',
       ['Some Winchester Victorians still have original stained woodwork, while others have trim that has been painted many times. If the wood is still stained, painting it is a permanent choice, so we talk about it first. If it has already been painted, the usual goal is to keep the profiles sharp instead of adding more layers that soften the detail.',
        'Where old paint is thick, cracked or peeling, it is removed with lead-safe methods before priming. Stripping trim back to bare wood is possible but slow and costly, so it is usually saved for the most visible pieces, such as a front door, a mantel or the newel post.'],
       ['Stained wood kept or painted only after a test',
        'Thick, failing paint removed with lead-safe methods',
        'Stripping saved for the most visible pieces']),
]
INTERIOR_OVERRIDES[(P, 'wilmington')]['local'] += [
    _p('Floors and paint', 'Painting before or after new floors in a Wilmington home', 'paint and new floors',
       ['If new flooring is planned, paint the walls and ceilings first and install the floors after, then finish with the baseboard and a final trim coat. That way no paint drips land on new floors, and the baseboard is painted where it meets the finished floor height.',
        'If the floors are being refinished instead, sanding creates fine dust, so the floor work is done first and the final wall coat comes after. We coordinate both schedules so you are not out of the rooms twice.'],
       ['Walls and ceilings before new floors',
        'Baseboard set and painted last',
        'Floor refinishing first, final wall coat after']),
]


# ---- rodada 5: FAQ local extra ----
INTERIOR_OVERRIDES[(P, 'burlington')]['faq_extra'] += [
    ('Should I paint or replace the 1970s kitchen cabinets in my Burlington house?',
     'If the boxes are solid, dry and the layout works, painting is usually the better value at about $4,000 to $9,000 for a kitchen. If they are water damaged, sagging or the layout does not work for you, a remodel makes more sense, and we will tell you which at the walkthrough.'),
    ('Do you paint split-level stairwells in Burlington?',
     'Yes. The tall half-flight walls are painted from proper staging as one surface, with one color carried across both levels so the stairway looks continuous.'),
]
INTERIOR_OVERRIDES[(P, 'weston')]['faq_extra'] += [
    ('How do you protect stone and custom cabinets while painting in Weston?',
     'Floors get breathable runners along every path, stone, cabinetry and stained wood are masked with low-tack tape, fixtures are bagged or removed, and the lines where paint meets stone or tile are cut by hand.'),
    ('Can you paint one wing of a large Weston home at a time?',
     'Yes. Large homes are usually painted in zones, so the rest of the house stays in normal use, with a walkthrough at the end of each zone before the crew moves on.'),
]
INTERIOR_OVERRIDES[(P, 'winchester')]['faq_extra'] += [
    ('Should I paint the original stained trim in my Winchester Victorian?',
     'It is your call, but it is permanent in practice. We test a hidden spot, show you the result and only then paint. Many owners keep stained wood in the entry or library and paint the trim in bedrooms and baths.'),
    ('Is lead paint a concern in Winchester homes?',
     'Most Winchester homes were built before 1978, so any sanding or scraping of old paint follows lead-safe work practices with containment and careful cleanup.'),
]

INTERIOR_OVERRIDES[(P, 'weston')]['faq_extra'] += [
    ('Do you leave touch-up paint after painting a Weston home?',
     'Yes. Every color and sheen is written down for you, and leftover paint is sealed and labeled by room, so future touch-ups on walls, trim and doors match the original job.'),
]


# ---- rodada 6: built-ins Lexington (lider tinosinc.com com 3.985 palavras na leitura de 20/10) ----
INTERIOR_OVERRIDES[(C, 'lexington')]['local'] += [
    _p('Mid-century modern', 'Built-ins for Lexington mid-century modern homes', 'mid-century built-in',
       ['Mid-century modern houses in Lexington neighborhoods such as Five Fields were designed with long, low lines, large windows, exposed beams and a lot of natural wood. Built-ins that suit them follow the same ideas: long, low credenzas under windows, wall units with flat slab doors, floating shelves between posts, and simple pulls or finger grooves instead of ornate hardware.',
        'Natural wood such as white oak or walnut is common in these pieces, often with a clear matte finish that lets the grain show. Because many of these homes have post-and-beam framing and large glass walls, there is less solid wall to attach to, so the layout is planned around where the framing actually is.',
        'When a mid-century house already has original built-ins, we can repair and extend them instead of replacing them, matching the wood and the reveal lines so the new section reads as part of the original design.'],
       ['Long, low credenzas and wall units with slab doors',
        'White oak or walnut with a clear matte finish',
        'Layout planned around post-and-beam framing',
        'Original built-ins repaired and extended when possible']),
    _p('Colonial built-ins', 'Built-ins for Lexington Colonials near the center', 'colonial bookcases',
       ['Colonials near Lexington Center and in the older neighborhoods around it call for a more traditional look: painted bookcases with face frames, raised or recessed panel doors below, crown molding at the top that matches the room, and window seats tucked into dormers or bays.',
        'These homes often have plaster walls and floors that have settled, so cabinets are scribed tight to the wall and the base is leveled with a toe kick that follows the floor. The finish is a hard enamel in the same white as the room trim, so the built-in looks like it was always there.',
        'Popular projects in these houses are bookcases on each side of the fireplace, a mudroom bench at the side or back door, and a home office wall in a spare bedroom.'],
       ['Painted bookcases with face frames and panel doors',
        'Crown matched to the existing room trim',
        'Scribed to plaster walls and settled floors',
        'Window seats in dormers and bays']),
    _p('Planning', 'Planning a Lexington built-in: from first visit to install day', 'planning a built-in',
       ['Most Lexington built-in projects start with a walkthrough where we measure the wall, check for outlets, heating registers, windows and the direction of the floor framing, and talk about what the piece needs to hold. That conversation decides depth, shelf spacing and whether doors or drawers make more sense than shelves without doors.',
        'Next comes a drawing with dimensions and a fixed, itemized price, then material and finish selection. The boxes, doors and drawers are built and dry-fitted in the shop, so the time in your home is usually a few days for installation and finishing. Heating registers and outlets that fall inside the new piece are relocated or extended so nothing is blocked.'],
       ['Measurements, outlets and registers checked first',
        'Drawing with dimensions and a fixed price',
        'Built in the shop, installed in a few days',
        'Registers and outlets moved or extended as needed']),
]
INTERIOR_OVERRIDES[(C, 'lexington')]['faq_extra'] += [
    ('Can you match the original built-ins in my Lexington mid-century house?',
     'Usually, yes. We match the wood species, finish and reveal lines, and when the original pieces are repairable we extend them instead of replacing them.'),
    ('How long does a built-in take in Lexington?',
     'Most bookcases, window seats or mudroom benches take one to three weeks from approved drawing to finished, with only a few days of installation and finishing in your home.'),
]
