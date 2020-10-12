#c1
print("Vyberte číslo 1:")
c1 = int(input("číslo: "))
print("")

#c2
print("Vyberte číslo 2:")
c2 = int(input("číslo: "))
print("")

#c3
print("Vyberte znaménko: (x | : | + | -)")
z = str(input(""))
print("")

#code
vysledek_krat = (c1 * c2)
vysledek_deleno = (c1 / c2)
vysledek_plus = (c1 + c2)
vysledek_minus = (c1 - c2)

if z == "x":
    print("")
    print("Výsledek: ")
    print(vysledek_krat)

if z == ":":
    print("")
    print("Výsledek: ")
    print(vysledek_deleno)

if z == "+":
    print("")
    print("Výsledek: ")
    print(vysledek_plus)

if z == "-":
    print("")
    print("Výsledek: ")
    print(vysledek_minus)
