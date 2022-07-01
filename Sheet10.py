def aufgabe1():
    sequence = list(input("Gib eine DNA-Sequenz ein: ").upper())
    dna_alphabet = ['A', 'C', 'G', 'T']

    i = 0
    for base in sequence:
        if base not in dna_alphabet:
            print(base, "an Position", i, "ist nicht Teil des DNA-Alphabets! Möchtest Du das zeichen ignorieren (1) oder ersetzen (2)?")
            query = input("1 oder 2? ")
            if query == '1':        # Zeichen ignorieren
                sequence.pop(i)
            elif query == '2':      # Zeichen ändern
                new_base = 'base'
                while new_base not in dna_alphabet:
                    new_base = input("Wodurch soll das Zeichen ersetzt werden? Gib eine Base ein: ").upper()
                sequence[i] = new_base
        i += 1
    print("Du hast folgende Sequenz eigegeben:", sequence)

    # Basen zählen
    a_count = 0
    c_count = 0
    g_count = 0
    t_count = 0
    for base in sequence:
        if base == 'A':
            a_count += 1
        elif base == 'C':
            c_count += 1
        elif base == 'G':
            g_count += 1
        elif base == 'T':
            t_count += 1
    print("Hier sind die Anzahl Vorkommen pro Base: A=", a_count, ", C=", c_count, ", G=", g_count, ", T=", t_count, sep='')
    # sep='' setzt den 'Seperator' des print-Befehls, so verschwinden die Leerzeichen zwischen den Elementen des prints

    # TATA-Boxen finden
    start_pos_tata = []
    for i in range(0, len(sequence)-3):
        if sequence[i] == 'T':
            if sequence[i+1] == 'A':
                if sequence[i+2] == 'T':
                    if sequence[i+3] == 'A':
                        start_pos_tata.append(i)

    print("An folgenden Positionen startet eine TATA-Box:", start_pos_tata)


def aufgabe2():
    inp = int(input("Gib eine Zahl ein: "))
    if inp < 66:        # a)
        if inp > 1:     # b)
            for i in range(2, int(inp / 2) + 1):
                if (inp % i) == 0:
                    print("No prime number, Dude. Gimme a prime number or you're fired.")
                    break
            else:
                print("Wow. A prime number! You hit the bull's eye!")
    else:
        print("Silly number!")

aufgabe1()
aufgabe2()
