# -*- coding: utf-8 -*-
start = float(input("Stan początkowy konta wynosi: "))

rate = float(input("Stopa oprocenotowania w skali roku: "))

y = int(input("Liczba lat na lokacie: "))
end = start*(1 + rate*y)

print ("Po {} latach kapitał będzie wynosił {} zł".format(y, end))
