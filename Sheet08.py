x_str = input("1. Zahl:")
y_str = input("2. Zahl:")
x = int(x_str)
y = int(y_str)

if x < 0 or y < 0:
    x = abs(x)
    y = abs(y)
    print("Um den ggT dieser Zahlen zu berechnen, wird hier der Betrag genommen: x = " + str(x) + ", y = " + str(y))

durchlauf = 0
while x > 0:
    if x < y:
        h = x
        x = y
        y = h
    x = x - y
    durchlauf += 1
    print(str(durchlauf) + ". Schleifendurchlauf")

print("Der ggT von " + x_str + " und " + y_str + " ist " + str(y) + ".")
print("Die Berechnung hat " + str(durchlauf) + " Schleifendurchläufe gebraucht.")
