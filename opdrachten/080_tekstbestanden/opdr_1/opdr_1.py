# Opdracht 1 while-loops
# Naam student: Ryan
# Groep: IT2B

# Jouw code komt hier

# Vragen stellen en antwoorden opslaan
vraag1 = input("Wat vind je van de huidige regering?\n")
vraag2 = input("Wat vind je van de Python-lessen tot nu toe?\n")
vraag3 = input("Wat vind jij de mooiste stad van Nederland?\n")

# Resultaten opslaan in een tekstbestand
with open("enquete_resultaten.txt", "w") as bestand:
    bestand.write("Enquete Resultaten\n")
    bestand.write("=================\n")
    bestand.write(f"Vraag 1: Wat vind je van de huidige regering?\nAntwoord: {vraag1}\n\n")
    bestand.write(f"Vraag 2: Wat vind je van de Python-lessen tot nu toe?\nAntwoord: {vraag2}\n\n")
    bestand.write(f"Vraag 3: Wat vind jij de mooiste stad van Nederland?\nAntwoord: {vraag3}\n")

