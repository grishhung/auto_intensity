from core import *

from glob import glob

def main():
    
    directory = input('Enter directory path to charts:\n')

    chart_labels = ['Guitar Easy', 'Guitar Medium', 'Guitar Hard', 'Guitar Expert',
                    'Bass Easy', 'Bass Medium', 'Bass Hard', 'Bass Expert',
                    'Rhythm Easy', 'Rhythm Medium', 'Rhythm Hard', 'Rhythm Expert',]

    chart_names = {
        'Guitar Easy':      'PART GUITAR',
        'Guitar Medium':    'PART GUITAR',
        'Guitar Hard':      'PART GUITAR',
        'Guitar Expert':    'PART GUITAR',
        'Bass Easy':        'PART BASS',
        'Bass Medium':      'PART BASS',
        'Bass Hard':        'PART BASS',
        'Bass Expert':      'PART BASS',
        'Rhythm Easy':      'PART RHYTHM',
        'Rhythm Medium':    'PART RHYTHM',
        'Rhythm Hard':      'PART RHYTHM',
        'Rhythm Expert':    'PART RHYTHM'
    }

    chart_diffs = {
        'Guitar Easy':      Diff.EASY,
        'Guitar Medium':    Diff.MEDIUM,
        'Guitar Hard':      Diff.HARD,
        'Guitar Expert':    Diff.EXPERT,
        'Bass Easy':        Diff.EASY,
        'Bass Medium':      Diff.MEDIUM,
        'Bass Hard':        Diff.HARD,
        'Bass Expert':      Diff.EXPERT,
        'Rhythm Easy':      Diff.EASY,
        'Rhythm Medium':    Diff.MEDIUM,
        'Rhythm Hard':      Diff.HARD,
        'Rhythm Expert':    Diff.EXPERT
    }
    
    for filename in glob(directory + '/**/notes.mid', recursive=True):
        
        print(filename)
        
        charts = []

        for chart_label in chart_labels:
            chart_name = chart_names[chart_label]
            chart_diff = chart_diffs[chart_label]
            chart = Chart(chart_label, chart_diff, [])
            chart.read_chart(filename, chart_name)
            if len(chart.chords) > 0:
                charts.append(chart)

        calculate_all_chart_stats(charts)


if __name__=="__main__":
    main()
