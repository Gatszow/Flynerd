#Formatowanie

print("\"Stare Formatowanie\"")
szer = 42
print("-" * szer)
print("|  Czas  |     Zawodnik     |    Data    |")
print("*" * szer)
print("| %6.3f | %16s | %10s |" % (9.58, "Usain Bolt", "16.08.2009"))
print("| %6.3f | %16s | %10s |" % (9.69, "Tyson Gay", "20.09.2009"))
print("| %6.3f | %16s | %10s |" % (9.69, "Yohan Blake", "23.09.2012"))
print("| %6.3f | %16s | %10s |" % (9.74, "Asafa Powell", "2.09.2008"))
print("-" * szer)

print("\n\"Nowe Formatowanie\"")
szer = 42
print("-" * szer)
print("|  Czas  |     Zawodnik     |    Data    |")
print("*" * szer)
print("| {:6.3f} | {:16s} | {:10s} |" .format(9.58, "Usain Bolt", "16.08.2009"))
print("| {:6.3f} | {:16s} | {:10s} |" .format(9.69, "Tyson Gay", "20.09.2009"))
print("| {:6.3f} | {:16s} | {:10s} |" .format(9.69, "Yohan Blake", "23.09.2012"))
print("| {:6.3f} | {:16s} | {:10s} |" .format(9.74, "Asafa Powell", "2.09.2008"))
print("-" * szer)

waluta = "dolar"
us = 1
pln = 4.08234915
print("\nAktualnie %d %s kosztuje %.2f zł\n" % (us, waluta, pln))
print("Akutalnie {} {} kosztuje {:.2f} zł".format(us, waluta, pln))
print("\nAktualnie %r %r kosztuje %r zł" % (us, waluta, pln))

#Dla starego formatowania wystąpienie, które ma zostać zastąpione przez:
#    napis oznaczamy: %s (s – string)
#    liczbę całkowitą oznaczamy: %d (d – digit)
#    liczbę zmiennoprzecinkową: %f (f – float)
#    dowolną wartość: %r (r – raw)

input()
