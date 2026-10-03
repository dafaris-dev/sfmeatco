"""Build 5 pages from shared template + per-page content."""
import os

NAV = '''<header class="nav" id="nav">
  <a class="brand" href="index.html" aria-label="San Francisco Meat Co. — home">
    <img class="brand-logo" src="assets/logo.png" alt="San Francisco Meat Co." width="140" height="88"/>
  </a>
  <nav class="nav-links" aria-label="Primary">
    <a href="index.html"    data-page="index.html">About</a>
    <a href="mission.html"  data-page="mission.html">Mission</a>
    <a href="services.html" data-page="services.html">Services</a>
    <a href="menu.html"     data-page="menu.html">Menu</a>
    <a href="visit.html"    data-page="visit.html">Visit</a>
  </nav>
  <button class="menu-btn" aria-label="Toggle menu" aria-expanded="false" id="menuBtn">
    <span></span><span></span><span></span>
  </button>
</header>

<aside class="mobile-sheet" aria-hidden="true">
  <nav aria-label="Mobile">
    <a href="index.html"    data-page="index.html">About</a>
    <a href="mission.html"  data-page="mission.html">Mission</a>
    <a href="services.html" data-page="services.html">Services</a>
    <a href="menu.html"     data-page="menu.html">Menu</a>
    <a href="visit.html"    data-page="visit.html">Visit</a>
  </nav>
  <div class="meta">
    Hayes Valley · San Francisco
    <a href="tel:+14155292349">(415) 529-2349</a>
    <a href="https://maps.google.com/?q=320+Fell+Street+San+Francisco" target="_blank" rel="noreferrer">320 Fell Street, SF 94102</a>
  </div>
</aside>'''

FOOTER = '''<footer aria-labelledby="footer-title">
  <div class="wrap">
    <div class="footer-grid">
      <div class="footer-brand">
        <div class="logo">
          <img src="assets/logo.png" alt="San Francisco Meat Co." width="150" height="94" style="width:150px;height:auto;filter:brightness(1.05)"/>
        </div>
        <p>
          A family-run Hayes Valley butcher shop. Dry-aged beef, Wagyu,
          pasture-raised chicken, pork and lamb — plus sandwiches, beer and wine
          to-go, and butchery classes on the floor.
        </p>
      </div>
      <div>
        <h4>Explore</h4>
        <ul>
          <li><a href="index.html">About</a></li>
          <li><a href="mission.html">Mission</a></li>
          <li><a href="services.html">Services</a></li>
          <li><a href="menu.html">Menu</a></li>
          <li><a href="visit.html">Visit</a></li>
        </ul>
      </div>
      <div>
        <h4>Visit</h4>
        <div class="block"><small>Address</small>320 Fell Street<br/>San Francisco, CA 94102</div>
        <div class="block" style="margin-top:22px"><small>Phone</small><a href="tel:+14155292349">(415) 529-2349</a></div>
      </div>
      <div>
        <h4>Hours</h4>
        <div class="block"><small>Tue – Sat</small>10 am – 7 pm</div>
        <div class="block" style="margin-top:22px"><small>Sunday</small>11 am – 6 pm</div>
        <div class="block" style="margin-top:22px"><small>Monday</small>Closed</div>
      </div>
    </div>
    <div class="footer-bottom">
      <div>© <span id="yr">2026</span> San Francisco Meat Co. · All rights reserved.</div>
      <nav aria-label="Footer">
        <a href="visit.html">Visit</a>
        <a href="tel:+14155292349">Call</a>
        <a href="https://maps.google.com/?q=320+Fell+Street+San+Francisco+CA+94102" target="_blank" rel="noreferrer">Directions</a>
      </nav>
    </div>
    <div class="footer-wordmark" aria-hidden="true" id="footer-title">SF&nbsp;MEAT&nbsp;CO.</div>
  </div>
</footer>'''

ARROW_SVG = '<svg viewBox="0 0 24 14" fill="none" aria-hidden="true"><path d="M0 7h22M17 1l6 6-6 6" stroke="currentColor" stroke-width="1.4" fill="none"/></svg>'

def next_page(label, url, page_n, title_html):
    return f'''<a class="next-page" href="{url}" aria-label="Next: {label}">
  <div class="wrap next-page-inner">
    <div>
      <span class="np-eyebrow">Next · Page {page_n} of 5</span>
      <h2 style="margin-top:16px">{title_html}</h2>
    </div>
    <div></div>
    <span class="np-arrow" aria-hidden="true">{ARROW_SVG}</span>
  </div>
</a>'''

