#!/usr/bin/env python3
"""publish - copy finished shorts into the kizubot-social-media repo.

  python3 tools/publish.py --check            list shorts and their QC state
  python3 tools/publish.py --ids 041-060      copy those shorts (mp4 + sources) into the repo
  python3 tools/publish.py --index            rebuild README index, metadata.json/csv and frame grids
  python3 tools/publish.py --studio           sync kit/, tools/, docs/, template/ into the repo

Repo layout written (relative to the repo root):
  motion/serie-neuro/NNN-slug.mp4
  motion/serie-neuro/README.md
  motion/serie-neuro/metadata.json, metadata.csv
  motion/serie-neuro/grid-01.jpg ...
  motion/serie-neuro/studio/{docs,tools,kit,template}/ and studio/shorts/NNN-slug/{index.html,audio.json,meta.json,kit->../../kit}
"""
import argparse
import csv
import json
import os
import re
import shutil
import subprocess
import sys

STUDIO = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
REPO = "/home/user/kizubot-social-media"
OUT = os.path.join(REPO, "motion", "serie-neuro")
SHORTS = os.path.join(STUDIO, "shorts")

SERIES = [
    ("F01", "A Conta", 41, 45), ("F02", "POV", 46, 50), ("F03", "Mito ou Verdade?", 51, 55),
    ("F04", "Espera o Alarme", 56, 60), ("F05", "Top 5", 61, 65), ("F06", "Currículo do KizuBot", 66, 70),
    ("F07", "Só Quem Joga PxG Entende", 71, 75), ("F08", "Ligação Recebida", 76, 80), ("F09", "Satisfatório", 81, 85),
    ("F10", "Você Prefere?", 86, 90), ("F11", "Dicionário PxG", 91, 95), ("F12", "Novidade no KizuBot", 96, 100),
    ("F13", "Raio-X", 101, 105), ("F14", "Prova Real", 106, 110), ("F15", "Terror no PxG", 111, 115),
    ("F16", "Speedrun", 116, 120), ("F17", "Infomercial", 121, 125), ("F18", "Ache o Shiny", 126, 130),
    ("F19", "O Dia de Quem Usa", 131, 135), ("F20", "Plot Twist", 136, 140),
]


def series_of(n):
    for code, name, a, b in SERIES:
        if a <= n <= b:
            return code, name
    return "", ""


def shorts():
    out = []
    for d in sorted(os.listdir(SHORTS)):
        m = re.match(r"^(\d{3})-(.+)$", d)
        if not m or int(m.group(1)) < 41:
            continue
        p = os.path.join(SHORTS, d)
        qc_path = os.path.join(p, "renders", "qc.json")
        meta_path = os.path.join(p, "meta.json")
        qc = json.load(open(qc_path)) if os.path.exists(qc_path) else None
        meta = json.load(open(meta_path)) if os.path.exists(meta_path) else {}
        out.append(dict(id=m.group(1), slug=m.group(2), dir=p, name=d, qc=qc, meta=meta,
                        final=os.path.join(p, "renders", "final.mp4")))
    return out


def parse_ids(spec):
    ids = set()
    for part in spec.split(","):
        if "-" in part:
            a, b = part.split("-")
            ids.update(range(int(a), int(b) + 1))
        elif part:
            ids.add(int(part))
    return ids


def copy_short(s):
    os.makedirs(OUT, exist_ok=True)
    dst = os.path.join(OUT, s["name"] + ".mp4")
    shutil.copy2(s["final"], dst)
    src_dst = os.path.join(OUT, "studio", "shorts", s["name"])
    os.makedirs(src_dst, exist_ok=True)
    smap = source_map()
    for f in ("index.html", "audio.json", "meta.json"):
        fp = os.path.join(s["dir"], f)
        if os.path.exists(fp):
            t = open(fp, encoding="utf-8").read()
            open(os.path.join(src_dst, f), "w", encoding="utf-8").write(scrub_text(t, smap) if f != "audio.json" else t)
    # any extra local assets the short ships (svg, json) but never renders/snapshots/audio wavs
    for f in os.listdir(s["dir"]):
        fp = os.path.join(s["dir"], f)
        if os.path.isfile(fp) and f not in ("index.html", "audio.json", "meta.json") and not f.endswith((".mp4", ".wav", ".png", ".jpg")):
            shutil.copy2(fp, os.path.join(src_dst, f))
    for sub in ("assets",):
        sp = os.path.join(s["dir"], sub)
        if os.path.isdir(sp):
            shutil.copytree(sp, os.path.join(src_dst, sub), dirs_exist_ok=True)
    link = os.path.join(src_dst, "kit")
    if not os.path.lexists(link):
        os.symlink("../../kit", link)
    return dst


