# -*- coding: utf-8 -*-
"""Motor de geração do site estático do Instituto Christian Andrade.
Gera HTML a partir de templates Python simples (sem dependências externas).
Rode com: python3 tools/build.py
"""
import json
import os

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
BASE_URL = "https://www.christianandrade.com.br"
SITE_NAME = "Instituto Christian Andrade"
PHONE_DISPLAY = "(41) 99873-0054"
PHONE_TEL = "+554198730054"
PHONE_SJP_DISPLAY = "(41) 3030-3010"
PHONE_SJP_TEL = "+554130303010"
EMAIL = "contato@christianandrade.com.br"
WHATSAPP_NUMBER = "5541996962223"

TODAY = "2026-09-11"

# ---------------------------------------------------------------------------
# Google Tag Manager
# Assim que o container for criado, cole o ID (formato "GTM-XXXXXXX") abaixo
# e rode `python3 tools/build.py` de novo — o snippet é injetado automaticamente
# em <head> e logo após <body> em TODAS as páginas. Enquanto estiver vazio,
# nenhum script do GTM é carregado, mas o dataLayer já é inicializado e
# populado por js/main.js (ver seção "rastreamento avançado" lá), então nenhum
# evento é perdido: o GTM lê o histórico do dataLayer assim que carregar.
# ---------------------------------------------------------------------------
GTM_CONTAINER_ID = ""  # ex.: "GTM-ABCD123"


def gtm_head_snippet():
    if not GTM_CONTAINER_ID:
        return ""
    return f'''<script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':
new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
}})(window,document,'script','dataLayer','{GTM_CONTAINER_ID}');</script>
'''


def gtm_body_snippet():
    if not GTM_CONTAINER_ID:
        return ""
    return (f'<noscript><iframe src="https://www.googletagmanager.com/ns.html?id={GTM_CONTAINER_ID}" '
            'height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>\n')

def wa_link(message):
    import urllib.parse
    return f"https://api.whatsapp.com/send?phone={WHATSAPP_NUMBER}&text={urllib.parse.quote(message)}"

WA_DEFAULT = wa_link("Olá Instituto Christian Andrade, quero agendar uma avaliação.")

# ---------------------------------------------------------------------------
# Banco de imagens (verificadas — fotos de estoque profissionais, licença
# livre Unsplash). Recomenda-se substituir por fotos reais da clínica e da
# equipe assim que possível para reforçar autenticidade (E-E-A-T).
# ---------------------------------------------------------------------------
IMG = {
    "consulta": "1606811841689-23dfddce3e95",     # dentista e paciente avaliando raio-x
    "raiox": "1588776814546-1ffcf47267a5",         # close-up exame de imagem
    "clinica_azul": "1629909613654-28e377c37b09",  # clínica branca/azul moderna
    "clinica_ampla": "1629909615184-74f495363b67", # clínica branca ampla
    "alinhador": "1609840114035-3c981b782dfe",     # alinhador ortodôntico transparente
    "clinica_vista": "1609207825181-52d3214556dd", # clínica clara com vista externa
    "clinica_vermelha": "1616391182219-e080b4d1043a", # clínica moderna cadeira vermelha
    "equipe": "1600334129128-685c5582fd35",        # profissional de jaleco branco
}

def img(key, w, h=None, q=80):
    photo_id = IMG[key]
    url = f"https://images.unsplash.com/photo-{photo_id}?q={q}&w={w}&auto=format&fit=crop"
    if h:
        url += f"&h={h}"
    return url

