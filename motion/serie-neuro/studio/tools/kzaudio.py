#!/usr/bin/env python3
"""kzaudio - original soundtrack + SFX mixer for the KizuBot motion shorts.

Everything here is synthesized in code (no samples, no licences), except the
optional SFX files in kit/sfx (starter-kit sounds made in code, and Pixabay
sounds under the Pixabay Content License).

Usage
  python3 kzaudio.py audio.json -o audio/mix.wav      # render the mix
  python3 kzaudio.py --beats 128 20                    # print the beat grid
  python3 kzaudio.py --list                            # styles and sfx names

audio.json
  {
    "duration": 20.0,              # seconds, must equal the composition length
    "style": "phonk",              # see STYLES
    "bpm": 130,                    # optional, style default otherwise
    "seed": 41,                    # varies melody / progression / fills
    "root": "A",                   # optional key root (minor keys)
    "sections": [                  # optional; default: groove then drop then outro
      {"at": 0.0,  "type": "groove"},
      {"at": 7.4,  "type": "build"},
      {"at": 9.25, "type": "drop"},
      {"at": 17.0, "type": "outro"}
    ],
    "stops": [{"at": 6.0, "len": 0.45, "tape": true}],   # music cut-outs
    "sfx": [{"t": 0.0, "name": "impact"}, {"t": 1.2, "name": "whoosh", "gain": -9}],
    "logo": 17.6,                  # KizuBot sonic logo time (null to skip)
    "music_gain": 0.0,             # dB trim for the music bed
    "fade_out": 0.6                # seconds
  }

Section types: intro, groove, build, drop, break, outro, silence.
The master is normalized to -14 LUFS integrated with peaks under -1 dBFS.
"""
import argparse
import json
import math
import os
import sys

import numpy as np
import pyloudnorm as pyln
import soundfile as sf
from scipy import signal

SR = 48000
HERE = os.path.dirname(os.path.abspath(__file__))
KIT_SFX = os.path.normpath(os.path.join(HERE, "..", "kit", "sfx"))

NOTE = {"C": 0, "C#": 1, "Db": 1, "D": 2, "D#": 3, "Eb": 3, "E": 4, "F": 5, "F#": 6,
        "Gb": 6, "G": 7, "G#": 8, "Ab": 8, "A": 9, "A#": 10, "Bb": 10, "B": 11}
MINOR = [0, 2, 3, 5, 7, 8, 10]
MAJOR = [0, 2, 4, 5, 7, 9, 11]
PENTA_MINOR = [0, 3, 5, 7, 10]


# --------------------------------------------------------------------------- dsp
def mtof(m):
    return 440.0 * 2 ** ((m - 69) / 12.0)


def tt(dur):
    return np.arange(max(1, int(round(dur * SR)))) / SR


def sos_filter(x, kind, fc, order=2):
    nyq = SR / 2
    if kind == "band":
        lo, hi = fc
        lo = max(10, min(lo, nyq * 0.95))
        hi = max(lo * 1.05, min(hi, nyq * 0.98))
        sos = signal.butter(order, [lo, hi], "bandpass", fs=SR, output="sos")
    else:
        fc = max(10, min(fc, nyq * 0.98))
        sos = signal.butter(order, fc, "low" if kind == "low" else "high", fs=SR, output="sos")
    return signal.sosfilt(sos, x, axis=0)


def lp(x, fc, order=2):
    return sos_filter(x, "low", fc, order)


def hp(x, fc, order=2):
    return sos_filter(x, "high", fc, order)


def bp(x, lo, hi, order=2):
    return sos_filter(x, "band", (lo, hi), order)


def fade(x, fin=0.002, fout=0.01):
    n = len(x)
    a = min(n, int(fin * SR))
    b = min(n, int(fout * SR))
    if a > 0:
        r = np.linspace(0, 1, a)
        x[:a] *= r[:, None] if x.ndim == 2 else r
    if b > 0:
        r = np.linspace(1, 0, b)
        x[n - b:] *= r[:, None] if x.ndim == 2 else r
    return x


def polyblep(ph, dt):
    out = np.zeros_like(ph)
    m = ph < dt
    x = ph[m] / dt[m]
    out[m] = x + x - x * x - 1.0
    m = ph > 1.0 - dt
    x = (ph[m] - 1.0) / dt[m]
    out[m] = x * x + x + x + 1.0
    return out


def phase_of(freq, n, start=0.0):
    f = np.broadcast_to(np.asarray(freq, dtype=float), (n,))
    dt = f / SR
    ph = (start + np.cumsum(dt) - dt) % 1.0
    return ph, dt


def saw(freq, n, start=0.0):
    ph, dt = phase_of(freq, n, start)
    return 2.0 * ph - 1.0 - polyblep(ph, dt)


def square(freq, n, duty=0.5, start=0.0):
    ph, dt = phase_of(freq, n, start)
    s1 = 2.0 * ph - 1.0 - polyblep(ph, dt)
    ph2 = (ph + duty) % 1.0
    s2 = 2.0 * ph2 - 1.0 - polyblep(ph2, dt)
    return 0.5 * (s1 - s2)


def tri(freq, n):
    ph, _ = phase_of(freq, n)
    return 2.0 * np.abs(2.0 * ph - 1.0) - 1.0


def sine(freq, n, start=0.0):
    ph, _ = phase_of(freq, n, start)
    return np.sin(2 * np.pi * ph)


def adsr(n, a=0.005, d=0.1, s=0.7, r=0.1):
    e = np.ones(n) * s
    ai, di, ri = int(a * SR), int(d * SR), int(r * SR)
    ai = min(ai, n)
    e[:ai] = np.linspace(0, 1, ai) if ai else e[:ai]
    di2 = min(di, max(0, n - ai))
    if di2:
        e[ai:ai + di2] = np.linspace(1, s, di2)
    ri = min(ri, n)
    if ri:
        e[n - ri:] *= np.linspace(1, 0, ri)
    return e


def expenv(n, tau):
    return np.exp(-np.arange(n) / SR / max(tau, 1e-4))


def sat(x, drive=1.5):
    return np.tanh(x * drive) / np.tanh(drive)


def to_stereo(x, pan=0.0, width=0.0):
    """Constant-power pan; width>0 adds a short Haas offset on one side."""
    if x.ndim == 2:
        return x
    l = math.cos((pan + 1) * math.pi / 4)
    r = math.sin((pan + 1) * math.pi / 4)
    out = np.stack([x * l, x * r], axis=1)
    if width > 0:
        d = int(width * 0.012 * SR)
        if d > 0:
            out[d:, 1] = out[:-d, 1].copy()
            out[:d, 1] = 0
    return out


def add(buf, x, t, gain=1.0):
    i = int(round(t * SR))
    if i >= len(buf) or len(x) == 0:
        return
    if i < 0:
        x = x[-i:]
        i = 0
    n = min(len(x), len(buf) - i)
    if x.ndim == 1:
        x = to_stereo(x)
    buf[i:i + n] += x[:n] * gain


def db(g):
    return 10 ** (g / 20.0)


_IR_CACHE = {}


def reverb_ir(size=1.6, damp=5000.0, seed=7):
    key = (round(size, 2), round(damp), seed)
    if key in _IR_CACHE:
        return _IR_CACHE[key]
    rng = np.random.default_rng(seed)
    n = int(size * SR)
    t = np.arange(n) / SR
    env = np.exp(-t * 6.9 / size)
    ir = np.zeros((n, 2))
    for c in range(2):
        noise = rng.standard_normal(n)
        noise = lp(noise, damp)
        # high frequencies die faster than lows
        bright = hp(noise, 2500) * np.exp(-t * 14.0 / size)
        ir[:, c] = (noise * 0.8 + bright * 0.5) * env
    ir[: int(0.006 * SR)] *= np.linspace(0, 1, int(0.006 * SR))[:, None]
    ir /= np.sqrt(np.sum(ir ** 2) / 2)
    _IR_CACHE[key] = ir
    return ir


