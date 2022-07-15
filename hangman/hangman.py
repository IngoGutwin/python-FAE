

# * definiere die Variablen
anzahl_Versuche = 7         # * Anzahl der Wortversuche
wort_laenge = 0             # * speichern der Wortlänge beim Hochzählen
# * greift das Suchwort bei user Eingabe ab, und speichert es
suchwort = input('\n gebe das Wort ein, das erraten werden soll ! \n')
vergleichs_Wort = ''  # * eine Kopie des Wortes für Wahrheitsabfragen
galgen_Man = True  # *  solange hier True ist, läuft das Spiel
hangman = ''  # * speichert die Hangman Darstellung
geratener_Buchstabe = ''  # * speichert den geratenen Buchstaben
erratenes_Wort = ''  # * speichert und aktualisiert das erratene Wort
erratene_Buchstaben = 0  # * zählt die erratenen Buchstaben
i = 0  # * der Iterator für die das Verschlüsseln des Wortes

while galgen_Man == True:
    # * sobald das suchwort verschlüsselt worden ist, und die länge des Wortes festgelegt worden ist
    # * dann gehe hier rein
    if vergleichs_Wort == suchwort:
        print('das zu erratende Wort: ' + erratenes_Wort)
        geratener_Buchstabe = input(
            '\n OK, dann versuche Mal das Wort zu erraten ! \n gebe den Buchstaben ein den du erraten möchtest ! \n\n')
        if geratener_Buchstabe in suchwort:
            j = 0
            while wort_laenge > j:
                if(wort_laenge == j):
                    break
                elif(geratener_Buchstabe == suchwort[j] and geratener_Buchstabe != erratenes_Wort[j]):
                    erratenes_Wort = (
                        erratenes_Wort[0:j] + geratener_Buchstabe + erratenes_Wort[j+1:wort_laenge])
                    erratene_Buchstaben += 1
                    if(erratene_Buchstaben == wort_laenge):
                        print(
                            '\n \n super du hast alle Buchstaben erraten \n das gesuchte Wort ist ' + erratenes_Wort + ' \n---- GAME - OVER -----\n')
                        galgen_Man = False
                        break
                    break
                j += 1
        elif geratener_Buchstabe not in suchwort:
            if(anzahl_Versuche == 0):
                galgen_Man == False
                print(
                    '\n ----- GAME OVER --------\n deine Versuche sind leider Aufgebraucht')
                break

            if(anzahl_Versuche == 7):
                hangman = '---------------'
                print(
                    '\n\n\n Hey, Vorsicht!\n  dein Galgen kommt näher ! \n Du hast nur noch IIIIII Versuche\n\n\n' + hangman + '\n\n\n ')
            elif(anzahl_Versuche == 6):
                hangman = '       |     \n       |     \n       |     \n       |     \n       |     \n       |     \n       |     \n       |     \n       |     \n       |     \n       |     \n' + \
                    hangman[0:]
                print(
                    '\n\n\n Und noch ein Versuch weniger!\n  dafür ein Schritt näher zum Galgen, Gratuliere!  \n Du hast nur noch IIIII Versuche \n\n\n' + hangman + '\n\n\n ')
            elif(anzahl_Versuche == 5):
                hangman = '        ________________\n' + hangman[0:]
                print(
                    '\n\n\n Ohne Worte! \n soviel Pech kann Man nicht haben \n Du hast noch IIII Versuche \n\n\n' + hangman + '\n\n\n ')
            elif(anzahl_Versuche == 4):
                hangman = hangman[0:-162] + '|                |\n       |                |    \n       |                |     \n       |     \n       |     \n       |     \n       |     \n       |     \n       |     \n       |     \n       |     ' + hangman[173:-1]
                print(
                    '\n\n\n Du stehst wohl auf Adrenalin, was? \n oder du kannst lange die Luft anhalten ! \n Du hast noch III \n\n\n' + hangman + '\n\n\n ')
            elif(anzahl_Versuche == 3):
                hangman = hangman[0:-133] + \
                    '\n       |                O' + hangman[106:-1]
                print(
                    '\n\n\n Hey, Vorsicht!\n  dein Galgen kommt näher !\n Du hast noch II \n\n\n' + hangman + '\n\n\n ')
            elif(anzahl_Versuche == 2):
                hangman = hangman[0:-133] + \
                    '\n       |               /|\\' + hangman[136:-1]
                print(
                    '\n\n\n Hey, Vorsicht!\n  dein Galgen kommt näher !\n Du hast noch I \n\n\n' + hangman + '\n\n\n ')
            elif(anzahl_Versuche == 1):
                hangman = hangman[0:-133] + \
                    '\n       |               / \\' + hangman[166:-1]
                print(
                    '\n\n\n Das wars !\n  guten Flug !\n Jetzt hilft nur noch Luft anhalten! \n\n\n' + hangman + '\n\n\n ')
            anzahl_Versuche -= 1
    # * hier wird die länge des Suchwortes bestimmt und das Verschlüsseln des Wortes vorgenommen
    elif vergleichs_Wort != suchwort:
        vergleichs_Wort += suchwort[i]
        erratenes_Wort += '-'
        wort_laenge += 1
        i += 1
