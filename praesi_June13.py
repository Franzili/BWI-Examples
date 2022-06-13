basis_urlaub = ["Zahnbürste", "Zahnpaste", "Unterwäsche", "Ladegerät", "Handtücher", "Kosmetikartikel"]
sommer_urlaub = ["kurze Hosen", "t-shirt", "Sommerkleid", "Sonnencreme", "Schwimmsachen"]
winter_urlaub = ["Pullover", "Winterjacke", "Schal", "Handschuhe"]
koffer = []
koffer.extend(basis_urlaub)

while(True):
    urlaub_art = input("Welchen Urlaub wollen Sie planen? ")
    if urlaub_art == "sommer" or urlaub_art == "Sommer":
        koffer.extend(sommer_urlaub)
        break
    elif urlaub_art == "winter" or urlaub_art == "Winter":
        koffer.extend(winter_urlaub)
        break
    else:
        print("Diese Art von Urlaub kenne ich nicht, bitte nochmal eingeben")
print("Ihr Koffer hat folgende Dinge:")
print(koffer)
while(True):
    hinzufuegen = input("Möchten sie weitere Gegenstände hinzufügen? ")
    if hinzufuegen == "Ja" or hinzufuegen == "ja":
        koffer.append(input("Geben Sie den Namen des Gegenstandes ein: "))
    else:
        break

print("Ihr Koffer hat jetzt folgende Dinge:")
koffer.sort()
print(koffer)
gegenstand = input("Wollen Sie einen Gegenstand entfernen? Falls ja geben sie einen Gegenstand ein: ")
if gegenstand in koffer:
    koffer.remove(gegenstand)
zweiter_koffer = koffer.copy()
koffer.remove("Unterwäsche")
print(koffer, zweiter_koffer)
