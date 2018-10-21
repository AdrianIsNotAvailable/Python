import random
liczba_tur = int(input('Wpisz ile rund chcesz grać (minimalnie 1) : '))
wygrane_k = 0
wygrane_g = 0
for liczba in range (0,liczba_tur):

    odp = str(input('Co chcesz wybrać ? \nWpisz papier, kamień lub nożyce : '))

    komputer = random.choice(['papier', 'kamień', 'nożyce'])

    print('\nWybrałeś ' + str(odp) +' !')
    print('Komputer wybrał ' + str(komputer) + ' !')
    print('\n')
    if odp == "papier":
        if komputer == "papier":
            print("! zremisowałeś !")
        if komputer == "kamień":
            print('! wygrałeś !')
            wygrane_g +=1
        if komputer == "nożyce":
            print('! przegrałeś !')
            wygrane_k += 1

    if odp == "kamień":
        if komputer == "kamień":
            print("! zremisowałeś !")
        if komputer == "nożyce":
            print('! wygrałeś !')
            wygrane_g += 1
        if komputer == "papier":
            print('! przegrałeś !')
            wygrane_k += 1

    if odp == "nożyce":
        if komputer == "nożyce":
            print("! zremisowałeś !")
        if komputer == "papier":
            print('! wygrałeś !')
            wygrane_g += 1
        if komputer == "kamień":
            print('! przegrałeś !')
            wygrane_k += 1

    print('Masz ' + str(wygrane_g) + ' punktów!')
    print('Komputer ma ' + str(wygrane_k) + ' punktów!\n')
if wygrane_g > wygrane_k:
    print('!!! WYGRAŁEŚ MECZ !!!')
if wygrane_k > wygrane_g:
    print('!!! PRZEGRAŁEŚ MECZ !!!')
if wygrane_k == wygrane_g or wygrane_g == wygrane_k:
    print('!!! REMIS !!!')
input('\n')