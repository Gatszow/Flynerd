#-*- coding: utf-8 -*-

width=51
for x in range(1,11):
    print(width * '-')
    print("| %2.f | %2.f | %2.f | %2.f |"
          " %2.f | %2.f | %2.f | %2.f | %2.f | %2.f |"
           % (x*1,x*2,x*3,x*4,x*5,x*6,x*7,x*8,x*9,x*10))
print(width * '-')

input()
