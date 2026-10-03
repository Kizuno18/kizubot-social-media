# Neuromarketing & retention playbook (production version)

Condensed from the research playbook (49 techniques, platform docs and studies up to Sep 2026; full version with sources: `docs/research/neuromarketing-playbook.md`). "Neuro" words explain *why* a pattern works; never put brain claims in the videos.

## The 10 rules that matter most
1. **Win 0–2 s.** Frame 0 already has motion + sound + a 2–5-word hook in the hook band. Half of an ad's impact lands in the first 2 s; Instagram's skip rate counts exits before 3 s; Shorts reports "viewed vs swiped away".
2. **Optimize watch-through and replays, not length.** 15–22 s loopable cuts for reach; 24–30 s only for demos. Every replay counts as a view on all three platforms.
3. **The ending feeds the beginning.** Last frame ≈ first frame's background/state; the last line can complete into the hook.
4. **Design for sends.** High-arousal emotions (excitement, awe, indignation, amusement) get shared; build on a pain every player shares (losing a shiny while AFK) with a payoff they'd send to their duo.
5. **One idea per screen.** ≤ 6 words per hook card, ≤ 8 per body card; pt-BR reading ≤ 15 characters/s → hold time ≈ characters ÷ 15 + 0.25 s. Hooks 120–180 px; must-read body text ≥ 56 px (small non-essential tags like "print real de cliente" ≥ 30 px). Leave headroom above uppercase accents (Ã, É, Ê) — tight line-heights clip them.
6. **Sound-on first, sound-off safe.** SFX on every visual event + original music; the burned-in text must tell the story alone.
7. **Real proof, precise numbers.** Precise numbers read as credible ("16:42", "8.434", "R$ 8,33"). Fakes get de-ranked (TikTok "misleading claims") and break consumer law (CDC art. 37).
8. **Brand early, lightly, repeatedly, with a sound.** A brand cue within ~5 s (e.g. the alarm sender "KizuBot™ | kizubot.com", the robot eye, a small purple chip), back 2–3 times in different places, total on-screen brand ≤ ~25% of runtime, the sonic logo at the reveal/end (≤ 2× per video, always identical).
9. **Talk like a player, never say "hack".** Frame KizuBot as automação / AFK / farm / alarme / qualidade de vida.
10. **Originality is ranked.** All platforms penalize templated near-duplicates: within a series change the narrative, layout, palette accents, motion and music — not just the hook text.

## Hooks (pick one mechanism, execute it in < 0.5 s)
Mechanisms: motion onset on frame 0 · audio transient on frame 0 (never fade in) · result first (show the real alarm/capture, then "como?") · specific curiosity gap (answer it at 40–60% of runtime, never after 70%) · "você" question (≤ 7 words, then 0.3 s pause) · negative/contrarian frame (pivot to positive by 3–5 s) · precise number · moderate schema violation ("Desliguei o PC. O farm não parou.") · POV casting · big type (120–180 px recommended, ≥ 96 px minimum, 2 lines max).
Templates that fit KizuBot (true versions only):
- "Você ainda farma na mão em 2026?"
- "O shiny nasceu às {hh:mm}. {Ele} tava dormindo." (real print time)
- "Para de perder shiny por estar AFK."
- "POV: são 2h e seu celular vibra."
- "Desliguei o PC. O farm não parou."
- "Farmar na mão: high cortisol. KizuBot: low cortisol." (2026 meme format)
- "Enquanto você farma aura, o KizuBot farma shiny." (2025–26 slang)
- "R$ 0,35 por hora de farm. Sério."
- "Seu farm para quando você dorme. O dele não."
- "Se você joga PxG, para 10 segundos."
- "O zap tocou. Era BOSS."
- "Tipos de jogador quando o shiny nasce às 3h:"

## Holding attention (2 s → end)
- **Re-hook every 5–7 s** (max one per 5 s): new question or number, scene change, a *different* SFX, a one-bar music variation. Lines: "Mas olha isso:", "E não para aí", "Agora o melhor:".
- **Visible progress:** a game-style XP/progress bar (fills fast early — slow-early bars increase abandonment), numbered items ("1/3"), five pips for a Top 5. Never present it as a deadline.
- **Cut rhythm:** hook shots 0.4–0.8 s, body 1.0–2.0 s, proof screenshots 1.5–2.5 s (reading time!). Vary lengths (1.2/0.8/1.6/0.8/2.0), don't metronome. Cuts and stamps on beats or half-beats; visual hit on the frame *at or just before* the beat (sound must never lead the picture).
- **SFX density:** 2–4 per second in the hook, 1–2 per second in the body; rotate variants (the same SFX over and over habituates). Silence before reveals.
- **One emphasized word per card** (gold/lime, scale 1.15–1.3×, `back.out(2)`, tick SFX).
- **Cognitive load:** one claim per card, ≤ 2 moving elements at once, strip UI chrome and zoom to the relevant line, text ≤ ~35% of the frame area.
- **Center-locked composition:** hero object around x = 540, y ≈ 650–1000; transitions move through the center (push-ins), not across edges.

