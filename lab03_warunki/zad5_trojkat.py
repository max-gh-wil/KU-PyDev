# Lab 03 – Zadanie 5 (☆, dodatkowe): Jaki to trójkąt?
#
# Program wczytuje trzy długości boków (float) i wypisuje:
#   - "Nie da się zbudować trójkąta", jeśli nie spełniają nierówności trójkąta
#     (każdy bok musi być krótszy od sumy dwóch pozostałych),
#   - w przeciwnym razie rodzaj: "równoboczny", "równoramienny" albo "różnoboczny",
#   - dodatkowo "prostokątny", jeśli a² + b² = c² dla najdłuższego boku c
#     (porównuj z tolerancją: abs(x - y) < 1e-9).

# TODO: Twój kod poniżej
print("Podaj 1 długość")
dlugosc1 = float(input())
print("Podaj 2 długość")
dlugosc2 = float(input())
print("Podaj 3 długość")
dlugosc3 = float(input())
if dlugosc1 + dlugosc2 < dlugosc3 or dlugosc3 + dlugosc2 < dlugosc1 or dlugosc1 + dlugosc3 < dlugosc2:
    print("Nie mozna utworzyć trójkąta")
else:
    print("Mozna utworzyć trójkąt")

    
