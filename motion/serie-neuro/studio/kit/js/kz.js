/* KizuBot motion kit — deterministic GSAP helpers for HyperFrames compositions.
   Load after gsap: <script src="kit/js/gsap.min.js"></script><script src="kit/js/kz.js"></script>
   Every helper only ADDS tweens to the timeline you pass in; nothing reads clocks or randomness. */
(function () {
  const KZ = {};

  /** Seeded PRNG (mulberry32). Use instead of Math.random. */
  KZ.rng = function (seed) {
    let a = seed >>> 0;
    return function () {
      a |= 0; a = (a + 0x6d2b79f5) | 0;
      let t = Math.imul(a ^ (a >>> 15), 1 | a);
      t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  };

  /** Beat grid helper: const b = KZ.beats(130); b(4) -> time of beat 4 in seconds. */
  KZ.beats = function (bpm, offset) {
    const beat = 60 / bpm;
    return function (n) { return (offset || 0) + n * beat; };
  };

  /** Wrap words (default) or chars of an element in inline-block spans. Returns the spans. */
  KZ.split = function (el, mode) {
    if (typeof el === "string") el = document.querySelector(el);
    const text = el.textContent;
    el.textContent = "";
    const out = [];
    if (mode === "chars") {
      for (const word of text.split(/(\s+)/)) {
        if (/^\s+$/.test(word)) { el.appendChild(document.createTextNode(" ")); continue; }
        const w = document.createElement("span");
        w.style.display = "inline-block"; w.style.whiteSpace = "nowrap";
        for (const ch of word) {
          const s = document.createElement("span");
          s.className = "kz-char"; s.style.display = "inline-block"; s.textContent = ch;
          w.appendChild(s); out.push(s);
        }
        el.appendChild(w);
      }
    } else {
      const words = text.trim().split(/\s+/);
      words.forEach(function (w, i) {
        const s = document.createElement("span");
        s.className = "kz-word"; s.style.display = "inline-block"; s.textContent = w;
        el.appendChild(s); out.push(s);
        if (i < words.length - 1) el.appendChild(document.createTextNode(" "));
      });
    }
    return out;
  };

  /** pt-BR number formatting. fmt: "int" (1.700), "k" (322,4k), "dec1" (8,3), "brl" (R$ 8,33), "pct" (42%) */
  KZ.fmt = function (v, fmt) {
    if (fmt === "k") return (v / 1000).toFixed(1).replace(".", ",") + "k";
    if (fmt === "dec1") return v.toFixed(1).replace(".", ",");
    if (fmt === "dec2") return v.toFixed(2).replace(".", ",");
    if (fmt === "brl") return "R$ " + v.toFixed(2).replace(".", ",");
    if (fmt === "pct") return Math.round(v) + "%";
    if (fmt === "time") { const m = Math.floor(v / 60), s = Math.floor(v % 60); return String(m).padStart(2, "0") + ":" + String(s).padStart(2, "0"); }
    return Math.round(v).toLocaleString("pt-BR");
  };

  /** Count a number up inside el (seek-safe onUpdate). */
  KZ.countUp = function (tl, el, from, to, at, dur, fmt, ease, suffix) {
    if (typeof el === "string") el = document.querySelector(el);
    const o = { v: from };
    const sfx = suffix || "";
    el.textContent = KZ.fmt(from, fmt) + sfx;
    tl.to(o, { v: to, duration: dur, ease: ease || "power2.out", onUpdate: function () { el.textContent = KZ.fmt(o.v, fmt) + sfx; } }, at);
    return tl;
  };

  /** Typewriter: reveal text char by char (cps = chars per second). Optional caret element. */
  KZ.typewriter = function (tl, el, text, at, cps) {
    if (typeof el === "string") el = document.querySelector(el);
    const o = { n: 0 };
    el.textContent = "";
    tl.to(o, { n: text.length, duration: text.length / (cps || 22), ease: "none", onUpdate: function () { el.textContent = text.slice(0, Math.round(o.n)); } }, at);
    return tl;
  };

  /** Punch-in: quick zoom on a wrapper (not a .clip). */
  KZ.punch = function (tl, target, at, scale, hold) {
    tl.fromTo(target, { scale: 1 }, { scale: scale || 1.12, duration: 0.12, ease: "power3.out", immediateRender: false }, at);
    tl.to(target, { scale: 1, duration: hold || 0.5, ease: "power2.inOut" }, at + 0.12);
    return tl;
  };

  /** Deterministic shake (seeded keyframes). */
  KZ.shake = function (tl, target, at, intensity, dur, seed) {
    const r = KZ.rng(seed || 7);
    const n = Math.max(4, Math.round((dur || 0.4) / 0.04));
    const amp = intensity || 18;
    for (let i = 0; i < n; i++) {
      const k = 1 - i / n;
      tl.to(target, { x: (r() * 2 - 1) * amp * k, y: (r() * 2 - 1) * amp * k, rotation: (r() * 2 - 1) * 2 * k, duration: 0.04, ease: "none" }, at + i * 0.04);
    }
    tl.to(target, { x: 0, y: 0, rotation: 0, duration: 0.05, ease: "none" }, at + n * 0.04);
    return tl;
  };

  /** Full-frame white (or colored) flash on an overlay element. */
  KZ.flash = function (tl, overlay, at, peak, color) {
    // immediateRender:false so several flashes on one overlay never leak their start state backwards in time
    tl.set(overlay, { backgroundColor: color || "#ffffff", immediateRender: false }, at);
    tl.fromTo(overlay, { opacity: peak || 0.85 }, { opacity: 0, duration: 0.35, ease: "power2.out", immediateRender: false }, at);
    return tl;
  };

  /** Pop in (scale from small with overshoot). */
  KZ.pop = function (tl, target, at, dur) {
    tl.fromTo(target, { scale: 0.4, opacity: 0 }, { scale: 1, opacity: 1, duration: dur || 0.45, ease: "back.out(2.2)" }, at);
    return tl;
  };

  /** Rise in. */
  KZ.rise = function (tl, target, at, dur, dist) {
    tl.fromTo(target, { y: dist || 60, opacity: 0 }, { y: 0, opacity: 1, duration: dur || 0.5, ease: "power3.out" }, at);
    return tl;
  };

  /** Slam: big to normal, very fast (kinetic type). */
  KZ.slam = function (tl, target, at, from) {
    tl.fromTo(target, { scale: from || 2.2, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.28, ease: "power4.out" }, at);
    return tl;
  };

  /** Word-by-word kinetic reveal; returns the time the last word lands. */
  KZ.words = function (tl, el, at, gap, style) {
    const spans = KZ.split(el, "words");
    spans.forEach(function (s, i) {
      const t = at + i * (gap || 0.18);
      if (style === "rise") tl.fromTo(s, { y: 70, opacity: 0 }, { y: 0, opacity: 1, duration: 0.35, ease: "power3.out" }, t);
      else if (style === "pop") tl.fromTo(s, { scale: 0.3, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.35, ease: "back.out(2.5)" }, t);
      else tl.fromTo(s, { scale: 1.9, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.26, ease: "power4.out" }, t);
    });
    return at + (spans.length - 1) * (gap || 0.18) + 0.3;
  };

  /** Top progress bar filling over [start, end]. el = the inner bar. */
  KZ.progress = function (tl, el, start, end) {
    tl.fromTo(el, { scaleX: 0 }, { scaleX: 1, duration: end - start, ease: "none" }, start);
    return tl;
  };

  /** Slow ambient drift for backgrounds (yoyo, finite). */
  KZ.drift = function (tl, target, total, dx, dy, period) {
    const p = period || 6;
    const reps = Math.max(0, Math.floor(total / p) - 1);
    tl.fromTo(target, { x: -(dx || 40), y: -(dy || 30) }, { x: dx || 40, y: dy || 30, duration: p, ease: "sine.inOut", yoyo: true, repeat: reps }, 0);
    return tl;
  };

  /** Glow pulse on the mascot eye overlay (see kit/README.md for the eye position). */
  KZ.eyePulse = function (tl, eye, at, times) {
    for (let i = 0; i < (times || 2); i++) {
      tl.fromTo(eye, { opacity: 0.2, scale: 0.8 }, { opacity: 1, scale: 1.25, duration: 0.18, ease: "power2.out", immediateRender: i === 0 }, at + i * 0.45);
      tl.to(eye, { opacity: 0.35, scale: 1, duration: 0.25, ease: "power2.in" }, at + i * 0.45 + 0.18);
    }
    return tl;
  };

  window.KZ = KZ;
})();
