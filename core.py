from chart import Chart
from chord import Chord
from constants import *
from enums import Diff, Forcing
from typing import Any, List, Dict, Type, TypeAlias

import math

def set_vels(chords: List[Type[Chord]]) -> None:
    for i, chord in enumerate(chords):
        if i < 1:
            # The first chord has no local velocity
            chord.vel = 0.0
        else:
            # Velocity = the change in time
            chord.set_vel(chords[i - 1].time)


def set_accs(chords: List[Type[Chord]]) -> None:
    for i, chord in enumerate(chords):
        if i < 2:
            # The first two chords have no local acceleration
            chord.acc = 0.0
        else:
            # Acceleration = the change in velocity
            chord.set_acc(chords[i - 1].vel)


def set_leniencies(chords: List[Type[Chord]]) -> None:
    radius = HIT_WINDOW_SIZE / 2
    strum_factor = radius - STRUM_NOTE_LENIENCY
    for i, chord in enumerate(chords):
        if i < 1:
            chord.set_leniency(0.0)
        elif i < 2:
            chord.set_leniency(2 * radius - strum_factor * chords[i-1].rh_actions)
        else:
            diff = chord.time - chords[i-1].time
            lower_bound = diff
            upper_bound = diff + 2 * radius - strum_factor * chords[i-1].rh_actions
            j = i-2
            leniency = -1
            while (j > 0) and (upper_bound - lower_bound > HIT_WINDOW_NOISE):
                new_lower = (chord.time - chords[j].time) / (i - j)
                new_upper = (chord.time - chords[j].time + 2 * radius - strum_factor * chords[j].rh_actions) / (i - j)
                if new_lower > upper_bound:
                    leniency = upper_bound
                    break
                if new_upper < lower_bound:
                    leniency = lower_bound
                    break
                upper_bound = min(upper_bound, new_upper)
                lower_bound = max(lower_bound, new_lower)
                j -= 1
            if leniency < 0:
                if j == 0:
                    leniency = upper_bound
                else:
                    leniency = lower_bound
            leniency -= diff
            chord.set_leniency(leniency)


def set_lh_actions(chords: List[Type[Chord]]) -> None:
    fretting_indices = [0,0]
    for i, chord in enumerate(chords):
        if i < 1:
            chord.lh_complexity = 0.0
        else:
            if chords[i - 1].shape != chord.shape:
                fretting_indices.append(i - 1)
                fretting_indices.pop(0)
            prev_chords = [chords[fretting_indices[-1]], chords[fretting_indices[-2]]]
            prev_shapes = [chord.shape for chord in prev_chords]
            prev_times = [chord.time for chord in prev_chords]
            chord.set_presses(prev_shapes)
            chord.set_lifts(prev_shapes)
            chord.set_lh_vel(prev_times)
            chord.set_lh_actions()


def set_rh_actions(chords: List[Type[Chord]]) -> None:
    strum_indices = [0,0]
    for i, chord in enumerate(chords):
        if i < 1:
            chord.rh_complexity = 0.0
            chord.rh_actions = 1
            chord.overstrum_prob = 1
        else:
            prev_chords = [chords[strum_indices[-1]], chords[strum_indices[-2]]]
            prev_times = [chord.time for chord in prev_chords]
            chord.set_rh_actions(chords[i - 1].shape)
            if i == len(chords) - 1:
                chord.overstrum_prob = chord.rh_actions
            else:
                chord.set_overstrum_prob(chords[i + 1].shape, chords[i + 1].time)
            if chord.rh_actions:
                strum_indices.append(i)
                strum_indices.pop(0)


def set_rh_vels(chords: List[Type[Chord]]) -> None:
    strum_indices = [0,0]
    for i, chord in enumerate(chords):
        if i < 1:
            chord.rh_complexity = 0.0
        else:
            prev_chords = [chords[strum_indices[-1]], chords[strum_indices[-2]]]
            prev_times = [chord.time for chord in prev_chords]
            chord.set_rh_vel(prev_times)
            if chord.rh_actions:
                strum_indices.append(i)
                strum_indices.pop(0)


def set_anchored_shapes_and_counts(chords: List[Type[Chord]]) -> None:
    for i, chord in enumerate(chords):
        if i < 1:
            # No frets anchored
            chord.anch_frets = 0
        else:
            chord.set_anchored_shape_and_count(chords[i - 1].anchorable_shape)


def print_name(name: str, is_last_chart: bool) -> None:
    print(('├' if not is_last_chart else '└') + f'── {name}')


