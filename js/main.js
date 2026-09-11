// Instituto Christian Andrade — interações do site

/* =========================================================================
   RASTREAMENTO AVANÇADO (dataLayer)
   Funciona independente do GTM estar instalado: os eventos ficam na fila do
   dataLayer e são lidos assim que o container do GTM carregar (ver
   tools/site_engine.py -> GTM_CONTAINER_ID). Ao configurar o GA4 dentro do
   GTM, mapeie principalmente o evento "generate_lead" (recomendado pelo
   Google para geração de leads) como conversão — ele dispara em todo clique
   de WhatsApp, telefone ou envio de formulário, com "lead_type" indicando o
   canal e "link_location" indicando de que região da página veio o clique.
   ========================================================================= */
window.dataLayer = window.dataLayer || [];

function track(eventName, params) {
  window.dataLayer.push(Object.assign({ event: eventName }, params || {}));
}

// ---- UTM / clique de anúncio: captura na 1ª página e mantém na sessão ----
const UTM_KEYS = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content', 'gclid', 'fbclid'];

function getStoredUTM() {
  try { return JSON.parse(sessionStorage.getItem('ica_utm') || '{}'); } catch (e) { return {}; }
}

(function captureUTM() {
  const params = new URLSearchParams(window.location.search);
  const stored = getStoredUTM();
  let found = false;
  UTM_KEYS.forEach((k) => {
    const v = params.get(k);
    if (v) { stored[k] = v; found = true; }
  });
  if (found) {
    try { sessionStorage.setItem('ica_utm', JSON.stringify(stored)); } catch (e) { /* modo privado etc. */ }
  }
})();

function utmSuffixForMessage() {
  const utm = getStoredUTM();
  if (!utm.utm_source && !utm.utm_campaign && !utm.gclid && !utm.fbclid) return '';
  const bits = [];
  if (utm.utm_source) bits.push('origem: ' + utm.utm_source);
  if (utm.utm_campaign) bits.push('campanha: ' + utm.utm_campaign);
  return bits.length ? ' [' + bits.join(', ') + ']' : '';
}

// injeta a origem da campanha na mensagem do WhatsApp, para a equipe ver de
// onde veio o contato direto na conversa (sem depender do GTM/GA4 pra isso)
function appendUtmToWhatsAppHref(a) {
  try {
    const url = new URL(a.href);
    const text = url.searchParams.get('text') || '';
    const suffix = utmSuffixForMessage();
    if (suffix && text.indexOf('[origem:') === -1) {
      url.searchParams.set('text', text + suffix);
      a.href = url.toString();
    }
  } catch (e) { /* URL malformada, ignora */ }
}

function throttle(fn, wait) {
  let last = 0;
  return function throttled(...args) {
    const now = Date.now();
    if (now - last >= wait) { last = now; fn.apply(this, args); }
  };
}

// classifica de qual região da página um clique partiu, sem precisar marcar
// manualmente cada botão nos templates
function trackLocation(el) {
  const map = [
    ['.lp-hero', 'lp_hero'],
    ['.lp-sticky-bar', 'lp_sticky_bar'],
    ['.lp-final-cta', 'lp_final_cta'],
    ['.hero', 'hero'],
    ['.cta-band', 'cta_band'],
    ['.cta-inline', 'article_inline'],
    ['.article-hero', 'article_hero'],
    ['.post-feat', 'blog_featured'],
    ['.post-card', 'blog_card'],
    ['.site-header', 'header'],
    ['.site-footer', 'footer'],
    ['.wa-float', 'floating_button'],
    ['.unit-card', 'unit_card'],
    ['.bento-item', 'treatment_bento'],
    ['.treat-card', 'treatment_card'],
    ['.page-hero', 'page_hero'],
    ['.testi-card', 'testimonial'],
  ];
  for (const [selector, label] of map) {
    if (el.closest(selector)) return label;
  }
  return 'content';
}

