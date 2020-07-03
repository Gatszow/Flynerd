#-*- coding: utf8 -*-
print("Witaj, to program sortujący 3 liczby w kolejności od największej do najmniejszej\n")

f_num = float(input("Podaj pierwszą liczbę: "))
s_num = float(input("Podaj drugą liczbę: "))
t_num = float(input("Podaj trzecią liczbę: "))
print("\n")
if f_num > s_num and f_num > t_num:
    if s_num > t_num:
        print(f_num, s_num, t_num)
    else:
        print(f_num, t_num, s_num)
elif s_num > f_num and s_num > t_num:
    if f_num > t_num:
        print(s_num, f_num, t_num)
    else:
        print(s_num, t_num, f_num)
else:
    if f_num > s_num:
        print(t_num, f_num, s_num)
    else:
        print(t_num, s_num, f_num)

input()
