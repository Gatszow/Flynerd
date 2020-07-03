#-*- coding: utf-8 -*-

s_range = int(input("Podaj początek zakresu sumowania liczb: "))
f_range = int(input("Podaj koniec zakresu sumowania liczb: "))
f_or_e_s = str(input("Czy chcesz zobaczyć jedynie ostateczny wynik?: (T/N) - "))
if_next = str(input("Czy chcesz, aby dodawało występujące kolejno po sobie liczby? (T/N) - "))

#f_or_e_s == final or every step

f_or_e_s = f_or_e_s.capitalize()
if_next = if_next.capitalize()

if if_next == "T":
    loop_range = 1
elif if_next == "N":
    loop_range = int(input("Wprowadź, co którą liczbę program ma sumować:(wpisz cyfrę, np. 3) - "))
else:
    print("Złe dane, dodaje kolejno występujące po sobie liczby.")
    loop_range = 1

result=0
for long in range(0,80):
    print("#", end="")

print("Wynik:")

if f_or_e_s == "N":
    for loop in range(s_range, f_range+1, loop_range):
        result = loop + result
        print(result)
elif f_or_e_s == "T":
    for loop in range(s_range, f_range+1, loop_range):
        result = loop + result
    print(result)
else:
    print("Złe Dane.")

input()