def page(title, desc, canonical, body):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"/>
<meta name="theme-color" content="#0d0b09"/>
<title>{title} — San Francisco Meat Co.</title>
<meta name="description" content="{desc}"/>
<link rel="canonical" href="{canonical}"/>
<meta property="og:type" content="website"/>
<meta property="og:title" content="{title} — San Francisco Meat Co."/>
<meta property="og:description" content="{desc}"/>
<meta property="og:site_name" content="San Francisco Meat Co."/>
<link rel="preconnect" href="https://fonts.googleapis.com" crossorigin/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,400;0,9..144,500;0,9..144,600;0,9..144,700;0,9..144,800;1,9..144,400&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet"/>
<link rel="stylesheet" href="styles.css"/>
</head>
<body>
{NAV}
<main>
{body}
</main>
{FOOTER}
<script src="script.js" defer></script>
</body>
</html>
'''

# -------- Page content blocks --------

ABOUT_BODY = '''<section class="page-hero page-hero--about">
  <div class="wrap">
    <div class="hero-crest reveal">
      <img src="assets/logo.png" alt="San Francisco Meat Co. — Est. 2023" width="320" height="200"/>
    </div>
    <p class="page-crumb">Page 01 of 05 · About</p>
    <h1>We're the <em>new guys</em><br/>on the block.</h1>
    <p class="page-lead">
      A family-run Hayes Valley butcher shop opened in 2023 by Justin Seabridge and
      Kevin Nishikawa on the former Fatted Calf corner — dry-aged beef, Japanese
      and domestic Wagyu, pasture-raised chicken, pork and lamb, plus sandwiches
      and bottles to take home.
    </p>
    <div class="page-meta">
      <div><small>Established</small><strong>2023</strong></div>
      <div><small>Neighborhood</small><strong>Hayes Valley</strong></div>
      <div><small>Address</small><strong>320 Fell Street</strong></div>
      <div><small>Founders</small><strong>Seabridge &amp; Nishikawa</strong></div>
    </div>
  </div>
</section>

<section class="sec story" id="story">
  <div class="wrap">
    <div class="about-intro">
      <div class="reveal">
        <p class="about-eyebrow">About Us</p>
        <h2>Great meals start with<br/><em>great ingredients.</em></h2>
        <div class="signature">
          <strong>Est. 2023 · Hayes Valley</strong>
          <span>Justin Seabridge &amp; Kevin Nishikawa</span>
        </div>
      </div>
      <div class="reveal d1">
        <p>At San Francisco Meat Co., we believe great meals start with great ingredients. That's why we source only the finest meats — from imported Japanese Wagyu to premium, hand-selected cuts — and bring them straight to your kitchen with care and consistency.</p>
        <p>Whether you're preparing a weeknight dinner or celebrating life's special moments, our meats are chosen for their flavor, quality, and reliability. With San Francisco Meat Co., you're not just buying meat — you're bringing home a culinary experience built on craftsmanship, trust, and tradition.</p>
      </div>
    </div>

    <div class="collage reveal">
      <figure class="c1"><img src="assets/4.webp" alt="Two marbled ribeye steaks on a wooden board" loading="lazy"/><span class="cap">Hand-Selected Ribeye</span></figure>
      <figure class="c2"><img src="assets/5.webp" alt="Raw ribeye with an aged carving fork" loading="lazy"/><span class="cap">Butcher's Fork</span></figure>
      <figure class="c3"><img src="assets/7.webp" alt="Dry-aged porterhouse" loading="lazy"/><span class="cap">Dry-Aged Porterhouse</span></figure>
      <figure class="c4"><img src="assets/6.webp" alt="Butcher case" loading="lazy"/><span class="cap">The Counter · Fell Street</span></figure>
      <figure class="c5"><img src="assets/4.webp" alt="Marbling, up close" loading="lazy" style="object-position:center 30%"/><span class="cap">Marbling, Up Close</span></figure>
    </div>

    <div class="about-history">
      <div class="copy reveal">
        <p class="about-eyebrow">About Us</p>
        <h2>Our <em>History.</em></h2>
        <p>At San Francisco Meat Co., we're a family-owned butchery proudly serving our community with premium meats and personalized service. Our roots run three generations deep — through Justin Seabridge's father, who built a farm-to-market wholesale business supplying Bay Area restaurants and grocers for decades, and the hunting trips through Wyoming and Colorado where Justin first learned to work a whole animal.</p>
        <p>Whether you're a professional chef or a home cook, we offer the same exceptional care and attention to detail in every cut. From classic favorites to specialty selections, our meats are chosen for superior flavor, tenderness, and quality.</p>
        <p>We believe great meals start with great ingredients — and we're here to make sure every meal you prepare is nothing short of delicious.</p>
      </div>
      <figure class="pic reveal d1">
        <img src="assets/5.webp" alt="Hand-selected raw ribeye with vintage carving fork" loading="lazy"/>
        <span class="cap">Hand-Cut · In-House</span>
      </figure>
    </div>

    <div class="timeline reveal" aria-label="Company timeline">
      <div class="tr"><div class="yr">Earlier</div><div class="tx"><strong>Family wholesale.</strong> Justin's father builds a farm-to-market wholesale business supplying Bay Area restaurants and grocers for decades.</div></div>
      <div class="tr"><div class="yr">Young</div><div class="tx"><strong>Hunting trips west.</strong> Justin learns to break down wild game on family trips through Wyoming and Colorado.</div></div>
      <div class="tr"><div class="yr">2023</div><div class="tx"><strong>Hayes Valley opens.</strong> San Francisco Meat Co. opens on the former Fatted Calf corner at 320 Fell Street — counter, dry agers, kitchen and wine license intact.</div></div>
      <div class="tr"><div class="yr">Today</div><div class="tx"><strong>A working butcher shop.</strong> Hand-cut counter, dry-aged beef, Wagyu, sandwiches, bottles — and a classroom running on quieter weeks.</div></div>
    </div>
  </div>
