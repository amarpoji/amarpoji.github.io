#!/usr/bin/env python3
"""
build.py — Amar Fauzie portfolio (Kinetic Clarity single-page build)
====================================================================
Generates ONE page (index.html) that scrolls vertically — no separate
sub-pages, no mobile-app bottom nav. Design follows DESIGN.md:
white-space-first Swiss minimalism, single high-vibrancy orange accent
(#ff4d00), near-black type (#121212), Hanken Grotesk / Inter /
JetBrains Mono.

Output: index.html
Run:   python3 build.py   (from this folder)
"""

import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = HERE

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
    ("Projects", "#projects"),
    ("Skills", "#skills"),
    ("About", "#about"),
    ("Contact", "#contact"),
]

# ---------------------------------------------------------------------------
# CERTIFICATIONS — self-contained (was /tmp/portfolio_data.json)
# ---------------------------------------------------------------------------
CERTS = [
    {"title": "Practical Multi AI Agents & Advanced Use Cases with crewAI", "issuer": "DeepLearning.AI", "url": "https://learn.deeplearning.ai/accomplishments/64ec04ba-3b91-44f0-82b1-6dcf62740a97"},
    {"title": "Multi AI Agent Systems with crewAI", "issuer": "DeepLearning.AI", "url": "https://learn.deeplearning.ai/accomplishments/84b48ed1-6537-4503-aa50-79e31f5cef37"},
    {"title": "Retrieval Augmented Generation (RAG)", "issuer": "DeepLearning.AI", "url": "https://learn.deeplearning.ai/certificates/b7671906-3210-4ee2-b17b-b3832efa1b86"},
    {"title": "Pydantic for LLM Workflows", "issuer": "DeepLearning.AI", "url": "https://learn.deeplearning.ai/accomplishments/afeb9d5e-51b0-4dd4-aa51-042ad7f4d558"},
    {"title": "Linear Algebra for Machine Learning & Data Science", "issuer": "DeepLearning.AI \u00b7 Coursera", "url": "https://www.coursera.org/account/accomplishments/verify/Y545OFFC7S1S"},
    {"title": "Probability & Statistics for ML & Data Science", "issuer": "DeepLearning.AI \u00b7 Coursera", "url": "https://www.coursera.org/account/accomplishments/verify/NWHRKJTRZUDM"},
    {"title": "Advanced Learning Algorithms", "issuer": "DeepLearning.AI \u00b7 Coursera", "url": "https://www.coursera.org/account/accomplishments/verify/WXB4LF7QYTBF"},
    {"title": "Supervised Machine Learning: Regression & Classification", "issuer": "DeepLearning.AI \u00b7 Coursera", "url": "https://www.coursera.org/account/accomplishments/verify/0FOCMDHNV2TN"},
]

# ---------------------------------------------------------------------------
# SKILL GROUPS
# ---------------------------------------------------------------------------
SKILLS = [
    ("Languages", ["Python", "SQL", "JavaScript / TS", "Bash"]),
    ("Frameworks & Tools", ["FastAPI", "LangChain", "Streamlit", "Gradio", "React", "Tailwind CSS"]),
    ("AI & Machine Learning", ["scikit-learn", "CrewAI", "Qdrant", "PyTorch", "TensorFlow", "Hugging Face"]),
    ("Cloud & Data", ["PostgreSQL", "MongoDB", "Docker", "AWS"]),
]

