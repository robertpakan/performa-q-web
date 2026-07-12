#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PERFORMA-Q website builder — generates static pages with shared shell."""
import os

OUT = os.path.dirname(os.path.abspath(__file__))

MUSTACHE = '''<svg class="stache" viewBox="0 0 60 24" aria-hidden="true"><path fill="#23CE4B" d="M30 10 C26 2 16 0 9 4 C3 7 1 14 5 18 C9 22 16 21 19 16 C21 13 24 12 27 13 L30 14 L33 13 C36 12 39 13 41 16 C44 21 51 22 55 18 C59 14 57 7 51 4 C44 0 34 2 30 10 Z"/></svg>'''

QBUG_FAVICON = ("data:image/svg+xml," +
  "%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E"
  "%3Crect width='64' height='64' fill='%2317150F'/%3E"
  "%3Cpath d='M17 40 L25 24 L33 40 Z' fill='%2323CE4B'/%3E"
  "%3Ctext x='38' y='42' font-family='Arial Black,Arial' font-size='26' font-weight='900' fill='%23F1EDE2'%3EQ%3C/text%3E"
  "%3C/svg%3E")

EU_FLAG = '''<svg width="66" height="44" viewBox="0 0 66 44" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Flag of the European Union"><rect width="66" height="44" fill="#003399"/><g fill="#FFCC00"><path d="M33.00 4.89L33.55 6.58L35.32 6.58L33.89 7.62L34.44 9.31L33.00 8.27L31.56 9.31L32.11 7.62L30.68 6.58L32.45 6.58Z"/><path d="M40.33 6.85L40.88 8.54L42.66 8.54L41.22 9.59L41.77 11.28L40.33 10.23L38.90 11.28L39.45 9.59L38.01 8.54L39.78 8.54Z"/><path d="M45.70 12.22L46.25 13.91L48.03 13.91L46.59 14.96L47.14 16.64L45.70 15.60L44.26 16.64L44.81 14.96L43.38 13.91L45.15 13.91Z"/><path d="M47.67 19.56L48.22 21.24L49.99 21.24L48.55 22.29L49.10 23.98L47.67 22.93L46.23 23.98L46.78 22.29L45.34 21.24L47.12 21.24Z"/><path d="M45.70 26.89L46.25 28.58L48.03 28.58L46.59 29.62L47.14 31.31L45.70 30.27L44.26 31.31L44.81 29.62L43.38 28.58L45.15 28.58Z"/><path d="M40.33 32.26L40.88 33.95L42.66 33.95L41.22 34.99L41.77 36.68L40.33 35.64L38.90 36.68L39.45 34.99L38.01 33.95L39.78 33.95Z"/><path d="M33.00 34.22L33.55 35.91L35.32 35.91L33.89 36.96L34.44 38.64L33.00 37.60L31.56 38.64L32.11 36.96L30.68 35.91L32.45 35.91Z"/><path d="M25.67 32.26L26.22 33.95L27.99 33.95L26.55 34.99L27.10 36.68L25.67 35.64L24.23 36.68L24.78 34.99L23.34 33.95L25.12 33.95Z"/><path d="M20.30 26.89L20.85 28.58L22.62 28.58L21.19 29.62L21.74 31.31L20.30 30.27L18.86 31.31L19.41 29.62L17.97 28.58L19.75 28.58Z"/><path d="M18.33 19.56L18.88 21.24L20.66 21.24L19.22 22.29L19.77 23.98L18.33 22.93L16.90 23.98L17.45 22.29L16.01 21.24L17.78 21.24Z"/><path d="M20.30 12.22L20.85 13.91L22.62 13.91L21.19 14.96L21.74 16.64L20.30 15.60L18.86 16.64L19.41 14.96L17.97 13.91L19.75 13.91Z"/><path d="M25.67 6.85L26.22 8.54L27.99 8.54L26.55 9.59L27.10 11.28L25.67 10.23L24.23 11.28L24.78 9.59L23.34 8.54L25.12 8.54Z"/></g></svg>'''

NAV_ITEMS = [
    ("index.html", "Home"),
    ("about.html", "About"),
    ("residency.html", "Residency"),
    ("qtheq.html", "QTHEQ Archive"),
    ("consortium.html", "Consortium"),
    ("open-call.html", "Open Call"),
]

SLOGANS = {
    "work":    ('THE STAGE HONORS <em>EVERY ROLE.</em>', 'work-facing'),
    "stage":   ('THE STAGE REVEALS <em>THE UNSEEN.</em>', 'stage-facing'),
    "archive": ('THE STAGE REMEMBERS <em>WHAT HISTORY ERASED.</em>', 'archive-facing'),
}