</section>

''' + next_page("Our Mission", "mission.html", 2, "Our<br/><em>Mission.</em>")


MISSION_BODY = '''<section class="page-hero">
  <div class="wrap">
    <p class="page-crumb">Page 02 of 05 · Mission</p>
    <h1>The community's<br/><em>go-to butcher.</em></h1>
    <p class="page-lead">
      Our vision is to become the community's go-to destination for high-quality
      meats and exceptional service — the premier butcher shop in our area, known
      for sourcing the finest cuts, personalized customer experiences, and
      supporting local farmers and ranchers.
    </p>
  </div>
</section>

<section class="sec craft" id="craft">
  <div class="wrap">
    <div class="values-head reveal" style="margin-top:0; border-top:0; padding-top:0">
      <p class="eyebrow" style="color:var(--tan); margin-bottom:18px">Our Vision</p>
      <h3 class="values-title">Five principles<br/><em>we work by.</em></h3>
    </div>

    <div class="grid3 values">
      <div class="cell reveal"><span class="num">— 01</span><div><h3>Quality</h3><p>The quality of our meats is the foundation of our business. We're committed to sourcing only the freshest, most flavorful, and ethically raised meats from trusted local suppliers. Every piece is carefully selected and hand-cut to meet our exacting standards for taste, tenderness, and texture.</p></div></div>
      <div class="cell reveal d1"><span class="num">— 02</span><div><h3>Service</h3><p>We're dedicated to providing exceptional service. Our knowledgeable, friendly staff is always available to offer expert advice, help with special orders, and share cooking tips and recipes — building long relationships, learning your preferences, and going the extra mile to exceed expectations.</p></div></div>
      <div class="cell reveal d2"><span class="num">— 03</span><div><h3>Community</h3><p>We actively collaborate with local farmers and ranchers who share our values of sustainability, animal welfare, and environmentally responsible practices. Promoting local agriculture contributes to the economic vitality and food security of our community — while reducing our carbon footprint.</p></div></div>
      <div class="cell reveal"><span class="num">— 04</span><div><h3>Education</h3><p>We're committed to educating our customers about the value of high-quality meats and the importance of knowing where their food comes from. By sharing what we know about meat production and processing, we help our customers make informed choices that align with their values and dietary needs.</p></div></div>
      <div class="cell reveal d1"><span class="num">— 05</span><div><h3>Innovation</h3><p>We embrace innovation as a means to continually improve and evolve — always on the lookout for new techniques, technologies, and trends in the meat industry that can enhance the quality, sustainability, and convenience of what we offer, and the service around it.</p></div></div>
      <div class="cell cell--quote reveal d2"><span class="num">— The Shop</span><div><h3 class="q">A trusted partner,<br/><em>not just a butcher shop.</em></h3><p>With our commitment to quality, service, community, education and innovation, we strive to make a lasting impact on the lives of our customers and our local community — helping families make delicious, wholesome, and sustainable choices every day.</p></div></div>
    </div>
  </div>
</section>

''' + next_page("Services", "services.html", 3, "Our<br/><em>Services.</em>")


SERVICES_BODY = '''<section class="page-hero">
  <div class="wrap">
    <p class="page-crumb">Page 03 of 05 · Services</p>
    <h1>What <em>we do</em><br/>on the block.</h1>
    <p class="page-lead">
      We take pride in a wide range of services built around the diverse needs of
      our customers. Our experienced team of butchers and staff is committed to
      service that goes beyond selling meat — making sure every visit to the shop
      is the best possible one.
    </p>
  </div>
</section>

