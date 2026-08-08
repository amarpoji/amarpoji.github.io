#!/usr/bin/env python3
"""
build.py — Amar Fauzie portfolio (consistent 4-page build)
==========================================================
Generates 4 static pages from ONE shared design system so the
top bar, bottom nav, footer, colors, and fonts can never drift.

Output: index.html, projects.html, skills.html, about.html
Run:   python3 build.py   (from this folder)

Edit the CONTENT dict below to change text; edit COMPONENTS to
change chrome. Re-run to regenerate all pages.
"""

import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = HERE

# ---------------------------------------------------------------------------
# TAILWIND CONFIG — single source of truth (Material 3 maroon scheme)
# ---------------------------------------------------------------------------
CONFIG = """  tailwind.config = {
    darkMode: "class",
    theme: {
      extend: {
        "colors": {
          "on-tertiary-container": "#b7b5af",
          "error-container": "#ffdad6",
          "on-error": "#ffffff",
          "on-surface-variant": "#554243",
          "tertiary-fixed-dim": "#c9c6c0",
          "error": "#ba1a1a",
          "on-tertiary": "#ffffff",
          "on-background": "#151c27",
          "on-surface": "#151c27",
          "inverse-primary": "#ffb2ba",
          "on-tertiary-fixed-variant": "#474742",
          "inverse-surface": "#2a313d",
          "primary-fixed": "#ffd9dc",
          "tertiary-container": "#484742",
          "on-primary": "#ffffff",
          "outline-variant": "#dcc0c2",
          "secondary": "#5d5e61",
          "on-error-container": "#93000a",
          "primary": "#630b22",
          "on-secondary-fixed-variant": "#454749",
          "background": "#f9f9ff",
          "surface-tint": "#a13b4d",
          "surface-container-highest": "#dce2f3",
          "surface": "#f9f9ff",
          "surface-container-lowest": "#ffffff",
          "on-tertiary-fixed": "#1c1c18",
          "primary-fixed-dim": "#ffb2ba",
          "on-primary-fixed": "#400011",
          "surface-container-high": "#e2e8f8",
          "secondary-fixed": "#e2e2e5",
          "surface-container": "#e7eefe",
          "on-secondary-container": "#636467",
          "secondary-fixed-dim": "#c6c6c9",
          "surface-variant": "#dce2f3",
          "surface-dim": "#d3daea",
          "surface-bright": "#f9f9ff",
          "secondary-container": "#e2e2e5",
          "outline": "#897173",
          "on-primary-container": "#ff98a5",
          "on-primary-fixed-variant": "#822437",
          "on-secondary-fixed": "#1a1c1e",
          "primary-container": "#822437",
          "surface-container-low": "#f0f3ff",
          "tertiary": "#31312c",
          "tertiary-fixed": "#e5e2db",
          "inverse-on-surface": "#ebf1ff",
          "on-secondary": "#ffffff"
        },
        "borderRadius": {
          "DEFAULT": "0.125rem",
          "lg": "0.25rem",
          "xl": "0.5rem",
          "full": "0.75rem"
        },
        "spacing": {
          "sm": "12px",
          "lg": "48px",
          "margin-desktop": "64px",
          "base": "8px",
          "xl": "80px",
          "margin-mobile": "16px",
          "gutter": "24px",
          "xs": "4px",
          "md": "24px"
        },
        "fontFamily": {
          "body-md": ["Hanken Grotesk"],
          "headline-sm": ["EB Garamond"],
          "display-lg": ["EB Garamond"],
          "body-sm": ["Hanken Grotesk"],
          "data-mono": ["JetBrains Mono"],
          "label-caps": ["JetBrains Mono"],
          "display-lg-mobile": ["EB Garamond"],
          "headline-md": ["EB Garamond"],
          "body-lg": ["Hanken Grotesk"]
        },
        "fontSize": {
          "body-md": ["16px", { "lineHeight": "24px", "fontWeight": "400" }],
          "headline-sm": ["24px", { "lineHeight": "32px", "fontWeight": "500" }],
          "display-lg": ["48px", { "lineHeight": "56px", "letterSpacing": "-0.02em", "fontWeight": "600" }],
          "body-sm": ["14px", { "lineHeight": "20px", "fontWeight": "400" }],
          "data-mono": ["13px", { "lineHeight": "18px", "fontWeight": "400" }],
          "label-caps": ["12px", { "lineHeight": "16px", "letterSpacing": "0.1em", "fontWeight": "600" }],
          "display-lg-mobile": ["32px", { "lineHeight": "40px", "letterSpacing": "-0.01em", "fontWeight": "600" }],
          "headline-md": ["32px", { "lineHeight": "40px", "fontWeight": "500" }],
          "body-lg": ["18px", { "lineHeight": "28px", "fontWeight": "400" }]
        }
      }
    }
  }"""

