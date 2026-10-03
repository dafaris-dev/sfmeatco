"""Build 5 pages from shared template + per-page content."""
import os

NAV = '''<header class="nav" id="nav">
  <a class="brand" href="index.html" aria-label="San Francisco Meat Co. — home">
    <img class="brand-logo" src="assets/logo.png" alt="San Francisco Meat Co." width="140" height="88"/>
  </a>
  <nav class="nav-links" aria-label="Primary">
    <a href="index.html"    data-page="index.html">About</a>
    <a href="review.html"   data-page="review.html">Review</a>
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
    <a href="review.html"   data-page="review.html">Review</a>
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

FOOTER = '''<footer class="footer-mini">
  <div class="wrap">
    <div>© <span id="yr">2026</span> San Francisco Meat Co. · 320 Fell Street, San Francisco</div>
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
    <p class="page-crumb">Page 01 of 06 · About</p>
    <h1>We're the <em>new guys</em><br/>on the block.</h1>
    <div class="page-meta">
      <div><small>Established</small><strong>2023</strong></div>
      <div><small>Neighborhood</small><strong>Hayes Valley</strong></div>
      <div><small>Address</small><strong>320 Fell Street</strong></div>
      <div><small>Founders</small><strong>Seabridge &amp; Nishikawa</strong></div>
    </div>
    <div class="mercato-wrap">
      <a class="mercato-btn"
         href="https://www.mercato.com/shop/san-francisco-meat-co?utm_source=2651.San_Francisco_Meat_Co.&amp;utm_medium=shopnow"
         target="_blank" rel="noreferrer"
         aria-label="Order local delivery with Mercato (opens in new tab)">
        <span>Local delivery with</span>
        <strong>mercato<span class="dot">&#769;</span></strong>
      </a>
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
        <p>At San Francisco Meat Co., we believe great meals start with great ingredients. That's why we source only the finest meats, from imported Japanese Wagyu to premium, hand-selected cuts, and bring them straight to your kitchen with care and consistency.</p>
        <p>Whether you're preparing a weeknight dinner or celebrating life's special moments, our meats are chosen for their flavor, quality, and reliability. With San Francisco Meat Co., you're not just buying meat. You're bringing home a culinary experience built on craftsmanship, trust, and tradition.</p>
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
        <p>At San Francisco Meat Co., we're a family-owned butchery proudly serving our community with premium meats and personalized service. Our roots run three generations deep, through Justin Seabridge's father, who built a farm-to-market wholesale business supplying Bay Area restaurants and grocers for decades, and the hunting trips through Wyoming and Colorado where Justin first learned to work a whole animal.</p>
        <p>Whether you're a professional chef or a home cook, we offer the same exceptional care and attention to detail in every cut. From classic favorites to specialty selections, our meats are chosen for superior flavor, tenderness, and quality.</p>
        <p>We believe great meals start with great ingredients, and we're here to make sure every meal you prepare is nothing short of delicious.</p>
      </div>
      <figure class="pic reveal d1">
        <img src="assets/5.webp" alt="Hand-selected raw ribeye with vintage carving fork" loading="lazy"/>
        <span class="cap">Hand-Cut · In-House</span>
      </figure>
    </div>

    <div class="timeline reveal" aria-label="Company timeline">
      <div class="tr"><div class="yr">Earlier</div><div class="tx"><strong>Family wholesale.</strong> Justin's father builds a farm-to-market wholesale business supplying Bay Area restaurants and grocers for decades.</div></div>
      <div class="tr"><div class="yr">Young</div><div class="tx"><strong>Hunting trips west.</strong> Justin learns to break down wild game on family trips through Wyoming and Colorado.</div></div>
      <div class="tr"><div class="yr">2023</div><div class="tx"><strong>Hayes Valley opens.</strong> San Francisco Meat Co. opens on the former Fatted Calf corner at 320 Fell Street. Counter, dry agers, kitchen and wine license intact.</div></div>
      <div class="tr"><div class="yr">Today</div><div class="tx"><strong>A working butcher shop.</strong> Hand-cut counter, dry-aged beef, Wagyu, sandwiches, bottles, and a classroom running on quieter weeks.</div></div>
    </div>
  </div>