<section class="sec services" id="services">
  <div class="wrap">
    <article class="feature reveal">
      <div class="feature-visual">
        <img src="assets/dry-age.webp" alt="Three shelves of dry-aged beef primals in the shop's aging cabinet, each tagged with the San Francisco Meat Co. butcher card" loading="lazy" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center"/>
        <span class="tag">In-House · Fell Street</span>
      </div>
      <div class="feature-copy">
        <p class="eyebrow" style="color:var(--tan); margin-bottom:22px">Specialty Dry Aging</p>
        <h3>What makes <em>our dry aging</em> different.</h3>
        <p>At San Francisco Meat Co., our dry aging process is a blend of time, science, and craftsmanship. In our temperature- and humidity-controlled aging room, premium beef cuts rest and develop unparalleled depth of flavor, tenderness, and aroma. Over several weeks, natural enzymes break down muscle fibers while the outer layer forms a protective crust, concentrating the meat's rich, buttery essence. The result is an exceptional steak experience — bold, complex, and unmistakably San Francisco Meat Co. quality.</p>
        <ul class="feature-list">
          <li>Custom dry age programs (21 to 90+ days)</li>
          <li>Premium cut selection</li>
          <li>Private label aging for your restaurant</li>
          <li>Controlled aging environment</li>
          <li>Dry age retail &amp; wholesale supply</li>
          <li>Custom portioning &amp; packaging</li>
          <li>Specialty dry age pork &amp; poultry programs</li>
        </ul>
        <a class="btn ember" href="visit.html" style="margin-top:28px">Enquire About Dry Aging <svg class="arrow" viewBox="0 0 14 10" fill="none" aria-hidden="true"><path d="M1 5h12M9 1l4 4-4 4" stroke="currentColor" stroke-width="1.4"/></svg></a>
      </div>
    </article>

    <div class="list">
      <article class="svc reveal"><span class="idx">— 01</span><h3>Fresh <em>Meat</em> Daily</h3><p>A hand-cut counter stocked and rotated every day — dry-aged Angus, Wagyu, pork, lamb and poultry pulled, trimmed and portioned to order.</p><a class="cta" href="menu.html">Today's Case <svg class="arrow" viewBox="0 0 28 8" fill="none"><path d="M0 4h26M22 1l5 3-5 3" stroke="currentColor" stroke-width="1.2"/></svg></a></article>
      <article class="svc reveal d1"><span class="idx">— 02</span><h3>Dry <em>Aging</em></h3><p>Our dry aging program brings out the very best in premium beef. Using carefully controlled temperature, humidity and airflow, select cuts develop unmatched tenderness and rich, concentrated flavor — monitored throughout for consistency and excellence.</p><a class="cta" href="visit.html">Programs <svg class="arrow" viewBox="0 0 28 8" fill="none"><path d="M0 4h26M22 1l5 3-5 3" stroke="currentColor" stroke-width="1.2"/></svg></a></article>
      <article class="svc reveal d2"><span class="idx">— 03</span><h3>Custom <em>Orders</em></h3><p>Every customer has unique preferences when it comes to cuts. Our skilled butchers are trained in the art of custom butchering and can prepare meat to your exact specifications — special cuts, portioning or trimming, done to order.</p><a class="cta" href="visit.html">Request <svg class="arrow" viewBox="0 0 28 8" fill="none"><path d="M0 4h26M22 1l5 3-5 3" stroke="currentColor" stroke-width="1.2"/></svg></a></article>
      <article class="svc reveal"><span class="idx">— 04</span><h3>Wholesale <em>&amp;</em> Bulk Orders</h3><p>We cater to the needs of restaurants, caterers and other businesses that require meat in larger quantities. Wholesale and bulk ordering options at competitive prices — contact us to discuss your needs and we'll work with you to fulfill them.</p><a class="cta" href="visit.html">Talk To Us <svg class="arrow" viewBox="0 0 28 8" fill="none"><path d="M0 4h26M22 1l5 3-5 3" stroke="currentColor" stroke-width="1.2"/></svg></a></article>
      <article class="svc reveal d1"><span class="idx">— 05</span><h3>Catering <em>&amp;</em> Events</h3><p>Hosting a special event? Let us take care of the meat. Catering for weddings, parties and other occasions — contact us for more details.</p><a class="cta" href="visit.html">Enquire <svg class="arrow" viewBox="0 0 28 8" fill="none"><path d="M0 4h26M22 1l5 3-5 3" stroke="currentColor" stroke-width="1.2"/></svg></a></article>
      <article class="svc reveal d2"><span class="idx">— 06</span><h3>Expert <em>Advice</em></h3><p>Our knowledgeable staff is always available for expert advice on meat selection, preparation and cooking — the perfect cut for your recipe, cooking tips, and answers to anything you want to know about our products.</p><a class="cta" href="visit.html">Come In <svg class="arrow" viewBox="0 0 28 8" fill="none"><path d="M0 4h26M22 1l5 3-5 3" stroke="currentColor" stroke-width="1.2"/></svg></a></article>
      <article class="svc reveal"><span class="idx">— 07</span><h3>Events <em>&amp;</em> Workshops</h3><p>We foster community and share our love for meat through events and workshops — tastings, cooking demonstrations and butchery classes (poultry, lamb and half-a-hog breakdowns) that bring customers and meat enthusiasts together.</p><a class="cta" href="visit.html">Schedule <svg class="arrow" viewBox="0 0 28 8" fill="none"><path d="M0 4h26M22 1l5 3-5 3" stroke="currentColor" stroke-width="1.2"/></svg></a></article>
    </div>
  </div>
</section>

''' + next_page("Menu", "menu.html", 4, "Our<br/><em>Menu.</em>")


MENU_BODY = '''<section class="page-hero">
  <div class="wrap">
    <p class="page-crumb">Page 04 of 05 · Menu</p>
    <h1>Our<br/><em>Menu.</em></h1>
    <p class="page-lead">
      A tight, considered counter — not an inventory. We stock what we can stand
      behind: hand-selected whole animals broken down in-house, aged to spec, and
      finished to order. Here's what you'll usually find in the case.
    </p>
  </div>
</section>

