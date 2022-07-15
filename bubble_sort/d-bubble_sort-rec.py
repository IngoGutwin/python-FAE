from termcolor import colored
import math

# * Ein bubble Algorithmus mit Farbe
# * grün + geld = ein index_fw
# * rot = ein index_fw


def bubble_Sort(arr):

    random_numbers = arr
    index_fw = 0
    end = math.trunc(len(random_numbers) / 2) + 1
    print(end)
    index_bw = len(random_numbers) - 1

    operations = 0
    iterations = 0

    def seek_and_destroy():
        nonlocal index_fw
        nonlocal index_bw
        nonlocal end
        nonlocal operations
        nonlocal iterations
        # * wenn index_fw gleich ende ist, dann wurde  ein Druchlauf vollendet
        print('index forward', index_fw)
        print('index backward', index_bw)
        # if index_fw <= end:
        if index_fw < end:
            # * vergleiche die laufenden Zahlen, wenn laufende Zahl > als die nächste ist
            iterations += 1
            # ? [15, 4, 9, 8, 13, 11, 0]
            # ! wenn vom Anfang oder vom Ende des Array Zahlen getauscht werden können
            if random_numbers[index_fw] > random_numbers[index_fw + 1] or random_numbers[index_bw] < random_numbers[index_bw-1]:

                # ! wenn vom start getauscht werden kann
                if random_numbers[index_fw] > random_numbers[index_fw + 1]:
                    # * tausche die Zahlen
                    temp_Var = random_numbers[index_fw+1]
                    random_numbers[index_fw+1] = random_numbers[index_fw]
                    random_numbers[index_fw] = temp_Var

                    # ! wenn vom start gatauscht wurde, prüfe ob das ende auch getauscht werden kann
                    if random_numbers[index_bw] < random_numbers[index_bw-1]:
                        # ! damit dieser print nicht doppelt ausgeführt word
                        print(colored('\n Zahlen getauscht vom Start \n {}'.format(
                            random_numbers), 'cyan', 'on_yellow'))
                        temp_Var_bw = random_numbers[index_bw-1]
                        random_numbers[index_bw-1] = random_numbers[index_bw]
                        random_numbers[index_bw] = temp_Var_bw
                        print(colored('\n Zahlen getauscht vom Ende \n {}'.format(
                            random_numbers), 'yellow', 'on_magenta'))
                        index_fw += 1
                        index_bw -= 1
                        operations += 1
                        print('return getauscht')
                        return seek_and_destroy()

                    # ! aktualisiere Werte wenn nur von Anfang getauscht wurde
                    print(colored('\n Zahlen getauscht vom Start \n {}'.format(
                        random_numbers), 'cyan', 'on_yellow'))
                    index_fw += 1
                    index_bw -= 1
                    operations += 1
                    print('return getauscht')
                    return seek_and_destroy()

                # ! sortiere vom Ende, da vom Start keine Sortierung möglich ist
                # * vergleiche vom Ende des Arrays und Sortiere
                else:
                    temp_Var_bw = random_numbers[index_bw-1]
                    random_numbers[index_bw-1] = random_numbers[index_bw]
                    random_numbers[index_bw] = temp_Var_bw
                    print(colored('\n Zahlen getauscht vom Ende \n {}'.format(
                        random_numbers), 'yellow', 'on_magenta'))
                    index_fw += 1
                    index_bw -= 1
                    operations += 1
                    print('return getauscht')
                    return seek_and_destroy()

            # * ansonsten erhöhe den index_fw um 1, und such weiter
            else:
                index_fw += 1
                index_bw -= 1
                print('return nicht getauscht')
                return seek_and_destroy()

        else:
            iterations += 1
            # * solange ende größer 1 ist, soll die Suche weiter laufen
            if end > 1:
                print('end ', end)
                end = end - 1
                index_fw = 0
                index_bw = len(random_numbers) - 1
                print('return index == ende')
                return seek_and_destroy()
            # * ansonsten wurden alle Positionen im Array durchsucht, beende die Suche
            else:
                return ' \n Array wurde sortiert ... \n {} \n\n es wurden {} Operationen benötigt \n und {} Durchläufe '.format(random_numbers, operations, iterations)

    return seek_and_destroy()


""" random_array = [15, 1, 4, 9, 8, 13, 3023, 11, 0, 3, 2, 345,
                45, 21, 9, 4, 6, 23, 7, 5, 6, 3, 52, 2, 2, 3, 1, 8, 20, 31] """
# random_array = [15, 1, 4, 9, 8, 13, 3023, 11, 0, 3, 2, 345, 45, 21] # gerade
# random_array = [15, 1, 4, 9, 8, 13, 3023,
#                11, 0, 3, 2, 345, 45, 21, 22]  # ungerade

random_array = [15, 4, 9, 8, 13, 11, 0]
# random_array = [4, 8, 13, 11, 0]

sorted_array = bubble_Sort(random_array)

print(sorted_array)
