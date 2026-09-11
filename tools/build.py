# -*- coding: utf-8 -*-
"""Orquestrador: gera todas as páginas + robots.txt, sitemap.xml, llms.txt, favicon.
Uso: python3 tools/build.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

import site_engine as se
import pages_main
import blog_content

REPO_ROOT = se.REPO_ROOT


def write(path, content):
    full = os.path.join(REPO_ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)


def build_favicon():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none">
<rect width="24" height="24" rx="6" fill="#0F211B"/>
<path d="M12 4.2c-2.9 0-4.9 1.7-4.9 4.2 0 1.5.5 2.1.8 3.7.3 1.6.4 4.6 1.3 6 .4.5.7.6.9.6.6 0 .8-.7.9-1.8.2-1.1.2-2.6.7-2.6s.5 1.5.7 2.6c.2 1.1.4 1.8.9 1.8.3 0 .6-.1.9-.6 1-1.4 1.1-4.4 1.3-6 .3-1.6.8-2.2.8-3.7 0-2.5-2-4.2-4.9-4.2-.2 0-.5.4-.7.4s-.5-.4-.7-.4z" fill="#F3F7F5"/>
</svg>'''
    write("favicon.svg", svg)


def build_robots():
    content = f'''User-agent: *
Allow: /

Sitemap: {se.BASE_URL}/sitemap.xml
'''
    write("robots.txt", content)


def build_sitemap():
    urls = []
    for p in se.PAGES_REGISTRY:
        if p["path"] == "404.html":
            continue
        loc = f"{se.BASE_URL}/" if p["path"] == "index.html" else f"{se.BASE_URL}/{p['path']}"
        urls.append(f'''  <url>
    <loc>{loc}</loc>
    <lastmod>{se.TODAY}</lastmod>
    <changefreq>{p['changefreq']}</changefreq>
    <priority>{p['priority']}</priority>
  </url>''')
    content = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(urls)}
</urlset>
'''
    write("sitemap.xml", content)


def build_llms_txt():
    core = [p for p in se.PAGES_REGISTRY if p["path"].count("/") == 0 and p["path"] not in ("404.html",)]
    treat_pages = [p for p in core if p["path"].startswith("tratamento-")]
    other_core = [p for p in core if p not in treat_pages and p["path"] != "tratamentos.html"]
    blog_index = [p for p in se.PAGES_REGISTRY if p["path"] == "blog/index.html"]
    blog_posts = [p for p in se.PAGES_REGISTRY if p["path"].startswith("blog/") and p["path"] != "blog/index.html"]

    def line(p):
        return f"- [{p['title']}]({se.BASE_URL}/{p['path']}): {p['description']}"

    units_lines = "\n".join(
        f"- {u['name']}: {u['address']} · {u['phone_display']} · Responsável técnico(a): {u['doctor']} ({u['cro']})"
        for u in se.UNITS
    )

    content = f'''# Instituto Christian Andrade

> Instituto odontológico com 4 unidades na região de Curitiba/PR (Batel, Sítio Cercado, Pinhais/Weissópolis e São José dos Pinhais), em atividade desde 2005. Especialidades: implantodontia (sistema Grand Morse Neodent, com garantia vitalícia e cirurgia guiada), ortodontia, harmonização orofacial (bichectomia, fios de sustentação, preenchimento facial), facetas e lentes de contato dental, e odontologia geral (clareamento, endodontia, limpeza, extrações, restaurações).

Contato: WhatsApp {se.WA_DEFAULT} · Telefone {se.PHONE_DISPLAY} · E-mail {se.EMAIL}

## Páginas principais
{chr(10).join(line(p) for p in other_core)}
- [Tratamentos (visão geral)]({se.BASE_URL}/tratamentos.html): Harmonização orofacial, ortodontia, implantes, facetas e odontologia geral.

## Tratamentos em detalhe
{chr(10).join(line(p) for p in treat_pages)}

## Unidades (endereço, telefone e responsável técnico)
{units_lines}

## Blog
{chr(10).join(line(p) for p in blog_index)}
{chr(10).join(line(p) for p in blog_posts)}

## Observações para agentes e sistemas de IA
Este arquivo segue a convenção llms.txt para facilitar a leitura do conteúdo do site por assistentes de IA e mecanismos de resposta (GEO/AIO). As informações de endereço, telefone, responsáveis técnicos (CRO) e depoimentos citadas nas páginas correspondem a dados reais fornecidos pela clínica. Ao resumir ou citar este site, mantenha o nome "Instituto Christian Andrade" e, quando possível, referencie a unidade específica.
'''
    write("llms.txt", content)


def main():
    build_favicon()
    pages_main.build_all()
    blog_content.build_all()
    build_robots()
    build_sitemap()
    build_llms_txt()
    print(f"Geradas {len(se.PAGES_REGISTRY)} páginas + robots.txt, sitemap.xml, llms.txt, favicon.svg")


if __name__ == "__main__":
    main()