</section>

''' + next_page("Reviews", "review.html", 2, "Our<br/><em>Reviews.</em>")


REVIEW_BODY = '''<section class="reviews-page">
  <div class="reviews-bg" aria-hidden="true"></div>
  <div class="wrap">
    <p class="page-crumb" style="justify-content:center; color:var(--paper); margin-bottom:28px">Page 02 of 06 · Reviews</p>
    <h1 class="reviews-title">Reviews</h1>

    <a class="yelp-summary"
       href="https://www.yelp.com/biz/san-francisco-meat-co-san-francisco-7"
       target="_blank" rel="noreferrer"
       aria-label="See all reviews on Yelp (opens in new tab)">
      <span class="yelp-logo" aria-hidden="true">
        <svg viewBox="0 0 48 48"><rect width="48" height="48" rx="8" fill="#d32323"/><path d="M22 10c-5 1-9 3-9 3l3 10c1 2 3 1 3 1l3-1V10zm2 15l-1 3c-1 2 1 3 1 3l8 2s2 1 2-1l1-5c0-2-2-2-2-2l-8-1s-1-1-1 1zm10-6l-6 4s-1 1 0 2l5 5s1 1 3-1l3-4s1-1-1-3zm-15 7l-3 2c-2 1-1 3-1 3l4 6s1 2 2 0l1-8s0-2-2-3zm9 7l-2 8c0 2 2 1 2 1l5-5c1-2 0-3 0-3l-3-2c-2-1-2 1-2 1z" fill="#fff"/></svg>
      </span>
      <span class="yelp-rating">4.5</span>
      <span class="yelp-stars" aria-label="4.5 out of 5 stars">
        <svg viewBox="0 0 100 20" aria-hidden="true">
          <defs>
            <polygon id="rs" points="10,0 12.5,7 20,7 14,11.5 16,19 10,14.5 4,19 6,11.5 0,7 7.5,7"/>
          </defs>
          <use href="#rs" x="0" fill="#f5c518"/>
          <use href="#rs" x="20" fill="#f5c518"/>
          <use href="#rs" x="40" fill="#f5c518"/>
          <use href="#rs" x="60" fill="#f5c518"/>
          <use href="#rs" x="80" fill="#dadada"/>
          <use href="#rs" x="80" fill="#f5c518" clip-path="inset(0 50% 0 0)"/>
        </svg>
      </span>
      <span class="yelp-info">
        <strong>San Francisco Meat Co</strong>
        <span>86 Reviews</span>
      </span>
    </a>

    <div class="review-cards">
      <!-- Card 1 -->
      <a class="review-card" href="https://www.yelp.com/biz/san-francisco-meat-co-san-francisco-7" target="_blank" rel="noreferrer" aria-label="Read Matthew L.'s review on Yelp">
        <div class="rc-avatar rc-avatar--letter" style="background:#b8b8b8">M</div>
        <div class="rc-stars" aria-label="5 out of 5 stars">
          <svg viewBox="0 0 100 20" aria-hidden="true"><use href="#rs" x="0" fill="#f5c518"/><use href="#rs" x="20" fill="#f5c518"/><use href="#rs" x="40" fill="#f5c518"/><use href="#rs" x="60" fill="#f5c518"/><use href="#rs" x="80" fill="#f5c518"/></svg>
        </div>
        <p class="rc-quote">"This place has the kind of old-school neighborhood fe..."</p>
        <span class="rc-link">Read full review &#9654;</span>
        <div class="rc-byline">
          <span class="rc-y" aria-hidden="true"><svg viewBox="0 0 48 48"><rect width="48" height="48" rx="6" fill="#d32323"/><path d="M22 10c-5 1-9 3-9 3l3 10c1 2 3 1 3 1l3-1V10zm2 15l-1 3c-1 2 1 3 1 3l8 2s2 1 2-1l1-5c0-2-2-2-2-2l-8-1s-1-1-1 1zm10-6l-6 4s-1 1 0 2l5 5s1 1 3-1l3-4s1-1-1-3zm-15 7l-3 2c-2 1-1 3-1 3l4 6s1 2 2 0l1-8s0-2-2-3zm9 7l-2 8c0 2 2 1 2 1l5-5c1-2 0-3 0-3l-3-2c-2-1-2 1-2 1z" fill="#fff"/></svg></span>
          <span>Matthew L. · 8/11/2026</span>
        </div>
      </a>

      <!-- Card 2 -->
      <a class="review-card" href="https://www.yelp.com/biz/san-francisco-meat-co-san-francisco-7" target="_blank" rel="noreferrer" aria-label="Read Thomas R.'s review on Yelp">
        <div class="rc-avatar" style="background:linear-gradient(135deg,#a67a4a,#4a3220)">T</div>
        <div class="rc-stars" aria-label="4 out of 5 stars">
          <svg viewBox="0 0 100 20" aria-hidden="true"><use href="#rs" x="0" fill="#f5c518"/><use href="#rs" x="20" fill="#f5c518"/><use href="#rs" x="40" fill="#f5c518"/><use href="#rs" x="60" fill="#f5c518"/><use href="#rs" x="80" fill="#dadada"/></svg>
        </div>
        <p class="rc-quote">"San Francisco Meat Co has caught my eye every time I'..."</p>
        <span class="rc-link">Read full review &#9654;</span>
        <div class="rc-byline">
          <span class="rc-y" aria-hidden="true"><svg viewBox="0 0 48 48"><rect width="48" height="48" rx="6" fill="#d32323"/><path d="M22 10c-5 1-9 3-9 3l3 10c1 2 3 1 3 1l3-1V10zm2 15l-1 3c-1 2 1 3 1 3l8 2s2 1 2-1l1-5c0-2-2-2-2-2l-8-1s-1-1-1 1zm10-6l-6 4s-1 1 0 2l5 5s1 1 3-1l3-4s1-1-1-3zm-15 7l-3 2c-2 1-1 3-1 3l4 6s1 2 2 0l1-8s0-2-2-3zm9 7l-2 8c0 2 2 1 2 1l5-5c1-2 0-3 0-3l-3-2c-2-1-2 1-2 1z" fill="#fff"/></svg></span>
          <span>Thomas R. · 7/23/2026</span>
        </div>
      </a>

      <!-- Card 3 -->
      <a class="review-card" href="https://www.yelp.com/biz/san-francisco-meat-co-san-francisco-7" target="_blank" rel="noreferrer" aria-label="Read Iris H.'s review on Yelp">
        <div class="rc-avatar" style="background:linear-gradient(135deg,#4a2a2a,#2a1612)">I</div>
        <div class="rc-stars" aria-label="2 out of 5 stars">
          <svg viewBox="0 0 100 20" aria-hidden="true"><use href="#rs" x="0" fill="#f5c518"/><use href="#rs" x="20" fill="#f5c518"/><use href="#rs" x="40" fill="#dadada"/><use href="#rs" x="60" fill="#dadada"/><use href="#rs" x="80" fill="#dadada"/></svg>
        </div>
        <p class="rc-quote">"I have been trying to support this place for years. I've liv..."</p>
        <span class="rc-link">Read full review &#9654;</span>
        <div class="rc-byline">
          <span class="rc-y" aria-hidden="true"><svg viewBox="0 0 48 48"><rect width="48" height="48" rx="6" fill="#d32323"/><path d="M22 10c-5 1-9 3-9 3l3 10c1 2 3 1 3 1l3-1V10zm2 15l-1 3c-1 2 1 3 1 3l8 2s2 1 2-1l1-5c0-2-2-2-2-2l-8-1s-1-1-1 1zm10-6l-6 4s-1 1 0 2l5 5s1 1 3-1l3-4s1-1-1-3zm-15 7l-3 2c-2 1-1 3-1 3l4 6s1 2 2 0l1-8s0-2-2-3zm9 7l-2 8c0 2 2 1 2 1l5-5c1-2 0-3 0-3l-3-2c-2-1-2 1-2 1z" fill="#fff"/></svg></span>
          <span>Iris H. · 4/12/2026</span>
        </div>
      </a>
    </div>

    <div class="reviews-cta">
      <a class="btn solid" href="https://www.yelp.com/biz/san-francisco-meat-co-san-francisco-7" target="_blank" rel="noreferrer">
        See All 86 Reviews on Yelp
        <svg class="arrow" viewBox="0 0 14 10" fill="none" aria-hidden="true"><path d="M1 5h12M9 1l4 4-4 4" stroke="currentColor" stroke-width="1.4"/></svg>
      </a>
    </div>
  </div>
