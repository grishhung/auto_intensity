from core import *

from glob import glob

def main():
    
    directory = input('Enter directory path to charts:\n')

    for filename in glob(directory + '/**/notes.mid', recursive=True):
        
        print(filename)
        
        charts = []
        
        custom_guitar_E = Chart('Guitar Easy', Diff.EASY, [])
        custom_guitar_M = Chart('Guitar Medium', Diff.MEDIUM, [])
        custom_guitar_H = Chart('Guitar Hard', Diff.HARD, [])
        custom_guitar_X = Chart('Guitar Expert', Diff.EXPERT, [])
        custom_bass_E = Chart('Bass Easy', Diff.EASY, [])
        custom_bass_M = Chart('Bass Medium', Diff.MEDIUM, [])
        custom_bass_H = Chart('Bass Hard', Diff.HARD, [])
        custom_bass_X = Chart('Bass Expert', Diff.EXPERT, [])
        custom_guitar_E.read_chart(filename, 'PART GUITAR')
        custom_guitar_M.read_chart(filename, 'PART GUITAR')
        custom_guitar_H.read_chart(filename, 'PART GUITAR')
        custom_guitar_X.read_chart(filename, 'PART GUITAR')
        custom_bass_E.read_chart(filename, 'PART BASS')
        custom_bass_M.read_chart(filename, 'PART BASS')
        custom_bass_H.read_chart(filename, 'PART BASS')
        custom_bass_X.read_chart(filename, 'PART BASS')
        charts.append(custom_guitar_E)
        charts.append(custom_guitar_M)
        charts.append(custom_guitar_H)
        charts.append(custom_guitar_X)
        charts.append(custom_bass_E)
        charts.append(custom_bass_M)
        charts.append(custom_bass_H)
        charts.append(custom_bass_X)

        calculate_all_chart_stats(charts)


if __name__=="__main__":
    main()