# ---------------------------------------------------------------------------
# Dados reais extraídos do site anterior (endereços, telefones, CROs, depoimentos)
# ---------------------------------------------------------------------------
UNITS = [
    {
        "key": "batel", "num": "01", "name": "Clínica Batel",
        "region": "Batel · Curitiba",
        "address": "Av. Silva Jardim, 2520 — Batel, Curitiba/PR",
        "phone_display": PHONE_DISPLAY, "phone_tel": PHONE_TEL,
        "doctor": "Dra. Sandra Mara Hretzko", "cro": "CRO/PR 12411 · CLM/PR 3311",
        "img": img("clinica_azul", 1000, 800),
        "maps_q": "Av.+Silva+Jardim,+2520,+Batel,+Curitiba,+PR",
    },
    {
        "key": "sitio-cercado", "num": "02", "name": "Clínica Sítio Cercado",
        "region": "Sítio Cercado · Curitiba",
        "address": "Rua Agudos do Sul, 40 — Sítio Cercado, Curitiba/PR",
        "phone_display": PHONE_DISPLAY, "phone_tel": PHONE_TEL,
        "doctor": "Dra. Barbara Hauser Novicki", "cro": "CRO/PR 22234 · CLM/PR 1695",
        "img": "images/unidade-sitio-cercado.webp",
        "maps_q": "Rua+Agudos+do+Sul,+40,+Sitio+Cercado,+Curitiba,+PR",
    },
    {
        "key": "pinhais", "num": "03", "name": "Clínica Pinhais (Weissópolis)",
        "region": "Weissópolis · Pinhais",
        "address": "Av. Iraí, 1632 — loja 2 — Weissópolis, Pinhais/PR",
        "phone_display": PHONE_DISPLAY, "phone_tel": PHONE_TEL,
        "doctor": "Dr. Mário Hayashi Junior", "cro": "CRO/PR 17908",
        "img": "images/unidade-pinhais.webp",
        "maps_q": "Av.+Irai,+1632,+Weissopolis,+Pinhais,+PR",
    },
    {
        "key": "sjp", "num": "04", "name": "Clínica São José dos Pinhais",
        "region": "Carioca · São José dos Pinhais",
        "address": "Av. Margarida de Araújo Franco, 2008 — Carioca, SJP/PR",
        "phone_display": PHONE_SJP_DISPLAY, "phone_tel": PHONE_SJP_TEL,
        "doctor": "Dra. Rafaela Bueno Silva", "cro": "CRO/PR 32974 · CFL 1953",
        "img": "images/unidade-sjp.webp",
        "maps_q": "Av.+Margarida+de+Araujo+Franco,+2008,+Sao+Jose+dos+Pinhais,+PR",
    },
]

TREATMENTS = [
    {
        "key": "harmonizacao", "num": "01", "slug": "tratamento-harmonizacao-orofacial.html",
        "name": "Harmonização Orofacial",
        "short": "Bichectomia, fios de sustentação e preenchimento facial para equilíbrio entre boca e rosto.",
        "eyebrow": "Harmonização Orofacial",
    },
    {
        "key": "ortodontia", "num": "02", "slug": "tratamento-ortodontia.html",
        "name": "Ortodontia",
        "short": "Aparelho estético, invisível ou metálico — o alinhamento certo para a sua rotina.",
        "eyebrow": "Ortodontia",
    },
    {
        "key": "implantes", "num": "03", "slug": "tratamento-implantes.html",
        "name": "Implantes e cirurgia guiada",
        "short": "Sistema Grand Morse Neodent, com garantia vitalícia e planejamento digital.",
        "eyebrow": "Implantes e Cirurgia Guiada",
    },
    {
        "key": "facetas", "num": "04", "slug": "tratamento-facetas-lentes.html",
        "name": "Facetas e lentes de contato",
        "short": "Lâminas ultrafinas e facetas que corrigem cor, forma e alinhamento do sorriso.",
        "eyebrow": "Facetas e Lentes de Contato Dental",
    },
    {
        "key": "geral", "num": "05", "slug": "tratamento-odontologia-geral.html",
        "name": "Odontologia geral",
        "short": "Limpeza, clareamento, endodontia, restaurações e extrações — a base da sua saúde bucal.",
        "eyebrow": "Odontologia Geral",
    },
]

