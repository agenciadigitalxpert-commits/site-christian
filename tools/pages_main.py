# -*- coding: utf-8 -*-
"""Páginas principais (institucionais) do site."""
from site_engine import (
    page, img, UNITS, TREATMENTS, TESTIMONIALS, WA_DEFAULT, PHONE_DISPLAY,
    PHONE_TEL, EMAIL, breadcrumb_ld, faq_ld, faq_block, organization_ld,
    website_ld, unit_ld, BASE_URL, wa_link,
)


def testimonial_track(items, slider_id="testi-home"):
    cards = "\n".join(f'''        <div class="testi-card" data-reveal>
          <div class="stars">★★★★★</div>
          <p class="quote">&ldquo;{t['quote']}&rdquo;</p>
          <div class="testi-who"><div class="ava">{t['initial']}</div><div><strong>{t['name']}</strong><span>{t['role']}</span></div></div>
        </div>''' for t in items)
    return f'''<div class="testi-track">
{cards}
      </div>'''


def stat(value, label):
    return f'<div><strong data-count="{value}">0</strong><span>{label}</span></div>'


def build_home():
    bento_items = []
    widths = {"harmonizacao": "wide", "geral": "wide"}
    for t in TREATMENTS:
        cls = "bento-item wide" if widths.get(t["key"]) else "bento-item"
        desc = f'<p>{t["short"]}</p>' if widths.get(t["key"]) else ""
        bento_items.append(f'''      <a class="{cls}" href="{t['slug']}" data-reveal="scale">
        <span class="num">{t['num']}</span>
        <div>
          <h3>{t['name']}</h3>
          {desc}
        </div>
        <span class="go">Explorar</span>
      </a>''')
    bento = "\n".join(bento_items)

    units_cards = "\n".join(f'''        <div class="unit-card" data-reveal>
          <span class="tag">{u['region']}</span>
          <p class="addr">{u['address']}</p>
          <div class="row"><span>{u['phone_display']}</span><a class="btn btn-outline btn-sm" href="unidades.html#{u['key']}">Ver unidade</a></div>
        </div>''' for u in UNITS)

    body = f'''  <section class="hero">
    <div class="wrap">
      <div class="hero-copy" data-reveal="left">
        <p class="eyebrow">Odontologia &amp; Harmonização Orofacial desde 2005</p>
        <h1>O sorriso que você imaginou existe e começa com uma avaliação.</h1>
        <p class="lede">Implantes, ortodontia, facetas e harmonização facial com equipe multidisciplinar, tecnologia de ponta e acompanhamento humano em 5 unidades na região de Curitiba.</p>
        <div class="hero-actions">
          <a class="btn btn-primary" href="{WA_DEFAULT}" target="_blank" rel="noopener">Falar no WhatsApp</a>
          <a class="btn btn-outline" href="tratamentos.html">Ver tratamentos</a>
        </div>
        <div class="stats">
          {stat("20+", "anos de atuação")}
          {stat("5", "unidades na região")}
          {stat("30 mil+", "implantes realizados")}
        </div>
      </div>
      <div class="hero-media" data-reveal="right">
        <div class="hero-cutout">
          <div class="hero-photo">
            <img src="images/christian-andrade.webp" alt="Dr. Christian Andrade" width="998" height="1607" loading="eager" fetchpriority="high">
            <div class="hero-ribbon">Número 1 em Implantes Neodent do Brasil &middot; Garantia Vitalícia</div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section" id="tratamentos">
    <div class="wrap">
      <div class="section-head" data-reveal>
        <div>
          <p class="eyebrow">O que tratamos</p>
          <h2>Cada sorriso pede um plano diferente</h2>
        </div>
        <a class="btn btn-outline" href="tratamentos.html">Ver todos os tratamentos</a>
      </div>
      <div class="bento">
{bento}
      </div>
    </div>
  </section>

  <section class="on-ink section">
    <div class="wrap">
      <div class="section-head" data-reveal>
        <div>
          <p class="eyebrow on-dark">Por que o Instituto</p>
          <h2>Técnica de referência, do planejamento ao resultado</h2>
        </div>
      </div>
      <div class="diff-band" data-reveal-group>
        <div class="diff">
          <div class="mark">Ⅰ</div>
          <h4>Implantes Grand Morse Neodent</h4>
          <p>Sistema de referência mundial em estabilidade e biocompatibilidade.</p>
        </div>
        <div class="diff">
          <div class="mark">Ⅱ</div>
          <h4>Cirurgia sem corte</h4>
          <p>Procedimentos guiados por planejamento digital, com menos trauma.</p>
        </div>
        <div class="diff">
          <div class="mark">Ⅲ</div>
          <h4>Carga imediata</h4>
          <p>Em casos indicados, você sai da clínica com dentes provisórios no mesmo dia.</p>
        </div>
        <div class="diff">
          <div class="mark">Ⅳ</div>
          <h4>Garantia vitalícia</h4>
          <p>Tranquilidade a longo prazo para o seu investimento em saúde.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap two-col">
      <div class="frame" style="aspect-ratio:4/3.2; border-radius:var(--radius-l); overflow:hidden;" data-reveal="left">
        <img src="{img('raiox', 1000, 800)}" alt="Especialista analisando exame de imagem odontológico em close" width="1000" height="800" loading="lazy">
      </div>
      <div data-reveal="right">
        <p class="eyebrow">Equipe especializada</p>
        <h2>Técnica avançada, cuidado de verdade</h2>
        <p class="lede">Com equipamentos de alta tecnologia e protocolos personalizados, unimos estética — como lentes de contato dental e clareamento — a tratamentos de saúde como implantes e endodontia. Você é atendido por especialistas de cada área, não por um único generalista.</p>
        <a class="btn btn-primary" href="sobre.html">Conhecer a clínica</a>
      </div>
    </div>
  </section>

  <section class="section on-mist" id="depoimentos">
    <div class="wrap">
      <div class="section-head" data-reveal>
        <div>
          <p class="eyebrow">Prova social</p>
          <h2>Quem já realizou o sonho conosco</h2>
        </div>
        <a class="btn btn-outline" href="depoimentos.html">Ver todos os depoimentos</a>
      </div>
      {testimonial_track(TESTIMONIALS[:3])}
    </div>
  </section>

  <section class="section" id="unidades">
    <div class="wrap">
      <div class="section-head" data-reveal>
        <div>
          <p class="eyebrow">Onde estamos</p>
          <h2>5 unidades para ficar perto de você</h2>
        </div>
        <a class="btn btn-outline" href="unidades.html">Ver todas as unidades</a>
      </div>
      <div class="units-grid">
{units_cards}
      </div>
    </div>
  </section>

  <section class="cta-band" data-reveal>
    <div class="wrap">
      <h2>Agende sua avaliação agora mesmo</h2>
      <p>Sem compromisso. Nossa equipe entende seu caso e monta um plano de tratamento sob medida.</p>
      <a class="btn btn-gold" href="{WA_DEFAULT}" target="_blank" rel="noopener">Chamar no WhatsApp</a>
    </div>
  </section>'''

    page(
        "index.html",
        "Instituto Christian Andrade — Odontologia em Curitiba",
        "Implantes, harmonização orofacial, ortodontia e estética dental em 5 unidades em Curitiba e região. Agende sua avaliação.",
        "home", body, root="",
        json_ld_list=[website_ld(), organization_ld()],
        og_image=img("consulta", 1200, 630),
        priority="1.0", changefreq="weekly",
    )


