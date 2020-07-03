# -*- coding: utf8 -*-
dlugosc = float(input("Wprowadź długość w centymetrach "))

wybor = str(input("Chcesz wynik w metrach czy w calach? "))

if wybor == ("w calach"):
    print(round(dlugosc/2.54,4), "cal")
elif wybor == ("w metrach"):
    print(dlugosc/100, "m")
    
input()
