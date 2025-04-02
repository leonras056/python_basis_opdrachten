# Opdracht 3 input functie
# Naam student: Ryan
# Groep: IT2B

# Hier komt je code...

lijst = []

for i in range(5):
    item = input("Vul een item in: ")
    lijst.append(item)

lijst.sort(reverse=True)
print(lijst)