# ---------------------------------------------------------------- public-repo sanitizing
# The target repo is PUBLIC. Customer names must never appear in it — not in images (the prints are
# redacted) and not in text either: the site's original filenames contain customers' names, and the
# research notes quote them. Game-staff names are removed too.
# Name lists live in studio/private/scrub.json, which is never copied into the repo.
_PRIV = os.path.join(STUDIO, "private", "scrub.json")
_SCRUB = json.load(open(_PRIV)) if os.path.exists(_PRIV) else {"staff_patterns": [], "deny": [], "names": []}
STAFF_PATTERNS = [tuple(x) for x in _SCRUB["staff_patterns"]]
DENY = _SCRUB["deny"]
NAME_SCRUB = _SCRUB["names"]


def source_map():
    """source basename -> safe slug, parsed from ASSETS.md's traceability list."""
    m = {}
    txt = open(os.path.join(STUDIO, "docs", "ASSETS.md"), encoding="utf-8").read()
    for src, slug in re.findall(r"- `(?:[a-z]+/)?([^`]+?)` → `([^`]+?)`", txt):
        m[src] = slug
    return m


def scrub_text(t, smap):
    # 1) every known source filename (with or without folder / extension) -> its safe slug
    for src in sorted(smap, key=len, reverse=True):
        slug = smap[src]
        stem = os.path.splitext(src)[0]
        t = re.sub(r"(?:(?:feedbacks|testimonials|results|images)/)?" + re.escape(src), slug, t)
        if len(stem) >= 8:
            t = re.sub(r"(?<![A-Za-z0-9-])" + re.escape(stem) + r"(?![A-Za-z0-9-])", os.path.splitext(slug)[0], t)

    def repl(mo):
        tok = mo.group(1)
        base = tok.split("/")[-1]
        if base in smap:
            return "`" + smap[base] + "`"
        if "…" in base or "..." in base:
            pre = base.split("…")[0].split("...")[0]
            for k, v in smap.items():
                if pre and k.startswith(pre):
                    return "`" + v + "`"
        for kd in ("prints", "brand", "ui", "bg"):
            if os.path.exists(os.path.join(STUDIO, "kit", "img", kd, base)):
                return mo.group(0)
        if re.search(r"\.(png|jpe?g)$", base):
            return "`print real`"
        return mo.group(0)
    t = re.sub(r"`([^`\n]*?(?:\.(?:png|jpe?g)|…[^`\n]*))`", repl, t)
    for pat, rep in STAFF_PATTERNS:
        t = re.sub(pat, rep, t)
    for name in NAME_SCRUB:
        t = re.sub(r"(?<![A-Za-zÀ-ÿ0-9-])" + re.escape(name) + r"(?![A-Za-zÀ-ÿ0-9-])", "[cliente]", t, flags=re.I)
    return t


def drop_sections(md, titles):
    out, skip = [], False
    for line in md.split("\n"):
        if line.startswith("## ") or line.startswith("### "):
            skip = any(line.lstrip("# ").startswith(tt) for tt in titles)
        if not skip:
            out.append(line)
    return "\n".join(out)


def deny_scan(root):
    hits = []
    for dp, dn, fn in os.walk(root):
        for f in fn:
            if not f.endswith((".md", ".json", ".html", ".csv", ".txt", ".py", ".js", ".css")):
                continue
            p = os.path.join(dp, f)
            low = open(p, encoding="utf-8", errors="ignore").read().lower()
            for w in DENY:
                if re.search(r"(?<![a-z0-9])" + re.escape(w) + r"(?![a-z0-9])", low):
                    hits.append((os.path.relpath(p, root), w))
    return hits


def referenced_kit_files():
    refs = set()
    for s in shorts():
        html = open(os.path.join(s["dir"], "index.html"), encoding="utf-8").read()
        refs.update(re.findall(r"kit/((?:img|video)/[A-Za-z0-9_./-]+?\.(?:png|jpe?g|mp4|svg|webp|gif))", html))
    return refs


