const { execFileSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const root = path.resolve(__dirname, '..');
const drive = path.join(root, '_drive-materiais');
const serviceImageVersion = '?v=20260611-menu';

const serviceImageSources = {
  'kitchen-remodeling': path.join(drive, '118-whiley-kitchen-selected', 'IMG_9226.jpeg'),
  'bathroom-remodeling': path.join(root, 'images', 'pages', 'bathroom-remodeling-detail.webp'),
  'interior-remodeling': path.join(root, 'images', 'pages', 'interior-remodeling-after.webp'),
  'commercial-projects': path.join(root, 'images', 'pages', 'commercial-projects-after.webp'),
  'home-additions': path.join(root, 'images', 'pages', 'ai-menu-sources', 'home-additions-menu-higgsfield-2026-06-11.png'),
  'interior-painting': path.join(root, 'images', 'pages', 'ai-menu-sources', 'interior-painting-menu-higgsfield-2026-06-11.png'),
  'exterior-painting': path.join(root, 'images', 'pages', 'ai-menu-sources', 'exterior-painting-menu-higgsfield-2026-06-11.png'),
  'finish-basements': path.join(drive, '18 Kensigton - Basement', 'IMG_8311.jpeg'),
  'custom-finish-carpentry': path.join(root, 'images', 'pages', 'ai-before-after-sources', 'custom-finish-carpentry-after-higgsfield-2026-06-11.png'),
  'decks-and-patios': path.join(drive, '277 Appleton - DECK ', 'IMG_8418.jpeg'),
  'foundation-and-framing': path.join(root, 'images', 'pages', 'ai-menu-sources', 'foundation-and-framing-menu-higgsfield-2026-06-11.png')
};

const aiPageImageSources = {
  'home-additions': {
    before: path.join(root, 'images', 'pages', 'ai-before-after-sources', 'home-additions-before-higgsfield-2026-06-11.png'),
    after: path.join(root, 'images', 'pages', 'ai-before-after-sources', 'home-additions-after-higgsfield-2026-06-11.jpeg')
  },
  'interior-painting': {
    before: path.join(root, 'images', 'pages', 'ai-before-after-sources', 'interior-painting-before-higgsfield-2026-06-11.png'),
    after: path.join(root, 'images', 'pages', 'ai-before-after-sources', 'interior-painting-after-higgsfield-2026-06-11.png')
  },
  'exterior-painting': {
    before: path.join(root, 'images', 'pages', 'ai-before-after-sources', 'exterior-painting-before-higgsfield-2026-06-11.png'),
    after: path.join(root, 'images', 'pages', 'ai-before-after-sources', 'exterior-painting-after-higgsfield-2026-06-11.png')
  },
  'foundation-and-framing': {
    before: path.join(root, 'images', 'pages', 'ai-before-after-sources', 'foundation-and-framing-before-higgsfield-2026-06-11.png'),
    after: path.join(root, 'images', 'pages', 'ai-before-after-sources', 'foundation-and-framing-after-higgsfield-2026-06-11.png')
  },
  'custom-finish-carpentry': {
    before: path.join(root, 'images', 'pages', 'ai-before-after-sources', 'custom-finish-carpentry-before-higgsfield-2026-06-11.png'),
    after: path.join(root, 'images', 'pages', 'ai-before-after-sources', 'custom-finish-carpentry-after-higgsfield-2026-06-11.png')
  }
};

const services = [
  {
    slug: 'kitchen-remodeling',
    title: 'Kitchen Remodeling',
    nav: 'Kitchen',
    meta: 'Kitchen remodeling in Middlesex County and Essex County with clear scope, material planning, finish coordination and reliable project updates.',
    h1: 'A kitchen remodel should feel planned before it feels expensive.',
    lead: 'DeFaria Construction helps homeowners turn kitchen ideas into a clear scope, visible material decisions and a project path that is easier to trust.',
    introTitle: 'Function, materials and communication belong in the estimate.',
    intro: [
      'A kitchen remodel touches the most used room in the home. The client needs to understand what will change, which materials matter, how the space will be protected and what decisions can affect timing.',
      'The DeFaria angle is not just craftsmanship. It is making the project feel controlled from the first walkthrough through the final review.'
    ],
    features: ['Cabinetry, finish and layout planning before demolition.', 'Material expectations explained before decisions become delays.', 'Progress updates that keep the home owner aware of what happens next.'],
    before: ['118 whiley Kitchen/Antes', 'IMG_8217.jpeg'],
    after: ['118-whiley-kitchen-selected', 'IMG_9226.jpeg'],
    detail: ['32 Hamilton - Kitchen', 'IMG_7456.jpeg'],
    caption: 'Kitchen photos from DeFaria project materials.',
    cta: 'Planning a kitchen project in Middlesex or Essex County?'
  },
  {
    slug: 'bathroom-remodeling',
    title: 'Bathroom Remodeling',
    nav: 'Bathroom',
    meta: 'Bathroom remodeling with clean rough-in, tile, fixtures, finish coordination and a process homeowners can follow.',
    h1: 'A bathroom should feel clean, durable and carefully controlled.',
    lead: 'From demolition to final fixture, DeFaria Construction organizes bathroom remodeling around visible steps, clean execution and finish details that hold up.',
    introTitle: 'Small rooms expose every detail.',
    intro: [
      'Bathrooms leave little room for vague planning. Plumbing, waterproofing, tile, storage and fixture placement need to be clear before the finish work begins.',
      'The goal is a room that looks finished and feels trustworthy because the hidden parts of the project were handled with the same care.'
    ],
    features: ['Rough-in, waterproofing and finish sequencing handled with discipline.', 'Tile, fixtures and trim coordinated before the final stage.', 'Clean jobsite habits for projects inside active homes.'],
    before: ['118 Whiley - Bath2', 'IMG_7616.jpeg'],
    after: ['118 Whiley - Bath2', 'IMG_8397.jpeg'],
    detail: ['32 Hamilton - Bath', 'IMG_7474.jpeg'],
    caption: 'Bathroom progress and finish photos from DeFaria materials.',
    cta: 'Ready to remodel a bathroom without losing control of the details?'
  },
  {
    slug: 'interior-remodeling',
    title: 'Interior Remodeling',
    nav: 'Interior',
    meta: 'Interior remodeling for family rooms, living areas, basements and home upgrades with a clear plan and reliable execution.',
    h1: 'Interior remodeling should make the home easier to live in.',
    lead: 'DeFaria Construction helps turn underused rooms into finished, useful spaces with clear planning, practical sequencing and careful finish work.',
    introTitle: 'A better interior is more than new surfaces.',
    intro: [
      'Interior work can involve framing, finish carpentry, paint, drywall, trim, doors, lighting coordination and layout changes. When those pieces are not organized, the project feels endless.',
      'DeFaria keeps the path understandable so the owner sees the progress, not just the disruption.'
    ],
    features: ['Room updates planned around daily use, not only appearance.', 'Finish details coordinated across trim, paint, doors and surfaces.', 'A practical process for active homes and occupied spaces.'],
    before: ['15 Worcester - Family room', 'IMG_7954.jpeg'],
    after: ['15 Worcester - Family room', 'IMG_9020.JPG'],
    detail: ['15 Worcester - Family room', 'Double Doors View.jpeg'],
    caption: 'Interior family room photos from DeFaria project materials.',
    cta: 'Have an interior space that needs to feel finished and useful?'
  },
  {
    slug: 'commercial-projects',
    title: 'Commercial Projects',
    nav: 'Commercial',
    meta: 'Commercial remodeling and improvement projects with clear communication, organized scheduling and practical execution.',
    h1: 'Commercial improvements need coordination as much as craftsmanship.',
    lead: 'DeFaria Construction supports business owners who need the work done clearly, respectfully and with attention to the operation around the project.',
    introTitle: 'A business space cannot be treated like a vague side job.',
    intro: [
      'Commercial projects need communication, scheduling awareness and a contractor who understands that the space is tied to revenue, customer experience and daily operations.',
      'The site experience should make that clear: scope first, coordination second, execution with as little confusion as possible.'
    ],
    features: ['Project communication for owners who need visibility.', 'Scheduling and scope decisions made before work interrupts the space.', 'Clean execution for offices, storefronts and commercial interiors.'],
    before: ['18 Kensigton - Basement', 'IMG_7633.jpeg'],
    after: ['18 Kensigton - Basement', 'IMG_8314.jpeg'],
    detail: ['15 Worcester - Family room', 'IMG_9018.jpeg'],
    caption: 'Interior improvement photos used to represent commercial coordination.',
    cta: 'Need a commercial space improved without guessing the next step?'
  },
  {
    slug: 'home-additions',
    title: 'Home Additions',
    nav: 'Additions',
    meta: 'Home additions with planning, framing, exterior coordination and communication from first walkthrough to final finish.',
    h1: 'A home addition has to look like it belongs there.',
    lead: 'DeFaria Construction helps homeowners expand usable space with planning that respects structure, exterior finish, function and the existing home.',
    introTitle: 'Adding space means connecting old and new without confusion.',
    intro: [
      'A home addition is not just extra square footage. It affects the exterior, structure, circulation, finishes and how the family uses the house every day.',
      'The right contractor keeps those pieces visible before the work starts, so the project does not become a stack of surprises.'
    ],
    features: ['Scope conversations around structure, exterior tie-ins and finish expectations.', 'Clear sequencing for framing, weather protection and interior completion.', 'Planning that protects the existing home during the expansion.'],
    before: ['132 Whiley - Exterior', 'IMG_5969.jpeg'],
    after: ['5 Baldwin Rd - Exterior', 'IMG_6907.jpeg'],
    detail: ['5 Baldwin Rd - Exterior', 'IMG_6905.jpeg'],
    caption: 'Exterior project photos from DeFaria materials.',
    cta: 'Thinking about adding space to the home?'
  },
  {
    slug: 'interior-painting',
    title: 'Interior Painting',
    nav: 'Interior Painting',
    meta: 'Interior painting with surface preparation, clean lines, trim coordination and a finished look that supports the remodel.',
    h1: 'Interior paint should finish the room, not hide the work.',
    lead: 'DeFaria Construction treats interior painting as part of the finish system, with prep, surfaces, trim and color transitions planned around the room.',
    introTitle: 'Paint exposes preparation.',
    intro: [
      'Good interior painting starts before the roller. Surface prep, drywall condition, trim lines, doors and lighting all affect whether the result feels clean or rushed.',
      'That is why DeFaria connects painting with the full remodeling process instead of treating it as a last-minute cover-up.'
    ],
    features: ['Surface prep before finish coats.', 'Trim, doors and wall transitions coordinated cleanly.', 'Painting that supports the remodel instead of masking unfinished detail.'],
    before: ['15 Worcester - Family room', 'IMG_8404.jpeg'],
    after: ['15 Worcester - Family room', 'IMG_9019.jpeg'],
    detail: ['15 Worcester - Family room', 'IMG_8702.jpeg'],
    caption: 'Interior finish photos from DeFaria project materials.',
    cta: 'Need a room painted as part of a real finish plan?'
  },
  {
    slug: 'exterior-painting',
    title: 'Exterior Painting',
    nav: 'Exterior Painting',
    meta: 'Exterior painting and finish updates with prep, weather awareness and a clean result for Massachusetts homes.',
    h1: 'Exterior paint is protection people can see from the street.',
    lead: 'DeFaria Construction helps homeowners improve curb appeal while paying attention to preparation, surfaces, trim and the weather realities around exterior work.',
    introTitle: 'The outside finish has to handle more than photos.',
    intro: [
      'Exterior painting is part appearance, part protection. Prep, surface condition, trim and weather timing determine whether the result holds up.',
      'The owner should understand what needs attention before the color goes on, especially when the project connects to siding, carpentry or exterior repair.'
    ],
    features: ['Prep-first approach for siding, trim and exterior surfaces.', 'Curb appeal improvements tied to practical protection.', 'Clear expectations around timing, access and weather.'],
    before: ['132 Whiley - Exterior', 'IMG_5969.jpeg'],
    after: ['132 Whiley - Exterior', 'IMG_6221.jpeg'],
    detail: ['132 Whiley - Exterior', 'IMG_6219.jpeg'],
    caption: 'Exterior photos from DeFaria project materials.',
    cta: 'Want the exterior to look sharper and hold up better?'
  },
  {
    slug: 'finish-basements',
    title: 'Finish Basements',
    nav: 'Basements',
    meta: 'Finished basement remodeling with framing, drywall, paint, trim and layout planning for more usable living space.',
    h1: 'A finished basement should feel like part of the home.',
    lead: 'DeFaria Construction turns unfinished or underused basement areas into cleaner, more usable spaces with planning, framing, drywall and finish work.',
    introTitle: 'Basements need practical planning before they need decoration.',
    intro: [
      'A basement project can include framing, insulation, drywall, paint, trim, flooring coordination and layout decisions. If those are unclear, the room can feel improvised.',
      'DeFaria positions basement finishing as a way to create real living value, not just cover concrete and call it done.'
    ],
    features: ['Framing, drywall and finish sequencing planned as one project.', 'Layout decisions tied to how the space will be used.', 'A cleaner, more valuable lower level with visible progress.'],
    before: ['18 Kensigton - Basement', 'IMG_7639.jpeg'],
    after: ['18 Kensigton - Basement', 'IMG_8311.jpeg'],
    detail: ['18 Kensigton - Basement', 'IMG_8311.jpeg'],
    caption: 'Basement progress and finish photos from DeFaria materials.',
    cta: 'Have a basement that could become real living space?'
  },
  {
    slug: 'custom-finish-carpentry',
    title: 'Custom and Finish Carpentry',
    nav: 'Carpentry',
    meta: 'Custom and finish carpentry for trim, doors, built-ins, finish details and remodeling upgrades.',
    h1: 'Finish carpentry is where the room starts to feel intentional.',
    lead: 'DeFaria Construction brings carpentry detail into remodels with trim, doors, finish transitions and built-in thinking that makes the work feel complete.',
    introTitle: 'The final inch is where quality becomes obvious.',
    intro: [
      'Clients may not know every construction term, but they notice doors, trim, lines, joints and finish details immediately.',
      'Custom and finish carpentry gives the site a proof point for craftsmanship, especially when paired with real project photos instead of generic promises.'
    ],
    features: ['Trim, doors and finish details aligned with the room.', 'Carpentry decisions connected to the whole remodel.', 'Visible craftsmanship that helps the home feel complete.'],
    before: ['15 Worcester - Family room', 'IMG_7957.jpeg'],
    after: ['15 Worcester - Family room', 'Double Doors View.jpeg'],
    detail: ['15 Worcester - Family room', 'IMG_8719.jpeg'],
    caption: 'Finish carpentry photos from DeFaria project materials.',
    cta: 'Need finish details that make the room feel complete?'
  },
  {
    slug: 'decks-and-patios',
    title: 'Decks and Patios',
    nav: 'Decks',
    meta: 'Deck and patio projects with planning, structure, exterior finish and a cleaner outdoor living experience.',
    h1: 'Outdoor space should feel sturdy before it feels inviting.',
    lead: 'DeFaria Construction builds and improves decks and patios with attention to structure, access, finish and how the outdoor space will be used.',
    introTitle: 'A deck is part structure, part lifestyle.',
    intro: [
      'Decks and patios affect how a family uses the home outside. The project needs practical decisions around structure, layout, access, materials and the finish clients see every day.',
      'DeFaria uses real project progress to show that outdoor work is planned, built and finished with care.'
    ],
    features: ['Deck structure and finish planned together.', 'Outdoor access and layout decisions made before the build.', 'Progress photos that show the work behind the final result.'],
    before: ['277 Appleton - DECK ', 'IMG_8299.jpeg'],
    after: ['277 Appleton - DECK ', 'IMG_8418.jpeg'],
    detail: ['277 Appleton - DECK ', 'IMG_8417.jpeg'],
    caption: 'Deck project photos from DeFaria materials.',
    cta: 'Want the outdoor space to become useful again?'
  },
  {
    slug: 'insulation-drywall-plaster',
    title: 'Insulation, Drywall and Plaster',
    nav: 'Drywall',
    meta: 'Insulation, drywall and plaster work with clean preparation, surface control and finish-ready execution.',
    h1: 'The walls people see depend on the work they never notice.',
    lead: 'DeFaria Construction handles insulation, drywall and plaster as the backbone of a clean interior finish, not as a rushed step before paint.',
    introTitle: 'Good finish work starts inside the wall.',
    intro: [
      'Insulation, drywall and plaster influence comfort, sound, surface quality and how the final paint or trim will look.',
      'This page gives DeFaria a clear place to show the hidden work behind a finished room, which builds trust with clients who fear shortcuts.'
    ],
    features: ['Insulation and wall preparation tied to the full remodel.', 'Drywall and plaster work prepared for clean paint and trim.', 'Progress visibility before the finished room appears.'],
    before: ['18 Kensigton - Basement', 'IMG_7636.jpeg'],
    after: ['18 Kensigton - Basement', 'IMG_8293.jpeg'],
    detail: ['15 Worcester - Family room', 'IMG_8406.jpeg'],
    caption: 'Drywall and interior progress photos from DeFaria materials.',
    cta: 'Need wall work handled before the finish stage?'
  },
  {
    slug: 'foundation-and-framing',
    title: 'Foundation and Framing',
    nav: 'Framing',
    meta: 'Foundation and framing support for remodels, additions and structural project phases with clear scope and coordination.',
    h1: 'Strong finish work starts with the structure nobody should question.',
    lead: 'DeFaria Construction supports remodeling and addition projects with framing and structural phases planned around safety, sequencing and the finished result.',
    introTitle: 'Framing is where the project becomes real.',
    intro: [
      'Before finishes, paint or tile, the project depends on structure, layout and disciplined sequencing. Foundation and framing work should never feel vague to the client.',
      'This service page positions DeFaria for the serious phases of a project while still connecting back to the visible final outcome.'
    ],
    features: ['Framing decisions tied to the remodel or addition plan.', 'Structural phases coordinated before finish work begins.', 'Progress photos used to show what is being built, not just what is promised.'],
    before: ['132 Whiley - Exterior', 'IMG_5970.jpeg'],
    after: ['132 Whiley - Exterior', 'IMG_6219.jpeg'],
    detail: ['132 Whiley - Exterior', 'IMG_6213.jpeg'],
    caption: 'Framing and exterior progress photos from DeFaria materials.',
    cta: 'Planning a project that needs structure before finish?'
  }
];

function esc(value) {
  return String(value)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

function assetVersion(service, type) {
  if (service.slug === 'interior-remodeling' && ['hero', 'detail'].includes(type)) {
    return '?v=20260611-cover';
  }
  if (aiPageImageSources[service.slug] && ['hero', 'before', 'after', 'detail'].includes(type)) {
    return '?v=20260611-ai-before-after';
  }
  return '';
}

function assetPath(pair) {
  return path.join(drive, pair[0], pair[1]);
}

function pageImageSource(service, type) {
  const aiSources = aiPageImageSources[service.slug];
  if (aiSources) {
    if (type === 'before') return aiSources.before;
    if (['hero', 'after', 'detail'].includes(type)) return aiSources.after;
  }
  return assetPath(service[type] || service.after);
}

function pageImageName(service, type) {
  if (service.slug === 'kitchen-remodeling' && type === 'before') {
    return 'kitchen-remodeling-before-img-8217.webp';
  }
  if (service.slug === 'kitchen-remodeling' && type === 'after') {
    return 'kitchen-remodeling-after-img-9226.webp';
  }
  return `${service.slug}-${type}.webp`;
}

function makeWebp(input, output, size) {
  fs.mkdirSync(path.dirname(output), { recursive: true });
  execFileSync('magick', [
    input,
    '-auto-orient',
    '-resize',
    `${size}^`,
    '-gravity',
    'center',
    '-extent',
    size,
    '-quality',
    '82',
    output
  ], { stdio: 'inherit' });
}

function navLinks(currentSlug) {
  const current = services.find((service) => service.slug === currentSlug);
  return `<a href="../../#services">All Services</a>
        <a href="../kitchen-remodeling/">Kitchen</a>
        <a href="../bathroom-remodeling/">Bathroom</a>
        <a href="../interior-remodeling/">Interior</a>
        <a href="../commercial-projects/">Commercial</a>
        ${current && !['kitchen-remodeling', 'bathroom-remodeling', 'interior-remodeling', 'commercial-projects'].includes(current.slug) ? `<a href="../${current.slug}/" aria-current="page">${esc(current.nav)}</a>` : ''}`;
}

function relatedLinks(currentSlug) {
  return services
    .filter((service) => service.slug !== currentSlug)
    .slice(0, 4)
    .map((service) => `<a href="../${service.slug}/">${esc(service.title)}</a>`)
    .join('\n          ');
}

function pageHtml(service) {
  return `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>${esc(service.title)} | DeFaria Construction</title>
  <meta name="description" content="${esc(service.meta)}">
  <link rel="canonical" href="https://www.defariaconstruction.com/pages/${service.slug}/">
  <meta property="og:type" content="website">
  <meta property="og:title" content="${esc(service.title)} | DeFaria Construction">
  <meta property="og:description" content="${esc(service.meta)}">
  <meta property="og:image" content="../../images/og-image.jpg">
  <link rel="icon" href="../../images/logo/favicon.avif" type="image/avif">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../../css/style.css">
</head>
<body>
  <header class="site-header" id="siteHeader">
    <div class="container nav">
      <a class="nav__brand" href="../../" aria-label="DeFaria Construction home">
        <img src="../../images/logo/logo-header.webp" width="210" height="70" alt="DeFaria Construction" loading="eager" fetchpriority="high">
      </a>
      <button class="nav__toggle" id="navToggle" aria-label="Open menu" aria-expanded="false"><span></span><span></span><span></span></button>
      <nav class="nav__menu" id="navMenu" aria-label="Primary navigation">
        ${navLinks(service.slug)}
        <a href="../../#contact">Contact</a>
      </nav>
      <a class="btn btn--small btn--primary nav__cta" href="tel:+16178932221">Call (617) 893-2221</a>
    </div>
  </header>

  <main>
    <section class="page-hero">
      <div class="page-hero__media"><img src="../../images/pages/${pageImageName(service, 'hero')}${assetVersion(service, 'hero')}" alt="${esc(service.title)} work by DeFaria Construction" fetchpriority="high"></div>
      <div class="page-hero__shade"></div>
      <div class="container page-hero__content">
        <a class="breadcrumb" href="../../">Home / Services</a>
        <p class="eyebrow">${esc(service.title)}</p>
        <h1>${esc(service.h1)}</h1>
        <p class="page-hero__lead">${esc(service.lead)}</p>
      </div>
    </section>

    <section class="section">
      <div class="container detail-grid">
        <div>
          <p class="eyebrow eyebrow--dark">What matters most</p>
          <h2>${esc(service.introTitle)}</h2>
        </div>
        <div class="detail-copy">
          ${service.intro.map((text) => `<p>${esc(text)}</p>`).join('\n          ')}
          <ul class="feature-list">
            ${service.features.map((item) => `<li>${esc(item)}</li>`).join('\n            ')}
          </ul>
        </div>
      </div>
    </section>

    <section class="section before-after">
      <div class="container before-after__grid">
        <div>
          <p class="eyebrow eyebrow--dark">Before and after</p>
          <h2>Show the path, not just the promise.</h2>
          <p>Each service page uses DeFaria project materials to show either the real transformation or the construction stage that makes the final result believable.</p>
        </div>
        <div class="ba-pair">
          <figure>
            <span>Before / In progress</span>
            <img src="../../images/pages/${pageImageName(service, 'before')}${assetVersion(service, 'before')}" alt="${esc(service.title)} before or in-progress project photo" loading="lazy">
          </figure>
          <figure>
            <span>After / Final detail</span>
            <img src="../../images/pages/${pageImageName(service, 'after')}${assetVersion(service, 'after')}" alt="${esc(service.title)} finished project photo" loading="lazy">
          </figure>
        </div>
      </div>
    </section>

    <section class="section service-split">
      <div class="container detail-grid">
        <figure class="image-panel">
          <img src="../../images/pages/${pageImageName(service, 'detail')}${assetVersion(service, 'detail')}" alt="${esc(service.title)} detail by DeFaria Construction" loading="lazy">
          <figcaption>${esc(service.caption)}</figcaption>
        </figure>
        <div class="service-split__grid">
          <article class="mini-card"><span>01</span><h3>Before the work</h3><p>Walkthrough, goals, constraints and estimate clarity before a commitment is made.</p></article>
          <article class="mini-card"><span>02</span><h3>During the build</h3><p>Progress updates, organized execution and attention to the home or business around the work.</p></article>
          <article class="mini-card"><span>03</span><h3>At completion</h3><p>Final review, photo guidance and the next project or referral mapped while trust is high.</p></article>
        </div>
      </div>
    </section>

    <section class="section service-cta">
      <div class="container service-cta__inner">
        <div>
          <p class="eyebrow">Estimate first</p>
          <h2>${esc(service.cta)}</h2>
          <p>Call DeFaria Construction or request an estimate with the service, city and any photos you already have.</p>
        </div>
        <a class="btn btn--secondary" href="tel:+16178932221">Call (617) 893-2221</a>
      </div>
    </section>

    <section class="section related-services">
      <div class="container">
        <div class="section__head"><p class="eyebrow eyebrow--dark">More services</p><h2>Keep exploring DeFaria services.</h2></div>
        <div class="related-grid">
          ${relatedLinks(service.slug)}
        </div>
      </div>
    </section>
  </main>

  <footer class="footer">
    <div class="container footer__grid">
      <img src="../../images/logo/logo-white.webp" width="190" height="64" alt="DeFaria Construction" loading="lazy">
      <p>Kitchen, bathroom, interior, exterior and commercial remodeling across Middlesex County and Essex County.</p>
      <div class="footer__links"><a href="../../#services">Services</a><a href="../../#process">Process</a><a href="../../#contact">Estimate</a></div>
    </div>
  </footer>
  <script src="../../js/main.js"></script>
</body>
</html>`;
}

function serviceCard(service) {
  return `          <a class="service-card" href="pages/${service.slug}/">
            <img src="images/services/${service.slug}.webp${serviceImageVersion}" alt="${esc(service.title)} by DeFaria Construction" loading="lazy">
            <div>
              <p class="service-card__label">${esc(service.title)}</p>
              <h3>${esc(service.h1)}</h3>
              <p>${esc(service.lead)}</p>
            </div>
          </a>`;
}

function updateHome() {
  const indexPath = path.join(root, 'index.html');
  const html = fs.readFileSync(indexPath, 'utf8');
  const start = html.indexOf('        <div class="services__grid">');
  const end = html.indexOf('        </div>\n      </div>\n    </section>', start);
  if (start === -1 || end === -1) {
    throw new Error('Services grid not found in index.html');
  }
  const replacement = `        <div class="services__grid">\n${services.map(serviceCard).join('\n')}\n        </div>`;
  let updated = html.slice(0, start) + replacement + html.slice(end + '        </div>'.length);
  updated = updated
    .replace('Kitchen, bathroom, interior and commercial remodeling across Middlesex County and Essex County.', 'Kitchen, bathroom, interior, exterior and commercial remodeling across Middlesex County and Essex County.')
    .replace(/              <option>Kitchen remodeling<\/option>[\s\S]*?              <option>Other home renovation<\/option>/, services.map((service) => `              <option>${service.title}</option>`).join('\n') + '\n              <option>Other home renovation</option>')
    .replace('<span>Kitchen</span>\n          <span>Bathroom</span>\n          <span>Interior</span>\n          <span>Commercial</span>', '<span>Kitchen</span>\n          <span>Bathroom</span>\n          <span>Basements</span>\n          <span>Decks</span>\n          <span>Carpentry</span>');
  fs.writeFileSync(indexPath, updated);
}

for (const service of services) {
  console.log(`building ${service.slug}`);
  makeWebp(serviceImageSources[service.slug] || assetPath(service.after), path.join(root, 'images', 'services', `${service.slug}.webp`), '920x720');
  makeWebp(pageImageSource(service, 'hero'), path.join(root, 'images', 'pages', pageImageName(service, 'hero')), '1600x1000');
  makeWebp(pageImageSource(service, 'before'), path.join(root, 'images', 'pages', pageImageName(service, 'before')), '900x700');
  makeWebp(pageImageSource(service, 'after'), path.join(root, 'images', 'pages', pageImageName(service, 'after')), '900x700');
  makeWebp(pageImageSource(service, 'detail'), path.join(root, 'images', 'pages', pageImageName(service, 'detail')), '1200x1000');
  const pageDir = path.join(root, 'pages', service.slug);
  fs.mkdirSync(pageDir, { recursive: true });
  fs.writeFileSync(path.join(pageDir, 'index.html'), pageHtml(service));
}

updateHome();
console.log('done');
