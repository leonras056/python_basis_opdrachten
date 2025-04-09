# Opdracht 3 Tekst opslaan
# Naam student: Ryan
# Groep: IT2B


# Functie om een tekst te encrypten
def encrypt(text):
    encrypted_text = ""
    for char in text:
        # Controleer of het een letter is
        if char.isalpha():
            # Bepaal de basis (A voor hoofdletters, a voor kleine letters)
            base = ord('A') if char.isupper() else ord('a')
            # Verschuif de letter 5 plaatsen in het alfabet
            new_pos = (ord(char) - base + 5) % 26 + base
            encrypted_text += chr(new_pos)
        else:
            # Behoud niet-letters (zoals spaties en leestekens)
            encrypted_text += char
    return encrypted_text

# Vraag de gebruiker om invoer
text = input("Geef de tekst die wilt encrypten..\n")

# Encrypt de tekst en print het resultaat
encrypted = encrypt(text)
print(encrypted)