# ---------------------------------------------------------------------------
# LINKS — single source of truth
# ---------------------------------------------------------------------------
LINKS = {
    "github": "https://github.com/amarpoji",
    "linkedin": "https://www.linkedin.com/in/amar-fauzie-53aa77334/",
    "email": "mailto:amarpoji1999@gmail.com",
    "diwanic": "https://github.com/amarpoji/Diwanic",
    "advisor": "https://github.com/amarpoji/academic-advisor-agent",
    "hadith": "https://github.com/amarpoji/crewai_agent",
    "phishing": "https://github.com/amarpoji/ai-fraud-detector-streamlit",
}

NAV = [
    ("Home", "index.html"),
    ("Projects", "projects.html"),
    ("Skills", "skills.html"),
    ("About", "about.html"),
    ("Contact", LINKS["email"]),
]

BOTTOM_NAV = [
    ("Home", "index.html", "home"),
    ("Projects", "projects.html", "code"),
    ("Skills", "skills.html", "psychology"),
    ("About", "about.html", "history_edu"),
]

# ---------------------------------------------------------------------------
# CHROME COMPONENTS
# ---------------------------------------------------------------------------
def head(title):
    return f"""<!DOCTYPE html>
<html class="light" lang="en">
<head>
<meta charset="utf-8">
<meta content="width=device-width, initial-scale=1.0" name="viewport">
<title>{title}</title>
<link href="https://fonts.googleapis.com" rel="preconnect">
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect">
<link href="https://fonts.googleapis.com/css2?family=EB+Garamond:wght@400;500;600;700&family=Hanken+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet">
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<script id="tailwind-config">
{CONFIG}
</script>
<style>
  .material-symbols-outlined {{ font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24; }}
  .material-symbols-outlined.filled {{ font-variation-settings: 'FILL' 1; }}
  body {{ min-height: max(884px, 100dvh); }}
</style>
</head>
<body class="bg-background text-on-background font-body-md text-body-md antialiased min-h-screen flex flex-col relative pb-16 md:pb-0">
"""

def topbar(active):
    items = []
    for label, href in NAV:
        if label == active:
            items.append(f'<a class="text-primary font-bold transition-colors duration-300" href="{href}">{label}</a>')
        else:
            items.append(f'<a class="text-on-surface-variant hover:text-primary transition-colors duration-300" href="{href}">{label}</a>')
    nav = "\n".join(items)
    return f"""<!-- TopAppBar (Desktop) -->
<header class="hidden md:flex bg-background fixed top-0 w-full z-50 border-b border-outline/20 justify-between items-center px-margin-desktop h-16">
  <a class="flex items-center gap-4" href="index.html">
    <span class="material-symbols-outlined text-primary">terminal</span>
    <span class="font-label-caps text-label-caps uppercase tracking-widest text-primary">AF</span>
  </a>
  <nav class="flex gap-8">
{nav}
  </nav>
</header>
<!-- TopAppBar (Mobile) -->
<header class="md:hidden bg-background fixed top-0 w-full z-50 border-b border-outline/20 flex justify-between items-center px-margin-mobile h-16">
  <a class="flex items-center gap-4" href="index.html">
    <span class="material-symbols-outlined text-primary">terminal</span>
    <span class="font-label-caps text-label-caps uppercase tracking-widest text-primary">AF</span>
  </a>
</header>
"""

