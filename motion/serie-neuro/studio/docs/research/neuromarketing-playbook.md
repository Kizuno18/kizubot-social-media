# KizuBot — Neuromarketing + Virality Playbook
### 15–30 s vertical motion-graphics shorts (TikTok · YouTube Shorts · Instagram Reels) for Brazilian PokeXGames players

Compiled 2026-10-03. Covers platform documentation, policies and studies available up to September 2026. Written for motion designers who build videos in code (HTML/CSS/GSAP → MP4) with no on-camera person: kinetic type, UI mockups, real customer screenshots, synthesized music, sound effects and, optionally, a synthesized voiceover.

**How to read this document**
- Numbers in brackets such as [12] point to the numbered source list in §11.
- Evidence tags: **[A]** official platform statement or policy · **[B]** peer-reviewed research · **[C]** industry or vendor data (treat as directional) · **[H]** practitioner heuristic, so A/B test it before relying on it.
- "Neuro" terms (dopamine, reward prediction error, orienting response) describe mechanisms from lab research. They explain *why* a pattern tends to work. They do not mean a single 20-second video produces a measurable brain effect. Never put such claims in the videos themselves.

**Product truth sheet (fill in before scripting).** Every on-screen claim must map to a row here. If a row can't be proven, the claim doesn't ship.

| Claim | Approved pt-BR wording | Proof needed |
|---|---|---|
| Farms, catches and fishes automatically in the cloud | "farma, captura e pesca por você — na nuvem" | Product demo footage |
| Runs 24/7 | "24h por dia" / "24/7" only if uptime is real; otherwise "enquanto seu PC tá desligado" | Uptime logs |
| WhatsApp alarm for shiny / mega / boss | "te avisa no WhatsApp quando aparece shiny, mega ou boss" | Real alert screenshots |
| Price R$ 250/mês | "R$ 250/mês ≈ R$ 8,33 por dia" (30-day month) · "≈ R$ 0,35 por hora de bot ligado" (720 h). Never "R$ 8/dia", which understates the price. | Price page |
| Customer, shiny or hours counts | Real numbers with a date ("até set/2026") | Logs / database export |
| Testimonials and screenshots | Real customers, written consent, unaltered (blurring nicknames and personal data is fine) | Consent records |
| Game-rule status | Confirm PokeXGames' rules on third-party automation (the official site returned errors during this research). Never say "sem ban", "indetectável" or "meme-testador-aprovado pelo PXG" unless it's documented. | PXG rules page |

---

## 1. Executive summary: the 10 highest-leverage rules

1. **Win the first 0.5–2 s, or nothing else matters.** TikTok's marketing science finds 50% of an ad's impact lands in the first 2 s and 90% of recall by 6 s [5]. 63% of the highest-CTR TikTok ads state the key message within 3 s [3]. Instagram's *Skip rate* counts viewers who leave within 3 s [38], and YouTube Shorts reports *viewed vs. swiped away* [27]. → Frame 0 must already have **motion + sound + a 2–5-word hook** in the upper-middle safe band.
2. **Optimize for watch-through and rewatches, not for length.** TikTok treats finishing a video as a strong interest signal [1]. YouTube counts every replay as a view (since 2025-03-31), and average percentage viewed can pass 100% through loops [17][28]. Mosseri named watch time, likes per reach and sends per reach as Instagram's top signals [30]. → Make **15–22 s loopable cuts** for reach and **24–30 s cuts** for demos and conversion.
3. **Make every ending feed back into the beginning.** The last frame should match the first frame's background and state, and the last line should complete into the hook line. Replays count as views and add watch time on all three platforms [17][28][37].
4. **Design for shares ("sends"), not likes.** Sends drive non-follower reach on Instagram [30]. High-arousal emotions (awe, anger, anxiety) increase sharing, while low-arousal ones (sadness) reduce it [100]. → Build around a pain every player shares (losing a shiny while AFK), with a payoff they want to send to their *duo*.
5. **One idea per screen, ≤ 6 words per hook card, ≥ 64 px text.** Brazilian adults read about 180 wpm (≈ 18 characters/s) aloud at maximum effort [112]. Netflix caps pt-BR subtitles at 17 cps for adults and 13 cps for children [111]. Faster pacing raises attention only up to the point of cognitive overload [94].
6. **Sound-on first, sound-off safe.** 88% of TikTok users call sound essential [6], and more than 75% of Reels views are sound-on [39]. But 69% of people watch sound-off in public [110]. → Put an SFX on every visual event and use original 120–155 BPM music [3][7]. The burned-in text must tell the story on its own.
7. **Real proof with precise numbers converts. Fakes get you de-ranked and sued.** Precise numbers read as more credible [107], and social proof works [58]. TikTok removes fake engagement and makes "misleading claims meant to boost views" FYF-ineligible [2]. CDC art. 37 bans misleading advertising [141].
8. **Brand early, lightly and repeatedly, with a sound.** In Meta/Toluna's Reels study, brand + message within 5 s gave 1.7× odds of top-tier purchase intent, dynamic branding (varied positions) 1.8×, and keeping brand presence to ~25% of runtime 4.8× (direct response) [40]. Audio brand assets outperform many visual ones [67]. → Use a ~1 s "Kizu ping" sonic logo and a purple-plus-accent motif.
9. **Talk like a player, not a marketer, and never say "hack".** In-group identity drives action [73]. But Google Ads prohibits "hacking services, including game enhancements and cheat softwares" [23], and Meta bans ads for products that enable cheating [41]. → Frame KizuBot as **automação / AFK / qualidade de vida**. Keep promotion mostly organic, and switch on TikTok's commercial-content disclosure ("Sua marca"), because undisclosed commercial content is ineligible for the For You feed [2].
10. **Protect minors and stay clear of IP.** Brazil's ECA Digital (in force since 2026-03-17) bans profiling-based ad targeting of under-18s [139][140]. The Pokémon Company aggressively enforces its IP, especially against monetized fan projects [144][145]. → Target paid ads 18+ only, keep Pokémon names, sprites and logos out of ads, and avoid casino or loot-box imagery (TikTok regulates gambling-like and "mystery value" content) [2].

---

## 2. Platform algorithm cheat-sheet (status: October 2026)