</section>

''' + next_page("Our Mission", "mission.html", 3, "Our<br/><em>Mission.</em>")


MISSION_BODY = '''<section class="page-hero">
  <div class="wrap">
    <p class="page-crumb">Page 03 of 06 · Mission</p>
    <h1>The community's<br/><em>go-to butcher.</em></h1>
  </div>
</section>

<section class="sec craft" id="craft">
  <div class="wrap">
    <div class="values-head reveal" style="margin-top:0; border-top:0; padding-top:0">
      <p class="eyebrow" style="color:var(--tan); margin-bottom:18px">Our Vision</p>
      <h3 class="values-title">Five principles<br/><em>we work by.</em></h3>
    </div>

    <div class="grid3 values">
      <div class="cell reveal"><span class="num">01</span><div><h3>Quality</h3><p>The quality of our meats is the foundation of our business. We're committed to sourcing only the freshest, most flavorful, and ethically raised meats from trusted local suppliers. Every piece is carefully selected and hand-cut to meet our exacting standards for taste, tenderness, and texture.</p></div></div>
      <div class="cell reveal d1"><span class="num">02</span><div><h3>Service</h3><p>We're dedicated to providing exceptional service. Our knowledgeable, friendly staff is always available to offer expert advice, help with special orders, and share cooking tips and recipes, building long relationships, learning your preferences, and going the extra mile to exceed expectations.</p></div></div>
      <div class="cell reveal d2"><span class="num">03</span><div><h3>Community</h3><p>We actively collaborate with local farmers and ranchers who share our values of sustainability, animal welfare, and environmentally responsible practices. Promoting local agriculture contributes to the economic vitality and food security of our community, while reducing our carbon footprint.</p></div></div>
      <div class="cell reveal"><span class="num">04</span><div><h3>Education</h3><p>We're committed to educating our customers about the value of high-quality meats and the importance of knowing where their food comes from. By sharing what we know about meat production and processing, we help our customers make informed choices that align with their values and dietary needs.</p></div></div>
      <div class="cell reveal d1"><span class="num">05</span><div><h3>Innovation</h3><p>We embrace innovation as a means to continually improve and evolve, always on the lookout for new techniques, technologies, and trends in the meat industry that can enhance the quality, sustainability, and convenience of what we offer, and the service around it.</p></div></div>
      <div class="cell cell--quote reveal d2"><span class="num">The Shop</span><div><h3 class="q">A trusted partner,<br/><em>not just a butcher shop.</em></h3><p>With our commitment to quality, service, community, education and innovation, we strive to make a lasting impact on the lives of our customers and our local community, helping families make delicious, wholesome, and sustainable choices every day.</p></div></div>
    </div>
  </div>
