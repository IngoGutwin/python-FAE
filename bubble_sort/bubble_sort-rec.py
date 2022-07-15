from termcolor import colored

# * Ein bubble Algorithmus mit Farbe
# * grün + geld = ein index
# * rot = ein index


def bubble_Sort(arr):

    random_numbers = arr
    index = 0
    end = len(random_numbers) - 1
    sort_operations = 0

    def seek_and_destroy():
        nonlocal index
        nonlocal end
        nonlocal sort_operations
        # * wenn index gleich ende ist, dann wurde  ein Druchlauf vollendet
        if index != end:
            # * vergleiche die laufenden Zahlen, wenn laufende Zahl > als die nächste ist
            if random_numbers[index] < random_numbers[index + 1]:
                print(colored('\n Zahl {} Index {} \n < \n Zahl {} mit Index {}\n'.format(
                    random_numbers[index], index, random_numbers[index+1], index + 1), 'cyan', 'on_green'))
                # * tausche die Zahlen
                temp_Var = random_numbers[index+1]
                random_numbers[index+1] = random_numbers[index]
                random_numbers[index] = temp_Var
                # * zeige was im Array passiert ist
                print(colored('\n Zahlen getauscht \n {}'.format(
                      random_numbers), 'cyan', 'on_yellow'))
                # * erhöhe index und suche weiter
                index += 1
                sort_operations += 1
                return seek_and_destroy()
            # * ansonsten erhöhe den index um 1, und such weiter
            else:
                print(colored('\n index {} Zahl {}  \n index {} Zahl {} Vergleich < \n index wird um 1 erhöht \n'.format(
                    index, random_numbers[index], index + 1,  random_numbers[index + 1]), 'white', 'on_red'))
                index += 1
                return seek_and_destroy()
        else:
            # * solange ende größer 1 ist, soll die Suche weiter laufen
            if end > 1:
                end = end - 1
                index = 0
                print(colored('\n ein Druchlauf wurde beendet \n index wird auf {} gesetzt \n Ende wird um 1 reduziert und ist jetzt {}\n'.format(
                    index, end), 'white', 'on_blue'))
                return seek_and_destroy()
            # * ansonsten wurden alle Positionen im Array durchsucht, beende die Suche
            else:
                return ' \n Array wurde sortiert ... \n {} \n es wurden {} Operatoinen benötigt'.format(random_numbers, sort_operations)

    return seek_and_destroy()


random_array = [9, 4, 6, 23, 7, 5, 6, 3, 52, 2, 2, 3, 1, 8, 20, 31]

sorted_array = bubble_Sort(random_array)

print(sorted_array)

# ! > 55 Operationen
# ! < 62 Operationen
