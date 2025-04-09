# Opdracht 1 condities
# Naam student: Ryan
# Groep: IT2B

# Hier komt je code, maak gebruik van de input functie om de lengte van de rechthoekzijden van de driehoek op te vragen.

# Hier start de for-loop....

numbers = []
for i in range(1, 11):
    numbers.append(i)

result = []
for num in numbers:
    if num > 4:
        result.append(num)

print(result)