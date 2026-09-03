const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const SITE = 'https://www.defariaconstruction.com';
const PHONE = '+16178932221';
const PHONE_LABEL = '(617) 893-2221';
const SERVICE = 'kitchen-remodeling';
const TODAY = '2026-09-03';

const cities = [
  {
    name: 'Acton',
    article: 'an',
    slug: 'acton',
    county: 'Middlesex County',
    zips: ['01718', '01720'],
    areas: ['West Acton', 'South Acton', 'Acton Center', 'North Acton', 'East Acton'],
    homeStyle: 'colonials, capes and newer family homes',
    localIntent: 'many homeowners want a Kitchen Remodel that opens the room up without losing storage or making the main floor feel patched together',
    cabinetAngle: 'cabinet layout, pantry space and appliance placement usually have to be solved before finishes are selected',
    islandAngle: 'a Kitchen Island often needs to work as prep space, homework space and casual seating instead of just a visual centerpiece',
    permitAngle: 'scope, sequencing and inspections should be discussed early when walls, plumbing or electrical work may change',
    searchAngle: 'kitchen remodel contractor in Acton MA'
  },
  {
    name: 'Ayer',
    article: 'an',
    slug: 'ayer',
    county: 'Middlesex County',
    zips: ['01432'],
    areas: ['Ayer Center', 'Devens area', 'Groton Road corridor', 'Sandy Pond area'],
    homeStyle: 'older village homes, compact layouts and practical single-family properties',
    localIntent: 'the right Kitchen Remodel usually starts with better circulation, stronger storage and a finish plan that does not overcomplicate the home',
    cabinetAngle: 'Kitchen Cabinets can change the whole feel of a smaller footprint when drawer banks, uppers and corners are planned together',
    islandAngle: 'not every Ayer kitchen needs a large island, but the prep zone and seating plan still need a clear answer',
    permitAngle: 'a measured walkthrough helps separate cosmetic updates from electrical, plumbing or layout changes',
    searchAngle: 'contractor for kitchen remodel in Ayer MA'
  },
  {
    name: 'Bedford',
    article: 'a',
    slug: 'bedford',
    county: 'Middlesex County',
    zips: ['01730'],
    areas: ['Bedford Center', 'Hartwell Road area', 'Great Road corridor', 'Fawn Lake area'],
    homeStyle: 'well-kept single-family homes where finish quality and daily function both matter',
    localIntent: 'homeowners comparing a Kitchen Remodel Near Me usually want proof that the contractor can manage layout, Cabinets and finish work without vague allowances',
    cabinetAngle: 'Kitchen Cabinets should be measured around storage habits, appliance clearances and the way the room connects to dining or living space',
    islandAngle: 'a Kitchen Island can anchor the room only if the walkway, lighting and countertop dimensions are planned together',
    permitAngle: 'Bedford projects benefit from confirming the real scope before materials drive the budget',
    searchAngle: 'kitchen remodel near me Bedford MA'
  },
  {
    name: 'Burlington',
    article: 'a',
    slug: 'burlington',
    county: 'Middlesex County',
    zips: ['01803', '01805'],
    areas: ['Burlington Center', 'Fox Hill', 'Mill Pond area', 'Cambridge Street corridor'],
    homeStyle: 'busy family homes, ranches, splits and updated properties near major commuter routes',
    localIntent: 'Burlington homeowners often search for a Kitchen Remodel Contractor because the kitchen has to support traffic, storage and everyday meals at the same time',
    cabinetAngle: 'Cabinets, countertops and backsplash choices should be coordinated before demolition so the project does not stall midstream',
    islandAngle: 'a Kitchen Island needs enough clearance to improve the room, not turn the center walkway into a bottleneck',
    permitAngle: 'planning should account for electrical, lighting and plumbing changes before the finish schedule is promised',
    searchAngle: 'kitchen remodel contractor Burlington MA'
  },
  {
    name: 'Carlisle',
    article: 'a',
    slug: 'carlisle',
    county: 'Middlesex County',
    zips: ['01741'],
    areas: ['Carlisle Center', 'Great Brook Farm area', 'East Street area', 'Concord Street corridor'],
    homeStyle: 'larger homes, rural settings and projects where the kitchen needs to feel intentional rather than rushed',
    localIntent: 'a Kitchen Remodel in Carlisle often has to balance refined finishes with practical construction planning',
    cabinetAngle: 'custom-feeling Kitchen Cabinets, trim transitions and hardware details matter when the kitchen connects to more formal living areas',
    islandAngle: 'a Kitchen Island can become the main gathering point, but it should be sized around circulation and sightlines',
    permitAngle: 'clear scope helps homeowners understand what is cosmetic and what requires deeper coordination',
    searchAngle: 'kitchen remodel Carlisle MA'
  },
  {
    name: 'Chelmsford',
    article: 'a',
    slug: 'chelmsford',
    county: 'Middlesex County',
    zips: ['01824', '01863', '01884'],
    areas: ['Chelmsford Center', 'North Chelmsford', 'South Chelmsford', 'Westlands', 'Drum Hill area'],
    homeStyle: 'ranches, colonials, split-level homes and active family kitchens',
    localIntent: 'Chelmsford homeowners usually want a Kitchen Remodel that modernizes layout, storage and lighting without turning the project into a guessing game',
    cabinetAngle: 'Kitchen Cabinets should be planned with countertop space, appliance locations and daily storage routines in one conversation',
    islandAngle: 'a Kitchen Island can add seating and prep space when the room has enough clearance for comfortable movement',
    permitAngle: 'the estimate should explain the work behind the finishes, especially if lighting, plumbing or walls are changing',
    searchAngle: 'kitchen remodel contractor Chelmsford MA'
  },
  {
    name: 'Concord',
    article: 'a',
    slug: 'concord',
    county: 'Middlesex County',
    zips: ['01742'],
    areas: ['Concord Center', 'West Concord', 'Nine Acre Corner', 'Thoreau Street area'],
    homeStyle: 'historic homes, carefully maintained properties and additions where finish transitions need extra attention',
    localIntent: 'a Kitchen Remodel in Concord should respect the home while still improving storage, lighting and the way the room works every day',
    cabinetAngle: 'Cabinets, millwork details and trim lines need to look like they belong with the rest of the house',
    islandAngle: 'a Kitchen Island should feel proportionate to the room instead of overpowering older floor plans',
    permitAngle: 'older homes call for a contractor who looks behind the visible surfaces before promising a simple update',
    searchAngle: 'contractor for kitchen remodel Concord MA'
  },
  {
    name: 'Dracut',
    article: 'a',
    slug: 'dracut',
    county: 'Middlesex County',
    zips: ['01826'],
    areas: ['Dracut Center', 'Collinsville', 'Navy Yard', 'Parker Village area'],
    homeStyle: 'family homes where durability, storage and budget clarity usually drive the conversation',
    localIntent: 'people searching Kitchen Remodel Near Me in Dracut are often trying to compare realistic contractors, not just collect design ideas',
    cabinetAngle: 'Kitchen Cabinets, counters and flooring should be priced with the real scope of work, not separated into unclear pieces',
    islandAngle: 'a Kitchen Island can help if it improves prep flow, seating and storage without crowding the room',
    permitAngle: 'a practical walkthrough helps identify electrical, plumbing and surface work before the project starts',
    searchAngle: 'kitchen remodel near me Dracut MA'
  },
  {
    name: 'Dunstable',
    article: 'a',
    slug: 'dunstable',
    county: 'Middlesex County',
    zips: ['01827'],
    areas: ['Dunstable Center', 'Main Street area', 'Mill Street area', 'Groton border area'],
    homeStyle: 'quiet residential homes and larger properties where kitchens often connect to family gathering spaces',
    localIntent: 'a Kitchen Remodel in Dunstable should make the home easier to use while keeping the finish level controlled',
    cabinetAngle: 'Cabinets and storage planning matter when the kitchen has to support groceries, cooking tools and everyday family routines',
    islandAngle: 'a Kitchen Island may need to support both prep and conversation, especially in homes with open dining connections',
    permitAngle: 'DeFaria starts with scope clarity so the homeowner knows which work is cosmetic and which work is deeper construction',
    searchAngle: 'kitchen remodel Dunstable MA'
  },
  {
    name: 'Groton',
    article: 'a',
    slug: 'groton',
    county: 'Middlesex County',
    zips: ['01450', '01471'],
    areas: ['Groton Center', 'West Groton', 'Forge Village edge', 'Lost Lake area'],
    homeStyle: 'historic properties, rural homes and family kitchens with older layouts',
    localIntent: 'Groton homeowners looking for a Contractor for Kitchen Remodel usually need someone who can see structure, storage and finish decisions together',
    cabinetAngle: 'Kitchen Cabinets should fit the architecture and the daily routine instead of forcing a showroom layout into the home',
    islandAngle: 'a Kitchen Island works best when the traffic path between sink, range, refrigerator and seating is protected',
    permitAngle: 'older layouts benefit from checking the hidden conditions before finalizing the cabinet and counter package',
    searchAngle: 'contractor for kitchen remodel Groton MA'
  },
  {
    name: 'Hudson',
    article: 'a',
    slug: 'hudson',
    county: 'Middlesex County',
    zips: ['01749'],
    areas: ['Downtown Hudson', 'Gleasondale', 'Wood Square', 'Main Street corridor'],
    homeStyle: 'older homes, updated condos and busy kitchens near a growing downtown',
    localIntent: 'Hudson homeowners often want a Kitchen Remodel that makes cooking, storage and entertaining easier without losing control of cost',
    cabinetAngle: 'Kitchen Cabinets, counters, backsplash and flooring need a clear sequence so the finish stage does not feel improvised',
    islandAngle: 'a Kitchen Island can be useful for entertaining, but it should be planned around real walking paths and appliance doors',
    permitAngle: 'the estimate should make allowances, material selections and construction steps easy to compare',
    searchAngle: 'kitchen remodel contractor Hudson MA'
  },
  {
    name: 'Lexington',
    article: 'a',
    slug: 'lexington',
    county: 'Middlesex County',
    zips: ['02420', '02421'],
    areas: ['Lexington Center', 'East Lexington', 'Munroe Hill', 'Follen Heights', 'Pierce-Lockwood area'],
    homeStyle: 'high-value homes where finish detail, layout logic and contractor communication carry real weight',
    localIntent: 'a Kitchen Remodel Contractor in Lexington has to show planning discipline before homeowners trust the disruption',
    cabinetAngle: 'Kitchen Cabinets, panel details, storage inserts and appliance placement should be treated as part of one finish plan',
    islandAngle: 'a Kitchen Island should support cooking, seating and hosting while matching the scale of the room',
    permitAngle: 'detailed preconstruction planning helps avoid surprises once older walls, wiring or plumbing are opened',
    searchAngle: 'kitchen remodel contractor Lexington MA'
  },
  {
    name: 'Lincoln',
    article: 'a',
    slug: 'lincoln',
    county: 'Middlesex County',
    zips: ['01773'],
    areas: ['Lincoln Center', 'Lincoln Station', 'Silver Hill', 'Farrar Pond area'],
    homeStyle: 'architectural homes, quieter residential streets and kitchens where restraint matters',
    localIntent: 'Lincoln homeowners often want a Kitchen Remodel that feels thoughtful, useful and consistent with the home instead of overbuilt',
    cabinetAngle: 'Cabinets, trim, lighting and material transitions should feel calm and precise',
    islandAngle: 'a Kitchen Island can add utility only when its size, outlets, seating and surrounding clearance are resolved early',
    permitAngle: 'the project should be mapped before demolition so hidden work and visible details stay connected',
    searchAngle: 'kitchen remodel Lincoln MA'
  },
  {
    name: 'Littleton',
    article: 'a',
    slug: 'littleton',
    county: 'Middlesex County',
    zips: ['01460'],
    areas: ['Littleton Common', 'Nagog Hill area', 'Spectacle Pond area', 'King Street corridor'],
    homeStyle: 'family homes and commuter-area properties where kitchens need better daily flow',
    localIntent: 'a Littleton Kitchen Remodel often starts with the same search intent: better Cabinets, better layout and a contractor who can make the estimate clear',
    cabinetAngle: 'Kitchen Cabinets should improve storage without creating awkward corners, blocked doors or wasted counter space',
    islandAngle: 'a Kitchen Island can be the right move when it improves prep, serving and seating without crowding the work triangle',
    permitAngle: 'a clear construction sequence keeps plumbing, electrical and finish work from competing for attention',
    searchAngle: 'kitchen remodel near me Littleton MA'
  },
  {
    name: 'Maynard',
    article: 'a',
    slug: 'maynard',
    county: 'Middlesex County',
    zips: ['01754'],
    areas: ['Downtown Maynard', 'Maynard Center', 'Presidential Village', 'Assabet River area'],
    homeStyle: 'compact homes, older kitchens and practical layouts where every cabinet run has to earn its place',
    localIntent: 'Maynard homeowners searching for a Kitchen Remodel Near Me usually want a practical contractor who can improve storage, lighting and finishes without inflating the scope',
    cabinetAngle: 'Kitchen Cabinets, drawer storage and wall cabinets should be designed around the footprint instead of copying a larger kitchen',
    islandAngle: 'a Kitchen Island may be smaller or movable in tighter Maynard homes, but the same planning discipline still matters',
    permitAngle: 'the estimate should explain what changes the room functionally and what is mainly cosmetic',
    searchAngle: 'kitchen remodel near me Maynard MA'
  }
];