def sync_studio():
    base = os.path.join(OUT, "studio")
    os.makedirs(base, exist_ok=True)
    smap = source_map()
    for sub in ("docs", "tools", "kit", "template"):
        dst = os.path.join(base, sub)
        if os.path.exists(dst):
            shutil.rmtree(dst)
    shutil.copytree(os.path.join(STUDIO, "tools"), os.path.join(base, "tools"), ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    shutil.copytree(os.path.join(STUDIO, "template"), os.path.join(base, "template"))
    # kit: code, fonts, sfx, brand; only the prints/clips the shorts actually use
    kit_src, kit_dst = os.path.join(STUDIO, "kit"), os.path.join(base, "kit")
    for sub in ("css", "js", "fonts", "sfx", os.path.join("img", "brand")):
        shutil.copytree(os.path.join(kit_src, sub), os.path.join(kit_dst, sub), ignore=shutil.ignore_patterns("pix-logo.png"))
    for rel in sorted(referenced_kit_files()):
        sp = os.path.join(kit_src, rel)
        if os.path.exists(sp):
            os.makedirs(os.path.dirname(os.path.join(kit_dst, rel)), exist_ok=True)
            shutil.copy2(sp, os.path.join(kit_dst, rel))
    # docs: sanitized copies; the raw research brief (it quotes names) stays out
    ddst = os.path.join(base, "docs")
    for dp, dn, fn in os.walk(os.path.join(STUDIO, "docs")):
        for f in fn:
            src = os.path.join(dp, f)
            rel = os.path.relpath(src, os.path.join(STUDIO, "docs"))
            if rel == os.path.join("research", "kizubot-brief.md"):
                continue
            os.makedirs(os.path.dirname(os.path.join(ddst, rel)), exist_ok=True)
            t = open(src, encoding="utf-8").read()
            if f == "ASSETS.md":
                t = drop_sections(t, ["Site caption errors", "Excluded files", "Source file"])
                t += "\n\n_Public copy: the excluded-files list and the source-filename map are kept out of this repository because the original filenames contain customers' names._\n"
            open(os.path.join(ddst, rel), "w", encoding="utf-8").write(scrub_text(t, smap))
    with open(os.path.join(base, "package.json"), "w") as f:
        json.dump({"name": "kizubot-shorts-studio", "private": True,
                   "dependencies": {"hyperframes": "0.8.114", "gsap": "3.14.2"}}, f, indent=2)
        f.write("\n")


def sync_sources():
    smap = source_map()
    n = 0
    for s in shorts():
        src_dst = os.path.join(OUT, "studio", "shorts", s["name"])
        os.makedirs(src_dst, exist_ok=True)
        for f in ("index.html", "audio.json", "meta.json"):
            fp = os.path.join(s["dir"], f)
            if os.path.exists(fp):
                t = open(fp, encoding="utf-8").read()
                open(os.path.join(src_dst, f), "w", encoding="utf-8").write(scrub_text(t, smap) if f != "audio.json" else t)
        link = os.path.join(src_dst, "kit")
        if not os.path.lexists(link):
            os.symlink("../../kit", link)
        n += 1
    return n


def frame_grid(items, path, t=1.0):
    """One frame per short, 10 per row, captioned with the id."""
    tmp = os.path.join(STUDIO, ".grid_tmp")
    shutil.rmtree(tmp, ignore_errors=True)
    os.makedirs(tmp)
    inputs = []
    for i, s in enumerate(items):
        src = os.path.join(OUT, s["name"] + ".mp4")
        png = os.path.join(tmp, f"{i:03d}.png")
        at = s["meta"].get("grid_frame", t)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(at), "-i", src, "-frames:v", "1",
                        "-vf", f"scale=216:384,drawtext=text='{s['id']}':x=10:y=10:fontsize=26:fontcolor=white:box=1:boxcolor=black@0.6:boxborderw=6",
                        png], check=False)
        inputs.append(png)
    cols = 10
    rows = (len(inputs) + cols - 1) // cols
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-framerate", "1", "-i", os.path.join(tmp, "%03d.png"),
                    "-vf", f"tile={cols}x{rows}:padding=6:margin=6:color=0x0b0712", "-frames:v", "1", "-q:v", "3", path], check=False)
    shutil.rmtree(tmp, ignore_errors=True)


