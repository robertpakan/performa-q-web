/* PERFORMA-Q site JS */
(function () {
  'use strict';

  /* mobile nav */
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.querySelector('nav.main');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  /* countdown to Open Call deadline — 31 July 2026, 23:59 CEST */
  var DEADLINE = new Date('2026-07-31T23:59:59+02:00').getTime();
  function pad(n) { return n < 10 ? '0' + n : '' + n; }
  function tick() {
    var els = document.querySelectorAll('[data-count]');
    if (!els.length) return;
    var d = DEADLINE - Date.now();
    var closed = d <= 0;
    var days = Math.max(0, Math.floor(d / 864e5));
    var hrs = Math.max(0, Math.floor(d % 864e5 / 36e5));
    var min = Math.max(0, Math.floor(d % 36e5 / 6e4));
    var sec = Math.max(0, Math.floor(d % 6e4 / 1e3));
    els.forEach(function (el) {
      var k = el.getAttribute('data-count');
      if (k === 'days') el.textContent = pad(days);
      if (k === 'hours') el.textContent = pad(hrs);
      if (k === 'minutes') el.textContent = pad(min);
      if (k === 'seconds') el.textContent = pad(sec);
    });
    var strips = document.querySelectorAll('[data-deadline-msg]');
    strips.forEach(function (s) {
      if (closed) s.textContent = 'Open Call · Cycle 1 is now closed. Thank you for applying — selections announced soon.';
    });
    if (!closed) setTimeout(tick, 1000);
  }
  tick();

  /* scroll reveal (skipped for reduced motion) */
  if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches && 'IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
      });
    }, { threshold: 0.12 });
    document.querySelectorAll('.rv').forEach(function (el) { io.observe(el); });
  } else {
    document.querySelectorAll('.rv').forEach(function (el) { el.classList.add('in'); });
  }

  /* contact form → FormSubmit (AJAX, stays on page) */
  var form = document.querySelector('form.contact');
  if (form) {
    form.addEventListener('submit', function (ev) {
      ev.preventDefault();
      var btn = form.querySelector('button[type=submit]');
      var note = form.querySelector('[data-form-note]');
      var data = new FormData(form);
      btn.disabled = true; btn.textContent = 'Sending…';
      fetch('https://formsubmit.co/ajax/performa@performa-q.eu', {
        method: 'POST',
        headers: { 'Accept': 'application/json' },
        body: data
      }).then(function (r) { return r.json(); }).then(function (res) {
        if (res.success === 'true' || res.success === true) {
          form.reset();
          btn.textContent = 'Sent ✓';
          if (note) note.textContent = 'Thank you — your message is on its way.';
        } else { throw new Error('send failed'); }
      }).catch(function () {
        btn.disabled = false; btn.textContent = 'Send message';
        if (note) note.textContent = 'Sending failed — please e-mail performa@performa-q.eu directly.';
      });
    });
  }
})();

/* pause ambient video for reduced-motion users */
(function () {
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    document.querySelectorAll('video[autoplay]').forEach(function (v) {
      v.removeAttribute('autoplay'); v.pause();
    });
  }
})();
