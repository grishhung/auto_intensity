from chart import Chart
from chord import Chord
from enums import *

# Sanity test (Swing)
SANITY_SWING = Chart('Sanity Swing', Diff.EXPERT, [
    # 1.1
    Chord(0.000, 0b_00001_0, Forcing.STRUM),
    Chord(0.333, 0b_00001_0, Forcing.STRUM),
    Chord(0.500, 0b_00001_0, Forcing.STRUM),
    Chord(0.667, 0b_00001_0, Forcing.STRUM),
    Chord(1.000, 0b_00001_0, Forcing.STRUM),
    Chord(1.333, 0b_00001_0, Forcing.STRUM),
    Chord(1.500, 0b_00001_0, Forcing.STRUM),
    Chord(1.667, 0b_00001_0, Forcing.STRUM),

    # 1.2
    Chord(2.000, 0b_00001_0, Forcing.STRUM),
    Chord(2.333, 0b_00001_0, Forcing.STRUM),
    Chord(2.500, 0b_00001_0, Forcing.STRUM),
    Chord(2.667, 0b_00001_0, Forcing.STRUM),
    Chord(3.000, 0b_00001_0, Forcing.STRUM),
    Chord(3.333, 0b_00001_0, Forcing.STRUM),
    Chord(3.500, 0b_00001_0, Forcing.STRUM),
    Chord(3.667, 0b_00001_0, Forcing.STRUM),

    # 1.3
    Chord(4.000, 0b_00001_0, Forcing.STRUM),
    Chord(4.333, 0b_00001_0, Forcing.STRUM),
    Chord(4.500, 0b_00001_0, Forcing.STRUM),
    Chord(4.667, 0b_00001_0, Forcing.STRUM),
    Chord(5.000, 0b_00001_0, Forcing.STRUM),
    Chord(5.333, 0b_00001_0, Forcing.STRUM),
    Chord(5.500, 0b_00001_0, Forcing.STRUM),
    Chord(5.667, 0b_00001_0, Forcing.STRUM),

    # 1.4
    Chord(6.000, 0b_00001_0, Forcing.STRUM),
    Chord(6.333, 0b_00001_0, Forcing.STRUM),
    Chord(6.500, 0b_00001_0, Forcing.STRUM),
    Chord(6.667, 0b_00001_0, Forcing.STRUM),
    Chord(7.000, 0b_00001_0, Forcing.STRUM),
    Chord(7.333, 0b_00001_0, Forcing.STRUM),
    Chord(7.500, 0b_00001_0, Forcing.STRUM),
    Chord(7.667, 0b_00001_0, Forcing.STRUM),
])


# Sanity test (Anchor, YGYR)
SANITY_ANCHOR_YGYR = Chart("Sanity Anchor (YGYR)", Diff.EXPERT, [
    # 1.1
    Chord(0.000, 0b_00100_0, Forcing.STRUM),
    Chord(0.200, 0b_00001_0, Forcing.STRUM),
    Chord(0.400, 0b_00100_0, Forcing.STRUM),
    Chord(0.600, 0b_00010_0, Forcing.STRUM),

    # 1.2
    Chord(0.800, 0b_00100_0, Forcing.STRUM),
    Chord(1.000, 0b_00001_0, Forcing.STRUM),
    Chord(1.200, 0b_00100_0, Forcing.STRUM),
    Chord(1.400, 0b_00010_0, Forcing.STRUM),

    # 1.3
    Chord(1.600, 0b_00100_0, Forcing.STRUM),
    Chord(1.800, 0b_00001_0, Forcing.STRUM),
    Chord(2.000, 0b_00100_0, Forcing.STRUM),
    Chord(2.200, 0b_00010_0, Forcing.STRUM),

    # 1.4
    Chord(2.400, 0b_00100_0, Forcing.STRUM),
    Chord(2.600, 0b_00001_0, Forcing.STRUM),
    Chord(2.800, 0b_00100_0, Forcing.STRUM),
    Chord(3.000, 0b_00010_0, Forcing.STRUM),

    # 2.1
    Chord(3.200, 0b_00100_0, Forcing.STRUM),
    Chord(3.400, 0b_00001_0, Forcing.STRUM),
    Chord(3.600, 0b_00100_0, Forcing.STRUM),
    Chord(3.800, 0b_00010_0, Forcing.STRUM),

    # 2.2
    Chord(4.000, 0b_00100_0, Forcing.STRUM),
    Chord(4.200, 0b_00001_0, Forcing.STRUM),
    Chord(4.400, 0b_00100_0, Forcing.STRUM),
    Chord(4.600, 0b_00010_0, Forcing.STRUM),

    # 2.3
    Chord(4.800, 0b_00100_0, Forcing.STRUM),
    Chord(5.000, 0b_00001_0, Forcing.STRUM),
    Chord(5.200, 0b_00100_0, Forcing.STRUM),
    Chord(5.400, 0b_00010_0, Forcing.STRUM),

    # 2.4
    Chord(5.600, 0b_00100_0, Forcing.STRUM),
    Chord(5.800, 0b_00001_0, Forcing.STRUM),
    Chord(6.000, 0b_00100_0, Forcing.STRUM),
    Chord(6.200, 0b_00010_0, Forcing.STRUM),
])