def build_index():
    items = [s for s in shorts() if os.path.exists(os.path.join(OUT, s["name"] + ".mp4"))]
    rows = []
    for s in items:
        n = int(s["id"])
        code, sname = series_of(n)
        m = s["meta"]
        q = s["qc"] or {}
        rows.append(dict(id=s["id"], file=s["name"] + ".mp4", series=f"{code} {sname}", title=m.get("title", ""),
                         hook=m.get("hook", ""), neuro=", ".join(m.get("neuro", [])), duration=q.get("duration"),
                         size_mb=round(os.path.getsize(os.path.join(OUT, s["name"] + ".mp4")) / 1e6, 1),
                         platforms=m.get("platforms", {}), pinned_comment=m.get("pinned_comment", ""),
                         claims=m.get("claims", []), assets=m.get("assets", [])))
    smap = source_map()
    rows = json.loads(scrub_text(json.dumps(rows, ensure_ascii=False), smap))
    json.dump(rows, open(os.path.join(OUT, "metadata.json"), "w"), ensure_ascii=False, indent=2)
    with open(os.path.join(OUT, "metadata.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["id", "file", "series", "title", "duration_s", "hook", "neuro",
                    "tiktok_caption", "tiktok_hashtags", "youtube_title", "youtube_description", "youtube_hashtags",
                    "instagram_caption", "instagram_hashtags", "pinned_comment"])
        for r in rows:
            p = r["platforms"]
            w.writerow([r["id"], r["file"], r["series"], r["title"], r["duration"], r["hook"], r["neuro"],
                        p.get("tiktok", {}).get("caption", ""), " ".join(p.get("tiktok", {}).get("hashtags", [])),
                        p.get("youtube", {}).get("title", ""), p.get("youtube", {}).get("description", ""),
                        " ".join(p.get("youtube", {}).get("hashtags", [])),
                        p.get("instagram", {}).get("caption", ""), " ".join(p.get("instagram", {}).get("hashtags", [])),
                        r["pinned_comment"]])
    # grids of 20
    grids = []
    for g in range(0, len(items), 20):
        chunk = items[g:g + 20]
        name = f"grid-{g // 20 + 1:02d}.jpg"
        frame_grid(chunk, os.path.join(OUT, name))
        grids.append((name, chunk[0]["id"], chunk[-1]["id"]))
    return rows, grids


SERIES_LEVERS = {
    "F01": "aversão à perda + ancoragem", "F02": "autorreferência + narrativa", "F03": "lacuna de curiosidade + compromisso (palpite)",
    "F04": "antecipação / recompensa variável", "F05": "loop aberto (o #1 no fim)", "F06": "humor (violação benigna) + ancoragem",
    "F07": "identidade de grupo + humor + compartilhamento", "F08": "interrupção de padrão (ligação)", "F09": "recompensa sensorial + loop",
    "F10": "escolha + contraste", "F11": "identidade + incongruência", "F12": "novidade + FOMO + autoridade",
    "F13": "superioridade da imagem + competência", "F14": "prova social + contágio emocional", "F15": "suspense + humor + sazonalidade (Halloween)",
    "F16": "pressão de tempo + fluência + loop", "F17": "empilhamento de valor + ancoragem + nostalgia", "F18": "participação + rewatch + efeito Von Restorff",
    "F19": "aspiração / future pacing", "F20": "transporte narrativo + quebra de expectativa",
}