def head(title, desc, page):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="https://www.performa-q.eu/{'' if page=='index.html' else page}">
<meta property="og:image" content="https://www.performa-q.eu/img/hero-home.webp">
<link rel="icon" href="{QBUG_FAVICON}">
<link rel="stylesheet" href="css/style.css">
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
'''

def header(page):
    links = "\n".join(
        f'      <a href="{href}"{" aria-current=\"page\"" if href == page else ""}>{label}</a>'
        for href, label in NAV_ITEMS if href not in ("index.html", "open-call.html"))
    return f'''<header class="site-head">
  <div class="bar">
    <a class="brand" href="index.html" aria-label="PERFORMA-Q — home">
      <span class="wm">PERFORMA-Q{MUSTACHE}</span>
      <span class="tag">European Queer Performing Arts Platform</span>
    </a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="mainnav">Menu</button>
    <nav class="main" id="mainnav" aria-label="Main">
{links}
      <a class="btn" href="open-call.html">Open Call</a>
    </nav>
  </div>
</header>
'''

def slogan_band(kind):
    text, _ = SLOGANS[kind]
    unit = f'<span>{text}</span>' * 4
    return f'''<div class="slogan-band" aria-hidden="true"><div class="inner">{unit}{unit}</div></div>
'''

def deadline_strip():
    return '''<div class="deadline-strip"><div class="in" data-deadline-msg>
  <span>Open Call · Cycle 1 closes 31 July 2026</span>
  <span aria-hidden="true">▲</span>
  <span><span data-count="days">–</span>d : <span data-count="hours">–</span>h : <span data-count="minutes">–</span>m left</span>
  <span aria-hidden="true">▲</span>
  <a href="open-call.html">Apply now</a>
</div></div>
'''

def footer(page):
    return f'''<footer class="site on-dark">
  <div class="wrap">
    <div class="footer-verbs" aria-hidden="true">Honors. Reveals.<br>Remembers. <span class="l">Laughs.</span></div>
    <div class="cols">
      <div>
        <h4>PERFORMA-Q</h4>
        <p style="max-width:44ch;font-size:15px">Stage for untold and erased queer stories from Europe's periphery. A transnational platform for residencies, touring and a living video archive — built by six partners across Europe.</p>
      </div>
      <div>
        <h4>Explore</h4>
        <ul>
          <li><a href="about.html">About the project</a></li>
          <li><a href="residency.html">Residency programme</a></li>
          <li><a href="qtheq.html">QTHEQ Video Archive</a></li>
          <li><a href="consortium.html">The Consortium</a></li>
          <li><a href="open-call.html">Open Call · Cycle 1</a></li>
        </ul>
      </div>
      <div>
        <h4>Contact</h4>
        <ul>
          <li><a href="index.html#contact">Write to us</a></li>
          <li><a href="https://www.instagram.com/nomantinels/" rel="noopener">Instagram</a></li>
          <li><a href="https://www.facebook.com/profile.php?id=61590369524751" rel="noopener">Facebook</a></li>
        </ul>
      </div>
    </div>
    <div class="eu-note">
      {EU_FLAG}
      <p><strong>Co-funded by the European Union.</strong> PERFORMA-Q is a transnational European platform, co-funded by the Creative Europe Programme of the European Union, implemented in partnership with the PERFORMA-Q Consortium Members: NOMANTINELS (Slovakia), SARTR (Bosnia and Herzegovina), CO.LABS (Czech Republic), Wiener Wortstaetten (Austria), Swedish Performing Arts Coalition (Sweden), and Mariupol Theatre in Exile / UCPE (Ukraine). Views and opinions expressed are those of the authors only and do not necessarily reflect those of the European Union or EACEA. Neither the European Union nor the granting authority can be held responsible for them.</p>
    </div>
    <div class="legal">
      <span>© 2026 NOMANTINELS · All rights reserved</span>
      <span><a href="#" style="border-bottom:2px solid rgba(241,237,226,.4)">Cookies &amp; privacy</a></span>
    </div>
  </div>
</footer>
<script src="js/main.js"></script>
</body>
</html>'''

def page(filename, title, desc, slogan_kind, body, strip=True):
    html = head(title, desc, filename)
    html += header(filename)
    if strip:
        html += deadline_strip()
    html += f'<main id="main">\n{body}\n</main>\n'
    html += slogan_band(slogan_kind)
    html += footer(filename)
    with open(os.path.join(OUT, filename), "w") as f:
        f.write(html)
    print("wrote", filename)

# ============================================================ HOME
home_body = '''
<div class="hero">
  <img class="img" src="img/hero-home.webp" alt="Collage: a drag performer and a person with a signal-green mustache in front of a halftone map of Europe" fetchpriority="high">
  <div class="plate">
    <p class="eyebrow green">European Queer Performing Arts Platform</p>
    <h1>Stage for untold and erased queer stories</h1>
  </div>
</div>

