# -*- coding: utf-8 -*-

silnia_num = int(input("Podaj cyfrę, z której chcesz zrobić silnię - "))

silnia = 1
for z in range(1, silnia_num+1):
    silnia = silnia * z
print("Silnia liczby {}, to {}".format(silnia_num, silnia))
input("The End\n")