const intros = [
  'This page is built for homeowners with hiring intent, not for people casually browsing photos. It connects the city, ZIP code area and kitchen scope to a direct estimate path.',
  'A local kitchen page needs to answer the first comparison questions quickly: what can be changed, who coordinates the details and how the work stays organized inside an active home.',
  'The goal is to help a homeowner move from search to a useful conversation about layout, Cabinets, surfaces, lighting, budget and timeline.',
  'Instead of repeating a generic service page, this city page explains what makes the local kitchen remodel conversation more specific.'
];

const scopeOpeners = [
  'A full Kitchen Remodel is more than a new finish package.',
  'A kitchen project becomes easier to manage when the construction order is clear before material decisions pile up.',
  'The visible result depends on decisions made before cabinets and counters arrive.',
  'Strong kitchen remodeling starts with the way the room is used every day.'
];

const finalAngles = [
  'For homeowners comparing a Kitchen Remodel Contractor, the deciding factor is often whether the contractor can connect design choices to construction reality.',
  'For searches like Kitchen Remodel Near Me, this page gives DeFaria a focused local answer instead of sending every visitor to one broad service page.',
  'For someone looking for a Contractor for Kitchen Remodel, the page makes the offer specific: owner-led planning, real project photos and clear scope before work starts.',
  'For homeowners researching Cabinets, Kitchen Cabinets and island planning, the page frames those choices as part of the remodel, not detached shopping decisions.'
];

