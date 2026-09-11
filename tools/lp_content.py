# -*- coding: utf-8 -*-
"""Landing pages de conversão para tráfego pago (Google/Meta Ads).
Sem menu, sem links de saída, uma oferta por página, CTA único pro WhatsApp.
"""
from site_engine import page, img, wa_link, TESTIMONIALS

TESTI_BY_NAME = {t["name"]: t for t in TESTIMONIALS}


def testi_pair(names):
    return [TESTI_BY_NAME[n] for n in names]


def check_icon():
    return ('<svg width="18" height="18" viewBox="0 0 24 24" fill="none">'
            '<path d="M4 12.5l5 5L20 6" stroke="currentColor" stroke-width="2.4" '
            'stroke-linecap="round" stroke-linejoin="round"/></svg>')


LANDING_PAGES = [
    {
        "slug": "lp-avaliacao.html",
        "title": "Agende sua avaliação odontológica — Instituto Christian Andrade",
        "description": "Implantes, harmonização, ortodontia e odontologia geral em 4 unidades em Curitiba. Agende sua avaliação pelo WhatsApp.",
        "eyebrow": "Instituto Christian Andrade · desde 2005",
        "h1": "O sorriso que você adia há anos pode começar hoje",
        "sub": "Implantes, harmonização orofacial, ortodontia e odontologia geral — uma equipe multidisciplinar avalia seu caso e monta o plano certo pra você, em 4 unidades na região de Curitiba.",
        "cta": "Agendar minha avaliação",
        "img": "consulta",
        "trust": ["20+ anos de atuação", "4 unidades em Curitiba e região", "Equipe multidisciplinar especializada"],
        "wa_msg": "Olá! Vim pelo site e quero agendar uma avaliação odontológica.",
        "testi": testi_pair(["Selena Maria Pimpão", "Dena Ruthes"]),
        "final_h2": "Sua avaliação começa com uma mensagem",
        "final_p": "Sem compromisso. Conte seu caso e a equipe indica o melhor caminho.",
    },
    {
        "slug": "lp-implantes.html",
        "title": "Implantes dentários com garantia vitalícia — Instituto Christian Andrade",
        "description": "Implantes Grand Morse Neodent, cirurgia guiada sem corte e carga imediata em casos indicados. Agende sua avaliação.",
        "eyebrow": "Implantes dentários · garantia vitalícia",
        "h1": "Recupere seus dentes — e a confiança de sorrir e mastigar sem medo",
        "sub": "Sistema Grand Morse Neodent, cirurgia guiada e, em casos indicados, carga imediata: você pode sair da consulta com dentes provisórios no mesmo dia.",
        "cta": "Quero avaliar meu caso",
        "img": "raiox",
        "trust": ["Garantia vitalícia no implante", "Carga imediata em casos indicados", "Cirurgia guiada, sem corte"],
        "wa_msg": "Olá! Vi o anúncio de Implantes Dentários e quero agendar uma avaliação.",
        "testi": testi_pair(["Edna Mattar", "Vera Andrade"]),
        "final_h2": "Descubra se o implante é indicado para o seu caso",
        "final_p": "A avaliação com exame de imagem responde essa pergunta com precisão.",
    },
    {
        "slug": "lp-harmonizacao.html",
        "title": "Harmonização Orofacial — Instituto Christian Andrade",
        "description": "Bichectomia, fios de sustentação e preenchimento facial com planejamento individual. Agende sua avaliação facial.",
        "eyebrow": "Harmonização Orofacial",
        "h1": "Equilíbrio natural para o seu rosto, sem exageros",
        "sub": "Bichectomia, fios de sustentação e preenchimento facial com planejamento individual para cada rosto — o objetivo é valorizar, não transformar.",
        "cta": "Agendar minha avaliação facial",
        "img": "clinica_vista",
        "trust": ["Procedimentos minimamente invasivos", "Planejamento individual por rosto", "Conduzido por equipe odontológica habilitada"],
        "wa_msg": "Olá! Vi o anúncio de Harmonização Orofacial e quero agendar uma avaliação.",
        "testi": testi_pair(["Suely Pimpão Maquiagens", "Selena Maria Pimpão"]),
        "final_h2": "Vamos avaliar o seu rosto?",
        "final_p": "Cada indicação é individual — o primeiro passo é uma consulta de avaliação.",
    },
    {
        "slug": "lp-ortodontia.html",
        "title": "Ortodontia: aparelho estético, invisível ou metálico — Instituto Christian Andrade",
        "description": "Descubra qual aparelho ortodôntico é ideal para o seu caso. Avaliação completa e acompanhamento até o resultado final.",
        "eyebrow": "Ortodontia",
        "h1": "O sorriso alinhado que você quer, no aparelho que combina com você",
        "sub": "Estético, invisível ou metálico — a avaliação indica o tratamento certo pro seu caso, com acompanhamento completo até o resultado final.",
        "cta": "Quero saber qual aparelho é ideal",
        "img": "alinhador",
        "trust": ["Estético, invisível ou metálico", "Acompanhamento mensal completo", "Plano de tratamento sob medida"],
        "wa_msg": "Olá! Vi o anúncio de Ortodontia e quero agendar uma avaliação.",
        "testi": testi_pair(["Elias Patricia", "Dena Ruthes"]),
        "final_h2": "Vamos indicar o aparelho certo pra você?",
        "final_p": "A avaliação ortodôntica completa é o primeiro passo.",
    },
]


