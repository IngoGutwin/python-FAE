
# ! importiere die Module
from tkinter import *
import math
# * deklariere die Variablen
garage = []
fahrzeugeDrin = 0


def sucheEbene(parkNr):
    # * prüft anahnd von der Parknummer auf welcher Ebene sich das Fahrzeug befindet
    global parkplaetzeProEtage
    global etagen
    ebene = 0
    while ebene <= etagen:
        if(parkNr < (parkplaetzeProEtage * ebene)):
            return ebene
        ebene += 1


def ausgabeReset(string):
    # * resetet das Ausgabefeld, macht es beschreibbar, fügt einen neuen Wert ein, macht die Textbox schreibgeschützt
    ausgabe.configure(state='normal')
    ausgabe.delete('1.0', 'end')
    ausgabe.insert(END, string)
    ausgabe.configure(state='disabled')
    return 'OK'


def entferneFahrzeug(kennzeichen):
    # * aktualisiert die Parkplatzdatenbank
    # ? überlege nochmal ob diese Methode richtig funktioniert
    global garage
    global fahrzeugeDrin
    garage.append(garage.index(kennzeichen))
    garage.remove(kennzeichen)
    fahrzeugeDrin -= 1
    return ausgabeReset('\n Auf wiedersehen Nr {} ... \n bis zum nächsten Parken \n'.format(kennzeichen))


def fahrzeugHinzufuegen(kennzeichen):
    # * sucht eine freie Parknummer in der Garage, sucht dann die Ebene auf der sich die gefundene ParkNr befindet, aktualisiert den Fahrzeugstand
    global fahrzeugeDrin
    ebene = 0
    for parkNr in garage:
        if(isinstance(parkNr, int)):
            garage[parkNr] = kennzeichen
            ebene = sucheEbene(parkNr)
            fahrzeugeDrin += 1
            return ausgabeReset('fahren Sie bitte auf Ebene: {}, Ihre Parknummer ist: {}'.format(ebene, parkNr))


def entscheidenUndAusfuehren(kennZeichen, suchWert):
    # * sucht das Kennzeichen in der Datenbank und führt die je nach Aufruf die entsprechnede Funktion aus
    if kennZeichen != 'Kennzeichen eingeben' and kennZeichen != '':
        if kennZeichen in garage and suchWert == 'S':
            indexKennZeichen = garage.index(kennZeichen)
            aufEbene = sucheEbene(indexKennZeichen)
            return ausgabeReset('Das Fahrzeug mit dem Kennzeichen: {} steht auf Ebene: {}, ParkNr: {}'.format(kennZeichen, aufEbene, indexKennZeichen))
        elif kennZeichen not in garage and suchWert == 'S':
            return ausgabeReset('Sorry, das gesuchte Kennzeichen {}, ist nicht in der Garage!'.format(kennZeichen))
        elif kennZeichen in garage and suchWert == 'P':
            return ausgabeReset('Entschuldigung, mit dem Kennzeichen {} ist etwas nicht in Ordnung.\n Wir haben freundlicherweise für Sie die Polizei verständigt,\n diese sollte jeden Moment eintreffen.\n Machen Sie bitte solange die Einfahr frei!\n Danke, bis zum nächsten Parken :)'.format(kennZeichen))
        elif kennZeichen not in garage and suchWert == 'P':
            if(fahrzeugeDrin == anzahlParkplaetze):
                return ausgabeReset('Sorry, unser Parkhaus ist leider voll\n ')
            elif(fahrzeugeDrin < anzahlParkplaetze):
                return fahrzeugHinzufuegen(kennZeichen)
        elif kennZeichen in garage and suchWert == 'R':
            return entferneFahrzeug(kennZeichen)
    elif kennZeichen == 'Kennzeichen eingeben' or kennZeichen == '':
        return ausgabeReset('gebe bitte ein gültiges Kennzeichen in das Kennzeichen-Feld ein !')