# Sanity test (Anchor, YGYR)
SANITY_ANCHOR_YGYG = Chart("Sanity Anchor (YGYG)", Diff.EXPERT, [
    # 1.1
    Chord(0.000, 0b_00100_0, Forcing.STRUM),
    Chord(0.200, 0b_00001_0, Forcing.STRUM),
    Chord(0.400, 0b_00100_0, Forcing.STRUM),
    Chord(0.600, 0b_00001_0, Forcing.STRUM),

    # 1.2
    Chord(0.800, 0b_00100_0, Forcing.STRUM),
    Chord(1.000, 0b_00001_0, Forcing.STRUM),
    Chord(1.200, 0b_00100_0, Forcing.STRUM),
    Chord(1.400, 0b_00001_0, Forcing.STRUM),

    # 1.3
    Chord(1.600, 0b_00100_0, Forcing.STRUM),
    Chord(1.800, 0b_00001_0, Forcing.STRUM),
    Chord(2.000, 0b_00100_0, Forcing.STRUM),
    Chord(2.200, 0b_00001_0, Forcing.STRUM),

    # 1.4
    Chord(2.400, 0b_00100_0, Forcing.STRUM),
    Chord(2.600, 0b_00001_0, Forcing.STRUM),
    Chord(2.800, 0b_00100_0, Forcing.STRUM),
    Chord(3.000, 0b_00001_0, Forcing.STRUM),

    # 2.1
    Chord(3.200, 0b_00100_0, Forcing.STRUM),
    Chord(3.400, 0b_00001_0, Forcing.STRUM),
    Chord(3.600, 0b_00100_0, Forcing.STRUM),
    Chord(3.800, 0b_00001_0, Forcing.STRUM),

    # 2.2
    Chord(4.000, 0b_00100_0, Forcing.STRUM),
    Chord(4.200, 0b_00001_0, Forcing.STRUM),
    Chord(4.400, 0b_00100_0, Forcing.STRUM),
    Chord(4.600, 0b_00001_0, Forcing.STRUM),

    # 2.3
    Chord(4.800, 0b_00100_0, Forcing.STRUM),
    Chord(5.000, 0b_00001_0, Forcing.STRUM),
    Chord(5.200, 0b_00100_0, Forcing.STRUM),
    Chord(5.400, 0b_00001_0, Forcing.STRUM),

    # 2.4
    Chord(5.600, 0b_00100_0, Forcing.STRUM),
    Chord(5.800, 0b_00001_0, Forcing.STRUM),
    Chord(6.000, 0b_00100_0, Forcing.STRUM),
    Chord(6.200, 0b_00001_0, Forcing.STRUM),
])