def reverb(x, size=1.6, wet=0.25, damp=5000.0, pre=0.012, dry=True):
    x = to_stereo(x) if x.ndim == 1 else x
    ir = reverb_ir(size, damp)
    y = np.zeros((len(x) + len(ir), 2))
    for c in range(2):
        y[: len(x) + len(ir) - 1, c] = signal.fftconvolve(x[:, c], ir[:, c])
    y = hp(y, 180)
    p = int(pre * SR)
    wetsig = np.zeros_like(y)
    wetsig[p:] = y[: len(y) - p]
    L = len(x) + int(size * SR * 0.6)
    if not dry:
        return wetsig[:L] * wet
    out = np.zeros_like(y)
    out[: len(x)] = x
    return out[:L] * (1 - wet * 0.3) + wetsig[:L] * wet


def delay(x, time, fb=0.35, wet=0.25, n_taps=4):
    x = to_stereo(x) if x.ndim == 1 else x
    d = int(time * SR)
    out = np.zeros((len(x) + d * n_taps, 2))
    out[: len(x)] += x
    g = wet
    for k in range(1, n_taps + 1):
        tap = x * g
        if k % 2:
            tap = tap[:, ::-1]  # ping-pong
        out[k * d: k * d + len(x)] += lp(tap, 6000)
        g *= fb
    return out


# ---------------------------------------------------------------- instruments
def kick(kind="punch", note_hz=50.0):
    if kind == "808":
        n = int(1.1 * SR)
        t = np.arange(n) / SR
        f = note_hz + (115 - note_hz) * np.exp(-t / 0.045)
        body = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.55)
        k = sat(body * 1.0, 2.6) + 0.45 * bp(sat(body * 3.0, 4.0), 160, 1400)
    elif kind == "soft":
        n = int(0.4 * SR)
        t = np.arange(n) / SR
        f = 48 + 90 * np.exp(-t / 0.05)
        k = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.22)
        k = lp(k, 900)
    elif kind == "hard":
        n = int(0.5 * SR)
        t = np.arange(n) / SR
        f = 46 + 190 * np.exp(-t / 0.03)
        body = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.28)
        click = hp(np.random.default_rng(3).standard_normal(n), 1800) * np.exp(-t / 0.004)
        k = sat(body * 1.4 + click * 0.35, 2.2)
    else:  # punch
        n = int(0.45 * SR)
        t = np.arange(n) / SR
        f = 50 + 110 * np.exp(-t / 0.05)
        body = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.3)
        click = hp(np.random.default_rng(5).standard_normal(n), 2200) * np.exp(-t / 0.003)
        k = sat(body + click * 0.25, 1.6)
    return fade(k * 0.95, 0.0005, 0.02)


def snare(kind="tight", seed=11):
    rng = np.random.default_rng(seed)
    if kind == "trap":
        n = int(0.32 * SR)
        t = np.arange(n) / SR
        tone = np.sin(2 * np.pi * np.cumsum(230 - 40 * (1 - np.exp(-t / 0.02))) / SR) * np.exp(-t / 0.05)
        noise = bp(rng.standard_normal(n), 1500, 9000) * np.exp(-t / 0.13)
        s = tone * 0.6 + noise * 0.9
    elif kind == "gated":
        n = int(0.42 * SR)
        t = np.arange(n) / SR
        tone = np.sin(2 * np.pi * 190 * t) * np.exp(-t / 0.06)
        noise = bp(rng.standard_normal(n), 900, 8000) * np.exp(-t / 0.5)
        gate = np.where(t < 0.28, 1.0, np.exp(-(t - 0.28) / 0.015))
        s = (tone * 0.5 + noise * 0.9) * gate
        s = to_stereo(s)
        s = reverb(s, 0.9, 0.35)[:n]
        return fade(s * 0.9)
    elif kind == "lofi":
        n = int(0.3 * SR)
        t = np.arange(n) / SR
        tone = np.sin(2 * np.pi * 180 * t) * np.exp(-t / 0.05)
        noise = bp(rng.standard_normal(n), 600, 5000) * np.exp(-t / 0.11)
        s = lp(tone * 0.6 + noise * 0.7, 4500)
    else:
        n = int(0.28 * SR)
        t = np.arange(n) / SR
        tone = np.sin(2 * np.pi * np.cumsum(205 - 25 * (1 - np.exp(-t / 0.01))) / SR) * np.exp(-t / 0.07)
        noise = bp(rng.standard_normal(n), 1200, 10000) * np.exp(-t / 0.12)
        s = tone * 0.55 + noise * 0.85
    return fade(sat(s, 1.3) * 0.85)


def clap(seed=13):
    rng = np.random.default_rng(seed)
    n = int(0.35 * SR)
    t = np.arange(n) / SR
    noise = bp(rng.standard_normal(n), 900, 4200)
    env = np.zeros(n)
    for k, off in enumerate([0.0, 0.009, 0.018, 0.026]):
        i = int(off * SR)
        env[i:] += np.exp(-(t[i:] - off) / (0.005 if k < 3 else 0.11))
    c = noise * env
    st = reverb(to_stereo(c), 0.8, 0.22)[:n]
    return fade(st * 0.8)


def hat(open_=False, seed=17):
    n = int((0.32 if open_ else 0.06) * SR)
    t = np.arange(n) / SR
    metal = np.zeros(n)
    for f in (205.3, 304.4, 369.6, 522.7, 540.0, 800.0):
        metal += square(f * 1.0, n)
    rng = np.random.default_rng(seed)
    noise = rng.standard_normal(n) * 0.6
    h = bp(metal * 0.3 + noise, 7000, 16000, 2)
    h *= np.exp(-t / (0.11 if open_ else 0.018))
    return fade(h * 0.55, 0.0005, 0.004)


def shaker(seed=19):
    n = int(0.09 * SR)
    t = np.arange(n) / SR
    rng = np.random.default_rng(seed)
    env = np.minimum(t / 0.012, 1.0) * np.exp(-t / 0.03)
    return fade(hp(rng.standard_normal(n), 5000) * env * 0.35)


def cowbell(freq=540.0, dur=0.32):
    n = int(dur * SR)
    t = np.arange(n) / SR
    s = square(freq, n) + square(freq * 1.4815, n)
    s = bp(s, freq * 0.9, freq * 4.0)
    env = np.exp(-t / 0.09) * 0.7 + np.exp(-t / 0.012) * 0.6
    return fade(sat(s * env * 0.7, 1.4))


def tom(freq=110.0, dur=0.5):
    n = int(dur * SR)
    t = np.arange(n) / SR
    f = freq * (1 + 0.6 * np.exp(-t / 0.04))
    s = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.22)
    return fade(sat(s, 1.2) * 0.8)


def rim():
    n = int(0.05 * SR)
    t = np.arange(n) / SR
    s = bp(np.sin(2 * np.pi * 1700 * t) + np.random.default_rng(23).standard_normal(n) * 0.4, 800, 6000)
    return fade(s * np.exp(-t / 0.01) * 0.6)


def bass808(freq, dur, glide_from=None, drive=2.2):
    n = int(dur * SR)
    t = np.arange(n) / SR
    if glide_from:
        f = freq + (glide_from - freq) * np.exp(-t / 0.06)
    else:
        f = np.full(n, freq)
    s = sine(f, n) + 0.25 * sine(f * 2, n)
    env = np.minimum(t / 0.004, 1) * np.exp(-t / max(0.4, dur * 0.8))
    return fade(sat(s * env, drive) * 0.9, 0.002, 0.03)


def bass_saw(freq, dur, cutoff=900.0):
    n = int(dur * SR)
    s = saw(freq, n) * 0.6 + square(freq / 2, n) * 0.4
    s = lp(s, cutoff, 2)
    env = adsr(n, 0.004, 0.08, 0.75, min(0.06, dur * 0.3))
    return fade(sat(s * env, 1.4) * 0.8)


def chip(freq, dur, duty=0.25, decay=None):
    n = int(dur * SR)
    s = square(freq, n, duty)
    env = adsr(n, 0.002, 0.05, 0.8, 0.02) if decay is None else expenv(n, decay)
    return fade(s * env * 0.5)