const scopeClosers = [
  'Lighting, flooring, backsplash, plumbing and electrical work are sequenced so the Acton-area style of project does not get reduced to disconnected finish choices.',
  'Material ordering, surface prep and finish coordination are mapped before the Ayer kitchen loses daily use.',
  'Bedford kitchens need the unseen parts of the project to line up with the visible cabinet and counter decisions.',
  'Burlington projects move more cleanly when flooring, lighting and rough-in decisions are locked before finish materials arrive.',
  'Carlisle kitchen work should connect quieter finish details with the practical order of construction.',
  'Chelmsford remodels need lighting, flooring, backsplash and rough-in work organized around family use, not just a product list.',
  'Concord projects benefit from sequencing that respects older conditions while still delivering a finished modern kitchen.',
  'Dracut kitchens need a practical order for flooring, counters, backsplash, lighting and rough-in work so budget and timing stay readable.',
  'Dunstable homeowners get a clearer estimate when the finish package is tied to the construction sequence from the start.',
  'Groton kitchens often need careful alignment between older structure, new cabinetry and the surfaces that finish the room.',
  'Hudson projects should connect traffic flow, storage and surface selections before the kitchen becomes unavailable.',
  'Lexington remodels need a finish sequence detailed enough to match higher expectations around Cabinets, lighting and trim.',
  'Lincoln kitchen work should feel calm and deliberate, with surfaces and rough-in decisions planned before demolition.',
  'Littleton projects benefit when storage, lighting, flooring and backsplash decisions are organized around everyday family use.',
  'Maynard kitchens need compact-space decisions sequenced carefully so Cabinets, counters and lighting all support the same footprint.'
];