# One, Darkness Riff
DARKNESS_RIFF = Chart('Darkness Riff', Diff.EXPERT, [
    # 1.1
    Chord(0.000, 0b_00001_0, Forcing.STRUM),
    Chord(0.090, 0b_00001_0, Forcing.STRUM),
    Chord(0.181, 0b_00001_0, Forcing.STRUM),
    Chord(0.272, 0b_00001_0, Forcing.STRUM),
    Chord(0.363, 0b_00001_0, Forcing.STRUM),
    Chord(0.454, 0b_00001_0, Forcing.STRUM),

    # 1.2
    Chord(0.545, 0b_00101_0, Forcing.STRUM),
    
    # 1.3
    Chord(1.090, 0b_00001_0, Forcing.STRUM),
    Chord(1.181, 0b_00001_0, Forcing.STRUM),
    Chord(1.272, 0b_00001_0, Forcing.STRUM),
    Chord(1.363, 0b_00001_0, Forcing.STRUM),
    Chord(1.454, 0b_00001_0, Forcing.STRUM),
    Chord(1.545, 0b_00001_0, Forcing.STRUM),

    # 1.4
    Chord(1.636, 0b_00101_0, Forcing.STRUM),

    # 2.1
    Chord(2.181, 0b_00001_0, Forcing.STRUM),
    Chord(2.272, 0b_00001_0, Forcing.STRUM),
    Chord(2.363, 0b_00001_0, Forcing.STRUM),
    Chord(2.454, 0b_00001_0, Forcing.STRUM),
    Chord(2.545, 0b_00001_0, Forcing.STRUM),
    Chord(2.636, 0b_00001_0, Forcing.STRUM),

    # 2.2
    Chord(2.727, 0b_00101_0, Forcing.STRUM),

    # 2.3
    Chord(3.272, 0b_00001_0, Forcing.STRUM),
    Chord(3.363, 0b_00001_0, Forcing.STRUM),
    Chord(3.454, 0b_00001_0, Forcing.STRUM),
    Chord(3.545, 0b_00001_0, Forcing.STRUM),
    Chord(3.636, 0b_00001_0, Forcing.STRUM),
    Chord(3.727, 0b_00001_0, Forcing.STRUM),

    # 2.4
    Chord(3.818, 0b_00101_0, Forcing.STRUM),
])