<section class="sec sec-dark products" id="products">
  <div class="wrap">
    <!-- Row 1 -->
    <article class="product-row reveal">
      <figure class="pr-media">
        <span class="num">— 01</span>
        <div class="photo photo--beef" style="position:absolute;inset:0" role="img" aria-label="Dry-aged ribeye steak">
          <svg viewBox="0 0 500 600" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
            <defs><radialGradient id="pr1" cx="50%" cy="55%" r="48%"><stop offset="0%" stop-color="#b4381e" stop-opacity=".7"/><stop offset="60%" stop-color="#4a140f" stop-opacity=".55"/><stop offset="100%" stop-color="#000" stop-opacity=".3"/></radialGradient><radialGradient id="pr1b" cx="40%" cy="40%" r="12%"><stop offset="0%" stop-color="#f3e2bf" stop-opacity=".75"/><stop offset="100%" stop-color="#f3e2bf" stop-opacity="0"/></radialGradient></defs>
            <ellipse cx="250" cy="330" rx="190" ry="150" fill="url(#pr1)"/>
            <ellipse cx="210" cy="270" rx="55" ry="18" fill="url(#pr1b)"/>
            <ellipse cx="300" cy="360" rx="40" ry="16" fill="url(#pr1b)"/>
          </svg>
          <div class="glint"></div>
        </div>
        <span class="tag">Dry-Aged · In-House</span>
      </figure>
      <div class="pr-copy">
        <p class="eyebrow">Beef</p>
        <h3>Dry-Aged <em>Angus</em> &amp; <em>Prime</em> Cuts</h3>
        <p>Whole primals broken down and aged in custom dry agers kept in plain sight of the counter. The case rotates with the hang: ribeye and strip, hanger and skirt, chuck and short rib, with longer-aged specials when they're ready.</p>
        <ul class="list">
          <li>Dry-Aged Ribeye</li><li>NY Strip</li><li>Dry-Rub Pepper Ribeye</li>
          <li>Hanger &amp; Skirt</li><li>Short Rib &amp; Chuck</li><li>Roast Beef</li>
        </ul>
        <a class="btn" href="visit.html">Reserve a Cut <svg class="arrow" viewBox="0 0 14 10" fill="none"><path d="M1 5h12M9 1l4 4-4 4" stroke="currentColor" stroke-width="1.4"/></svg></a>
      </div>
    </article>

    <!-- Row 2 -->
    <article class="product-row rev reveal">
      <figure class="pr-media">
        <span class="num">— 02</span>
        <div class="photo photo--wagyu" style="position:absolute;inset:0" role="img" aria-label="Marbled Wagyu beef cut">
          <svg viewBox="0 0 500 600" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
            <defs><radialGradient id="pr2" cx="50%" cy="55%" r="52%"><stop offset="0%" stop-color="#c25c3e" stop-opacity=".6"/><stop offset="60%" stop-color="#5a1a14" stop-opacity=".45"/><stop offset="100%" stop-color="#000" stop-opacity=".3"/></radialGradient></defs>
            <ellipse cx="250" cy="320" rx="200" ry="170" fill="url(#pr2)"/>
            <g stroke="#f6e8cf" stroke-opacity=".55" fill="none" stroke-width="1.4" stroke-linecap="round">
              <path d="M110,270 C 180,250 240,310 310,280 C 360,260 400,300 430,290"/>
              <path d="M120,330 C 180,340 230,320 290,350 C 340,370 400,345 440,360"/>
              <path d="M140,380 C 190,400 260,380 320,410 C 370,430 420,410 450,420"/>
              <path d="M100,230 C 160,210 220,240 280,220"/>
              <path d="M130,420 C 180,445 250,430 310,450"/>
            </g>
          </svg>
          <div class="glint"></div>
        </div>
        <span class="tag">Imported &amp; Domestic</span>
      </figure>
      <div class="pr-copy">
        <p class="eyebrow">Wagyu</p>
        <h3>Japanese &amp; <em>Domestic Wagyu</em></h3>
        <p>Imported Japanese Wagyu brought in by the gram, alongside domestic Wagyu from US farms we know by name. Cut thick for the pan or thin for the counter sandwich — ask what's open today, and we'll walk you through it.</p>
        <ul class="list">
          <li>Japanese A5 Wagyu</li><li>Domestic Wagyu Steaks</li>
          <li>Wagyu Burger Blend</li><li>Wagyu Beef Sandwich</li>
        </ul>
        <a class="btn" href="visit.html">See It at the Counter <svg class="arrow" viewBox="0 0 14 10" fill="none"><path d="M1 5h12M9 1l4 4-4 4" stroke="currentColor" stroke-width="1.4"/></svg></a>
      </div>
    </article>

    <!-- Row 3 -->
    <article class="product-row reveal">
      <figure class="pr-media">
        <span class="num">— 03</span>
        <div class="photo photo--pork" style="position:absolute;inset:0" role="img" aria-label="Pork, lamb and poultry cuts">
          <svg viewBox="0 0 500 600" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
            <defs><radialGradient id="pr3" cx="50%" cy="55%" r="55%"><stop offset="0%" stop-color="#d49572" stop-opacity=".45"/><stop offset="60%" stop-color="#4a2615" stop-opacity=".45"/><stop offset="100%" stop-color="#000" stop-opacity=".3"/></radialGradient></defs>
            <ellipse cx="250" cy="320" rx="200" ry="160" fill="url(#pr3)"/>
            <g fill="#8c3a2a" fill-opacity=".55"><ellipse cx="160" cy="400" rx="80" ry="24"/><ellipse cx="250" cy="430" rx="80" ry="22"/><ellipse cx="340" cy="410" rx="80" ry="24"/></g>
          </svg>
          <div class="glint"></div>
        </div>
        <span class="tag">Pork · Lamb · Poultry</span>
      </figure>
      <div class="pr-copy">
        <p class="eyebrow">Beyond The Beef</p>
        <h3>Pork, Lamb <em>&amp;</em> Poultry</h3>
        <p>Pasture-raised chicken, heritage pork and American lamb, received whole and broken down on-site. Roasts for Sunday, cutlets for a Tuesday, half-birds and whole legs on request. If you want it tied, scored or butterflied, say the word.</p>
        <ul class="list">
          <li>Pasture-Raised Chicken</li><li>Heritage Pork</li>
          <li>American Lamb</li><li>Custom Cutting</li>
        </ul>
        <a class="btn" href="services.html">Custom Orders <svg class="arrow" viewBox="0 0 14 10" fill="none"><path d="M1 5h12M9 1l4 4-4 4" stroke="currentColor" stroke-width="1.4"/></svg></a>
      </div>
    </article>

    <!-- Row 4 -->
    <article class="product-row rev reveal">
      <figure class="pr-media">
        <span class="num">— 04</span>
        <div class="photo photo--sandwich" style="position:absolute;inset:0" role="img" aria-label="Butcher sandwich">
          <svg viewBox="0 0 500 600" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
            <defs><linearGradient id="pr4a" x1="0" x2="0" y1="0" y2="1"><stop offset="0%" stop-color="#d49462" stop-opacity=".8"/><stop offset="60%" stop-color="#8c5230" stop-opacity=".6"/><stop offset="100%" stop-color="#3a1d10" stop-opacity=".5"/></linearGradient><linearGradient id="pr4b" x1="0" x2="0" y1="0" y2="1"><stop offset="0%" stop-color="#a63a24" stop-opacity=".75"/><stop offset="100%" stop-color="#5a1a14" stop-opacity=".55"/></linearGradient></defs>
            <path d="M80 290 Q 250 180 420 290 L 420 320 L 80 320 Z" fill="url(#pr4a)"/>
            <rect x="80" y="320" width="340" height="60" fill="url(#pr4b)"/>
            <path d="M70 345 Q 150 335 230 350 Q 310 370 430 345 L 430 380 L 70 380 Z" fill="#6b2016" fill-opacity=".65"/>
            <path d="M80 380 L 420 380 Q 300 460 80 410 Z" fill="url(#pr4a)"/>
          </svg>
          <div class="glint"></div>
        </div>
        <span class="tag">Lunch · To-Go</span>
      </figure>
      <div class="pr-copy">
        <p class="eyebrow">From The Kitchen</p>
        <h3>Sandwiches, Beer <em>&amp;</em> Wine</h3>
        <p>A short lunch program built from what's hanging and what came in that morning — roast beef, Wagyu, pork, whatever is best that week. We kept the Fatted Calf liquor license, so there's beer and wine to-go with the help of a certified sommelier on the floor.</p>
        <ul class="list">
          <li>Wagyu Beef Sandwich</li><li>Roast Beef Sandwich</li>
          <li>Rotating Daily Specials</li><li>Beer &amp; Wine To-Go</li>
        </ul>
        <a class="btn" href="visit.html">Hours &amp; Directions <svg class="arrow" viewBox="0 0 14 10" fill="none"><path d="M1 5h12M9 1l4 4-4 4" stroke="currentColor" stroke-width="1.4"/></svg></a>
      </div>
    </article>
  </div>
