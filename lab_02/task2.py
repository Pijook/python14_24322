numberA = int(input("Enter number A "))
numberB = int(input("Enter number B "))

operator = input("Enter operator (+, -, * , /) ")

if operator == "+":
    print(numberA + numberB)
elif operator == "-":
    print(numberA - numberB)
elif operator == "*":
    print(numberA * numberB)
elif operator == "/":
    print(numberA / numberB)
else:
    print("Invalid operator!")