def bottombar(active):
    items = []
    for label, href, icon in BOTTOM_NAV:
        if label == active:
            items.append(f"""<a class="flex flex-col items-center justify-center bg-primary-container text-on-primary rounded-full p-2 active:scale-90 transition-all duration-200 w-16" href="{href}">
  <span class="material-symbols-outlined text-2xl filled">{icon}</span>
  <span class="text-[10px] font-label-caps uppercase tracking-tighter mt-0.5">{label}</span>
</a>""")
        else:
            items.append(f"""<a class="flex flex-col items-center justify-center text-on-surface-variant p-2 hover:bg-surface-container-high active:scale-90 transition-all duration-200 w-16" href="{href}">
  <span class="material-symbols-outlined text-2xl">{icon}</span>
  <span class="text-[10px] font-label-caps uppercase tracking-tighter mt-0.5">{label}</span>
</a>""")
    bar = "\n".join(items)
    return f"""<!-- BottomNavBar (Mobile Only) -->
<nav class="md:hidden bg-surface-container-lowest fixed bottom-0 w-full z-50 border-t border-outline/20 flex justify-around items-center px-4 py-2">
{bar}
</nav>
"""

def footer():
    return f"""<!-- Footer -->
<footer class="w-full bg-primary-container text-on-primary mt-auto py-12 px-margin-mobile md:px-margin-desktop">
  <div class="max-w-[1200px] mx-auto flex flex-col md:flex-row justify-between items-center gap-6 text-center">
    <div>
      <div class="font-headline-md text-headline-md mb-2">AF</div>
      <p class="font-body-sm text-body-sm opacity-80">© 2026 Amar Fauzie. Bridging Tradition &amp; Innovation.</p>
    </div>
    <div class="flex gap-8">
      <a class="font-label-caps text-label-caps text-on-primary/90 hover:text-on-primary transition-colors" href="{LINKS['github']}" target="_blank" rel="noopener">GitHub</a>
      <a class="font-label-caps text-label-caps text-on-primary/90 hover:text-on-primary transition-colors" href="{LINKS['linkedin']}" target="_blank" rel="noopener">LinkedIn</a>
      <a class="font-label-caps text-label-caps text-on-primary/90 hover:text-on-primary transition-colors" href="{LINKS['email']}">Email</a>
    </div>
  </div>
</footer>
</body>
</html>
"""

# ---------------------------------------------------------------------------
# PAGE BODIES
# ---------------------------------------------------------------------------
def page_index():
    body = f"""<main class="flex-grow flex items-center justify-center pt-24 pb-24 md:pt-32 md:pb-32 px-margin-mobile md:px-margin-desktop">
<div class="max-w-[1200px] w-full grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
  <!-- Hero Text -->
  <div class="lg:col-span-7 space-y-8 relative z-10">
    <div class="w-16 h-1 bg-primary-container mb-8"></div>
    <div class="space-y-4">
      <h1 class="font-display-lg-mobile md:font-display-lg text-display-lg-mobile md:text-display-lg text-on-surface tracking-tight">Amar Fauzie</h1>
      <h2 class="font-headline-sm text-headline-sm text-on-surface-variant">AI Engineer | Data Scientist</h2>
    </div>
    <p class="font-body-lg text-body-lg text-secondary max-w-2xl leading-relaxed">
      I&rsquo;m an Arabic and Islamic studies graduate turned self-taught AI and data science enthusiast, driven by curiosity to connect language, analytical thinking, and technology to solve real-world problems.
    </p>
    <div class="flex flex-wrap gap-6 pt-4">
      <a class="group flex items-center gap-2 font-label-caps text-label-caps text-primary-container hover:text-primary transition-colors duration-300 border-b border-outline/20 hover:border-primary-container pb-1" href="{LINKS['github']}" target="_blank" rel="noopener">
        <span class="material-symbols-outlined text-[18px]">code</span><span>GitHub</span>
      </a>
      <a class="group flex items-center gap-2 font-label-caps text-label-caps text-primary-container hover:text-primary transition-colors duration-300 border-b border-outline/20 hover:border-primary-container pb-1" href="{LINKS['linkedin']}" target="_blank" rel="noopener">
        <span class="material-symbols-outlined text-[18px]">work</span><span>LinkedIn</span>
      </a>
      <a class="group flex items-center gap-2 font-label-caps text-label-caps text-primary-container hover:text-primary transition-colors duration-300 border-b border-outline/20 hover:border-primary-container pb-1" href="{LINKS['email']}">
        <span class="material-symbols-outlined text-[18px]">mail</span><span>Email</span>
      </a>
    </div>
  </div>
  <!-- Hero Visual -->
  <div class="lg:col-span-5 relative h-[400px] lg:h-[600px] w-full flex items-center justify-center">
    <div class="absolute inset-0 bg-surface-container-low rounded-tl-full rounded-br-full transform -rotate-12 scale-90 border border-outline/10"></div>
    <div class="relative w-full max-w-[400px] aspect-[4/5] bg-surface border border-outline/20 p-4 shadow-[0_8px_30px_rgb(0,0,0,0.05)] hover:shadow-[0_12px_40px_rgb(0,0,0,0.1)] transition-shadow duration-500 z-10 group rounded">
      <div class="w-full h-full relative overflow-hidden bg-surface-container border border-outline/10 rounded">
        <img alt="Abstract portrait representation" class="object-cover w-full h-full filter saturate-50 group-hover:saturate-100 transition-all duration-700" src="assets/hero.png">
        <div class="absolute bottom-0 left-0 w-full h-1/3 bg-gradient-to-t from-primary-container/80 to-transparent"></div>
        <div class="absolute bottom-4 left-4 right-4">
          <span class="font-label-caps text-label-caps text-on-primary bg-primary-container/90 px-2 py-1 backdrop-blur-sm rounded">TRADITION &times; INNOVATION</span>
        </div>
      </div>
      <div class="absolute top-0 left-0 w-4 h-4 border-t border-l border-outline"></div>
      <div class="absolute top-0 right-0 w-4 h-4 border-t border-r border-outline"></div>
      <div class="absolute bottom-0 left-0 w-4 h-4 border-b border-l border-outline"></div>
      <div class="absolute bottom-0 right-0 w-4 h-4 border-b border-r border-outline"></div>
    </div>
    <div class="absolute -right-8 bottom-1/4 w-24 h-24 bg-surface-container border border-outline/20 rounded-full flex items-center justify-center shadow-sm z-20 hidden md:flex animate-[bounce_4s_infinite]">
      <span class="material-symbols-outlined text-primary-container text-3xl">psychology</span>
    </div>
  </div>
</div>
</main>
"""
    return body

