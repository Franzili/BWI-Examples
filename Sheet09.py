# Aufgabe 1

fertig = False
while not fertig:
    fertig = True
    x = float(input("Gib eine Zahl ein: "))             # 3
    op = input("Gib eine Rechenoperation ein: ")        # *
    y = float(input("Gib eine weitere Zahl ein: "))     # 4
    if op == '+':
        print("Das Ergebnis ist", x + y)
    elif op == '-':
        print("Das Ergebnis ist", x - y)
    elif op == '*':
        print("Das Ergebnis ist", x * y)
    elif op == '/':
        print("Das Ergebnis ist", x / y)
    else:
        print("Der Operand ist ungültig, versuchs nochmal.")
        fertig = False


# Aufgabe 2

tagesliste = ["Nudeln", "Quark", "Eier", "Eis", "Tomaten", "Basilikum", "Nudeln", "Oregano", "Pizzateig", "Käse", "Nudeln"]
monatsliste = ["Toilettenpapier", "Zahnbürste", "Duschgel", "Shampoo", "Taschentücher"]

# 1.
neue_liste = tagesliste + monatsliste

# 2.
neue_liste.count("Nudeln")

# 3.
neue_liste = list(set(neue_liste))

# 4.
neue_liste.append("Nutella")

# 5.
neue_liste.remove("Oregano")
neue_liste.remove("Pizzateig")

# 6.
forgotten_items = ["Quark", "Eier"]

# 7.
tagesliste = forgotten_items