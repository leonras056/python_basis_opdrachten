# Opdracht 1 functies
# Naam student: Ryan
# Groep: IT2B



def write_to_file(afile, atext):
    with open(afile, "a", encoding="utf-8") as f:
        f.write(atext + "\n")

my_tekst = "Schrijf dit maar even in een bestandje"
my_file = "test.txt"
write_to_file(my_file, my_tekst)