def page_projects():
    projects = [
        {
            "icon": "translate", "name": "Diwanic", "sub": "Flagship Project - Arabic Poetry Retrieval System",
            "desc": "I have always been interested in Arabic poetry. Sometimes, when you are going through a certain moment in life, you want to find a poem that truly matches your feelings. Finding the right words from the right poet can be a special experience. One of the websites I often visit is AlDiwan, which has a huge collection of Arabic poems from different generations of poets. However, I noticed that its search system felt outdated, making it difficult to discover poems based on their meaning and emotions. This inspired me to explore how AI could help people search and discover Arabic poetry in a smarter and more meaningful way.",
            "img": "assets/diagram.svg", "img_alt": "Diwanic architecture diagram: ingestion, embedding, hybrid retrieval and orchestration flow",
            "href": LINKS["diwanic"], "stack": ["Python", "FastAPI", "Qdrant", "PostgreSQL", "Prefect", "bge-m3"],
        },
        {
            "icon": "school", "name": "Master Advisor Agent", "sub": "LangGraph Pipeline",
            "desc": "An autonomous agent workflow that researches, evaluates, and compiles real master's degree programs and associated scholarship opportunities based on user criteria.",
            "href": LINKS["advisor"], "stack": ["LangGraph", "LangChain", "OpenAI", "Tavily", "SQLAlchemy"],
        },
        {
            "icon": "menu_book", "name": "Hadith Research Agent", "sub": "Multi-Agent Pipeline",
            "desc": "As a student of Islamic knowledge, I know how challenging it is to find authentic hadith on a specific topic. The collection spans thousands of books. Relying on LLMs alone is risky: a single hallucinated word in the matn can distort the narration. This agent searches trusted sources (sunnah.com, shamela.ws) and provides every source link for verification, reducing research time while maintaining reliability.",
            "img": "assets/crewai.png", "img_alt": "CrewAI Hadith Research Agent workflow: research, validate, and report agents drawing from Shamela and Sunnah.com",
            "href": LINKS["hadith"], "stack": ["CrewAI", "Multi-Agent", "Arabic NLP"],
        },
        {
            "icon": "security", "name": "Phishing Detector", "sub": "ML Classification App",
            "desc": "AI Fraud Detection was my first hackathon project organized by Expert Academy. We built the project from scratch, starting with finding data from Kaggle, training and testing machine learning models, and finally deploying it on AWS. The project started with three team members, but I was the one who continued and completed it alone. Although it was not a perfect project, it taught me a lot about the complete machine learning workflow and gave me the confidence to build AI solutions independently.",
            "img": "assets/fraud.png", "img_alt": "SMS Fraud detection illustration: phone with chat bubbles and a masked scammer",
            "href": LINKS["phishing"], "stack": ["scikit-learn", "DVC", "MLflow", "Docker"],
        },
        {
            "icon": "account_tree", "name": "Hadith GraphRAG", "sub": "Knowledge Graph Pipeline (Ongoing)",
            "desc": "Semantic knowledge graph over Hadith literature using Microsoft GraphRAG — entity extraction, relationship mapping, intelligent retrieval for scholarship research.",
            "href": "https://github.com/amarpoji", "coming_soon": True, "stack": ["GraphRAG", "Knowledge Graphs", "Arabic NLP"],
        },
    ]
    cards = []
    for p in projects:
        preview = ""
        if p.get("img"):
            preview = f'<img src="{p["img"]}" alt="{p["img_alt"]}" class="w-full h-full object-cover rounded">'
        else:
            preview = f'''<span class="material-symbols-outlined text-outline/40 text-4xl mb-2">image</span>
          <span class="font-label-caps text-label-caps text-on-surface-variant uppercase tracking-widest">Project Preview</span>'''
        btn = f'<a class="inline-flex items-center gap-2 bg-primary text-on-primary px-4 py-2 rounded hover:bg-primary/90 transition-colors w-fit font-label-caps text-label-caps uppercase tracking-widest" href="{p["href"]}" target="_blank" rel="noopener"><span class="material-symbols-outlined text-xl">link</span>{"Coming Soon" if p.get("coming_soon") else "View Repository"}</a>'
        chips = "\n".join(f'<span class="px-2 py-1 bg-surface-container-low text-primary font-label-caps text-label-caps rounded-sm">{s}</span>' for s in p["stack"])
        cards.append(f'''<article class="group bg-surface-container-lowest border border-outline/20 p-6 md:p-8 hover:shadow-[0_4px_24px_rgba(99,11,34,0.1)] transition-all duration-300 rounded flex flex-col h-full relative overflow-hidden">
  <div class="absolute top-0 right-0 p-4 opacity-10 pointer-events-none"><span class="material-symbols-outlined text-6xl text-primary filled">{p["icon"]}</span></div>
  <div class="flex-grow z-10">
    <h2 class="font-headline-md text-headline-md text-primary mb-2">{p["name"]}</h2>
    <h3 class="font-body-lg text-body-lg text-secondary mb-4">{p["sub"]}</h3>
    <p class="mb-6 text-on-surface-variant">{p["desc"]}</p>
    <div class="mb-6 aspect-video bg-surface-container-low border-2 border-dashed border-outline/20 flex flex-col items-center justify-center rounded overflow-hidden">
      {preview}
    </div>
    {btn}
  </div>
  <div class="mt-auto z-10 pt-4 border-t border-outline/10">
    <h4 class="font-label-caps text-label-caps text-primary mb-2 uppercase tracking-widest">Stack</h4>
    <div class="flex flex-wrap gap-2">{chips}</div>
  </div>
</article>''')
    body = f"""<main class="max-w-[1200px] mx-auto px-margin-mobile md:px-margin-desktop pt-24 md:pt-32 pb-24 flex-grow w-full">
<div class="mb-16 md:mb-24 text-center md:text-left">
  <h1 class="font-display-lg-mobile text-display-lg-mobile md:font-display-lg md:text-display-lg mb-4 text-primary">Selected Works</h1>
  <p class="font-body-md text-body-md text-on-surface-variant max-w-2xl">A portfolio of projects bridging classical scholarship and modern computation. Showcasing implementations in machine learning, natural language processing, and robust engineering.</p>
</div>
<div class="grid grid-cols-1 md:grid-cols-2 gap-gutter">
{chr(10).join(cards)}
</div>
</main>
"""
    return body

