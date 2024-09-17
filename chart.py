from enums import Diff
from chord import Chord

from typing import List, Type


class Chart:
    def __init__(self, name: str, diff: Type[Diff], chords: List[Type[Chord]]):
        self.name = name
        self.diff = diff
        self.chords = chords
