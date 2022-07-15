

from termcolor import colored


zufalls_zahlen = [9, 4, 7, 5, 6, 8, 1, 3, 2]


sortiert = False


ende = len(zufalls_zahlen) - 1


zufalls_zahlen = [9, 4, 7, 5]


sortiert = False


ende = len(zufalls_zahlen) - 1


while sortiert == False:

    sortiert = True

    for i in range(0, ende):

        print(colored('\n\naktueller Durchlauf {}\naktuelle Reihenfolge {}\n'.format(

            i+1, zufalls_zahlen), 'red', 'on_yellow'))

        # ! prüfe ob die aktuelle Zahl größer ist

        if zufalls_zahlen[i] > zufalls_zahlen[i+1]:

            print(colored('\nindex {}={} ist größer als index{}={}\n'.format(

                i, zufalls_zahlen[i], i+1, zufalls_zahlen[i+1]), 'magenta', 'on_white'))

            tausch_Feld = zufalls_zahlen[i+1]

            zufalls_zahlen[i+1] = zufalls_zahlen[i]

            zufalls_zahlen[i] = tausch_Feld

            print(colored('\nschiebe {}, hinter {}\n {}'.format(

                zufalls_zahlen[i+1], zufalls_zahlen[i], zufalls_zahlen), 'yellow', 'on_blue'))

            sortiert = False

        # print('\n Zahl Sortiert\n')

    ende = ende - 1
    print('ende ', ende)
