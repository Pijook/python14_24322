numberStream = input("Podaj serie numerow (numer,numer,numer) ")

first = 1
currentMin = 0
currentMax = 0

for numberString in numberStream.split(","):
    temp = int(numberString)
    if first == 1:
        first = 0
        currentMin = temp
        currentMax = temp
    else:
        if temp < currentMin:
            currentMin = temp
        elif temp > currentMax:
            currentMax = temp

print("Min ", currentMin)
print("Max ", currentMax)
