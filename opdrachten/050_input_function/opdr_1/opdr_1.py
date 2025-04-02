# Opdracht 1 input function
# Naam student: Ryan
# Groep: IT2B

# Hier komt je code, maak gebruik van de input functie om de lengte van de rechthoekzijden van de driehoek op te vragen.

import math

a = float(input("Geef de lengte van de eerste zijde\n"))
b = float(input("Geef de lengte van de tweede zijde\n"))

c = math.sqrt(a**2 + b**2)

print(f"\nDe lengte van de schuine zijde is: {c}")