</section>

''' + next_page("Services", "services.html", 4, "Our<br/><em>Services.</em>")


SERVICES_BODY = '''<section class="page-hero">
  <div class="wrap">
    <p class="page-crumb">Page 04 of 06 · Services</p>
    <h1>What <em>we do</em><br/>on the block.</h1>
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
        <p>At San Francisco Meat Co., our dry aging process is a blend of time, science, and craftsmanship. In our temperature- and humidity-controlled aging room, premium beef cuts rest and develop unparalleled depth of flavor, tenderness, and aroma. Over several weeks, natural enzymes break down muscle fibers while the outer layer forms a protective crust, concentrating the meat's rich, buttery essence. The result is an exceptional steak experience, bold, complex, and unmistakably San Francisco Meat Co. quality.</p>
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
      <article class="svc reveal"><span class="idx">01</span><h3>Fresh <em>Meat</em> Daily</h3><p>A hand-cut counter stocked and rotated every day, with dry-aged Angus, Wagyu, pork, lamb and poultry pulled, trimmed and portioned to order.</p><a class="cta" href="menu.html">Today's Case <svg class="arrow" viewBox="0 0 28 8" fill="none"><path d="M0 4h26M22 1l5 3-5 3" stroke="currentColor" stroke-width="1.2"/></svg></a></article>
      <article class="svc reveal d1"><span class="idx">02</span><h3>Dry <em>Aging</em></h3><p>Our dry aging program brings out the very best in premium beef. Using carefully controlled temperature, humidity and airflow, select cuts develop unmatched tenderness and rich, concentrated flavor, monitored throughout for consistency and excellence.</p><a class="cta" href="visit.html">Programs <svg class="arrow" viewBox="0 0 28 8" fill="none"><path d="M0 4h26M22 1l5 3-5 3" stroke="currentColor" stroke-width="1.2"/></svg></a></article>
      <article class="svc reveal d2"><span class="idx">03</span><h3>Custom <em>Orders</em></h3><p>Every customer has unique preferences when it comes to cuts. Our skilled butchers are trained in the art of custom butchering and can prepare meat to your exact specifications, from special cuts to portioning or trimming, done to order.</p><a class="cta" href="visit.html">Request <svg class="arrow" viewBox="0 0 28 8" fill="none"><path d="M0 4h26M22 1l5 3-5 3" stroke="currentColor" stroke-width="1.2"/></svg></a></article>
      <article class="svc reveal"><span class="idx">04</span><h3>Wholesale <em>&amp;</em> Bulk Orders</h3><p>We cater to the needs of restaurants, caterers and other businesses that require meat in larger quantities. Wholesale and bulk ordering options at competitive prices. Contact us to discuss your needs and we'll work with you to fulfill them.</p><a class="cta" href="visit.html">Talk To Us <svg class="arrow" viewBox="0 0 28 8" fill="none"><path d="M0 4h26M22 1l5 3-5 3" stroke="currentColor" stroke-width="1.2"/></svg></a></article>
      <article class="svc reveal d1"><span class="idx">05</span><h3>Catering <em>&amp;</em> Events</h3><p>Hosting a special event? Let us take care of the meat. Catering for weddings, parties and other occasions. Contact us for more details.</p><a class="cta" href="visit.html">Enquire <svg class="arrow" viewBox="0 0 28 8" fill="none"><path d="M0 4h26M22 1l5 3-5 3" stroke="currentColor" stroke-width="1.2"/></svg></a></article>
      <article class="svc reveal d2"><span class="idx">06</span><h3>Expert <em>Advice</em></h3><p>Our knowledgeable staff is always available for expert advice on meat selection, preparation and cooking: the perfect cut for your recipe, cooking tips, and answers to anything you want to know about our products.</p><a class="cta" href="visit.html">Come In <svg class="arrow" viewBox="0 0 28 8" fill="none"><path d="M0 4h26M22 1l5 3-5 3" stroke="currentColor" stroke-width="1.2"/></svg></a></article>
      <article class="svc reveal"><span class="idx">07</span><h3>Events <em>&amp;</em> Workshops</h3><p>We foster community and share our love for meat through events and workshops: tastings, cooking demonstrations and butchery classes (poultry, lamb and half-a-hog breakdowns) that bring customers and meat enthusiasts together.</p><a class="cta" href="visit.html">Schedule <svg class="arrow" viewBox="0 0 28 8" fill="none"><path d="M0 4h26M22 1l5 3-5 3" stroke="currentColor" stroke-width="1.2"/></svg></a></article>
    </div>
  </div>
