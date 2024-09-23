import math

from constants import *
from enums import Diff, Forcing
from typing import Dict, Type, List
from utils import *


class Chord:
    time: float = None              # The timestamp of the chord, NOT length
    shape: float = None             # Bitwise; 0b_00011_0 = GR; 0b_00000_1 = P
    forcing: Type[Forcing] = None   # Strum, HOPO, or tap
    laned: bool = None              # Whether this note is in a lane

    leniency: float = None          # Extra amount of time allowed by 140ms hit window based on previous notes
    lh_vel: List[float] = []        # Reciprocals of delta time from previous distinct chords (includes leniency)
    rh_vel: List[float] = []        # Reciprocals of delta time from previous strummed chords (includes leniency)
    vel: float = None               # Reciprocal of delta time from previous chord
    acc: float = None               # Acceleration by delta velocity

    presses: Shape = None           # New frets that WERE NOT in the last
    lifts: Shape = None             # Absent frets that WERE in the last
    holds: Shape = None             # Present frets that WERE in the last, or NONE if identical
    lh_actions: List[int] = None    # Number of LH actions relative to previous distinct chords
    rh_actions: int = None          # Number of RH actions

    anchorable_shape: Shape = None  # SHAPE that you're ALLOWED to anchor
    anchored_shape: Shape = None    # SHAPE that MAY be anchored at this time
    anchored_count: int = None      # COUNT of frets in anchored_shape

    lh_complexity: float = None     # Composite fretting complexity
    rh_complexity: float = None     # Composite strumming complexity


    def __init__(self, time: float, shape: Shape, forcing: Type[Forcing], laned: bool):
        self.time = time
        self.shape = shape
        self.forcing = forcing
        self.laned = laned

        # If a single B (0b_01000_0), then all frets under + open (0b_00111_1)
        self.anchorable_shape = shape - 1 if self.is_single_note() else shape


    def is_single_note(self) -> bool:
        """Return True if only one bit (fret) is 1"""
        shape = self.shape
        return shape > 0 and (shape & (shape - 1)) == 0

    def set_leniency(self, leniency: float):
        self.leniency = leniency


    def set_lh_vel(self, prev_times: List[float]) -> None:
        lane_multiplier = 1 + self.laned
        self.lh_vel = [1 / (lane_multiplier * (self.time - prev_time) + self.leniency) for prev_time in prev_times]


    def set_rh_vel(self, prev_times: List[float]) -> None:
        lane_multiplier = 1 + self.laned
        self.rh_vel = [1 / (lane_multiplier * (self.time - prev_time) + self.leniency) for prev_time in prev_times]


    def set_vel(self, prev_time: float) -> None:
        self.vel = 1 / (self.time - prev_time)


    def set_acc(self, prev_vel: float) -> None:
        self.acc = self.vel - prev_vel


    def set_anchored_shape_and_count(self, prev_anchored_shape: Shape) -> None:
        self.anchored_shape = self.shape & prev_anchored_shape
        self.anchored_count = count_frets(self.anchored_shape)


    def set_presses(self, prev_shapes: List[Shape]) -> None:
        """Return frets pressed in the current shape, but not the previous"""
        self.presses = [(self.shape >> 1) & ~(prev_shape >> 1) for prev_shape in prev_shapes]


    def set_lifts(self, prev_shapes: List[Shape]) -> None:
        """Return frets pressed in the previous shape, but not the current"""
        self.lifts = [(prev_shape >> 1) & ~(self.shape >> 1) for prev_shape in prev_shapes]


    def set_lh_actions(self) -> None:
        # Composite of presses and lifts
        self.lh_actions = [count_frets(self.lifts[i]) + count_frets(self.presses[i]) for i in range(len(self.lifts))]


    def set_rh_actions(self, prev_shape: Shape) -> None:
        # 1 if a strum or identical shape to previous chord
        self.rh_actions = FORCING_TO_RH_ACTIONS[self.forcing] or (prev_shape == self.shape)


    def get_intensity(self) -> float:
        """Local intensity of the current chord"""
        lh_intensity = sum([self.lh_vel[i] * self.lh_actions[i] for i in range(len(self.lh_vel))])
        rh_intensity = sum(self.rh_vel) * self.rh_actions
        
        # Expected contribution of the chord n previous is 1/n, readjust sum accordingly
        note_lookback_factor = 1 / sum([1 / i for i in range(1, len(self.lh_vel) + 1)])
        
        # Floor of a note's intensity is 1 (1 action per second; a refretting + strum takes 3 actions)
        local_intensity = max(1, note_lookback_factor * (lh_intensity + rh_intensity))
        return local_intensity