TESTIMONIALS = [
    {"initial": "S", "name": "Suely Pimpão Maquiagens", "role": "Harmonização facial",
     "quote": "Recomendo o Instituto pela qualidade do local, do atendimento de toda equipe e dos profissionais qualificados. Já estou a um ano fazendo procedimentos na harmonização facial e me sinto maravilhada."},
    {"initial": "E", "name": "Edna Mattar", "role": "Implantes",
     "quote": "Fiquei muito feliz com o atendimento, profissionais qualificados e atenciosos, esperei 30 anos para realizar esse sonho. Agradeço por fazerem parte dessa realização!"},
    {"initial": "V", "name": "Vera Andrade", "role": "Familiar de paciente",
     "quote": "Minha mãe tinha dificuldade em comer, falar, sorrir, perda de peso, após vários tratamentos sem sucesso. Procuramos o Dr. Christian. Hoje minha mãe recuperou o peso, está bem, está feliz. Agora só alegria."},
    {"initial": "S", "name": "Selena Maria Pimpão", "role": "Paciente",
     "quote": "Só tenho a agradecer o meu atendimento a esta clínica maravilhosa. Desde o 1º contato até o término foi tudo bem encaminhado. Hoje sou uma nova pessoa e tenho de volta minha autoestima."},
    {"initial": "E", "name": "Elias Patricia", "role": "Paciente",
     "quote": "Atendimento nota 10. Fiquei muito satisfeito, gostei muito do resultado. Vale a pena, o trabalho é excelente com grandes profissionais."},
    {"initial": "D", "name": "Dena Ruthes", "role": "Paciente",
     "quote": "Sou paciente da clínica e estou super, mega feliz. Atendimento excelente. Desde a recepção, os doutores são super atenciosos e passam segurança."},
]

NAV = [
    ("home", "Home", "index.html"),
    ("sobre", "Sobre a Clínica", "sobre.html"),
    ("tratamentos", "Tratamentos", "tratamentos.html"),
    ("blog", "Blog", "blog/index.html"),
    ("unidades", "Unidades", "unidades.html"),
    ("depoimentos", "Depoimentos", "depoimentos.html"),
    ("contato", "Contato", "contato.html"),
]

FOOTER_TREATMENT_LINKS = [
    ("Harmonização orofacial", "tratamentos.html#harmonizacao"),
    ("Ortodontia", "tratamentos.html#ortodontia"),
    ("Implantes", "tratamentos.html#implantes"),
    ("Facetas e lentes", "tratamentos.html#facetas"),
    ("Odontologia geral", "tratamentos.html#geral"),
]

PAGES_REGISTRY = []  # preenchido por page()

# ---------------------------------------------------------------------------
# Helpers de marcação
# ---------------------------------------------------------------------------

def jsonld(data):
    return f'<script type="application/ld+json">{json.dumps(data, ensure_ascii=False)}</script>'


