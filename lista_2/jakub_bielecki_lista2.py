import ssl
import urllib.request

import pandas as pd
import requests
from sklearn import preprocessing


ssl._create_default_https_context = ssl._create_unverified_context

#Wczytaj dane z adresu podanego w pliku tekstowym: pliktextowy.txt
# do ramki danych.
#Użyj reszty wierszy jako nagłówków ramki danych.
#Uwaga! Zobacz która zmienna jest zmienną objaśnianą, będzie to potrzebne do dalszych zadań.
file = open("pliktextowy.txt")
url = file.readline()
data = str(urllib.request.urlopen(url).read())
data = data.replace('b', '')
data = data.replace('\'', '')

headers = []
for line in file:
    line = line.replace("\n", "")
    headers.append(line)

simple_format_data = data.split("\\n")
ready_data = []

for temp in simple_format_data:
    ready_data.append(temp.split(","))

data_frame_data = {}

i = 0
for header in headers:
    columns_data = []

    for a in ready_data:
        print("A")
        columns_data.append(a[i])

    data_frame_data[header] = columns_data
    i = i + 1

print(data_frame_data)

df = pd.DataFrame(data_frame_data) # tutaj podmień df. Ma zawierać wczytane dane.

#Zadanie1 przypisz nazwy kolumn z df w jednej linii:   (2pkt)

wynik1 = ""
for column in df.columns:
    wynik1 = wynik1 + " " + column
print(wynik1)

#Zadanie 2: Wypisz liczbę wierszy oraz kolumn ramki danych w jednej linii.  (2pkt)
wynik2 = str(len(df.columns)) + " " + str(len(df.index))
print(wynik2)


#Zadanie Utwórz klasę Wine na podstawie wczytanego zbioru:
#wszystkie zmienne objaśniające powinny być w liscie.
#Zmienna objaśniana jako odrębne pole.
# metoda __init__ powinna posiadać 2 parametry:
#listę (zmienne objaśniające) oraz liczbę(zmienna objaśniana).
#nazwy mogą być dowolne.

# Klasa powinna umożliwiać stworzenie nowego obiektu na podstawie
# już istniejącego obiektu jak w pdf z lekcji lab6.
# podpowiedź: metoda magiczna __repr__
#Nie pisz metody __str__.

#Zadanie 3 Utwórz przykładowy obiekt:   (3pkt)
wynik3 = "przykladowy obiekt typu Wine" #do podmiany. Pamiętaj - ilość elementów, jak w zbiorze danych.
#Uwaga! Pamiętaj, która zmienna jest zmienną objaśnianą
print(wynik3)

#Zadanie 4.                             (3pkt)
#Zapisz wszystkie dane z ramki danych do listy obiektów typu Wine.
#Nie podmieniaj listy, dodawaj elementy.
##Uwaga! zobacz w jakiej kolejności podawane są zmienne objaśniające i objaśniana.
# Podpowiedź zobacz w pliktextowy.txt
wineList = []
wynik4 = len(wineList)
print(wynik4)


#Zadanie5 - Weź ostatni element z listy i na podstawie         (3pkt)
#wyniku funkcji repr utwórz nowy obiekt - eval(repr(obiekt))
#do wyniku przypisz zmienną objaśnianą z tego obiektu:
wynik5 = "tu kod aby uzyskać nowy obiekt"
print(wynik5)


#Zadanie 6:                                                          (3pkt)
#Zapisz ramkę danych  do bazy SQLite nazwa bazy(dopisz swoje imię i nazwisko):
# wines_imie_nazwisko, nazwa tabeli: wines.
#Następnie wczytaj dane z tabeli wybierając z bazy danych tylko wiersze z typem wina nr 3
# i zapisz je do nowego data frame:
wynik6 = "W następnej linijce podmień na nowy  data frame z winami tylko klasy trzeciej:"
wynik6 = pd.DataFrame() #tutaj do podmiany

print(wynik6.shape)


#Zadanie 7                                                          (1pkt)
#Utwórz model regresji Logistycznej z domyślnymi ustawieniami:

model = "tu wstaw kod inicjalizujacy model"


wynik7 = model.__class__.__name__
print(wynik7)

# Zadanie 8:                                                        (3pkt)
#Dokonaj podziału ramki danych na dane objaśniające i  do klasyfikacji.
#Znormalizuj dane objaśniające za pomocą:
#X = preprocessing.normalize(X)
# Wytenuj model na wszystkich danych bez podziału na zbiór treningowy i testowy.
# Wykonaj sprawdzian krzyżowy, używając LeaveOneOut() zamiast KFold (Parametr cv)
#  Podaj średnią dokładność (accuracy)

wynik8 = "tu wstaw średnią dokładność"
print(wynik8)