def chip_noise(dur=0.08, rate=9000, seed=29):
    n = int(dur * SR)
    rng = np.random.default_rng(seed)
    hold = max(1, int(SR / rate))
    vals = rng.choice([-1.0, 1.0], size=n // hold + 2)
    s = np.repeat(vals, hold)[:n]
    return fade(s * expenv(n, dur / 3) * 0.4)


def pluck(freq, dur, bright=1.0, decay=0.35):
    """Additive pluck: upper harmonics die faster."""
    n = int(dur * SR)
    t = np.arange(n) / SR
    s = np.zeros(n)
    for k in range(1, 14):
        if freq * k > 15000:
            break
        s += (1.0 / k) * np.sin(2 * np.pi * freq * k * t + k) * np.exp(-t * (1 / decay + k * 3.5 / bright))
    return fade(s * 0.5, 0.001, 0.02)


def epiano(freq, dur):
    n = int(dur * SR)
    t = np.arange(n) / SR
    index = 1.6 * np.exp(-t / 0.35)
    s = np.sin(2 * np.pi * freq * t + index * np.sin(2 * np.pi * freq * t))
    s += 0.25 * np.sin(2 * np.pi * freq * 2 * t) * np.exp(-t / 0.2)
    trem = 1 + 0.08 * np.sin(2 * np.pi * 4.5 * t)
    env = np.minimum(t / 0.004, 1) * np.exp(-t / 1.2)
    return fade(s * env * trem * 0.4, 0.001, 0.05)


def bell(freq, dur):
    n = int(dur * SR)
    t = np.arange(n) / SR
    index = 3.0 * np.exp(-t / 0.5)
    s = np.sin(2 * np.pi * freq * t + index * np.sin(2 * np.pi * freq * 3.5 * t))
    return fade(s * np.exp(-t / 0.7) * 0.35, 0.001, 0.05)


def supersaw(freqs, dur, cutoff=2400.0, attack=0.02, release=0.15, voices=3, detune=0.12):
    n = int(dur * SR)
    out = np.zeros((n, 2))
    for f in freqs:
        for v in range(voices):
            cents = (v - (voices - 1) / 2) * detune * 100 / max(1, voices - 1) * 2
            fv = f * 2 ** (cents / 1200)
            s = saw(fv, n, start=(v * 0.37) % 1)
            p = (v - (voices - 1) / 2) / max(1, voices - 1)
            out += to_stereo(s, pan=p * 0.7)
    out = lp(out, cutoff, 2)
    env = adsr(n, attack, 0.2, 0.85, min(release, dur * 0.4))
    return out * env[:, None] * (0.22 / max(1, len(freqs)) ** 0.5)


def lead(freq, dur, kind="saw", vib=0.0):
    n = int(dur * SR)
    t = np.arange(n) / SR
    f = freq * (1 + vib * np.sin(2 * np.pi * 5.5 * t) * np.minimum(t / 0.25, 1))
    if kind == "square":
        s = square(f, n, 0.5)
    elif kind == "pulse":
        s = square(f, n, 0.25)
    else:
        s = saw(f, n) * 0.7 + saw(f * 1.004, n, 0.3) * 0.5
    s = lp(s, 4200)
    env = adsr(n, 0.008, 0.12, 0.7, min(0.08, dur * 0.3))
    return fade(s * env * 0.32)


def brass(freqs, dur):
    n = int(dur * SR)
    t = np.arange(n) / SR
    out = np.zeros(n)
    for f in freqs:
        out += saw(f, n) + saw(f * 1.003, n, 0.5) * 0.6
    bright = lp(out, 3500)
    dark = lp(out, 700)
    e = np.exp(-t / 0.12)
    s = bright * e + dark * (1 - e)
    env = adsr(n, 0.015, 0.1, 0.8, min(0.1, dur * 0.3))
    return fade(s * env * 0.18 / max(1, len(freqs)) ** 0.5)


def strings(freqs, dur, attack=0.4):
    n = int(dur * SR)
    out = np.zeros((n, 2))
    t = np.arange(n) / SR
    for f in freqs:
        for v, c in enumerate((-9, 0, 8)):
            fv = f * 2 ** (c / 1200) * (1 + 0.003 * np.sin(2 * np.pi * (5 + v * 0.3) * t))
            out += to_stereo(saw(fv, n, v * 0.21), pan=(v - 1) * 0.6)
    out = lp(out, 2600)
    out = hp(out, 120)
    env = adsr(n, attack, 0.3, 0.9, min(0.4, dur * 0.4))
    return out * env[:, None] * (0.16 / max(1, len(freqs)) ** 0.5)


def drone(freq, dur):
    n = int(dur * SR)
    t = np.arange(n) / SR
    s = saw(freq, n) + saw(freq * 1.006, n, 0.4) + 0.5 * saw(freq * 0.5, n, 0.7)
    s = lp(s, 300 + 200 * (1 + np.sin(2 * np.pi * 0.07 * t)).mean())
    return fade(s * 0.22, 0.3, 0.3)


# ---------------------------------------------------------------- one-shot fx
def fx_impact(seed=31):
    rng = np.random.default_rng(seed)
    n = int(2.2 * SR)
    t = np.arange(n) / SR
    sub = np.sin(2 * np.pi * np.cumsum(38 + 70 * np.exp(-t / 0.08)) / SR) * np.exp(-t / 0.7)
    crack = bp(rng.standard_normal(n), 300, 7000) * np.exp(-t / 0.05)
    s = sat(sub * 1.3 + crack * 0.6, 1.8)
    return reverb(to_stereo(s), 2.2, 0.3)[:n] * 0.9


def fx_boom(seed=37):
    rng = np.random.default_rng(seed)
    n = int(3.0 * SR)
    t = np.arange(n) / SR
    sub = np.sin(2 * np.pi * np.cumsum(30 + 50 * np.exp(-t / 0.15)) / SR) * np.exp(-t / 1.1)
    rumble = lp(rng.standard_normal(n), 180) * np.exp(-t / 0.9) * 2.0
    s = sat(sub + rumble * 0.5, 1.6)
    return reverb(to_stereo(s), 2.8, 0.35)[:n]


def fx_braam(root=45.0):
    n = int(2.6 * SR)
    t = np.arange(n) / SR
    s = np.zeros(n)
    for m, g in ((1, 1.0), (1.5, 0.6), (2, 0.5), (1.003, 0.8)):
        s += saw(root * m, n) * g
    s = lp(s, 900) * np.minimum(t / 0.05, 1) * np.exp(-t / 1.3)
    return reverb(to_stereo(sat(s * 0.6, 2.0)), 2.4, 0.3)[:n] * 0.7


def fx_whoosh(dur=0.55, up=True, seed=41):
    rng = np.random.default_rng(seed)
    n = int(dur * SR)
    t = np.arange(n) / SR
    noise = rng.standard_normal(n)
    out = np.zeros(n)
    steps = 24
    for k in range(steps):
        a, b = int(k * n / steps), int((k + 1) * n / steps)
        frac = k / (steps - 1)
        fc = 300 * (20 ** (frac if up else 1 - frac))
        seg = bp(noise, fc * 0.6, fc * 1.8)[a:b]
        out[a:b] = seg
    env = np.sin(np.pi * np.clip(t / dur, 0, 1)) ** 1.5
    st = to_stereo(out * env * 0.8)
    # pan sweep
    pan = np.linspace(-0.7, 0.7, n)
    st[:, 0] *= np.cos((pan + 1) * np.pi / 4) * 1.41
    st[:, 1] *= np.sin((pan + 1) * np.pi / 4) * 1.41
    return st


def fx_riser(dur=1.5, seed=43):
    rng = np.random.default_rng(seed)
    n = int(dur * SR)
    t = np.arange(n) / SR
    frac = t / dur
    noise = rng.standard_normal(n)
    out = np.zeros(n)
    steps = 32
    for k in range(steps):
        a, b = int(k * n / steps), int((k + 1) * n / steps)
        fc = 400 * (25 ** (k / (steps - 1)))
        out[a:b] = bp(noise, fc * 0.7, fc * 1.6)[a:b]
    tone = saw(110 * (2 ** (frac * 2.5)), n) * 0.25
    tone = lp(tone, 5000)
    s = (out * 0.7 + tone) * (frac ** 2)
    return fade(to_stereo(s, width=0.6) * 0.8, 0.01, 0.01)


def fx_downlifter(dur=1.2, seed=47):
    r = fx_riser(dur, seed)[::-1].copy()
    return r


def fx_pop():
    n = int(0.12 * SR)
    t = np.arange(n) / SR
    f = 400 + 900 * np.exp(-t / 0.012)
    s = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.03)
    return fade(s * 0.7)