</section>

''' + next_page("Menu", "menu.html", 5, "Our<br/><em>Menu.</em>")


MENU_BODY = '''<section class="sec sec-dark sandwich-menu" style="padding-top:clamp(140px, 15vw, 200px)">
  <div class="wrap">
    <div class="section-head reveal" style="margin-bottom:48px">
      <div>
        <p class="eyebrow" style="margin-bottom:24px">Sandwich Menu</p>
        <h2>Specialty<br/><span style="font-style:italic;color:var(--tan);font-weight:300">Sandwiches.</span></h2>
      </div>
      <p class="lead" style="color:var(--bone)">
        Handcrafted artisanal sandwiches, built to order on the bread of your choice:
        Dutch Crunch, Sweet Roll, Sliced Rye, or Sliced Sourdough.
      </p>
    </div>

    <div class="sw-list">

      <!-- 01 -->
      <article class="sw-row reveal">
        <span class="sw-num">01</span>
        <div class="sw-img">
          <img src="assets/sw-01-rueben.png" alt="Rueben sandwich with pastrami, Swiss, and sauerkraut on sliced rye" loading="lazy" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover"/>
        </div>
        <div class="sw-copy">
          <h3>Rueben</h3>
          <p class="ing">Pastrami · Swiss Cheese · Sauerkraut · Thousand Island · Sliced Rye</p>
        </div>
      </article>

      <!-- 02 -->
      <article class="sw-row reveal">
        <span class="sw-num">02</span>
        <div class="sw-img">
          <img src="assets/sw-02-turkey.webp" alt="Turkey sandwich with bacon, cheddar, lettuce and tomato on dutch crunch roll" loading="lazy" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover"/>
        </div>
        <div class="sw-copy">
          <h3>Turkey</h3>
          <p class="ing">Deli Turkey · Sliced Bacon · Cheddar · Lettuce · Tomato · Mayo</p>
        </div>
      </article>

      <!-- 03 -->
      <article class="sw-row reveal">
        <span class="sw-num">03</span>
        <div class="sw-img">
          <img src="assets/sw-03-ham-cheese.webp" alt="Ham and cheese sandwich with pimento cheese, pickled jalapeño, tomato and lettuce on a soft roll" loading="lazy" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover"/>
        </div>
        <div class="sw-copy">
          <h3>Ham and Cheese</h3>
          <p class="ing">Ham · Cheddar · Pimento Cheese · Pickled Jalapeño · Mayo · Tomato · Lettuce</p>
        </div>
      </article>

      <!-- 04 -->
      <article class="sw-row reveal">
        <span class="sw-num">04</span>
        <div class="sw-img">
          <img src="assets/sw-04-roast-beef.webp" alt="Roast beef sandwich with mushroom, Swiss, baby kale and balsamic vinaigrette on sliced bread" loading="lazy" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover"/>
        </div>
        <div class="sw-copy">
          <h3>Roast Beef</h3>
          <p class="ing">Roast Beef · Mushroom · Swiss · Mayo · Baby Kale · Balsamic Vinaigrette</p>
        </div>
      </article>

      <!-- 05 -->
      <article class="sw-row reveal">
        <span class="sw-num">05</span>
        <div class="sw-img">
          <img src="assets/sw-05-grilled-cheese.webp" alt="Grilled cheese with caramelized onions, spaghetti squash and baby kale" loading="lazy" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover"/>
        </div>
        <div class="sw-copy">
          <h3>Grilled Cheese</h3>
          <p class="ing">Cheese · Caramelized Onions · Spaghetti Squash · Baby Kale · Apple Cider Vinegar Dressing</p>
        </div>
      </article>

      <!-- 06 -->
      <article class="sw-row reveal">
        <span class="sw-num">06</span>
        <div class="sw-img">
          <img src="assets/sw-06-muffaletta.webp" alt="Muffaletta with mortadella, provolone, olive spread, tomato and lettuce on a rustic roll" loading="lazy" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover"/>
        </div>
        <div class="sw-copy">
          <h3>Muffaletta</h3>
          <p class="ing">Mortadella · Provolone · Olive Spread · Italian Dressing · Lettuce · Tomato · Mayo</p>
        </div>
      </article>

      <!-- 07 -->
      <article class="sw-row reveal">
        <span class="sw-num">07</span>
        <div class="sw-img">
          <img src="assets/sw-07-meatball.webp" alt="Meatball sandwich with house meatballs, tomato sauce, provolone, parmesan and basil on crusty roll" loading="lazy" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover"/>
        </div>
        <div class="sw-copy">
          <h3>Meatball Sandwich</h3>
          <p class="ing">House Meatballs · Tomato Sauce · Provolone · Parmesan · Basil</p>
        </div>
      </article>

      <!-- 08 -->
      <article class="sw-row reveal">
        <span class="sw-num">08</span>
        <div class="sw-img">
          <img src="assets/sw-08-hot-dog.webp" alt="All-beef hot dog with sauerkraut, relish, jalapeños, pickles, pickled onions, ketchup, mustard and mayo on the side" loading="lazy" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover"/>
        </div>
        <div class="sw-copy">
          <h3>All Beef Hot Dog</h3>
          <p class="ing">Sauerkraut · Relish · Jalapeños · Pickles · Onions · Raw Onions · Ketchup · Yellow Mustard · Mayo</p>
        </div>
      </article>

    </div>
  </div>
