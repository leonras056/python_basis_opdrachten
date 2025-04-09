# Opdracht 1 functies
# Naam student: Ryan
# Groep: IT2B


def volledige_naam(lijst_met_namen):
    for naam in lijst_met_namen:
        tussenvoegsel = naam["tussenvoegsel"]
        if tussenvoegsel:
            print(f"{naam['voornaam']} {tussenvoegsel} {naam['achternaam']}")
        else:
            print(f"{naam['voornaam']} {naam['achternaam']}")

namen = [
    {"voornaam": "Willem", "tussenvoegsel": "van", "achternaam": "Dijk"},
    {"voornaam": "Klaas", "tussenvoegsel": "", "achternaam": "Wopstra"},
    {"voornaam": "Miep", "tussenvoegsel": "van der", "achternaam": "Plas"},
    {"voornaam": "Carla", "tussenvoegsel": "", "achternaam": "Hoogvliet"},
]

volledige_naam(namen)