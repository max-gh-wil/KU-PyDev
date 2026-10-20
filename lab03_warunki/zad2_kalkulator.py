# Lab 03 – Zadanie 2 (★): Kalkulator z wyborem działania
#
# Program wczytuje kolejno: liczbę, operator (+, -, *, /) i drugą liczbę,
# a potem wypisuje wynik, np.:  8.0 * 2.0 = 16.0
#
# Obsłuż przypadki szczególne instrukcją if:
#   - dzielenie przez zero  -> "Nie można dzielić przez zero"
#   - inny operator         -> "Nieznany operator"

# TODO: Twój kod poniżej
print("Podaj liczbę")
liczba = int(input())
print("Podaj operator: +, -, *, /")
operator = input()
print("Podaj drugą liczbę")
druga = int(input())
if operator not in ["+", "-", "*", "/"]:
    print("nieznany operator")
if operator == "+":
    print(liczba + druga)
if operator == "-":
    print(liczba - druga)
if operator == "*":
    print(liczba * druga)
if operator == "/":
    if druga == 0:
        print("Nie można dzielić przez zero!")
    else:
        print(liczba / druga)