</section>

''' + next_page("Visit", "visit.html", 6, "Come<br/><em>Visit.</em>")


VISIT_BODY = '''<section class="visit-page" id="contact">
  <div class="wrap visit-page-grid">

    <!-- LEFT: form -->
    <div class="vp-form reveal">
      <p class="vp-eyebrow">Contact Us</p>
      <h2 class="vp-heading">Drop us a line!</h2>
      <form class="form" action="mailto:contact@sfmeatco.com" method="post" enctype="text/plain" novalidate>
        <label class="field"><input type="text" name="name" placeholder="Name" autocomplete="name"/></label>
        <label class="field"><input type="email" name="email" placeholder="Email*" autocomplete="email" required/></label>
        <label class="field"><textarea name="message" rows="6" placeholder="Message"></textarea></label>
        <button class="btn-send" type="submit">Send</button>
        <p class="form-note">
          This site is protected by reCAPTCHA and the Google
          <a href="https://policies.google.com/privacy" target="_blank" rel="noreferrer">Privacy Policy</a>
          and
          <a href="https://policies.google.com/terms" target="_blank" rel="noreferrer">Terms of Service</a>
          apply.
        </p>
      </form>
    </div>

    <!-- RIGHT: in person -->
    <div class="vp-info reveal d1">
      <h2 class="vp-heading">Better yet, see us in person!</h2>
      <p class="vp-lead">We love our customers, so feel free to visit during normal business hours.</p>

      <h3 class="vp-shop">San Francisco Meat Co.</h3>

      <a class="vp-link"
         href="https://www.google.com/maps/search/?api=1&query=320+Fell+Street+San+Francisco+CA+94102"
         target="_blank" rel="noreferrer"
         aria-label="Open 320 Fell Street in Google Maps">
        320 Fell Street, San Francisco, California 94102, United States
      </a>

      <a class="vp-link" href="tel:+14155292349">415-529-2349</a>

      <a class="vp-link" href="mailto:contact@sfmeatco.com">contact@sfmeatco.com</a>

      <h3 class="vp-shop vp-shop--hours">Hours</h3>

      <details class="vp-hours">
        <summary>
          <span class="dot" aria-hidden="true"></span>
          <span class="label"><strong>Open today</strong> <em id="todayHours">10:00 am to 07:00 pm</em></span>
          <svg class="chev" viewBox="0 0 14 8" aria-hidden="true"><path d="M1 1l6 6 6-6" stroke="currentColor" stroke-width="1.6" fill="none" stroke-linecap="round"/></svg>
        </summary>
        <table class="vp-hours-table">
          <tbody>
            <tr><td>Monday</td><td class="closed">Closed</td></tr>
            <tr><td>Tuesday</td><td>10:00 am to 07:00 pm</td></tr>
            <tr><td>Wednesday</td><td>10:00 am to 07:00 pm</td></tr>
            <tr><td>Thursday</td><td>10:00 am to 07:00 pm</td></tr>
            <tr><td>Friday</td><td>10:00 am to 07:00 pm</td></tr>
            <tr><td>Saturday</td><td>10:00 am to 07:00 pm</td></tr>
            <tr><td>Sunday</td><td>11:00 am to 06:00 pm</td></tr>
          </tbody>
        </table>
      </details>
      <p class="vp-holiday">Closed Major Holidays</p>

      <div class="vp-map-ctas">
        <a class="map-btn" href="https://maps.google.com/?q=320+Fell+Street+San+Francisco+CA+94102" target="_blank" rel="noreferrer">
          Open in Google Maps
          <svg viewBox="0 0 14 10" fill="none" aria-hidden="true"><path d="M1 5h12M9 1l4 4-4 4" stroke="currentColor" stroke-width="1.4"/></svg>
        </a>
        <a class="map-btn" href="https://maps.apple.com/?q=San+Francisco+Meat+Co&amp;address=320+Fell+Street,San+Francisco,CA+94102" target="_blank" rel="noreferrer">
          Open in Apple Maps
          <svg viewBox="0 0 14 10" fill="none" aria-hidden="true"><path d="M1 5h12M9 1l4 4-4 4" stroke="currentColor" stroke-width="1.4"/></svg>
        </a>
      </div>
    </div>
  </div>
