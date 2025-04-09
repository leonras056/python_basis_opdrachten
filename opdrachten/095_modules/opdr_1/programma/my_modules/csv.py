def sanitize(line):
    new_lst = []
    lst = line.split(',')
    for item in lst:
        new_lst.append(item.lower().strip())
    return new_lst

def create_person(lst):
    person = {
        "voornaam": lst[0],
        "tussenvoegsel": lst[1],
        "achternaam": lst[2],
        "adres": lst[3],
        "postcode": lst[4],
        "plaats": lst[5]
    }
    return person

def add_fullname(person):
    if person["tussenvoegsel"] == "":
        person['full_name'] = f"{person['voornaam'].title()} {person['achternaam'].title()}"
    else:
        person['full_name'] = f"{person['voornaam'].title()} {person['tussenvoegsel']} {person['achternaam'].title()}"
    return person

def print_persons(persons, filter=["full_name"]):
    counter = 0
    for person in persons:
        counter += 1
        for attr in filter:
            print(person[attr].title(), end=" ")
        print(end="\n")
    print(f"Er zijn in totaal {counter} personen")

def do_filter(key, value, data):
    filtered = [person for person in data if person[key].lower().startswith(value.lower())]
    return filtered