# A Punk, Intro - 1.1.000 to 11.1.000
INTRO_A_PUNK = Chart('Intro (A Punk)', Diff.EXPERT, [
    # 1.1
    Chord(0.000, 0b_01100_0, Forcing.STRUM),
    Chord(0.171, 0b_01100_0, Forcing.STRUM),
    Chord(0.343, 0b_10100_0, Forcing.STRUM),
    Chord(0.514, 0b_10100_0, Forcing.STRUM),
    Chord(0.686, 0b_00110_0, Forcing.STRUM),
    Chord(0.857, 0b_00110_0, Forcing.STRUM),
    Chord(1.029, 0b_01010_0, Forcing.STRUM),
    Chord(1.200, 0b_01010_0, Forcing.STRUM),

    # 2.1
    Chord(1.371, 0b_00011_0, Forcing.STRUM),
    Chord(1.543, 0b_00011_0, Forcing.STRUM),
    Chord(1.714, 0b_00011_0, Forcing.STRUM),
    Chord(1.886, 0b_00011_0, Forcing.STRUM),
    Chord(2.057, 0b_00011_0, Forcing.STRUM),
    Chord(2.229, 0b_00011_0, Forcing.STRUM),
    Chord(2.400, 0b_00011_0, Forcing.STRUM),
    Chord(2.571, 0b_00010_0, Forcing.STRUM),

    # 3.1
    Chord(2.743, 0b_01100_0, Forcing.STRUM),
    Chord(2.914, 0b_01100_0, Forcing.STRUM),
    Chord(3.086, 0b_10100_0, Forcing.STRUM),
    Chord(3.257, 0b_10100_0, Forcing.STRUM),
    Chord(3.429, 0b_00110_0, Forcing.STRUM),
    Chord(3.600, 0b_00110_0, Forcing.STRUM),
    Chord(3.771, 0b_01010_0, Forcing.STRUM),
    Chord(3.943, 0b_01010_0, Forcing.STRUM),

    # 4.1
    Chord(4.114, 0b_00011_0, Forcing.STRUM),
    Chord(4.286, 0b_00011_0, Forcing.STRUM),
    Chord(4.457, 0b_00011_0, Forcing.STRUM),
    Chord(4.629, 0b_00011_0, Forcing.STRUM),
    Chord(4.800, 0b_00011_0, Forcing.STRUM),
    Chord(4.971, 0b_00011_0, Forcing.STRUM),
    Chord(5.143, 0b_00011_0, Forcing.STRUM),
    Chord(5.314, 0b_00010_0, Forcing.STRUM),

    # 5.1
    Chord(5.486, 0b_01100_0, Forcing.STRUM),
    Chord(5.657, 0b_01100_0, Forcing.STRUM),
    Chord(5.829, 0b_10100_0, Forcing.STRUM),
    Chord(6.000, 0b_10100_0, Forcing.STRUM),
    Chord(6.171, 0b_00110_0, Forcing.STRUM),
    Chord(6.343, 0b_00110_0, Forcing.STRUM),
    Chord(6.514, 0b_01010_0, Forcing.STRUM),
    Chord(6.686, 0b_01010_0, Forcing.STRUM),

    # 6.1
    Chord(6.857, 0b_00011_0, Forcing.STRUM),
    Chord(7.029, 0b_00011_0, Forcing.STRUM),
    Chord(7.200, 0b_00011_0, Forcing.STRUM),
    Chord(7.371, 0b_00011_0, Forcing.STRUM),
    Chord(7.543, 0b_00011_0, Forcing.STRUM),
    Chord(7.714, 0b_00011_0, Forcing.STRUM),
    Chord(7.886, 0b_00011_0, Forcing.STRUM),
    Chord(8.057, 0b_00011_0, Forcing.STRUM),

    # 7.1
    Chord(8.229, 0b_01100_0, Forcing.STRUM),
    Chord(8.400, 0b_01100_0, Forcing.STRUM),
    Chord(8.571, 0b_01100_0, Forcing.STRUM),
    Chord(8.743, 0b_01100_0, Forcing.STRUM),
    Chord(8.914, 0b_01010_0, Forcing.STRUM),
    Chord(9.086, 0b_01010_0, Forcing.STRUM),
    Chord(9.257, 0b_01010_0, Forcing.STRUM),
    Chord(9.429, 0b_01010_0, Forcing.STRUM),

    # 8.1
    Chord(9.600, 0b_00011_0, Forcing.STRUM),
    Chord(9.771, 0b_00011_0, Forcing.STRUM),
    Chord(9.943, 0b_00011_0, Forcing.STRUM),
    Chord(10.114, 0b_00011_0, Forcing.STRUM),
    Chord(10.286, 0b_00011_0, Forcing.STRUM),
    Chord(10.457, 0b_00011_0, Forcing.STRUM),
    Chord(10.629, 0b_00011_0, Forcing.STRUM),
    Chord(10.800, 0b_00011_0, Forcing.STRUM),

    # 9.1
    Chord(10.971, 0b_01100_0, Forcing.STRUM),
    Chord(11.143, 0b_01100_0, Forcing.STRUM),
    Chord(11.314, 0b_01100_0, Forcing.STRUM),
    Chord(11.486, 0b_01100_0, Forcing.STRUM),
    Chord(11.657, 0b_01010_0, Forcing.STRUM),
    Chord(11.829, 0b_01010_0, Forcing.STRUM),
    Chord(12.000, 0b_01010_0, Forcing.STRUM),
    Chord(12.171, 0b_01010_0, Forcing.STRUM),

    # 10.1
    Chord(12.343, 0b_00011_0, Forcing.STRUM),
    Chord(12.514, 0b_00011_0, Forcing.STRUM),
    Chord(12.686, 0b_00011_0, Forcing.STRUM),
    Chord(12.857, 0b_00011_0, Forcing.STRUM),
    Chord(13.029, 0b_00011_0, Forcing.STRUM),
    Chord(13.200, 0b_00011_0, Forcing.STRUM),
    Chord(13.371, 0b_00011_0, Forcing.STRUM),
    Chord(13.543, 0b_00011_0, Forcing.STRUM),
])


