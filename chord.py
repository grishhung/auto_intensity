import math

from constants import *
from enums import Diff, Forcing
from typing import Dict, Type
from utils import *


class Chord:
    time: float = None              # The timestamp of the chord, NOT length
    shape: float = None             # Bitwise; 0b_00011_0 = GR; 0b_00000_1 = P
    forcing: Type[Forcing] = None   # Strum, HOPO, or tap

    vel: float = None               # Reciprocal of delta time
    acc: float = None               # Acceleration by delta velocity

    presses: Shape = None           # New frets that WERE NOT in the last
    lifts: Shape = None             # Absent frets that WERE in the last
    lh_actions: int = None          # All possible LH actions per the chart
    rh_actions: int = None          # Number of RH actions

    anchorable_shape: Shape = None  # SHAPE that you're ALLOWED to anchor
    anchored_shape: Shape = None    # SHAPE that MAY be anchored at this time
    anchored_count: int = None      # COUNT of frets in anchored_shape

    lh_complexity: float = None     # Composite fretting complexity
    rh_complexity: float = None     # Composite strumming complexity


    def __init__(self, time: float, shape: Shape, forcing: Type[Forcing]):
        self.time = time
        self.shape = shape
        self.forcing = forcing
        self.rh_actions = FORCING_TO_RH_ACTIONS[forcing]

        # If a single B (0b_01000_0), then all frets under + open (0b_00111_1)
        self.anchorable_shape = shape - 1 if self.is_single_note() else shape


    def is_single_note(self) -> bool:
        """Return True if only one bit (fret) is 1"""
        shape = self.shape
        return shape > 0 and (shape & (shape - 1)) == 0


    def set_vel(self, prev_time: float) -> None:
        self.vel = 1 / (self.time - prev_time);


    def set_acc(self, prev_vel: float) -> None:
        self.acc = self.vel - prev_vel


    def set_anchored_shape_and_count(self, prev_anchored_shape: Shape) -> None:
        self.anchored_shape = self.shape & prev_anchored_shape
        self.anchored_count = count_frets(self.anchored_shape)


    def set_presses(self, prev_shape: Shape) -> None:
        """Return frets pressed in the current shape, but not the previous"""
        self.presses = (self.shape >> 1) & ~(prev_shape >> 1)


    def set_lifts(self, prev_shape: Shape) -> None:
        """Return frets pressed in the previous shape, but not the current"""
        self.lifts = (prev_shape >> 1) & ~(self.shape >> 1)


    def set_lh_actions(self) -> None:
        # Composite of presses and lifts
        self.lh_actions = count_frets(self.presses) + count_frets(self.lifts)


    def get_intensity(self) -> float:
        """Local intensity of the current chord"""
        # Each note requires at least one action
        # Floor of a note's intensity is 1 (1 action per second; a refretting + strum takes 3 actions)
        local_intensity = max(1, self.vel * max(1, self.lh_actions + self.rh_actions))
        return local_intensity
