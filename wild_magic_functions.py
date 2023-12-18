import csv
from colored import (fg, attr, bg, style)

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
    print(f"{style('bold')}{fg('yellow')}{bg('red')}=====Character Creation====={attr('reset')}")
    # List for coping contents into new character.csv file
    stat_list = []
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            # Skips title,value for input
            if row[1] != "value":
                stat_input = input("Input Stat Value(1-20): ")
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
    print(f"{style('bold')}{fg('yellow')}{bg('red')}=====Character Stats====={attr('reset')}")
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        reader.__next__()
        for row in reader:
            # Reading out Character stats
            print(f"{row[0]} | {row[1]}")

# Gives a list of allowed spells to be used.
def spell_list(file_name):
    print(f"{style('bold')}{fg('yellow')}{bg('red')}=====Spell-list====={attr('reset')}\n")
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        reader.__next__()
        for row in reader:
            # Checking if spell is learnt (True)
            # Prints out spell name and level
            # if (row[2] == "True"):
                print(f"{row[0]} | {row[1]}")
            # else:
            #     # continues the loop for the next spell
            #     continue


def spells(file_name):
    print(f"{style('bold')}{fg('yellow')}{bg('red')}=====Spellbook====={attr('reset')}")
    # Allows adding of spells into Spellbook
    print("1. Show Spells")
    print("2. Add Spells")
    print("3. Exit")
    spell_choice = ""
    spell_choice = input("Please select an option: ")
    while spell_choice != "3":
        if spell_choice == "1":
            # Prints out the Spellbook for the user to see
            with open(file_name, "r") as f:
                reader = csv.reader(f)
                reader.__next__()
                for row in reader:
                    print(f"{row[0]} | {row[1]}")
            break
        elif spell_choice == "2": 
            # Adding spells
            # def add_spell():
            #     # Check condition list for allowed spells.
            #     spell_add = input("Please add a spell: ")
            #     spell_level = input("The spell's level: ")
            #     with open(spell_file, "a") as f:
            #         writer = csv.writer(f)
            #         writer.writerow([spell_add, spell_level, True])
            with open(file_name, "a") as f:
                spell_name = input("Add choosen spell: ")
                writer = csv.writer(f)
                writer.writerow([spell_name, "Known"])
            break

# Used for Wild Surge
def wild_magic():
    print("Wild Magic Check")

# Dice roll (?)
def roll():
    pass