const experienceAngles = [
  'Acton searches usually reward detail: the homeowner wants to know how the kitchen will function after the remodel, not only how it photographs.',
  'Ayer homeowners often need a contractor who can keep the scope practical while still improving storage and finish quality.',
  'Bedford visitors compare professionalism quickly, so the page has to show scope clarity before asking for a call.',
  'Burlington homeowners tend to care about timing, disruption and whether the contractor can keep a busy household moving.',
  'Carlisle projects need restraint and craft, which means the page should sound specific instead of inflated.',
  'Chelmsford searchers are usually balancing budget, family use and the desire for a kitchen that feels current.',
  'Concord homeowners often notice whether new work respects the older home, so the copy keeps structure and finish together.',
  'Dracut visitors need a realistic contractor comparison, especially when Cabinets, flooring and lighting all affect cost.',
  'Dunstable homeowners usually want a remodel that improves daily life without making the home feel overbuilt.',
  'Groton projects can involve older layouts, so the page connects cabinet planning to the condition of the room.',
  'Hudson searchers often want better entertaining space and more useful storage near a growing downtown lifestyle.',
  'Lexington homeowners need evidence of planning discipline before inviting a contractor into a high-value kitchen project.',
  'Lincoln projects call for a calmer tone: useful improvements, precise finish work and scope that stays under control.',
  'Littleton homeowners often compare local contractors through practical details like timeline, storage and project communication.',
  'Maynard kitchens can be tighter, so the page focuses on footprint discipline instead of oversized design promises.'
];

