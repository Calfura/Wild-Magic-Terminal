from wild_magic_functions import spell_list, view_character, spells, wild_magic

print("Welcome to the Wild Magic: Sorcerer terminal app")

char_file = "character.csv"
spell_file = "spell.csv"

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
    char_create = open(char_file, "w")
    char_create.write("stats,value\n")
    char_create.close()
    # Creation of spell.csv
    spell_create = open(spell_file, "w")
    spell_create.write("spell,level,learnt\n")
    spell_create.close()
    # Confirmation of file creation
    print("Creating files...")

# Choice for new character or current saved character
def creation():
    print("1. Use current saved character")
    print("2. Create new")
    print("3. Exit")
    user = input("Please select an option: ")
    return user
    
creation_choice = ""

while creation_choice != "3":
    creation_choice = creation()
    if creation_choice == "1":
        # Use saved character set
        break
    elif creation_choice == "2":
        # Create new character set
        break
    else:
        print("Invalid response")

# Main menu navigation for each section
def main_menu():
    # View current character stat sheet
    print("1. View character")
    # View the allowed spell list
    print("2. Spell-list")
    # Current learnt spells
    print("3. Spells")
    # Wild Surge Table
    print("4. Wild Surge!!!")
    # Exit the program
    print("5. Quit")
    user = input("Please selection an option: ")
    return user

users_input = ""

while users_input != "5":
    users_input = main_menu()
    if (users_input) == "1":
        # View current character stats
        view_character()
    elif (users_input) == "2":
        # View allowed spell list
        spell_list()
    elif (users_input) == "3":
        # Current spells learnt
        spells()
    elif (users_input) == "4":
        # Wild magic table
        wild_magic()
    elif (users_input) == "5":
        # Exit program
        continue
    else:
        print("Invalid response")

# Leave Message

print("Thank you for using the Wild Magic: Sorcerer terminal app!!!")