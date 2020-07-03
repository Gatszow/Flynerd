#-*- coding: utf8 -*-

name = str(input("Podaj swoje imię: "))
age = float(input("Podaj swój wiek: "))
if name == "Olga":
    print('''Jaki skarbuś, napisała z wielkiej literki, hihi, kocham cię!!!!
Ale ciekawe, czy to jest twoja pierwsza próba (hmmm), haha
Pamiętaj, aby pisać z wielkiej literki koteczku!!!''')
else:
    print("Witaj nieznana mi osobo. Znajdź prawidłowe imię.")
if age < 18:
    print("Użytkownik niepełnoletni")
    before_18 = 18 - age
    print("Zostało do pełnoletności {} lat".format(before_18))
elif age > 18:
    print("Użytkownik pełnoletni")
    if age > 100:
        print("200 lat!!!")
    else:
        print("100 lat!!!")
input()
