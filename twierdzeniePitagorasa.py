#-*- coding: utf8 -*-

side1 = float(input("Podaj miarę pierwszego boku: "))
side2 = float(input("Podaj miarę drugiego boku: "))
side3 = float(input("Podaj miarę trzeciego boku: "))

if side3 < side1:
    temp = side3
    side3 = side1
    side1 = temp
if side3 < side2:
    temp = side3
    side3 = side2
    side2 = temp
if side2 < side1:
    temp = side2
    side2 = side1
    side1 = temp

if side1+side2>side3 and side2+side3>side1 and side1+side3>side2:
    if side1**2 + side2**2 == side3**2:
        print("Trójkąt jest trójkątem pitagorejskim", end="")
        if side1/3 == side2/4 == side3/5:
            print(", a dodatkowo jest to trójkąt egipski.")
        else:
            print(".")
    else:
        print("Jest to trójkąt, jednak nie pitagorejski.")
else:
    print("Nie ma trójkąta o takich miarach.")

input()
