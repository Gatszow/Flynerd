#-*- coding: utf-8 -*-
print("Jest to program pokazujący wynik sumy naturalnych poprzedników\n")
times = int(input("Ile chcesz wyników? "))
num = 1
t_num = 0

while num <= times:
    print("Wynik",num, "-", num+t_num)
    t_num = t_num + num
    num += 1
    
