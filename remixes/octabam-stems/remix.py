"""octabam-stems -- STEM REC with KITS, MUTE_MODES and USB on the stock effects.

STEM REC (multitrack to the card), KITS (255 Kits per project, Em's Octakit
design; needs STORE), MUTE_MODES from DRAM, USB at MAIN CUE with MIDI, and
BRAIN so USB's settings can change on the unit, on all 14 stock effects. No
octabam DSP code. Not LOAD METER: it refuses STEM REC by name.
"""

from remix.schema import Pin, Proof, Remix

STOCK14 = ("FILTER", "EQUALIZER", "DJ EQ", "PHASER", "FLANGER", "CHORUS", "SPATIALIZER",
           "COMB FILTER", "COMPRESSOR", "LO-FI", "DELAY", "PLATE REV", "SPRING REV", "DARK REV")

REMIX = Remix(
    name="octabam-stems",
    family="mods", proof=Proof.PORT, proof_note="make check-remix under the port, 21 Oct 2026: every gate but verify_stems' takes (frame budgets); not flashed",
    doc="STEM REC with KITS, MUTE_MODES and USB (MAIN CUE and MIDI) on the 14 stock effects.",
    modules=("STEM REC", "KITS", "STORE", "MUTE_MODES", "USB", "BRAIN") + STOCK14,
    fallback="NONE",
    settings={("octabam.usb", "TRACKS"): "PRE", ("octabam.usb", "MAIN"): 1,
              ("octabam.usb", "CUE"): 1, ("octabam.usb", "MASTER"): 0,
              ("octabam.usb", "IN"): Pin("OFF"),
              ("kyoti.mute-modes", "PLACE"): Pin("DRAM")},
)