document.addEventListener('DOMContentLoaded', () => {

  /* ---------- menu mobile ---------- */
  const toggle = document.querySelector('.nav-toggle');
  const nav = document.querySelector('.main-nav');
  const scrim = document.querySelector('.nav-scrim');
  const closeNav = () => {
    nav && nav.classList.remove('open');
    toggle && toggle.setAttribute('aria-expanded', 'false');
    scrim && scrim.classList.remove('show');
    document.body.style.overflow = '';
  };
  if (toggle && nav) {
    toggle.addEventListener('click', () => {
      const open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      scrim && scrim.classList.toggle('show', open);
      document.body.style.overflow = open ? 'hidden' : '';
    });
    nav.querySelectorAll('a').forEach(link => link.addEventListener('click', closeNav));
    scrim && scrim.addEventListener('click', closeNav);
  }

  /* ---------- link ativo do menu ---------- */
  const path = (window.location.pathname.split('/').pop() || 'index.html');
  document.querySelectorAll('.main-nav a[href]').forEach(link => {
    const href = link.getAttribute('href').split('/').pop();
    if (href === path) link.classList.add('active');
  });

  /* ---------- header: encolher ao rolar ---------- */
  const header = document.querySelector('.site-header');
  const backToTop = document.querySelector('.back-to-top');
  let lastY = window.scrollY;
  const onScroll = () => {
    const y = window.scrollY;
    if (header) header.classList.toggle('is-scrolled', y > 12);
    if (backToTop) backToTop.classList.toggle('show', y > 700);
    lastY = y;
  };
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });
  backToTop && backToTop.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));

  /* ---------- animações de entrada (scroll reveal) ---------- */
  const revealTargets = document.querySelectorAll('[data-reveal], [data-reveal-group]');
  if ('IntersectionObserver' in window && revealTargets.length) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.15, rootMargin: '0px 0px -8% 0px' });
    revealTargets.forEach(el => io.observe(el));
  } else {
    revealTargets.forEach(el => el.classList.add('is-visible'));
  }

  /* ---------- contadores animados (stats) ---------- */
  const counters = document.querySelectorAll('[data-count]');
  if ('IntersectionObserver' in window && counters.length) {
    const animateCount = (el) => {
      const raw = el.getAttribute('data-count');
      const match = raw.match(/^(\D*)(\d+)(\D*)$/);
      if (!match) { el.textContent = raw; return; }
      const [, prefix, numStr, suffix] = match;
      const target = parseInt(numStr, 10);
      const duration = 1400;
      const start = performance.now();
      const step = (now) => {
        const p = Math.min((now - start) / duration, 1);
        const eased = 1 - Math.pow(1 - p, 3);
        el.textContent = prefix + Math.round(target * eased) + suffix;
        if (p < 1) requestAnimationFrame(step);
      };
      requestAnimationFrame(step);
    };
    const ioCount = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          animateCount(entry.target);
          ioCount.unobserve(entry.target);
        }
      });
    }, { threshold: 0.6 });
    counters.forEach(el => ioCount.observe(el));
  }

  /* ---------- FAQ: mantém só um aberto por vez ---------- */
  document.querySelectorAll('.faq details').forEach(d => {
    d.addEventListener('toggle', () => {
      if (d.open) {
        document.querySelectorAll('.faq details').forEach(other => {
          if (other !== d) other.open = false;
        });
        const q = d.querySelector('summary');
        track('faq_open', { question: q ? q.textContent.replace('+', '').replace('–', '').trim() : '' });
      }
    });
  });

  /* ---------- carrossel de depoimentos (arraste/scroll) ---------- */
  document.querySelectorAll('.testi-slider').forEach(slider => {
    const trackEl = slider.querySelector('.testi-track');
    const prev = slider.querySelector('.testi-prev');
    const next = slider.querySelector('.testi-next');
    if (!trackEl) return;
    const scrollByCard = (dir) => {
      const card = trackEl.querySelector('.testi-card');
      const gap = parseFloat(getComputedStyle(trackEl).gap || 24);
      const amount = card ? (card.offsetWidth + gap) * dir : 320 * dir;
      trackEl.scrollBy({ left: amount, behavior: 'smooth' });
    };
    prev && prev.addEventListener('click', () => scrollByCard(-1));
    next && next.addEventListener('click', () => scrollByCard(1));
  });

  /* ---------- formulário de contato -> WhatsApp ---------- */
  const form = document.querySelector('#form-contato');
  if (form) {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const status = form.querySelector('.form-status');
      const nome = form.nome.value.trim();
      const telefone = form.telefone.value.trim();
      if (!nome || !telefone) {
        status.textContent = 'Preencha nome e telefone para enviarmos seu contato.';
        status.style.color = '#B25A38';
        return;
      }
      const unidade = form.unidade ? form.unidade.value : '';
      const mensagemCampo = form.mensagem ? form.mensagem.value.trim() : '';
      let msg = `Olá, Instituto Christian Andrade! Meu nome é ${nome}.`;
      if (unidade) msg += ` Gostaria de agendar uma avaliação na unidade ${unidade}.`;
      else msg += ' Gostaria de agendar uma avaliação.';
      if (mensagemCampo) msg += ` Assunto: ${mensagemCampo}`;
      msg += utmSuffixForMessage();
      track('form_submit', { form_name: 'contato', unit: unidade || 'sem_preferencia' });
      track('generate_lead', { lead_type: 'form', link_location: 'contact_page', unit: unidade || 'sem_preferencia' });
      window.open(`https://api.whatsapp.com/send?phone=5541996962223&text=${encodeURIComponent(msg)}`, '_blank');
      status.textContent = 'Perfeito! Abrimos o WhatsApp para você concluir o contato.';
      status.style.color = '#16816B';
      form.reset();
    });
  }

  /* ---------- filtro de categorias do blog ---------- */
  const tagPills = document.querySelectorAll('.tag-pill[data-filter]');
  const postCards = document.querySelectorAll('[data-category]');
  if (tagPills.length && postCards.length) {
    tagPills.forEach(pill => {
      pill.addEventListener('click', () => {
        tagPills.forEach(p => p.classList.remove('active'));
        pill.classList.add('active');
        const filter = pill.getAttribute('data-filter');
        postCards.forEach(card => {
          const show = filter === 'todos' || card.getAttribute('data-category') === filter;
          card.style.display = show ? '' : 'none';
        });
        track('blog_filter', { category: filter });
      });
    });
  }

  /* ---------- rastreamento: cliques (whatsapp, telefone, e-mail, cards) ---------- */
  document.addEventListener('click', (e) => {
    const a = e.target.closest('a[href]');
    if (!a) return;
    const href = a.getAttribute('href') || '';
    const location = trackLocation(a);
    const linkText = (a.textContent || '').trim().slice(0, 80);

    if (/api\.whatsapp\.com|wa\.me/.test(href)) {
      appendUtmToWhatsAppHref(a);
      let waMessage = '';
      try { waMessage = decodeURIComponent(new URL(a.href).searchParams.get('text') || ''); } catch (err) { /* ignore */ }
      track('whatsapp_click', { link_location: location, link_text: linkText, whatsapp_message: waMessage });
      track('generate_lead', { lead_type: 'whatsapp', link_location: location });
      return;
    }
    if (href.indexOf('tel:') === 0) {
      track('phone_click', { link_location: location, phone_number: href.replace('tel:', '') });
      track('generate_lead', { lead_type: 'phone', link_location: location });
      return;
    }
    if (href.indexOf('mailto:') === 0) {
      track('email_click', { link_location: location, email_address: href.replace('mailto:', '') });
      return;
    }
    if (a.closest('.bento-item') || a.closest('.treat-card')) {
      const h = a.querySelector('h3, h4');
      track('treatment_click', { treatment: h ? h.textContent.trim() : linkText, link_location: location });
    } else if (a.closest('.post-card') || a.closest('.post-feat')) {
      const h = a.querySelector('h3, h2');
      track('blog_post_click', { post_title: h ? h.textContent.trim() : linkText, link_location: location });
    } else if (a.closest('.main-nav')) {
      track('nav_click', { nav_label: linkText });
    }
    try {
      const u = new URL(a.href, window.location.href);
      if (u.hostname && u.hostname !== window.location.hostname) {
        track('outbound_click', { link_location: location, link_url: a.href, link_domain: u.hostname });
      }
    } catch (err) { /* href inválido, ignora */ }
  });

  /* ---------- rastreamento: profundidade de rolagem ---------- */
  const scrollMarks = [25, 50, 75, 90];
  const scrollFired = {};
  const trackScrollDepth = throttle(() => {
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    if (docHeight <= 0) return;
    const pct = Math.round((window.scrollY / docHeight) * 100);
    scrollMarks.forEach((m) => {
      if (pct >= m && !scrollFired[m]) {
        scrollFired[m] = true;
        track('scroll_depth', { percent: m, page_path: window.location.pathname });
      }
    });
  }, 500);
  window.addEventListener('scroll', trackScrollDepth, { passive: true });

  /* ---------- rastreamento: tempo na página ---------- */
  [30, 60, 120].forEach((seconds) => {
    setTimeout(() => track('time_on_page', { seconds, page_path: window.location.pathname }), seconds * 1000);
  });

  /* ---------- rastreamento: visualização de página (com UTM da sessão) ---------- */
  const utm = getStoredUTM();
  track('page_view_advanced', {
    page_path: window.location.pathname,
    page_title: document.title,
    utm_source: utm.utm_source || '',
    utm_medium: utm.utm_medium || '',
    utm_campaign: utm.utm_campaign || '',
  });
});
