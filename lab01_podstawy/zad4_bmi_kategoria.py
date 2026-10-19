# Lab 01 – Zadanie 4 (☆, dodatkowe): Kategoria BMI
#
# Rozbuduj kalkulator BMI: po obliczeniu wypisz także kategorię (wg WHO):
#     BMI < 18.5          -> niedowaga
#     18.5 <= BMI < 25    -> waga prawidłowa
#     25 <= BMI < 30      -> nadwaga
#     BMI >= 30           -> otyłość
#
# To zadanie wymaga instrukcji if / elif / else, którą dokładnie poznasz
# w labie 03. Spróbuj już teraz – składnię znajdziesz na slajdach.

# TODO: Twój kod poniżej
print("Podaj swoją wagę w kg")
masa = float(input())
print("Podaj swój wzrost w m")
wzrost = float(input())
bmi = masa / wzrost ** 2
if bmi < 18.5:
    print("niedowaga")
elif bmi < 25:
    print("waga prawidłowa")
elif bmi < 30:
    print("nadwaga")
elif bmi >= 30:
    print("otyłość")