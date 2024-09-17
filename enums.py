from enum import Enum


class Diff(Enum):
    EASY = 0
    MEDIUM = 1
    HARD = 2
    EXPERT = 3


class Forcing(Enum):
    STRUM = 0
    HOPO = 1
    TAP = 2
