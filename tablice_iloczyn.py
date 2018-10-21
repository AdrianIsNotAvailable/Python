tablica = []
ile = int(input('Ile chesz mieć liczb w tablicy : '))
for owca in range(1,ile + 1):
     wyraz = int(input('Podaj ' + str(owca) + ' liczbę : '))
     tablica.append(wyraz)
print('\n')
print('Twoja tablica to : ' + str(tablica))
print('\n')
wynik = 1
for el in tablica:
    wynik = wynik * el
print('Iloraz liczb w tablicy to : ' + str(wynik))
input('\n')