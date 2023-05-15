import random
#Lista1

'''
UWAGA! Nie należy zmieniać nazw funkcji, oraz wartości zmiennych podanych w pliku
poza wartościami ze stringiem "PODAJ WYNIK" - w tych zmiennych należy przechowywać wynik
dotyczący poszczególnych zadań w_1, w_2 ... w_6.

Ciało funkcji wpisujemy w kodzie zamiast "pass".

Wyniki z każdego zadania powinny wyświetlać się w jednej linijce.
Nie należy wyświetlań nic poza wynikiem działania kodu z poszczególnych zadań
w kolejności tak jak w pliku.
Plik należy zapisać w postaci: imie_nazwisko_lista1.py
'''

#1. Ile unikatowych elementów znajduje się w liście:
#1 pkt
lista_1 = [0,7,8,3,3,0,7,0,3]

lista_1_dict = {}
for element in lista_1:
    if element in lista_1_dict.keys():
        lista_1_dict[element] = lista_1_dict[element] + 1
    else:
        lista_1_dict[element] = 1

w_1 = "PODAJ WYNIK"
w_1 = 0
for key in lista_1_dict.keys():
    if lista_1_dict[key] == 1:
        w_1 = w_1 + 1

print(w_1)

#2. Napisz kod, który podmieni losowy znak ze stringa
s_2 = "ala ma kota"
#na '0':
#2 pkt

w_2 = "PODAJ WYNIK"

print(w_2)


#3. Napisz kod który podmieni z lista_3 język programowania R na JS, następnie wyświetl podmieniony JS.
# Przed JS nadal musi znajdować się python w strukturze takiego samego typu jak w przykladowej lista_3.
# 2pkt
lista_3 = [[{1: 'java', 0: ('python', 'R')},'c++'],['word', 'excel']]

w_3 = "PODAJ WYNIK"
print(w_3)


#4. Jakiego typu dane z poniższych nie mogą być kluczami słownika?
#boolean,float,int,string,tuple,list,set. Odpowiedź umieśc w stringu w_4
#1 pkt

w_4 = "PODAJ WYNIK"
print(w_4)

#5. Dla stringa wypisz
#ile razy pojawił się dany znak, w kolejności alfabetycznej.
#Użyj słownika - wynik również ma być słownikiem.
#Sprawdzamy tylko te znaki, które występują w podanym stringu.
#2 pkt

s_5 = "ala ma kota imie ma macko"

w_5 = "PODAJ WYNIK"
print(w_5)

#6. Napisz kod który sprawdzi, czy w poprzednim stringu s_5,
#jakikolwiek znak wystąpił dokładnie 3 razy. Wyświetl Tak jeżeli wystąpił,
#Nie jeżeli nie wystąpił.
#1 pkt

w_6="PODAJ WYNIK"
print(w_6)

#7. Napisz funkcję sprawdzającą czy podane słowa/zdania są palindromem
#i zwróci True lub False ( jest/ nie jest).
#Pomiń znaki nie będące literami, wielkość liter nie ma znaczenia
#3pkt

def palindrom(s):
    pass

s_7_1 ="Nowy Targ, góry, Zakopane – na pokazy róg, graty won"
print(palindrom(s_7_1))


#8. Napisz funkcję, która zwróci
#wszystkie liczby od 1 do n w jednym stringu rozdzielone przecinkami,
#jednak jeżeli liczba jest podzielna przez:
#trzy – zamiast liczby mamy „Fizz”,
#pięć – zamiast liczby mamy „Buzz”,
#trzy i pięć zamiast liczby mamy „FizzBuzz”.
#wszystkie liczby/słowa mają zostać zwróćone w jednej linii, oraz być rozdzielone przecinkiem
#BEZ spacji
#2 pkt

def fizzbuzz(n):
    pass

n_8 = 16
print(fizzbuzz(n_8))

#9. Napisz funkcję zwracającą n-ty element ciągu Fibonacciego
# przy F(0)= 0 i F(1) = 1.
#bez rekurencji:
#3 pkt

n_9 = 6
def fibonacci(n):
    pass
print(fibonacci(n_9))

#10. Napisz funkcję, która dla podanej posortowanej listy
#zwróci index wyszukiwanego elementu za pomocą wyszkukiwania binarnego,
#lub zwróci None gdy nie ma elementu w liscie:
#3 pkt


def binary_search(lista, e):
    pass

l_10 = [0,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768]
print(binary_search(l_10, 2))
