from core import *
from data import *


def main():
    charts = [
        INTRO_A_PUNK,
        MACHINATIONS_A,
        THEYRE_HAMMER_ONS,
        SANITY_SWING,
        SANITY_ANCHOR_YGYR,
        SANITY_ANCHOR_YGYG,
    ]

    calculate_all_chart_stats(charts)


if __name__=="__main__":
    main()