## Emotion & reward
- **Anticipation → drop:** 2 bars of build (riser, filtered drums, element rising), 150–300 ms of near-silence, then the reveal on the downbeat with impact, a 6 px / 0.2 s shake and particles. Place the drop at **35–55% of runtime**. Once per video. Use radar/sonar/countdown metaphors — **never slot machines, roulettes or loot boxes** (TikTok regulates gambling-like content).
- **Variable reveal:** irregular intervals, common items then one rare in gold with a bigger SFX. Show realistic frequency; no repeated near-miss "quase!" mechanics.
- **Peak–end:** one clear emotional peak (the reveal) and a positive, simple last 1.5–2 s (end on the outcome; price as supporting text, not the last word).
- **Loss aversion:** losses weigh ≈ 2× gains — frame what gets lost while AFK (a sparkle that despawns while a clock ticks), then switch to the gain frame.
- **FOMO only when true:** the spawn really disappears; KizuBot's alarm really solves it. No "só hoje", no "últimas vagas".
- **Humor = benign violation (zoeira):** self-deprecating player pain, absurd exaggeration; keep proof segments serious to protect credibility. Never joke about real people, minorities or game staff.
- **Nostalgia:** chiptune blips, pixel labels, CRT transitions for the "old way" segment vs the modern purple KizuBot look. No Nintendo/Game Boy trademarks, boot sounds or Pokémon music.
- **Satisfying micro-motion (ASMR):** precise ticking counters, cards snapping into grids, bars filling with `power2.inOut`, calm 80–90 BPM.
- **Micro-story:** setup (night) → conflict (spawn while you sleep) → turn (alarm) → resolution (captured) → tag. Precise timestamps and sensory details (vibration, screen lighting the ceiling). A fictional scene must never be presented as a testimonial.

## Persuasion
- **Social proof (real):** real alarm/chat screenshots stacking like a feed, 0.5–2 s each, "print real de cliente". Don't crop or reorder lines in a way that changes meaning.
- **Authority by competence:** changelog facts ("mais de 170 atualizações desde 2024"), real HUD numbers. No implied endorsement by PxG, staff or streamers.
- **Anchoring:** anchor on the time cost first (8 h × 30 = 240 h), then the price (R$ 250/mês), then the reframes (≈ R$ 8,33/dia → "menos de R$ 9 por dia"; ≈ R$ 0,35/hora). Hold the final price ≥ 1.2 s; say it's a monthly plan.
- **Ownership language:** "o SEU bot", "SEU farm". Never imply the viewer already owns it.
- **IKEA / easy setup:** 3 steps, ~1 s each, satisfying toggles, "pronto ✅" — but don't make it look trivial (customers do mention a learning curve; say "o suporte ajuda").
- **Commitment ladder:** 2–3 rhetorical yes-questions, each ticking a ✅ ("Já perdeu shiny dormindo?").
- **Reciprocity:** a genuinely useful tip only if it's accurate (don't invent game tips).
- **Fluent slogans for end cards:** "Você dorme. Ele farma." · "PC desligado, farm ligado." · "Shiny apareceu? O zap avisou."

## Brand & memory
- Same font family, purple identity, mascot eye glow and sonic logo across all shorts. Color code: **purple = brand**, **gold/yellow = shiny/rare**, **lime = alert/active/gain**, **red = pain/manual/loss** only. Purple text on dark backgrounds fails contrast — use lavender (#d8b4fe) or white.
- Picture superiority: every claim gets a visual proof; show the product in context (phone on the nightstand at 3 a.m.).
- Product mockups: the real panel UI isn't available in current form, so draw stylized illustrations (toggles, icons, cards) that read as illustration — never fake detailed "screenshots"; label example chats "exemplo".
- **Seamless loop:** the last 0.5 s morphs into frame 0 (same background, same positions); the CTA sits at 70–90% of runtime with the loop seam after it.

## Safe zones (1080×1920, organic)
Readable box **x 90→960, y 220→1400**; below y = 860 keep text at **x ≤ 880** (right action rail). Hook band x 120→888, y 290→840 (also survives the 3:4 profile-grid crop: keep the cover title inside x 120→960, y 300→1380). Never put must-read text at y < 220, y > 1400, x < 60 or x > 880 between y 860–1700. Decorative motion may bleed anywhere. Split screens: top/bottom, not left/right (the rail covers the right).

## CTAs (end card, one ask)
- On screen: a **genuine question** tied to the story ("Qual shiny você mais perdeu?"), or "link na bio", or a slogan + kizubot.com. Never "comenta X", "marca um amigo", "compartilha", "curte", "segue" on screen (Instagram de-recommends engagement bait; TikTok penalizes false incentives / like-for-like).
- Caption/pinned comment may carry the explicit ask (TikTok/YouTube). Shorts can't have clickable links in descriptions: say "kizubot.com" in text.
- Don't promise a DM ("comenta KIZU que eu te mando") — no automated DM flow is confirmed.

## Audio rules
- Transient at 0.00, first downbeat at 0.00, no fade-in. Music 120–155 BPM for energy (phonk/funk/trap/house), 80–90 for calm/satisfying, tension for suspense.
- Durations in whole bars when you can (20 s @ 130 BPM ≈ 10.8 bars — fine, but land the end card on a bar line).
- The KizuBot `alert` (motif twice) = in-game alarm, the `logo` sting = end card; never imitate the WhatsApp tone or platform sounds (ours are original).
- Flash rule: no more than 3 full-screen flashes per second.

## Wording guide
Avoid: hack, cheat, trapaça, macro, script, "indetectável", "anti-ban", "sem ban", "100% seguro", "meme-testador-aprovado pelo PXG", "GM não pega", "fique rico", "renda extra", "dinheiro fácil", "últimas vagas", "só hoje", R$ earnings, odds/probabilities, "IA" as the headline benefit.
Prefer: automação, AFK, farm, farmar, upar, alarme, avisa no zap/WhatsApp, PC desligado, na nuvem, enquanto você dorme/trabalha/treina, seu tempo de volta, detecção de shiny/mega/boss, pesca sozinho, tudo pelo celular.
