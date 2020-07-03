# -*- coding: utf-8 -*-

waga = float(input("Ile ważysz kilogramów? "))

wzrost = float(input("Jaki masz wzrost (w cm)? "))

wiek = int(input("Ile masz lat? "))

k = float(input("Porównaj się z następującą tabelą oraz wpisz wartość, która jest przypisana\ndo niej: \nPraca siedząca, brak aktywności fizycznej - 1.2\nPraca niefizyczna, mało aktywny tryb życia - 1.4\nLekka praca fizyczna, regularne ćwiczenia 3-4 razy (ok. 5h) w tygodniu - 1.6\nPraca fizyczna, regularne ćwiczenia od 5 razy (ok.7h) w tygodniu - 1.8\nPraca fizyczna ciężka, regularne ćwiczenia 7 razy w tygodniu - 2.0\n"))

p = str(input("Jesteś kobietą czy mężczyzną? (k/m) "))
p = p.upper()

if p == "K":
    S = -161
    PPM = 10*waga + 6.25*wzrost - 5*wiek + S
    print("\nPowinnaś dostarczać", int(PPM*k), "kalorii każdego dnia")
    input()
    
elif p == ("M"):
    S = 5
    PPM = 10*waga + 6.25*wzrost - 5*wiek + S
    print("\nPowinieneś dostarczać", int(PPM*k), "kalorii każdego dnia")
    input()
    
else:
    print("Nie ma takiej płci, papa!")
    input()
    