# ---------------------------------------------------------------------------
# PROJECTS
# ---------------------------------------------------------------------------
PROJECTS = [
    {
        "index": "01",
        "name": "Diwanic",
        "sub": "Flagship — Arabic Poetry Retrieval System",
        "desc": "I have always been interested in Arabic poetry. Sometimes, when you are going through a certain moment in life, you want to find a poem that truly matches your feelings. Finding the right words from the right poet can be a special experience. One of the websites I often visit is AlDiwan, which has a huge collection of Arabic poems from different generations of poets. However, I noticed that its search system felt outdated, making it difficult to discover poems based on their meaning and emotions. This inspired me to explore how AI could help people search and discover Arabic poetry in a smarter and more meaningful way.",
        "img": "assets/diagram.svg",
        "img_alt": "Diwanic architecture diagram",
        "href": LINKS["diwanic"],
        "stack": ["Python", "FastAPI", "Qdrant", "PostgreSQL", "Prefect", "bge-m3"],
    },
    {
        "index": "02",
        "name": "Master Advisor",
        "sub": "LangGraph Multi-Agent Pipeline",
        "desc": "An autonomous agent workflow that researches, evaluates, and compiles real master's degree programs and their associated scholarship opportunities, based on user criteria.",
        "href": LINKS["advisor"],
        "stack": ["LangGraph", "LangChain", "OpenAI", "Tavily", "SQLAlchemy"],
    },
    {
        "index": "03",
        "name": "Hadith Research Agent",
        "sub": "Multi-Agent Verification Pipeline",
        "desc": "As a student of Islamic knowledge, I know how hard it is to find authentic hadith on a topic — the collections span thousands of books. Relying on LLMs alone is risky: a single hallucinated word in the matn can distort the narration. This agent searches trusted sources (sunnah.com, shamela.ws) and provides every source link for verification, cutting research time while keeping reliability.",
        "img": "assets/crewai.png",
        "img_alt": "CrewAI Hadith Research Agent workflow",
        "href": LINKS["hadith"],
        "stack": ["CrewAI", "Multi-Agent", "Arabic NLP"],
    },
    {
        "index": "04",
        "name": "Phishing Detector",
        "sub": "ML Classification App",
        "desc": "AI Fraud Detection was my first hackathon project (Expert Academy). Built from scratch — sourcing data on Kaggle, training ML models, deploying on AWS. Of the three team members, I was the one who stayed to finish it alone. Not perfect, but it taught me the complete ML workflow and gave me the confidence to build AI solutions independently.",
        "img": "assets/fraud.png",
        "img_alt": "SMS Fraud detection illustration",
        "href": LINKS["phishing"],
        "stack": ["scikit-learn", "DVC", "MLflow", "Docker"],
    },
]

# ---------------------------------------------------------------------------
# BRAND ICONS (inline SVG, fill currentColor)
# ---------------------------------------------------------------------------
GITHUB_ICON = (
    '<svg class="w-4 h-4" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">'
    '<path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/>'
    "</svg>"
)
LINKEDIN_ICON = (
    '<svg class="w-4 h-4" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">'
    '<path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>'
    "</svg>"
)

# ---------------------------------------------------------------------------
# HEAD
# ---------------------------------------------------------------------------
def head():
    return """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Amar Fauzie — AI Engineer | Data Scientist</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@500;600;700;800&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
<script src="https://cdn.tailwindcss.com"></script>
<script>
tailwind.config = {
  theme: {
    extend: {
      colors: {
        ink: "#121212",
        muted: "#6E6E6E",
        paper: "#FFFFFF",
        paper2: "#FAFAFA",
        paper3: "#F4F4F5",
        accent: "#ff4d00",
        accentdark: "#e64400",
      },
      fontFamily: {
        display: ["Hanken Grotesk", "sans-serif"],
        body: ["Inter", "sans-serif"],
        mono: ["JetBrains Mono", "monospace"],
      },
      borderRadius: {
        DEFAULT: "4px",
        lg: "12px",
      },
    }
  }
}
</script>
<style>
  html { scroll-behavior: smooth; }
  section[id] { scroll-margin-top: 88px; }
  ::selection { background: #ff4d00; color: #fff; }
  @keyframes pulse-dot { 0%,100% { box-shadow: 0 0 0 0 rgba(255,77,0,.5);} 50% { box-shadow: 0 0 0 6px rgba(255,77,0,0);} }
  .pulse-dot { animation: pulse-dot 2s infinite; }
</style>
</head>
<body class="bg-paper text-ink font-body antialiased">
"""

