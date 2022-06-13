x = input("1. Zahl: ")      # liest die erste Zahl als Zeichenkette ein und speichert sie in der neuen Variable x
y = input("2. Zahl: ")      # liest die zweite Zahl als Zeichenkette ein und speichert sie in der neuen Variable y
x = int(x)                  # Umwandeln der Zeichenketten in Zahlen vom Datentyp int
y = int(y)                  # Umwandeln der Zeichenketten in Zahlen vom Datentyp int
while x > 0:                # Solange x > 0 ist ...
    if x < y:               # Ist x < y, dann vertausche x und y
        h = x               # speichere den Wert von x in h zwischen
        x = y               # weise x den Wert von y zu ...
        y = h               # ... und y den in h zwischengespeicherten Wert von x zu
    x = x - y               # Weise x die Differenz zwischen x und y zu
print("Der ggT ist:", y)
