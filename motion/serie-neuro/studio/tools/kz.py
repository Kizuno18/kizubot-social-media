#!/usr/bin/env python3
"""kz - production CLI for the KizuBot motion shorts.

  python3 tools/kz.py new  <dir>                 scaffold a short from the template (dir = shorts/NNN-slug)
  python3 tools/kz.py audio <dir>                render <dir>/audio.json -> <dir>/audio/mix.wav
  python3 tools/kz.py snap <dir> 0.3 4.2 9.8     PNG frames (cheap visual check) -> <dir>/snapshots/
  python3 tools/kz.py render <dir> [--draft]     lint, audio, queued render, mux, QC -> <dir>/renders/final.mp4
  python3 tools/kz.py qc <dir>                   QC an existing final.mp4 (probe, loudness, black frames, sheet)

Renders are serialized through a lock file so parallel agents never fight for the CPU:
only one `hyperframes render` (3 workers) runs at a time; everyone else waits in line.
"""
import fcntl
import json
import os
import re
import shutil
import subprocess
import sys
import time

STUDIO = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
TOOLS = os.path.join(STUDIO, "tools")
KIT = os.path.join(STUDIO, "kit")
LOCK = os.path.join(STUDIO, ".render.lock")
SNAP_LOCK = os.path.join(STUDIO, ".snap.lock")
HF = ["npx", "--prefix", STUDIO, "hyperframes"]


def sh(cmd, cwd=None, check=True, capture=True, env=None):
    r = subprocess.run(cmd, cwd=cwd, text=True, capture_output=capture, env=env)
    if check and r.returncode != 0:
        sys.stderr.write((r.stdout or "") + (r.stderr or ""))
        raise SystemExit(f"command failed ({r.returncode}): {' '.join(cmd)}")
    return r


def comp_duration(d):
    html = open(os.path.join(d, "index.html"), encoding="utf-8").read()
    m = re.search(r'data-composition-id="[^"]+"[^>]*?data-duration="([\d.]+)"', html, re.S) or re.search(r'data-duration="([\d.]+)"', html)
    return float(m.group(1)) if m else None


def ensure_kit_link(d):
    link = os.path.join(d, "kit")
    if not os.path.exists(link):
        os.symlink(os.path.relpath(KIT, d), link)


def cmd_new(d):
    if os.path.exists(os.path.join(d, "index.html")):
        raise SystemExit(f"{d}/index.html exists")
    os.makedirs(d, exist_ok=True)
    tpl = os.path.join(STUDIO, "template")
    for f in os.listdir(tpl):
        src = os.path.join(tpl, f)
        if os.path.isfile(src):
            shutil.copy(src, os.path.join(d, f))
    ensure_kit_link(d)
    print(f"scaffolded {d}: edit index.html, audio.json, meta.json")


def cmd_audio(d):
    d = os.path.abspath(d)
    spec = os.path.join(d, "audio.json")
    if not os.path.exists(spec):
        raise SystemExit(f"no {spec}")
    dur = comp_duration(d)
    j = json.load(open(spec))
    if dur and abs(float(j.get("duration", 0)) - dur) > 0.01:
        raise SystemExit(f"audio.json duration {j.get('duration')} != composition data-duration {dur}")
    out = os.path.join(d, "audio", "mix.wav")
    r = sh([sys.executable, os.path.join(TOOLS, "kzaudio.py"), spec, "-o", out])
    print(r.stdout.strip())
    return out


def lint(d):
    r = sh(HF + ["lint", "."], cwd=d, check=False)
    txt = (r.stdout or "") + (r.stderr or "")
    m = re.search(r"(\d+) error\(s\), (\d+) warning\(s\)", txt)
    errs = int(m.group(1)) if m else (0 if r.returncode == 0 else 1)
    if errs:
        sys.stderr.write(txt)
        raise SystemExit(f"lint: {errs} error(s) in {d}")
    warn_lines = [l.strip() for l in txt.splitlines() if l.strip().startswith("⚠") and "nested_structure_needs_subcomposition" not in l and "studio_missing_editable_id" not in l and "timed_element_missing_clip_class" not in l]
    for l in warn_lines[:12]:
        print("  lint warn:", l[:220])
    return warn_lines