# ---------------------------------------------------------------------------
# TOPBAR — fixed, white, hairline border, desktop links + mobile menu
# ---------------------------------------------------------------------------
def topbar():
    links = "\n".join(
        '<a href="' + href + '" class="text-sm font-medium text-muted hover:text-ink transition-colors">' + label + "</a>"
        for label, href in NAV
    )
    hire = LINKS["email"]
    return f"""
<header class="fixed top-0 inset-x-0 z-50 bg-paper/90 backdrop-blur border-b border-paper3">
  <div class="mx-auto max-w-[1280px] px-5 md:px-16 h-16 flex items-center justify-between">
    <a href="#top" class="font-display text-xl font-bold tracking-tight">Amar<span class="text-accent">.</span></a>
    <nav class="hidden md:flex items-center gap-8">{links}</nav>
    <div class="flex items-center gap-3">
      <a href="{hire}" class="hidden md:inline-flex bg-ink text-paper text-sm font-medium px-4 py-2 rounded-sm hover:bg-accent transition-colors">Hire me</a>
      <button id="menu-btn" class="md:hidden p-2 -mr-2 text-ink" aria-label="Open menu">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M4 7h16M4 12h16M4 17h16"/></svg>
      </button>
    </div>
  </div>
  <nav id="mobile-menu" class="hidden md:hidden bg-paper border-b border-paper3 px-5 py-4 flex flex-col gap-4">
    {links}
    <a href="{hire}" class="inline-flex justify-center bg-ink text-paper text-sm font-medium px-4 py-2.5 rounded-sm">Hire me</a>
  </nav>
</header>
"""

# ---------------------------------------------------------------------------
# HERO
# ---------------------------------------------------------------------------
def hero():
    github = LINKS["github"]
    return f"""
<!-- Hero -->
<section id="top" class="mx-auto max-w-[1280px] px-5 md:px-16 pt-36 pb-20 md:pb-28 min-h-screen flex items-center">
  <div class="w-full">
    <div class="flex items-center gap-3 mb-8">
      <span class="w-2 h-2 rounded-full bg-accent pulse-dot"></span>
      <span class="font-mono text-xs md:text-sm tracking-[0.2em] text-muted uppercase">Available for work</span>
    </div>
    <h1 class="font-display font-extrabold tracking-tight leading-[1.04] text-5xl md:text-7xl lg:text-8xl">
      Amar Fauzie<span class="text-accent">.</span>
    </h1>
    <h2 class="mt-4 font-mono text-xs md:text-sm text-muted tracking-[0.25em] uppercase">
      AI Engineer · Data Scientist · Language Nerd
    </h2>
    <p class="mt-10 max-w-xl text-base md:text-lg text-muted leading-relaxed">
      I&rsquo;m an Arabic and Islamic studies graduate turned self-taught AI and
      data science enthusiast, driven by curiosity to connect language,
      analytical thinking, and technology to solve real-world problems.
    </p>
    <div class="mt-10 flex flex-wrap gap-3">
      <a href="#projects" class="bg-accent text-white px-6 py-3 rounded font-medium hover:bg-accentdark transition-colors">View projects</a>
      <a href="#about" class="border border-ink px-6 py-3 rounded font-medium hover:bg-ink hover:text-paper transition-colors">My story</a>
      <a href="{github}" target="_blank" rel="noopener" class="inline-flex items-center gap-2 border border-paper3 px-6 py-3 rounded font-medium text-muted hover:text-ink hover:border-ink transition-colors">
        {GITHUB_ICON}<span>GitHub</span>
      </a>
    </div>
    <div class="mt-16 pt-6 border-t border-paper3 flex flex-wrap gap-x-10 gap-y-3 font-mono text-xs text-muted">
      <span>Python</span><span>FastAPI</span><span>LangGraph</span><span>Qdrant</span><span>Docker</span><span>Machine Learning</span>
    </div>
  </div>
</section>
"""