<section>
  <div class="wrap grid-2">
    <div class="rv">
      <p class="eyebrow">What this is</p>
      <h2>From Europe's periphery, to every stage.</h2>
    </div>
    <div class="rv">
      <p>PERFORMA-Q is a three-year, EU co-funded platform for queer performing arts. Six partner organisations — from Bratislava to Sarajevo, Brno to Vienna, Stockholm to Mariupol-in-exile — build residencies, touring routes and a living video archive for stories that dominant stages have ignored or erased.</p>
      <p>We honor the work. We reveal the unseen. We remember what history erased. And we laugh out loud while doing it — because joy is a refusal too.</p>
      <p><a class="btn ghost" href="about.html">About the project</a></p>
    </div>
  </div>
</section>

<section class="band-ink on-dark ruled">
  <div class="wrap">
    <p class="eyebrow green">Open Call · Cycle 1 · closes 31 July 2026</p>
    <div class="grid-2" style="align-items:center">
      <div class="rv">
        <h2>18 residencies.<br>3 years.<br>Cycle 1 is open.</h2>
        <p style="margin-top:20px">Performing artists, directors, playwrights and collectives working with queer identity and marginalisation in and from Europe's periphery — this stage is built for you and with you.</p>
        <p style="display:flex;gap:16px;flex-wrap:wrap;margin-top:26px">
          <a class="btn" href="open-call.html">Read the call &amp; apply</a>
        </p>
      </div>
      <div class="countdown rv" role="timer" aria-label="Time remaining until the application deadline">
        <div class="cell"><span class="n" data-count="days">–</span><span class="l">Days</span></div>
        <div class="cell"><span class="n" data-count="hours">–</span><span class="l">Hours</span></div>
        <div class="cell"><span class="n" data-count="minutes">–</span><span class="l">Minutes</span></div>
        <div class="cell"><span class="n" data-count="seconds">–</span><span class="l">Seconds</span></div>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <p class="eyebrow">PERFORMA-Q in action</p>
    <h2 style="max-width:14ch">Three ways the platform works</h2>
    <div class="grid-3" style="margin-top:44px">
      <div class="tile rv">
        <span class="num">01 · CREATE</span>
        <h3>Residency</h3>
        <p style="font-size:15.5px">Time, care and resources to develop new performance work — 18 residencies across three years, with mentoring, shared facilities and critical companionship. First cycle runs October 2026 – April 2027.</p>
        <a class="more" href="residency.html">Residency programme</a>
      </div>
      <div class="tile rv">
        <span class="num">02 · CIRCULATE</span>
        <h3>Touring &amp; Networking</h3>
        <p style="font-size:15.5px">Selected works travel between partner stages and festivals, building routes for queer performance across borders — and building the alliances that keep it moving after the curtain call.</p>
        <a class="more" href="about.html#touring">How touring works</a>
      </div>
      <div class="tile dark rv">
        <span class="num" style="color:#23CE4B">03 · REMEMBER</span>
        <h3>QTHEQ Video Archive</h3>
        <p style="font-size:15.5px">A living video archive of queer performing arts — documentation, interviews and captured performances, so that what happens on these stages is never erased again.</p>
        <a class="more" href="qtheq.html" style="color:#F1EDE2">Enter the archive</a>
      </div>
    </div>
  </div>
</section>

<section class="band-mustard ruled">
  <div class="wrap grid-2" style="align-items:center">
    <div class="rv">
      <p class="eyebrow">The Consortium</p>
      <h2>Six partners.<br>Six countries.<br>One stage.</h2>
      <p style="margin-top:18px">Led by NOMANTINELS (Bratislava), the consortium spans Slovakia, Bosnia &amp; Herzegovina, Czech Republic, Austria, Sweden and Ukraine.</p>
      <p><a class="btn ghost" href="consortium.html">Meet the partners</a></p>
    </div>
    <figure class="rv" style="margin:0">
      <img src="img/europe-map.webp" alt="Halftone map of Europe collaged with black-and-white portraits wearing green mustaches" style="border:3px solid #17150F">
      <figcaption class="figure-note">The continent is one stage — halftoned in one ink.</figcaption>
    </figure>
  </div>
</section>

<section id="contact">
  <div class="wrap grid-2">
    <div class="rv">
      <p class="eyebrow">Contact us</p>
      <h2>Write to the platform</h2>
      <p>Questions about the residency, touring, or the archive — or press and partnership enquiries. We read everything.</p>
      <div style="display:grid;gap:16px;margin-top:34px;max-width:360px">
        <div class="postit r1">The stage honors every role.</div>
        <div class="postit r2" style="margin-left:34px">The stage reveals the unseen.</div>
        <div class="postit r3">The stage remembers <em>what history erased.</em></div>
      </div>
    </div>
    <form class="contact rv" aria-label="Contact form">
      <div>
        <label for="c-name">Name</label>
        <input id="c-name" name="name" type="text" autocomplete="name" required>
      </div>
      <div>
        <label for="c-topic">Topic</label>
        <select id="c-topic" name="topic">
          <option>Residency</option>
          <option>Touring</option>
          <option>Queer Archive</option>
          <option>Press</option>
          <option>Other</option>
        </select>
      </div>
      <div>
        <label for="c-msg">Message</label>
        <textarea id="c-msg" name="message" required></textarea>
      </div>
      <button class="btn" type="submit">Send message</button>
      <p class="figure-note">Opens your e-mail client — nothing is stored on this site.</p>
    </form>
  </div>
