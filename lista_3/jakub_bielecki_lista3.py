# Zadanie 1 (4pkt):
# Utwórz klasę iteratora dla listy. Użyj go do wstawienia elementów listy lista1 do strina.
# elementy mają znajdować się w stringu jednym wierszu niczym nierozdzielone:
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
wynik1 = "wstaw w wynik1"
wynik1 = ""


class MyIterator:
    def __init__(self, lst):
        self.lst = lst
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.lst):
            element = str(self.lst[self.index])
            self.index += 1
            return element
        else:
            raise StopIteration


iterator = MyIterator(lista1)

for element in iterator:
    wynik1 = wynik1 + element

print(wynik1)


# Zadanie2: (4pkt)
# Napisz funkcję fizzbuzz(n), która używając listy składanej zwróci
# listę od 1 do n włącznie liczb lub wyrazów Fizz, Buzz, FizzBuzz, zgodnie ze standradową
# reguła gry w FizzBuzz:
# Jeśli liczba jest podzielna przez 3 i niepodzielna przez 5, zamiast liczby mamy "Fizz".
# Jeśli liczba jest podzielna przez 5 i niepodzielna przez 3, zamiast liczby mamy "Buzz".
# Jeśli liczba jest zarówno podzielna przez 3, jak i przez 5, zamiast liczby mamy "FizzBuzz".
def fizbuzz(n):
    return [
        'Fizz' if i % 3 == 0 and i % 5 != 0
        else 'Buzz' if i % 5 == 0 and i % 3 != 0
        else 'FizzBuzz' if i % 3 == 0 and i % 5 == 0
        else i
        for i in range(1, n + 1)
    ]


wynik2 = fizbuzz(16)
print(wynik2)


# Zadanie 3 (4pkt):
# Napisz generator zwracający n wyrazów ciągu Lucasa
# do wyniku zapisz 6 element tego ciągu.
def ciag_lucasa(n):
    pierwsze_pole = 2
    drugie_pole = 1
    yield pierwsze_pole
    yield drugie_pole
    for _ in range(2, n):
        pierwsze_pole, drugie_pole = drugie_pole, pierwsze_pole + drugie_pole
        yield drugie_pole


wynik3 = list(ciag_lucasa(6))[-1]
print(wynik3)


# Zadanie4 (4pkt):
# Uzyj klasy napisanej na ostatnich zajęciach - wersji z iteratorem (wklej tutaj klasę)
# Do przechowywania znaków kodu javy z pliku Main.java.
class Stack:
    def __init__(self, max_size=99999):
        self.items = []
        self.max_size = max_size

    def push(self, item):
        if len(self.items) < self.max_size:
            self.items.append(item)
        else:
            raise IndexError("Stack overflow")

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __iter__(self):
        return self

    def __next__(self):
        if not self.is_empty():
            return self.pop()
        else:
            raise StopIteration


file_path = "Main.java"
java_code = ""

with open(file_path, "r") as file:
    java_code = file.read()

stack = Stack()

# Push each character of the Java code onto the stack
for char in java_code:
    stack.push(char)

obiekt = stack
wynik4 = obiekt
# następnie wstaw do niej znaki z kodu javy, które wczytasz z pliku Main.java
# ODKOMENTUJ poniższą linijkę, gdy utworzysz obiekt i dodasz do niego znaki:
'''
!odkomentuj wynik4!:
'''
wynik4 = obiekt.size()
print(wynik4)


# Zadanie 5 (4pkt):
# Napisz funkcję, która sprawdzi poprawność kodu javy, używając obiektu z poprzedniego zadania
# i uwzględniając tylko nawiasy w kodzie.
# funkcja ma zwrocic True albo False w zależności czy kod jest poprawny czy nie.

def validation(kod_o):
    stack = Stack()
    otwarte_nawiasy = ["(", "{", "["]
    zamkniete_nawiasy = [")", "}", "]"]

    for znak in kod_o:
        if znak in otwarte_nawiasy:
            stack.push(znak)
        elif znak in zamkniete_nawiasy:
            if stack.is_empty():
                return False
            ostatni_otwarty = stack.pop()
            if otwarte_nawiasy.index(ostatni_otwarty) != zamkniete_nawiasy.index(znak):
                return False

    return stack.is_empty()


wynik5 = validation(kod_o=obiekt)
print(wynik5)
