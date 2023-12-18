import csv
from colored import (fg, attr, bg, style)
from wild_magic_functions import (spell_list, view_character,
                                   spells, wild_magic, char_create)
import d20
from test_functions import wild_magic


char_file = "character.csv"
spell_file = "spell.csv"
allowed_spells = "spell_list.csv"
wild_table = "wild_magic_table.csv"

try:
    # Checking for exsisting character.csv
    char_load = open(char_file, "r")
    char_load.close()
    # Checking for exsisting spell.csv
    spell_load = open(spell_file, "r")
    spell_load.close()
    # Confirmation of found files
    print("Checking files...")
except FileNotFoundError:
    # Creation of character.csv
    character_create = open(char_file, "w")
    character_create.write("stats,value\n")
    character_create.close()
    # Creation of spell.csv
    spell_create = open(spell_file, "w")
    spell_create.write("spell,level,learnt\n")
    spell_create.close()
    # Confirmation of file creation
    print("Creating files...")

# Choice for new character or current saved character
def creation():
    print(f"{style('bold')}{fg('yellow')}{bg('red')}=====Character Menu====={attr('reset')}")
    print("1. Use current saved character")
    print("2. Create new")
    user = input("Please select an option: ")
    return user
    
creation_choice = ""

while creation_choice != "1":
    creation_choice = creation()
    if creation_choice == "1":
        # Use saved character set | Stops error
        break
    elif creation_choice == "2":
        # Create new character set
        char_create(char_file)
        break
    else:
        print("Invalid response")

# Main menu navigation for each section
def main_menu():
    print(f"{style('bold')}{fg('yellow')}{bg('red')}=====Main Menu====={attr('reset')}")
    # View current character stat sheet
    print("1. View character")
    # View the allowed spell list
    print("2. Spell-list")
    # Current learnt spells
    print("3. Spells")
    # Wild Surge Table
    print("4. Wild Surge!!!")
    # Exit the program
    print("5. Exit Program")
    user = input("Please selection an option: ")
    return user

users_input = ""

while users_input != "5":
    users_input = main_menu()
    if (users_input) == "1":
        # View current character stats
        view_character(char_file)
    elif (users_input) == "2":
        # View allowed spell list
        spell_list(allowed_spells)
    elif (users_input) == "3":
        # Current spells learnt
        spells(spell_file)
    elif (users_input) == "4":
        # Wild magic table
        wild_magic(wild_table)
    elif (users_input) == "5":
        # Exit program
        continue
    else:
        print("Invalid response")

# Leave Message

print("Thank you for using the Wild Magic: Sorcerer terminal app!!!")