</section>
'''

page("index.html",
     "PERFORMA-Q — Stage for Untold and Erased Queer Stories",
     "PERFORMA-Q is a European Queer Performing Arts Platform: residencies, touring and a living video archive for queer stories from Europe's periphery. Open Call Cycle 1 closes 31 July 2026.",
     "stage", home_body)

# ============================================================ ABOUT
about_body = '''
<div class="hero sub">
  <video class="img" autoplay muted loop playsinline preload="metadata" poster="img/loop-poster.jpg" aria-label="Animated collage: performers with signal-green and ink mustaches over a shifting field of colour shards">
    <source src="video/loop_performa_q.mp4" type="video/mp4">
    <img class="img" src="img/loop-poster.jpg" alt="">
  </video>
  <div class="plate">
    <p class="eyebrow green">About the project</p>
    <h1>A stage built against erasure</h1>
  </div>
</div>

<section>
  <div class="wrap grid-2">
    <div class="rv">
      <p class="eyebrow">The premise</p>
      <p class="serif-pull">"Refusal is the most affirmative thing this platform does."</p>
    </div>
    <div class="rv">
      <p>Queer performing arts from Europe's periphery are made under pressure — defunded, delegitimised, sometimes criminalised. The work exists anyway. What it lacks is infrastructure: time to create, routes to travel, and a memory that outlasts the season.</p>
      <p>PERFORMA-Q builds all three. Over three years, six partner organisations run <strong>18 artistic residencies</strong>, open <strong>touring and networking routes</strong> between their stages, and grow <strong>QTHEQ</strong> — a video archive so that queer performance is documented, citable and impossible to erase.</p>
      <p>The platform is co-funded by the Creative Europe Programme of the European Union and coordinated by NOMANTINELS, the Slovak queer theatre and civic association behind the Drama Queer festival.</p>
    </div>
  </div>
</section>

<section class="band-paper ruled" id="pillars">
  <div class="wrap">
    <p class="eyebrow">How it works</p>
    <h2>Create · Circulate · Remember</h2>
    <ul class="big-list" style="margin-top:36px">
      <li class="rv"><span class="k">01</span><div><h3>Create — the residencies</h3><p>Each cycle hosts artists and collectives for research and creation: shared rehearsal facilities, mentoring, work-in-progress sharings, and honest fees. Process is valued as much as premiere. <a href="residency.html">Residency programme →</a></p></div></li>
      <li class="rv" id="touring"><span class="k">02</span><div><h3>Circulate — touring &amp; networking</h3><p>Work developed on the platform travels between partner stages and allied festivals. Networking events connect artists with presenters, producers and each other — because a periphery connected is a periphery no longer.</p></div></li>
      <li class="rv"><span class="k">03</span><div><h3>Remember — the QTHEQ archive</h3><p>Performances, interviews and documentation enter a living video archive, openly accessible. What history erased once, it will not erase twice. <a href="qtheq.html">Enter the archive →</a></p></div></li>
    </ul>
  </div>
</section>

<section class="band-ink on-dark ruled">
  <div class="wrap">
    <p class="eyebrow green">PERFORMA-Q is</p>
    <h2>Six words we answer to</h2>
    <div class="grid-3" style="margin-top:40px">
      <div class="trait rv" style="background:#C9A227;color:#17150F"><span class="word">Engaged.</span><p>The platform never speaks at people. Every call asks a question, every page invites a click, every show begins with a name and a hand.</p></div>
      <div class="trait rv" style="background:#E8492A"><span class="word">Embraced.</span><p>Everyone who steps in — artist, audience, staff, partner — is met as a person before they are met as a category.</p></div>
      <div class="trait rv" style="background:#1E7F80"><span class="word">Reflected.</span><p>A person who is queer, European, and a performer finds themselves in our images and language without having to translate.</p></div>
      <div class="trait rv" style="background:#B02A6B"><span class="word">Uni<span class="q">Q</span>ue.</span><p>Every artist, work and gesture is one-of-one. We never run "campaigns featuring queer voices" — we run the work of named people.</p></div>
      <div class="trait rv" style="background:#17150F;border:3px solid #F1EDE2"><span class="word">Fearless.</span><p>We do not soften language for the funder, crop faces for the venue, or pretend the work is family-friendly when it is not.</p></div>
      <div class="trait rv" style="background:#8A9A3B;color:#17150F"><span class="word">Empathic.</span><p>We listen before we broadcast, ask before we represent, pay before we credit. Care is procedural, not performative.</p></div>
    </div>
  </div>
</section>