def build_sobre():
    galeria = "\n".join(f'''        <div class="frame" style="aspect-ratio:1/1; border-radius:var(--radius-m); overflow:hidden;" data-reveal="scale">
          <img src="{src}" alt="{alt}" width="800" height="800" loading="lazy">
        </div>''' for src, alt in [
        ("images/consultorio-interno-square.webp", "Sala de atendimento do Instituto Christian Andrade"),
        (img("clinica_ampla", 800, 800), "Sala de atendimento com equipamentos de alta tecnologia"),
        (img("clinica_vista", 800, 800), "Ambiente amplo e iluminado de uma das unidades"),
    ])

    body = f'''  <section class="page-hero">
    <div class="wrap">
      <p class="breadcrumb"><a href="index.html">Home</a> / Sobre a Clínica</p>
      <p class="eyebrow">Desde 2005</p>
      <h1 data-reveal>Uma equipe que transforma sonhos em sorrisos</h1>
      <p class="lede" data-reveal>Nascemos no ramo da odontologia em 2005 e crescemos até formar uma equipe multidisciplinar capacitada para as melhores soluções em estética e implantodontia.</p>
    </div>
  </section>

  <section class="section">
    <div class="wrap two-col">
      <div data-reveal="left">
        <p class="eyebrow">Nossa história</p>
        <h2>Técnica avançada, tratamento personalizado</h2>
        <p>Com técnicas avançadas e equipamentos altamente tecnológicos, oferecemos tratamentos personalizados de acordo com a necessidade de cada paciente. Além de questões estéticas — como lentes de contato dental e clareamento — somos especialistas em tratamentos de saúde, como implantes e endodontia.</p>
        <p>Renove sua autoestima e busque o que você sempre sonhou. Ajudamos você a melhorar sua saúde bucal com tratamentos seguros e alta tecnologia, em qualquer uma das nossas 5 unidades na região de Curitiba.</p>
        <a class="btn btn-primary" href="contato.html">Marcar consulta inicial</a>
      </div>
      <div class="frame" style="aspect-ratio:4/4.8; border-radius:var(--radius-l); overflow:hidden;" data-reveal="right">
        <img src="{img('clinica_vista', 1000, 1200)}" alt="Consultório do Instituto Christian Andrade com ambiente claro e acolhedor" width="1000" height="1200" loading="lazy">
      </div>
    </div>
  </section>

  <section class="section on-mist">
    <div class="wrap">
      <div class="section-head" data-reveal>
        <div>
          <p class="eyebrow">O que nos move</p>
          <h2>Missão, visão e valores</h2>
        </div>
      </div>
      <div class="value-cols" data-reveal-group>
        <div class="card">
          <h3>Missão</h3>
          <p>Promover e executar serviços multidisciplinares no ramo da odontologia, com ética e excelência, de forma acolhedora e humana, visando o bem-estar e a qualidade de vida do paciente.</p>
        </div>
        <div class="card">
          <h3>Visão</h3>
          <p>Ser referência em implantodontia e estética, transformando sonhos em sorrisos.</p>
        </div>
        <div class="card">
          <h3>Valores</h3>
          <p>Humanização e gentileza, transparência na comunicação, sigilo ético, compromisso com o bem-estar do paciente e crescimento profissional contínuo da equipe.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="section-head" data-reveal>
        <div>
          <p class="eyebrow">Bastidores</p>
          <h2>Nossas clínicas e nossa equipe</h2>
        </div>
      </div>
      <div class="units-grid" style="grid-template-columns:repeat(3,1fr);">
{galeria}
      </div>
    </div>
  </section>

  <section class="cta-band" data-reveal>
    <div class="wrap">
      <h2>Agende sua avaliação agora mesmo</h2>
      <p>Estamos te esperando em uma das nossas 5 unidades.</p>
      <a class="btn btn-gold" href="{WA_DEFAULT}" target="_blank" rel="noopener">Chamar no WhatsApp</a>
    </div>
  </section>'''

    page(
        "sobre.html",
        "Sobre a Clínica — Instituto Christian Andrade",
        "Desde 2005 no ramo da odontologia. Conheça a história, a missão, a visão e os valores do Instituto Christian Andrade.",
        "sobre", body,
        json_ld_list=[breadcrumb_ld([("Home", ""), ("Sobre a Clínica", "sobre.html")])],
        og_image=img("clinica_vista", 1200, 630),
        priority="0.7",
    )


