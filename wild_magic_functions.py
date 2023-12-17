import csv

# Creating a new character
def create():
    pass

def view_character(file_name):
    print("=====Character Stats====")
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        reader.__next__()
        for row in reader:
            # Reading out Character stats
            print(f"{row[0]} | {row[1]}")

# Gives a list of allowed spells to be used.
def spell_list(file_name):
    print("=====Spell-list=====\n")
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        reader.__next__()
        for row in reader:
            # Checking if spell is learnt (True)
            # Prints out spell name and level
            if (row[2] == "True"):
                print(f"{row[0]}, {row[1]}")
            else:
                # continues the loop for the next spell
                continue


def spell_add():
    print("Spells Check")

# Adding spells
# def add_spell():
#     # Check condition list for allowed spells.
#     spell_add = input("Please add a spell: ")
#     spell_level = input("The spell's level: ")
#     with open(spell_file, "a") as f:
#         writer = csv.writer(f)
#         writer.writerow([spell_add, spell_level, True])
    
# Viewing of spells learnt
def spells():
    print("Spells check")


# Used for Wild Surge
def wild_magic():
    print("Wild Magic Check")

# Dice roll (?)
def roll():
    pass