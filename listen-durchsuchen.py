from termcolor import colored

colors = ['red', [2, 5], 'green', '']
nums = [134, 1, 2, 923]
cities = ['Bonn', 'Berlin', 'Koblenz', '']
random = ['Hase', 2, [True, 'Wolf', 'Köln', ['hunger', 1, 2, 3]]]

b = [[cities] + [colors] + [cities[1]] + [random] + nums + [cities[0]]]

print(colored('unsere Liste {}'.format(b), 'magenta', 'on_cyan'))

# ! erste Schleife
for i in b:
    print(colored('\nerste Schleife...\n i ist = {}\n'.format(i), 'blue', 'on_yellow'))

    # ! prüfe Bedingung für die zweite Schleife
    if isinstance(i, int) == False:
        for j in i:
            print(colored('\nzweite Schleife...\n j ist = {}\n'.format(
                j), 'red', 'on_green'))

            # ! prüfe Bedingung für die dritte Schleife
            if isinstance(j, int) != True:
                for k in j:
                    if k != j:
                        print(colored('\ndritte Schleife\n k ist = {}\n'.format(
                            k), 'green', 'on_blue'))
                    else:
                        break

                    # ! prüefe Bedingung für die vierte Schleife
                    if isinstance(k, int) != True:
                        for l in k:
                            if l != k:
                                print(colored('\nvierte Schleife\n l ist = {}\n'.format(
                                    l), 'cyan', 'on_white'))

                            # ! prüefe Bedingung für die fünfte Schleife
                            if isinstance(l, int) != True:
                                for m in l:
                                    if m != l:
                                        print(colored('\n fünfte Schleife\n m ist = {}\n'.format(
                                            m), 'green', 'on_magenta'))

                                    # ! prüefe Bedingung für die sechste Schleife
                                    if isinstance(m, int) != True:
                                        for n in m:
                                            if n != m:
                                                print(colored('\n sechte Schleife\n n ist = {}\n'.format(
                                                    n), 'red', 'on_yellow'))
