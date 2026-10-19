# Lab 02 – Zadanie 4 (★): Sekundy na godziny, minuty i sekundy
#
# Program wczytuje liczbę sekund (int) i wypisuje ją DOKŁADNIE w formacie:
#     1 h 2 min 5 s
# (dla 3725 sekund).
#
# Wskazówki:
#   - int(input(...)) – konwersja tekstu na liczbę całkowitą
#   - // dzielenie całkowite, % reszta z dzielenia
#   - 1 h = 3600 s, 1 min = 60 s

# TODO: Twój kod poniżej
print("Podaj liczbę sekund")
sek = int(input())
godz = sek // 60 // 60 
minuty = ((sek / 60 / 60) - godz) * 60
sec = minuty / 60 - int(minuty) /60 
print(f"{godz} h {minuty:.0f} min {sec:.0f} s")
