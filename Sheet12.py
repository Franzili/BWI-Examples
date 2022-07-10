# Aminosäuren

# Liest zwei Aminosäuresequenzen ein und gibt diese zurück
def input_amino_seqs():
    alphabet = "ARNDCQEGHILKMFPSTWYVUO"
    valid_amino_seq = False
    seq_a = ""
    seq_b = ""
    while not valid_amino_seq:
        seq_a = input("Gib eine Sequenz ein: ").upper()
        seq_b = input("Gib eine zweite Sequenz gleicher Länge ein: ").upper()

        # Prüfe, ob die Eingaben valide Aminosäuresequenzen sind
        valid_amino_seq = True
        for char in (seq_a + seq_b):
            if char not in alphabet:
                valid_amino_seq = False
                print("Ups, irgendwas stimmt hier nicht... Ich erwarte Aminosäuren!")
                break
    return seq_a, seq_b


# Wenn die zwei Eingabesequenzen unterschiedlich lang
# wird die länge Sequenz auf die der kürzeren gekürzt
def cut_to_same_len(seq_a, seq_b):
    len_a = len(seq_a)
    len_b = len(seq_b)
    if not (len_a == len_b):
        diff = len_a - len_b
        if diff < 0:    # B ist länger als A
            seq_b = seq_b[:len_b - abs(diff)]
        else:           # A ist länger als B
            seq_a = seq_a[:len_a - diff]
    return seq_a, seq_b


# Gibt den Grad der Übereinstimmung zweier Sequenzen als
# Anzahl übereinstimmender Positionen und prozentual aus
def compare_seqs(seq_a, seq_b):
    num_equal_aminos = 0
    len_seqs = len(seq_a)
    for i in range(0, len_seqs):
        if seq_a[i] == seq_b[i]:
            num_equal_aminos += 1
    print("Die beiden Sequenzen beinhalten", num_equal_aminos,
          "gleiche Aminosäuren, das sind", (num_equal_aminos/len_seqs) * 100, "%.")


# Aufgabe 1
seq_1, seq_2 = input_amino_seqs()
seq_1, seq_2 = cut_to_same_len(seq_1, seq_2)
compare_seqs(seq_1, seq_2)


# Palindrome

# Prüfe, ob eine gegebene Sequenz ein Palindrom einer gegebenen Minimallänge ist
def palicheck(seq, min_len):
    if len(seq) < min_len:
        return False
    return seq == seq[::-1]


# Überprüfe Teilsequenzen einer Sequenz auf Wortpalindrome
def varipalicheck():
    min_len = 0
    max_len = 0
    while min_len < 2 and max_len < 2:
        try:
            min_len = int(input("Minimallänge: "))
            max_len = int(input("Maximallänge: "))
        except Exception:
            print("Es sollten schon Zahlen sein...")

    seq = input("Gib eine Sequenz ein: ")
    palindromes = {}
    for i in range(min_len, max_len + 1):
        pali_len_i = []
        for start_pos in range(0, len(seq)-i-1):
            substring = seq[start_pos:start_pos+i]
            if palicheck(substring, min_len):
                pali_len_i.append(substring)
        if not len(pali_len_i) == 0:
            palindromes[i] = pali_len_i

    print("Folgende Wortpalindrome konnten gefunden werden:\n", palindromes)
    return palindromes


# Aufgabe 2
varipalicheck()


# Bonusaufgabe

# Entfernt kleinere Teilpalindrome aus aus Wortpalindromen in einem gegebenen Dictionary
def bonus(dict_of_palindromes):
    pali_keys = dict_of_palindromes.keys()  # Die Schlüssel im Dict sind die Längen der Palindrome
    for key in pali_keys:
        larger_pali_keys = [k for k in pali_keys if k > key]    # Liste aller keys > key
        for pali in dict_of_palindromes[key]:
            for second_key in larger_pali_keys:     # Vergleich mit längerem Palindrom
                for larger_pali in dict_of_palindromes[second_key]:
                    if pali in larger_pali:
                        # Prüfen, dass wir das Palindrom nicht bereits gelöscht haben
                        if pali in dict_of_palindromes[key]:
                            dict_of_palindromes[key].remove(pali)
    print("Ohne kleinere Teilpalindrome von größeren:\n", dict_of_palindromes)
    return dict_of_palindromes


# Bonusaufgabe
bonus(varipalicheck())