def breadcrumb_ld(items, root_path=""):
    """items: lista de (nome, path-relativo-ao-site-a-partir-da-raiz ou None p/ atual)"""
    elements = []
    for i, (name, path) in enumerate(items, start=1):
        entry = {"@type": "ListItem", "position": i, "name": name}
        if path:
            entry["item"] = f"{BASE_URL}/{path}"
        elements.append(entry)
    return jsonld({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": elements})


def faq_ld(items):
    return jsonld({
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in items
        ],
    })


def faq_block(items):
    rows = []
    for i, (q, a) in enumerate(items):
        open_attr = " open" if i == 0 else ""
        rows.append(f'''        <details{open_attr}>
          <summary>{q}<span class="icon">+</span></summary>
          <p class="a">{a}</p>
        </details>''')
    return '\n' + '\n'.join(rows) + '\n      '


def logo_mark():
    return ('<svg class="logo-mark" width="26" height="26" viewBox="0 0 24 24" fill="none" aria-hidden="true">'
            '<path d="M12 2C8.5 2 6 4 6 7.3c0 2.2.7 3.1 1.1 5.4.4 2.4.5 6.8 2 8.9.5.7 1 .9 1.4.9.9 0 1.2-1 1.4-2.6.2-1.6.3-3.8 1-3.8s.8 2.2 1 3.8c.2 1.6.5 2.6 1.4 2.6.4 0 .9-.2 1.4-.9 1.5-2.1 1.6-6.5 2-8.9C18.3 10.4 19 9.5 19 7.3 19 4 16.5 2 13 2c-.4 0-.7.6-1 .6S12.4 2 12 2z" '
            'stroke="currentColor" stroke-width="1.4" stroke-linejoin="round"/></svg>')


def topbar(root):
    links = "\n      ".join(
        f'<a href="{root}unidades.html#{u["key"]}"><span>{u["num"]}</span>{u["region"].split(" · ")[0]}</a>'
        for u in UNITS
    )
    return f'''<div class="topbar">
  <div class="wrap">
    <div class="topbar-units">
      {links}
    </div>
    <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>
  </div>
</div>'''


def header(root, active):
    active_cls = ' class="active"'
    nav_links = "\n      ".join(
        f'<a href="{root}{href}"{active_cls if key == active else ""}>{label}</a>'
        for key, label, href in NAV
    )
    return f'''<header class="site-header">
  <div class="wrap">
    <a href="{root}index.html" class="logo">{logo_mark()} Christian Andrade <span>Odontologia</span></a>
    <nav class="main-nav" id="main-nav">
      {nav_links}
    </nav>
    <div class="nav-cta">
      <span class="nav-phone">{PHONE_DISPLAY}</span>
      <a class="btn btn-gold btn-sm" href="{WA_DEFAULT}" target="_blank" rel="noopener">Agendar avaliação</a>
      <button class="nav-toggle" aria-label="Abrir menu" aria-expanded="false"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>
<div class="nav-scrim"></div>'''


def footer(root):
    unit_links = "\n          ".join(
        f'<li><a href="{root}unidades.html#{u["key"]}">{u["region"].split(" · ")[0]}</a></li>' for u in UNITS
    )
    treat_links = "\n          ".join(
        f'<li><a href="{root}{href}">{label}</a></li>' for label, href in FOOTER_TREATMENT_LINKS
    )
    return f'''<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <div class="footer-logo">{logo_mark()} Christian Andrade</div>
        <p>Instituto Odontológico com 4 unidades em Curitiba e região, atuando desde 2005 em odontologia e harmonização orofacial. O branco da porcelana e a confiança clínica guiam cada atendimento.</p>
        <div class="footer-social">
          <a href="{WA_DEFAULT}" target="_blank" rel="noopener" aria-label="WhatsApp"><svg width="16" height="16" viewBox="0 0 24 24" fill="none"><path d="M17.5 14.4c-.3-.1-1.6-.8-1.9-.9-.3-.1-.4-.1-.6.1-.2.3-.7.9-.8 1-.2.2-.3.2-.5.1-.3-.1-1.2-.4-2.2-1.4-.8-.7-1.4-1.6-1.5-1.9-.2-.3 0-.5.1-.6.1-.1.3-.3.4-.5.2-.1.2-.3.3-.4.1-.2 0-.4 0-.5-.1-.1-.6-1.5-.8-2-.2-.5-.4-.4-.6-.5h-.5c-.2 0-.5.1-.7.3-.2.3-1 1-1 2.3 0 1.4 1 2.7 1.1 2.9.1.2 2 3.1 4.9 4.3.7.3 1.2.5 1.6.6.7.2 1.3.2 1.8.1.5-.1 1.6-.7 1.9-1.3.2-.6.2-1.1.2-1.2-.1-.1-.3-.2-.5-.3z" fill="#fff"/><path d="M12 2a10 10 0 00-8.6 15L2 22l5.2-1.4A10 10 0 1012 2zm0 18.2a8.2 8.2 0 01-4.2-1.1l-.3-.2-3.1.8.8-3-.2-.3A8.2 8.2 0 1120.2 12 8.2 8.2 0 0112 20.2z" fill="#fff"/></svg></a>
          <a href="mailto:{EMAIL}" aria-label="E-mail"><svg width="16" height="16" viewBox="0 0 24 24" fill="none"><path d="M3 6h18v12H3z" stroke="#fff" stroke-width="1.4"/><path d="M3 7l9 6 9-6" stroke="#fff" stroke-width="1.4"/></svg></a>
        </div>
      </div>
      <div>
        <h5>Navegação</h5>
        <ul>
          <li><a href="{root}index.html">Home</a></li>
          <li><a href="{root}sobre.html">Sobre a clínica</a></li>
          <li><a href="{root}tratamentos.html">Tratamentos</a></li>
          <li><a href="{root}blog/index.html">Blog</a></li>
          <li><a href="{root}depoimentos.html">Depoimentos</a></li>
          <li><a href="{root}contato.html">Contato</a></li>
        </ul>
      </div>
      <div>
        <h5>Tratamentos</h5>
        <ul>
          {treat_links}
        </ul>
      </div>
      <div>
        <h5>Unidades</h5>
        <ul>
          {unit_links}
        </ul>
      </div>
      <div>
        <h5>Contato</h5>
        <ul>
          <li><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li><a href="{WA_DEFAULT}" target="_blank" rel="noopener">WhatsApp</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© 2026 Instituto Christian Andrade — CNPJ e responsabilidade técnica por unidade. Todos os direitos reservados.</span>
      <span>{PHONE_DISPLAY} · Av. Silva Jardim, 2520, Batel, Curitiba/PR</span>
    </div>
  </div>
</footer>'''


def wa_float(root):
    return f'''<a class="wa-float" href="{WA_DEFAULT}" target="_blank" rel="noopener" aria-label="Conversar no WhatsApp">
  <svg width="27" height="27" viewBox="0 0 24 24" fill="none"><path d="M17.5 14.4c-.3-.1-1.6-.8-1.9-.9-.3-.1-.4-.1-.6.1-.2.3-.7.9-.8 1-.2.2-.3.2-.5.1-.3-.1-1.2-.4-2.2-1.4-.8-.7-1.4-1.6-1.5-1.9-.2-.3 0-.5.1-.6.1-.1.3-.3.4-.5.2-.1.2-.3.3-.4.1-.2 0-.4 0-.5-.1-.1-.6-1.5-.8-2-.2-.5-.4-.4-.6-.5h-.5c-.2 0-.5.1-.7.3-.2.3-1 1-1 2.3 0 1.4 1 2.7 1.1 2.9.1.2 2 3.1 4.9 4.3.7.3 1.2.5 1.6.6.7.2 1.3.2 1.8.1.5-.1 1.6-.7 1.9-1.3.2-.6.2-1.1.2-1.2-.1-.1-.3-.2-.5-.3z" fill="#fff"/><path d="M12 2a10 10 0 00-8.6 15L2 22l5.2-1.4A10 10 0 1012 2zm0 18.2a8.2 8.2 0 01-4.2-1.1l-.3-.2-3.1.8.8-3-.2-.3A8.2 8.2 0 1120.2 12 8.2 8.2 0 0112 20.2z" fill="#fff"/></svg>
</a>
<button class="back-to-top" aria-label="Voltar ao topo"><svg width="18" height="18" viewBox="0 0 24 24" fill="none"><path d="M12 19V5M5 12l7-7 7 7" stroke="#0F211B" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></button>'''


def lp_header(root):
    """Cabeçalho minimalista para landing pages de tráfego pago: sem menu,
    sem links de saída — só marca e telefone, para não competir com o CTA."""
    return f'''<header class="lp-header">
  <div class="wrap">
    <span class="logo">{logo_mark()} Christian Andrade <span>Odontologia</span></span>
    <a class="lp-header-phone" href="tel:{PHONE_TEL}">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none"><path d="M6.6 10.8c1.4 2.8 3.8 5.1 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.5.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1C10.3 21 3 13.7 3 5c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.2.2 2.4.6 3.5.1.4 0 .8-.2 1L6.6 10.8z" stroke="currentColor" stroke-width="1.4" stroke-linejoin="round"/></svg>
      {PHONE_DISPLAY}
    </a>
  </div>
</header>'''


def lp_footer(root):
    """Rodapé enxuto para landing pages: identificação legal mínima, sem
    sitemap completo (evita abrir rotas de saída da página de conversão)."""
    return f'''<footer class="lp-footer">
  <div class="wrap">
    <p>© 2026 Instituto Christian Andrade — odontologia e harmonização orofacial desde 2005. {PHONE_DISPLAY} · {EMAIL}</p>
    <a href="{root}index.html">Conhecer o site completo →</a>
  </div>
</footer>'''


ORG_LOGO = f"{BASE_URL}/favicon.svg"

def organization_ld():
    return {
        "@context": "https://schema.org",
        "@type": "Organization",
        "@id": f"{BASE_URL}/#organization",
        "name": SITE_NAME,
        "alternateName": "Christian Andrade Odontologia",
        "url": BASE_URL + "/",
        "logo": ORG_LOGO,
        "image": img("clinica_azul", 1200, 800),
        "telephone": PHONE_TEL,
        "email": EMAIL,
        "sameAs": [],
        "foundingDate": "2005",
        "medicalSpecialty": ["Dentistry", "Orthodontics", "OralSurgery", "CosmeticSurgery"],
        "areaServed": {"@type": "City", "name": "Curitiba"},
        "department": [unit_ld(u) for u in UNITS],
    }


def abs_url(path):
    return path if path.startswith("http") else f"{BASE_URL}/{path}"


def unit_ld(u):
    return {
        "@type": "Dentist",
        "name": f"{SITE_NAME} — {u['name']}",
        "image": abs_url(u["img"]),
        "telephone": u["phone_tel"],
        "priceRange": "$$",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": u["address"].split("—")[0].strip(),
            "addressLocality": u["region"].split(" · ")[-1],
            "addressRegion": "PR",
            "addressCountry": "BR",
        },
        "medicalSpecialty": ["Dentistry"],
    }


