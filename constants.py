from typing import Dict
from enums import *

GLOBAL_COEFF = 1.4
CURVE_FINAL_MULT = 3.1 # Curve so that scale is 0.0-15.0/20.0 for setlist/customs 
CURVE_LEN_COEFF = 5

# Based on assumption: playing same song twice = ? increase in difficulty 
ENDURANCE_CURVE = 0.0

# Based on whether a strum is required
FORCING_TO_RH_ACTIONS: Dict[Forcing, int] = {
    Forcing.STRUM: 1,
    Forcing.HOPO: 0,
    Forcing.TAP: 0,
}

# Based roughly on subsequent multiplications by 0.75 
DIFF_TO_ROCK_METER_SIZE: Dict[Diff, int] = {
    Diff.EASY: 30, # 21,
    Diff.MEDIUM: 36, # 28,
    Diff.HARD: 42, # 37,
    Diff.EXPERT: 42 # 50
}

# MIDI to notes and markers
MID_TO_NOTE: Dict[Diff, Dict[int, int]] = {
    Diff.EASY: {
        59: 0b_00000_1,
        60: 0b_00001_0,
        61: 0b_00010_0,
        62: 0b_00100_0,
        63: 0b_01000_0,
        64: 0b_10000_0,
    },
    Diff.MEDIUM: {
        71: 0b_00000_1,
        72: 0b_00001_0,
        73: 0b_00010_0,
        74: 0b_00100_0,
        75: 0b_01000_0,
        76: 0b_10000_0,
    },
    Diff.HARD: {
        83: 0b_00000_1,
        84: 0b_00001_0,
        85: 0b_00010_0,
        86: 0b_00100_0,
        87: 0b_01000_0,
        88: 0b_10000_0,
    },
    Diff.EXPERT: {
        95: 0b_00000_1,
        96: 0b_00001_0,
        97: 0b_00010_0,
        98: 0b_00100_0,
        99: 0b_01000_0,
        100: 0b_10000_0,
    }
}

MID_TO_MOD: Dict[Diff, Dict[int, Forcing]] = {
    Diff.EASY: {
        65: Forcing.HOPO,
        66: Forcing.STRUM,
        104: Forcing.TAP
    },
    Diff.MEDIUM: {
        77: Forcing.HOPO,
        78: Forcing.STRUM,
        104: Forcing.TAP
    },
    Diff.HARD: {
        89: Forcing.HOPO,
        90: Forcing.STRUM,
        104: Forcing.TAP
    },
    Diff.EXPERT: {
        101: Forcing.HOPO,
        102: Forcing.STRUM,
        104: Forcing.TAP
    }
}