def fx_click():
    n = int(0.03 * SR)
    t = np.arange(n) / SR
    s = bp(np.random.default_rng(53).standard_normal(n), 2000, 9000) * np.exp(-t / 0.004)
    s += np.sin(2 * np.pi * 3200 * t) * np.exp(-t / 0.003) * 0.4
    return fade(s * 0.6)


def fx_tick():
    n = int(0.04 * SR)
    t = np.arange(n) / SR
    s = np.sin(2 * np.pi * 5200 * t) * np.exp(-t / 0.004) + np.sin(2 * np.pi * 2100 * t) * np.exp(-t / 0.008) * 0.5
    return fade(s * 0.5)


def fx_notif():
    """Generic phone notification: two soft bell tones."""
    a = bell(mtof(88), 0.5) * 0.8
    b = bell(mtof(93), 0.7)
    out = np.zeros(int(0.9 * SR))
    out[: len(a)] += a
    i = int(0.12 * SR)
    out[i: i + len(b)] += b[: len(out) - i]
    return reverb(to_stereo(out), 0.8, 0.15)[: len(out)]


def fx_type(seed=59, dur=0.9, rate=14):
    rng = np.random.default_rng(seed)
    n = int(dur * SR)
    out = np.zeros(n)
    t0 = 0.0
    while t0 < dur - 0.03:
        c = fx_click() * rng.uniform(0.5, 1.0)
        i = int(t0 * SR)
        out[i: i + len(c)] += c[: n - i]
        t0 += rng.uniform(0.6, 1.4) / rate
    return out


def fx_coin():
    a = chip(mtof(83), 0.08, 0.5, 0.05)
    b = chip(mtof(88), 0.35, 0.5, 0.12)
    out = np.zeros(int(0.45 * SR))
    out[: len(a)] += a
    i = int(0.075 * SR)
    out[i: i + len(b)] += b[: len(out) - i]
    return out * 0.8


def fx_levelup():
    notes = [72, 76, 79, 84, 88]
    out = np.zeros(int(0.9 * SR))
    for k, m in enumerate(notes):
        c = chip(mtof(m), 0.16 if k < 4 else 0.45, 0.25, 0.08 if k < 4 else 0.2)
        i = int(k * 0.07 * SR)
        out[i: i + len(c)] += c[: len(out) - i]
    return out * 0.8


def fx_sparkle(seed=61):
    rng = np.random.default_rng(seed)
    n = int(1.2 * SR)
    out = np.zeros(n)
    for k in range(9):
        f = mtof(rng.choice([88, 91, 93, 95, 96, 98, 100, 103]))
        b = bell(f, 0.5) * rng.uniform(0.25, 0.6)
        i = int((k * 0.06 + rng.uniform(0, 0.03)) * SR)
        out[i: i + len(b)] += b[: n - i]
    return reverb(to_stereo(out, width=0.5), 1.2, 0.3)[:n]


def fx_wrong():
    n = int(0.55 * SR)
    s = square(110, n, 0.5) + square(116.5, n, 0.5)
    s = lp(s, 1500) * adsr(n, 0.005, 0.05, 0.9, 0.08)
    return fade(s * 0.35)


def fx_right():
    out = np.zeros(int(0.8 * SR))
    for k, m in enumerate((84, 88, 91)):
        b = bell(mtof(m), 0.6)
        i = int(k * 0.06 * SR)
        out[i: i + len(b)] += b[: len(out) - i]
    return out


def fx_heartbeat():
    n = int(0.8 * SR)
    out = np.zeros(n)
    for off, g in ((0.0, 1.0), (0.22, 0.75)):
        k = kick("soft") * g
        i = int(off * SR)
        out[i: i + len(k)] += k[: n - i]
    return lp(out, 400) * 1.4


def fx_clock():
    n = int(0.06 * SR)
    t = np.arange(n) / SR
    s = bp(np.random.default_rng(67).standard_normal(n), 2500, 7000) * np.exp(-t / 0.006)
    s += np.sin(2 * np.pi * 1400 * t) * np.exp(-t / 0.01) * 0.6
    return fade(s * 0.55)


def fx_shutter():
    n = int(0.25 * SR)
    t = np.arange(n) / SR
    rng = np.random.default_rng(71)
    s = bp(rng.standard_normal(n), 800, 8000) * (np.exp(-t / 0.01) + 0.6 * np.exp(-np.maximum(t - 0.09, 0) / 0.012) * (t > 0.09))
    return fade(s * 0.7)


def fx_glitch(seed=73, dur=0.35):
    rng = np.random.default_rng(seed)
    n = int(dur * SR)
    out = np.zeros(n)
    pos = 0
    while pos < n:
        seg = int(rng.uniform(0.008, 0.04) * SR)
        f = rng.choice([80, 160, 320, 640, 1280, 2560])
        piece = square(f, seg, rng.uniform(0.1, 0.5)) if rng.random() < 0.6 else rng.standard_normal(seg) * 0.6
        out[pos: pos + seg] = piece[: max(0, min(seg, n - pos))]
        pos += seg
    out = np.round(out * 6) / 6
    return fade(to_stereo(out * 0.4, width=0.4))