def build_tratamentos():
    detail = {
        "harmonizacao": {
            "items": [
                ("Bichectomia", "Remoção da bola de Bichat para afinar o contorno facial."),
                ("Fios de sustentação", "Sustentação e rejuvenescimento facial sem cirurgia."),
                ("Preenchimento facial", "Volume e simetria com ácido hialurônico, harmonizando lábios e contornos."),
            ],
        },
        "ortodontia": {
            "items": [
                ("Aparelho estético (porcelana)", "Discrição no dia a dia, com a mesma eficácia do metálico."),
                ("Aparelho invisível", "Alinhadores transparentes e removíveis para rotinas exigentes."),
                ("Aparelho metálico (tradicional)", "Custo-benefício e eficiência comprovada para todos os casos."),
            ],
        },
        "implantes": {
            "items": [
                ("Implantes dentários", "Sistema Grand Morse Neodent, com garantia vitalícia e carga imediata em casos indicados."),
                ("Cirurgia guiada", "Planejamento digital que reduz cortes e acelera a recuperação."),
            ],
        },
        "facetas": {
            "items": [
                ("Lentes de contato dental", "Lâminas ultrafinas que corrigem cor, forma e alinhamento sem desgaste do dente."),
                ("Facetas dentárias", "Reconstrução estética com resina ou porcelana, sob medida para cada sorriso."),
            ],
        },
        "geral": {
            "items": [
                ("Clareamento dental", "A gel com moldeira, ou de consultório para resultado mais rápido."),
                ("Endodontia (canal)", "Tratamento de canal com tecnologia que reduz desconforto."),
                ("Limpeza", "Profilaxia profissional para prevenção de cáries e gengivite."),
                ("Extrações", "Procedimento seguro para dentes comprometidos ou sisos."),
                ("Restaurações", "Recuperação de dentes com cárie ou fratura, com estética natural."),
            ],
        },
    }
    headings = {
        "harmonizacao": "Equilíbrio entre o sorriso e o rosto",
        "ortodontia": "Dentes alinhados, do jeito que combina com você",
        "implantes": "Recupere função e confiança",
        "facetas": "Sorrisos naturalmente perfeitos",
        "geral": "A base de uma boca saudável",
    }
    sections = []
    for i, t in enumerate(TREATMENTS):
        bg = " on-mist" if i % 2 else ""
        cards = "\n".join(f'''          <div class="treat-card" data-reveal>
            <h4>{name}</h4>
            <p>{desc}</p>
          </div>''' for name, desc in detail[t["key"]]["items"])
        sections.append(f'''  <section class="section{bg}" id="{t['key']}">
    <div class="wrap">
      <div class="section-head" data-reveal>
        <div>
          <p class="eyebrow">{t['num']} · {t['eyebrow']}</p>
          <h2>{headings[t['key']]}</h2>
        </div>
        <a class="btn btn-outline" href="{t['slug']}">Ver detalhes</a>
      </div>
      <div class="treat-grid">
{cards}
      </div>
    </div>
  </section>''')

    body = f'''  <section class="page-hero">
    <div class="wrap">
      <p class="breadcrumb"><a href="index.html">Home</a> / Tratamentos</p>
      <p class="eyebrow">Nossos tratamentos</p>
      <h1 data-reveal>Um plano de tratamento para cada objetivo</h1>
      <p class="lede" data-reveal>Da estética à saúde bucal, cada área é conduzida por especialistas dedicados — com tecnologia e protocolos próprios para cada caso.</p>
    </div>
  </section>

{chr(10).join(sections)}

  <section class="cta-band" data-reveal>
    <div class="wrap">
      <h2>Não sabe por onde começar?</h2>
      <p>Marque uma avaliação e nossa equipe indica o melhor caminho para o seu caso.</p>
      <a class="btn btn-gold" href="{WA_DEFAULT}" target="_blank" rel="noopener">Chamar no WhatsApp</a>
    </div>
  </section>'''

    page(
        "tratamentos.html",
        "Tratamentos — Instituto Christian Andrade",
        "Harmonização orofacial, ortodontia, implantes, facetas e odontologia geral. Conheça todos os tratamentos do Instituto Christian Andrade.",
        "tratamentos", body,
        json_ld_list=[breadcrumb_ld([("Home", ""), ("Tratamentos", "tratamentos.html")])],
        og_image=img("clinica_ampla", 1200, 630),
        priority="0.9", changefreq="weekly",
    )


