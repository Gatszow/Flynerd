# -*- coding: utf-8 -*-
import webbrowser

s_range = int(input("Podaj liczbę od której program ma działać: "))
f_range = int(input("Podaj liczbę do której program ma działać: "))

for i in range(s_range, f_range+1):
    print("Liczba ", i)
    if i%3 == 0 and i%4 == 0:
        print("Liczba jest wielokrotnością trójki i czwórki")
    elif i%3 == 0:
        print("Liczba jest wielokrotnością trójki")
    elif i%4 == 0:
        print("Liczba jest wielokrotnością czwórki")
    else:
        print("Liczba nie jest wielokrotnością ani trójki, ani czwórki")

for a in range(80):
    print("#", end="")
"""
bonus = input("\nPamiętaj, że cię kocham Skarbie!!!\nWściśnij \"pewną\" literę, a zobaczysz bonusik, hihi: ")
bonus = bonus.capitalize()
if bonus == "K":
    print("\nHaha, a tym razem jak długo szukałaś? Mrrrr <3")
    bonus = input("Szukaj kolejnej, jeszcze sporo przed tobą :P - ")
    bonus = bonus.capitalize()
    if bonus == "O":
        print("\nNo, no, gratuluję, chyba powoli trzeba zacząć brać tutaj twoją determinację na \npoważnie!!")
        bonus = input("Następna litera to... ")
        bonus = bonus.capitalize()
        if bonus == "C":
            print("\nJesteś najlepsza koteczku najukochańszy... Ale to jeszcze nie koniec 3:)")
            bonus = input("A o to kolejna litera w naszej grrrrze: ")
            bonus = bonus.capitalize()
            if bonus == "H":
                print("\nMmmmm, podoba mi się ten upór, kociaczku, ale bym cię brał po prostu, hihi")
                bonus = input("A zgadniesz kolejną literkę? Podaj ją teraz: ")
                bonus = bonus.capitalize()
                if bonus == "A":
                    print("\nKocham cię za twoją troskę, miłość, rozmowę, zapach, śmiech, a szczególnie za tą twoją pozytywna stronę, hihi")
                    bonus = input("Jakby ci to powiedzieć... Potrzebuję kolejnej literki ;( - ")
                    bonus = bonus.capitalize()
                    if bonus == "M":
                        print("\nHehe, Teraz powinno być już z górki, o ile już rozszyfrowałaś hasło, ale no jak nie, to po co skarbie, bejb, please stop, BEJB, hahaha")
                        bonus = input("No ale poproszę o kolejną literkę: ")
                        bonus = bonus.capitalize()
                        if bonus == "C":
                            print("\nNo, no, teraz powiem ci co było na końcu Inkuba, to co masz mi przypominać, jak zapomnę, hehe")
                            bonus = input("Ale najpierw litereczka, aby przejść dalej - ")
                            bonus = bonus.capitalize()
                            if bonus == "I":
                                print("\nJuż na pewno znasz hasełko, którym się posluguje, ale to nie szkodzi, a więc na końcu było to...")
                                bonus = input('''\"... wszystko to kwestia determinacji.\nPrzy jej określonym poziomie można
osiągnąć każdy cel.\nNawet oszukać śmierć\"\nTo koniec, no albo prawie koniec, who knows, haha ''')
                                bonus = bonus.capitalize()
                                if bonus == "E":
                                    print("\nNo jak widać serio mnie kochasz moja kochaniutka istotko, ale jaki uparciszek, hihi, bardzo podoba mi się twoja determinacja!!!")
                                else:
                                    webbrowser.open('https://www.youtube.com/watch?v=WNnzw90vxrE')
                            else:
                                print("\nDziękuję ci, że dotrwałaś do tego momentu, pewnie trwało to nie lada moment, jednak jak widac, Opłacało się!!, czyż nie mam racji?")
                        else:
                            print("\nNo kociaczku, tak jak ty coś stworzyłaś dla mnie, tak i ja tu sobie tworzę, hehe, spróbuj raz jeszcze!!!")
                    else:
                        print("\nZostały ci jedynie jeszcze parę literek, Kochanie!!! Wiem, że dasz radę!!! Spróbuj raz jeszcze!!!")
                else:
                    print("\nHmmm, właśnie chcę ci powiedzieć, że już jesteś w mniejszej połowie programu, oby tak dalej!!!")
            else:
                print("\nWażne, że się nie poddajesz!!!! Spróbuj ponownie!!! Powodzenia kochany skarbusiu!!!!")
        
        else:
            print("\nBardzo ładnie Ci to wychodzi, jestem dumny!!! Spróbuj ponownie!!!! Good luck my dear!!! Jesteś bardzo kochaniutka :P")
                          
    else:
        print("\nMmm, jesteś inteligentna, dlatego sobie poradzisz, wierzę w Ciebie!!! Spróbuj ponownie!!!! Good luck my dear!!! Kooooocham cie!!!")
                          
else:
    print("\nNo cóż, nie ta litera, spróbuj ponownie! Good luck my dear!")
"""                        
input("\nTHE END\n")

