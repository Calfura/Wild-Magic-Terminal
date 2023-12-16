

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
print("1. Use current saved character")
print("2. Create new")



# Options

print("1. View character")
print("2. Spellbook")
print("3. Wild Surge!!!")
print("4. Quit")










# Leave Message

print("Thank you for using the Wild Magic: Sorcerer terminal app!!!")