def erstelleGarage():
    # * prüft ob die Garagen-Datenbank bereits erstellt worden ist
    # * wenn nicht, dann greift die Etagen und Parkplätze ab, erstellt daraus das Array mit Parkplätzen
    # * wenn doch, gibt nur das bereits erstellte Array aus
    if(garage == []):
        global etagen
        global parkplaetzeProEtage
        global anzahlParkplaetze
        anzahlParkplaetze = int(anzahlParkplaetze.get())
        etagen = int(etagen.get())
        parkplaetzeProEtage = math.trunc(
            anzahlParkplaetze/etagen)
        for parkPlatz in range(anzahlParkplaetze):
            garage.append(parkPlatz)

        print('die erstellte Garage:\n {}'.format(garage))
        return ausgabeReset('Die Garage wurde erstellt:\n {}'.format(garage))
    elif(garage != []):
        return ausgabeReset('aktuelle Lage in der Garage:\n {}'.format(garage))


# * start der Anwendung
root = Tk()  # * pH steht für parkHaus, hier beginnt die Anwendung
root.title("Parkhaus-Anlage")
root.configure(bg='#B0B0B0')


# * das Ausgabe-Fenster
ausgabe = Text(root, width=80, height=10,
               bg='#FFFFFF', padx=5, pady=5, border=5)
ausgabe.grid(row=1, column=0, columnspan=3)
scroll = Scrollbar(ausgabe)
ausgabe.configure(state='disabled')


# * Eingabe-Feld für die Etagen
etagen = Entry(root, bg='#FFCD29')
etagen.grid(column=0, row=0, padx=20, pady=10)
etagen.insert(0, 'Etagen eingeben')
# * Eingabe-Feld für die Parkplätze
anzahlParkplaetze = Entry(root, bg='#FFCD29')
anzahlParkplaetze.grid(column=1, row=0, padx=20, pady=10)
anzahlParkplaetze.insert(0, 'Anzahl Parkplätze eing.')
# * Eingabe-Feld für den Parkplatz
kennZeichen = Entry(root, bg='#FFCD29')
kennZeichen.grid(column=1, row=5, padx=20, pady=10)
kennZeichen.insert(0, 'Kennzeichen eingeben')
# * Button für die Berechnung der Garage
btnBerechneGarage = Button(
    root, text="Garage\nErstellen\n oder \n Aktualisieren", width=10, padx=40, pady=20, bg='#14AE5C', command=erstelleGarage)
btnBerechneGarage.grid(column=2, row=0)
# * Button für die Funktion Parken
btnParken = Button(
    root, text="Parken", width=10, padx=40, pady=20, bg='#14AE5C', command=lambda: entscheidenUndAusfuehren(kennZeichen.get(), 'P'))
btnParken.grid(column=0, row=5)
# * Button für die Funktion Raus-Fahren
btnRausFahren = Button(
    root, text="Raus-Fahren", width=10, padx=40, pady=20, bg='#14AE5C', command=lambda: entscheidenUndAusfuehren(kennZeichen.get(), 'R'))
btnRausFahren.grid(column=0, row=6)
# * Button für die Funktion Suche-Kennzeichen
btnSucheKennzeichen = Button(
    root, text="Wo ist mein Auto?", width=10, padx=40, pady=20, bg='#14AE5C', command=lambda: entscheidenUndAusfuehren(kennZeichen.get(), 'S'))
btnSucheKennzeichen.grid(column=1, row=6)
# * Button für die Funktion freie Parkplätze
btnFreierParkp = Button(
    root, text="Freie Plätze?", width=10, padx=40, pady=20, bg='#14AE5C', command=lambda: ausgabeReset('Es sind noch {} Parkplätze frei!'.format(anzahlParkplaetze-fahrzeugeDrin)))
btnFreierParkp.grid(column=2, row=6)

if(garage == []):
    ausgabeReset('\n Hallo und willkommen in unserer Parkanlage !\n Erstelle zuerst die Datenbank, \n gebe dazu die Etagenanzahl sowie die Anzahl der Parkplätze ein \n und drücke den Garage Erstellen Button')


root.mainloop()