def treatment_detail_page(t, hero_lede, intro_eyebrow, intro_title, intro_text, sub_items,
                            steps, faqs, hero_img_key, description, wa_extra=""):
    subs = "\n".join(f'''          <div class="treat-card">
            <h4>{name}</h4>
            <p>{desc}</p>
          </div>''' for name, desc in sub_items)
    steps_html = "\n".join(f'''        <div class="step" data-reveal><div class="n">{i+1:02d}</div><div><h3>{title}</h3><p>{desc}</p></div></div>'''
                            for i, (title, desc) in enumerate(steps))
    faq_html = faq_block(faqs)
    wa_msg = wa_link(f"Olá, quero agendar uma avaliação de {t['name'].lower()}." if not wa_extra else wa_extra)

    body = f'''  <section class="page-hero">
    <div class="wrap">
      <p class="breadcrumb"><a href="index.html">Home</a> / <a href="tratamentos.html">Tratamentos</a> / {t['name']}</p>
      <p class="eyebrow">{t['eyebrow']}</p>
      <h1 data-reveal>{hero_lede[0]}</h1>
      <p class="lede" data-reveal>{hero_lede[1]}</p>
    </div>
  </section>

  <section class="section">
    <div class="wrap two-col">
      <div class="frame" style="aspect-ratio:4/4.4; border-radius:var(--radius-l); overflow:hidden;" data-reveal="left">
        <img src="{img(hero_img_key, 1000, 1100)}" alt="{intro_title}" width="1000" height="1100" loading="lazy">
      </div>
      <div data-reveal="right">
        <p class="eyebrow">{intro_eyebrow}</p>
        <h2>{intro_title}</h2>
        <p>{intro_text}</p>
        <div class="treat-grid" style="grid-template-columns:1fr; margin-top:1.5em;">
{subs}
        </div>
      </div>
    </div>
  </section>

  <section class="section on-mist">
    <div class="wrap">
      <p class="eyebrow">Como funciona</p>
      <h2>Da avaliação ao resultado</h2>
      <div class="steps">
{steps_html}
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <p class="eyebrow">Dúvidas frequentes</p>
      <h2>Perguntas sobre {t['name'].lower()}</h2>
      <div class="faq" style="margin-top:1.5em;">{faq_html}</div>
    </div>
  </section>

  <section class="cta-band" data-reveal>
    <div class="wrap">
      <h2>Vamos avaliar o seu caso?</h2>
      <p>Marque uma avaliação e receba um plano personalizado.</p>
      <a class="btn btn-gold" href="{wa_msg}" target="_blank" rel="noopener">Chamar no WhatsApp</a>
    </div>
  </section>'''

    page(
        t["slug"],
        f"{t['name']} — Instituto Christian Andrade",
        description,
        "tratamentos", body,
        json_ld_list=[
            breadcrumb_ld([("Home", ""), ("Tratamentos", "tratamentos.html"), (t["name"], t["slug"])]),
            faq_ld(faqs),
        ],
        og_image=img(hero_img_key, 1200, 630),
        priority="0.8",
    )