def page_skills(certs):
    dlai = [c for c in certs if "Coursera" not in c["issuer"]]
    coursera = [c for c in certs if "Coursera" in c["issuer"]]

    def cert_card(c):
        return f'''<div class="bg-surface-container-lowest border border-outline/20 p-6 hover:bg-surface-container-low transition-colors duration-300 flex flex-col rounded">
  <div class="flex items-start gap-4 mb-4">
    <span class="material-symbols-outlined text-primary text-3xl">verified</span>
    <h2 class="font-headline-md text-headline-md text-primary">{c["title"]}</h2>
  </div>
  <div class="mt-auto pt-4 border-t border-outline/10 flex justify-between items-center gap-4 flex-wrap">
    <span class="font-label-caps text-label-caps text-secondary">{c["issuer"]}</span>
    <a class="text-primary hover:text-primary-container font-label-caps text-label-caps flex items-center gap-1" href="{c["url"]}" target="_blank" rel="noopener">Verify Credential <span class="material-symbols-outlined text-sm">open_in_new</span></a>
  </div>
</div>'''

    def skill_card(icon, title, items, extra=""):
        chips = "\n".join(f'<span class="font-label-caps text-label-caps bg-surface-container-low text-primary px-3 py-1 rounded border border-outline/10">{s}</span>' for s in items)
        return f'''<div class="bg-surface-container-lowest border border-outline/20 p-8 skill-card transition-all duration-300 flex flex-col h-full rounded {extra}">
  <div class="flex items-center gap-4 mb-6 pb-4 border-b border-outline/20">
    <span class="material-symbols-outlined text-primary text-3xl">{icon}</span>
    <h2 class="font-headline-md text-headline-md text-primary">{title}</h2>
  </div>
  <div class="flex flex-wrap gap-3 mt-auto">{chips}</div>
</div>'''

    body = f"""<main class="max-w-[1200px] mx-auto px-margin-mobile md:px-margin-desktop pt-24 md:pt-32 pb-24 flex-grow w-full">
<div class="mb-16 md:mb-24 text-center md:text-left">
  <h1 class="font-display-lg-mobile md:font-display-lg text-display-lg-mobile md:text-display-lg text-primary mb-6">Technical Capabilities</h1>
  <p class="font-body-md text-body-md text-secondary max-w-2xl mx-auto md:mx-0">A synthesis of classical software engineering and contemporary artificial intelligence tools, demonstrating proficiency across the modern data stack.</p>
</div>
<style>
  .skill-card:hover {{ box-shadow: 0 4px 6px -1px rgba(99,11,34,0.1), 0 2px 4px -1px rgba(99,11,34,0.06); transform: translateY(-2px); }}
</style>
<!-- Skills -->
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-24">
  {skill_card("code", "Languages", ["Python", "SQL", "JavaScript / TS", "Bash"])}
  {skill_card("build", "Frameworks &amp; Tools", ["FastAPI", "LangChain", "Streamlit", "Gradio", "React", "Tailwind CSS"], "lg:col-span-2")}
  {skill_card("psychology", "AI &amp; Machine Learning", ["scikit-learn", "CrewAI", "Qdrant", "PyTorch", "TensorFlow", "Hugging Face"], "lg:col-span-2 lg:row-start-2")}
  {skill_card("cloud", "Cloud &amp; Data", ["PostgreSQL", "MongoDB", "Docker", "AWS"], "lg:row-start-2")}
</div>
<!-- Certifications -->
<div class="mb-12">
  <div class="flex items-center gap-4 mb-12 border-b border-outline/20 pb-4">
    <span class="material-symbols-outlined text-primary text-4xl">school</span>
    <h2 class="font-display-lg-mobile md:font-display-lg text-display-lg-mobile md:text-display-lg text-primary">Certifications</h2>
  </div>
  <div class="space-y-12">
    <div>
      <h3 class="font-headline-md text-headline-md text-primary mb-8 border-b border-outline/10 pb-2">Machine Learning Specialization &mdash; Coursera</h3>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        {chr(10).join(cert_card(c) for c in coursera)}
      </div>
    </div>
    <div>
      <h3 class="font-headline-md text-headline-md text-primary mb-8 border-b border-outline/10 pb-2">Advanced AI Short Courses &mdash; DeepLearning.AI</h3>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        {chr(10).join(cert_card(c) for c in dlai)}
      </div>
    </div>
  </div>
</div>
</main>
"""
    return body