# ---------------------------------------------------------------------------
# PROJECTS
# ---------------------------------------------------------------------------
def projects():
    out = []
    for p in PROJECTS:
        chips = "\n".join(
            '<span class="px-2.5 py-1 bg-paper3 font-mono text-[11px] rounded">' + s + "</span>"
            for s in p["stack"]
        )
        if p.get("img"):
            preview = f'<img src="{p["img"]}" alt="{p["img_alt"]}" class="w-full h-full object-cover">'
        else:
            preview = '<div class="w-full h-full flex items-center justify-center font-mono text-xs text-muted">preview</div>'
        href = p["href"]
        cards = f"""
  <article class="bg-paper border border-paper3 rounded-lg hover:border-ink transition-colors flex flex-col">
    <div class="aspect-[16/10] bg-paper2 border-b border-paper3 overflow-hidden">{preview}</div>
    <div class="p-6 md:p-8 flex flex-col grow">
      <div class="flex items-center justify-between mb-3">
        <span class="font-mono text-xs text-accent">/ {p["index"]}</span>
        <span class="font-mono text-xs text-muted">{p["sub"]}</span>
      </div>
      <h3 class="font-display text-2xl md:text-3xl font-bold tracking-tight">{p["name"]}</h3>
      <p class="mt-4 text-sm md:text-base text-muted leading-relaxed grow">{p["desc"]}</p>
      <div class="flex flex-wrap gap-2 mt-6">{chips}</div>
      <a href="{href}" target="_blank" rel="noopener" class="mt-6 inline-flex items-center gap-2 font-mono text-sm text-accent hover:text-ink transition-colors w-fit">View repository <span aria-hidden="true">↗</span></a>
    </div>
  </article>"""
        out.append(cards)
    return f"""
<!-- Projects -->
<section id="projects" class="mx-auto max-w-[1280px] px-5 md:px-16 py-24 md:py-32 border-t border-paper3">
  <div class="flex items-end justify-between gap-8 mb-14 flex-wrap">
    <div>
      <p class="font-mono text-xs tracking-[0.2em] text-accent uppercase mb-3">01 / Selected Work</p>
      <h2 class="font-display font-extrabold tracking-tight text-4xl md:text-5xl">Projects</h2>
    </div>
    <p class="max-w-sm text-muted text-sm md:text-base">A portfolio of work bridging classical scholarship and modern computation.</p>
  </div>
  <div class="grid grid-cols-1 md:grid-cols-2 gap-6 md:gap-8">
{chr(10).join(out)}
  </div>
</section>
"""

# ---------------------------------------------------------------------------
# SKILLS + CERTIFICATIONS
# ---------------------------------------------------------------------------
def skills(certs):
    dlai = [c for c in certs if "Coursera" not in c["issuer"]]
    coursera = [c for c in certs if "Coursera" in c["issuer"]]

    def group(title, items, accent=True):
        chips = "".join(
            '<span class="px-3 py-1.5 bg-paper3 font-mono text-[11px] rounded-sm">' + s + "</span>"
            for s in items
        )
        dot = '<span class="w-1.5 h-1.5 rounded-full bg-accent"></span>' if accent else '<span class="w-1.5 h-1.5 rounded-full bg-ink"></span>'
        return f"""
    <div class="border border-paper3 rounded-sm p-6 md:p-8 bg-paper">
      <div class="flex items-center gap-2 mb-6">{dot}<h3 class="font-display font-bold text-lg tracking-tight">{title}</h3></div>
      <div class="flex flex-wrap gap-2">{chips}</div>
    </div>"""

    groups = (
        group("Languages", SKILLS[0][1])
        + group("Frameworks & Tools", SKILLS[1][1])
        + group("AI & Machine Learning", SKILLS[2][1])
        + group("Cloud & Data", SKILLS[3][1])
    )

    def cert_row(c):
        return f"""
    <div class="flex items-start md:items-center justify-between gap-4 border-b border-paper3 py-4 last:border-0">
      <div>
        <p class="text-sm md:text-base font-medium leading-snug">{c["title"]}</p>
        <p class="font-mono text-xs text-muted mt-1">{c["issuer"]}</p>
      </div>
      <a href="{c["url"]}" target="_blank" rel="noopener" class="shrink-0 font-mono text-xs text-accent hover:underline">Verify ↗</a>
    </div>"""

    def block(title, items):
        return f"""
    <div class="border border-paper3 rounded-sm p-6 md:p-8">
      <h3 class="font-mono text-xs tracking-[0.2em] text-muted uppercase mb-6">{title}</h3>
      {chr(10).join(items)}
    </div>"""

    return f"""
<!-- Skills -->
<section id="skills" class="bg-paper2 border-y border-paper3 py-24 md:py-32">
  <div class="mx-auto max-w-[1280px] px-5 md:px-16">
    <p class="font-mono text-xs tracking-[0.2em] text-accent uppercase mb-3">02 / Capabilities</p>
    <h2 class="font-display font-extrabold tracking-tight text-4xl md:text-5xl mb-14">Skills &amp; Credentials</h2>
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 md:gap-8">{groups}</div>
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 md:gap-8 mt-8">
      {block("Machine Learning Specialization — Coursera", [cert_row(c) for c in coursera])}
      {block("Advanced AI Short Courses — DeepLearning.AI", [cert_row(c) for c in dlai])}
    </div>
  </div>
</section>
"""