</section>

<section class="strip" aria-hidden="true">
  <div class="strip-grid">
    <div class="strip-cell wide"><div class="photo photo--strip1" style="position:absolute;inset:0"></div><span class="label">The Block</span></div>
    <div class="strip-cell"><div class="photo photo--strip2" style="position:absolute;inset:0"></div><span class="label">Dry-Age</span></div>
    <div class="strip-cell"><div class="photo photo--strip3" style="position:absolute;inset:0"></div><span class="label">On The Pan</span></div>
    <div class="strip-cell"><div class="photo photo--strip4" style="position:absolute;inset:0"></div><span class="label">The Case</span></div>
    <div class="strip-cell"><div class="photo photo--strip5" style="position:absolute;inset:0"></div><span class="label">To-Go</span></div>
  </div>
</section>

''' + next_page("Visit", "visit.html", 5, "Come<br/><em>Visit.</em>")


VISIT_BODY = '''<section class="page-hero">
  <div class="wrap">
    <p class="page-crumb">Page 05 of 05 · Visit</p>
    <h1>Come by<br/><em>the counter.</em></h1>
    <p class="page-lead">
      We're on the corner of Fell and Gough in Hayes Valley. Walk-ins welcome.
      For a specific cut or something off-list, call ahead and we'll have it
      ready.
    </p>
    <div class="page-meta">
      <div><small>Address</small><strong>320 Fell Street</strong></div>
      <div><small>Phone</small><strong><a href="tel:+14155292349">(415) 529-2349</a></strong></div>
      <div><small>Tue–Sat</small><strong>10 am – 7 pm</strong></div>
      <div><small>Sunday</small><strong>11 am – 6 pm</strong></div>
    </div>
  </div>
</section>