def print_stat(stat: str, value: float, is_last_chart: bool,
               is_last_stat: bool) -> None:
    print(('│' if not is_last_chart else ' ') + '   '
            + ('├' if not is_last_stat else '└')
            + f'── {stat:<20}{value}')


def prepare_chart_for_stat_collection(chart: Type[Chart]) -> None:
    chords = chart.chords

    set_vels(chords)
    set_accs(chords)
    set_anchored_shapes_and_counts(chords)
    set_rh_actions(chords)
    set_leniencies(chords)
    set_rh_vels(chords)
    set_lh_actions(chords)

def find_min_pass_intensity(intensities, strums, overstrum_probs, meter, start):
    if len(intensities) == 0:
        return MIN_CAPABILITY
    left = MIN_CAPABILITY
    right = max(intensities)
    while right - left > 0.005:
        capability = (left + right) / 2
        meter_level = start
        skill_heatsink_max = capability * SKILL_HEATSINK_MAX
        skill_heatsink = skill_heatsink_max
        chart_passed = True
        prev_hit_prob = 1
        for i, intensity in enumerate(intensities):
            if skill_heatsink > 0:
                skill_heatsink = min(skill_heatsink_max, skill_heatsink + capability - intensity)
            else:
                skill_heatsink = skill_heatsink + capability
            if skill_heatsink > 0:
                hit_prob = 1
            else:
                hit_prob = min(capability / intensity, 1)
            overstrum_prob = overstrum_probs[i]
            # To do: implement feature that taps don't need recovery
            if strums[i]:
                e_prev_hit = hit_prob * 0.25 - (1 - hit_prob) * (1 + overstrum_prob)
                e_prev_miss = hit_prob * 0.25 - (1 - hit_prob) * (1 + overstrum_prob)
            else:
                e_prev_hit = hit_prob * 0.25 - (1 - hit_prob)
                e_prev_miss = HOPO_RECOVERY * (hit_prob * 0.25 - (1 - hit_prob) * (1 + overstrum_prob)) - (1 - HOPO_RECOVERY)
            expected_change = prev_hit_prob * e_prev_hit + (1 - prev_hit_prob) * e_prev_miss
            meter_level = min(meter, meter_level+expected_change)
            prev_hit_prob = hit_prob
            if meter_level < 0:
                chart_passed = False
                break
        if chart_passed:
            right = capability
        else:
            left = capability
    return right


def calculate_chart_stats(chart: Type[Chart], is_last: bool) -> None:
    chords = chart.chords
    n = len(chords)

    '''
    avg_vel = sum([c.vel for c in chords[1:]]) / (n - 1)
    avg_abs_acc = sum([abs(c.acc) for c in chords[2:]]) / (n - 2)
    avg_lh_actions = sum([c.lh_actions for c in chords[1:]]) / (n - 1)
    avg_anch = sum([c.anchored_count for c in chords[1:]]) / (n - 1)
    '''

    local_intensities = [chord.get_intensity() for chord in chords[1:]]
    strums = [chord.rh_actions for chord in chords[1:]]
    overstrum_probs = [chord.overstrum_prob for chord in chords[1:]]

    if False:
        for i in range(len(chords[1:])):
            print(chords[i].leniency)

    min_pass_intensity = find_min_pass_intensity(local_intensities, strums, overstrum_probs, DIFF_TO_ROCK_METER_SIZE[chart.diff], 5 * DIFF_TO_ROCK_METER_SIZE[chart.diff] // 6)

    # Make chart intensity agnostic with respect to the rock meter size
    # chart_intensity = CURVE_FINAL_MULT * math.log(relative_intensity_max / sample_size, 2)
    chart_intensity = CURVE_FINAL_MULT * max(0, math.log(min_pass_intensity / MIN_CAPABILITY, 2))

    print_name(chart.name, is_last)
    print_stat('note count', f'{n:.2f} n', is_last, False)
    #print_stat('avg vel', f'{avg_vel:.2f} n/s', is_last, False)
    #print_stat('avg abs acc', f'{avg_abs_acc:.2f} n/s^2', is_last, False)
    #print_stat('avg LH actions', f'{avg_lh_actions:.2f}', is_last, False)
    #print_stat('avg anchor count', f'{avg_anch:.2f}', is_last, False)
    print_stat('intensity', f'{chart_intensity:.2f}', is_last, True)


def calculate_all_chart_stats(charts: List[Type[Chart]]):
    print('CHART STATISTICS')
    for i, chart in enumerate(charts):
        prepare_chart_for_stat_collection(chart)
        calculate_chart_stats(chart, i == len(charts) - 1)
