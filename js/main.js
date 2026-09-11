// Instituto Christian Andrade — interações do site
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
      }
    });
  });

  /* ---------- carrossel de depoimentos (arraste/scroll) ---------- */
  document.querySelectorAll('.testi-slider').forEach(slider => {
    const track = slider.querySelector('.testi-track');
    const prev = slider.querySelector('.testi-prev');
    const next = slider.querySelector('.testi-next');
    if (!track) return;
    const scrollByCard = (dir) => {
      const card = track.querySelector('.testi-card');
      const gap = parseFloat(getComputedStyle(track).gap || 24);
      const amount = card ? (card.offsetWidth + gap) * dir : 320 * dir;
      track.scrollBy({ left: amount, behavior: 'smooth' });
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
      });
    });
  }
});