def build_treatment_pages():
    t = {x["key"]: x for x in TREATMENTS}

    treatment_detail_page(
        t["harmonizacao"],
        ("Equilíbrio entre boca e rosto, com resultado natural",
         "Procedimentos minimamente invasivos que valorizam suas características — sem exageros, com acompanhamento odontológico especializado."),
        "O que é", "Três procedimentos, um objetivo",
        "A harmonização orofacial reúne técnicas que atuam em conjunto com a saúde bucal para melhorar a proporção entre lábios, bochechas e contorno facial. No Instituto Christian Andrade, ela é conduzida por profissionais habilitados, com planejamento individual para cada rosto.",
        [
            ("Bichectomia", "Remoção parcial da bola de Bichat para afinar o contorno do rosto de forma definitiva."),
            ("Fios de sustentação", "Fios bioabsorvíveis que estimulam colágeno e sustentam a pele sem cirurgia."),
            ("Preenchimento facial", "Ácido hialurônico para devolver volume aos lábios, maçãs do rosto e queixo."),
        ],
        [
            ("Avaliação facial", "Analisamos proporções, expressões e histórico de saúde para indicar o procedimento certo."),
            ("Plano personalizado", "Definimos técnica, quantidade de sessões e expectativa de resultado com você."),
            ("Procedimento", "Realizado em consultório, com anestesia local e curto tempo de recuperação."),
            ("Acompanhamento", "Retornos programados para acompanhar a evolução e manter o resultado."),
        ],
        [
            ("O resultado é permanente?", "A bichectomia tem efeito definitivo; fios e preenchimentos têm duração média de 12 a 18 meses, variando conforme metabolismo e técnica."),
            ("Dói fazer o procedimento?", "Os procedimentos são realizados com anestesia local, garantindo conforto durante a aplicação."),
            ("Quem pode fazer harmonização orofacial?", "A indicação é avaliada individualmente. Por isso o primeiro passo é sempre uma consulta de avaliação com nossa equipe."),
        ],
        "clinica_vista",
        "Bichectomia, fios de sustentação e preenchimento facial. Conheça a harmonização orofacial do Instituto Christian Andrade.",
    )

    treatment_detail_page(
        t["ortodontia"],
        ("Dentes alinhados, do jeito que combina com a sua rotina",
         "Estético, invisível ou metálico: cada aparelho tem uma indicação técnica — e nossa equipe ajuda você a escolher o caminho certo."),
        "O que é", "Um aparelho para cada estilo de vida",
        "A ortodontia corrige o posicionamento dos dentes e a mordida, prevenindo desgastes, dores na articulação e dificuldades de higienização. No Instituto Christian Andrade, o tratamento começa por uma avaliação completa — moldagem, fotos e, quando necessário, exames de imagem — para indicar o aparelho mais adequado ao seu caso.",
        [
            ("Aparelho estético (porcelana)", "Bráquetes na cor do dente, discretos no dia a dia, com a mesma eficácia do metálico."),
            ("Aparelho invisível", "Alinhadores transparentes e removíveis, ideais para rotinas profissionais exigentes."),
            ("Aparelho metálico (tradicional)", "Ótimo custo-benefício e eficiência comprovada para praticamente todos os casos."),
        ],
        [
            ("Avaliação ortodôntica", "Moldagem ou escaneamento digital, fotos e análise da mordida para definir o diagnóstico."),
            ("Plano de tratamento", "Apresentamos o tipo de aparelho indicado, o tempo estimado e o investimento."),
            ("Instalação do aparelho", "Colagem dos bráquetes ou entrega do primeiro conjunto de alinhadores."),
            ("Manutenções periódicas", "Ajustes mensais (ou troca de alinhadores) até atingir o alinhamento planejado."),
        ],
        [
            ("Quanto tempo dura o tratamento ortodôntico?", "Varia conforme a complexidade do caso — em média entre 18 e 36 meses, com manutenções periódicas."),
            ("Dói colocar o aparelho?", "É comum sentir um leve desconforto nos primeiros dias após a instalação ou troca dos alinhadores, que passa rapidamente."),
            ("Posso escolher o tipo de aparelho?", "A indicação técnica considera sua mordida e objetivo, mas sua preferência estética e de rotina é sempre levada em conta na avaliação."),
        ],
        "alinhador",
        "Aparelho estético, invisível ou metálico. Conheça a ortodontia do Instituto Christian Andrade em Curitiba e região.",
    )

    treatment_detail_page(
        t["implantes"],
        ("Recupere função e confiança para sorrir sem limites",
         "Sistema Grand Morse Neodent, cirurgia guiada por planejamento digital e garantia vitalícia para o seu investimento em saúde."),
        "O que é", "Tecnologia e segurança em cada etapa",
        "O implante dentário substitui a raiz do dente perdido, devolvendo função de mastigação e estética. Utilizamos o sistema Grand Morse Neodent, referência mundial em estabilidade e biocompatibilidade, com planejamento guiado por exame de imagem que reduz cortes e acelera a recuperação.",
        [
            ("Implantes dentários", "Sistema Grand Morse Neodent, com garantia vitalícia e carga imediata em casos indicados."),
            ("Cirurgia guiada", "Planejamento 100% digital que reduz cortes, sangramento e tempo de recuperação."),
        ],
        [
            ("Avaliação com exame de imagem", "Tomografia e análise da estrutura óssea para planejar o posicionamento ideal do implante."),
            ("Planejamento digital guiado", "Criação de um guia cirúrgico personalizado, com previsibilidade no resultado."),
            ("Cirurgia de implante", "Instalação do implante com técnica minimamente invasiva, muitas vezes sem cortes."),
            ("Prótese e acompanhamento", "Instalação da coroa protética e retornos para garantir a saúde do implante a longo prazo."),
        ],
        [
            ("Implante dentário dói?", "O procedimento é feito com anestesia local; o desconforto no pós-operatório costuma ser leve e controlado com medicação prescrita."),
            ("Quanto tempo dura um implante?", "Com os cuidados adequados e acompanhamento periódico, o implante Grand Morse Neodent tem garantia vitalícia."),
            ("Preciso ficar sem dente durante o tratamento?", "Em casos indicados, oferecemos carga imediata: você sai da clínica com dentes provisórios no mesmo dia."),
        ],
        "raiox",
        "Implantes dentários Grand Morse Neodent com garantia vitalícia e cirurgia guiada. Conheça no Instituto Christian Andrade.",
    )

    treatment_detail_page(
        t["facetas"],
        ("Sorrisos naturalmente perfeitos, sob medida",
         "Lentes de contato dental e facetas que corrigem cor, forma e alinhamento — com resultado que parece (e é) seu."),
        "O que é", "Lâminas ultrafinas, resultado natural",
        "Lentes de contato dental e facetas são lâminas cimentadas sobre os dentes para corrigir cor, forma, tamanho e pequenos desalinhamentos. No Instituto Christian Andrade, o planejamento do sorriso é feito antes da confecção, para que o resultado combine com as proporções do seu rosto.",
        [
            ("Lentes de contato dental", "Lâminas ultrafinas de porcelana que, na maioria dos casos, não exigem desgaste do dente."),
            ("Facetas dentárias", "Reconstrução estética com resina ou porcelana, indicada para correções mais específicas."),
        ],
        [
            ("Avaliação e planejamento do sorriso", "Fotos, moldagem e simulação digital do resultado antes de iniciar o tratamento."),
            ("Preparo do dente", "Na maioria dos casos de lentes, feito com desgaste mínimo ou nenhum desgaste."),
            ("Confecção em laboratório", "As peças são confeccionadas sob medida, seguindo cor e formato planejados."),
            ("Cimentação e ajustes finais", "Fixação das lentes ou facetas com ajuste de oclusão e polimento final."),
        ],
        [
            ("Lentes de contato dental desgastam o dente?", "Na maioria dos casos não é necessário nenhum desgaste, ou apenas um preparo mínimo — isso é avaliado caso a caso."),
            ("Quanto tempo duram as lentes ou facetas?", "Com bons hábitos de higiene e acompanhamento, a durabilidade costuma ultrapassar 10 anos."),
            ("Qual a diferença entre lente de contato e faceta?", "As lentes são mais finas e geralmente dispensam desgaste do dente; as facetas permitem correções mais amplas de forma e alinhamento."),
        ],
        "clinica_vermelha",
        "Lentes de contato dental e facetas dentárias. Conheça a estética dental do Instituto Christian Andrade.",
    )

    treatment_detail_page(
        t["geral"],
        ("A base de uma boca saudável, em um só lugar",
         "Clareamento, canal, limpeza, extrações e restaurações — cuidado completo com quem entende de cada especialidade."),
        "O que é", "Saúde bucal do jeito certo",
        "A odontologia geral reúne os cuidados essenciais para manter dentes e gengivas saudáveis: prevenção, tratamento de canal com microscopia, periodontia, restaurações e procedimentos cirúrgicos simples. É também a partir dela que identificamos a necessidade de tratamentos mais específicos, como implantes ou ortodontia.",
        [
            ("Clareamento dental", "A gel com moldeira personalizada, ou de consultório para resultado mais rápido."),
            ("Endodontia (canal) com microscopia", "Tratamento de canal com microscópio odontológico, que aumenta a precisão e reduz o desconforto durante e após o procedimento."),
            ("Periodontia", "Tratamento das gengivas e das estruturas de suporte do dente, prevenindo e tratando a doença periodontal."),
            ("Limpeza (profilaxia)", "Remoção de placa e tártaro para prevenção de cáries e doenças gengivais."),
            ("Extrações", "Procedimento seguro para dentes comprometidos, inclusive extração de sisos."),
            ("Restaurações", "Recuperação de dentes com cárie ou fratura, com resultado estético natural."),
        ],
        [
            ("Avaliação geral", "Exame clínico completo e, quando necessário, radiografias para diagnóstico preciso."),
            ("Diagnóstico e plano", "Definição do tratamento prioritário e do plano preventivo de manutenção."),
            ("Procedimento", "Execução do tratamento indicado, sempre com foco em conforto e segurança."),
            ("Retorno preventivo", "Consultas de manutenção para preservar o resultado e a saúde bucal."),
        ],
        [
            ("Com que frequência devo fazer limpeza dental?", "Em geral, a cada 6 meses — mas a frequência ideal é definida conforme sua condição bucal na avaliação."),
            ("Tratamento de canal dói?", "Com anestesia e as técnicas atuais, o desconforto é bastante reduzido durante e após o procedimento."),
            ("Clareamento dental estraga o dente?", "Quando feito com acompanhamento profissional e produtos adequados, o clareamento é seguro para o esmalte."),
        ],
        "clinica_ampla",
        "Clareamento, endodontia com microscopia, periodontia, limpeza, extrações e restaurações. Conheça a odontologia geral do Instituto Christian Andrade.",
    )


