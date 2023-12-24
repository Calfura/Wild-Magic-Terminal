# Wild Magic - Sorcerer Terminal Application

## Description

Terminal application for the archetype of Wild Magic Sorcerer's, where it will roll on the d100 table of Wild Magic to determine what Wild Surge is casted. The terminal application will check if the spell casted was a cantrip(base level spell) or if it is a 1st level spell. It then will proceede to roll to check if a Wild Surge happens, outputs if the Surge does not occur or if the Surge occured. If a Surge occurs, it will roll on the d100 table and print out the Surge effect that happened (with possible additional rolls added).

The application will hold basic information about the character stats to use as modifiers for spells casted. A basic spell list will be used/added for the terminal application (as there are far to many spells to add, check and work on within a short amount of time). On first use, the app will create the additional csv files needed to record any data to be used as well as a way to delete old 'saved' files, so the user can add in new character data when appropriate. Additional development will continue to include additional levels, spells and possible archetypes in future.

## References

Neumeyer. A, 2023, A Proven Test Plan Template for Software Testing (Excel), _A proven test plan template for Excel_, web blog post, viewed 26 December 2023, https://www.tacticalprojectmanager.com/test-case-template-excel-with-example/

D20, Dice rolling module, DnD-Beyond, https://github.com/avrae/d20

Rossum. G, Warsaw. B, Coghlan A, 2001, PEP 8 – Style Guide for Python Code, viewed 19 December, https://peps.python.org/pep-0008/

## GitHub

https://github.com/Calfura/Wild-Magic-Terminal

## Features

### Spell Book

Allows the user to store information on spells that the character has learnt on an approved spell list (upto 1st level spells). CSV file will contain the spell name, spell level, if the spell is known or not and the dice required for the roll. Feature will show a list of choices to show the known spells in a print format listing from Cantrips to 1st Level spells. A seperate function will handle the spell list of approved spells that can be learnt within the program. Additional spells will be added to the program as development continues.

```py
def spells(file_name):
    print(f"{style('bold')}{fg('yellow')}{bg('red')}=====Spellbook====={attr('reset')}")
    # Allows adding of spells into Spellbook
    print("1. Show Spells")
    print("2. Add Spells")
    print("3. Back")
    spell_choice = ""
    # Asks the user for an input
    spell_choice = input("Please select an option: ")
    # Allows the user to show their Spell Book, Add Spells or go back
    while spell_choice != "3":
        if spell_choice == "1":
            # Prints out the Spellbook for the user to see
            print(f"{style('bold')}{fg('yellow')}{bg('red')}=====Known Spells====={attr('reset')}\n")
            with open(file_name, "r") as f:
                reader = csv.reader(f)
                # Skips title line for print
                reader.__next__()
                for row in reader:
                    # Checking for if the spell is learnt by the character or not
                    if row[2] == "True":
                        print(f"{row[0]} | {row[1]}")
                break
        elif spell_choice == "2":
            # Asks for spell name to learn
            spell_name = input("Add choosen spell: ")
            # Tuple list for updated spell.csv
            spell_update = []
            with open(file_name, "r") as f:
                reader = csv.reader(f)
                # Checking for spell name in spell.csv
                for row in reader:
                    # Checks and adds into tuple if not chosen spell
                    if (spell_name != row[0]):
                        spell_update.append(row)
                    # Updates spell to being learnt "True"
                    else:
                        spell_update.append([row[0], row[1], "True", row[3]])
            # Writes the new .csv file to include the newly added spell
            with open(file_name, "w") as f:
                writer = csv.writer(f)
                writer.writerows(spell_update)
            break
```

### Character Creation

Will create all required CSV files apond program launch, when New Character is selected it will overwrite the previous files with fresh ones. When creating a new character it will allow the user to set their stat values for each stat type (STR,DEX,CON,INT,CHA,WIS) and the program will set their modifiers automatically to the correct values (n / 2 - 5 , rounded down for whole value)

```py
def char_create(file1, file2, file3):
    csv_create(file1, file2, file3)
    print(f"{style('bold')}{fg('yellow')}{bg('red')}=====Character Creation====={attr('reset')}")
    # List for coping contents into new character.csv file
    stat_list = []
    with open(file1, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            # Skips title,value for input
            if row[1] != "value":
                stat_input = input(f"{row[0]} | Input Stat Value(1-20): ")
                # Math for modifier for each stat type
                # Always rounding down to get correct modifier
                mod_sum = floor(int(stat_input) / 2)
                # Divide the Total by 2 then reduce by 5 for correct value
                mod = mod_sum - 5
            # Add's stats line by line to correct Stat types
            if row[1] != "":
                # Copies filled rows for file write
                stat_list.append(row)
            else:
                # Copies name of Stat type and inputs stat value
                stat_list.append([row[0], stat_input, mod])
    # Rewrites Character stat file
    with open(file1, "w") as f:
        writer = csv.writer(f)
        writer.writerows(stat_list)
```

### Wild Surge

Main feature of the program. CSV containing the table from the Wild Magic Table (1-100) with the effects of each Surge and any rolls that occur with the Wild Surge effect. The user will have a attack command that will let them use any known spells from their spell book (user will input the spell name), it will do the roll for the attack then checks the level of the spell. Any spell of 1st Level will then have a d20 roll to check for a 1. Each roll will print out the roll value and notify if a Wild Surge occured. On Wild Surge success (fail in D&D), it will then roll on the Wild Magic Table (d100) print out the effect and do any additional rolling required for the outcome to complete.

```py
def attack(file1, file2):
    print("=====Attack Menu=====")
    print("1. Spell Book")
    print("2. Back")
    # Asks the user to select an option from above
    user_choice = input("Please select option: ")
    # Opens Spell Book and allows user to cast the selected spell
    while user_choice != "2":
        if user_choice == "1":        
            print("=====Spell Book=====")
            spell_choice = ""
            # Asks user for input
            spell_choice = input("Choose an attack: ")
            with open(file1, "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    # Checking for known spell in spell book
                    if (spell_choice == row[0]):
                        # Fetches the dice roll for spell
                        num = (f"{row[3]}")
                        # Rolls Dice
                        r = d20.roll(num)
                        # Prints out total damage from spell
                        print(f"Damage: {r.total}")
                        # Checking if spell is 1st level
                        if row[1] == "1st Level":
                            # Rolls a d20 to check for wild surge
                            wild_n = ("1d20")
                            wild_r = d20.roll(wild_n)
                            # If dice roll is 1, wild surge will occur
                            if (wild_r.total == 1):
                                print(f"Roll: {wild_r.total}")   
                                print("Wild Surge!!!")
                                # Runs wild_magic function on fail
                                wild_magic(file2)
                            # If dice roll is not 1, executes else block
                            else:
                                print(f"Roll: {wild_r.total}")
                                print("No Wild Surge")
        # Stops the loop and returns to main menu
        break
```

## Design (R8)