function esc(value) {
  return String(value)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

function jsonLd(data) {
  return JSON.stringify(data, null, 2).replace(/</g, '\\u003c');
}

function zipPhrase(city) {
  return city.zips.length === 1 ? `${city.zips[0]} ZIP code area` : `${city.zips.join(', ')} ZIP code areas`;
}

function relatedLinks(city) {
  const sameCounty = cities.filter((item) => item.county === city.county && item.slug !== city.slug).slice(0, 5);
  return [
    ['Kitchen Remodeling scope, layout and finish planning', '../../../pages/kitchen-remodeling/'],
    [`${city.county} remodeling service area`, '../../../areas/middlesex-county/'],
    ...sameCounty.map((item) => [`${item.name} Kitchen Remodel Contractor`, `../${item.slug}/`]),
    ['Kitchen remodel cost guide for Massachusetts homeowners', '../../../blog/kitchen-remodel-cost-massachusetts/']
  ].slice(0, 8);
}

function page(city, index) {
  const canonical = `${SITE}/services/${SERVICE}/${city.slug}/`;
  const zipText = zipPhrase(city);
  const title = `Kitchen Remodel in ${city.name}, MA | DeFaria Construction`;
  const description = `${city.name} Kitchen Remodel Contractor for Cabinets, Kitchen Cabinets, Kitchen Island planning, layout, finishes and owner-led estimates in ${city.zips.join(', ')}.`;
  const areaServed = [`${city.name}, MA`, ...city.areas.map((area) => `${area}, MA`), ...city.zips.map((zip) => `${zip} ZIP code area`)];
  const schema = [
    {
      '@context': 'https://schema.org',
      '@type': 'Service',
      name: `${city.name} Kitchen Remodel Contractor`,
      serviceType: 'Kitchen Remodel',
      description,
      provider: {
        '@type': 'LocalBusiness',
        name: 'DeFaria Construction',
        telephone: PHONE,
        url: SITE,
        areaServed: ['Middlesex County, MA', 'Essex County, MA']
      },
      areaServed,
      url: canonical
    },
    {
      '@context': 'https://schema.org',
      '@type': 'BreadcrumbList',
      itemListElement: [
        { '@type': 'ListItem', position: 1, name: 'Home', item: `${SITE}/` },
        { '@type': 'ListItem', position: 2, name: 'Kitchen Remodeling', item: `${SITE}/pages/kitchen-remodeling/` },
        { '@type': 'ListItem', position: 3, name: `${city.name} Kitchen Remodel`, item: canonical }
      ]
    },
    {
      '@context': 'https://schema.org',
      '@type': 'FAQPage',
      mainEntity: [
        {
          '@type': 'Question',
          name: `What does a Kitchen Remodel in ${city.name}, MA usually include?`,
          acceptedAnswer: { '@type': 'Answer', text: `${city.article.charAt(0).toUpperCase() + city.article.slice(1)} ${city.name} Kitchen Remodel can include layout planning, Kitchen Cabinets, counters, backsplash, flooring, lighting, plumbing, electrical updates, a Kitchen Island and finish carpentry.` }
        },
        {
          '@type': 'Question',
          name: `How do I compare a Kitchen Remodel Contractor in ${city.name}?`,
          acceptedAnswer: { '@type': 'Answer', text: `For ${city.name}, compare the contractor's scope clarity, communication, project photos, cabinet planning, finish sequencing and how well the estimate explains the work before demolition starts.` }
        },
        {
          '@type': 'Question',
          name: `Does DeFaria serve the ${city.zips.join(', ')} area?`,
          acceptedAnswer: { '@type': 'Answer', text: `Yes. DeFaria Construction serves ${city.name}, MA and the ${city.zips.join(', ')} area for kitchen remodeling, Cabinets, Kitchen Island planning and related interior remodeling work.` }
        },
        {
          '@type': 'Question',
          name: `Can DeFaria help if I searched for Kitchen Remodel Near Me?`,
          acceptedAnswer: { '@type': 'Answer', text: `Yes. If you are near ${city.name}, DeFaria can review the kitchen layout, Cabinets, surfaces, lighting and project scope before preparing the estimate for that local home.` }
        }
      ]
    }
  ];

  return `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>${esc(title)}</title>
  <meta name="description" content="${esc(description)}">
  <link rel="canonical" href="${canonical}">
  <meta property="og:type" content="website">
  <meta property="og:title" content="${esc(title)}">
  <meta property="og:description" content="${esc(description)}">
  <meta property="og:image" content="../../../images/og-image.jpg">
  <link rel="icon" href="../../../images/logo/favicon.avif" type="image/avif">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../../../css/style.css">
  <script type="application/ld+json">${jsonLd(schema)}</script>
  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-MT05J4KESX"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-MT05J4KESX');
  </script>
  <!-- MG Analytics v1.3 (7 comportamento + 5 conversao) -->
  <script>window.MG_CONV_CFG={form:"#estimateForm",estimateText:/estimate|quote/i};</script>
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
      <a class="btn btn--small btn--primary nav__cta" href="tel:${PHONE}">Call ${PHONE_LABEL}</a>
    </div>
  </header>

  <main>
    <section class="page-hero">
      <div class="page-hero__media"><img src="../../../images/pages/kitchen-remodeling-hero.webp?v=seo-kitchen-${city.slug}" alt="${esc(city.name)} Kitchen Remodel project by DeFaria Construction" fetchpriority="high"></div>
      <div class="page-hero__shade"></div>
      <div class="container page-hero__content">
        <a class="breadcrumb" href="../../../">Home / Kitchen Remodeling / ${esc(city.name)}</a>
        <p class="eyebrow">${esc(city.searchAngle)}</p>
        <h1>Kitchen Remodel in ${esc(city.name)}, MA with Cabinets, layout and finish details planned together</h1>
        <p class="page-hero__lead">DeFaria Construction helps ${esc(city.name)} homeowners plan a Kitchen Remodel around the way the room is used every day: Kitchen Cabinets, counters, lighting, flooring, Kitchen Island options and a clear construction scope before work begins.</p>
      </div>
    </section>

    <section class="section">
      <div class="container detail-grid">
        <div>
          <p class="eyebrow eyebrow--dark">Local search focus</p>
          <h2>${esc(city.name)} homeowners need a kitchen page that answers the real hiring question.</h2>
        </div>
        <div class="detail-copy">
          <p>In ${esc(city.name)}, kitchen remodeling often happens in ${esc(city.homeStyle)}. ${esc(city.localIntent.charAt(0).toUpperCase() + city.localIntent.slice(1))}.</p>
          <p>${esc(intros[index % intros.length])} Someone searching for ${esc(city.searchAngle)} should see more than one generic paragraph about remodeling.</p>
          <ul class="feature-list">
            <li>${esc(city.name)} Kitchen Remodel planning for the ${esc(zipText)}.</li>
            <li>${esc(city.name)} Kitchen Cabinets, Cabinets, counters and backsplash decisions tied to the same scope.</li>
            <li>Owner-led communication for ${esc(city.name)} homeowners from walkthrough to final walkthrough.</li>
          </ul>
        </div>
      </div>
    </section>

    <section class="section section--light">
      <div class="container detail-grid">
        <div>
          <p class="eyebrow eyebrow--dark">The scope</p>
          <h2>What a full ${esc(city.name)} Kitchen Remodel can include</h2>
        </div>
        <div class="detail-copy">
          <p>${esc(scopeOpeners[index % scopeOpeners.length])} In ${esc(city.name)}, DeFaria looks at the existing footprint, the daily traffic path, appliance locations and the finish level before separating the project into disconnected purchases.</p>
          <ul class="feature-list">
            <li>${esc(city.cabinetAngle.charAt(0).toUpperCase() + city.cabinetAngle.slice(1))}.</li>
            <li>${esc(city.islandAngle.charAt(0).toUpperCase() + city.islandAngle.slice(1))}.</li>
            <li>${esc(scopeClosers[index])}</li>
          </ul>
          <p>${esc(city.permitAngle.charAt(0).toUpperCase() + city.permitAngle.slice(1))}. That is why the first conversation is about scope, not only colors and materials.</p>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container detail-grid">
        <div>
          <p class="eyebrow eyebrow--dark">Local planning notes</p>
          <h2>How kitchen remodeling decisions change across ${esc(city.name)}</h2>
        </div>
        <div class="detail-copy">
          <p>Homes around ${esc(city.areas.slice(0, 3).join(', '))} do not all need the same kitchen plan. Some need better Cabinets and counter space. Some need lighting, flooring and backsplash work. Others need a Kitchen Island, wall opening or a more complete remodel.</p>
          <p>For ${esc(city.name)}, DeFaria treats Kitchen Remodeling as a construction conversation first. The estimate should explain what will be opened, what will be replaced, how the room will be protected and how the finished kitchen will support everyday use.</p>
          <p>${esc(finalAngles[index % finalAngles.length])} The page is written around searches in ${esc(city.zips.join(' and '))}, but the content stays specific to how people actually choose a remodeler.</p>
        </div>
      </div>
    </section>

    <section class="section seo-photo-proof" id="service-photos">
      <div class="container">
        <div class="section__head">
          <p class="eyebrow eyebrow--dark">Project photos</p>
          <h2>Kitchen Remodeling photos for ${esc(city.name)} homeowners</h2>
          <p>Real kitchen project photography helps ${esc(city.name)} homeowners judge Cabinets, layout, finish level and construction cleanliness before requesting an estimate.</p>
        </div>
        <div class="seo-photo-grid">
          <figure class="seo-photo-card"><img src="../../../images/pages/kitchen-remodeling-before-img-8217.webp" width="720" height="520" alt="${esc(city.name)} Kitchen Remodel before or in-progress project photo" loading="lazy"><figcaption>Before / in progress</figcaption></figure>
          <figure class="seo-photo-card"><img src="../../../images/pages/kitchen-remodeling-after-img-9226.webp" width="720" height="520" alt="${esc(city.name)} Kitchen Remodel finished kitchen by DeFaria Construction" loading="lazy"><figcaption>Finished kitchen</figcaption></figure>
          <figure class="seo-photo-card"><img src="../../../images/pages/kitchen-remodeling-detail.webp" width="720" height="520" alt="${esc(city.name)} Kitchen Cabinets and finish detail by DeFaria Construction" loading="lazy"><figcaption>Cabinet and finish detail</figcaption></figure>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container detail-grid">
        <div>
          <p class="eyebrow eyebrow--dark">Areas covered</p>
          <h2>Kitchen Remodel service across ${esc(city.name)} neighborhoods and ZIP codes</h2>
        </div>
        <div class="detail-copy">
          <p>DeFaria Construction supports kitchen remodeling searches across ${esc(city.name)} and nearby ${esc(city.county)} towns, giving ${esc(city.name)} visitors enough local context to decide whether DeFaria is the right contractor to call.</p>
          <ul class="feature-list">
            ${city.areas.map((area) => `<li>${esc(area)}</li>`).join('\n            ')}
            ${city.zips.map((zip) => `<li>${esc(zip)}</li>`).join('\n            ')}
          </ul>
        </div>
      </div>
    </section>

    <section class="section section--light seo-related" id="related-pages">
      <div class="container">
        <div class="section__head">
          <p class="eyebrow eyebrow--dark">Internal links</p>
          <h2>Related DeFaria Construction pages</h2>
          <p>Compare the full kitchen remodeling scope, the Middlesex service area and nearby city pages connected to ${esc(city.name)} search intent.</p>
        </div>
        <div class="seo-link-grid">
          ${relatedLinks(city).map(([label, href]) => `<a class="seo-link-card" href="${href}"><span>${esc(label)}</span><strong>View page</strong></a>`).join('\n          ')}
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container detail-grid">
        <div>
          <p class="eyebrow eyebrow--dark">Experience</p>
          <h2>Why this ${esc(city.name)} page is built for homeowners ready to compare contractors.</h2>
        </div>
        <div class="detail-copy">
          <p>DeFaria Construction is a local construction and remodeling company serving homeowners and business owners across Middlesex County and Essex County. ${esc(experienceAngles[index])} With direct owner involvement from Luiz DeFaria and BBB A+ credibility in the trust stack, this page is written around real Kitchen Remodeling scope.</p>
          <p>Every ${esc(city.name)} kitchen project should connect the visible design decisions to the construction work behind them: Cabinets, layout, flooring, backsplash, lighting, plumbing, electrical updates and final finish coordination.</p>
          <aside class="seo-author-proof">
            <div class="seo-author-proof__avatar" aria-hidden="true">LD</div>
            <div>
              <p><strong>Reviewed by Luiz DeFaria</strong>, Owner of DeFaria Construction. Luiz estimates kitchen, bathroom and remodeling projects personally for homeowners comparing options in ${esc(city.name)} and nearby Middlesex County towns.</p>
              <p>This ${esc(city.name)} page connects homeowner search intent to the ${esc(city.zips.join(', '))} area, where a Kitchen Remodel often depends on storage, traffic flow, owner communication and a realistic construction sequence.</p>
              <span class="seo-author-proof__cred">Licensed &middot; BBB Accredited Business &middot; A+ Rating &middot; Owner-led</span>
            </div>
          </aside>
          <p>Someone looking for a Kitchen Remodel Contractor in ${esc(city.name)}, MA should understand the scope, ZIP codes covered and estimate path before they pick up the phone.</p>
          <a class="btn btn--primary" href="tel:${PHONE}">Call ${PHONE_LABEL} for a free estimate</a>
        </div>
      </div>
    </section>

    <section class="section section--light">
      <div class="container">
        <p class="eyebrow eyebrow--dark">FAQ</p>
        <h2>Common questions about Kitchen Remodel work in ${esc(city.name)}</h2>
        <div class="faq-list">
          <details><summary>What does a Kitchen Remodel in ${esc(city.name)}, MA usually include?</summary><p>${esc(city.article.charAt(0).toUpperCase() + city.article.slice(1))} ${esc(city.name)} Kitchen Remodel can include layout planning, Kitchen Cabinets, counters, backsplash, flooring, lighting, plumbing, electrical updates, a Kitchen Island and finish carpentry.</p></details>
          <details><summary>How do I compare a Kitchen Remodel Contractor in ${esc(city.name)}?</summary><p>For ${esc(city.name)}, compare the contractor's scope clarity, communication, project photos, cabinet planning, finish sequencing and how well the estimate explains the work before demolition starts.</p></details>
          <details><summary>Does DeFaria serve the ${esc(city.zips.join(', '))} area?</summary><p>Yes. DeFaria Construction serves ${esc(city.name)}, MA and the ${esc(city.zips.join(', '))} area for kitchen remodeling, Cabinets, Kitchen Island planning and related interior remodeling work.</p></details>
          <details><summary>Can DeFaria help if I searched for Kitchen Remodel Near Me in ${esc(city.name)}?</summary><p>Yes. If you are near ${esc(city.name)}, DeFaria can review the kitchen layout, Cabinets, surfaces, lighting and project scope before preparing the estimate for that local home.</p></details>
        </div>
      </div>
    </section>
  </main>

  <footer class="footer">
    <div class="container footer__grid">
      <div>
        <img src="../../../images/logo/logo-white.webp" width="190" height="64" alt="DeFaria Construction" loading="lazy">
        <p>Kitchen, bathroom, interior, exterior and commercial remodeling for ${esc(city.name)} and nearby Middlesex County communities.</p>
      </div>
      <div class="footer__links"><a href="../../../#services">Services</a><a href="../../../#process">Process</a><a href="../../../#contact">Estimate</a></div>
    </div>
  </footer>
  <script src="../../../js/main.js"></script>
</body>
</html>
`;
}

function updateSitemap() {
  const sitemapPath = path.join(ROOT, 'sitemap.xml');
  let xml = fs.readFileSync(sitemapPath, 'utf8');
  const block = cities.map((city) => `  <url>
    <loc>${SITE}/services/${SERVICE}/${city.slug}/</loc>
    <lastmod>${TODAY}</lastmod>
    <priority>0.9</priority>
  </url>`).join('\n');

  for (const city of cities) {
    const escaped = `${SITE}/services/${SERVICE}/${city.slug}/`.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    xml = xml.replace(new RegExp(`\\s*<url>\\s*<loc>${escaped}<\\/loc>\\s*<lastmod>[^<]+<\\/lastmod>\\s*<priority>[^<]+<\\/priority>\\s*<\\/url>`, 'g'), '');
  }

  xml = xml.replace(/\s*<\/urlset>\s*$/, `\n${block}\n</urlset>\n`);
  fs.writeFileSync(sitemapPath, xml);
  console.log(`updated sitemap.xml with ${cities.length} kitchen URLs`);
}

for (const [index, city] of cities.entries()) {
  const out = path.join(ROOT, 'services', SERVICE, city.slug, 'index.html');
  fs.mkdirSync(path.dirname(out), { recursive: true });
  fs.writeFileSync(out, page(city, index));
  console.log(`wrote services/${SERVICE}/${city.slug}/index.html`);
}

updateSitemap();
