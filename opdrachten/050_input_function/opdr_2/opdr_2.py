# Opdracht 2 berekeningen
# Naam student: Ryan
# Groep: IT2B

# Hier komt je code...

gasten = []

gasten.append("Jij")
gasten.append("Paul")
gasten.append("Kees")
gasten.append("Marie")
gasten.append("Hilda")

print(gasten)

gasten.remove("Marie")
print(gasten)

kees_index = gasten.index("Kees")
gasten.insert(kees_index + 1, "George")

print(gasten)