<section class="band-magenta on-dark ruled">
  <div class="wrap grid-2" style="align-items:center">
    <div class="rv">
      <p class="eyebrow" style="color:#F1EDE2">Tone</p>
      <h2>Joy is a refusal.<br>Laughing out loud<br>is a politic.</h2>
    </div>
    <div class="rv">
      <p>A funded artist, paid in full, on a stage that does not flinch, making an audience laugh until they cry — that is the most affirmative refusal of erasure this platform can stage.</p>
      <p>So the archive holds grief and glitter in the same shelf. The residencies make room for rage and for rock-star entrances. Never at the expense of a name, a credit, or a payment. Always at the expense of solemnity.</p>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <p class="eyebrow coral">The platform refuses</p>
    <h2 style="max-width:16ch">Five things, by name</h2>
    <div class="grid-3" style="margin-top:36px;grid-template-columns:repeat(auto-fit,minmax(190px,1fr))">
      <div class="refusal rv">No pink&shy;washing.</div>
      <div class="refusal rv">No discrimi&shy;nation.</div>
      <div class="refusal rv">No hate.</div>
      <div class="refusal rv">No nationa&shy;lism.</div>
      <div class="refusal rv">No manipu&shy;lation.</div>
    </div>
    <p style="margin-top:34px;max-width:64ch">They are non-negotiable, and they are the floor: no co-branding with sponsors who fund anti-queer politics, no flag-only campaigns, no dark patterns in ticketing, no space we cannot keep safe.</p>
  </div>
</section>
'''

page("about.html",
     "About — PERFORMA-Q",
     "What PERFORMA-Q is: an EU co-funded platform of six partners running 18 residencies, touring routes and the QTHEQ video archive for queer performing arts from Europe's periphery.",
     "archive", about_body)

# ============================================================ RESIDENCY
residency_body = '''
<div class="hero sub" style="background:#C9A227">
  <video class="img" autoplay muted loop playsinline preload="metadata" poster="img/residency-ensemble-poster.jpg" aria-label="Animated collage: three performers with mustaches over shifting colour shards" style="opacity:1;object-fit:cover">
    <source src="video/residency_ensemble.mp4" type="video/mp4">
  </video>
  <div class="plate">
    <p class="eyebrow green">Residency programme</p>
    <h1>Time, care and resources to make the work</h1>
  </div>
</div>

<section>
  <div class="wrap grid-2">
    <div class="rv">
      <p class="eyebrow">The frame</p>
      <h2>18 residencies across three years</h2>
    </div>
    <div class="rv">
      <p>The PERFORMA-Q residency is a laboratory for experimental and politically engaged performance — live art, choreography, expanded dramaturgy and hybrid forms that cross stage, visual arts, sound and digital media. Risk-taking is the point: process, research and collective reflection are valued as much as finished results.</p>
      <p>Each residency offers dedicated time and space for research and creation, access to shared rehearsal or work facilities, and guidance from mentors or invited guests, depending on project needs. Residents are connected to local partners, peers and networks — with opportunities for work-in-progress sharings, public presentations, or support toward future production.</p>
    </div>
  </div>
</section>

<section class="band-paper ruled">
  <div class="wrap">
    <p class="eyebrow">Who it is for</p>
    <h2 style="max-width:18ch">Voices from the periphery, centred</h2>
    <div class="grid-2" style="margin-top:34px">
      <div class="rv">
        <p>We welcome performing artists, directors, playwrights and collectives — emerging and established — whose practice is connected to Europe's periphery and its social, cultural or political realities, including artists based elsewhere whose work meaningfully engages with them.</p>
        <p>The programme centres artists who navigate racialized, migrant, working-class, trans, disabled and other intersecting experiences of exclusion — not only as themes, but through the way projects are made, shared and organised.</p>
      </div>
      <div class="rv">
        <p>Especially welcome: projects that trace minoritized lineages, reclaim forgotten archives, or speculate on alternative queer worlds; work engaging memory, loss, care and resilience; new dramaturgies that blur fiction and documentary, rework popular or folk forms, or question who is allowed to speak and be seen.</p>
        <p>Basic accessibility support can be discussed with selected residents within available resources.</p>
      </div>
    </div>
  </div>
</section>

<section class="band-ink on-dark ruled">
  <div class="wrap">
    <p class="eyebrow green">Cycle 1 at a glance</p>
    <h2>October 2026 – April 2027</h2>
    <table class="spec" style="margin-top:30px;color:#F1EDE2">
      <tr><th style="color:#F1EDE2;width:34%">Applications close</th><td>31 July 2026 · complete applications only</td></tr>
      <tr><th style="color:#F1EDE2">Residency period</th><td>October 2026 – April 2027</td></tr>
      <tr><th style="color:#F1EDE2">You submit</th><td>Project description · motivation statement · portfolio or documentation links · short CVs for key collaborators</td></tr>
      <tr><th style="color:#F1EDE2">Selection weighs</th><td>Artistic quality · clarity of intent · feasibility within the framework · relevance to the programme's focus</td></tr>
      <tr><th style="color:#F1EDE2">Hosted by</th><td>Partner organisations across the consortium, matched to project needs</td></tr>
    </table>
    <p style="margin-top:34px"><a class="btn" href="open-call.html">Open Call · read &amp; apply</a></p>
  </div>
