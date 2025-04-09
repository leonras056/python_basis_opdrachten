# Opdracht 3 condities
# Naam student: Ryan
# Groep: IT2B




normale_toegangsprijs = 12.50
kortings_percentages = {"baby": 100, "kinderen": 50, "volwassenen": 0, "ouderen": 30}
leeftijd = {"baby": (0, 2), "kinderen": (3, 18), "volwassenen": (19, 64), "ouderen": (65, 150)}

# Hier komt je code...
# Given data
normal_access_price = 12.50
discount_percentages = {"baby": 100, "kinderen": 50, "volwassenen": 0, "ouderen": 30}
age_groups = {"baby": (0, 2), "kinderen": (3, 18), "volwassenen": (19, 64), "ouderen": (65, 150)}

# Get age input from user
age = int(input("Geef uw leeftijd in aantal jaar: "))

# Determine the age group
group = None
for category, (min_age, max_age) in age_groups.items():
    if min_age <= age <= max_age:
        group = category
        break

# Calculate discount and final price
print(f"U behoort tot de groep {group}")
discount = discount_percentages[group]
print(f"U krijgt {discount}% korting")
final_price = normal_access_price * (1 - discount / 100)
print(f"U betaalt daarom {final_price}")