def build_lp(lp):
    wa = wa_link(lp["wa_msg"])
    trust_items = "\n".join(f'          <li>{check_icon()} {t}</li>' for t in lp["trust"])
    testi_cards = "\n".join(f'''        <div class="testi-card" data-reveal>
          <div class="stars">★★★★★</div>
          <p class="quote">&ldquo;{t['quote']}&rdquo;</p>
          <div class="testi-who"><div class="ava">{t['initial']}</div><div><strong>{t['name']}</strong><span>{t['role']}</span></div></div>
        </div>''' for t in lp["testi"])

    body = f'''  <section class="hero lp-hero">
    <div class="wrap">
      <div class="hero-copy" data-reveal="left">
        <p class="eyebrow">{lp['eyebrow']}</p>
        <h1>{lp['h1']}</h1>
        <p class="lede">{lp['sub']}</p>
        <div class="hero-actions">
          <a class="btn btn-primary" href="{wa}" target="_blank" rel="noopener">{lp['cta']}</a>
        </div>
        <ul class="lp-trust">
{trust_items}
        </ul>
      </div>
      <div class="hero-media" data-reveal="right">
        <div class="frame">
          <img src="{img(lp['img'], 1000, 1150)}" alt="{lp['h1']}" width="1000" height="1150" loading="eager" fetchpriority="high">
        </div>
      </div>
    </div>
  </section>

  <section class="section on-mist">
    <div class="wrap">
      <div class="testi-track" style="grid-template-columns:repeat(2,1fr); max-width:900px; margin:0 auto;">
{testi_cards}
      </div>
    </div>
  </section>

  <section class="cta-band lp-final-cta" data-reveal>
    <div class="wrap">
      <h2>{lp['final_h2']}</h2>
      <p>{lp['final_p']}</p>
      <a class="btn btn-gold" href="{wa}" target="_blank" rel="noopener">{lp['cta']}</a>
    </div>
  </section>

  <div class="lp-sticky-bar">
    <div><strong>{lp['cta']}</strong><span>Resposta rápida no WhatsApp</span></div>
    <a class="btn btn-primary btn-sm" href="{wa}" target="_blank" rel="noopener">Chamar agora</a>
  </div>'''

    page(
        lp["slug"], lp["title"], lp["description"], "", body,
        og_image=img(lp["img"], 1200, 630),
        robots="noindex, follow",
        chrome="minimal",
    )


def build_all():
    for lp in LANDING_PAGES:
        build_lp(lp)
