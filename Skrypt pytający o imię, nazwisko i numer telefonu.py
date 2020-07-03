# -*- coding: utf-8 -*-

name = input("Podaj swoje imię: ")
second_name = input("Podaj swoje nazwisko: ")
number = input("Podaj swój numer telefonu: ")

print("Czy imię składa się tylko z liter?", name.isalnum())
print("Czy nazwisko składa się tylko z liter?", second_name.isalnum())
print("Czy numer telefonu składa się z cyfr", number.isdigit())
#print(name)
name = name.capitalize()
#print(second_name)
second_name = second_name.capitalize()
#print(name, second_name)

#print(number)
number = number.replace(" ", "").replace("-", "")
#print(number)

personal = name + " " + second_name + " " + number
print("Podsumowanie:\n", personal)

print("\nIlość znaków w \"Podsumowanie\": ", len(personal))

letters = len(personal) - personal.count(" ") - 9
print("\nLiczba liter w Podsumowaniu: ",  letters)
input()

'''
name = input("Imię: ")
surname = input("Nazwisko: ")
number = input("Numer telefonu: ")

print("Czy imię składa się tylko z liter?", name.isalpha())
print("Czy nazwisko składa się tylko z liter?", surname.isalnum())
print("Czy numer telefonu składa się z cyfr", number.isdigit())

print(name, surname)
name = name.capitalize()
surname = surname.capitalize()
print(name, surname)

print(number)
number = number.replace(" ", "").replace("-","")
print(number)

print("Imię kobiece:", name.endswith("a"))

personal = name + " " + surname + " " + number
print(personal)
print(len(personal))

letters = len(personal) - personal.count(" ") - 9
print(letters)
print (len(name + surname)) #sprawdzenie
input()
'''