| | **TikTok** | **YouTube Shorts** | **Instagram Reels** |
|---|---|---|---|
| **Officially stated ranking inputs** | User interactions (likes, shares, comments, follows, content you create), video information (captions, sounds, hashtags), device/account settings. "A strong indicator of interest, such as whether a user finishes watching a longer video from beginning to end," gets greater weight. Follower count and past hits are **not** direct factors [1] **[A]** | The algorithm "follows the audience": it pulls videos for each viewer [29]. Satisfaction surveys separate watch time from value — Todd Beaupré warns against assuming "all time is valuable" — with the goal of long-term viewer value (2026-09-01) [24] **[A]** | "The top three signals … are watch time, likes and sends" — watch *likes per reach* and *sends per reach* (Mosseri, 2025-01-22). Sends matter more for reaching non-followers, likes more for followers [30] **[A, via secondary report]** |
| **Hook metric in analytics** | 2-second and 6-second view rates (Ads), retention curve, "watched full video" | **Viewed vs. swiped away** (share who chose to view). YouTube publishes **no universal good threshold**; benchmark against your own Shorts [27] | **Skip rate** = % who scroll away within 3 s, plus a retention chart (added Aug 2025) [38] |
| **How views count** | Per play | Since **2025-03-31** every play *and replay* counts as a view. The old metric survives as "engaged views" and is still used for monetization (YPP) [17] **[A]** | "Views" = every start or replay. It became the primary metric across formats in Apr 2025 [37] |
| **Loops** | Completion is the strongest stated signal [1]. Replays as a strong signal is creator consensus **[H]** | Average percentage viewed can exceed 100% because loops add watch time [28] | Replays add views and watch time [37] |
| **Length** | Long uploads allowed. For organic posts, 15–30 s maximizes completion **[H]** | Up to 3 min since 2024-10-15 [18]. No official "ideal length"; YouTube publishes no retention threshold [27]. For Shorts ads, only the first 60 s play in the feed [19] | Must be **≤ 3 min to be recommended** to non-followers [31][33] **[A]** |
| **Seeding / early test** | Personalized by predicted interest [1]. "Follower-first" seeding has been widely reported since late 2025 but **TikTok hasn't confirmed it** [13] | Pull model per viewer [29]. Small-audience "testing" is what creators observe **[H]** | **Trial Reels** (2024-12-10) show a Reel to non-followers first, which makes them a free hook A/B test [34]. "Your Algorithm" lets viewers tune topics (Dec 2025) [35] |
| **Eligibility traps** | Undisclosed commercial content → not eligible for For You. Also ineligible: unoriginal or watermarked material, low-quality or minimally edited clips, "like-for-like", false incentives, "misleading claims meant to boost views". Gambling-like and "mystery value" items (including in-game currency) are regulated goods [2] **[A]** | "Inauthentic content" — templated, mass-produced, "scrolling text with minimal or no narrative" — is demonetized (renamed 2025-07-15) [20]. No clickable links in Shorts descriptions or comments since Aug 2023 [26] **[A]** | Not recommended: watermarks, blur, borders, **text covering the majority of the screen**, reposts, length > 3 min [31]. Content that explicitly asks for shares/comments/tags won't be recommended, *but* genuine comment→DM lead generation is allowed [32]. Accounts that are mostly reposts lose recommendations (expanded 2026-04-30) [36] **[A]** |
| **CTA / link surfaces** | Bio link needs a business account or ≥ 1,000 followers, and age 18+ [16]. DMs are 16+ only [2] | Channel links, "Related video" link to a long-form demo, pinned comment (not clickable) [26] | Bio link. Comment keyword → automated DM (allowed when it's real lead generation) [32]. Clickable links inside Reels only through paid Meta Verified tiers, still in test [44] |
| **Music** | Business accounts only see the Commercial Music Library in-app. Upload your own original audio instead [15] | Content ID applies, so synthesized original music avoids claims | Meta recommends original audio or its Sound Collection for ads [12] |
| **2025–26 changes** | New Community Guidelines effective 2025-09-13 (originality, commercial disclosure, AI-content labels) [2]. Creator Search Insights for keyword ideas [14] | 200 B daily Shorts views (Jun 2025) [25]. View-count change [17]. Inauthentic-content policy [20] | Views metric (Apr 2025) [37], Skip rate (Aug 2025) [38], Trial Reels [34], Your Algorithm [35], repost crackdown [36] |

**What this means for a KizuBot short**
- **Hook KPIs:** TikTok 2-s and 6-s view rate, Shorts *chose to view*, Instagram *skip rate*. Treat any third-party "70%+ = viral" threshold as anecdotal [27]. Compare against your own median per format.
- **Depth KPIs:** full-watch % (TikTok), average percentage viewed (Shorts — aim for > 100% on loop cuts), average watch time and *sends per reach* (Instagram).
- **Originality is a ranking input in practice.** All three platforms now penalize templated or reposted output [2][20][36]. A code pipeline makes it easy to mass-produce near-duplicates, so don't. Change the narrative, visuals and audio between posts, not just the hook text.
- **Testing loop:** for each concept, render 3 hook variants over the same body. Run them as Instagram Trial Reels [34] or space them out on TikTok/Shorts, keep the winner, and retire the rest.

### 2b. Brazil context that shapes every creative decision (2025–2026)

| Fact | Implication |
|---|---|
| 150 M YouTube users, 147 M on Instagram, and TikTok ads reach 131 M adults (80% of adults); data Oct 2025 [120]. Kwai has ~60 M monthly users in Brazil [138] | All three platforms are mass channels. Kwai is an optional fourth outlet for the same 9:16 export |
| 75.3% of Brazilians play games (down from 82.8% in 2025 [123]); mobile is the main platform (44.1%), Gen Z is now the largest group (36.5%); 62.6% revisit old games and 55.1% play classics with friends (PGB 2026, n = 7,115) [121][122] | Gaming identity and nostalgia (8-bit sounds, "old school" grind) resonate. Design phone-first |
| 45.7% worry about AI degrading creative work; ~39–41% would buy or consider AI-made games [122] | "IA" is a polarizing word. Lead with the outcome (farm 24h, alarme no zap); mention IA only as secondary proof |
| WhatsApp: 97% open it daily; 82% have messaged a company; 54% have bought through it; Pix is the top payment method in those purchases (71%) (Opinion Box, Jun 2025) [124] | "Chama no zap" and "paga no Pix" are low-friction, native CTAs. The WhatsApp alarm itself is culturally strong proof |
| Pix: 148.3 M active individual users in Dec 2025 (~86% of adults) [125]. **Pix Automático** for recurring payments launched 2025-06-16 [126] | For a monthly plan, "assina no Pix Automático" removes card friction (only if you actually offer it) |
| TikTok audience activity in Brazil concentrates after 16h and peaks at 20h BRT; Metricool's best TikTok slots are Mon 19h, Tue 16h, Wed–Thu 17h, Fri 16h, Sat 17h, Sun 20h; Instagram Wed/Fri 20h [127] | Start testing at 12:00–13:30 and 18:30–22:30 BRT on weekdays, 10:00–13:00 and 19:00–23:00 on weekends. Post 30–60 min before the peak, then read your own analytics |
| Funk is everywhere on TikTok (#funk on 22.4 M+ videos, Jul 2025) [129]; **#brazilianphonk grew 62%** in Europe Feb–May 2026, and creators use it in gaming edits [128]. Funk moved from 130 to 150 BPM after 2017 [130] | Synthesize *original* funk 150 / mandelão / automotivo / phonk-style beds. Don't recreate famous melodies |
| Gaming slang went mainstream: **"farmar aura"** (2025–26 craze, with tournaments in Belém, São Paulo and Juazeiro) [131], "buffado", "amassou", "flopou", "cringe 2.0" [132]. Memes of 2025: Guiana Brasileira, brainrot, "meme Dexter" [134]; brainrot was the most-searched term on YouTube Brazil in 2025 [135]. 2026: "high cortisol vs low cortisol" format [136] | "Enquanto você farma aura, o KizuBot farma shiny" is native. Reuse meme *formats*, never other people's footage or likeness. Check freshness weekly, because memes die in weeks |
| Brazilian online humor is "zoeira": self-deprecating, absurdist, inside jokes that don't care about outsiders [137] | Laugh *with* the player's suffering ("acordei e o shiny já tinha sumido 💀"), never at them |

**Gíria bank (use at most 1–2 per video; check freshness before every batch)** [131][132][133]
- **Core gaming terms (safe, durable):** farmar, upar, drop, dropar, loot, AFK, shiny, boss, mega, duo, tankar, grindar, nerfado/buffado, GG, "F".
- **2025–26 internet slang (fast-decaying, test first):** farmar aura / +1000 de aura, amassou, flopou/flopado, estourado, hypeado, cringe 2.0, memetizado, sigma, NPC, cracked ("manda muito bem no jogo"), sweat ("tryhard").
- **Brazilian everyday tone:** mano, pô, véi, tá ligado, bora, partiu, "zap" (WhatsApp), kkkk, 💀 (dying of laughter / "morri").
- **Avoid:** regional slang you can't voice authentically, sexual double meanings common in funk lyrics, and anything that mocks groups of people.

---

## 3. Safe zones for 1080 × 1920

Platforms move their UI often, and there are no official numbers for organic posts. The ad templates are the only official references. Values are in px from each edge (y is measured from the top).

| Platform & source | Top | Bottom | Left | Right | Notes |
|---|---|---|---|---|---|
| **TikTok In-Feed ads** (TikTok Ads Manager overlay) [8][9][10] | 240 | 660 | 120 | 120 + **300-px action column from y ≈ 840 down** (some overlays start it higher) | Caption length and add-ons change the zone. Download the official overlay zip [8] |
| TikTok organic (measured UI) [11] | ~108–150 | ~320–480 (grows with caption) | ~60 | ~120–140 rail | Username, caption, music ticker and progress bar sit at the bottom |
| **Instagram Reels ads** (Meta Ads Guide) [12] | 269 (14%) | 672 (35%) | 65 (6%) | 65 (6%) | Meta: "Consider leaving at least 14% of the top, 35% of the bottom, and 6% on each side … free from text, logos" |
| Instagram Reels organic (measured UI) [11] | ~210 | ~310 | ~65 | ~84 rail | Profile grid crops the cover to **3:4 (1080 × 1440, y 240–1680)** [33][43] |
| **YouTube Shorts ads** (Google vertical template, as compiled in [10]) | 288 (15%) | 672 (35%) | 48 | 192 | Google provides PNG safe-area templates [19] |
| YouTube Shorts organic (measured UI) [11][46] | ~120–288 | ~300 (≈ 360 with expanded description) | ~48 | ~96–140 rail | Title, channel handle and subscribe button sit at the bottom; search/menu icons at the top |

**Universal boxes (use these in every composition)**

```
          x=0      120                 780   888   960 1080
y=0     ┌──────────────────────────────────────────────┐
        │  DEAD: status bar / platform header / search │
y=290   ├────────┬───────────────────────────┬─────────┤
        │        │  HOOK BAND (strict)       │         │
        │        │  x 120→888, y 290→840     │         │
y=840   │        ├──────────────────┬────────┘  RIGHT  │
        │        │  BODY BOX        │   ACTION RAIL    │
        │        │  x 120→780       │  (likes, share,  │
        │        │  y 840→1248      │   avatar)        │
y=1248  ├────────┴──────────────────┴──────────────────┤
        │  ADS DEAD ZONE (35%): CTA bar, caption       │
y=1440  ├──────────────────────────────────────────────┤
        │  ORGANIC DEAD ZONE: username, caption, music │
y=1920  └──────────────────────────────────────────────┘
```

- **Hook band (strict, works for ads and organic on all platforms):** x 120→888, y 290→840 (768 × 550 px). Hook headline, hero number, "SHINY!" stamp.
- **Body box (strict):** x 120→780, y 840→1248 (660 × 408 px). UI mockups, screenshots, secondary text. It sits left of TikTok's action column and above Meta's 35% bottom band.
- **Organic-only practical box:** x 90→960, y 220→1400, but keep x ≤ 880 wherever y ≥ 860. Use this only for cuts that will never run as ads.
- **Never put must-read text, prices or logos at:** y < 220 · y > 1248 (ads) or y > 1440 (organic) · x > 880 between y 860 and 1700 · x < 60.
- **Cover frame:** keep the title inside x 120→960, y 300→1380 so it survives the 3:4 grid crop and feed overlays [43].
- **Center gravity:** in vertical video, centered subjects get longer fixations and fewer eye jumps than subjects that move around [108]. Anchor the hero object (phone with the alarm, bot dashboard) around x = 540, y ≈ 650–1000.
- Decorative full-bleed motion (backgrounds, particles, glows) may fill the whole 1080 × 1920 frame. Only information has to respect the boxes.

```js
// Safe-zone constants for GSAP/CSS layouts (1080x1920)
export const SAFE = {
  hook:    { x: 120, y: 290,  w: 768, h: 550 },   // strict, all platforms
  body:    { x: 120, y: 840,  w: 660, h: 408 },   // strict, left of TikTok rail
  organic: { x: 90,  y: 220,  w: 870, h: 1180, railX: 880, railFromY: 860 },
  cover:   { x: 120, y: 300,  w: 840, h: 1080 },  // survives 3:4 grid crop
};
// CSS: :root { --safe-top: 290px; --safe-bottom-ads: 672px; --safe-left: 120px; --safe-right: 192px; }
```

---
## 4. Technique library (49 techniques)

Each card has the same five parts: **Why** (mechanism and evidence) · **Do** (how to execute in a 15–30 s code-built short) · **pt-BR** (KizuBot example line) · **Risk** (ethics and compliance). Timings assume 30 or 60 fps and a beat grid (§8).

### A. Stop the scroll (0–2 s)

**T01 · Motion onset on frame 0** [B]
- **Why:** The *onset* of motion captures attention automatically; ongoing motion does not [82]. People can recall mobile feed content after just 0.25 s of exposure [42].
- **Do:** Frame 0 is never static or black. The hook text or hero object starts entering at t = 0.00–0.08 s (e.g. `scale 0.85→1, y +40→0, expo.out, 0.18 s`). Add a second onset at 0.5–0.7 s (the phone vibrates, a counter starts). Every cut re-triggers an onset.
- **pt-BR:** "SHINY APARECEU" slams in at 0.05 s over a vibrating phone.
- **Risk:** No more than 3 full-screen flashes per second (WCAG three-flashes rule) [115]. Don't imitate the platform's own UI or system alerts.

**T02 · Audio-visual hit on frame 0** [B][A]
- **Why:** Sound effects, production effects and jingles trigger orienting responses [95]. 88% of TikTok users say sound is essential [6], and Google reports sound lifts Shorts-ad conversions by more than 20% [19]. Viewers prefer music and visual accents that coincide [96].
- **Do:** Audio starts at t = 0 with a transient (impact, vibration buzz, whoosh) exactly on the first visual onset. Never fade audio in. Put the first music downbeat at 0.00.
- **pt-BR:** "📳 bzz-bzz" + text "O ZAP TOCOU ÀS 3H".
- **Risk:** Don't use the real WhatsApp notification tone or platform sounds; synthesize your own ping and buzz [45].

**T03 · Result first** [B][A]
- **Why:** Knowing the outcome doesn't spoil a story and can even increase enjoyment [105]. 63% of TikTok's highest-CTR ads show the key message within 3 s [3]. Brand + message within 5 s → 1.7× odds of top purchase intent on Reels [40].
- **Do:** 0.0–1.5 s shows the end state (real alert screenshot: "✨ SHINY detectado 03:12"). 1.5–2.5 s: "Como?" with a tape-rewind SFX and a scrub-back effect, then the process.
- **pt-BR:** "Acordei com isso no zap 👇"
- **Risk:** The result must be real. If it's atypical, say so ("resultado de um cliente; varia"). Leaving out material context is misleading under CDC art. 37 [141].

**T04 · Curiosity gap** [B]
- **Why:** Curiosity is the feeling of a gap between what we know and what we want to know [47]. It recruits reward circuitry and improves memory for the answer [48][49].
- **Do:** State one specific gap in ≤ 6 words. Answer it between 40% and 60% of runtime (6–10 s in a 15–20 s video), never after 70%. Visual: a masked or blurred card with a scanning line, revealed on a downbeat.
- **pt-BR:** "O PC tava desligado. Mesmo assim…" → reveal: "farmou 9h na nuvem".
- **Risk:** A gap that never pays off reads as clickbait, which lowers credibility [104]. TikTok makes "misleading claims meant to boost views" FYF-ineligible [2].

**T05 · Self-referencing question ("você")** [B][C]
- **Why:** Information related to the self is encoded better [106]. Self-referencing question headlines got ~175% more clicks than statements [103]. In TikTok's research, saying "you" within the first 5 s gave +128% purchase intent [4]. Caveat: in news, question headlines can feel like bait [104].
- **Do:** Second person singular, ≤ 7 words, ending in "?". Follow with a 0.3 s pause (music dips) so the viewer silently answers "sim". Give the key word its own line.
- **pt-BR:** "Você ainda farma na mão?"
- **Risk:** Only ask questions the video answers. Never address viewers by age ("você que tem 12 anos").

**T06 · Negative / contrarian frame** [B]
- **Why:** Bad is stronger than good (negativity bias) [102]. Across ~105k A/B-tested headlines, each extra negative word raised CTR by 2.3% [101]. High-arousal negative emotions (anger, anxiety) spread more; sadness spreads less [100].
- **Do:** Open with a pain or a "stop doing X". Pivot to the positive payoff by 3–5 s, so arousal stays high but the video ends positive (peak–end, T27). A 0.2 s red ❌ strike-through over "farmar na mão".
- **pt-BR:** "Para de perder shiny por estar AFK."
- **Risk:** Never attack PXG, other players or competitors by name; aim the negativity at the situation. Avoid fear appeals aimed at minors (abusive advertising, CDC art. 37 §2) [141].

**T07 · Precise numbers** [B]
- **Why:** Precise numbers read as more credible and competent than round ones [107].
- **Do:** Numerals, never words: "9h12", "R$ 8,33", "3 alarmes". Count up from 0 to the target in 0.6–0.9 s with a tick SFX on each step. Hero numbers ≥ 160 px.
- **pt-BR:** "9h12 de farm enquanto eu dormia."
- **Risk:** Real logged figures only, date-stamped. No cherry-picked outliers shown as typical.

**T08 · Pattern interrupt / schema violation** [B]
- **Why:** Moderately unexpected information is processed more deeply and liked more than fully expected or bizarre information [87]. Structural changes trigger involuntary orienting [93].
- **Do:** Break the feed's expected pattern within the first second. Example: the PC shuts down (CRT collapse to a line), yet the farm counter keeps climbing. The violation must be understood instantly ("moderate").
- **pt-BR:** "Desliguei o PC. O farm não parou."
- **Risk:** Don't imitate crash screens, virus warnings or system dialogs (deceptive).

**T09 · POV casting (substitute for a face)** [C][B]
- **Why:** In TikTok's research, a person in the first 2 s gives +50% "hooking power" [4]. Without a person, make the *viewer* the protagonist through self-reference [106].
- **Do:** A "POV:" label at the top of the hook band and a first-person scene: phone in hand, alarm at 3 a.m., dark room. Hands or a cursor do the "acting".
- **pt-BR:** "POV: são 3h da manhã e seu celular vibra"
- **Risk:** Keep it visibly illustrated; never fake "real footage" of a person.

**T10 · Mascot face + directional cues** [B][C]
- **Why:** Faces and text draw 16.6× and 11.1× more fixations than comparable regions [81]. Owned characters and sonic cues beat borrowed culture as brand assets [67]. Gaze cues steer attention toward what they point at [146].
- **Do:** A simple robot mascot ("Kizu"): two rounded-rectangle LED eyes that blink at 0.4 s (`scaleY 1→0.1→1`, 0.12 s), then *look* at the key element (alert, price). Use the same mascot in every video.
- **pt-BR:** Kizu looks at the alert: "Achei um shiny pra você 👀"
- **Risk:** The mascot must not resemble a Pokémon or any Nintendo character [144].

**T11 · Big-type hook (text as the attention magnet)** [B][A]
- **Why:** Text attracts gaze almost as strongly as faces [81]. 40% of TikTok's top-VTR auction ads use concise text overlays [3].
- **Do:** Hook headline at 120–180 px, 2 lines max, inside the hook band. White on a purple plate, or with an 8 px dark stroke, with one accent word. It appears by 0.1 s and is fully readable by 0.5 s.
- **pt-BR:** "FARMAR NA MÃO / em 2026? 💀"
- **Risk:** Instagram doesn't recommend videos where text covers the majority of the screen [31]. Keep text under ~35% of the frame and let visuals carry the rest.

### B. Hold attention (2–25 s)

**T12 · Open loop → payoff (resumption)** [B]
- **Why:** A 2025 meta-analysis found no memory advantage for unfinished tasks (the Zeigarnik effect), but it did find a general tendency to *resume* interrupted tasks (the Ovsiankina effect) [50]. Curiosity makes people willing to wait for answers [48].
- **Do:** Open the loop at 0–2 s ("a 3ª é a mais importante") and close it at 70–85% of runtime or at the end, never later. Make it visible: three empty slots, or a locked card that fills in.
- **pt-BR:** "3 coisas que o KizuBot faz enquanto você dorme — a 3ª salvou meu shiny"
- **Risk:** Leaving a loop unresolved is bait, and TikTok treats misleading view-boosting claims as FYF-ineligible [2].

**T13 · Re-hook every 5–7 s** [A][B][H]
- **Why:** 90% of TikTok ad recall is built by 6 s [5], so after that people need fresh reasons to stay. Structural changes re-trigger orienting [93], and voice changes keep doing so without habituating [95].
- **Do:** Insert re-hook beats at ~5 s, ~10–12 s and ~17 s: a new question or number, a scene change, a *different* SFX and a one-bar musical variation (fill, drop, filter sweep). Lines: "Mas olha isso:", "E não para aí", "Agora o melhor:".
- **pt-BR:** (at 6 s) "E quando aparece BOSS?"
- **Risk:** Too many re-hooks fragment attention and cause overload [94][109]. Max one per 5 s.

**T14 · XP / progress bar (goal gradient)** [B]
- **Why:** Effort accelerates as people near a goal (goal-gradient effect) [98]. Progress bars that move fast early reduce abandonment; slow-early bars increase it (~11% vs ~22% breakoff) [99].
- **Do:** A game-style XP bar (6–8 px, purple→gold) at y ≈ 300 in the hook band. It fills 0→40% in the first 25% of runtime, then linearly. Milestones = list items ("Lv 1/2/3"). It hits 100% at the CTA with a "LEVEL UP" ping. Keep it off the top/bottom edges, where native progress bars live.
- **pt-BR:** "XP do farm: 37% → 100%"
- **Risk:** Never present it as a deadline countdown (fake scarcity).

**T15 · Numbered list (1/3 · 2/3 · 3/3)** [B]
- **Why:** Predictable structure is processed fluently [68], visible progress motivates [98], and the last item is an open loop [50].
- **Do:** 3 items in 15–20 s (≈ 4 s each), up to 4 in 25–30 s. An index chip ("1/3") at the top-left of the hook band. Each item = title ≤ 4 words + one visual proof. Save the strongest for last and tease it upfront.
- **pt-BR:** "1/3 Farma 24h · 2/3 Pesca sozinho · 3/3 Te acorda no zap se vier shiny"
- **Risk:** Accuracy only.

**T16 · Before/after split (contrast)** [B][H]
- **Why:** Contrast makes differences salient [83], and loss framing adds weight [55]. It's also a current meme template ("high vs low cortisol", 2026) [136].
- **Do:** Split into **top/bottom** halves (not left/right, because the right rail covers the right side) for 2–4 s. Top: "Farmando na mão" with a red tint, error buzzer and spinning clock. Bottom: "KizuBot" in purple, calm lo-fi, rising counter. Put the labels at the top of each half.
- **pt-BR:** "HIGH CORTISOL: farmando na mão 😵 / LOW CORTISOL: KizuBot farmando 24h 😌"
- **Risk:** Don't show a real competing product as the "before".

**T17 · Countdown / "espera…" anticipation** [B]
- **Why:** Dopamine neurons ramp up while a reward is uncertain, peaking at 50/50 odds [52]. With music, dopamine release happens during anticipation (caudate) and again at the peak (nucleus accumbens) [53].
- **Do:** A 3-2-1 count or radar sweep over 1.5–3 s (3–6 beats) with a riser, then 150–300 ms of near-silence, then the reveal on the downbeat with the sonic logo. Once per video.
- **pt-BR:** "Radar ligado… 3… 2… 1…" → "✨ SHINY"
- **Risk:** Never make it look like a slot machine or roulette. TikTok regulates gambling-like content [2], and betting is a sensitive topic in Brazil. Use a radar or sonar metaphor.

**T18 · Variable reveal** [B]
- **Why:** Unexpected rewards generate prediction-error signals that drive learning; fully predicted rewards don't [51]. Uncertainty sustains attention [52].
- **Do:** The bot's "found" feed pops entries at irregular intervals (0.4, 0.9, 1.1, 1.8 s): grey common loot, then one rare in gold with a sparkle and a bigger SFX. Vary both timing and value.
- **pt-BR:** "comum… comum… comum… ✨ SHINY"
- **Risk:** Show realistic frequency; never imply shinies every minute. Don't build repeated "quase!" near-misses, which is a gambling mechanic [54].

**T19 · Cut rhythm of 0.8–2 s, with variation** [B]
- **Why:** Average shot length in films fell from 8–10 s in the 1960s to 3–4 s by 2005, and the rhythm of shot lengths drifted toward a 1/f pattern that resembles natural fluctuations in attention [97]. Faster pacing raises attention up to the point of overload [94].
- **Do:** Hook shots 0.4–0.8 s, body 1.0–2.0 s, proof screenshots 1.5–2.5 s (they need reading time, §9). Vary lengths (e.g. 1.2 / 0.8 / 1.6 / 0.8 / 2.0) instead of a metronome, and cut on beats.
- **pt-BR:** n/a
- **Risk:** Never cut away from text before its reading time has elapsed.

**T20 · Beat-synced cuts** [B][A]
- **Why:** Viewers prefer more frequent alignment of musical and visual accents [96]. Audio–video offset becomes noticeable if sound leads by > 45 ms or lags by > 125 ms (ITU-R BT.1359) [117].
- **Do:** Cuts and text stamps land on beats or half-beats. Snap each visual hit to the frame *at or just before* the beat, so sound never leads. Make durations whole bars: 15 s @ 128 BPM = 8 bars, 20 s @ 144 = 12, 25 s @ 153.6 = 16, 30 s @ 128 = 16.
- **pt-BR:** n/a
- **Risk:** None.

**T21 · SFX on every visual change, varied** [B]
- **Why:** SFX, production effects and jingles all trigger orienting responses. Repeated identical production effects and jingles habituate; voice changes don't [95].
- **Do:** Every entrance, cut and counter step gets a sound. Rotate 3–5 variants per SFX family (different sample, ±2 semitones). Density: 2–4 SFX/s in the hook, 1–2/s in the body.
- **pt-BR:** n/a
- **Risk:** Clutter. Leave silence before reveals (T17).

**T22 · One-word kinetic emphasis (isolation effect)** [B]
- **Why:** An isolated, distinctive item is remembered better (von Restorff) [70]. Signaling key words reduces cognitive load [92].
- **Do:** In each card, one word turns gold or lime and scales 1.15–1.3× (`back.out(2)`, 0.2 s) with a tick SFX. Never more than one emphasized word per card.
- **pt-BR:** "Seu farm **para** quando você dorme."
- **Risk:** None.

**T23 · Burned-in text for sound-off viewers** [C]
- **Why:** 69% of US adults watch sound-off in public, and 80% say they're more likely to finish a video with captions [110].
- **Do:** The story must work muted. Every audio-only beat needs a text or visual equivalent (a vibration icon plus "bzz"). With voiceover, caption it in 2–4-word chunks synced to the voice.
- **pt-BR:** n/a
- **Risk:** Don't stack long verbatim voiceover text in big blocks (redundancy overload) [92].

**T24 · Cognitive-load budget: one idea per screen** [B]
- **Why:** Working memory is limited [91]. Multimedia messages work better when extraneous material is cut, key words are signaled and content is segmented [92]. Fast pacing on top of dense information leads to overload [94], and fast-paced videos produce fragmented gaze patterns [109].
- **Do:** One claim per card. ≤ 6 words for hooks, ≤ 8 for body cards. At most 2 moving elements at once. Strip UI mockups of ~70% of the real interface chrome and zoom to the relevant row.
- **pt-BR:** n/a
- **Risk:** None.

**T25 · Center-locked composition** [B]
- **Why:** In vertical video, centered subjects get longer fixations and fewer eye jumps, so they're processed better [108].
- **Do:** Keep the hero at x = 540. Transitions move *through* the center (push-in, zoom) rather than across edges. Put the next key element where the eye already is ("match on attention").
- **pt-BR:** n/a
- **Risk:** None.

### C. Emotion and reward

**T26 · Anticipation → drop** [B]
- **Why:** Music produces dopamine release in two phases: during anticipation and at the peak [53].
- **Do:** Two bars of build (riser, filtered drums, the on-screen element rising in pitch or scale), one beat of silence, then the drop together with the reveal, the sonic logo, a 6 px / 0.2 s camera shake and particles. Place the drop at 35–55% of runtime.
- **pt-BR:** "…e aí o zap tocou" → DROP → "BOSS NASCEU"
- **Risk:** No loud jump-scares (they trigger complaints and skips).

**T27 · Peak–end engineering** [B]
- **Why:** People remember an experience mostly by its peak and its end, largely ignoring duration; this holds for film clips too [62][63].
- **Do:** One clear emotional peak (the reveal) and a satisfying end (resolution, calm logo, loop seam). The final 1.5–2 s should be positive and simple. End on the outcome ("e você acorda com isso"), with the price as supporting text, not as the last word.
- **pt-BR:** "Você dorme. Ele farma. ✨"
- **Risk:** None.

**T28 · Loss aversion** [B]
- **Why:** Losses loom larger than equivalent gains (prospect theory) [55]. A meta-analysis of 607 estimates puts the loss-aversion ratio at ≈ 1.96 [56].
- **Do:** Frame what gets lost while AFK. Visual: a sparkle that "despawns" while a clock ticks. Then switch to the gain frame for the solution.
- **pt-BR:** "Cada noite AFK é um shiny que passa batido."
- **Risk:** Don't inflate the odds, and don't guilt-trip kids.

**T29 · FOMO (only when true)** [B]
- **Why:** Fear of missing out is a measurable motivational state tied to social-media use [57]. KizuBot's alarm genuinely solves "missing the spawn".
- **Do:** A map ping plus a timer showing how long the spawn stays: "O shiny nasce. Você tá dormindo. Quem tem alarme pega."
- **Risk:** No artificial urgency ("só hoje") unless it's true. Pressuring minors through FOMO can be abusive advertising [141][139].

**T30 · Humor through benign violation (zoeira)** [B]
- **Why:** Something is funny when it's a violation that also feels benign [74]. A meta-analysis finds humor raises attention and ad liking but can lower credibility [75]. Brazilian online humor runs on self-deprecating zoeira [137].
- **Do:** Self-deprecating player pain (falling asleep on the keyboard, "acordei e o shiny já tinha ido embora 💀"), absurd exaggeration ("meu bot tem mais aura que eu"). Keep the proof segments serious to protect credibility.
- **pt-BR:** "Eu: vou dormir 5 minutinhos. O shiny: 👋"
- **Risk:** Never joke at the expense of real people, minorities or PXG staff, and never reuse footage from real memes.

**T31 · Nostalgia cues** [B]
- **Why:** Nostalgia increases social connectedness and willingness to pay [76]. 62.6% of Brazilian players revisit old games [122].
- **Do:** 8-bit chiptune blips for loot, a pixel font for small labels, a CRT-scanline transition, and a greenish "old handheld" palette for the "old way" segment, contrasted with the modern purple KizuBot UI.
- **pt-BR:** "Do macro no teclado… pro farm na nuvem."
- **Risk:** Don't copy Nintendo or Game Boy trademarks, boot sounds or Pokémon music [144][145].

**T32 · ASMR / satisfying micro-motion** [B][A]
- **Why:** ASMR-type stimuli produce reliable relaxation and positive-affect changes [77]. Meta lists ASMR and sound effects among its Reels creative essentials [39].
- **Do:** Counters that tick precisely (30 ms click per step), cards snapping into a grid with soft clacks, loot stacking perfectly, bars filling with `power2.inOut`. Use these in the "while you sleep" segment at a calm 80–90 BPM.
- **pt-BR:** "Enquanto isso… 🤫" over smoothly stacking loot.
- **Risk:** None.

**T33 · Micro-story / narrative transportation** [B][A]
- **Why:** Being transported into a story increases persuasion [85], confirmed across 132 effect sizes [86]. Almost half of TikTok's best-performing auction ads use emotional storylines [3]. Slice-of-life scenes give 1.5× on Reels [40].
- **Do:** Setup (night, 0–2 s) → conflict (spawn while you sleep, 2–5 s) → turn (alarm, 5–8 s) → resolution (captured, 8–12 s) → tag (CTA). Use precise timestamps ("03:12") and sensory detail (vibration, screen lighting up).
- **pt-BR:** "03:12. Eu dormindo. O zap: '✨ SHINY detectado'."
- **Risk:** A real customer story needs consent. A fictional one must not be presented as a testimonial.

**T34 · Tribe language and meme formats** [B][H]
- **Why:** Cues that fit a group identity make an action feel "for people like me" [73]. Gaming slang is now mainstream in Brazil [131][132].
- **Do:** 1–2 slang tokens per video at most ("farmar", "upar", "drop", "AFK", "duo", "amassou", "buffado"). Reuse current meme *formats* (POV, high vs low cortisol, farmar aura, "tipos de jogador", "meme Dexter" certainty) as structure only. Check freshness weekly.
- **pt-BR:** "Enquanto você farma aura, o KizuBot farma shiny."
- **Risk:** Overdone slang reads as "cringe 2.0" [132]. Never use real people's likeness or footage from memes [2].

### D. Persuasion and conversion

**T35 · Social proof (real)** [B]
- **Why:** Telling people what peers like them do changes behavior (hotel-towel field experiment) [58].
- **Do:** Three real customer alert screenshots (nicknames blurred) stacking like a feed, 0.5 s each, then a real counter: "{N} jogadores de PXG usando (set/2026)". Use "jogadores como você" framing.
- **pt-BR:** "Isso chegou no zap de 3 clientes só essa semana."
- **Risk:** Get consent. Don't crop or reorder screenshots in a way that changes their meaning (TikTok counts that as "significantly edited") [2]. TikTok also bans fake reviews [2]. Follow CONAR's testimonial rules [142].

**T36 · Authority through demonstrated competence** [B]
- **Why:** Authority cues increase compliance (Cialdini), and precise data signals competence [107].
- **Do:** Show real dashboard metrics (uptime %, hours farmed, alerts sent), a version number or a changelog snippet. "Feito por quem joga PXG desde {ano}" only if true.
- **pt-BR:** "Uptime de {x}% em setembro. Print real do painel."
- **Risk:** No fake experts, and no implied endorsement by PXG staff or streamers without a contract.

**T37 · Anchoring + price reframing** [B]
- **Why:** An initial number biases later estimates [60]. Reframing a cost as "pennies a day" makes people compare it to small daily expenses [61].
- **Do:** Anchor on the time cost first ("30 noites × 8h = 240h de farm"), then the price ("R$ 250/mês"), then the reframes: "≈ R$ 8,33/dia" and "≈ R$ 0,35 por hora de bot ligado". Use a count-up or flip animation, and hold the final price ≥ 1.2 s.
- **pt-BR:** "Menos de R$ 9 por dia. Uns 35 centavos por hora de farm."
- **Risk:** Do the math honestly (30-day month, 720 h), state that it's a monthly plan, and avoid misleading comparisons.

**T38 · Scarcity (only if real)** [B]
- **Why:** People value scarce items more (cookie-jar experiment) [59].
- **Do:** Only real constraints, e.g. per-server capacity backed by data. Otherwise lean on the *game's* real scarcity: shinies are rare. That's a game fact, not sales pressure.
- **pt-BR:** "Shiny é raro. Perder um dói mais ainda."
- **Risk:** Fake countdowns or "últimas vagas" are misleading advertising (CDC art. 37) [141]. ECA Digital bans interfaces designed to compromise minors' autonomy [139].

**T39 · Ownership language (endowment)** [B]
- **Why:** People value what they own more than the same thing not owned [72].
- **Do:** Possessive and personalized framing: "o SEU bot", "SEU farm rodando", a dashboard labelled "Bot do {nick}".
- **pt-BR:** "Seu bot já podia estar farmando agora."
- **Risk:** Never imply the viewer already owns or has paid for anything.

**T40 · IKEA effect (show the setup)** [B]
- **Why:** People value things more when they put effort into them, provided they succeed [71].
- **Do:** A 3-step setup montage, ~1 s each: escolher rota → alvo (shiny/boss) → número do zap. Satisfying toggles and checkmarks, ending on "pronto ✅".
- **pt-BR:** "Escolhe o alvo. Coloca seu zap. Pronto."
- **Risk:** If setup is actually complex, don't make it look trivial; mismatched expectations lead to refunds.

**T41 · Commitment ladder (micro-yes)** [B]
- **Why:** Agreeing to something small increases agreement with a larger request later (foot-in-the-door) [88].
- **Do:** 2–3 rhetorical yes-questions, ~0.6 s each, each ticking a ✅ box: "Já perdeu shiny dormindo? / Já deixou o PC ligado a noite toda? / Já acordou e o boss já tinha caído?" Then the solution.
- **pt-BR:** (as above)
- **Risk:** Keep the questions rhetorical and don't use them to pressure minors.

**T42 · Reciprocity (give value first)** [B]
- **Why:** A small unsolicited favor increases compliance with a later request [89].
- **Do:** Open the body with one genuinely useful PXG farming tip that doesn't need the bot, or offer a free checklist delivered by DM.
- **pt-BR:** "Dica grátis: anota o horário dos teus spawns. Se você não tiver acordado, o bot anota por você."
- **Risk:** The tip must be accurate.

**T43 · Ben Franklin effect / genuine comment prompts** [B][A]
- **Why:** Asking someone for a small favor can increase their liking for you [90].
- **Do:** Ask an easy question whose answer you'll actually use: "Qual alarme a gente coloca no próximo update: mega ou boss?" Pin the answer, then ship it.
- **pt-BR:** "Vota aí: próximo alarme é mega ou boss? 👇"
- **Risk:** TikTok makes "like-for-like" and false incentives FYF-ineligible [2], and Instagram won't recommend explicit engagement bait [32]. The question has to be real.

**T44 · Rhyme and fluency in slogans** [B]
- **Why:** Easy-to-process messages are liked more [68]. Rhyming sayings are judged more accurate (rhyme-as-reason effect) [69].
- **Do:** A 3–5-word rhyming or rhythmic tagline on the end card.
- **pt-BR:** "Você dorme. Ele farma." · "Shiny apareceu? O zap avisou." · "PC desligado, farm ligado."
- **Risk:** Rhyme isn't proof. The slogan can't carry a factual claim you can't back up.

### E. Brand and memory

**T45 · Distinctive brand assets + mere exposure (dynamic branding)** [B][C]
- **Why:** Repeated exposure increases liking [64][65]. Distinctive assets need both fame and uniqueness [66]. Meta/Toluna (Reels, Dec 2025): brand + message within 5 s → 1.7×; dynamic branding in varied positions → 1.8×; brand presence capped at ~25% of runtime → 4.8× (direct response) [40].
- **Do:** A brand cue by 2 s (small "KizuBot" chip in the hook band, or the mascot). Bring it back 2–3 times in different places (dashboard header, alert sender name, end card). Total on-screen brand time ≤ 25% of runtime. Same font, purple, mascot and sonic logo in every video.
- **pt-BR:** Alert sender name shown as "KizuBot 🤖".
- **Risk:** Overbranding kills retention.

**T46 · Sonic logo** [C]
- **Why:** Ipsos's analysis of 2,000+ ads found audio brand assets on average more effective than some visual ones [67]. A consistent sound becomes a distinctive asset [66].
- **Do:** The "Kizu ping" (spec in §8) plays only at the reveal and on the end card (≤ 2× per video), always identical.
- **pt-BR:** n/a
- **Risk:** It must not resemble the WhatsApp notification or any other brand's sound [45].

**T47 · Color system: purple + accents** [B]
- **Why:** Colors shape brand-personality impressions (red → excitement, blue → competence; purple and black lean toward sophistication in these studies) [79]. Effects depend on context and the evidence is modest [80].
- **Do:** Purple for brand plates and glows; gold = shiny/rare; lime = alert/active; red only for "pain / manual". Use white or near-black on these colors. Purple is common in Brazil (Nubank, Twitch), so distinctiveness has to come from the *combination*: purple + gold + mascot + ping.
- **pt-BR:** n/a
- **Risk:** Contrast checks in §9 (purple text on a dark background fails).

**T48 · Picture superiority (show, don't tell)** [B][C]
- **Why:** Pictures are remembered far better than words; recognition stayed high even after 10,000 pictures [84]. Meta/Toluna: product + context → 5.3×, product shown multiple times → 2.7× (direct response) [40].
- **Do:** Every claim gets a visual proof (alert screenshot, dashboard, counter). Show the product in context (phone on the nightstand at 3 a.m.) at least twice.
- **pt-BR:** n/a
- **Risk:** Mockups must match the real product UI.

**T49 · Seamless loop ending** [A]
- **Why:** Replays count as views and add watch time on all three platforms [17][28][37], and loops can push average percentage viewed above 100% [28].
- **Do:** The last 0.5 s morphs into frame 0: same background, same element positions. The final text line completes into the hook ("…e é por isso que eu não farmo mais na mão" → "Você ainda farma na mão?"). Musically, the last bar resolves into the first bar's downbeat; render the audio as a loop with the reverb tail mixed into the head.
- **pt-BR:** see above.
- **Risk:** Don't bury the CTA. Place it at 70–90% of runtime, with the loop seam after it.

---
## 5. Twenty hook templates in pt-BR

Rules for every hook: on screen by 0.1 s · ≤ 6 words per card (split longer templates into 2 cards at 0.00 and ~0.8 s) · one accent word · SFX on entry · the claim must be true and paid off inside the video. **Every number, time and count in the examples below is a placeholder.** Replace it with logged data before rendering.

| # | Template (fill the {slots}) | Filled example | Mechanism |
|---|---|---|---|
| 1 | "Você ainda {ação manual} em {ano}?" | "Você ainda farma na mão em 2026?" | Self-referencing question [103][106] + mild contrarian [101] |
| 2 | "{N}h{MM} de {farm} enquanto você {dormia}" | "9h12 de farm enquanto você dormia" | Result first [105] + precise number [107] |
| 3 | "O {shiny} nasceu às {hh:mm}. Eu tava {dormindo}." | "O shiny nasceu às 03:12. Eu tava dormindo." | Micro-story [85] + loss [55] + open loop [50] |
| 4 | "Para de perder {raro} por estar {AFK}." | "Para de perder shiny por estar AFK." | Negative frame [101][102] + loss aversion [56] |
| 5 | "POV: são {hora} e seu celular vibra" | "POV: são 3h e seu celular vibra 📳" | POV / self-reference [106] + sound onset [95] |
| 6 | "Desliguei o {PC}. O {farm} não parou." | "Desliguei o PC. O farm não parou." | Schema violation [87] + curiosity gap [47] |
| 7 | "{A}: high cortisol. {B}: low cortisol." | "Farmar na mão: high cortisol. KizuBot: low cortisol." | 2026 meme format [136] + contrast [83] + humor [74] |
| 8 | "Enquanto você farma aura, {ele} farma {shiny}." | "Enquanto você farma aura, o KizuBot farma shiny." | Trend hijack [131] + wordplay/fluency [68] |
| 9 | "{3} sinais de que você precisa {solução} (o {3º} dói)" | "3 sinais de que você precisa de um bot de farm (o 3º dói)" | Numbered list [98] + open loop [50] |
| 10 | "Calculei quanto {tempo} eu perco {farmando na mão}" | "Calculei quantas horas eu perco farmando na mão" | Precise number reveal [107] + loss [55] |
| 11 | "{R$ 0,35} por hora de {farm}. Sério." | "R$ 0,35 por hora de farm. Sério." | Anchoring / pennies-a-day [60][61] + surprise [51] |
| 12 | "Esse {alarme} me salvou {N} {shinies}." *(real customer, with consent)* | "Esse alarme salvou {N real} shinies de um cliente." | Result + social proof [58] |
| 13 | "Seu {farm} para quando você {dorme}. O dele não." | "Seu farm para quando você dorme. O dele não." | Contrast + loss [55] + ownership [72] |
| 14 | "Se você joga {PXG}, {para} {10} segundos." | "Se você joga PXG, para 10 segundos." | In-group call-out [73] + direct address [4] |
| 15 | "Isso é o que acontece em {24h} de {farm automático}:" | "Isso é o que acontece em 24h de farm automático:" | Process curiosity [47] + anticipation [53] |
| 16 | "Você dormiria se soubesse que {um boss} vai nascer hoje?" | "Você dormiria se soubesse que um boss vai nascer hoje?" | Question [103] + FOMO (true) [57] |
| 17 | "Erro nº1 de quem {caça shiny}:" | "Erro nº1 de quem caça shiny:" | Negative frame [101] + curiosity gap [47] |
| 18 | "Deixei o {bot} ligado {7 dias}. Resultado:" *(real data only)* | "Deixei o KizuBot ligado 7 dias. Resultado:" | Experiment + result tease [105] + precision [107] |
| 19 | "O zap tocou. Era {BOSS}." | "O zap tocou. Era BOSS. 🔥" | Four-word story [85] + sound onset [95] + pattern interrupt [93] |
| 20 | "Tipos de jogador quando {o shiny nasce às 3h}:" | "Tipos de jogador quando o shiny nasce às 3h:" | Identity [73] + zoeira humor [74][137] |

---

## 6. Fifteen retention structures (beat-by-beat)

Every structure runs on a bar grid, so durations loop musically (§8): **15 s @ 128 BPM** (bar = 1.875 s, 8 bars) · **20 s @ 144 BPM** (bar = 1.667 s, 12 bars) · **25 s @ 153.6 BPM** (bar = 1.5625 s, 16 bars). Text goes in the hook band, UI and proof in the body box (§3). `{x}` = slot for real data. Each structure follows *hook → re-hook → peak at 35–55% → proof/CTA → loop seam*.

### 15-second formats (128 BPM)

**R01 · Resultado primeiro → loop** (reach) — T03 · T04 · T26 · T49
```
t(s)   bar BEAT       VISUAL                                          TEXT (pt-BR)                             AUDIO
00.00  1   HOOK       Phone on nightstand lights up; real alert card  "Acordei com isso no zap 👇"              buzz-buzz + downbeat (funk groove)
01.88  2   CONTEXT    Dark room, clock 03:12, "você 💤"                 "03:12. Eu dormindo."                     drums out, pad + clock tick
03.75  3   HOW        Dashboard: farm / captura / pesca counters      "O KizuBot farma, captura e pesca"        drums back, tick per counter step
05.63  4   RE-HOOK    Gold flash, radar starts sweeping               "E se vier BOSS?"                         riser (1 bar)
07.50  5   PEAK       Radar → "🔥 BOSS" + mascot eyes look at alert     "Alarme no WhatsApp na hora"              1-beat gap → DROP + Kizu ping
09.38  6   PROOF      2 more real alerts stack (nicks blurred)        "Prints reais de clientes"                full groove
11.25  7   CTA        Price chip in body box                          "R$ 250/mês ≈ R$ 8,33/dia · link na bio"  groove + fill
13.13  8   LOOP SEAM  Zoom back to phone (= frame 0), screen dims      "…e você acordando com isso"              last bar resolves into bar 1
```

**R02 · High vs low cortisol** (reach + shares) — T16 · T30 · T34
```
00.00  1   HOOK       Top/bottom split: red HIGH / purple LOW         "Farmar na mão 😵 vs KizuBot 😌"           stinger + groove
01.88  2   TOP        Top: spinning clock, red eyes, error buzzer     "03h, olho aberto, zero shiny"            buzzer, tense pad
03.75  3   BOTTOM     Bottom: 💤 + counters climbing; top dims          "Dormindo. Farm rodando."                 switch to half-time lo-fi
05.63  4   RE-HOOK    Alert falls into bottom half; top misses it     "O shiny nasceu…"                         riser
07.50  5   PEAK       Bottom: "✨ SHINY capturado"; top: "💀"            "…e só um viu"                            DROP + Kizu ping
09.38  6   PUNCH      Full-screen "low cortisol" meme card            "Você dorme. Ele farma."                  groove
11.25  7   CTA        Brand chip + small price line                   "KizuBot · link na bio"                   groove
13.13  8   LOOP SEAM  Split re-forms exactly as frame 0               —                                         resolve to bar 1
```

**R03 · "Para de…" problem → fix** (conversion) — T06 · T28 · T37
```
00.00  1   HOOK       ❌ strike-through over "farmar na mão"            "Para de perder shiny por estar AFK."     impact + groove
01.88  2   AGITATE    Count-up 0 → 30 nights                          "30 noites AFK = 30 chances perdidas"     error ticks
03.75  3   SOLVE      Dashboard + alarm toggles (shiny/mega/boss)     "Alarme no zap: shiny, mega, boss"        toggle clicks
05.63  4   RE-HOOK    PC icon powers off; cloud keeps running         "E o PC? Desligado. Roda na nuvem."       power-down + whoosh
07.50  5   PEAK       Real alert screenshot                           "Print real ✅"                            DROP + Kizu ping
09.38  6   PRICE      "R$ 250/mês" flips to "≈ R$ 8,33/dia"           (as shown)                                flip SFX
11.25  7   CTA        Link/zap chips                                  "Link na bio · chama no zap"              groove
13.13  8   LOOP SEAM  ❌ re-forms over "farmar na mão"                 —                                         resolve
```

**R04 · Radar countdown** (suspense) — T17 · T18 · T26
```
00.00  1   HOOK       Center radar sweeping                           "Deixei o bot procurando shiny. Espera…"  sonar ping on each beat
01.88  2   VARIABLE   Finds pop at irregular times: grey commons      "comum… comum…"                           soft ticks
03.75  3   CONTEXT    Clock races 22:00 → 03:00, "você 💤"             "Enquanto eu dormia"                      half-time
05.63  4   RE-HOOK    Radar turns gold, 3-2-1                         "3… 2… 1…"                                riser + 0.3 s silence
07.50  5   PEAK       "✨ SHINY" + phone buzz + alert card              —                                         DROP + Kizu ping
09.38  6   EXPLAIN    Feature chips                                   "Farma, captura, pesca 24/7 + alarme no zap"  groove
11.25  7   CTA        Brand + link chip                               "Link na bio"                             groove
13.13  8   LOOP SEAM  Radar back to sweeping (= frame 0)              —                                         resolve
```

**R05 · Mito vs fato** (objection handling) — T08 · T07
```
00.00  1   HOOK       Red "MITO:" stamp                               "MITO: sem PC ligado não tem farm"        stamp SFX
01.88  2   BUST       Stamp flips green "FATO:"                       "FATO: o farm roda na nuvem"              flip SFX
03.75  3   SHOW       PC shutdown (CRT collapse), cloud counters keep going  "PC desligado 🔌 → farm ligado ☁️"   power-down, ticks
05.63  4   RE-HOOK    Second myth stamp                               "MITO 2: alarme só no PC" → "FATO: chega no WhatsApp"  stamp + flip
07.50  5   PEAK       Phone receives alert                            —                                         DROP + Kizu ping
09.38  6   PROOF      Hours count-up 0 → {9h12} (real)                "{9h12} de farm numa noite"               fast ticks
11.25  7   CTA        Link chip                                       "Link na bio"                             groove
13.13  8   LOOP SEAM  "MITO:" stamp returns                           —                                         resolve
```

### 20-second formats (144 BPM)

**R06 · 3 sinais** (list) — T15 · T12 · T14
```
00.00  1   HOOK       Two cards (0.00 / 0.83)                         "3 sinais de que…" / "…você precisa de um bot de farm"  impact, whoosh
01.67  2   PROMISE    3 empty slots + XP bar appears                  "(o 3º dói 💀)"                            3 ticks
03.33  3   ITEM 1     Fan icon roaring, PC on all night               "1/3 · Teu PC fica ligado a noite toda"   fan whir
05.00  4   ITEM 2     Clock + 💀 + "boss já caiu"                       "2/3 · Você acorda e o boss já caiu"      sad blip
06.67  5   RE-HOOK    Slot 3 shakes                                   "Mas o 3º…"                               riser
08.33  6   ITEM 3     Sparkle despawns                                "3/3 · O shiny nasceu e você dormia"      despawn SFX
10.00  7   PEAK       Dashboard + alert, XP 100%                      "KizuBot: farma 24/7 e te avisa no zap"   DROP + Kizu ping
13.33  9   PROOF      Real alert screenshot (nick blurred)            "Print real de cliente ✅"                 buzz
16.67  11  CTA        Link + price chip                               "Link na bio · ≈ R$ 8,33/dia"             groove
18.33  12  LOOP SEAM  Slots empty again (= frame 0)                   —                                         resolve
```

**R07 · 24h em 20 s (time-lapse)** — T07 · T32 · T13
```
00.00  1   HOOK       Clock 00:00                                     "24h de farm automático em 20s:"          clock tick, groove
01.67  2   NIGHT      00:00–06:00 time-lapse, moon, counters climb    —                                         lo-fi half-time
05.00  4   RE-HOOK 1  03:12 phone buzz, shiny alert                   "03:12 ✨ SHINY"                           Kizu ping
06.67  5   MORNING    06:00–12:00, "você na escola/trampo"             "Você fora. Ele farmando."                groove returns
10.00  7   RE-HOOK 2  14:40 boss alert                                "14:40 🔥 BOSS"                            impact
11.67  8   EVENING    Catch list stacking (satisfying)                —                                         soft clacks
15.00  10  SUMMARY    Big real numbers                                "24h: {x} capturas · {y} peixes · {z} alertas"  count-up ticks
16.67  11  CTA        Link chip                                       "Link na bio"                             groove
18.33  12  LOOP SEAM  Clock rolls 23:59 → 00:00 (= frame 0)           —                                         resolve
```

**R08 · Calculadora** (anchoring) — T37 · T07 · T28
```
00.00  1   HOOK       Calculator UI                                   "Quanto custa farmar 24/7?"               key clicks
01.67  2   ANCHOR     "8h/noite × 30 noites = 240h acordado"          "Na mão? Impossível 💀"                    calc ticks, buzzer
05.00  4   RE-HOOK    Bed icon + cloud                                "E se o farm não dormisse?"               riser
06.67  5   PRICE      Display shows price                             "KizuBot: R$ 250/mês"                     cash-register blip
08.33  6   REFRAME 1  Flip                                            "= R$ 8,33 por dia"                       flip
10.00  7   PEAK       Count down to per-hour price                    "= R$ 0,35 por hora de bot ligado"        DROP + Kizu ping
13.33  9   VALUE      Included feature chips                          "Farma · captura · pesca · alarme no zap" 4 ticks
16.67  11  CTA        Pix + link chips                                "Paga no Pix · link na bio"               groove
18.33  12  LOOP SEAM  Calculator clears (= frame 0)                   —                                         resolve
```

**R09 · POV madrugada** (story) — T09 · T33 · T26
```
00.00  1   HOOK       Dark screen, phone vibrates                     "POV: 3h da manhã e seu celular vibra"    buzz + heartbeat
01.67  2   TENSION    Blurred notification                            —                                         heartbeat, riser
03.33  3   REVEAL 1   Alert from "KizuBot 🤖"                          "✨ SHINY detectado"                       Kizu ping
05.00  4   RE-HOOK    Thumb moves toward the notification             "Mas o melhor…"                           1-beat gap
06.67  5   PEAK       {real next step: bot action or "você abre e pega"}  "{…ele já tá {ação real}}"             DROP
10.00  7   RELIEF     Back to sleep; counters keep ticking (ASMR)     "Volta a dormir. Ele segue."              lo-fi
13.33  9   MORNING    Summary card                                    "Acordei com isso:"                       morning chime
16.67  11  CTA        Link chip                                       "Link na bio"                             groove
18.33  12  LOOP SEAM  Screen fades to dark (= frame 0)                —                                         resolve
```
*Only show automatic capture if the bot really does it after the alert; otherwise show the player opening the game.*

**R10 · Prova social em pilha** — T35 · T48 · T45
```
00.00  1   HOOK       Feed of alerts begins                           "Chegou no zap dos clientes essa semana:" buzz + groove
01.67  2   STACK 1    Real alert 1 (blurred) + date                   "seg 02:14"                               buzz
03.33  3   STACK 2    Real alert 2                                    "qua 05:40"                               buzz
05.00  4   RE-HOOK    Real alert 3 (BOSS)                             "sex 🔥 BOSS"                              impact
06.67  5   BUILD      Count-up starts, riser                          "Quantos alertas em setembro?"            riser + fast ticks
08.33  6   PEAK       Counter lands on the real total                 "{N} alertas enviados em set/2026"        DROP + Kizu ping
11.67  8   HOW        Dashboard                                       "Farma, captura e pesca na nuvem"         groove
13.33  9   TAGLINE    Slogan card                                     "Você dorme. Ele farma."                  groove
16.67  11  CTA        IG: comment-keyword · TikTok/Shorts: bio link   "Comenta KIZU 📩" / "Link na bio"          groove
18.33  12  LOOP SEAM  Alerts collapse (= frame 0)                     —                                         resolve
```

### 25-second formats (153.6 BPM)

**R11 · Experimento 7 dias** (case study) — T07 · T13 · T36
```
00.00  1   HOOK       Two cards                                       "Deixei o KizuBot ligado 7 dias." / "Resultado:"  impact
01.56  2   RULES      7-day calendar                                  "Regra: não toquei no jogo"               ticks
03.13  3   DAY 1–2    Counters                                        "Dia 1: {x} capturas"                     groove
06.25  5   RE-HOOK 1  Alert                                           "Dia 3: o zap tocou às 04:41"             buzz + ping
07.81  6   DAY 4–5    Fishing counter, satisfying stacks              "Dia 5: {y} peixes"                       clacks
10.94  8   RE-HOOK 2  Boss alert                                      "Dia 6: 🔥 BOSS"                           impact
12.50  9   PEAK       Big totals count-up (real)                      "7 dias: {totais}"                        DROP + Kizu ping
15.63  11  HONESTY    One real limitation                             "O que não rolou: {limitação real}"       quiet bar
18.75  13  PRICE      Price reframe                                   "R$ 250/mês ≈ R$ 8,33/dia"                flip
21.88  15  CTA        Link chip                                       "Link na bio"                             groove
23.44  16  LOOP SEAM  Calendar resets to day 1                        —                                         resolve
```
*Admitting one real limitation makes the rest of the claims more believable [H]. It also prevents disappointed buyers.*

**R12 · PAS + prova** (problem–agitate–solve–proof) — T06 · T28 · T40 · T35
```
00.00  1   PROBLEM    Frozen counter at 0                             "Seu farm para quando você dorme."        impact
01.56  2   PROBLEM+   Sleeping avatar, counter frozen                 —                                         clock tick
03.13  3   AGITATE    Sparkle despawns at 03:00                       "E o shiny nasce justo às 3h"             despawn
04.69  4   AGITATE+   Count-up of nights                              "30 noites por mês"                       error ticks
06.25  5   RE-HOOK    Cut to purple                                   "Tem um jeito:"                           riser
07.81  6   SOLVE      Cloud + dashboard                               "KizuBot farma na nuvem 24/7"             groove
10.94  8   SOLVE+     3-step setup toggles                            "Rota · alvo · teu zap"                   clicks
12.50  9   PEAK       Alert arrives                                   "✨ SHINY → avisado na hora"               DROP + Kizu ping
15.63  11  PROOF      2 real customer screenshots                     "Prints reais"                            buzz ×2
18.75  13  OFFER      Price reframe                                   "≈ R$ 8,33/dia"                           flip
21.88  15  CTA        Link/zap chips                                  "Link na bio · chama no zap"              groove
23.44  16  LOOP SEAM  Frozen counter (= frame 0)                      —                                         resolve
```

**R13 · "Espera o alarme…"** (wait for it) — T17 · T18 · T14 · T27
```
00.00  1   HOOK       XP bar appears, fills fast to 40% by 6 s        "Espera o alarme tocar…"                  sonar ping
01.56  2   BUILD 1    Farm montage, counters                          —                                         lo-fi
04.69  4   RE-HOOK 1  "Alarm" for a common item (false alarm)         "comum 😐"                                 small blip
06.25  5   BUILD 2    Fishing, map, radar                             —                                         groove
09.38  7   RE-HOOK 2  Radar flickers gold once                        "quase… 👀"                                riser
10.94  8   BUILD 3    Heartbeat, screen tightens                      —                                         heartbeat + riser
12.50  9   PEAK       Phone alarm, XP 100% "LEVEL UP"                 "🔥 BOSS NASCEU"                           DROP + Kizu ping
15.63  11  HUMOR      Bathroom-door gag illustration                  "E eu tava no banho 😂"                   comedic sting
18.75  13  EXPLAIN    Feature chips                                   "Farma · captura · pesca · alarme no zap" ticks
21.88  15  CTA        Link chip                                       "Link na bio"                             groove
23.44  16  LOOP SEAM  Back to "Espera…" (= frame 0)                   —                                         resolve
```
*Use one near-miss at most (T18 risk note).*

**R14 · Tutorial em 3 passos** (IKEA effect + saves) — T40 · T15 · T42
```
00.00  1   HOOK       Setup screen                                    "Configura teu bot de farm em 3 passos"   impact
01.56  2   STEP 1     Route toggle                                    "1/3 · Escolhe a rota"                    click
04.69  4   STEP 2     Target chips                                    "2/3 · Alvo: shiny · mega · boss"         3 clicks
06.25  5   RE-HOOK    Step 3 card pulses                              "O 3º é o mais importante:"               riser
07.81  6   STEP 3     Phone field (number masked)                     "3/3 · Coloca teu zap"                    typing ticks
10.94  8   RESULT     Bot starts, counters move                       "Pronto ✅"                                success chime
12.50  9   PEAK       Test alert arrives                              "Chegou! 📲"                               DROP + Kizu ping
15.63  11  SAVE       Bookmark icon                                   "Salva pra configurar depois 🔖"          soft tick
18.75  13  PRICE      Price chip                                      "≈ R$ 8,33/dia"                           flip
21.88  15  CTA        Link chip                                       "Link na bio"                             groove
23.44  16  LOOP SEAM  Steps reset (= frame 0)                         —                                         resolve
```
*The steps must match the real setup flow.*

**R15 · Quebra-objeções** ("Mas e…?") — T05 · T37 · T35
```
00.00  1   HOOK       Quote card                                      "'Bot de farm não vale a pena' — será?"   record scratch
01.56  2   OBJ 1      PC off + cloud                                  "Mas e o PC? → Roda na nuvem"             power-down
04.69  4   OBJ 2      Alert                                           "Mas e se vier shiny? → Alarme no zap"    buzz
07.81  6   RE-HOOK    Price question                                  "Mas e o preço?"                          riser
09.38  7   OBJ 3      Flip                                            "R$ 250/mês = R$ 8,33/dia"                flip
12.50  9   PEAK       Count down                                      "= R$ 0,35 por hora de farm"              DROP + Kizu ping
14.06  10  OBJ 4      Honest answer card                              "{resposta real sobre dados/regras}"      quiet bar
18.75  13  PROOF      Real screenshots                                "Prints reais de clientes"                buzz
21.88  15  CTA        Zap + link chips                                "Chama no zap: link na bio"               groove
23.44  16  LOOP SEAM  Back to the quote card                          —                                         resolve
```
*Only include OBJ 4 ("É seguro? / dá ban?") if you can answer it truthfully and verifiably. Otherwise drop it.*

---

## 7. Ten CTA patterns in pt-BR

**Timing:** a soft CTA overlay at 60–75% of runtime; the hard CTA on the last 1–2 bars, *before* the loop seam. The CTA must fade out before the loop frame so the restart looks clean. In VidMob's TikTok data, a CTA in the opening frame correlated with +44% conversion rate [7], and including a CTA gave 1.9× in Meta/Toluna's direct-response Reels [40]. → For conversion variants, add a small brand + offer chip in the body box from 0–2 s without disturbing the hook.

| # | On-screen CTA (pt-BR) | Soft / hard | When to use | Platform notes |
|---|---|---|---|---|
| 1 | "Comenta **KIZU** que eu te mando o link 📩" | Hard (lead gen) | Instagram Reels with automated DMs; demos and offers | Allowed when it's genuine lead generation, not engagement farming [32]. Deliver the DM within minutes, and pin a comment with instructions |
| 2 | "Link na bio 👆" (add "testa grátis" only if a free trial really exists) | Hard | All platforms, final 1.5–2 s, also in the caption | TikTok bio links need a business account or ≥ 1,000 followers, and age 18+ [16]. Shorts: use channel links (no clickable links in descriptions) [26] |
| 3 | "Chama no zap: link na bio 💬" | Hard | High-intent viewers, objection-handling videos | 82% of Brazilian WhatsApp users have messaged a company and 54% have bought through it [124]. Collect numbers with explicit opt-in (LGPD) [143] |
| 4 | "Plano R$ 250/mês (≈ R$ 8,33/dia) · paga no Pix" | Hard (price) | End card on bottom-funnel or retargeting cuts | Pix is the top payment method in WhatsApp purchases (71%) [124]. Say "Pix Automático" only if you offer it [126] |
| 5 | "Salva pra configurar depois 🔖" | Soft (save) | Tutorials and setup videos (R14) | Saves signal lasting value. Keep it brief |
| 6 | "Manda pro teu duo que ainda farma na mão 😂" | Soft (share) | Humor and meme videos (R02) | Make it part of the punchline, not a demand. Instagram won't recommend explicit share bait [32] |
| 7 | "Qual shiny você mais perdeu? 👇" | Soft (conversation) | Story videos (R09, R01) | Answer comments with video replies, which become new content. It has to be a real question [2] |
| 8 | "Segue pra ver o próximo alarme 🔔" | Soft (follow) | Series ("Diário do bot, dia 3/7") | Followers may gate early distribution (widely reported on TikTok, unconfirmed [13]). Build a real audience; never buy one, since TikTok removes inflated metrics [2] |
| 9 | "Vídeo completo no canal ▶️" | Soft–medium | YouTube Shorts that tease a long demo | Use the Shorts "Related video" link [26] |
| 10 | "Vota aí: próximo alarme é mega ou boss?" | Soft (Ben Franklin) | Community and roadmap posts | Only if you act on the result. Rigged polls count as engagement bait [2][32] |

---
## 8. Audio design rules

### 8.1 What the evidence says
- **Sound is a main channel on these platforms.** 88% of TikTok users call sound essential and 73% say they'd stop and look at a TikTok ad with sound (Kantar) [6]. More than 75% of Reels views are sound-on [39]. Google reports sound lifts Shorts-ad conversions by more than 20% [19]. Meta/Toluna: audio + visual cues → 1.8× brand interest; speech + music → 2.0× [40].
- **Original audio helps.** In VidMob's TikTok data, custom/original audio correlated with +52% 6-s view rate, music-only audio with +51% 6-s view rate (awareness), and music + narration with 2× conversion rate [7].
- **Tempo drives arousal; mode (major vs minor) drives mood** [78]. TikTok: "fast-paced tracks above 120 BPM … often drive higher view-through rate" [3].
- **Build–gap–drop.** Dopamine is released during musical anticipation and again at the peak [53], so the reveal should land on a drop that follows a riser and a short gap.
- **Orienting and habituation.** SFX, production effects and jingles grab attention. Repeating the same production effect or jingle wears out; voice changes don't [95].
- **Sync tolerance.** Viewers prefer frequent audio-visual sync [96]. Never let audio lead the picture by more than 45 ms; it may lag by up to ~125 ms before anyone notices (ITU-R BT.1359) [117].

### 8.2 BPM by emotion (all synthesized, original)

| Emotion / segment | BPM | Synth recipe | Use for |
|---|---|---|---|
| Calm, satisfying, "enquanto você dorme" | 70–95 | Lo-fi FM keys, vinyl noise, soft kick, sidechained pad | ASMR stacking, night scenes (T32) |
| Curiosity / suspense | 85–110, or a half-time feel over 140–155 | Sparse pulse, filtered drums, 1–2-bar noise riser, 60–70 bpm heartbeat | Open loops, radar scans (T04, T17) |
| Zoeira / comedy | 100–130 | Bouncy plucks, brega-funk-style syncopation, cartoon stings | Memes, "tipos de jogador" (T30) |
| Hype, flex, reveal | 128–155 | Funk-150-style tamborzão pattern (syncopated kick/snare + atabaque-like percussion), 808 sub, an original phonk-style cowbell motif, distorted bass | Shiny / boss drops (T26) |
| Urgency (real deadlines only) | 150–170, hats going 1/16 → 1/32 | Snare roll, rising pitch | Countdowns (T17) |
| Nostalgia | Any tempo | Square/triangle/noise channels (chiptune), 8-bit arpeggios | "Old way" segments, loot blips (T31) |
| Pain / "farm na mão" | Same tempo, minor or diminished | Detuned, low-passed, error buzzer | Before-states (T06, T16) |

### 8.3 Beat grid: audio is the master clock

| BPM | Beat (s) | Bar (s) | Frames/beat @ 30 fps | @ 60 fps | Durations that loop on whole bars |
|---|---|---|---|---|---|
| 120 | 0.500 | 2.000 | 15 | 30 | 16 s (8 bars) · 20 s (10) · 24 s (12) |
| 128 | 0.469 | 1.875 | 14.06 | 28.13 | **15 s (8)** · 22.5 s (12) · **30 s (16)** |
| 144 | 0.417 | 1.667 | 12.5 | 25 | **20 s (12)** · 26.7 s (16) |
| 150 | 0.400 | 1.600 | 12 | 24 | 16 s (10) · 19.2 s (12) · 25.6 s (16) |
| 153.6 | 0.391 | 1.5625 | 11.72 | 23.44 | **25 s (16)** |

- Render the music first, then drive the GSAP timeline from audio time (`tl.seek(frame / FPS)`). Never let animation time drift from audio time.
- Snap each visual hit to `Math.floor(t * FPS) / FPS` (visual at or just before the transient, so audio lags by at most one frame) [117].
- Cuts land on beats, text stamps on beats or eighth notes, and big reveals on the downbeat of a phrase.
- **Loop seam:** total length = whole bars. Render one extra bar of tail and mix it under bar 1 so the restart doesn't chop a reverb tail. No fade-out at the end.

```js
// Beat-grid skeleton (example: 15 s @ 128 BPM, 60 fps)
const BPM = 128, FPS = 60, beat = 60 / BPM, bar = beat * 4;
const q = t => Math.floor(t * FPS) / FPS;                 // visual at/just before the beat
const B = (barIdx, beatIdx = 0) => q(barIdx * bar + beatIdx * beat);

const tl = gsap.timeline({ paused: true, defaults: { ease: "expo.out" } });
tl.addLabel("hook", 0)
  .from("#hook .w", { y: 40, scale: 0.85, autoAlpha: 0, duration: 0.18, stagger: beat / 2 }, "hook")
  .addLabel("rehook", B(3))   // ≈ 5.63 s
  .addLabel("peak",   B(4))   // ≈ 7.50 s  (drop + Kizu ping already in the audio file)
  .addLabel("cta",    B(6))   // ≈ 11.25 s
  .addLabel("seam",   B(7));  // ≈ 13.13 s → morph back to the frame-0 state by 15.00 s
// Renderer: for each frame f → tl.seek(f / FPS); capture.
```

### 8.4 SFX palette and density

| Event | Recipe | Length | Notes |
|---|---|---|---|
| Text stamp / card in | Short noise burst + click (2–5 kHz) | 30–80 ms | 3–5 variants, rotated |
| Cut / transition | Whoosh (filtered noise sweep) | 120–250 ms | Alternate up and down sweeps |
| Counter tick | Soft click / wood tick | 20–40 ms | Pitch rises with the value ("satisfying") |
| Phone alarm | Vibration pulses (150–180 Hz) ×2 + your own ping | 300–600 ms | Never the real WhatsApp tone [45] |
| Shiny reveal | Sparkle shimmer (2–8 kHz arpeggio) + Kizu ping | 0.6–1.2 s | On the downbeat, after 150–300 ms of near-silence |
| Boss reveal | Sub hit (45–60 Hz) + mid punch (100–200 Hz) + noise tail | 0.5–0.8 s | The 100–200 Hz layer is what phone speakers actually reproduce |
| Error / manual pain | Dull square buzzer (200–300 Hz) | 150–300 ms | Sparingly |
| Loot (nostalgia) | 8-bit square-wave blip, 2–3 rising notes | 80–150 ms | Chiptune palette |
| Riser | White noise + pitch-up synth | 1–2 bars | Ends one beat before the drop |

**Density:** 2–4 audio events per second in the hook, 1–2 in the body. Leave 150–400 ms of "air" before each reveal. Never stack two loud transients within 100 ms. Rotate variants within every SFX family to avoid habituation [95].

### 8.5 Sonic logo: the "Kizu ping"
- Three rising notes (root → fifth → octave, e.g. E6–B6–E7) in a bright FM-bell/triangle blend with a short sparkle tail. 0.9–1.2 s total, resolving on the octave.
- Identical pitch, timbre and timing in every video, so it becomes a distinctive asset [66][67]. Use it **only** at the reveal and on the end card (≤ 2× per video) to avoid habituation [95]. Mix it 2–3 dB above the music.
- Visual pairing: the mascot's eyes flash gold on note 3, on the same frame every time.
- Before locking it, check it doesn't resemble WhatsApp, iPhone, Discord, Nintendo or Pokémon sounds [45][144].

### 8.6 Synthesized voiceover (optional)
- On TikTok, generic text-to-speech needs no AI label as long as it doesn't mimic a recognizable real person. Never clone a streamer's or any real person's voice [2].
- Rate for pt-BR: 2.6–3.2 words/s (≈ 155–190 wpm). VidMob (US English) linked VO at ≥ 4 words/s with +19% conversion [7]; treat that as an energetic upper bound and test it.
- **Awareness cuts:** music-only + text (best 6-s view rate in VidMob [7]). **Conversion cuts:** VO + music (2× conversion in VidMob [7]; speech + music 2.0× brand interest in Meta/Toluna [40]).
- Use a second voice (e.g. the mascot as the "alarm voice") for re-hooks. Voice changes re-orient attention without habituating [95].
- Caption VO in 2–4-word chunks synced to ±1 frame, highlighting the stressed word (T22).

### 8.7 Mix and loudness
- **Integrated −14 LUFS, true peak ≤ −1 dBTP** [118][119]. YouTube turns loud uploads down to its reference level but doesn't boost quiet ones [118]. TikTok and Instagram don't publish a target, so −14 LUFS is the safe common denominator.
- Duck the music 6–9 dB under VO (fast sidechain, 50–100 ms release).
- High-pass the whole mix at 30–40 Hz (phone speakers can't play it and it eats headroom). Give bass elements harmonics at 100–300 Hz so the groove survives a phone speaker.
- Audio starts at sample 0 (no silence, no fade-in) and ends without a fade-out (loop).
- Check every export on a phone speaker at 50% volume and on cheap earbuds.

### 8.8 Music direction
- A palette that feels Brazilian without licensing risk: funk 150 / mandelão (tamborzão-like syncopation, 808 sub), funk automotivo (high synth stabs), Brazilian-phonk-style cowbell lines with distorted bass, brega-funk bounce, and lo-fi for calm sections. Brazilian funk and phonk are booming on TikTok [128][129][130].
- **Never** sample real tracks or MC vocals, and never re-create a recognizable melody or hook (Content ID and copyright). Write new motifs.
- TikTok business accounts can only pick Commercial Music Library tracks in-app, so upload the original audio already mixed into the video [15]. A distinctive original track can itself become a reusable sound.

---

## 9. Reading speed and typography for pt-BR on a phone

### 9.1 Reading-speed facts
- Brazilian adults (19–35) read standardized IReST texts **aloud** at 1,100 ± 167 characters/min — about 180 wpm, ~18 characters/s, averaging 6.11 characters per word including spaces [112][113].
- Netflix's pt-BR subtitle rules: **≤ 17 cps for adults, ≤ 13 cps for children**, ≤ 42 characters per line, ≤ 2 lines, bottom-heavy pyramid. Break lines after punctuation and before conjunctions or prepositions. Never split article + noun, noun + adjective, subject + verb, or first + last name [111].
- Reading faster than normal costs comprehension; speed-reading claims don't hold up [116].
- Faster pacing and arousing content raise attention until overload [94]. In a companion experiment, as pacing and arousal increased, **verbal** recognition declined while visual recognition held up [147]. → At high pace, carry the message with visuals and numbers and keep words minimal.
- VidMob linked 5–10 *words per second* on screen with a 2.1× higher 6-s view rate [7]. That reflects energetic kinetic rhythm (usually redundant with the audio), not comprehension. Use fast word-flashes only for decorative or redundant words. Information-bearing text must respect reading time.

### 9.2 Rules for must-read text (hooks, claims, numbers, prices, CTAs)
- Budget: **≤ 15 cps for adults (≈ 2.5 words/s)**, and ≤ 13 cps when the audience skews teen.
- **Hold time = max(0.6 s, characters ÷ 15 + 0.25 s)**; use ÷ 13 for teen-skewed audiences.

| Characters (incl. spaces) | Example | Hold @ 15 cps | Hold @ 13 cps |
|---|---|---|---|
| 11 | "SHINY 03:12" | 1.0 s | 1.1 s |
| 24 | "Você ainda farma na mão?" | 1.9 s | 2.1 s |
| 24 | "R$ 250/mês ≈ R$ 8,33/dia" | 1.9 s | 2.1 s |
| 33 | "Desliguei o PC. O farm não parou." | 2.5 s | 2.8 s |
| 40 | (body-card maximum) | 2.9 s | 3.3 s |

- **Words per card:** hook ≤ 6 words (≤ ~30 characters), body ≤ 8 (≤ ~40), never more than 12 on any card. Max 2 lines (3 only for small labels inside UI mockups).
- If a sentence exceeds the budget, split it into consecutive cards on beats, or reveal it word by word with the VO and then hold the full line for ≥ 0.8 s.
- One idea per card and one emphasized word per card (T22, T24).

### 9.3 Type sizes at 1080 px wide
A 1080-px-wide video fills a phone screen roughly 390–430 points wide, so **1 iOS point ≈ 2.5–2.8 px**. Apple's minimum text size is 11 pt and its default body size is 17 pt [114].

| Role | Size in px (cap height ≈ 70% of size) | ≈ iOS pt | Notes |
|---|---|---|---|
| Absolute minimum (non-essential labels inside UI mockups) | 36–42 | 13–15 | Never for must-read information |
| Secondary text / captions | 56–72 | 20–26 | Body box |
| Main lines | 80–110 | 29–40 | Hook band or body box |
| Hook words | 120–180 | 44–65 | Hook band; about 14–16 characters per line fit at 120 px in a bold condensed face |
| Hero numbers / prices | 160–300 | 58–108 | "R$ 8,33", "9h12" |

Line capacity in the 768-px hook band (bold condensed face, average glyph ≈ 0.5 em): ~14–16 characters at 120 px, ~18–20 at 96 px, ~26–28 at 72 px. At these sizes the frame width, not Netflix's 42-character rule, is the real limit.

### 9.4 Typeface and pt-BR specifics
- Pick open-licensed families with full Portuguese diacritics (ã õ ç á é ê í ó ô ú à) and a large x-height: Inter / Inter Tight, Montserrat or Poppins for body text; Anton or Bebas Neue for 1–3-word punches.
- **Uppercase accents (Ã Õ É Ç) need vertical room.** Use line-height ≥ 1.1 for caps and ≥ 1.2 for mixed case. Check that tildes and acute accents aren't clipped by `overflow:hidden`, `clip-path` or masks in reveal animations — a common bug in kinetic type.
- Sentence case for anything longer than 3 words; ALL CAPS only for short punches.
- Tracking: 0 to +2% for large caps; never negative tracking below 72 px.

### 9.5 Contrast and legibility over screenshots and motion
WCAG 2.2 asks for 4.5:1 for normal text and 3:1 for large text [115]. Ratios for the suggested palette:

| Pair | Contrast | Verdict |
|---|---|---|
| White on purple #6D28D9 | 7.1:1 | ✅ AAA |
| Near-black #0E0A1F on gold #FFD54A | 13.7:1 | ✅ |
| Lime #A3FF12 on #0E0A1F | 15.6:1 | ✅ |
| White on #0E0A1F | 19.4:1 | ✅ |
| Lavender #C4B5FD on #0E0A1F | 10.5:1 | ✅ (secondary text) |
| Purple #7C3AED on #0E0A1F | 3.4:1 | ⚠️ large text only |
| Purple #6D28D9 on #0E0A1F | 2.7:1 | ❌ never for text |

Over busy screenshots, put text on a solid plate (purple or black at 85–92% opacity, 24–32 px radius, 24 px padding), or use a 6–10 px stroke plus a soft shadow. Dim and blur the screenshot behind the text (e.g. `filter: blur(6px) brightness(.6)`).

### 9.6 Text motion
- Entrance 120–250 ms (`expo.out` or `back.out(1.7)`), exit 80–150 ms. Text stays still (at most a 1–2% scale drift) for ≥ 70% of its time on screen.
- Only one text block moves at a time. Don't move text and background in opposite directions simultaneously.
- Avoid letter-by-letter typewriter effects for more than 3 words; reveal word by word on beats instead.
- No more than 3 flashes per second [115].

### 9.7 Numbers, currency and emoji
- "R$ 8,33" with a non-breaking space, decimal comma, dot for thousands ("1.240 alertas"), times as "03:12" or "9h12", "24/7", "3×".
- Emoji as semantic icons (✨ shiny, 📳/🔔 alarme, 💤 dormindo, 🔥 boss), 1–2 per card. Meta/Toluna: emoji gave 2.5× odds of top-tier purchase intent in direct-response Reels [40]. Render an openly licensed set into the video (e.g. Noto Color Emoji). Apple's emoji artwork is proprietary.

---

## 10. Policy-risk wording guide

### 10.1 Words to avoid → words to prefer

| Avoid | Prefer | Why |
|---|---|---|
| hack, hacker, cheat, trapaça, trapacear | automação, assistente de farm, farm automático | Google Ads prohibits "game enhancements and cheat softwares" [23]; Meta prohibits ads for products that enable cheating [41]; YouTube polices "hacking" content [21] |
| burlar, bypass, driblar anti-cheat, indetectável | (don't mention detection at all) | Implies circumventing security systems [41] |
| sem ban, anti-ban, 100% seguro, risco zero | Only verified, documented facts about the game's rules | Misleading claim → CDC art. 37 [141]; TikTok makes misleading view-boosting claims FYF-ineligible [2] |
| exploit, bug, glitch, dupar item | rotina, roteiro de farm, automação de tarefas | Exploit framing = cheating framing |
| macro, script, injetar, mod menu | "roda na nuvem", "sem instalar nada no seu PC" (only if true) | Cheat-tool vocabulary feeds classifiers |
| ganhar dinheiro, renda extra, vende o que farmar | economizar tempo, upar enquanto dorme | Real-money trading of in-game currency is "mystery value" / regulated territory on TikTok [2] and usually against game rules |
| grátis, só hoje, últimas vagas, promoção relâmpago (when not true) | Real price, real dates, "plano mensal" | Fake scarcity = misleading advertising [141] |
| garantido, todo dia vem shiny | "te avisa quando aparece", "resultados variam" | Overclaiming |
| oficial, parceiro do PXG, meme-testador-aprovado pelo PXG | (no affiliation claims unless contracted) | False endorsement / trademark |
| Pokémon, Pikachu, Poké Ball, official sprites (especially in ads) | "shiny", "mega", "boss", "PXG" (descriptive) | The Pokémon Company enforces aggressively, especially against monetized projects [144][145] |
| "IA que joga por você" as the headline | "farma 24h e te avisa no zap" (IA as a supporting detail) | Many Brazilian players are wary of AI [122] |
| #hack #cheat #trapaça #bot | #pxg #farm #shiny #afk #mmorpg #gamerbr | Hashtags feed content classifiers |

### 10.2 Never claim
- That PokeXGames allows KizuBot, or that using it carries no account risk, unless PXG has documented it.
- That it's "undetectable" or "anti-ban".
- Income or real-money gains.
- Customer numbers, results or testimonials you can't prove; fabricated or edited screenshots [2][141].
- Endorsement by streamers or PXG staff without a contract.
- Health or sleep benefits ("melhora seu sono").

### 10.3 Visual and IP rules
- No Pokémon names, sprites, logos or music in ads. In organic posts, minimize or blur them and favor abstract sparkles plus the bot's own UI [144][145].
- No WhatsApp logo in any way that suggests partnership. Write "WhatsApp" as plain text and use a generic chat UI [45].
- Blur nicknames, phone numbers and faces in screenshots, and keep written consent (LGPD) [143].
- No casino, slot, roulette or loot-box imagery. TikTok regulates gambling-like content [2], and ECA Digital bans loot boxes in games minors are likely to access (art. 20) [139].
- No real people's likeness or footage from memes, and no other creators' clips or watermarks (originality rules) [2][31][36].

### 10.4 Platform checklist
- **TikTok:** switch on "Divulgar conteúdo comercial → Sua marca" for every promotional post; undisclosed commercial content is ineligible for the For You feed [2]. No like-for-like, false giveaways or misleading view-bait [2]. DMs are 16+ only [2]. AI labels aren't needed for generic TTS or stylized graphics but are required for realistic AI people or scenes [2]. Never show or imply automating TikTok accounts, which is explicitly prohibited [2].
- **Instagram:** ≤ 3 min, no watermarks, text never covering most of the frame [31]. Comment-keyword CTAs only when a DM is genuinely delivered [32]. Original content only [36].
- **YouTube Shorts:** avoid templated near-duplicates ("inauthentic content") [20]. Links go in channel links or the Related video slot, not the description [26]. Stay away from "hacking" framing [21]. Paid product placements can't promote hacking [22].
- **Paid ads:** Google Ads explicitly lists game enhancements and cheat software as prohibited [23], Meta bans products that enable cheating or circumvent security [41], and TikTok prohibits deceptive content, scams and misleading view-boosting claims [2]. Expect disapprovals and possible account-level enforcement. → **Grow organically first.** If you test paid at all, target **18+**, position strictly as automação / qualidade de vida, and avoid any gameplay-cheat imagery [139].

### 10.5 Brazil legal checklist
- **CDC (Lei 8.078/1990) art. 37:** no misleading advertising, including by omission, and no abusive advertising, which explicitly includes exploiting a child's lack of judgment and experience [141].
- **ECA Digital (Lei 15.211/2025, in force 2026-03-17)** [139][140]:
  - Bans profiling-based targeting of commercial ads to children and adolescents (art. 22).
  - Bans loot boxes in games directed at or likely accessed by minors (art. 20).
  - Bars suppliers of products minors are likely to use from designing interfaces that compromise user autonomy (art. 18 §2).
  - Requires those suppliers to mitigate exposure to predatory, unfair or deceptive advertising practices (art. 6, V).
  - KizuBot is plausibly "likely accessed" by teens, so design the funnel accordingly.
- **CONAR:** testimonials must be genuine. Any creator partnership must be clearly identified as advertising ("publi", "publicidade") and use the platform's disclosure tools [142].
- **LGPD (Lei 13.709/2018):** WhatsApp numbers and DM leads are personal data. Get explicit consent, state the purpose, and honor opt-outs [143].

### 10.6 Pre-publish checklist (10 checks)
1. Hook readable and moving by 0.5 s, with sound on frame 0?
2. Every claim mapped to the truth sheet (top of document)?
3. All must-read text inside the safe boxes (§3) and meeting its hold time (§9)?
4. Peak between 35% and 55% of runtime; a re-hook every 5–7 s?
5. Loop seam clean (last frame → first frame, music loops on the bar)?
6. Brand by 2 s and ≤ 25% of runtime; Kizu ping ≤ 2×?
7. No banned words (§10.1); hashtags clean?
8. No Pokémon IP, WhatsApp logo, casino imagery, or unconsented screenshots?
9. TikTok commercial disclosure on; paid targeting 18+?
10. Loudness −14 LUFS / −1 dBTP, checked on a phone speaker?

---
## 11. Sources

**Platforms: TikTok**
1. TikTok Newsroom — How TikTok recommends videos #ForYou (2020). https://newsroom.tiktok.com/en-us/how-tiktok-recommends-videos-for-you
2. TikTok Community Guidelines (released 2025-08-14, effective 2025-09-13): commercial disclosure, FYF eligibility, deceptive behavior, regulated goods, AI-generated content. Official: https://www.tiktok.com/community-guidelines/en · archived full text: https://github.com/OpenTermsArchive/contrib-versions/blob/main/TikTok/Community%20Guidelines.md
3. TikTok for Business — 9 creative tips to drive auction ad performance (2020-10-21). https://ads.tiktok.com/business/en-US/blog/9-creative-tips-to-drive-auction-ad-performance
4. TikTok × CreatorIQ special report, press release (2023-12-06). https://www.creatoriq.com/press/releases/tiktok-creatoriq-release-special-report-with-data-backed-keys-to-success-for-advertisers
5. Social Media Today — TikTok marketing science on ad impact in the first 2 s / 6 s (2023-09-27). https://www.socialmediatoday.com/news/tiktok-shares-new-notes-on-how-to-maximize-ad-effectiveness-in-the-app/694989/
6. Social Media Today — Kantar × TikTok sound study (2021-06-09). https://www.socialmediatoday.com/news/tiktok-shares-new-insights-into-the-importance-of-sound-for-marketing-promo/601569
7. VidMob — 12 creative insights for better-performing TikTok ads (2020-11-09; 1,400+ ads, 5.4 B impressions). https://vidblog.vidmob.com/blog/12-creative-insights-for-better-performing-tiktok-ads
8. TikTok Ads Help — Auction In-Feed ads specifications and safe-zone templates. https://ads.tiktok.com/help/article/video-ads-specifications
9. Adkit — TikTok safe zones measured from the official overlays (updated 2026-09-10). https://adkit.so/tools/safe-zones/tiktok
10. Upload-Post — Safe-zone checker (TikTok / Reels / Shorts ad-template numbers). https://www.upload-post.com/tools/safe-zone-checker/
11. Adaptly — Social media vertical-video safe zones 2026 (organic UI measurements). https://adaptlypost.com/blog/social-media-safe-zones-2026-complete-guide
12. Meta Ads Guide — Instagram Reels video ads (14% / 35% / 6% safe zone, audio advice). https://www.facebook.com/business/ads-guide/update/video/instagram-reels
13. Socialday — Reports of TikTok "follower-first" seeding (not confirmed by TikTok). https://socialday.live/features/tiktoks-follower-first-algorithm-is-quietly-killing-reach-for-creators-with-dise
14. TikTok Newsroom — Creator Search Insights (2024-03-13). https://newsroom.tiktok.com/creator-search-insights
15. Soundstripe — Why TikTok business accounts only see the Commercial Music Library. https://www.soundstripe.com/blogs/why-can-i-only-use-commercial-sounds-on-tiktok
16. Rocketlink — TikTok link-in-bio requirements. https://rocketlink.io/blog/tiktok-link-in-bio-requirements

**Platforms: YouTube / Google**

17. PPC Land — YouTube changes how Shorts views are counted from 2025-03-31 (announced 2025-03-26). https://ppc.land/youtube-changes-how-shorts-views-are-counted-from-march-31/
18. PPC Land — YouTube expands Shorts to 3 minutes (2024-10-15). https://ppc.land/youtube-expands-shorts-duration-to-3-minutes/
19. Google Ads Help — Your guide to YouTube Shorts ads. https://support.google.com/google-ads/answer/16041697
20. YouTube Help — Channel monetization policies ("inauthentic content", renamed 2025-07-15). https://support.google.com/youtube/answer/1311392
21. YouTube Help — Harmful or dangerous content policies. https://support.google.com/youtube/answer/2801964
22. YouTube Help — Paid product placements, sponsorships and endorsements. https://support.google.com/youtube/answer/154235
23. Google Ads policy — Enabling dishonest behavior ("hacking services, including game enhancements and cheat softwares"). https://support.google.com/adspolicy/answer/6016086 · reorganized 2025-08-14 without enforcement change: https://ppc.land/google-reorganizes-dishonest-behavior-policy-without-enforcement-changes/
24. PPC Land — Todd Beaupré on Creator Insider: satisfaction surveys, long-term viewer value (2026-09-01). https://ppc.land/subscribers-skip-90-of-uploads-in-their-feed-youtube-director-says/
25. Tubefilter — YouTube Shorts averages 200 billion daily views (2025-06-18). https://www.tubefilter.com/2025/06/18/youtube-shorts-200-billion-daily-views-google-veo-3-ai-neal-mohan/
26. 9to5Google — YouTube removes clickable links from Shorts descriptions and comments (2023-08-10). https://9to5google.com/2023/08/10/youtube-shorts-links-spam/
27. Bytecap — YouTube Shorts retention benchmarks: "chose to view" definition, no official universal threshold (2026-07-17). https://www.bytecap.io/research/youtube-shorts-retention-benchmarks
28. Creator Essentials — Shorts engaged views; average percentage viewed can exceed 100% with loops. https://www.creatoressentials.com/glossary/shorts-engaged-views/
29. Search Engine Journal — Rene Ritchie: "the algorithm follows the audience". https://www.searchenginejournal.com/youtube-algorithm-insights

**Platforms: Instagram / Meta**

30. Dataslayer — Instagram signals confirmed by Mosseri (2025-01-22: watch time, likes per reach, sends per reach). https://www.dataslayer.ai/blog/instagram-algorithm-2025-complete-guide-for-marketers
31. Instagram Creators — What creators need to know about recommendations (eligibility, ≤ 3 min, first 3 seconds). https://creators.instagram.com/blog/instagram-recommendations-eligibility-tips-creators
32. Social Media Today — Instagram clarifies single-word CTAs and engagement bait (2024-06-05). https://www.socialmediatoday.com/news/instagram-clarifies-advice-on-single-word-ctas-and-longer-reels/718151/
33. MacMagazine — Reels up to 3 minutes and rectangular 3:4 grid (2025-01-20). https://macmagazine.com.br/post/2025/01/20/instagram-ganha-reels-de-ate-3-minutos-e-grade-de-posts-retangulares/
34. Business Today — Instagram launches Trial Reels (2024-12-12). https://www.businesstoday.in/technology/news/story/instagram-launches-trial-reels-letting-creators-test-content-before-reaching-followers-457022-2024-12-12
35. Android Central — Instagram "Your Algorithm" controls for Reels (Dec 2025). https://www.androidcentral.com/apps-software/meta/instagram-hands-you-the-keys-to-control-your-algorithm-in-reels-plans-to-expand
36. PetaPixel — New Instagram policies target reposted content (2026-04-30). https://petapixel.com/2026/04/30/new-instagram-policies-target-reposted-content/
37. SocialPilot — Instagram makes "Views" the primary metric (Apr 2025). https://www.socialpilot.co/instagram-marketing/instagram-views-metrics-changes
38. Social Samosa — Instagram adds Retention chart and Skip rate for Reels (Aug 2025). https://www.socialsamosa.com/news-2/instagram-retention-chart-skip-rate-new-performance-metrics-reels-9730992
39. Meta for Developers — Unlock the power of Reels ads (2024-11-07: "Over 75% of Reels views on Instagram are sound on"). https://developers.facebook.com/blog/post/2024/11/07/unlock-the-power-of-reel-ads/
40. PPC Land — Meta × Toluna Reels creative study: 100 ads × 65 variables, 4 markets (2025-12-02). https://ppc.land/meta-and-toluna-study-finds-emojis-lift-reels-purchase-intent-2-5x/
41. Meta Transparency Center — Advertising Standards: Cheating and deceitful practices. https://transparency.meta.com/policies/ad-standards/deceptive-content/cheating-and-deceitful-practices/
42. Marketing Dive — Facebook: mobile feed content recalled after 0.25 s (Fors Marsh research). https://www.marketingdive.com/news/facebook-why-mobile-video-ads-must-work-fast/446217/
43. Hopper HQ — Instagram Reel size; 3:4 profile-grid crop (1080 × 1440). https://www.hopperhq.com/blog/instagram-reel-size/
44. Inro — Clickable links in Reels via Meta Verified tiers (2026). https://www.inro.social/blog/meta-verified-clickable-links-instagram-reels-pricing
45. Meta — WhatsApp brand assets and guidelines. https://www.meta.com/brand/resources/whatsapp/whatsapp-brand/
46. ClipSpeed — YouTube Shorts size and safe zones (2026-09-11). https://www.clipspeed.ai/blog/youtube-shorts-size.html

**Research: attention, curiosity, reward**

47. Loewenstein, G. (1994). The psychology of curiosity. *Psychological Bulletin*. https://doi.org/10.1037/0033-2909.116.1.75
48. Kang, M. J., et al. (2009). The wick in the candle of learning. *Psychological Science*. https://pubmed.ncbi.nlm.nih.gov/19619181/
49. Gruber, M. J., Gelman, B. D., & Ranganath, C. (2014). States of curiosity modulate hippocampus-dependent learning. *Neuron*. https://doi.org/10.1016/j.neuron.2014.08.060
50. Ghibellini, R., & Meier, B. (2025). The Zeigarnik effect: a meta-analysis (Zeigarnik vs Ovsiankina). *Humanities and Social Sciences Communications*. https://ideas.repec.org/a/pal/palcom/v12y2025i1d10.1057_s41599-025-05000-w.html
51. Schultz, W., Dayan, P., & Montague, P. R. (1997). A neural substrate of prediction and reward. *Science*. https://doi.org/10.1126/science.275.5306.1593
52. Fiorillo, C. D., Tobler, P. N., & Schultz, W. (2003). Discrete coding of reward probability and uncertainty by dopamine neurons. *Science*. https://doi.org/10.1126/science.1077349
53. Salimpoor, V. N., et al. (2011). Anatomically distinct dopamine release during anticipation and experience of peak emotion to music. *Nature Neuroscience*. https://www.zlab.mcgill.ca/publications/docs/salimpoor_2011_nn.pdf
54. Clark, L., et al. (2009). Gambling near-misses enhance motivation to gamble. *Neuron*. https://doi.org/10.1016/j.neuron.2008.12.031

**Research: decision-making and persuasion**

55. Kahneman, D., & Tversky, A. (1979). Prospect theory. *Econometrica*. https://doi.org/10.2307/1914185
56. Brown, A. L., Imai, T., Vieider, F. M., & Camerer, C. F. (2024). Meta-analysis of empirical estimates of loss aversion. *Journal of Economic Literature*. https://www.aeaweb.org/doi/10.1257/jel.20221698
57. Przybylski, A. K., et al. (2013). Correlates of fear of missing out. *Computers in Human Behavior*. https://doi.org/10.1016/j.chb.2013.02.014
58. Goldstein, N. J., Cialdini, R. B., & Griskevicius, V. (2008). A room with a viewpoint. *Journal of Consumer Research*. https://doi.org/10.1086/586910
59. Worchel, S., Lee, J., & Adewole, A. (1975). Effects of supply and demand on ratings of object value. *JPSP*. https://doi.org/10.1037/0022-3514.32.5.906
60. Tversky, A., & Kahneman, D. (1974). Judgment under uncertainty: heuristics and biases. *Science*. https://doi.org/10.1126/science.185.4157.1124
61. Gourville, J. T. (1998). Pennies-a-day: the effect of temporal reframing on transaction evaluation. *Journal of Consumer Research*. https://ideas.repec.org/a/oup/jconrs/v24y1998i4p395-408.html
62. Kahneman, D., Fredrickson, B. L., Schreiber, C. A., & Redelmeier, D. A. (1993). When more pain is preferred to less: adding a better end. *Psychological Science*. https://doi.org/10.1111/j.1467-9280.1993.tb00589.x
63. Fredrickson, B. L., & Kahneman, D. (1993). Duration neglect in retrospective evaluations of affective episodes. *JPSP*. https://doi.org/10.1037/0022-3514.65.1.45
64. Zajonc, R. B. (1968). Attitudinal effects of mere exposure. *JPSP*. https://doi.org/10.1037/h0025848
65. Bornstein, R. F. (1989). Exposure and affect: meta-analysis 1968–1987. *Psychological Bulletin*. https://doi.org/10.1037/0033-2909.106.2.265
66. Romaniuk, J. (2018). *Building Distinctive Brand Assets*. Oxford University Press (Ehrenberg-Bass). https://www.oup.com.au/books/higher-education/business-marketing/9780190311506
67. Ipsos — The power of you: why distinctive brand assets are a driving force of creative effectiveness (meta-analysis of 2,000+ video ads). https://www.ipsos.com/en-us/knowledge/media-brand-communication/power-you-why-distinctive-brand-assets-are-driving-force-creative-effectiveness
68. Reber, R., Schwarz, N., & Winkielman, P. (2004). Processing fluency and aesthetic pleasure. *Personality and Social Psychology Review*. https://doi.org/10.1207/s15327957pspr0804_3
69. McGlone, M. S., & Tofighbakhsh, J. (2000). Birds of a feather flock conjointly (?): rhyme as reason in aphorisms. *Psychological Science*. https://pubmed.ncbi.nlm.nih.gov/11228916/
70. Hunt, R. R. (1995). The subtlety of distinctiveness: what von Restorff really did. *Psychonomic Bulletin & Review*. https://doi.org/10.3758/BF03214414
71. Norton, M. I., Mochon, D., & Ariely, D. (2012). The IKEA effect: when labor leads to love. *Journal of Consumer Psychology*. https://dash.harvard.edu/handle/1/12136084
72. Kahneman, D., Knetsch, J. L., & Thaler, R. H. (1990). Experimental tests of the endowment effect. *Journal of Political Economy*. https://doi.org/10.1086/261737
73. Oyserman, D. (2009). Identity-based motivation. *Journal of Consumer Psychology*. https://doi.org/10.1016/j.jcps.2009.05.008
74. McGraw, A. P., & Warren, C. (2010). Benign violations: making immoral behavior funny. *Psychological Science*. https://leeds-faculty.colorado.edu/mcgrawp/pdf/mcgraw.warren.2010.pdf
75. Eisend, M. (2009). A meta-analysis of humor in advertising. *Journal of the Academy of Marketing Science*. https://doi.org/10.1007/s11747-008-0096-y
76. Lasaleta, J. D., Sedikides, C., & Vohs, K. D. (2014). Nostalgia weakens the desire for money. *Journal of Consumer Research*. https://www.southampton.ac.uk/~crsi/Lasaleta,%20Sedikides,%20and%20Vohs%202014.pdf
77. Poerio, G. L., et al. (2018). More than a feeling: ASMR is characterized by reliable changes in affect and physiology. *PLOS ONE*. https://doi.org/10.1371/journal.pone.0196645
78. Husain, G., Thompson, W. F., & Schellenberg, E. G. (2002). Effects of musical tempo and mode on arousal, mood, and spatial abilities. *Music Perception*. https://sites.utm.utoronto.ca/sites/sites.utm.utoronto.ca.glenn_website/files/download/Husain.pdf
79. Labrecque, L. I., & Milne, G. R. (2012). Exciting red and competent blue: the importance of color in marketing. *JAMS*. https://doi.org/10.1007/s11747-010-0245-y
80. Elliot, A. J., & Maier, M. A. (2014). Color psychology. *Annual Review of Psychology*. https://doi.org/10.1146/annurev-psych-010213-115035

**Research: perception, narrative, cognitive load**

81. Cerf, M., Frady, E. P., & Koch, C. (2009). Faces and text attract gaze independent of the task. *Journal of Vision*. https://resolver.caltech.edu/CaltechAUTHORS:20130816-103355264
82. Abrams, R. A., & Christ, S. E. (2003). Motion onset captures attention. *Psychological Science*. https://pubmed.ncbi.nlm.nih.gov/12930472/
83. Itti, L., & Koch, C. (2001). Computational modelling of visual attention. *Nature Reviews Neuroscience*. https://doi.org/10.1038/35058500
84. Standing, L. (1973). Learning 10,000 pictures. *Quarterly Journal of Experimental Psychology*. https://doi.org/10.1080/14640747308400340
85. Green, M. C., & Brock, T. C. (2000). The role of transportation in the persuasiveness of public narratives. *JPSP*. https://doi.org/10.1037/0022-3514.79.5.701
86. van Laer, T., de Ruyter, K., Visconti, L. M., & Wetzels, M. (2014). The extended transportation-imagery model (meta-analysis). *Journal of Consumer Research*. https://openaccess.city.ac.uk/id/eprint/6755/
87. Meyers-Levy, J., & Tybout, A. M. (1989). Schema congruity as a basis for product evaluation. *Journal of Consumer Research*. https://doi.org/10.1086/209192
88. Freedman, J. L., & Fraser, S. C. (1966). Compliance without pressure: the foot-in-the-door technique. *JPSP*. https://doi.org/10.1037/h0023552
89. Regan, D. T. (1971). Effects of a favor and liking on compliance. *Journal of Experimental Social Psychology*. https://doi.org/10.1016/0022-1031(71)90025-4
90. Jecker, J., & Landy, D. (1969). Liking a person as a function of doing him a favour. *Human Relations*. https://doi.org/10.1177/001872676902200407
91. Sweller, J. (1988). Cognitive load during problem solving. *Cognitive Science*. https://doi.org/10.1207/s15516709cog1202_4
92. Mayer, R. E., & Moreno, R. (2003). Nine ways to reduce cognitive load in multimedia learning. *Educational Psychologist*. https://doi.org/10.1207/S15326985EP3801_6
93. Lang, A. (1990). Involuntary attention and physiological arousal evoked by structural features and emotional content in TV commercials. *Communication Research*. https://doi.org/10.1177/009365090017003001
94. Lang, A., Bolls, P., Potter, R. F., & Kawahara, K. (1999). The effects of production pacing and arousing content on the information processing of television messages. *Journal of Broadcasting & Electronic Media*. https://doi.org/10.1080/08838159909364504
95. Auditory structural features and the cardiac orienting response (Potter et al. line of research; *Journal of Cognition*). https://journalofcognition.org/articles/43
96. Rogers, A., & Gibson, I. (2012). Emotional impact of musical/visual synchrony variation in film. ICMPC 12. https://eprints.hud.ac.uk/id/eprint/14946/
97. Cutting, J. E., DeLong, J. E., & Nothelfer, C. E. (2010). Attention and the evolution of Hollywood film. *Psychological Science*. https://doi.org/10.1177/0956797610361679
98. Kivetz, R., Urminsky, O., & Zheng, Y. (2006). The goal-gradient hypothesis resurrected. *Journal of Marketing Research*. https://business.columbia.edu/sites/default/files-efs/pubfiles/1200/goalgradient.pdf
99. Conrad, F. G., Couper, M. P., Tourangeau, R., & Peytchev, A. (2010). The impact of progress indicators on task completion. *Interacting with Computers*. https://pmc.ncbi.nlm.nih.gov/articles/PMC2910434
100. Berger, J., & Milkman, K. L. (2012). What makes online content viral? *Journal of Marketing Research*. https://doi.org/10.1509/jmr.10.0353
101. Robertson, C. E., et al. (2023). Negativity drives online news consumption. *Nature Human Behaviour*. https://pmc.ncbi.nlm.nih.gov/articles/PMC10202797/
102. Baumeister, R. F., et al. (2001). Bad is stronger than good. *Review of General Psychology*. https://doi.org/10.1037/1089-2680.5.4.323
103. Lai, L., & Farbrot, A. (2014). What makes you click? The effect of question headlines (BPS Research Digest summary). https://www.bps.org.uk/research-digest/are-you-more-likely-click-headlines-are-phrased-question
104. Journalism.co.uk — Readers perceive question-based headlines more negatively (Scacco & Muddiman). https://www.journalism.co.uk/readers-perceive-question-based-headlines-more-negatively-study-shows/
105. Leavitt, J. D., & Christenfeld, N. J. S. (2011). Story spoilers don't spoil stories (APS summary). https://www.psychologicalscience.org/news/surprise-spoilers-make-stories-better.html
106. Rogers, T. B., Kuiper, N. A., & Kirker, W. S. (1977). Self-reference and the encoding of personal information. *JPSP*. https://doi.org/10.1037/0022-3514.35.9.677
107. Xie, G.-X., & Kronrod, A. (2012). Is the devil in the details? The signaling effect of numerical precision in environmental advertising claims. *Journal of Advertising*. https://collaborate.umb.edu/en/publications/is-t-he-dev-il-in-t-he-det-ails-the-signaling-effect-of-numerical/
108. RealEye / Baig (2025) — The gravity of the center: what grabs attention in vertical videos. https://realeye.io/blog/post/the-gravity-of-the-center-what-grabs-attention-in-vertical-videos/
109. Communication Today (2026) — Watching TikTok: an eye-tracking study of visual attention paid to short-form videos. https://communicationtoday.sk/watching-tiktok-an-eye-tracking-study-of-visual-attention-paid-to-short-form-videos/
110. Streaming Media — Verizon Media & Publicis captions study (2019; 69% sound-off in public, 80% more likely to finish with captions). https://www.streamingmedia.com/Articles/News/Online-Video-News/80-of-Video-Caption-Users-Arent-Hearing-Impaired-Finds-Verizon-131860.aspx
111. Netflix Partner Help — Portuguese (Brazil) Timed Text Style Guide. https://partnerhelp.netflixstudios.com/hc/en-us/articles/215600497-Portuguese-Brazil-Timed-Text-Style-Guide
112. Arquivos Brasileiros de Oftalmologia — IReST in Brazilian Portuguese (reading speed 1,100 ± 167 cpm). https://aboonline.org.br/details/1379/en-US
113. Trauzettel-Klosinski, S., & Dietz, K. (2012). Standardized assessment of reading performance: the International Reading Speed Texts (IReST). *IOVS*. https://repositorio.usp.br/item/002346519
114. Apple Human Interface Guidelines — Typography. https://developer.apple.com/design/human-interface-guidelines/typography
115. W3C — WCAG 2.2: contrast minimum (1.4.3) and three flashes (2.3.1). https://www.w3.org/TR/WCAG22/
116. Rayner, K., et al. (2016). So much to read, so little time: how do we read, and can speed reading help? *Psychological Science in the Public Interest*. https://doi.org/10.1177/1529100615623267
117. ITU-R BT.1359 audio-video sync thresholds, as summarized in arXiv 2212.01686. https://arxiv.org/abs/2212.01686
118. MeterPlugs — YouTube changes its loudness reference to −14 LUFS (2019). https://www.meterplugs.com/blog/2019/09/18/youtube-changes-loudness-reference-to-14-lufs.html
119. Production Advice — AES TD1008 streaming loudness recommendations. https://productionadvice.co.uk/td1008/

**Brazil: market, culture and trends**

120. DataReportal — Digital 2026: Brazil (data Oct 2025). https://datareportal.com/reports/digital-2026-brazil
121. IstoÉ — Pesquisa Game Brasil 2026: players and AI (2026). https://istoe.com.br/brasileiros-games-ia-pgb
122. GameHall — PGB 2026: AI concerns, nostalgia, platforms (n = 7,115, March 2026). https://gamehall.com.br/pgb-2026-revela-preocupacao-com-ia-e-mudancas-no-consumo-de-games/
123. Canaltech — Pesquisa Game Brasil 2025 (82.8% play). https://canaltech.com.br/games/pesquisa-game-brasil-2025-revela-como-diferentes-geracoes-de-brasileiros-jogam/
124. Canaltech — What Brazilians do on WhatsApp (Opinion Box, June 2025, n = 1,126). https://canaltech.com.br/apps/o-que-os-brasileiros-mais-fazem-no-whatsapp-segundo-pesquisa/
125. Movimento Econômico — Pix 2025 figures from the Banco Central's Pix management report. https://movimentoeconomico.com.br/economia/2026/08/11/chaves-pix-chegam-a-920-milhoes-e-sistema-movimenta-r-35-tri-em-2025/
126. Olhar Digital — Pix Automático launches 2025-06-16. https://olhardigital.com.br/2025/06/02/pro/pix-automatico-sera-lancado-ainda-neste-mes-saiba-como-funciona/
127. Metricool — Best time to post on TikTok (Brasília time; TikTok study 2026). https://metricool.com/pt/melhor-horario-postar-tiktok/
128. Billboard Brasil — Brazilian phonk grows 62% in Europe (2026). https://billboard.com.br/brazilian-phonk-crescimento-global-tiktok-funk/
129. Billboard Brasil — TikTok data on Brazilian funk (2025-07-12). https://billboard.com.br/tiktok-divulga-dados-sobre-o-impacto-do-funk-brasileiro-na-plataforma/
130. Billboard Brasil — O que é BPM (funk from 130 to 150 BPM). https://billboard.com.br/voce-sabe-o-que-e-bpm/
131. Xataka Brasil — "Torneio de farmar aura" (2026-08-21). https://www.xataka.com.br/diversos/torneio-farmar-aura-milhares-jovens-estao-colocando-seu-carisma-a-prova-com-uma-tradicao-milenar
132. HBR Brasil — 10 most-used slang terms of 2026 (2025-11-21). https://hbrbr.com.br/10-girias-mais-usadas.html
133. Conversar com Adolescente — Gen Z and Gen Alpha slang dictionary 2026 (updated 2026-03-24). https://www.conversarcomadolescente.com.br/post/dicion%C3%A1rio-de-g%C3%ADrias-da-gera%C3%A7%C3%A3o-z-e-gera%C3%A7%C3%A3o-alpha-atualizado-2026
134. Band — 10 memes that marked 2025 (2025-12-26). https://www.band.com.br/entretenimento/patixa-telo-brainrot-e-mais-relembre-10-memes-que-marcaram-2025-202512261524
135. Band — "Brainrot" was the most-searched topic on YouTube Brazil in 2025. https://www.band.com.br/entretenimento/brainrot-foi-assunto-mais-pesquisado-no-youtube-em-2025-saiba-o-que-e-202512041604
136. The Bobcat Prowl — The cortisol craze of 2026 ("high vs low cortisol" format). https://thebobcatprowl.com/20613/opinion/the-cortisol-craze-of-2026
137. Global Voices — If you want to understand Brazil, check out its memes. https://globalvoices.org/2017/09/29/if-you-want-to-understand-brazil-you-should-check-out-its-memes/
138. Caixin Global — Kwai reaches 60 M monthly active users in Brazil (2025-12-11). https://www.caixinglobal.com/2025-12-11/kuaishous-kwai-conquers-brazil-by-ditching-the-time-machine-strategy-102392161.html

**Brazil: law, IP and compliance**

139. Lei nº 15.211/2025 — Estatuto Digital da Criança e do Adolescente (ECA Digital). https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15211.htm
140. Machado Meyer — ECA Digital in force from 2026-03-17. https://www.machadomeyer.com.br/pt/inteligencia-juridica/publicacoes-ij/direito-digital/estatuto-digital-da-crianca-e-do-adolescente-lei-n-15-211-2025-entra-em-vigor-em-17-de-marco-de-2026
141. Lei nº 8.078/1990 — Código de Defesa do Consumidor (art. 37: misleading and abusive advertising). https://www.planalto.gov.br/ccivil_03/leis/l8078compilado.htm
142. Meio & Mensagem — CONAR launches guide for advertising by digital influencers (identification as "publi"/"publicidade"). https://www.meioemensagem.com.br/home/comunicacao/2020/12/09/conar-lanca-guia-para-publicidade-com-influenciadores.html
143. Lei nº 13.709/2018 — Lei Geral de Proteção de Dados (LGPD). https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm
144. Video Games Chronicle — Former Pokémon lawyer says fundraising and press coverage lead to fan-project takedowns (2024-03-14). https://videogameschronicle.com/news/former-pokemon-lawyer-says-fundraising-and-press-coverage-lead-to-fan-project-takedowns
145. Techdirt — Pokémon Co. is DMCAing years-old videos showing Pokémon modded into other games (2024-03-20). https://www.techdirt.com/2024/03/20/pokemon-co-is-now-dmcaing-years-old-videos-showing-pokemon-modded-into-other-games/
146. Sajjacholapunt, P., & Ball, L. J. (2014). The influence of banner advertisements on attention and memory: human faces with averted gaze can enhance advertising effectiveness. *Frontiers in Psychology*. https://doi.org/10.3389/fpsyg.2014.00166
147. Lang, A., Potter, R. F., & Bolls, P. D. (1999). Something for nothing: is visual encoding automatic? *Media Psychology*. https://doi.org/10.1207/s1532785xmep0102_4

**Research limits:** PokeXGames' official site returned HTTP 503 during this research, so the game's rules on third-party automation **could not be verified**. Safe-zone pixel values for organic posts come from third-party UI measurements, because platforms only publish ad templates. Benchmarks marked [C] come from vendor datasets (mostly US/EU English-language ads) and should be re-validated with your own pt-BR analytics.
