import csv

new_char_file = [['stat', 'value'],
                 ['STR', ''],
                 ['DEX', ''],
                 ['CON', ''],
                 ['INT', ''],
                 ['CHA', ''],
                 ['WIS', '']]

# Creating a new character
def char_create(file_name):
    with open(file_name, "w") as f:
        writer = csv.writer(f)
        writer.writerows(new_char_file)
    print("=====Character Creation=====")
    # List for coping contents into new character.csv file
    stat_list = []
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            # Skips title,value for input
            if row[1] != "value":
                stat_input = input("Input Stat Value: ")
            # Add's stats line by line to correct Stat types
            if row[1] != "":
                # Copies filled rows for file write
                stat_list.append(row)
            else:
                # Copies name of Stat type and inputs stat value
                stat_list.append([row[0], stat_input])

    with open(file_name, "w") as f:
        writer = csv.writer(f)
        writer.writerows(stat_list)

def view_character(file_name):
    print("=====Character Stats=====")
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