def fx_scratch(seed=79):
    rng = np.random.default_rng(seed)
    n = int(0.45 * SR)
    t = np.arange(n) / SR
    noise = rng.standard_normal(n)
    f = 600 + 1800 * np.abs(np.sin(2 * np.pi * 3.2 * t))
    out = np.zeros(n)
    steps = 30
    for k in range(steps):
        a, b = int(k * n / steps), int((k + 1) * n / steps)
        fc = f[(a + b) // 2]
        out[a:b] = bp(noise, fc * 0.7, fc * 1.4)[a:b]
    return fade(out * np.sin(np.pi * t / 0.45) * 0.7)


def fx_drumroll(dur=1.5, seed=83):
    n = int(dur * SR)
    out = np.zeros(n)
    t0, k = 0.0, 0
    while t0 < dur - 0.02:
        s = snare("tight", seed + k) * (0.35 + 0.65 * t0 / dur)
        i = int(t0 * SR)
        out[i: i + len(s)] += s[: n - i]
        rate = 8 + 24 * (t0 / dur) ** 1.5
        t0 += 1 / rate
        k += 1
    return out * 0.8


def fx_swoosh_hit():
    w = fx_whoosh(0.35, True)
    h = to_stereo(snare("tight", 89)) * 0.6
    out = np.zeros((len(w) + len(h), 2))
    out[: len(w)] += w
    out[int(0.3 * SR): int(0.3 * SR) + len(h)] += h
    return out


def fx_cash():
    """Bright register 'ding' (no real money connotation needed: loot)."""
    out = np.zeros(int(1.0 * SR))
    b = bell(mtof(96), 0.9)
    out[: len(b)] += b
    c = fx_click() * 0.8
    out[: len(c)] += c
    return out


def fx_vinyl(dur=2.0, seed=97):
    rng = np.random.default_rng(seed)
    n = int(dur * SR)
    hiss = lp(rng.standard_normal(n), 3000) * 0.02
    pops = np.zeros(n)
    idx = rng.integers(0, n, size=int(dur * 9))
    pops[idx] = rng.uniform(0.2, 0.6, size=len(idx)) * rng.choice([-1, 1], size=len(idx))
    pops = hp(pops, 1500)
    return hiss + pops * 0.3


def kizu_motif(scale=1.0):
    """The KizuBot three-note motif (E5 B5 E6) with a robotic bleep timbre."""
    notes = [76, 83, 88]
    out = np.zeros(int(0.75 * SR))
    for k, m in enumerate(notes):
        dur = 0.13 if k < 2 else 0.45
        n = int(dur * SR)
        t = np.arange(n) / SR
        f = mtof(m)
        s = square(f, n, 0.5) * 0.35 + np.sin(2 * np.pi * f * t) * 0.6 + np.sin(2 * np.pi * 2 * f * t) * 0.15
        s = lp(s, 6000)
        s = np.round(s * 24) / 24  # slight bit-crush: the robot
        s *= np.minimum(t / 0.003, 1) * np.exp(-t / (0.09 if k < 2 else 0.25))
        i = int(k * 0.095 * SR)
        out[i: i + n] += s[: len(out) - i]
    return out * scale


def fx_logo():
    """KizuBot sonic logo: sub thump + motif + shimmer chord. Same in every short."""
    n = int(1.8 * SR)
    out = np.zeros((n, 2))
    sub = kick("soft") * 0.9
    out[: len(sub)] += to_stereo(sub)
    m = kizu_motif()
    out[: len(m)] += to_stereo(m, width=0.3)
    t = np.arange(int(1.4 * SR)) / SR
    shimmer = np.zeros(len(t))
    for f in (mtof(88), mtof(92), mtof(95), mtof(100)):
        shimmer += np.sin(2 * np.pi * f * t * (1 + 0.002 * np.sin(2 * np.pi * 6 * t)))
    shimmer *= np.minimum(t / 0.02, 1) * np.exp(-t / 0.45) * 0.12
    i = int(0.19 * SR)
    out[i: i + len(shimmer)] += to_stereo(shimmer, width=0.6)
    sp = fx_sparkle(101)[: n - i] * 0.5
    out[i: i + len(sp)] += sp
    return reverb(out, 1.4, 0.22)[:n]


def fx_alert():
    """KizuBot in-app alert (shiny / mega / boss): the motif twice. Pavlov on purpose."""
    a = kizu_motif(0.9)
    n = int(1.1 * SR)
    out = np.zeros(n)
    out[: len(a)] += a
    i = int(0.42 * SR)
    out[i: i + len(a)] += a[: n - i] * 0.85
    return reverb(to_stereo(out, width=0.3), 0.9, 0.18)[:n]


def fx_tapestop():
    return None  # handled as a music event


SYNTH_FX = {
    "impact": fx_impact, "boom": fx_boom, "braam": fx_braam,
    "whoosh": lambda: fx_whoosh(0.55, True), "whoosh_down": lambda: fx_whoosh(0.55, False),
    "whoosh_fast": lambda: fx_whoosh(0.28, True, 42), "riser": lambda: fx_riser(1.5),
    "riser_long": lambda: fx_riser(3.0, 44), "riser_short": lambda: fx_riser(0.8, 45),
    "downlifter": fx_downlifter, "pop2": fx_pop, "click": fx_click, "tick2": fx_tick,
    "notif": fx_notif, "type": fx_type, "type_long": lambda: fx_type(60, 2.2),
    "coin": fx_coin, "levelup": fx_levelup, "sparkle": fx_sparkle, "wrong": fx_wrong,
    "right": fx_right, "heartbeat": fx_heartbeat, "clock": fx_clock, "shutter": fx_shutter,
    "glitch": fx_glitch, "glitch_long": lambda: fx_glitch(74, 0.8), "scratch": fx_scratch,
    "drumroll": fx_drumroll, "drumroll_long": lambda: fx_drumroll(2.6, 84),
    "swoosh_hit": fx_swoosh_hit, "ding": fx_cash, "vinyl": fx_vinyl,
    "logo": fx_logo, "alert": fx_alert, "motif": lambda: kizu_motif(0.9),
    "snare": lambda: snare("tight"), "clap": clap, "kick": lambda: kick("hard"),
    "cowbell": cowbell, "rim": rim,
}

# file-based sfx (kit/sfx/*.wav): pop tick counter chime snap star switch fill success
# and Pixabay: px-whoosh, px-impact-bass-1, px-riser, px-sparkle, px-notification, ...


def load_sfx(name):
    if name in SYNTH_FX:
        x = SYNTH_FX[name]()
        return to_stereo(x) if x.ndim == 1 else x
    path = os.path.join(KIT_SFX, name + ".wav")
    if not os.path.exists(path):
        raise SystemExit(f"unknown sfx '{name}' (not synthesized, no {path})")
    x, sr = sf.read(path, always_2d=True)
    if sr != SR:
        x = signal.resample_poly(x, SR, sr, axis=0)
    if x.shape[1] == 1:
        x = np.repeat(x, 2, axis=1)
    peak = np.max(np.abs(x)) or 1.0
    return x / peak * 0.8


# ------------------------------------------------------------------- styles
# patterns are 16 steps per bar; strings use x (hit), o (accent), . (rest)
STYLES = {
    "phonk": dict(bpm=130, kick="808", kick_pat="x.....x...x.....", snare="clap", snare_pat="....x.......x...",
                  hat_pat="x.x.x.x.x.x.x.x.", open_pat="..............x.", perc="cowbell", bass="808",
                  chords="dark", lead="cowbell", sidechain=0.35, prog=[[0], [0], [5], [3]], swing=0.0,
                  root="F#"),
    "funk": dict(bpm=130, kick="808", kick_pat="x..x..x...x.x...", snare="clap", snare_pat="....x.......x...",
                 hat_pat="..x...x...x...x.", open_pat="", perc="tamborzao", bass="808", chords="stab",
                 lead="pluck", sidechain=0.25, prog=[[0], [0], [3], [4]], swing=0.0, root="A"),
    "trap": dict(bpm=145, kick="808", kick_pat="x.........x.x...", snare="trap", snare_pat="........x.......",
                 hat_pat="x.x.x.x.x.x.xxx.", open_pat="", perc="none", bass="808", chords="pad", lead="bell",
                 sidechain=0.0, prog=[[0], [5], [3], [6]], swing=0.0, halftime=True, root="C"),
    "house": dict(bpm=124, kick="punch", kick_pat="x...x...x...x...", snare="clap", snare_pat="....x.......x...",
                  hat_pat="..x...x...x...x.", open_pat="", perc="shaker", bass="saw", chords="supersaw",
                  lead="pluck", sidechain=0.55, prog=[[0], [5], [2], [6]], swing=0.0, root="A"),
    "synthwave": dict(bpm=104, kick="punch", kick_pat="x.......x.......", snare="gated", snare_pat="....x.......x...",
                      hat_pat="x.x.x.x.x.x.x.x.", open_pat="", perc="none", bass="arp8", chords="supersaw",
                      lead="saw", sidechain=0.3, prog=[[0], [5], [2], [6]], swing=0.0, root="E"),
    "chiptune": dict(bpm=150, kick="chip", kick_pat="x.......x.......", snare="chip", snare_pat="....x.......x...",
                     hat_pat="x.x.x.x.x.x.x.x.", open_pat="", perc="none", bass="chip", chords="arp",
                     lead="chip", sidechain=0.0, prog=[[0], [5], [3], [4]], swing=0.0, major=True, root="C"),
    "lofi": dict(bpm=84, kick="soft", kick_pat="x......x..x.....", snare="lofi", snare_pat="....x.......x...",
                 hat_pat="x.x.x.x.x.x.x.x.", open_pat="", perc="vinyl", bass="sine", chords="epiano",
                 lead="epiano", sidechain=0.0, prog=[[0], [5], [3], [4]], swing=0.18, root="D"),
    "tension": dict(bpm=96, kick="soft", kick_pat="x.......x.......", snare="none", snare_pat="",
                    hat_pat="", open_pat="", perc="clock", bass="drone", chords="strings", lead="none",
                    sidechain=0.0, prog=[[0], [0], [1], [0]], swing=0.0, root="D"),
    "gameshow": dict(bpm=122, kick="punch", kick_pat="x.....x.x.......", snare="tight", snare_pat="....x.......x...",
                     hat_pat="x.xxx.xxx.xxx.xx", open_pat="", perc="rim", bass="saw", chords="brass",
                     lead="square", sidechain=0.0, prog=[[0], [5], [1], [4]], swing=0.12, major=True, root="F"),
    "epic": dict(bpm=90, kick="hard", kick_pat="x.....x...x.....", snare="gated", snare_pat="....x.......x...",
                 hat_pat="", open_pat="", perc="toms", bass="saw", chords="strings", lead="brass",
                 sidechain=0.0, prog=[[0], [5], [3], [6]], swing=0.0, root="D"),
}

SECTION_MIX = {
    #            kick snare hat  perc bass chords lead
    "intro":   (0.0, 0.0, 0.3, 0.0, 0.0, 0.9, 0.0),
    "groove":  (1.0, 1.0, 0.8, 0.7, 1.0, 0.6, 0.0),
    "build":   (0.0, 0.0, 0.6, 0.3, 0.0, 0.8, 0.0),
    "drop":    (1.0, 1.0, 1.0, 1.0, 1.0, 0.75, 1.0),
    "break":   (0.0, 0.0, 0.0, 0.0, 0.5, 1.0, 0.7),
    "outro":   (0.8, 0.6, 0.5, 0.4, 0.8, 0.8, 0.0),
    "silence": (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0),
}
TRACKS = ("kick", "snare", "hat", "perc", "bass", "chords", "lead")


def scale_degrees(major):
    return MAJOR if major else MINOR


def chord_notes(root_midi, degree, major, size=3):
    sc = scale_degrees(major)
    notes = []
    for k in range(size):
        d = degree + 2 * k
        octv, idx = divmod(d, 7)
        notes.append(root_midi + sc[idx] + 12 * octv)
    return notes


def make_melody(rng, steps_per_bar, bars, major, density=0.45):
    sc = PENTA_MINOR if not major else [0, 2, 4, 7, 9]
    motif = []
    for s in range(steps_per_bar * 2):
        if s % 2 == 0 and rng.random() < density * (1.4 if s % 4 == 0 else 0.8):
            motif.append(int(rng.choice(range(len(sc) + 2))))
        else:
            motif.append(None)
    if all(m is None for m in motif):
        motif[0] = 0
    # repeat motif, vary the last quarter of every second repetition
    mel = []
    for b in range(0, bars, 2):
        var = list(motif)
        if (b // 2) % 2 == 1:
            for s in range(len(var) * 3 // 4, len(var)):
                if var[s] is not None:
                    var[s] = int(rng.choice(range(len(sc) + 2)))
        mel.extend(var)
    return mel, sc


def section_at(sections, t):
    cur = sections[0]
    for s in sections:
        if s["at"] <= t + 1e-6:
            cur = s
        else:
            break
    return cur


def render_music(spec):
    style_name = spec.get("style", "phonk")
    if style_name not in STYLES:
        raise SystemExit(f"unknown style {style_name}; choose from {', '.join(STYLES)}")
    st = dict(STYLES[style_name])
    bpm = float(spec.get("bpm", st["bpm"]))
    dur = float(spec["duration"])
    seed = int(spec.get("seed", 1))
    rng = np.random.default_rng(seed)
    major = bool(st.get("major", False))
    root_name = spec.get("root", st.get("root", "A"))
    root = 36 + NOTE[root_name]  # E2..D#3 so the bass sits low and chords mid
    if root < 40:
        root += 12
    step = 60.0 / bpm / 4.0
    halftime = st.get("halftime", False)
    total_steps = int(math.ceil((dur + 1.0) / step))
    n_total = int((dur + 2.5) * SR)

    sections = sorted(spec.get("sections") or [
        {"at": 0.0, "type": "groove"},
        {"at": max(0.0, dur * 0.42 - 4 * 60 / bpm), "type": "build"},
        {"at": dur * 0.42, "type": "drop"},
        {"at": max(0.0, dur - 3.2), "type": "outro"},
    ], key=lambda s: s["at"])
    if sections[0]["at"] > 0:
        sections.insert(0, {"at": 0.0, "type": "groove"})

    tracks = {k: np.zeros((n_total, 2)) for k in TRACKS}
    kick_times = []

    # progression: choose a rotation for variety
    prog = st["prog"]
    rot = int(rng.integers(0, len(prog)))
    prog = prog[rot:] + prog[:rot] if style_name not in ("tension",) else prog
    bars = int(math.ceil(total_steps / 16)) + 1
    mel, mel_scale = make_melody(rng, 16, bars + 2, major, density=0.5 if style_name != "lofi" else 0.35)

    swing = st.get("swing", 0.0)

    def step_time(s):
        t = s * step
        if swing and s % 2 == 1:
            t += step * swing
        return t

    kick_kind = st["kick"]
    k808 = kick("808", mtof(root - 12)) if kick_kind == "808" else None
    sn_kind = st["snare"]

    # pre-render reusable hits
    hits = {
        "kick": k808 if k808 is not None else (kick(kick_kind) if kick_kind != "chip" else None),
        "hat": hat(False), "open": hat(True),
    }
    if sn_kind == "clap":
        hits["snare"] = clap()
    elif sn_kind == "chip":
        hits["snare"] = chip_noise(0.12, 7000)
    elif sn_kind != "none":
        hits["snare"] = snare(sn_kind)
    else:
        hits["snare"] = None

    def pat(p, s):
        return bool(p) and p[s % len(p)] in "xo"

    for s in range(total_steps):
        t = step_time(s)
        if t >= dur + 0.5:
            break
        bar = s // 16
        pos = s % 16
        sec = section_at(sections, t)
        typ = sec["type"]
        chord_deg = prog[bar % len(prog)][0]
        chord = chord_notes(root + 12, chord_deg, major)

        # ---- drums
        kp = st["kick_pat"]
        if pat(kp, pos):
            if kick_kind == "chip":
                k = chip(mtof(36), 0.12, 0.5, 0.04)
                add(tracks["kick"], k, t)
            else:
                if kick_kind == "808":
                    k = kick("808", mtof(root + chord_deg_to_semitone(chord_deg, major) - 12))
                else:
                    k = hits["kick"]
                add(tracks["kick"], k, t)
            if SECTION_MIX.get(typ, SECTION_MIX["groove"])[0] > 0:
                kick_times.append(t)
        if hits["snare"] is not None and pat(st["snare_pat"], pos):
            add(tracks["snare"], hits["snare"], t, 0.9)
        hp_ = st["hat_pat"]
        if pat(hp_, pos):
            vel = 0.55 + 0.45 * (pos % 4 == 0) + rng.uniform(-0.1, 0.1)
            if style_name == "trap" and pos >= 12 and rng.random() < 0.5:
                # triplet roll
                for r in range(3):
                    add(tracks["hat"], hits["hat"], t + r * step * 2 / 3, vel * 0.7)
            elif style_name == "chiptune":
                add(tracks["hat"], chip_noise(0.03, 12000, 30 + pos), t, vel * 0.6)
            else:
                add(tracks["hat"], to_stereo(hits["hat"], pan=0.35 if pos % 4 == 2 else -0.2), t, vel)
        if pat(st.get("open_pat", ""), pos):
            add(tracks["hat"], hits["open"], t, 0.6)

        # ---- percussion
        perc = st["perc"]
        if perc == "cowbell" and pos in (0, 3, 6, 10, 12, 14):
            deg = mel[(bar % 2) * 16 + pos] if mel[(bar % 2) * 16 + pos] is not None else 0
            m = root + 24 + mel_scale[deg % len(mel_scale)] + 12 * (deg // len(mel_scale))
            add(tracks["perc"], cowbell(mtof(m) * 0.5 if m > 80 else mtof(m)), t, 0.55)
        elif perc == "tamborzao" and pos in (0, 3, 6, 8, 10, 13):
            add(tracks["perc"], tom(140 if pos in (0, 8) else 190, 0.25), t, 0.55)
            if pos in (3, 10):
                add(tracks["perc"], rim(), t + step, 0.5)
        elif perc == "shaker" and pos % 2 == 1:
            add(tracks["perc"], shaker(19 + pos), t, 0.7)
        elif perc == "rim" and pos in (3, 7, 11, 15):
            add(tracks["perc"], rim(), t, 0.6)
        elif perc == "clock" and pos % 4 == 0:
            add(tracks["perc"], fx_clock(), t, 0.7)
        elif perc == "toms" and pos in (0, 6, 10, 14):
            add(tracks["perc"], tom(70 if pos == 0 else 95, 0.8), t, 0.9)

        # ---- bass
        bass = st["bass"]
        bass_note = root + chord_deg_to_semitone(chord_deg, major)
        if bass == "808":
            pass  # the 808 kick is the bass
        elif bass == "saw" and (pos % 4 in (0, 3) if style_name != "epic" else pos % 8 == 0):
            add(tracks["bass"], bass_saw(mtof(bass_note), step * (3 if pos % 4 == 0 else 1) * 0.95), t, 0.8)
        elif bass == "arp8" and pos % 2 == 0:
            m = bass_note + (12 if (pos // 2) % 2 else 0)
            add(tracks["bass"], bass_saw(mtof(m), step * 1.9, 1400), t, 0.7)
        elif bass == "chip" and pos % 2 == 0:
            m = bass_note + (12 if (pos // 2) % 4 == 2 else 0)
            add(tracks["bass"], tri(mtof(m), int(step * 1.9 * SR)) * adsr(int(step * 1.9 * SR), 0.002, 0.03, 0.9, 0.01) * 0.5, t)
        elif bass == "sine" and pos in (0, 7, 10):
            n = int(step * 3 * SR)
            add(tracks["bass"], sine(mtof(bass_note), n) * adsr(n, 0.01, 0.1, 0.8, 0.05) * 0.6, t)
        elif bass == "drone" and pos == 0 and bar % 2 == 0:
            add(tracks["bass"], drone(mtof(bass_note - 12), step * 32), t, 0.8)
            add(tracks["bass"], fx_heartbeat(), t, 0.6)

        # ---- chords (one event per bar)
        if pos == 0:
            cname = st["chords"]
            bar_len = step * 16
            freqs = [mtof(m) for m in chord]
            if cname == "supersaw":
                add(tracks["chords"], supersaw(freqs, bar_len, 2600), t)
            elif cname == "pad" or cname == "dark":
                add(tracks["chords"], supersaw([f / 2 for f in freqs], bar_len, 1100 if cname == "dark" else 1600, 0.25, 0.4), t, 0.9)
            elif cname == "strings":
                add(tracks["chords"], strings([f / 2 for f in freqs], bar_len, 0.35), t)
            elif cname == "epiano":
                for k, f in enumerate(freqs):
                    add(tracks["chords"], to_stereo(epiano(f, bar_len), pan=(k - 1) * 0.3), t + k * 0.012)
            elif cname == "brass":
                for off in (0, 6, 10):
                    add(tracks["chords"], to_stereo(brass(freqs, step * 1.6)), t + off * step, 0.9)
            elif cname == "stab":
                for off in (0, 3, 6, 10, 12):
                    add(tracks["chords"], to_stereo(brass(freqs, step * 0.9)), t + off * step, 0.6)
            elif cname == "arp":
                for k in range(16):
                    m = chord[k % 3] + (12 if (k // 3) % 2 else 0)
                    add(tracks["chords"], chip(mtof(m), step * 0.9, 0.125, 0.05), step_time(s + k), 0.45)

        # ---- lead melody (16th grid, notes on even steps)
        ln = st["lead"]
        if ln not in ("none", "cowbell"):
            deg = mel[(bar % 4) * 16 + pos] if (bar % 4) * 16 + pos < len(mel) else None
            if deg is not None:
                m = root + 24 + mel_scale[deg % len(mel_scale)] + 12 * (deg // len(mel_scale))
                f = mtof(m)
                ln_dur = step * 2
                if ln == "pluck":
                    x = pluck(f, 0.5, 1.2, 0.25)
                elif ln == "bell":
                    x = bell(f, 0.6)
                elif ln == "epiano":
                    x = epiano(f, 0.8) * 0.8
                elif ln == "chip":
                    x = chip(f, ln_dur * 0.95, 0.25, None)
                elif ln == "square":
                    x = lead(f, ln_dur, "square")
                elif ln == "brass":
                    x = brass([f / 2], ln_dur * 1.8)
                else:
                    x = lead(f, ln_dur * 1.5, "saw", 0.004)
                add(tracks["lead"], to_stereo(x, pan=0.15), t, 0.75)

    # ---- section automation (per-track gains with short ramps)
    env = {k: np.zeros(n_total) for k in TRACKS}
    bounds = sections + [{"at": dur + 3.0, "type": "silence"}]
    for i in range(len(bounds) - 1):
        a = int(bounds[i]["at"] * SR)
        b = int(bounds[i + 1]["at"] * SR)
        mix = SECTION_MIX.get(bounds[i]["type"], SECTION_MIX["groove"])
        energy = float(bounds[i].get("energy", 1.0))
        for k, g in zip(TRACKS, mix):
            env[k][a:b] = g * (energy if k in ("hat", "perc", "lead") else 1.0)
    ramp = int(0.012 * SR)
    kern = np.ones(ramp) / ramp
    for k in TRACKS:
        env[k] = np.convolve(env[k], kern, mode="same")

    # build sections: snare roll + riser + low-passed chords sweeping open
    music = np.zeros((n_total, 2))
    for i in range(len(bounds) - 1):
        if bounds[i]["type"] == "build":
            a = bounds[i]["at"]
            L = max(0.4, bounds[i + 1]["at"] - a)
            add(music, fx_drumroll(L, 200 + i) * 0.7, a)
            add(music, fx_riser(L, 300 + i) * 0.6, a)

    # chords filter sweep during build: crossfade a dark copy
    dark = lp(tracks["chords"], 500)
    sweep = np.ones(n_total)
    for i in range(len(bounds) - 1):
        if bounds[i]["type"] in ("build", "intro"):
            a = int(bounds[i]["at"] * SR)
            b = int(bounds[i + 1]["at"] * SR)
            sweep[a:b] = np.linspace(0.0, 1.0, max(1, b - a)) if bounds[i]["type"] == "build" else 0.15
    chords_mix = tracks["chords"] * sweep[:, None] + dark * (1 - sweep[:, None])

    # sidechain pump from kicks
    sc_depth = st.get("sidechain", 0.0)
    pump = np.ones(n_total)
    if sc_depth > 0:
        rel = int(60 / bpm * 0.55 * SR)
        shape = 1 - sc_depth * np.exp(-np.arange(rel) / (rel / 4))
        for kt in kick_times:
            i = int(kt * SR)
            j = min(n_total, i + rel)
            pump[i:j] = np.minimum(pump[i:j], shape[: j - i])

    gains = {"kick": 0.62, "snare": 1.1, "hat": 0.75, "perc": 1.0, "bass": 0.55, "chords": 1.6, "lead": 1.5}
    if style_name in ("phonk", "funk", "trap"):
        gains.update(kick=0.7, bass=0.7, perc=1.5, chords=1.3)
    if style_name == "lofi":
        gains.update(hat=0.45, chords=1.6)
    if style_name == "tension":
        gains.update(chords=1.8, perc=1.0)

    tracks["lead"] = tracks["lead"] + delay(tracks["lead"], 60 / bpm * 0.75, 0.3, 0.22)[:n_total] * 0.8
    for k in TRACKS:
        x = chords_mix if k == "chords" else tracks[k]
        g = env[k][:, None] * gains[k]
        if k in ("chords", "bass", "lead", "perc") and sc_depth > 0:
            g = g * pump[:, None]
        music += x * g

    # space
    send = tracks["chords"] * env["chords"][:, None] * 0.6 + tracks["lead"] * env["lead"][:, None] * 0.5 + tracks["snare"] * env["snare"][:, None] * 0.25 + tracks["perc"] * env["perc"][:, None] * 0.2
    wet = reverb(send, 1.8, 1.0, dry=False)[:n_total]
    music += wet * (0.18 if style_name not in ("tension", "lofi", "epic") else 0.3)

    if style_name == "lofi":
        music = lp(music, 5200)
        music += to_stereo(fx_vinyl(dur + 2.5)[:n_total], width=0.3)[:n_total]
    if style_name in ("phonk", "funk"):
        music = sat(music * 1.15, 1.25)
    # phone-speaker translation: clear the rumble, lift presence
    music = hp(music, 30, 2)
    music = music - 0.25 * lp(music, 90, 2) + 0.22 * bp(music, 1800, 6500, 2)

    # stops: hard cut-outs (optionally tape-stop the second before)
    for stp in spec.get("stops", []):
        a = int(stp["at"] * SR)
        b = int((stp["at"] + stp.get("len", 0.4)) * SR)
        if stp.get("tape"):
            L = int(0.35 * SR)
            s0 = max(0, a - L)
            seg = music[s0:a].copy()
            if len(seg) > 10:
                # pitch-down by resampling a growing stretch
                idx = np.cumsum(np.linspace(1.0, 0.15, len(seg)))
                idx = np.clip(idx, 0, len(seg) - 1).astype(int)
                music[s0:a] = seg[idx] * np.linspace(1, 0.2, len(seg))[:, None]
        g = np.ones(n_total)
        g[a:b] = 0.0
        g = np.convolve(g, np.ones(96) / 96, mode="same")
        music *= g[:, None]

    music *= db(float(spec.get("music_gain", 0.0)))
    return music, sections


def chord_deg_to_semitone(deg, major):
    sc = scale_degrees(major)
    octv, idx = divmod(deg, 7)
    return sc[idx] + 12 * octv


def master(mix, dur, target=-14.0, fade_out=0.6):
    n = int(dur * SR)
    mix = mix[:n].copy()
    if len(mix) < n:
        mix = np.vstack([mix, np.zeros((n - len(mix), 2))])
    fo = int(fade_out * SR)
    if fo > 0:
        mix[n - fo:] *= np.linspace(1, 0, fo)[:, None] ** 1.5
    mix[: int(0.003 * SR)] *= np.linspace(0, 1, int(0.003 * SR))[:, None]
    meter = pyln.Meter(SR)
    for _ in range(4):
        loud = meter.integrated_loudness(mix)
        if not np.isfinite(loud):
            break
        mix *= db(target - loud)
        # soft limiter at -1 dBFS (oversampled peak estimate)
        ceiling = db(-1.8)  # AAC encoding adds up to ~0.6 dB of true peak; keep the mp4 under -1 dBTP
        over = signal.resample_poly(mix, 4, 1, axis=0)
        peak = np.max(np.abs(over))
        if peak <= ceiling:
            break
        knee = ceiling * 0.7
        a = np.abs(mix)
        comp = np.where(a > knee, knee + (ceiling - knee) * np.tanh((a - knee) / (ceiling - knee)), a)
        mix = np.sign(mix) * comp
    over = signal.resample_poly(mix, 4, 1, axis=0)
    peak = np.max(np.abs(over))
    if peak > db(-1.6):
        mix *= db(-1.6) / peak
    return mix, meter.integrated_loudness(mix)


def aac_guard(mix, ceiling_db=-1.4, rounds=4):
    """Encode like kz.py's mux (ffmpeg AAC 192k), decode, and dip the gain locally (±25 ms) wherever
    the decoded true peak would pass `ceiling_db`. A loud transient right after a quiet moment can
    gain 2 dB in the AAC encode even when the PCM true peak is well under the limiter's ceiling."""
    import shutil
    import subprocess
    import tempfile
    from scipy.ndimage import minimum_filter1d
    if not shutil.which("ffmpeg"):
        return mix
    ceiling = db(ceiling_db)
    w = int(0.025 * SR)
    hann = np.hanning(2 * w + 1)
    hann /= hann.sum()
    with tempfile.TemporaryDirectory() as tmp:
        src, enc, dec = (os.path.join(tmp, f) for f in ("in.wav", "enc.m4a", "dec.wav"))
        for _ in range(rounds):
            sf.write(src, mix.astype(np.float32), SR, subtype="FLOAT")
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", src, "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
                            "-ac", "2", enc], check=True)
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", enc, "-f", "wav", "-acodec", "pcm_f32le", dec], check=True)
            y, _ = sf.read(dec, dtype="float64")
            n = min(len(y), len(mix))
            env = np.abs(signal.resample_poly(y[:n], 4, 1, axis=0)).max(axis=1)[: 4 * n].reshape(n, 4).max(axis=1)
            if env.max() <= ceiling:
                break
            need = np.minimum(1.0, ceiling * 0.97 / np.maximum(env, 1e-9))
            gain = np.convolve(np.pad(minimum_filter1d(need, 2 * w + 1), w, mode="edge"), hann, mode="valid")
            mix = mix.copy()
            mix[:n] *= gain[:, None]
            print(f"aac guard: {20 * np.log10(env.max()):.1f} dBTP after AAC -> dipped {20 * np.log10(gain.min()):.1f} dB "
                  f"at {int((need < 1).sum())} samples")
    return mix


def render(spec_path, out_path, stems=False):
    with open(spec_path) as f:
        spec = json.load(f)
    dur = float(spec["duration"])
    music, sections = render_music(spec)
    n = len(music)
    sfx_bus = np.zeros((n, 2))
    for ev in spec.get("sfx", []):
        x = load_sfx(ev["name"])
        add(sfx_bus, x, float(ev["t"]), db(float(ev.get("gain", -6.0))))
    logo_t = spec.get("logo")
    if logo_t is not None:
        add(sfx_bus, fx_logo(), float(logo_t), db(float(spec.get("logo_gain", -3.0))))
        # duck the music under the logo
        a = int(float(logo_t) * SR)
        g = np.ones(n)
        g[a:] = 0.55
        g = np.convolve(g, np.ones(2400) / 2400, mode="same")
        music *= g[:, None]
    mix = music + sfx_bus
    mix, lufs = master(mix, dur, float(spec.get("lufs", -14.0)), float(spec.get("fade_out", 0.6)))
    mix = aac_guard(mix)
    os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)
    sf.write(out_path, mix.astype(np.float32), SR, subtype="PCM_24")
    if stems:
        base = os.path.splitext(out_path)[0]
        sf.write(base + "_music.wav", master(music, dur)[0].astype(np.float32), SR, subtype="PCM_24")
    peak = 20 * np.log10(np.max(np.abs(signal.resample_poly(mix, 4, 1, axis=0))) + 1e-9)
    print(f"wrote {out_path}: {dur:.2f}s, {lufs:.1f} LUFS, peak {peak:.1f} dBFS, style {spec.get('style')}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("spec", nargs="?")
    ap.add_argument("-o", "--out")
    ap.add_argument("--stems", action="store_true")
    ap.add_argument("--beats", nargs=2, metavar=("BPM", "DURATION"))
    ap.add_argument("--list", action="store_true")
    a = ap.parse_args()
    if a.list:
        print("styles:", ", ".join(f"{k}({v['bpm']})" for k, v in STYLES.items()))
        print("synth sfx:", ", ".join(sorted(SYNTH_FX)))
        files = sorted(f[:-4] for f in os.listdir(KIT_SFX) if f.endswith(".wav"))
        print("file sfx:", ", ".join(files))
        print("sections:", ", ".join(SECTION_MIX))
        return
    if a.beats:
        bpm, d = float(a.beats[0]), float(a.beats[1])
        b = 60.0 / bpm
        k = 0
        rows = []
        while k * b < d:
            rows.append(f"{k * b:6.3f}" + ("  | bar %d" % (k // 4 + 1) if k % 4 == 0 else ""))
            k += 1
        print(f"beat = {b:.4f}s, bar = {4 * b:.4f}s")
        print("\n".join(rows))
        return
    if not a.spec or not a.out:
        ap.error("spec and -o are required")
    render(a.spec, a.out, a.stems)


if __name__ == "__main__":
    main()
