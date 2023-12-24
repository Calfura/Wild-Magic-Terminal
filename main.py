import csv
from colored import (fg, attr, bg, style)
from wild_magic_functions import (spell_list, view_character,
                                   spells, wild_magic, char_create, csv_create, attack)
import d20
# from test_functions import test_attack, test_wild_magic

char_file = "character.csv"
spell_file = "spell.csv"
wild_table = "wild_magic_table.csv"
      
try:
    # Checking for exsisting character.csv
    char_load = open(char_file, "r")
    char_load.close()
    # Checking for exsisting spell.csv
    spell_load = open(spell_file, "r")
    spell_load.close()
    # Checking for exsiting wild_magic_table.csv
    wild_table_load = open(wild_table, "r")
    wild_table_load.close
    # Confirmation of found files
    print("Checking files...")
# No CSV's found. Creates required files and data
except FileNotFoundError:
    # Goes straight into Character creation mode
    csv_create(char_file, spell_file, wild_table)
    # Confirmation of file creation
    print("Creating files...")

# Choice for new character or current saved character
def creation():
    # Shows current menu title
    print(f"{style('bold')}{fg('yellow')}{bg('red')}=====Character Menu====={attr('reset')}")
    print("1. Use current saved character")
    print("2. Create new")
    # Allows user to create a new character or use previous character
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
        char_create(char_file, spell_file, wild_table)
        # Breaks loop to begin character creation function
        break
    else:
        # User used incorrect responses, loops user back
        print("Invalid response")

# Main menu navigation for each section
def main_menu():
    # Shows current menu title
    print(f"{style('bold')}{fg('yellow')}{bg('red')}=====Main Menu====={attr('reset')}")
    # View current character stat sheet
    print("1. View character")
    # View the allowed spell list
    print("2. Spell-list")
    # Current learnt spells
    print("3. Spells")
    # Wild Surge Table
    print("4. Wild Surge!!!")
    # Attack Roll
    print("5. Attack")
    # Exits Program
    print("6. Exit")
    # Ask for user input for the above options
    user = input("Please selection an option: ")
    # Returns input response for user_input
    return user

users_input = ""

while users_input != "6":
    users_input = main_menu()
    if (users_input) == "1":
        # View current character stats
        view_character(char_file)
    elif (users_input) == "2":
        # View allowed spell list
        spell_list(spell_file)
    elif (users_input) == "3":
        # Current spells learnt
        spells(spell_file)
    elif (users_input) == "4":
        # Wild magic table
        wild_magic(wild_table)
    elif (users_input) == "5":
        # Attack Command
        attack(spell_file,wild_table)
    elif (users_input) == "6":
        # Exit program
        continue
    else:
        # Incorrect input response. Loops user back
        print("Invalid response")

# Leave Message
print("Thank you for using the Wild Magic: Sorcerer terminal app!!!")