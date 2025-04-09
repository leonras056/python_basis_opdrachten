# Opdracht 2 tekstbestanden
# Naam student: Ryan
# Groep: IT2B

import random

# Genereer een willekeurig getal tussen 1 en 100
geheim_getal = random.randint(1, 100)
aantal_pogingen = 0

# Start de loop voor het raden
while True:
    # Vraag de gebruiker om een getal in te voeren
    gok = int(input("Raad mijn geheime getal\n"))
    aantal_pogingen += 1

    # Controleer of het geraden getal klopt
    if gok == geheim_getal:
        print(f"Je hebt het getal geraden het is {geheim_getal}!")
        print(f"Je hebt het in {aantal_pogingen} keer gedaan")
        break
    elif gok < geheim_getal:
        print("hoger")
    else:
        print("lager")
        