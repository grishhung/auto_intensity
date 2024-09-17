from typing import Dict
from enums import *

GLOBAL_COEFF = 1
CURVE_LOG_BASE = 2

# Chosen arbitrarily; subject to change
FORCING_TO_RH_ACTIONS: Dict[Forcing, int] = {
    Forcing.STRUM: 1,
    Forcing.HOPO: 0,
    Forcing.TAP: 0,
}


# Based roughly on subsequent multiplications by 0.75 
DIFF_TO_ROCK_METER_SIZE: Dict[Diff, int] = {
    Diff.EASY: 21,
    Diff.MEDIUM: 28,
    Diff.HARD: 37,
    Diff.EXPERT: 50,
}
