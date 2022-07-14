from termcolor import colored

# ! Berechnung von fibonacci Zahlen

user_eingabe = int(input(
    '\n bis zu welcher Zahl sollen die Fibonacci-Folge laufen? \n'))

erste_Zahl = 0
zweite_Zahl = 1
iterator = -1
fibo_Nr = []

while erste_Zahl < user_eingabe:

    print(colored('\nerste_Zahl ist = {}\n'.format(
        erste_Zahl), 'blue', 'on_yellow'))

    print(colored('\nzweite_Zahl ist =  {}\n'.format(
        zweite_Zahl), 'blue', 'on_red'))

    # ! soll hier nach einem Durchlauf reingehen, sonst gibt es einen IndexError: list index out of range
    if erste_Zahl > 0:
        if fibo_Nr[iterator] == user_eingabe or fibo_Nr[iterator] > user_eingabe:
            # ! wenn die user-Eingabe auch eine Fibonacci Zahl ist
            if fibo_Nr[iterator] == user_eingabe:
                print(colored('\n Ergebnis = {}\n'.format(
                    fibo_Nr), 'red', 'on_blue'))
                break
            else:
                # ! entfernt die letzte Zahl aus der Liste, da user Eingabe kleiner ist
                fibo_Nr.pop(iterator)
                print(colored('\n Ergebnis = {}\n'.format(
                    fibo_Nr), 'red', 'on_blue'))
                break

    iterator += 1

    print(colored('\niterator ist gleich {}\n'.format(
        iterator), 'red', 'on_green'))

    fibo_Nr.insert(iterator, erste_Zahl + zweite_Zahl)

    print(colored('\ndas sind Ihre fibonacci Zahlen = {}\n'.format(
        fibo_Nr), 'green', 'on_blue'))

    erste_Zahl = zweite_Zahl

    zweite_Zahl = fibo_Nr[iterator]