def website_ld():
    return {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "url": BASE_URL + "/",
        "name": SITE_NAME,
        "publisher": {"@id": f"{BASE_URL}/#organization"},
        "inLanguage": "pt-BR",
    }


# ---------------------------------------------------------------------------
# Montagem de página
# ---------------------------------------------------------------------------

def page(path, title, description, active, body, root="", json_ld_list=None,
         og_image=None, priority="0.6", changefreq="monthly", extra_head="",
         robots="index, follow", chrome="full"):
    canonical = f"{BASE_URL}/{path}" if path != "index.html" else f"{BASE_URL}/"
    og_image = og_image or img("clinica_azul", 1200, 630)
    json_ld_list = json_ld_list or []
    json_ld_html = "\n".join(jsonld(d) if isinstance(d, dict) else d for d in json_ld_list)

    html = f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<script>window.dataLayer = window.dataLayer || [];</script>
{gtm_head_snippet()}<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<meta name="robots" content="{robots}">
<meta name="theme-color" content="#FFFFFF">
<link rel="icon" type="image/svg+xml" href="{root}favicon.svg">
<link rel="apple-touch-icon" href="{root}favicon.svg">

<meta property="og:type" content="website">
<meta property="og:site_name" content="{SITE_NAME}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{og_image}">
<meta property="og:locale" content="pt_BR">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="{og_image}">

<link rel="stylesheet" href="{root}css/style.css">
{extra_head}{json_ld_html}
</head>
<body>
{gtm_body_snippet()}
{topbar(root) if chrome == "full" else ""}

{header(root, active) if chrome == "full" else lp_header(root)}

<main>

{body}

</main>

{footer(root) if chrome == "full" else lp_footer(root)}

{wa_float(root)}

<script src="{root}js/main.js"></script>
</body>
</html>
'''
    full_path = os.path.join(REPO_ROOT, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(html)

    PAGES_REGISTRY.append({
        "path": path, "title": title, "description": description,
        "priority": priority, "changefreq": changefreq, "robots": robots,
    })
    return html