def cmd_snap(d, times):
    d = os.path.abspath(d)
    ensure_kit_link(d)
    out = os.path.join(d, "snapshots")
    shutil.rmtree(out, ignore_errors=True)  # keep disk use flat across iterations
    os.makedirs(out, exist_ok=True)
    args = HF + ["snapshot", ".", "-o", out, "--no-end", "--describe", "false"]
    if times:
        args += ["--at", ",".join(times)]
    with RenderLock(SNAP_LOCK, slots=2):
        r = sh(args, cwd=d, check=False)
    txt = (r.stdout or "") + (r.stderr or "")
    if r.returncode != 0:
        sys.stderr.write(txt[-3000:])
        raise SystemExit("snapshot failed")
    pngs = sorted(f for f in os.listdir(out) if f.endswith(".png"))
    # build one small sheet so the reviewer opens one image instead of many
    if pngs:
        sheet = os.path.join(out, "_sheet.jpg")
        inputs = []
        for p in pngs[-12:]:
            inputs += ["-i", os.path.join(out, p)]
        n = len(inputs) // 2
        filt = "".join(f"[{i}:v]scale=270:480[s{i}];" for i in range(n)) + "".join(f"[s{i}]" for i in range(n)) + f"hstack=inputs={n}" if n > 1 else "[0:v]scale=270:480"
        sh(["ffmpeg", "-v", "error", "-y"] + inputs + ["-filter_complex", filt, "-frames:v", "1", sheet], check=False)
        print("snapshots:", ", ".join(pngs[-12:]), "| sheet:", sheet)


class RenderLock:
    """Exclusive lock (renders) or an N-slot semaphore (snapshots) built on flock."""

    def __init__(self, path=None, slots=1):
        self.path = path or LOCK
        self.slots = slots

    def __enter__(self):
        t0 = time.time()
        if self.slots == 1:
            self.f = open(self.path, "a+")
            fcntl.flock(self.f, fcntl.LOCK_EX)
        else:
            self.f = None
            while self.f is None:
                for i in range(self.slots):
                    f = open(f"{self.path}.{i}", "a+")
                    try:
                        fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
                        self.f = f
                        break
                    except OSError:
                        f.close()
                if self.f is None:
                    time.sleep(0.5)
        waited = time.time() - t0
        if waited > 1:
            print(f"  (waited {waited:.0f}s in the queue)")
        return self

    def __exit__(self, *a):
        fcntl.flock(self.f, fcntl.LOCK_UN)
        self.f.close()


def cmd_render(d, draft=False):
    d = os.path.abspath(d)
    ensure_kit_link(d)
    dur = comp_duration(d)
    if not dur:
        raise SystemExit("root data-duration missing")
    lint(d)
    mix = cmd_audio(d) if os.path.exists(os.path.join(d, "audio.json")) else None
    os.makedirs(os.path.join(d, "renders"), exist_ok=True)
    silent = os.path.join(d, "renders", "video.mp4")
    q = ["--quality", "draft"] if draft else ["--crf", "19"]
    with RenderLock():
        t0 = time.time()
        r = sh(HF + ["render", ".", "-w", "3", "-o", silent, "--quiet"] + q, cwd=d, check=False)
        took = time.time() - t0
    txt = (r.stdout or "") + (r.stderr or "")
    if r.returncode != 0 or not os.path.exists(silent):
        sys.stderr.write(txt[-4000:])
        raise SystemExit("render failed")
    print(f"  rendered video in {took:.0f}s")
    final = os.path.join(d, "renders", "final.mp4")
    if mix:
        # audio.json or the audio engine may have changed while the render waited in the queue
        srcs = [os.path.join(d, "audio.json"), os.path.join(TOOLS, "kzaudio.py")]
        if not os.path.exists(mix) or max(os.path.getmtime(p) for p in srcs) > os.path.getmtime(mix):
            mix = cmd_audio(d)
        sh(["ffmpeg", "-v", "error", "-y", "-i", silent, "-i", mix, "-map", "0:v:0", "-map", "1:a:0",
            "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
            "-t", f"{dur:.3f}", "-movflags", "+faststart", final])
    else:
        sh(["ffmpeg", "-v", "error", "-y", "-i", silent, "-c", "copy", "-movflags", "+faststart", final])
    try:
        os.remove(silent)
    except OSError:
        pass
    cmd_qc(d)


def ebur128(path):
    r = sh(["ffmpeg", "-hide_banner", "-nostats", "-i", path, "-filter_complex", "ebur128=peak=true", "-f", "null", "-"], check=False)
    txt = r.stderr
    i = re.findall(r"I:\s+(-?[\d.]+) LUFS", txt)
    tp = re.findall(r"Peak:\s+(-?[\d.]+) dBFS", txt)
    return (float(i[-1]) if i else None, float(tp[-1]) if tp else None)