# Soulless 4, Machinations A - 1.1.000 to 4.4.240
MACHINATIONS_A = Chart('Machinations A', Diff.EXPERT, [
    # 1.1
    Chord(0.000, 0b_01000_0, Forcing.STRUM),
    Chord(0.120, 0b_00100_0, Forcing.STRUM),
    Chord(0.240, 0b_00100_0, Forcing.STRUM),
    Chord(0.360, 0b_01000_0, Forcing.STRUM),

    # 1.2
    Chord(0.480, 0b_00100_0, Forcing.STRUM),
    Chord(0.600, 0b_00100_0, Forcing.STRUM),
    Chord(0.720, 0b_01000_0, Forcing.STRUM),
    Chord(0.840, 0b_00100_0, Forcing.STRUM),

    # 1.3
    Chord(0.960, 0b_01000_0, Forcing.STRUM),
    Chord(1.080, 0b_00100_0, Forcing.STRUM),
    Chord(1.200, 0b_00100_0, Forcing.STRUM),
    Chord(1.320, 0b_01000_0, Forcing.STRUM),

    # 1.4
    Chord(1.440, 0b_00100_0, Forcing.STRUM),
    Chord(1.560, 0b_00100_0, Forcing.STRUM),
    Chord(1.680, 0b_10000_0, Forcing.STRUM),
    Chord(1.800, 0b_10000_0, Forcing.STRUM),

    # 2.1
    Chord(1.920, 0b_01000_0, Forcing.STRUM),
    Chord(2.040, 0b_00100_0, Forcing.STRUM),
    Chord(2.160, 0b_00100_0, Forcing.STRUM),
    Chord(2.280, 0b_01000_0, Forcing.STRUM),

    # 2.2
    Chord(2.400, 0b_00100_0, Forcing.STRUM),
    Chord(2.520, 0b_00100_0, Forcing.STRUM),
    Chord(2.640, 0b_01000_0, Forcing.STRUM),
    Chord(2.760, 0b_00100_0, Forcing.STRUM),

    # 2.3
    Chord(2.880, 0b_10000_0, Forcing.HOPO),
    Chord(2.910, 0b_10000_0, Forcing.STRUM),
    Chord(2.940, 0b_00001_0, Forcing.HOPO),
    Chord(2.970, 0b_00001_0, Forcing.STRUM),
    Chord(3.000, 0b_01000_0, Forcing.HOPO),
    Chord(3.030, 0b_01000_0, Forcing.STRUM),
    Chord(3.060, 0b_00001_0, Forcing.HOPO),
    Chord(3.090, 0b_00001_0, Forcing.STRUM),
    Chord(3.120, 0b_00100_0, Forcing.HOPO),
    Chord(3.150, 0b_00100_0, Forcing.STRUM),
    Chord(3.180, 0b_00001_0, Forcing.HOPO),
    Chord(3.210, 0b_00001_0, Forcing.STRUM),
    Chord(3.240, 0b_00010_0, Forcing.HOPO),
    Chord(3.270, 0b_00010_0, Forcing.STRUM),
    Chord(3.300, 0b_00001_0, Forcing.HOPO),
    Chord(3.330, 0b_00001_0, Forcing.STRUM),

    # 2.4
    Chord(3.360, 0b_10000_0, Forcing.HOPO),
    Chord(3.390, 0b_10000_0, Forcing.STRUM),
    Chord(3.420, 0b_00001_0, Forcing.HOPO),
    Chord(3.450, 0b_00001_0, Forcing.STRUM),
    Chord(3.480, 0b_01000_0, Forcing.HOPO),
    Chord(3.510, 0b_01000_0, Forcing.STRUM),
    Chord(3.540, 0b_00001_0, Forcing.HOPO),
    Chord(3.570, 0b_00001_0, Forcing.STRUM),
    Chord(3.600, 0b_00100_0, Forcing.HOPO),
    Chord(3.630, 0b_00100_0, Forcing.STRUM),
    Chord(3.660, 0b_00001_0, Forcing.HOPO),
    Chord(3.690, 0b_00001_0, Forcing.STRUM),
    Chord(3.720, 0b_00010_0, Forcing.HOPO),
    Chord(3.750, 0b_00010_0, Forcing.STRUM),
    Chord(3.780, 0b_00001_0, Forcing.HOPO),
    Chord(3.810, 0b_00001_0, Forcing.STRUM),

    # 3.1
    Chord(3.840, 0b_00100_0, Forcing.STRUM),
    Chord(3.960, 0b_00010_0, Forcing.STRUM),
    Chord(4.080, 0b_00010_0, Forcing.STRUM),
    Chord(4.200, 0b_00100_0, Forcing.STRUM),

    # 3.2
    Chord(4.320, 0b_00010_0, Forcing.STRUM),
    Chord(4.440, 0b_00010_0, Forcing.STRUM),
    Chord(4.560, 0b_00100_0, Forcing.STRUM),
    Chord(4.680, 0b_00010_0, Forcing.STRUM),

    # 3.3
    Chord(4.800, 0b_00100_0, Forcing.STRUM),
    Chord(4.920, 0b_00010_0, Forcing.STRUM),
    Chord(5.040, 0b_00010_0, Forcing.STRUM),
    Chord(5.160, 0b_00100_0, Forcing.STRUM),

    # 3.4
    Chord(5.280, 0b_00010_0, Forcing.STRUM),
    Chord(5.400, 0b_00010_0, Forcing.STRUM),
    Chord(5.520, 0b_01000_0, Forcing.STRUM),
    Chord(5.640, 0b_01000_0, Forcing.STRUM),

    # 4.1
    Chord(5.760, 0b_00100_0, Forcing.STRUM),
    Chord(5.880, 0b_00010_0, Forcing.STRUM),
    Chord(6.000, 0b_00010_0, Forcing.STRUM),
    Chord(6.120, 0b_00100_0, Forcing.STRUM),

    # 4.2
    Chord(6.240, 0b_00100_0, Forcing.STRUM),
    Chord(6.360, 0b_00010_0, Forcing.STRUM),
    Chord(6.480, 0b_00100_0, Forcing.STRUM),
    Chord(6.600, 0b_00010_0, Forcing.STRUM),

    # 4.3
    Chord(6.720, 0b_10000_0, Forcing.TAP),
    Chord(6.780, 0b_00001_0, Forcing.TAP),
    Chord(6.840, 0b_01000_0, Forcing.TAP),
    Chord(6.900, 0b_00001_0, Forcing.TAP),
    Chord(6.960, 0b_00100_0, Forcing.TAP),
    Chord(7.020, 0b_00001_0, Forcing.TAP),
    Chord(7.080, 0b_00010_0, Forcing.TAP),
    Chord(7.140, 0b_00001_0, Forcing.TAP),

    # 4.4
    Chord(7.200, 0b_10000_0, Forcing.TAP),
    Chord(7.260, 0b_00001_0, Forcing.TAP),
    Chord(7.320, 0b_01000_0, Forcing.TAP),
    Chord(7.380, 0b_00001_0, Forcing.TAP),
])


