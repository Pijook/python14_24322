import random
from getpass import getpass

rulesDict = {
    "Papier": "Kamien",
    "Kamien": "Nozyce",
    "Nozyce": "Papier"
}

symbols = ["", "Papier", "Kamien", "Nozyce"]

roundAmount = int(input("Wybierz ilosc rund: "))
gameType = int(input("Wybierz typ gry (1 - Gracz vs Komputer, 2 - Gracz vs Gracz)"))

userName1 = ""
userName2 = ""

gameResults = []

if gameType == 1:
    userName1 = input("Wpisz swoja nazwe")
    userName2 = "Komputer"
elif gameType == 2:
    userName1 = input("Wpisz swoja nazwe pierwszego gracza")
    userName2 = input("Wpisz swoja nazwe drugiego gracza")

for i in range(roundAmount):
    choice1 = -1
    choice2 = -1

    roundResult = 0

    if gameType == 1:
        choice1 = int(input("Wybierz ruch (1 - Papier, 2 - Kamien, 3 - Nozyce)"))
        choice2 = int(random.randrange(1, 4))
    elif gameType == 2:
        choice1 = int(getpass("Wybierz ruch (1 - Papier, 2 - Kamien, 3 - Nozyce)"))
        choice2 = int(getpass("Wybierz ruch (1 - Papier, 2 - Kamien, 3 - Nozyce)"))

    print(symbols[choice1], "vs", symbols[choice2])

    if choice1 == choice2:
        roundResult = 0
    elif rulesDict[symbols[choice1]] == rulesDict[symbols[choice2]]:
        roundResult = 1
    else:
        roundResult = 2

    if roundResult == 0:
        print("Remis!")
    else:
        print("Wygral " + userName2)

    gameResults.append(roundResult)

gamesResultSum = {
    0: 0,
    1: 0,
    2: 0
}

for roundResult in gameResults:
    gamesResultSum[roundResult] = gameResults[roundResult] + 1
    if roundResult == 0:
        print("Remis")
    elif roundResult == 1:
        print("Runde wygral " + userName1)
    else:
        print("Runde wygral " + userName2)

if gamesResultSum[0] > gamesResultSum[1] and gamesResultSum[0] > gamesResultSum[2]:
    print("To byla rowna gra!")
elif gamesResultSum[1] > gamesResultSum[0] and gamesResultSum[1] > gamesResultSum[2]:
    print("Gre wygral", userName1)
elif gamesResultSum[2] > gamesResultSum[0] and gamesResultSum[2] > gamesResultSum[1]:
    print("Gre wygral", userName2)
