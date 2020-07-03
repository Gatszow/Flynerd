# -*- coding: utf-8 -*-

import random
print("#"*80, end="")

print("Jest to gra, w której musisz zgadnąć wylosowane słowo\n- aby natychmiast zakończyć działanie progamu wprowadź literę \"Q\",\n- aby od razu przejść do innego słowa, wprowadź literę \"N\"")

print("#"*80, end="")

lista = ["Pieseł", "Ludź", "Nieumięśniony", "Powała", "Kartka", "Owal", "Koral"]

obiekt = random.choice(lista)
p_obiekt = list(obiekt)
random.shuffle(p_obiekt)

ch = True
while ch == True:
    print("Zgadnij co to za słowo: {} ".format("".join(p_obiekt)))
    wybor = input()
    wybor = wybor.lower()
    wybor = wybor.capitalize()
    if wybor == obiekt:
        ch = input("Gratuluję, nastąpiło zgadnięcie słowa, czy chcesz kontynuować? T/N ")
        ch = ch.upper()
        if ch == "N":
            break
        else:
            ch = True
            obiekt = random.choice(lista)
            p_obiekt = list(obiekt)
            random.shuffle(p_obiekt)
    elif wybor == "N":
        obiekt = random.choice(lista)
        p_obiekt = list(obiekt)
        random.shuffle(p_obiekt)
    elif wybor == "Q":
        break
    else:
        print("Nie wyszło, spróbuj ponownie!")
print("#"*80, end="")
input("The End\n")