# Through the Fire and Flames, They're hammer ons - 13.1.000 to 17.1.000
THEYRE_HAMMER_ONS = Chart('They\'re hammer ons', Diff.EXPERT, [
    # 13.1
    Chord(0.000, 0b_00010_0, Forcing.HOPO),
    Chord(0.075, 0b_00001_0, Forcing.HOPO),
    Chord(0.150, 0b_00100_0, Forcing.HOPO),
    Chord(0.225, 0b_00001_0, Forcing.HOPO),
    Chord(0.300, 0b_01000_0, Forcing.HOPO),
    Chord(0.375, 0b_00001_0, Forcing.HOPO),
    Chord(0.450, 0b_00010_0, Forcing.HOPO),
    Chord(0.525, 0b_00001_0, Forcing.HOPO),
    Chord(0.600, 0b_00100_0, Forcing.HOPO),
    Chord(0.675, 0b_00001_0, Forcing.HOPO),
    Chord(0.750, 0b_01000_0, Forcing.HOPO),
    Chord(0.825, 0b_00001_0, Forcing.HOPO),
    Chord(0.900, 0b_10000_0, Forcing.HOPO),
    Chord(0.975, 0b_00001_0, Forcing.HOPO),
    Chord(1.050, 0b_01000_0, Forcing.HOPO),
    Chord(1.125, 0b_00001_0, Forcing.HOPO),

    # 14.1
    Chord(1.200, 0b_10000_0, Forcing.HOPO),
    Chord(1.275, 0b_00001_0, Forcing.HOPO),
    Chord(1.350, 0b_00100_0, Forcing.HOPO),
    Chord(1.425, 0b_00001_0, Forcing.HOPO),
    Chord(1.500, 0b_01000_0, Forcing.HOPO),
    Chord(1.575, 0b_00001_0, Forcing.HOPO),
    Chord(1.650, 0b_00010_0, Forcing.HOPO),
    Chord(1.725, 0b_00001_0, Forcing.HOPO),
    Chord(1.800, 0b_10000_0, Forcing.HOPO),
    Chord(1.875, 0b_00001_0, Forcing.HOPO),
    Chord(1.950, 0b_00100_0, Forcing.HOPO),
    Chord(2.025, 0b_00001_0, Forcing.HOPO),
    Chord(2.100, 0b_01000_0, Forcing.HOPO),
    Chord(2.175, 0b_00001_0, Forcing.HOPO),
    Chord(2.250, 0b_00100_0, Forcing.HOPO),
    Chord(2.325, 0b_00001_0, Forcing.HOPO),

    # 15.1
    Chord(2.400, 0b_00010_0, Forcing.HOPO),
    Chord(2.475, 0b_00001_0, Forcing.HOPO),
    Chord(2.550, 0b_00100_0, Forcing.HOPO),
    Chord(2.625, 0b_00001_0, Forcing.HOPO),
    Chord(2.700, 0b_01000_0, Forcing.HOPO),
    Chord(2.775, 0b_00001_0, Forcing.HOPO),
    Chord(2.850, 0b_00010_0, Forcing.HOPO),
    Chord(2.925, 0b_00001_0, Forcing.HOPO),
    Chord(3.000, 0b_00100_0, Forcing.HOPO),
    Chord(3.075, 0b_00001_0, Forcing.HOPO),
    Chord(3.150, 0b_01000_0, Forcing.HOPO),
    Chord(3.225, 0b_00001_0, Forcing.HOPO),
    Chord(3.300, 0b_10000_0, Forcing.HOPO),
    Chord(3.375, 0b_00001_0, Forcing.HOPO),
    Chord(3.450, 0b_01000_0, Forcing.HOPO),
    Chord(3.525, 0b_00001_0, Forcing.HOPO),

    # 16.1
    Chord(3.600, 0b_10000_0, Forcing.HOPO),
    Chord(3.675, 0b_01000_0, Forcing.HOPO),
    Chord(3.750, 0b_00100_0, Forcing.HOPO),
    Chord(3.825, 0b_00010_0, Forcing.HOPO),
    Chord(3.900, 0b_00001_0, Forcing.HOPO),
    Chord(3.975, 0b_00001_0, Forcing.STRUM),
    Chord(4.050, 0b_00010_0, Forcing.HOPO),
    Chord(4.125, 0b_00100_0, Forcing.HOPO),
    Chord(4.200, 0b_01000_0, Forcing.HOPO),
    Chord(4.275, 0b_10000_0, Forcing.HOPO),
    Chord(4.350, 0b_10000_0, Forcing.STRUM),
    Chord(4.425, 0b_01000_0, Forcing.HOPO),
    Chord(4.500, 0b_00100_0, Forcing.HOPO),
    Chord(4.575, 0b_00010_0, Forcing.HOPO),
    Chord(4.650, 0b_00001_0, Forcing.HOPO),
    Chord(4.725, 0b_00010_0, Forcing.HOPO),
])
