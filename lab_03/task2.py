import random

availableCityList = ["Warszawa", "Gdansk", "Torun",
                     "Bydgoszcz", "Pieklo", "Niebo",
                     "Zamosc", "Krakow", "Radom",
                     "Pokemon", "Gdynia", "Poznan",
                     "Wroclaw", "Lodz", "Katowice"]

claimedCities = []

for i in range(10):
    passed = False
    while not passed:
        temp = True
        index = random.randrange(len(availableCityList))

        for city in claimedCities:
            if availableCityList[index] == city:
                temp = False
                break
        if temp:
            claimedCities.append(availableCityList[index])
            passed = True

resultString = ""
for city in claimedCities:
    resultString = resultString + city + " "

print(resultString)