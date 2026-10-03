# F09 — Satisfatório (081–085)

**Lever:** sensory reward and closure. "Oddly satisfying" motion (perfect alignment, completion, rhythm) releases a small reward and invites rewatching; a seamless loop makes the replay invisible, and loops count as extra views and watch time. Keep these short: **12–15 s**, minimal text (one line), product meaning carried by the objects.
**Look:** clean, tactile, minimal: soft 3D-ish UI on a dark violet gradient, rounded toggles and bars with subtle inner shadows and highlights, perfectly synced to the beat, buttery eases (`power2.inOut`, `expo.inOut`), no shake, no clutter. Each episode one mechanic. The last frame must match the first frame so it loops (end card can be a compact 2.5 s lockup that dissolves back into frame 1).
**Music:** minimal house (124) or lofi (84) at low energy; crisp foley SFX carry it: `switch`, `click`, `tick`, `fill`, `snap`, `success`, `pop`.

---

### 081 · todos-os-modulos-on — Todos os módulos: ON
- **Hook:** "TODOS OS MÓDULOS: ON." (13 toggles in a column, all OFF).
- **Beats:** the toggles flip ON one per beat in a cascade (`switch` each), labels: Cavebot · Combat · Healing · Catch · Farming · Fishing · Alarms · Party · Engine · Actions · Account · Setup Pokémon · Humanização. When all are on, a purple glow sweeps and "100% AFK" lights up. Loop: all flip OFF in one satisfying wave back to frame 1.
- **Pinned:** "Assistiu quantas vezes? 🔁"

### 082 · barras-de-loot — Barras de loot enchendo
- **Hook:** "RELATÓRIO DE LOOT." (empty bars).
- **Beats:** bars fill smoothly with real numbers from `alarme-12335-itens.png` (Screw 11616, Electric Box 542, Electric Rat Tail 115, Electric Tail 45, Thunder Stone 12; "Total dropped items: 12335") — `fill` + `counter`; the total lands with `success`. Small tag "print real de cliente" + the print thumbnail at the end.
- **Pinned:** "Qual barra você queria ver cheia? 📊"

### 083 · checklist-perfeito — Checklist perfeito
- **Hook:** "CHECKLIST DO FARM." 
- **Beats:** 8 lines tick in rhythm (`tick` on the beat, the ticks draw with DrawSVG): "Caça sozinho ✓ · Captura ✓ · Pesca ✓ · Coleta ✓ · Cura ✓ · Avisa no WhatsApp ✓ · Roda com PC desligado ✓ · Você dormindo ✓". The list then folds into a tiny card that becomes frame 1 again.
- **Pinned:** "Qual item é o melhor? ✅"

### 084 · encaixe-perfeito — Encaixe perfeito
- **Hook:** "ENCAIXE PERFEITO." 
- **Beats:** 12–16 real print thumbnails (from ASSETS.md, all safe) fly in from the edges and snap into a perfect grid with satisfying `snap` sounds; the grid then morphs (scale/opacity) into the KizuBot logo silhouette; eye glow; dissolve back to the empty frame. Tag "prints reais de clientes".
- **Pinned:** "Achou algum print que você conhece? 👀"

### 085 · inventario-organizado — Inventário se organizando sozinho
- **Hook:** "INVENTÁRIO SE ORGANIZANDO SOZINHO." (a messy grid of generic item icons — stones, balls, berries, drawn in CSS/SVG, no game sprites).
- **Beats:** items glide and sort by color and type into perfect rows (FLIP-style moves, `pop` per row), the counter "itens organizados" climbs; caption "Assim é o farm com KizuBot: tudo no lugar." Loop back by un-sorting in one wave.
- **Pinned:** "Seu inventário é organizado assim? 😂"
