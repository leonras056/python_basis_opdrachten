# Opdracht 4 Tekst opslaan
# Naam student: Ryan
# Groep: IT2B


# Party enquete

vragen = [
    "Wat is je voornaam?",
    "Wat is je achternaam?",
    "Wat neem je mee aan drank?",
    "Wat neem je mee om te eten?"
]

gasten = []

def voeg_gast_toe():
    gast = {}
    for i, vraag in enumerate(vragen, 1):
        antwoord = input(f"{i}. {vraag} \n> ")
        if i == 1:
            gast["voornaam"] = antwoord
        elif i == 2:
            gast["achternaam"] = antwoord
        elif i == 3:
            gast["drank"] = antwoord
        elif i == 4:
            gast["eten"] = antwoord
    gasten.append(gast)
    print("\nBedankt voor het invullen!")
    print("See you at the party.\n")

def sla_op_in_bestand():
    with open("party_gasten.txt", "a", encoding="utf-8") as bestand:
        for gast in gasten:
            bestand.write("----\n")
            bestand.write(f"voornaam: {gast['voornaam']}\n")
            bestand.write(f"achternaam: {gast['achternaam']}\n")
            bestand.write(f"drank: {gast['drank']}\n")
            bestand.write(f"eten: {gast['eten']}\n\n")

while True:
    voeg_gast_toe()
    nog_een = input("Wil je nog een gast toevoegen? (ja/nee): ").lower()
    if nog_een != "ja":
        break

sla_op_in_bestand()
print("Alle gegevens zijn opgeslagen in 'party_gasten.txt'.")