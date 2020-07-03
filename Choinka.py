# -*- coding: utf8 -*-

r_ch = int(input("Podaj rozmiar: "))
for r in range(0, r_ch):
    for y in range(0, r+2):
        for x in range(0, y+1):
            print("#", end="")
        print()