</section>
'''

page("residency.html",
     "Residency — PERFORMA-Q",
     "The PERFORMA-Q residency: 18 residencies over three years for experimental, politically engaged queer performance. Cycle 1 runs October 2026 – April 2027; applications close 31 July 2026.",
     "work", residency_body)

# ============================================================ QTHEQ
qtheq_body = '''
<section class="band-ink on-dark" style="padding-top:clamp(64px,10vw,140px)">
  <div class="wrap">
    <p class="eyebrow green">QTHEQ · Video Archive</p>
    <h1 style="max-width:12ch">The stage remembers</h1>
    <p class="serif-pull" style="color:#F1EDE2;margin-top:24px">A cinémathèque for queer performance — recorded, kept, and impossible to erase.</p>
  </div>
</section>

<section class="band-ink on-dark ruled">
  <div class="wrap grid-2">
    <div class="rv">
      <p class="eyebrow green">Why an archive</p>
      <p style="color:#F1EDE2">Performance disappears the moment it ends — and queer performance from Europe's periphery disappears twice: once with the applause, once when funding, politics or fear removes it from the record.</p>
      <p style="color:#F1EDE2">QTHEQ is PERFORMA-Q's answer: a growing video archive of captured performances, artist interviews and residency documentation. Openly accessible, properly credited, built to outlast the project itself.</p>
    </div>
    <div class="rv" style="display:grid;gap:20px">
      <div class="qtheq-card"><h3>Performances</h3><p style="color:#F1EDE2">Full captures of works developed on the platform and staged by the consortium partners.</p></div>
      <div class="qtheq-card"><h3>Voices</h3><p style="color:#F1EDE2">Interviews with artists, makers and organisers — the context around the work, in their own words.</p></div>
      <div class="qtheq-card"><h3>Process</h3><p style="color:#F1EDE2">Residency documentation: rehearsals, sharings, the unfinished and the in-between.</p></div>
    </div>
  </div>
</section>

<section class="band-ink on-dark ruled">
  <div class="wrap" style="text-align:center;padding:20px 0">
    <p class="pixel rv" style="color:#23CE4B;font-size:clamp(18px,3vw,30px)">FIRST RECORDINGS ARRIVE WITH CYCLE 1</p>
    <p class="rv" style="max-width:56ch;margin:16px auto 30px;color:#F1EDE2">The archive grows as the programme does. Want to be told when the first collection opens — or propose material for it?</p>
    <p class="rv"><a class="btn" href="index.html#contact">Contact the archive team</a></p>
  </div>
</section>
'''

page("qtheq.html",
     "QTHEQ Video Archive — PERFORMA-Q",
     "QTHEQ is PERFORMA-Q's living video archive of queer performing arts: captured performances, artist interviews and residency documentation from across Europe's periphery.",
     "archive", qtheq_body)

# ============================================================ CONSORTIUM
# NOTE for editor: verify partner URLs before launch.
PARTNERS = [
    ("SK", "NOMANTINELS", "Lead Coordinator",
     "Queer theatre and civic association in Bratislava — producer of the Drama Queer festival, publisher of QYS magazine, and a long-standing engine of Slovak queer culture. Coordinates the platform.",
     "https://nomantinels.sk"),
    ("BA", "Sarajevski ratni teatar SARTR", "",
     "The Sarajevo War Theatre — founded during the siege of Sarajevo in 1992 — is a stage where theatre has always been an act of resistance and survival.",
     "https://sartr.ba"),
    ("CZ", "CO.LABS", "",
     "Brno-based independent performing arts hub for emerging makers — a space for co-creation, residencies and new dramaturgies in the Czech scene.",
     "https://colabs.cz"),
    ("AT", "Wiener Wortstaetten", "",
     "Viennese intercultural theatre project developing new writing for the stage, with a long practice of amplifying marginalised authors and stories.",
     "https://wortstaetten.at"),
    ("SE", "Swedish Performing Arts Coalition", "",
     "National coalition connecting Sweden's performing arts field — bringing structural know-how, networks and touring capacity to the platform.",
     "https://scensverige.se"),
    ("UA", "Mariupol Theatre in Exile (UCPE)", "",
     "The company of the Mariupol Drama Theatre working in exile — carrying a stage that war tried to erase, and proof of why this platform exists.",
     ""),
]

partner_html = ""
for cc, name, role, desc, url in PARTNERS:
    role_html = f'<span class="role">{role}</span>' if role else ""
    link_html = f'<a class="site" href="{url}" rel="noopener">Website ↗</a>' if url else '<span class="mono" style="font-size:12px;opacity:.6">WEB TBA</span>'
    partner_html += f'''      <div class="partner rv">
        <span class="cc">{cc} · {"★ LEAD" if role else "PARTNER"}</span>
        <div><h3>{name}{role_html}</h3><p>{desc}</p></div>
        {link_html}
      </div>\n'''

consortium_body = f'''
<div class="hero sub" style="background:#1E7F80">
  <img class="img" src="img/europe-map.webp" alt="Halftone map of Europe collaged with portraits of performers wearing green mustaches">
  <div class="plate">
    <p class="eyebrow green">The Consortium</p>
    <h1>Six partners, one stage</h1>
  </div>
