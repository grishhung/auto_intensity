from enums import Diff, Forcing
from chord import Chord
from constants import *

from typing import List, Type
from mido import MidiFile, MetaMessage


class Chart:
    def __init__(self, name: str, diff: Type[Diff], chords: List[Type[Chord]]):
        self.name = name
        self.diff = diff
        self.chords = chords

    def add_chord(self, chord: Type[Chord]):
        self.chords.append(chord)

    def read_chart(self, filename: str, track_name: str):
        try:
            mid = MidiFile(filename)
        except:
            return
        track_indices = [i for i in range(len(mid.tracks)) if mid.tracks[i].name == track_name]
        if len(track_indices) < 1:
            return
        track = mid.tracks[track_indices[0]]
        track.append(MetaMessage('end_of_track', time=1))
        ticks_per_beat = mid.ticks_per_beat

        tempo_list = []
        tempo_msg_time = 0
        for msg in mid.tracks[0]:
            tempo_msg_time += msg.time
            if msg.type == 'set_tempo':
                tempo_list.append((tempo_msg_time, msg.tempo))
        tempo_list.append((10**10,0))
        tempo_ptr = 0
        
        current_time = 0
        previous_time = 0
        current_tick = 0
        previous_tick = 0
        current_chord = 0b_00000_0
        active_mods = []
        mid_to_note = MID_TO_NOTE[self.diff]
        mid_to_mod = MID_TO_MOD[self.diff]
        for msg in track:
            ticks_to_add = msg.time
            while tempo_list[tempo_ptr+1][0] < current_tick + ticks_to_add:
                added_ticks = tempo_list[tempo_ptr+1][0] - current_tick
                current_time += added_ticks / ticks_per_beat * tempo_list[tempo_ptr][1] / 1000000
                ticks_to_add -= added_ticks
                current_tick += added_ticks
                tempo_ptr += 1
            current_time += ticks_to_add / ticks_per_beat * tempo_list[tempo_ptr][1] / 1000000
            current_tick += ticks_to_add
            
            if msg.type not in ['note_on', 'note_off']:
                continue
            if (msg.note in mid_to_mod.keys()):
                if msg.type == 'note_on':
                    active_mods.append(msg.note)
                elif msg.type == 'note_off':
                    active_mods.remove(msg.note)
                continue
            if msg.note not in mid_to_note.keys():
                continue
            
            if msg.type == 'note_on':
                if current_tick > previous_tick:
                    if current_chord != 0b_00000_0:
                        forcing = Forcing.STRUM
                        if current_tick - previous_tick >= 170:
                            forcing = Forcing.HOPO
                        if len(active_mods) > 0:
                            forcing = mid_to_mod[max(active_mods)]
                        chord = Chord(previous_time, current_chord, forcing)
                        self.add_chord(chord)
                        current_chord = 0b_00000_0
                    previous_tick = current_tick
                    previous_time = current_time
                current_chord += mid_to_note[msg.note]
