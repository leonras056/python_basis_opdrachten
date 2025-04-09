# Opdracht 4 condities
# Naam student: Ryan
# Groep: IT2B



toppings = [("olijven", 4.50), ("kaas", 3.50), ("salami", 3.00), ("pepperoni", 2.00) , ("ansjovis", 2.50)]
beschikbare_toppings = ...

keuze = input(f"Maak een keuze uit onze toppings: {beschikbare_toppings} \n")

# Hier de rest van jouw code...

toppings = [("olijven", 4.50), ("kaas", 3.50), ("salami", 3.00), ("pepperoni", 2.00), ("ansjovis", 2.50)]

# Create a list of topping names for display
beschikbare_toppings = [topping[0] for topping in toppings]

# Get user input
keuze = input(f"Maak een keuze uit onze toppings: {beschikbare_toppings}\n")

# Check if the choice exists and get the price
found = False
for topping, prijs in toppings:
    if keuze == topping:
        print(f"U heeft {keuze} besteld. Dat kost {prijs}")
        found = True
        break

if not found:
    print("Uw keuze zit niet in ons assortiment")