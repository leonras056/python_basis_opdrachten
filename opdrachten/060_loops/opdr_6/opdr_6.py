# Opdracht 3 input functie
# Naam student: Ryan
# Groep:IT2B

# Hier komt je code...

# Hier start de for-loop

pizzas = ['margharita', 'calzone', 'verdi', 'olivio', 'quattro stagioni']

# Sort the list alphabetically
pizzas.sort()
print(pizzas)

# Add a new pizza
pizzas.append('yo-favorito')
print(pizzas)

# Remove the least favorite pizza
pizzas.remove('calzone')
print(pizzas)

# Print the first 3 pizzas
print(pizzas[:3])

# Print the middle pizza
middle_index = len(pizzas) // 2
print([pizzas[middle_index]])

# Print the last 3 pizzas
print(pizzas[-3:])