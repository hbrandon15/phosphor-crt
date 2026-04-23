# Phosphor CRT Simulation

A personal project exploring the aesthetics of vintage CRT displays through both a digital simulation pipeline and a practical photography setup. The goal is to render a logo through a CRT visual language — subpixel structure, phosphor glow, scanlines, and analog noise — and evaluate how well a purely digital simulation holds up against a real CRT photograph.

---

## Digital Simulation Pipeline

Processing steps applied programmatically to simulate CRT output:

1. **Input Prep** — Load logo as a high-resolution image, normalize to float
2. **Subpixel Mask** — Generate an RGB stripe or dot triad pattern and apply it as a spatial mask
3. **Scanline Layer** — Darken alternating rows to simulate electron beam scan gaps
4. **Phosphor Bloom** — Apply a Gaussian blur to bright areas to simulate phosphor glow and light spread
5. **Vignette** — Darken edges to simulate CRT curvature and electron beam falloff
6. **Color Grading** — Shift white point toward the bluish-green phosphor cast typical of vintage CRTs
7. **Noise Layer** — Add subtle low-level noise to simulate analog signal interference
8. **Output** — Export final simulated image

---

## Practical Setup

Steps for capturing the logo on a real CRT and photographing the result:

1. **Logo Design** — Create a personal brand mark that works at CRT resolution
2. **Signal Setup** — Identify CRT inputs, source cables, get logo displaying stably
3. **Environment Setup** — Control ambient light, eliminate reflections, warm up CRT
4. **Camera Setup** — Dial in Sony a7 IV for screen photography, manage moiré
5. **The Shoot** — Capture RAW stills, shoot tethered if possible
6. **Digital Simulation Pipeline** — Apply CRT simulation filters to the logo digitally
7. **Comparison Analysis** — Side-by-side evaluation of practical vs. digital output
8. **Post Processing** — White balance correction, color grading, final selects
9. **Deliverable Output** — Final images, simulation output, README
