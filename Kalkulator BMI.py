# -*- coding: utf8 -*-

wzrost = float(input("Podaj wzrost (cm): "))

waga = float(input("Podaj wagę (kg): "))

BMI = waga/(wzrost/100)**2

#alternatywy:
"""
print("Twoje BMI wynosi: %f" % BMI)
print("Twoje BMI wynosi: {:f}".format(BMI))
"""
print("Twoje BMI wynosi:", round(BMI,2))

if BMI < 18.5:
    condition = "Niedowaga"
elif 18.5 < BMI < 24:
    condition = "Waga normalna"
elif 24 < BMI < 26.5:
    condiion = "Lekka nadwaga"
elif BMI > 26.5:
    condition = "Nadwaga"
    if 30 < BMI < 35:
        condition = condition + " oraz Otyłość I stopnia"
    elif 35 < BMI < 40:
        condition = condition + " oraz Otyłość II stopnia"
    elif BMI > 40:
        condition = condition + " oraz Otyłość III stopnia"
    else:
        condition = condition + ", brak otyłości"

print("Twój stan: %s" % condition)

input()
