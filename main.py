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

    charts = []

    custom_E = Chart('Custom Easy', Diff.EASY, [])
    custom_M = Chart('Custom Medium', Diff.MEDIUM, [])
    custom_H = Chart('Custom Hard', Diff.HARD, [])
    custom_X = Chart('Custom Expert', Diff.EXPERT, [])
    filename = input('Enter directory path to chart:\n')
    custom_E.read_chart(filename)
    custom_M.read_chart(filename)
    custom_H.read_chart(filename)
    custom_X.read_chart(filename)
    charts.append(custom_E)
    charts.append(custom_M)
    charts.append(custom_H)
    charts.append(custom_X)

    calculate_all_chart_stats(charts)


if __name__=="__main__":
    main()