<section class="sec city">
  <div class="wrap city-inner">
    <div class="city-copy reveal">
      <p class="eyebrow" style="margin-bottom:28px">On The Block</p>
      <h2>Hayes Valley,<br/><em>on the corner of Fell.</em></h2>
      <p>San Francisco Meat Co. sits on the corner of Fell and Gough, on a block that's been feeding this neighborhood for a long time. We took over the space from Fatted Calf Charcuterie in 2023 — kept the sightline through to the dry agers, kept the wine license, and added a counter the neighborhood could walk to on a weekday.</p>
      <p>We're a short walk from the farmers' market, the Opera House and the park. Come on foot, come in a chef's coat, come at 6:45 on a Saturday — we'll be here.</p>
      <div class="city-stats">
        <div><small>Neighborhood</small><strong>Hayes Valley</strong></div>
        <div><small>Address</small><strong>320 Fell Street</strong></div>
        <div><small>Zip</small><strong>SF, CA 94102</strong></div>
      </div>
    </div>
    <div class="city-visual reveal d1" aria-hidden="true">
      <div class="photo photo--city" style="position:absolute;inset:0">
        <svg viewBox="0 0 800 1000" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
          <defs><linearGradient id="sky2" x1="0" x2="0" y1="0" y2="1"><stop offset="0%" stop-color="#e8c89a" stop-opacity=".35"/><stop offset="100%" stop-color="#2a1612" stop-opacity="0"/></linearGradient></defs>
          <rect x="0" y="0" width="800" height="500" fill="url(#sky2)"/>
          <g fill="#1a0d08" fill-opacity=".85">
            <path d="M60 480 L 60 320 L 160 240 L 260 320 L 260 480 Z"/>
            <path d="M260 480 L 260 300 L 360 220 L 460 300 L 460 480 Z"/>
            <path d="M460 480 L 460 310 L 560 230 L 660 310 L 660 480 Z"/>
            <path d="M660 480 L 660 330 L 760 260 L 820 320 L 820 480 Z"/>
          </g>
          <g fill="#f6c882" fill-opacity=".35">
            <rect x="90" y="360" width="18" height="30"/><rect x="130" y="360" width="18" height="30"/>
            <rect x="170" y="360" width="18" height="30"/><rect x="210" y="360" width="18" height="30"/>
            <rect x="290" y="340" width="18" height="30"/><rect x="330" y="340" width="18" height="30"/>
            <rect x="370" y="340" width="18" height="30"/><rect x="490" y="350" width="18" height="30"/>
            <rect x="530" y="350" width="18" height="30"/><rect x="570" y="350" width="18" height="30"/>
          </g>
          <rect x="0" y="480" width="800" height="520" fill="#0a0504"/>
          <g stroke="#c7461c" stroke-opacity=".35" stroke-width="2" stroke-dasharray="20 20"><line x1="0" y1="620" x2="800" y2="620"/></g>
        </svg>
      </div>
      <span class="caption">Fell &amp; Gough · Hayes Valley</span>
    </div>
  </div>
</section>

<section class="visit" id="visit">
  <div class="visit-inner">
    <div class="visit-map" aria-hidden="true">
      <svg viewBox="0 0 800 800" preserveAspectRatio="xMidYMid slice" style="position:absolute;inset:0;width:100%;height:100%">
        <defs>
          <linearGradient id="mb" x1="0" x2="1" y1="0" y2="1"><stop offset="0%" stop-color="#1a1512"/><stop offset="100%" stop-color="#0a0706"/></linearGradient>
          <pattern id="dts" x="0" y="0" width="24" height="24" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r=".6" fill="#f4ece0" fill-opacity=".08"/></pattern>
        </defs>
        <rect width="800" height="800" fill="url(#mb)"/>
        <rect width="800" height="800" fill="url(#dts)"/>
        <path d="M0 460 L 800 300 L 800 380 L 0 540 Z" fill="#1f2a1a" fill-opacity=".55"/>
        <g stroke="#f4ece0" stroke-opacity=".14" stroke-width="1.4" fill="none">
          <path d="M-50 180 L 850 60"/><path d="M-50 290 L 850 170"/>
          <path d="M-50 410 L 850 290"/><path d="M-50 540 L 850 420"/>
          <path d="M-50 680 L 850 560"/>
          <path d="M80 -40 L 240 820"/><path d="M240 -40 L 400 820"/>
          <path d="M400 -40 L 560 820"/><path d="M560 -40 L 720 820"/>
        </g>
        <path d="M-50 410 L 850 290" stroke="#c7461c" stroke-opacity=".6" stroke-width="2.5" fill="none"/>
        <g font-family="Inter, sans-serif" font-size="10" letter-spacing="2" fill="#f4ece0" fill-opacity=".55">
          <text x="520" y="310" transform="rotate(-9 520 310)">FELL STREET</text>
          <text x="300" y="565" transform="rotate(-9 300 565)">OAK STREET</text>
          <text x="200" y="195" transform="rotate(-9 200 195)">HAYES STREET</text>
          <text x="620" y="130" transform="rotate(80 620 130)">GOUGH</text>
          <text x="420" y="130" transform="rotate(80 420 130)">OCTAVIA</text>
        </g>
      </svg>
      <div class="pin">
        <span class="marker"></span>
        <span class="lbl">SF Meat Co. · 320 Fell</span>
      </div>
    </div>

    <div class="visit-info reveal">
      <p class="eyebrow" style="margin-bottom:24px">Hours &amp; Directions</p>
      <h2>Visit<br/><em>the shop.</em></h2>
      <p class="lead">Walk-ins welcome. For a specific cut or something off-list, call ahead and we'll have it ready at the counter.</p>
      <div class="block"><span class="lbl">Address</span><span class="val"><a href="https://maps.google.com/?q=320+Fell+Street+San+Francisco+CA+94102" target="_blank" rel="noreferrer">320 Fell Street<br/>San Francisco, CA 94102</a></span></div>
      <div class="block"><span class="lbl">Phone</span><span class="val"><a href="tel:+14155292349">(415) 529-2349</a></span></div>
      <div class="block"><span class="lbl">Hours</span><span class="val">Tue – Sat · 10 am – 7 pm<br/>Sunday · 11 am – 6 pm<br/><span style="font-size:14px;color:var(--bone);font-family:var(--sans)">Monday · Closed</span></span></div>
      <div class="ctas">
        <a class="btn solid" href="tel:+14155292349">Call <svg class="arrow" viewBox="0 0 14 10" fill="none"><path d="M1 5h12M9 1l4 4-4 4" stroke="currentColor" stroke-width="1.4"/></svg></a>
        <a class="btn" href="https://maps.google.com/?q=320+Fell+Street+San+Francisco+CA+94102" target="_blank" rel="noreferrer">Get Directions</a>
      </div>
    </div>
  </div>
