# -*- coding: utf-8 -*-
import time

persons = input("Podaj imiona, które mam przywitać ")
persons = persons.split()
for person in persons:
    person = person.strip(',')
    print("Witaj ", person.capitalize())
    time.sleep(1.5)
input("\nThe End\n")