def page_about():
    body = f"""<main class="max-w-[1200px] mx-auto px-margin-mobile md:px-margin-desktop py-xl pb-24 flex-grow w-full">
<section class="mb-xl text-center">
  <p class="font-label-caps text-label-caps text-primary-container mb-2 uppercase tracking-widest text-xs">The story &bull; About Me</p>
  <h1 class="font-display-lg-mobile text-display-lg-mobile md:font-display-lg md:text-display-lg mb-base font-semibold text-primary-container">The story behind the code.</h1>
  <p class="font-body-lg text-body-lg text-on-surface-variant max-w-2xl mx-auto">A narrative of curiosity, unexpected paths, and the persistent drive to build things that matter.</p>
</section>
<section class="grid grid-cols-1 md:grid-cols-12 gap-gutter mb-xl relative">
  <aside class="hidden md:block md:col-span-3 pt-lg">
    <div class="sticky top-32">
      <h3 class="font-label-caps text-label-caps text-primary-container mb-4 border-b border-outline-variant pb-2">Chapters</h3>
      <ul class="space-y-4">
        <li><a class="flex items-center gap-2 text-on-surface-variant hover:text-primary-container transition-colors" href="#journey"><span class="material-symbols-outlined text-sm">explore</span><span class="font-data-mono text-data-mono">01. Journey</span></a></li>
        <li><a class="flex items-center gap-2 text-on-surface-variant hover:text-primary-container transition-colors" href="#experience"><span class="material-symbols-outlined text-sm">work</span><span class="font-data-mono text-data-mono">02. Experience</span></a></li>
        <li><a class="flex items-center gap-2 text-on-surface-variant hover:text-primary-container transition-colors" href="#languages"><span class="material-symbols-outlined text-sm">language</span><span class="font-data-mono text-data-mono">03. Languages</span></a></li>
      </ul>
    </div>
  </aside>
  <article class="md:col-span-8 lg:col-span-7 bg-surface-container-lowest border border-outline-variant rounded-xl p-6 md:p-12 shadow-[0_4px_20px_rgba(0,0,0,0.04)] text-center">
    <div class="mb-12" id="journey">
      <h2 class="font-headline-md text-headline-md text-on-surface mb-6 font-semibold">My Journey</h2>
      <p class="font-body-md text-body-md text-on-surface-variant mb-4 leading-relaxed text-left">
        My journey has taken a path I never expected. During high school, I was in the science stream, spending countless nights studying subjects like Additional Mathematics, Physics, Chemistry, and Biology. I worked hard to achieve a good result in my SPM, believing that I would eventually become a doctor or an engineer. After receiving my SPM results, my mother invited me to perform Umrah with my eldest brother. That journey changed the direction of my life. During my stay in Madinah, I met someone named Ahmad at a grocery store near the Prophet&rsquo;s Mosque. We could barely communicate at that time because I did not understand Arabic, and he did not speak my language. However, we stayed in contact through WhatsApp, and I relied on Google Translate to understand our conversations. That small connection sparked a new curiosity within me. I started learning Arabic seriously, and my dream shifted from becoming an engineer or doctor to mastering the Arabic language and its sciences. Years later, I earned a Diploma in Arabic Language and Literature from UniSZA and completed my Bachelor's degree in Theology at the Islamic University of Madinah. But my story did not end there. My curiosity for technology returned, bringing me back to mathematics and problem-solving. I discovered data science as a bridge between my analytical background and my passion for technology. Since then, I have been continuously learning through courses in machine learning, deep learning, and artificial intelligence, exploring how technology can be used to solve real-world problems. My journey has always been about learning, adapting, and connecting different fields together. From Arabic and Islamic studies to AI and data science, I believe every experience has shaped the person I am today.
      </p>
    </div>
    <div class="mb-12" id="experience">
      <h2 class="font-headline-md text-headline-md text-on-surface mb-6 font-semibold border-t border-outline-variant pt-12">Professional Experience</h2>
      <div class="space-y-6 text-left">
        <div>
          <h3 class="font-headline-sm text-headline-sm text-on-surface font-medium">Hajj Pilgrimage Guide / Mutawwif</h3>
          <p class="font-label-caps text-label-caps text-primary-container mb-2 uppercase tracking-widest text-xs">Tabung Haji 2024 &ndash; 2026</p>
          <p class="font-body-md text-body-md text-on-surface-variant">Communicated religious, logistical, and safety information clearly to pilgrims from diverse backgrounds; managed coordination and problem-solving in a high-pressure, time-sensitive environment.</p>
        </div>
        <div>
          <h3 class="font-headline-sm text-headline-sm text-on-surface font-medium">Company Representative / Exhibitor</h3>
          <p class="font-label-caps text-label-caps text-primary-container mb-2 uppercase tracking-widest text-xs">Siiru &mdash; Hajj &amp; Umrah Forum, King Salman Int'l Convention Centre</p>
          <p class="font-body-md text-body-md text-on-surface-variant">Presented company offerings and communicated with diverse audiences in a professional, public-facing exhibition environment.</p>
        </div>
        <div>
          <h3 class="font-headline-sm text-headline-sm text-on-surface font-medium">Committee Member (AJK)</h3>
          <p class="font-label-caps text-label-caps text-primary-container mb-2 uppercase tracking-widest text-xs">Nadi Pencinta Madinah</p>
          <p class="font-body-md text-body-md text-on-surface-variant">Co-developed educational modules and organized cultural activities and historical tours across Makkah, Madinah, and Taif for Malaysian students.</p>
        </div>
        <div>
          <h3 class="font-headline-sm text-headline-sm text-on-surface font-medium">President</h3>
          <p class="font-label-caps text-label-caps text-primary-container mb-2 uppercase tracking-widest text-xs">ARCOM, International Islamic University Malaysia 2019&ndash;2020</p>
          <p class="font-body-md text-body-md text-on-surface-variant">Led a student organization focused on Arabic communication; organized competitions and represented the group in Arabic debate and public speaking.</p>
        </div>
        <div>
          <h3 class="font-headline-sm text-headline-sm text-on-surface font-medium">President</h3>
          <p class="font-label-caps text-label-caps text-primary-container mb-2 uppercase tracking-widest text-xs">Sejahtera, Universiti Sultan Zainal Abidin 2018</p>
          <p class="font-body-md text-body-md text-on-surface-variant">Led organizational activities and built the organization's social media and digital communication presence.</p>
        </div>
      </div>
    </div>
    <div class="mb-12" id="languages">
      <h2 class="font-headline-md text-headline-md text-on-surface mb-6 font-semibold border-t border-outline-variant pt-12">Languages</h2>
      <p class="font-body-md text-body-md text-on-surface-variant leading-relaxed text-left">I am fluent in Malay, English, and Arabic.</p>
    </div>
  </article>
  <aside class="hidden lg:block lg:col-span-2 pt-lg">
    <div class="sticky top-32">
      <div class="w-full aspect-[3/4] bg-surface-container-high rounded-lg overflow-hidden border border-outline-variant relative">
        <img src="assets/about.png" alt="Abstract circuit and architectural structure" class="w-full h-full object-cover opacity-80">
      </div>
      <p class="font-data-mono text-data-mono text-on-surface-variant mt-4 text-right">Fig. 1 &mdash; Structure</p>
    </div>
  </aside>
</section>
</main>
"""
    return body

# ---------------------------------------------------------------------------
# BUILD
# ---------------------------------------------------------------------------
import json

certs = json.load(open("/tmp/portfolio_data.json"))["certs"]

PAGES = [
    ("index.html", "Amar Fauzie - AI Engineer | Data Scientist", page_index(), "Home"),
    ("projects.html", "Amar Fauzie - Projects", page_projects(), "Projects"),
    ("skills.html", "Amar Fauzie - Skills & Certifications", page_skills(certs), "Skills"),
    ("about.html", "About Me - Amar Fauzie", page_about(), "About"),
]

for fname, title, body, active in PAGES:
    html = head(title) + topbar(active) + body + bottombar(active) + footer()
    path = os.path.join(OUT, fname)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"wrote {fname} ({len(html):,} bytes)")
print("done")