</div>

<section>
  <div class="wrap">
    <p class="eyebrow">Who builds the platform</p>
    <h2 style="max-width:20ch">From Bratislava to Mariupol-in-exile</h2>
    <p style="margin:18px 0 44px;max-width:64ch">The consortium deliberately spans Europe's so-called periphery — capitals and cities where queer performance is made against the current. Each partner hosts, tours and documents; together they carry the platform.</p>
    <div>
{partner_html}    </div>
  </div>
</section>

<section class="band-paper ruled">
  <div class="wrap grid-2">
    <div class="rv">
      <p class="eyebrow">Artistic Board</p>
      <h2>Curatorial care, named</h2>
    </div>
    <div class="rv">
      <p>An Artistic Board drawn from across the consortium reviews open calls and accompanies selected residents. Members and profiles will be published here — every PERFORMA-Q decision carries a name, never an anonymous committee.</p>
      <p><a class="btn ghost" href="index.html#contact">Press &amp; partnership enquiries</a></p>
    </div>
  </div>
</section>
'''

page("consortium.html",
     "The Consortium — PERFORMA-Q",
     "Six partners build PERFORMA-Q: NOMANTINELS (SK, lead), SARTR (BA), CO.LABS (CZ), Wiener Wortstaetten (AT), Swedish Performing Arts Coalition (SE) and Mariupol Theatre in Exile / UCPE (UA).",
     "archive", consortium_body)

# ============================================================ OPEN CALL
FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSe9jOwn6hAoRVssOPVfXVTDfvvjDmfLUEJQaMpPHg7H2FH9Pw/viewform?usp=header"
CALLTEXT_URL = "https://drive.google.com/file/d/1g2B9rDTdTe08HfsxBduqLZ1fUkvljoo8/view?usp=sharing"

opencall_body = f'''
<section class="band-sangria on-dark" style="padding-top:clamp(56px,8vw,110px);padding-bottom:0">
  <div class="wrap grid-2" style="align-items:end">
    <div class="rv" style="padding-bottom:clamp(44px,7vw,90px)">
      <p class="eyebrow green">Open Call · Cycle 1 · Residency programme</p>
      <h1 style="font-size:clamp(38px,5vw,74px)">Step onto a stage built for you and with you</h1>
      <div class="countdown" style="margin-top:36px" role="timer" aria-label="Time remaining until the application deadline">
        <div class="cell"><span class="n" data-count="days">–</span><span class="l">Days</span></div>
        <div class="cell"><span class="n" data-count="hours">–</span><span class="l">Hours</span></div>
        <div class="cell"><span class="n" data-count="minutes">–</span><span class="l">Min</span></div>
        <div class="cell"><span class="n" data-count="seconds">–</span><span class="l">Sec</span></div>
      </div>
      <p style="display:flex;gap:16px;flex-wrap:wrap;margin-top:34px">
        <a class="btn" href="{FORM_URL}" rel="noopener">Apply now ↗</a>
        <a class="btn ghost on-ink" href="{CALLTEXT_URL}" rel="noopener" style="color:#F1EDE2">Call text (PDF) ↗</a>
      </p>
    </div>
    <figure class="rv" style="margin:0;align-self:end">
      <div style="display:flex;gap:28px;justify-content:center;align-items:stretch;flex-wrap:wrap">
        <img src="img/poster-opencall.webp" alt="Open call poster: portrait of a performer with a green mustache and the slogan The Stage Honors Every Role — apply now" style="display:block;max-height:560px;width:auto;border:3px solid #17150F">
        <video autoplay muted loop playsinline preload="metadata" poster="img/opencall-tropics-poster.jpg" aria-label="Animated tropical collage: a bright bird among hibiscus flowers and palm leaves over halftone shapes" style="display:block;max-height:560px;width:auto;aspect-ratio:1/1;border:3px solid #17150F;object-fit:cover">
          <source src="video/opencall_tropics.mp4" type="video/mp4">
        </video>
      </div>
    </figure>
  </div>
</section>

<section>
  <div class="wrap grid-2">
    <div class="rv">
      <p class="eyebrow">The invitation</p>
      <h2>Untold and erased queer stories</h2>
    </div>
    <div class="rv">
      <p><strong>Open Call – Cycle 1</strong> of the PERFORMA-Q residency programme invites performing artists, directors, playwrights and collectives whose work confronts queer identity and marginalisation in and from Europe's periphery. We are looking for bold voices ready to reclaim erased histories, challenge dominant narratives, and carve out space for stories that rarely reach the spotlight.</p>
      <p>The residency, running <strong>October 2026 – April 2027</strong>, offers time, care and resources to develop performance projects that center queer lives, struggles and joys at the edges of Europe. Applications are open until <strong>31 July 2026</strong>, and we especially welcome proposals that experiment with form, language and collaboration.</p>
      <p>If your practice is rooted in resistance, community and visibility, this call is an invitation to step onto a stage built for you and with you.</p>
    </div>
  </div>
