# `octabam-stems` — STEM REC, KITS, MUTE_MODES and USB

Multitrack recording to the card with Kits, the mute modes and USB audio
and MIDI, on the 14 stock effects. No octabam DSP code.

## What is in it

- **STEM REC** (yvesrosius): UP + REC opens STEMS and records each track
  after its fader, MAIN, CUE and the inputs as separate WAV files, each
  with a `.ot` beside it that carries the take's tempo and a playback gain.
  [The module page](../../modules/stems/README.md).
- **KITS** (sambanks, after Em's Octakit) with **STORE**, which it needs:
  255 Kits per project. [The module page](../../modules/kits/README.md).
- **MUTE_MODES** (Zac Kyoti), from DRAM.
  [The module page](../../modules/mute-modes/README.md).
- **USB** at MAIN CUE with MIDI, the inputs off.
  [The module page](../../modules/usb/README.md).
- **BRAIN**, so USB's settings can change on the unit.
- **The 14 stock effects**, so the FX2 chooser is stock's.

Not LOAD METER: it refuses STEM REC by name until the two are measured
together.

## Memory

The platform reserve takes 18.9 MB of the sample arena, 11,529 pages
(67 MB) left for samples and recorders (stock 14,602). STEM REC's 8 MiB
ring sits above REMIX SWITCH's image stage, which it does not overlap.

## Status

Under the port only, not flashed. `make check-remix REMIX=octabam-stems`
(21 Oct 2026, EZBot's Ultimate FX 1.5.3 as the STEMS fixture): 339 pass,
26 fail. Every gate of KITS, STORE, MUTE_MODES, USB, BRAIN, REMIX SWITCH
and the boot passes. The failures are `verify_stems`' takes, as on the
`stems` remix and on `main` itself under today's port: the writer is
still saving when a run's frames end (`master` passes at 1,200 frames
instead of 300). One differs from `stems`: `cardfail`'s refused write
does not hang the writer here (state IDLE, 20 sectors), not yet
explained.

## Build

```bash
make image REMIX=octabam-stems BUILD=N
```

[BUILDING.md](../../docs/guide/BUILDING.md) has every step to a flashed
unit, and the way back to stock.
