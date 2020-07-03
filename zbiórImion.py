#-*- coding: utf-8 -*-

m_names = ['Rafał', 'Wojtek', 'Michał']
f_names = ['Olga', 'Julia', 'Jolanta']

name = input("Podaj imię: ")
name = name.capitalize()

try:
    name = float(name)
except:
    pass

if name in m_names:
    print(name, "to imię męskie")
elif name in f_names:
    print(name, "to imię damskie")
else:
    if type(name) == str:
        new = input("Tego imienia nie ma na liście. Jest to imię męskie czy żeńskie?: (Wybór: m/z) ")
        new = new.capitalize()
        if new == 'Z' or 'Ż':
            f_names.append(name)
            print("Imię dodane do listy!")
        elif new == "M":
            m_names.append(name)
            print("Imię dodane do listy!")
        else:
            print("Nieprawidłowa płeć")
    else:
        print("Nieprawidłowe dane")

print("Imiona męskie w bazie:", m_names, '\n' + "Imiona żeńskie w bazie:", f_names)
input()