# ---------------------------------------------------------------------------
# ABOUT
# ---------------------------------------------------------------------------
def about():
    return """
<!-- About -->
<section id="about" class="mx-auto max-w-[1280px] px-5 md:px-16 py-24 md:py-32">
  <p class="font-mono text-xs tracking-[0.2em] text-accent uppercase mb-3">03 / The Story</p>
  <h2 class="font-display font-extrabold tracking-tight text-4xl md:text-5xl max-w-2xl leading-tight mb-16">From Madinah to machine learning<span class="text-accent">.</span></h2>
  <div class="grid grid-cols-1 lg:grid-cols-2 gap-10 lg:gap-16 items-start">
    <div class="space-y-8 text-muted leading-relaxed text-sm md:text-base">
      <p>My journey has taken a path I never expected. During high school I was in the science stream — Additional Mathematics, Physics, Chemistry, Biology — certain I would become a doctor or an engineer one day. After SPM, my mother invited me to perform Umrah with my eldest brother. That journey changed the direction of my life.</p>
      <p>In Madinah I met someone named Ahmad at a grocery store near the Prophet&rsquo;s Mosque. We could barely communicate — I knew no Arabic, he knew no Malay — but we stayed in contact through WhatsApp, with Google Translate carrying our conversations. That small connection sparked a new curiosity in me. I started learning Arabic seriously, and my dream shifted from medicine to language and its sciences.</p>
      <p>Years later I earned a Diploma in Arabic Language and Literature from UniSZA, then a Bachelor&rsquo;s in Theology from the Islamic University of Madinah. The story didn&rsquo;t end there: curiosity pulled me back to mathematics and problem-solving, and I discovered data science — the bridge between my analytical background and my love of technology. Since then I&rsquo;ve studied machine learning, deep learning, and AI, exploring how technology can solve real-world problems.</p>
    </div>
    <div class="space-y-6">
      <div class="border border-paper3 rounded-sm p-6 md:p-8 bg-paper2">
        <h3 class="font-display font-bold text-lg tracking-tight mb-6 flex items-center gap-2"><span class="w-1.5 h-1.5 rounded-full bg-accent"></span>Education</h3>
        <div class="space-y-6">
          <div><p class="font-medium text-ink">B.A. Theology</p><p class="font-mono text-xs text-muted mt-1">Islamic University of Madinah</p></div>
          <div><p class="font-medium text-ink">Diploma, Arabic Language &amp; Literature</p><p class="font-mono text-xs text-muted mt-1">Universiti Sultan Zainal Abidin</p></div>
        </div>
      </div>
      <div class="border border-paper3 rounded-sm p-6 md:p-8 bg-paper2/50">
        <h3 class="font-display font-bold text-lg tracking-tight mb-6 flex items-center gap-2"><span class="w-1.5 h-1.5 rounded-full bg-accent"></span>Languages</h3>
        <div class="space-y-6">
          <div><p class="font-medium text-ink">Malay</p><p class="font-mono text-xs text-muted mt-1">Native</p></div>
          <div><p class="font-medium text-ink">English</p><p class="font-mono text-xs text-muted mt-1">Fluent</p></div>
          <div><p class="font-medium text-ink">Arabic</p><p class="font-mono text-xs text-muted mt-1">Fluent — studied in Madinah</p></div>
        </div>
      </div>
    </div>
  </div>
  <div class="mt-12 md:mt-16">
    <h3 class="font-mono text-xs tracking-[0.2em] text-muted uppercase mb-8">Experience</h3>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-x-10 gap-y-8">
      <div class="border-t border-ink pt-4"><div class="flex justify-between gap-4 flex-wrap"><h4 class="font-display font-bold text-lg">Hajj Guide / Mutawwif</h4><span class="font-mono text-xs text-muted">2024 — 26</span></div><p class="font-mono text-xs text-muted mt-1">Tabung Haji</p><p class="text-sm text-muted mt-3 leading-relaxed">Communicated religious, logistical, and safety information to pilgrims from diverse backgrounds; managed coordination and problem-solving in a high-pressure, time-sensitive environment.</p></div>
      <div class="border-t border-ink pt-4"><div class="flex justify-between gap-3 flex-wrap"><h4 class="font-display font-bold text-lg">Company Representative</h4><span class="font-mono text-xs text-muted">Forum</span></div><p class="font-mono text-xs text-muted mt-1">Siiru — Hajj &amp; Umrah Forum, King Salman Int&rsquo;l Convention Centre</p><p class="text-sm text-muted mt-3 leading-relaxed">Presented company offerings and engaged diverse audiences in a professional, public-facing exhibition environment.</p></div>
      <div class="border-t border-ink pt-4"><div class="flex justify-between gap-3 flex-wrap"><h4 class="font-display font-bold text-lg">Committee Member (AJK)</h4><span class="font-mono text-xs text-muted">Committee</span></div><p class="font-mono text-xs text-muted mt-1">Nadi Pencinta Madinah</p><p class="text-sm text-muted mt-3 leading-relaxed">Co-created educational modules and organized cultural activities and historical tours across Makkah, Madinah, and Taif for Malaysian students.</p></div>
      <div class="border-t border-ink pt-4"><div class="flex justify-between gap-3 flex-wrap"><h4 class="font-display font-bold text-lg">President</h4><span class="font-mono text-xs text-muted">2019 — 20</span></div><p class="font-mono text-xs text-muted mt-1">ARCOM, International Islamic University Malaysia</p><p class="text-sm text-muted mt-3 leading-relaxed">Led a student organization focused on Arabic communication; organized competitions and represented the group in Arabic debate and public speaking.</p></div>
    </div>
  </div>
</section>
"""