</section>

<section class="band-paper ruled">
  <div class="wrap">
    <p class="eyebrow">Artistic focus</p>
    <h2 style="max-width:20ch">What we are looking for</h2>
    <div class="grid-2" style="margin-top:34px">
      <div class="rv">
        <p>PERFORMA-Q is dedicated to experimental and politically engaged performance practices that question dominant narratives and open space for queer imaginaries: performance, live art, choreography, expanded dramaturgy and hybrid forms crossing stage, visual arts, sound and digital media. The residency is a laboratory for risk-taking, where process, research and collective reflection are valued as much as finished results.</p>
        <p>A central focus is the exploration of queer histories and futures — especially those silenced, fragmented or erased. We are particularly interested in projects that trace minoritized lineages, reclaim forgotten archives, or speculate on alternative queer worlds; works engaging memory, loss, care and resilience, through intimate gestures or bold public interventions.</p>
      </div>
      <div class="rv">
        <p>The residency centres voices from Europe's periphery and other marginalised positions — artists navigating racialized, migrant, working-class, trans, disabled and other intersecting experiences of exclusion. We encourage proposals addressing intersectionality, decolonial perspectives and structural inequalities, not only as themes but through the ways projects are made, shared and organised. Community-based and collaborative practices building alliances across movements, geographies and generations are strongly supported.</p>
        <p>If your work is grounded in queer and feminist politics, attentive to power relations, and curious about how performance can reimagine social realities — this call is likely for you.</p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <p class="eyebrow">Practical information</p>
    <h2>How to apply</h2>
    <table class="spec" style="margin-top:28px">
      <tr><th style="width:30%">Who can apply</th><td>Performing artists, directors, playwrights and artistic collectives — emerging and established — with practices connected to Europe's periphery or meaningfully engaging with its realities.</td></tr>
      <tr><th>Framework</th><td>18 residencies across three years. This call concerns Cycle 1: October 2026 – April 2027. Each residency offers dedicated time and space, shared facilities, and mentoring matched to project needs.</td></tr>
      <tr><th>Your application</th><td>Concise project description · connection to Europe's periphery or related contexts · goals for the residency · short motivation statement · portfolio or documentation links · brief CVs for key collaborators.</td></tr>
      <tr><th>Deadline</th><td><strong>31 July 2026</strong> — only complete applications received by the deadline are considered.</td></tr>
      <tr><th>Selection</th><td>Artistic quality · clarity of intent · feasibility within the residency framework · relevance to the programme's focus. Applications from artists with diverse backgrounds, working methods and access needs are encouraged.</td></tr>
    </table>
  </div>
</section>

<section class="band-paper ruled">
  <div class="wrap">
    <p class="eyebrow">FAQ</p>
    <h2>Before you ask</h2>
    <div style="margin-top:30px;max-width:820px">
      <details class="rv"><summary>Can I apply as a collective?</summary><div class="a"><p>Yes — collectives are explicitly welcome. Include brief CVs for all key collaborators in the application.</p></div></details>
      <details class="rv"><summary>Do I have to be based in one of the partner countries?</summary><div class="a"><p>No. The programme is oriented toward practices connected to Europe's periphery, including artists based elsewhere whose work meaningfully engages with these realities.</p></div></details>
      <details class="rv"><summary>Does my project have to be finished during the residency?</summary><div class="a"><p>No. Research-driven proposals, long-term inquiries and early-stage experiments are welcome — process is valued as much as finished results. Work-in-progress sharings and public presentations happen within realistic organisational capacities.</p></div></details>
      <details class="rv"><summary>What about accessibility?</summary><div class="a"><p>Basic support for accessibility can be discussed with selected residents within available resources. State your access needs in the application — it has no bearing on selection.</p></div></details>
      <details class="rv"><summary>When will I hear back?</summary><div class="a"><p>Selection follows the July 31 deadline; all applicants will be notified by e-mail. Questions in the meantime — use the <a href="index.html#contact">contact form</a>.</p></div></details>
    </div>
    <p style="margin-top:44px"><a class="btn" href="{FORM_URL}" rel="noopener">Apply now — shape the first cycle ↗</a></p>
  </div>
</section>
'''

page("open-call.html",
     "Open Call · Cycle 1 — PERFORMA-Q",
     "Open Call Cycle 1: PERFORMA-Q residency for queer performing artists from Europe's periphery. Residency October 2026 – April 2027. Applications close 31 July 2026.",
     "work", opencall_body)

print("all pages built")