</section>

''' + next_page("Back to About", "index.html", 1, "Start<br/><em>Over.</em>")


# -------- Write pages --------
pages = [
    ('index.html', 'About', 'A family-run Hayes Valley butcher shop at 320 Fell Street — dry-aged beef, Wagyu, sandwiches, and butchery classes.', 'https://sfmeatco.com/', ABOUT_BODY),
    ('review.html', 'Reviews', '4.5 stars from 86 reviews on Yelp. Read what the Hayes Valley neighborhood has to say about San Francisco Meat Co.', 'https://sfmeatco.com/review.html', REVIEW_BODY),
    ('mission.html', 'Mission', 'Our vision: become the community\'s go-to destination for high-quality meats and exceptional service.', 'https://sfmeatco.com/mission.html', MISSION_BODY),
    ('services.html', 'Services', 'Specialty dry aging, custom orders, wholesale, catering, expert advice and butchery workshops.', 'https://sfmeatco.com/services.html', SERVICES_BODY),
    ('menu.html', 'Menu', 'Dry-aged Angus, Japanese and domestic Wagyu, pork, lamb, poultry and sandwiches at the Hayes Valley counter.', 'https://sfmeatco.com/menu.html', MENU_BODY),
    ('visit.html', 'Visit', '320 Fell Street, Hayes Valley, San Francisco · (415) 529-2349 · hours, map, and contact.', 'https://sfmeatco.com/visit.html', VISIT_BODY),
]

for fname, title, desc, canonical, body in pages:
    with open(fname, 'w') as f:
        f.write(page(title, desc, canonical, body))
    print(f'wrote {fname} ({os.path.getsize(fname)} bytes)')