# ---------------------------------------------------------------------------
# CONTACT
# ---------------------------------------------------------------------------
def contact():
    email = LINKS["email"]
    github = LINKS["github"]
    linkedin = LINKS["linkedin"]
    return f"""
<!-- Contact -->
<section id="contact" class="bg-ink text-paper py-24 md:py-32">
  <div class="mx-auto max-w-[1280px] px-5 md:px-16 text-center">
    <p class="font-mono text-xs tracking-[0.2em] text-accent uppercase mb-4">04 / Contact</p>
    <h2 class="font-display font-extrabold tracking-tight text-4xl md:text-6xl max-w-3xl mx-auto leading-tight">Let&rsquo;s build something useful<span class="text-accent">.</span></h2>
    <p class="mt-6 text-paper/70 max-w-xl mx-auto text-sm md:text-base">Looking for opportunities in AI engineering, data science, and ML — remote or Malaysia-based.</p>
    <div class="mt-10 flex flex-wrap justify-center gap-3">
      <a href="{email}" class="bg-accent text-white px-8 py-3.5 rounded font-medium hover:bg-accentdark transition-colors">Contact me</a>
      <a href="{github}" target="_blank" rel="noopener" class="inline-flex items-center gap-2 border border-paper/40 px-8 py-3.5 rounded font-medium hover:border-paper transition-colors">
        {GITHUB_ICON}<span>GitHub</span>
      </a>
      <a href="{linkedin}" target="_blank" rel="noopener" class="inline-flex items-center gap-2 border border-paper/40 px-8 py-3.5 rounded font-medium hover:border-paper transition-colors">
        {LINKEDIN_ICON}<span>LinkedIn</span>
      </a>
    </div>
    <p class="mt-16 font-mono text-xs text-paper/40">© 2026 Amar Fauzie — built with Python, coffee, and a lot of curiosity.</p>
  </div>
</section>
"""

# ---------------------------------------------------------------------------
# SCRIPT
# ---------------------------------------------------------------------------
def scripts():
    return """
<script>
  const menuBtn = document.getElementById('menu-btn');
  const mobileMenu = document.getElementById('mobile-menu');
  if (menuBtn) menuBtn.addEventListener('click', () => mobileMenu.classList.toggle('hidden'));
</script>
</body>
</html>
"""

# ---------------------------------------------------------------------------
# BUILD
# ---------------------------------------------------------------------------
PAGES = [
    ("index.html", head() + topbar() + hero() + projects() + skills(CERTS) + about() + contact() + scripts()),
]

for fname, html in PAGES:
    path = os.path.join(OUT, fname)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"wrote {fname} ({len(html):,} bytes)")
print("done")