def write_readme(rows, grids):
    L = []
    L.append("# Série Neuro (041–140)\n")
    L.append("Cem shorts verticais (1080×1920, 30 fps, 12–25 s) para o KizuBot, feitos inteiramente em código: composições HTML/GSAP renderizadas com [HyperFrames](https://github.com/heygen-com/hyperframes), trilha original sintetizada (sem samples nem licenças) e efeitos sonoros, com áudio normalizado em −14 LUFS. Cada short aplica de propósito uma ou mais técnicas de neuromarketing e retenção, e usa só material real: o logo oficial, prints de clientes publicados no kizubot.com (com nomes, rostos e dados pessoais removidos) e gameplay real do site.\n")
    for name, a, b in grids:
        L.append(f'<p align="center"><img src="{name}" width="100%" alt="Um frame de cada short de {a} a {b}"></p>\n')
    L.append("## Como a série foi pensada\n")
    L.append("Vinte formatos recorrentes × cinco episódios. Formato recorrente é o que faz o público reconhecer o vídeo em meio segundo, maratonar a série e lembrar da marca (efeito de mera exposição). Todos seguem as mesmas regras: gancho legível em 0,4 s com movimento e som no primeiro frame, um novo motivo para continuar assistindo a cada 5–7 s, revelação no drop da música, prova real, card final com logo, brilho no olho do robô, kizubot.com e o mesmo logo sonoro, e final que emenda no começo para virar loop.\n")
    L.append("| Série | IDs | Alavanca principal |")
    L.append("| --- | --- | --- |")
    for code, name, a, b in SERIES:
        L.append(f"| {code} {name} | {a:03d}–{b:03d} | {SERIES_LEVERS.get(code, '')} |")
    L.append("")
    L.append("## Os 100 shorts\n")
    L.append("| # | Arquivo | Série | Título | Gancho | Técnicas |")
    L.append("| --- | --- | --- | --- | --- | --- |")
    for r in rows:
        hook = r["hook"].replace("|", "/")
        L.append(f"| {r['id']} | [`{r['file']}`]({r['file']}) | {r['series']} | {r['title']} | {hook} | {r['neuro']} |")
    L.append("")
    L.append("Legendas, títulos, descrições, hashtags e comentário fixado por plataforma (TikTok, YouTube Shorts e Instagram Reels) estão em [`metadata.json`](metadata.json) e [`metadata.csv`](metadata.csv).\n")
    L.append("## Regras de conteúdo\n")
    L.append("- Só afirmações aprovadas (100% AFK, uso com PC desligado, acesso pelo celular, alarmes no WhatsApp, detecção de shinys/megas/bosses, Humanização, planos a partir de R$ 250/mês) e fatos do changelog público. Contas feitas só sobre esses números (R$ 250 ÷ 30 ≈ R$ 8,33/dia).")
    L.append("- Nada de \"sem ban\", \"100% seguro\", \"últimas vagas\", garantia como devolução de dinheiro, valores em reais ou números inventados.")
    L.append("- Prints reais, citados palavra por palavra e marcados como \"print real de cliente\"; quando juntam clientes diferentes, o vídeo diz isso. Prints com membros da staff do PxG ficaram de fora.")
    L.append("- Sem arte oficial de Pokémon/Nintendo/PxG e sem imitar a identidade visual de apps de terceiros.\n")
    L.append("## Para publicar\n")
    L.append("- Melhores horários para testar (BRT): dias úteis 12:00–13:30 e 18:30–22:30; fim de semana 10:00–13:00 e 19:00–23:00.")
    L.append("- No TikTok, ative a divulgação de conteúdo comercial (\"Sua marca\"): conteúdo comercial sem divulgação não entra no Para Você.")
    L.append("- Alterne as séries ao publicar (um formato por vez cansa) e mantenha o comentário fixado de cada vídeo.\n")
    L.append("## Como refazer ou editar\n")
    L.append("As fontes de cada short estão em [`studio/shorts/`](studio/shorts/) (`index.html`, `audio.json`, `meta.json`), com o kit compartilhado, as ferramentas e os documentos de produção em [`studio/`](studio/). Com Node 22, FFmpeg e Python 3 (numpy, scipy, soundfile, pyloudnorm):\n")
    L.append("```bash\ncd studio && npm install && npx hyperframes browser ensure\npython3 tools/kz.py render shorts/041-a-conta\n```\n")
    L.append("Fontes: OFL/Apache (Google Fonts e o starter kit). Efeitos `px-*`: Pixabay Content License. Trilhas e demais efeitos: sintetizados em `studio/tools/kzaudio.py`.\n")
    open(os.path.join(OUT, "README.md"), "w").write("\n".join(L) + "\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--ids")
    ap.add_argument("--index", action="store_true")
    ap.add_argument("--studio", action="store_true")
    ap.add_argument("--sources", action="store_true", help="copy index.html/audio.json/meta.json of every short (no mp4)")
    ap.add_argument("--scan", action="store_true", help="privacy scan of the repo output")
    a = ap.parse_args()
    if a.check:
        ok = 0
        for s in shorts():
            q = s["qc"]
            state = "missing" if not q else ("OK" if q.get("ok") else "ISSUES " + "; ".join(q.get("issues", [])))
            meta = "meta" if s["meta"].get("platforms", {}).get("youtube", {}).get("title") else "NO-META"
            print(f"{s['name']:40s} {state:10s} {meta}")
            ok += bool(q and q.get("ok"))
        print(f"{ok} shorts pass QC")
    if a.ids:
        want = parse_ids(a.ids)
        for s in shorts():
            if int(s["id"]) in want:
                if not (s["qc"] and s["qc"].get("ok")):
                    print("skip (QC not ok):", s["name"])
                    continue
                print("copied", copy_short(s))
    if a.studio:
        sync_studio()
        print("studio synced")
    if a.sources:
        print(f"sources synced for {sync_sources()} shorts")
    if a.scan or a.studio or a.sources or a.index:
        hits = deny_scan(OUT)
        if hits:
            for h in hits[:40]:
                print("PRIVACY HIT:", h)
            raise SystemExit(f"{len(hits)} privacy hits in {OUT} — fix before committing")
        print("privacy scan: clean")
    if a.index:
        rows, grids = build_index()
        write_readme(rows, grids)
        print(f"index: {len(rows)} shorts, grids: {grids}")


if __name__ == "__main__":
    main()
