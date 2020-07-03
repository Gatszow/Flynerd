#-*- coding: utf-8 -*-
import random

l_num = int(input("Podaj liczbę końcową losowania: "))

r_num = random.randint(1, l_num+1)

a_num = int(input("Podaj ile chcesz mieć prób zgadnięcia liczby: "))

attempt = 0
while attempt < a_num:
    u_num = input("Podaj numer, który myślisz, że wylosowało: ")
    attempt += 1
    try:
        u_num = int(u_num)
        if r_num == u_num:
            print("Gratuluję, liczba została odgadnięta")
            break
        elif r_num > u_num:
            print("Niestety to nie ta liczba, twoja liczba jest za mała")
        elif r_num < u_num:
            print("Liczba nie została zgadnięta, wpisz mniejszą cyfrę!")
        print("Pozostało prób:", a_num - attempt)
    except ValueError:
        print("Błąd danych, spróbuj raz jeszcze")
        attempt -= 1
if attempt == a_num:
    print("Zostały wykorzystane wszystkie próby\nPRZEGRANA")

input()
