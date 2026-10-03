# F18 — Ache o Shiny (126–130)

**Lever:** participation. A spot-the-difference puzzle with a 3-second timer forces active looking, makes people rewatch (loops count as views) and comment ("achei!", "linha 4"). The Von Restorff effect is the mechanic itself. The ending ties it to the product: KizuBot detects shiny, mega and boss automatically and sends the alarm.
**Look:** a dense grid of creatures that are **not** Pokémon: use emoji animals (🐛🦎🐢🐟🐦🦊🐲🐌🦀…) rendered with Noto Color Emoji, and make the "shiny" one with a CSS `filter: hue-rotate()` / saturation shift (that's literally what a shiny is: a color variant). A big timer ring, "PAUSA E PROCURA!", then the answer: everything dims except the shiny, a circle draws around it (DrawSVG), sparkle SFX. Difficulty rises across episodes (bigger grid, subtler hue, slight idle motion).
**Music:** chiptune (150); `clock` ticks on the countdown, `sparkle` + `right` on the answer, `alert` when the KizuBot alarm appears.
**Fairness:** the shiny must really be findable in a paused frame (test it on a snapshot).

---

### 126 · ache-o-shiny-facil — Ache o shiny em 3 segundos
- **Hook:** "ACHE O SHINY EM 3 SEGUNDOS." (grid 5×7 of 🐛, one with hue shift ~120°).
- **Beats:** timer 3-2-1 → reveal → "Você levou 3 segundos. O KizuBot detecta sozinho." → real alarm line `shiny-cubone.png` → claim "detecção de shinys, megas e bosses".
- **Pinned:** "Achou em quantos segundos? ⏱️"

### 127 · ache-o-shiny-medio — Nível 2
- **Hook:** "NÍVEL 2: ACHE O SHINY." (grid 7×10 of 🦎, hue shift ~50°, two decoys with slight size changes).
- **Ending:** "E se ele aparecer às 3h da manhã?" → alarm sound → real alarm line from `shiny-raichu-7-alarms.png` ("shinyDetected ~ --> shiny Raichu").
- **Pinned:** "Em que linha e coluna tava? 👀"

### 128 · ache-o-shiny-impossivel — Nível impossível
- **Hook:** "NÍVEL IMPOSSÍVEL." (grid 9×13 of mixed animals with a gentle idle bob; the shiny has hue ~25° and is in a corner).
- **Ending:** "Ninguém acha isso com os olhos. A IA acha." → real print `shiny-muk.png` safe crop: "pena que n vi piscar" / "tava afk" + the Shiny Muk card.
- **Pinned:** "Se achou sem pausar, você é lenda 🏆"

### 129 · ache-o-boss — Ache o boss
- **Hook:** "ACHE O BOSS." (grid of 🐢; the boss is slightly bigger with a faint red aura that pulses — subtle).
- **Ending:** "O KizuBot avisa: bossDetected." → `boss-tangrowth-electivire.png` alarm lines (nick hidden): "bossDetected ~ --> boss Tangrowth" / "dropRare ~ Gaia Tentacles", or `boss-loot-15kk.png` ("15kk de item de boss" "dropou 2 em 1h").
- **Pinned:** "Qual boss você mais quer? 💀"

### 130 · ache-a-mega — Ache a mega
- **Hook:** "ACHE A MEGA." (grid of 🦖/🐲; the mega has a different shape accessory — a small glowing stone sticker).
- **Ending:** "Uma mega aparece. O alarme toca." → `mega-stone-barbaracite.png` ("Olha o que o kizu me presenteou", Barbaracite tooltip) — or the megaDetected lines from `mega-scizor-8-alarms.png`.
- **Pinned:** "Pegou de primeira? ⚡"