def build_unidades():
    sections = []
    for i, u in enumerate(UNITS):
        bg = " on-mist" if i % 2 else ""
        img_first = i % 2 == 0
        doc_line = f'<p class="doc">Responsável técnico(a): {u["doctor"]} — {u["cro"]}</p>' if u.get("doctor") else ""
        img_block = f'''<div class="frame" style="aspect-ratio:4/3.2; border-radius:var(--radius-l); overflow:hidden;" data-reveal="left">
        <img src="{u['img']}" alt="Ambiente da {u['name']}" width="1000" height="800" loading="lazy">
      </div>'''
        text_block = f'''<div data-reveal="right">
        <span class="tag" style="background:var(--gold-pale); color:var(--gold-deep); padding:.4em .9em; border-radius:20px; font-size:.74rem; font-weight:700; text-transform:uppercase;">Unidade {u['num']}</span>
        <h2 style="margin-top:.7em;">{u['name']}</h2>
        <p class="addr">{u['address']}</p>
        <p>{u['phone_display']}</p>
        {doc_line}
        <a class="btn btn-primary" href="{wa_link(f"Olá, quero agendar uma avaliação na unidade {u['name']}.", u.get('whatsapp'))}" target="_blank" rel="noopener">Agendar nesta unidade</a>
      </div>'''
        if img_first:
            inner = img_block + "\n      " + text_block
        else:
            inner = text_block + "\n      " + img_block
        sections.append(f'''  <section class="section{bg}" id="{u['key']}">
    <div class="wrap two-col">
      {inner}
    </div>
  </section>''')

    unit_ld_list = [breadcrumb_ld([("Home", ""), ("Unidades", "unidades.html")])]
    unit_ld_list.append({"@context": "https://schema.org", "@graph": [unit_ld(u) for u in UNITS]})

    body = f'''  <section class="page-hero">
    <div class="wrap">
      <p class="breadcrumb"><a href="index.html">Home</a> / Unidades</p>
      <p class="eyebrow">Onde estamos</p>
      <h1 data-reveal>5 unidades para ficar perto de você</h1>
      <p class="lede" data-reveal>Cada unidade conta com responsável técnico habilitado e a mesma estrutura de qualidade do Instituto Christian Andrade.</p>
    </div>
  </section>

{chr(10).join(sections)}

  <section class="cta-band" data-reveal>
    <div class="wrap">
      <h2>Fale com a unidade mais próxima</h2>
      <p>Toda a equipe está pronta para te atender.</p>
      <a class="btn btn-gold" href="{WA_DEFAULT}" target="_blank" rel="noopener">Chamar no WhatsApp</a>
    </div>
  </section>'''

    page(
        "unidades.html",
        "Unidades — Instituto Christian Andrade",
        "Batel, Sítio Cercado, Pinhais e São José dos Pinhais. Encontre a unidade do Instituto Christian Andrade mais perto de você.",
        "unidades", body,
        json_ld_list=unit_ld_list,
        og_image=img("clinica_azul", 1200, 630),
        priority="0.9",
    )


