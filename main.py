from core import *
from metadatareader import MetadataReader
from csv import DictWriter

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

    data = []
    
    for filename in glob(directory + '/**/notes.mid', recursive=True):

        filename_ini = filename[:-9] + 'song.ini'
        ini_reader = MetadataReader()
        ini_reader.read(filename_ini)
        song_info = ini_reader.get_info()

        if 'artist' in song_info.keys() and 'name' in song_info.keys():
            print(song_info['artist'] + ' - ' + song_info['name'])
        else:
            print(filename)
        
        charts = []

        for chart_label in chart_labels:
            chart_name = chart_names[chart_label]
            chart_diff = chart_diffs[chart_label]
            chart = Chart(chart_label, chart_diff, [])
            chart.read_chart(filename, chart_name)
            if len(chart.chords) > 0:
                charts.append(chart)

        song_info.update(calculate_all_chart_stats(charts))
        data.append(song_info)

    fieldnames = ['artist', 'name',
                    'Guitar Easy', 'Guitar Medium', 'Guitar Hard', 'Guitar Expert', 'diff_guitar',
                    'Bass Easy', 'Bass Medium', 'Bass Hard', 'Bass Expert', 'diff_bass',
                    'Rhythm Easy', 'Rhythm Medium', 'Rhythm Hard', 'Rhythm Expert', 'diff_rhythm']
    csv_data = []
    for song_info in data:
        csv_song_info = {}
        for attribute in fieldnames:
            if attribute in song_info.keys():
                csv_song_info[attribute] = song_info[attribute]
            else:
                csv_song_info[attribute] = "N/A"
        csv_data.append(csv_song_info)

    with open(directory + '/results.csv', 'w', newline='') as csvfile:
        writer = DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(csv_data)


if __name__=="__main__":
    main()