</section>

<section class="b2b">
  <div class="wrap b2b-inner">
    <div class="reveal">
      <p class="eyebrow" style="margin-bottom:28px; color:var(--tan)">For The Professional Kitchen</p>
      <h2>Built from a<br/><em>Bay Area wholesale</em><br/>bloodline.</h2>
      <p>Our roots are in the family's farm-to-market wholesale business supplying restaurants and grocery stores across the Bay Area. We bring that relationship-first approach to the counter — and to the chefs, cooks and kitchens who already walk through our door.</p>
      <div class="cta">
        <a class="btn ember" href="tel:+14155292349">Contact Our Team <svg class="arrow" viewBox="0 0 14 10" fill="none"><path d="M1 5h12M9 1l4 4-4 4" stroke="currentColor" stroke-width="1.4"/></svg></a>
        <a class="btn" href="tel:+14155292349">Call (415) 529-2349</a>
      </div>
    </div>
    <aside class="b2b-side reveal d1">
      <h4>Talk To Us About</h4>
      <ul>
        <li>Hand-selected Wagyu, dry-aged beef and heritage cuts for your menu</li>
        <li>Custom portioning and off-list cuts</li>
        <li>Whole-animal arrangements and private tastings</li>
        <li>Private butchery demonstrations and group classes</li>
        <li>Bottle pairings and sommelier-assisted selections</li>
      </ul>
    </aside>
  </div>
</section>

<section class="contact-bar">
  <div class="wrap contact-bar-inner">
    <div class="reveal">
      <p class="eyebrow" style="margin-bottom:28px; color:var(--tan)">Contact</p>
      <h2>Hand-cut, by<br/><em>phone or in person.</em></h2>
      <p>Reserve a cut, book a class, ask what's on the block, or plan an event — the best way is still a call. For everything else, we're on the corner.</p>
    </div>
    <div class="ctas reveal d1">
      <a class="btn solid" href="tel:+14155292349">Call (415) 529-2349 <svg class="arrow" viewBox="0 0 14 10" fill="none"><path d="M1 5h12M9 1l4 4-4 4" stroke="currentColor" stroke-width="1.4"/></svg></a>
      <a class="btn" href="https://maps.google.com/?q=320+Fell+Street+San+Francisco+CA+94102" target="_blank" rel="noreferrer">Get Directions</a>
    </div>
  </div>
</section>

''' + next_page("Back to About", "index.html", 1, "Start<br/><em>Over.</em>")


# -------- Write pages --------
pages = [
    ('index.html', 'About', 'A family-run Hayes Valley butcher shop at 320 Fell Street — dry-aged beef, Wagyu, sandwiches, and butchery classes.', 'https://sfmeatco.com/', ABOUT_BODY),
    ('mission.html', 'Mission', 'Our vision: become the community\'s go-to destination for high-quality meats and exceptional service.', 'https://sfmeatco.com/mission.html', MISSION_BODY),
    ('services.html', 'Services', 'Specialty dry aging, custom orders, wholesale, catering, expert advice and butchery workshops.', 'https://sfmeatco.com/services.html', SERVICES_BODY),
    ('menu.html', 'Menu', 'Dry-aged Angus, Japanese and domestic Wagyu, pork, lamb, poultry and sandwiches at the Hayes Valley counter.', 'https://sfmeatco.com/menu.html', MENU_BODY),
    ('visit.html', 'Visit', '320 Fell Street, Hayes Valley, San Francisco · (415) 529-2349 · hours, map, and contact.', 'https://sfmeatco.com/visit.html', VISIT_BODY),
]

for fname, title, desc, canonical, body in pages:
    with open(fname, 'w') as f:
        f.write(page(title, desc, canonical, body))
    print(f'wrote {fname} ({os.path.getsize(fname)} bytes)')