def build_depoimentos():
    body = f'''  <section class="page-hero">
    <div class="wrap">
      <p class="breadcrumb"><a href="index.html">Home</a> / Depoimentos</p>
      <p class="eyebrow">Sorria com confiança</p>
      <h1 data-reveal>Quem já realizou o sonho conosco</h1>
      <p class="lede" data-reveal>Histórias reais de pacientes que recuperaram autoestima, função e saúde bucal no Instituto Christian Andrade.</p>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      {testimonial_track(TESTIMONIALS, "testi-all")}
    </div>
  </section>

  <section class="cta-band" data-reveal>
    <div class="wrap">
      <h2>Seja o próximo sorriso transformado</h2>
      <p>Marque sua avaliação e conte sua história com a gente.</p>
      <a class="btn btn-gold" href="{WA_DEFAULT}" target="_blank" rel="noopener">Chamar no WhatsApp</a>
    </div>
  </section>'''

    page(
        "depoimentos.html",
        "Depoimentos — Instituto Christian Andrade",
        "Veja quem já realizou o sonho do sorriso ideal com o Instituto Christian Andrade.",
        "depoimentos", body,
        json_ld_list=[breadcrumb_ld([("Home", ""), ("Depoimentos", "depoimentos.html")])],
        og_image=img("consulta", 1200, 630),
        priority="0.6",
    )


