import random

odp = str(input('Co chcesz wybrać'))
print('Wpisz papier, kamień lub nożyce')
komputer = random.choice(['papier', 'kamień', 'nożyce'])

if odp == "papier":
    if komputer == "papier":
        print("!zremisowałeś!")
    if komputer == "kamień":
        print('!wygrałeś!')
    if komputer == "nożyce":
        print('!przegrałeś!')

if odp == "kamień"