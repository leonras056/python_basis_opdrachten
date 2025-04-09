from my_modules import csv

persons = []
with open("test.csv", 'rt', encoding="utf-8") as file:
    for line in file:
        lst = csv.sanitize(line)
        person = csv.create_person(lst)
        person = csv.add_fullname(person)
        persons.append(person)

print("Alle personen:")
csv.print_persons(persons)

print("\nFilter op achternaam beginnend met 'V':")
filtered_v = csv.do_filter("achternaam", "V", persons)
csv.print_persons(filtered_v)

print("\nFilter op plaats beginnend met 'D':")
filtered_d = csv.do_filter("plaats", "D", persons)
csv.print_persons(filtered_d)