def build_contato():
    body = f'''  <section class="page-hero">
    <div class="wrap">
      <p class="breadcrumb"><a href="index.html">Home</a> / Contato</p>
      <p class="eyebrow">Fale conosco</p>
      <h1 data-reveal>Vamos agendar sua avaliação</h1>
      <p class="lede" data-reveal>Prefere WhatsApp, telefone ou formulário — escolha o canal mais fácil para você. Respondemos rápido.</p>
    </div>
  </section>

  <section class="section">
    <div class="wrap two-col" style="align-items:flex-start;">
      <div data-reveal="left">
        <h2>Envie seus dados</h2>
        <p style="margin-bottom:1.6em;">Preencha o formulário e continuamos a conversa no WhatsApp.</p>
        <form id="form-contato" novalidate>
          <div class="form-grid">
            <div class="field full">
              <label for="nome">Nome completo</label>
              <input type="text" id="nome" name="nome" placeholder="Seu nome" required>
            </div>
            <div class="field">
              <label for="telefone">Telefone / WhatsApp</label>
              <input type="tel" id="telefone" name="telefone" placeholder="(41) 90000-0000" required>
            </div>
            <div class="field">
              <label for="unidade">Unidade de preferência</label>
              <select id="unidade" name="unidade">
                <option value="">Sem preferência</option>
                <option value="Batel">Batel</option>
                <option value="Sítio Cercado">Sítio Cercado</option>
                <option value="Pinhais">Pinhais</option>
                <option value="São José dos Pinhais">São José dos Pinhais</option>
              </select>
            </div>
            <div class="field full">
              <label for="mensagem">O que você gostaria de tratar?</label>
              <textarea id="mensagem" name="mensagem" rows="4" placeholder="Ex: implantes, harmonização, ortodontia..."></textarea>
            </div>
          </div>
          <p class="form-status" style="min-height:1.4em; font-size:.85rem; margin-top:.8em;"></p>
          <button class="btn btn-primary btn-block" type="submit" style="margin-top:.4em;">Enviar e continuar no WhatsApp</button>
        </form>
      </div>

      <div data-reveal="right">
        <h2>Outros canais</h2>
        <div class="units-grid" style="grid-template-columns:1fr; margin-top:1.4em;">
          <div class="unit-card">
            <span class="tag">WhatsApp</span>
            <p class="addr">Atendimento rápido para agendamentos e dúvidas.</p>
            <a class="btn btn-outline btn-sm" style="width:fit-content;" href="{WA_DEFAULT}" target="_blank" rel="noopener">Chamar agora</a>
          </div>
          <div class="unit-card">
            <span class="tag">Telefone</span>
            <p class="addr">{PHONE_DISPLAY} — unidade Batel</p>
            <p class="addr">(41) 3030-3010 — unidade São José dos Pinhais</p>
          </div>
          <div class="unit-card">
            <span class="tag">E-mail</span>
            <p class="addr">{EMAIL}</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section on-mist">
    <div class="wrap">
      <p class="eyebrow">Sede — Batel</p>
      <h2>Av. Silva Jardim, 2520, Curitiba/PR</h2>
      <div class="map-block" style="margin-top:1.6em;" data-reveal="scale">
        <iframe src="https://www.google.com/maps?q=Av.+Silva+Jardim,+2520,+Batel,+Curitiba,+PR&output=embed" title="Mapa Clínica Batel" loading="lazy"></iframe>
      </div>
    </div>
  </section>'''

    page(
        "contato.html",
        "Contato — Instituto Christian Andrade",
        "Agende sua avaliação no Instituto Christian Andrade. WhatsApp, telefone e formulário de contato.",
        "contato", body,
        json_ld_list=[breadcrumb_ld([("Home", ""), ("Contato", "contato.html")])],
        og_image=img("clinica_azul", 1200, 630),
        priority="0.8",
    )


def build_404():
    body = f'''  <section class="error-page">
    <div class="wrap">
      <div class="code">404</div>
      <h1 style="margin-top:.2em;">Essa página não foi encontrada</h1>
      <p class="lede" style="margin:1em auto 2em;">O endereço pode ter mudado. Volte para a home ou fale com a gente pelo WhatsApp.</p>
      <div class="hero-actions" style="justify-content:center;">
        <a class="btn btn-primary" href="index.html">Voltar para a Home</a>
        <a class="btn btn-outline" href="{WA_DEFAULT}" target="_blank" rel="noopener">Falar no WhatsApp</a>
      </div>
    </div>
  </section>'''
    page(
        "404.html",
        "Página não encontrada — Instituto Christian Andrade",
        "A página que você procura não foi encontrada. Volte para a home do Instituto Christian Andrade.",
        "", body, robots="noindex, follow", priority="0.1", changefreq="yearly",
    )


def build_all():
    build_home()
    build_sobre()
    build_tratamentos()
    build_treatment_pages()
    build_unidades()
    build_depoimentos()
    build_contato()
    build_404()
