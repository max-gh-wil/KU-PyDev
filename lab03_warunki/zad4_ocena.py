# Lab 03 – Zadanie 4 (★): Ocena z przedmiotu
#
# Program wczytuje liczbę punktów (0–100) i wypisuje ocenę według progów
# z sylabusa naszego przedmiotu:
#     > 91        -> 5
#     > 83 – 91   -> 4.5
#     > 75 – 83   -> 4
#     > 67 – 75   -> 3.5
#     > 60 – 67   -> 3
#     <= 60       -> 2
#
# Przykład:  Ocena: 4.5
# Uwaga: w zachęcie input() nie wypisuj liczb (np. „0-100”) – testy szukają liczb w wyjściu.

# TODO: Twój kod poniżej
print("Podaj ile procent z przedmiotu")
procent = int(input())
if procent > 91:
    ocena = 5
if 83 < procent <= 91:
    ocena = 4.5
if 75 < procent <= 83:
    ocena = 4
if 67 < procent <= 75:
    ocena = 3.5
if 60 < procent <= 67:
    ocena = 3
if procent <= 60:
    ocena = 2 
print(ocena)