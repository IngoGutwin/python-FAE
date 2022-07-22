import os

""" 
dieser Algorithmus durchläuft die Ordner Strucktur nach oben
von dem Ordner aus in dem die Datei plaziert wird
wenn der Ordner gefunden worden ist, wird eine neue Datei erstellt
und der angegebene Code wird eingefügt  
"""


def make_virus():
    your_virus = 'plaziere hier deinen beliebigen Inhalt'
    return your_virus


def place_virus():  # ? make and place file
    file = open('your_first_virus.py', 'w')
    the_virus = make_virus()
    file.write(the_virus)
    file.close()
    return print('... done \n file placed')


def check_listdir(dir):
    print('\n', os.getcwd())
    list_dir = os.listdir()
    print('\ninhalt aktueller Ordner\n', list_dir)
    try:
        print('\ntry\n')
        print(list_dir.index(dir))
        check_dir = list_dir.index(dir)
        return check_dir
    except:
        print('\n nichts gefunden \n')
        input('---------------------------------')
        return None


def searching_for_input(val):
    check_for_val = check_listdir(val)
    if check_for_val != None:
        os.chdir(val)
        print('\nZiel Ordner gefunden\n', os.getcwd())
        return place_virus()
    else:
        path = '../'
        os.chdir(path)
        searching_for_input(val)


searching_for_input('target_')
