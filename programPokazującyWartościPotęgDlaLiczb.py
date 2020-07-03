# -*- coding: utf-8 -*-

power = int(input("Podaj potęgę, do jakiej chcesz podnieść liczby: "))
s_range = int(input("Podaj początek zakresu liczb, które chcesz, aby spotęgowało: "))
f_range = int(input("Podaj koniec zakresu liczb, które chcesz, aby spotęgowało: "))

if type(power) == int and type(s_range) == int and type(f_range) == int:
    print("Liczba:         Potęga:")
    for result in range(s_range, f_range+1):
        print(result, "       -     ", result**power)
else:
    print("Nieprawidłowe dane ")

input()