def cmd_qc(d):
    d = os.path.abspath(d)
    final = os.path.join(d, "renders", "final.mp4")
    if not os.path.exists(final):
        raise SystemExit("no renders/final.mp4")
    dur = comp_duration(d)
    pr = json.loads(sh(["ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", final]).stdout)
    v = next(s for s in pr["streams"] if s["codec_type"] == "video")
    a = next((s for s in pr["streams"] if s["codec_type"] == "audio"), None)
    fdur = float(pr["format"]["duration"])
    num, den = v["r_frame_rate"].split("/")
    fps = float(num) / float(den)
    lufs, tp = ebur128(final) if a else (None, None)
    bd = sh(["ffmpeg", "-hide_banner", "-nostats", "-i", final, "-vf", "blackdetect=d=0.6:pix_th=0.06", "-an", "-f", "null", "-"], check=False).stderr
    blacks = re.findall(r"black_start:([\d.]+) black_end:([\d.]+)", bd)
    fz = sh(["ffmpeg", "-hide_banner", "-nostats", "-i", final, "-vf", "freezedetect=n=0.002:d=2.5", "-an", "-f", "null", "-"], check=False).stderr
    freezes = re.findall(r"freeze_start: ([\d.]+)", fz)
    size_mb = os.path.getsize(final) / 1e6
    issues = []
    if (v["width"], v["height"]) != (1080, 1920):
        issues.append(f"resolution {v['width']}x{v['height']}")
    if abs(fps - 30) > 0.01 and abs(fps - 60) > 0.01:
        issues.append(f"fps {fps}")
    if dur and abs(fdur - dur) > 0.08:
        issues.append(f"duration {fdur:.2f} vs composition {dur}")
    if not a:
        issues.append("no audio stream")
    else:
        if lufs is None or abs(lufs + 14) > 1.0:
            issues.append(f"loudness {lufs} LUFS (want -14 +-1)")
        if tp is not None and tp > -0.9:
            issues.append(f"true peak {tp} dBFS (want <= -1)")
    if blacks:
        issues.append("black segments " + ", ".join(f"{float(s):.2f}-{float(e):.2f}" for s, e in blacks))
    if size_mb > 30:
        issues.append(f"file {size_mb:.1f} MB (too big)")
    # contact sheet: one frame every 1.5 s, 8 per row; plus the hook frame
    sheet = os.path.join(d, "renders", "sheet.jpg")
    n = max(1, int(fdur / 1.5))
    cols = 8
    rows = (n + cols - 1) // cols
    sh(["ffmpeg", "-v", "error", "-y", "-i", final, "-vf", f"fps=1/1.5,scale=216:384,tile={cols}x{rows}:padding=4:color=0x222222", "-frames:v", "1", sheet], check=False)
    sh(["ffmpeg", "-v", "error", "-y", "-ss", "0.4", "-i", final, "-frames:v", "1", "-vf", "scale=540:960", os.path.join(d, "renders", "hook.jpg")], check=False)
    qc = dict(file=final, duration=round(fdur, 3), composition_duration=dur, fps=fps, width=v["width"], height=v["height"],
              vcodec=v["codec_name"], acodec=a["codec_name"] if a else None, lufs=lufs, true_peak=tp,
              black_segments=blacks, freezes_over_2_5s=freezes, size_mb=round(size_mb, 2), issues=issues,
              sheet=sheet, ok=not issues)
    json.dump(qc, open(os.path.join(d, "renders", "qc.json"), "w"), indent=2)
    status = "OK" if not issues else "ISSUES: " + "; ".join(issues)
    print(f"  QC {os.path.basename(d)}: {fdur:.2f}s {v['width']}x{v['height']} {fps:g}fps {size_mb:.1f}MB LUFS {lufs} TP {tp} freezes {freezes or '-'} -> {status}")
    print(f"  sheet: {sheet}")
    return qc


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    c, d = sys.argv[1], sys.argv[2]
    if c == "new":
        cmd_new(d)
    elif c == "audio":
        cmd_audio(d)
    elif c == "snap":
        cmd_snap(d, sys.argv[3:])
    elif c == "render":
        cmd_render(d, draft="--draft" in sys.argv)
    elif c == "qc":
        cmd_qc(d)
    else:
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    sys.stdout.reconfigure(line_buffering=True)  # progress shows up in redirected logs
    main()
