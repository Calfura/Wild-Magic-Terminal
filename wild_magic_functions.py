import csv
from colored import (fg, attr, bg, style)
import d20
from math import floor

new_char_file = [['stat', 'value', 'mod'],
                 ['STR', '', ''],
                 ['DEX', '', ''],
                 ['CON', '', ''],
                 ['INT', '', ''],
                 ['CHA', '', ''],
                 ['WIS', '', '']]

wild_magic_table = [['num1', 'num2', 'effect', 'dice'],
                    ['1', '2', 'Roll on this table at the start of each of your turns for the next minute. Ignoring this result on subsequent rolls', '0'],
                    ['3', '4', 'For the next minute. You can see any invisible creature if you have line of sight to it', '0'],
                    ['5', '6', 'A modron chosen and controlled by the DM appears in an unoccupied space within 5 feet of you. Then disappears I minute later', '0'],
                    ['7', '8', 'You cast Fireball as a 3rd-level spell centered on yourself', '8d6'],
                    ['9', '10', 'You cast Magic Missile as a 5th-level spell', '5d4+1'],
                    ['11', '12', 'Roll a d10. Your height changes by a number of inches equal to the roll. If the roll is odd you shrink. If the roll is even you grow', '1d10'],
                    ['13', '14', 'You cast Confusion centered on yourself', '0'],
                    ['15', '16', 'For the next minute. You regain 5 hit points at the start of each of your turns', '0'],
                    ['17', '18', 'You grow a long beard made of feathers that remains until you sneeze. At which point the feathers explode out from your face', '0'],
                    ['19', '20', 'You cast Grease centered on yourself', '0']]

spell_book = [['spell', 'level', 'learnt', 'dice'],
                ['Fire Bolt', 'Cantrip','False', '1d10'],
                ['Chill Touch', 'Cantrip', 'False', '1d8'],
                ['Ray of Frost', 'Cantrip', 'False', '1d8'],
                ['Burning Hands', '1st Level', 'False', '3d6'],
                ['Color Spray', '1st Level', 'False', '6d10'],
                ['Sleep', '1st Level', 'False', '5d8']]

def csv_create(file1, file2, file3):
    # Creates all required CSV files needed
    with open(file1, "w") as f:
        # Character Stat block creation
        writer = csv.writer(f)
        writer.writerows(new_char_file)
    with open(file2,"w") as f:
        # Spell Book creation
        writer = csv.writer(f)
        writer.writerows(spell_book)
    with open(file3, "w") as f:
        # Wild Magic Table creation
        writer = csv.writer(f)
        writer.writerows(wild_magic_table)

# Creating a new character
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

def view_character(file_name):
    print(f"{style('bold')}{fg('yellow')}{bg('red')}=====Character Stats====={attr('reset')}")
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        reader.__next__()
        for row in reader:
            # Reading out Character stats
            print(f"{row[0]} | {row[1]} | {row[2]}")

# Gives a list of allowed spells to be used.
def spell_list(file_name):
    print(f"{style('bold')}{fg('yellow')}{bg('red')}=====Spell-list====={attr('reset')}\n")
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        reader.__next__()
        for row in reader:
                print(f"{row[0]} | {row[1]}")

def spells(file_name):
    print(f"{style('bold')}{fg('yellow')}{bg('red')}=====Spellbook====={attr('reset')}")
    # Allows adding of spells into Spellbook
    print("1. Show Spells")
    print("2. Add Spells")
    print("3. Back")
    spell_choice = ""
    spell_choice = input("Please select an option: ")
    while spell_choice != "3":
        if spell_choice == "1":
            # Prints out the Spellbook for the user to see
            print(f"{style('bold')}{fg('yellow')}{bg('red')}=====Known Spells====={attr('reset')}\n")
            with open(file_name, "r") as f:
                reader = csv.reader(f)
                reader.__next__()
                for row in reader:
                    if row[2] == "True":
                        print(f"{row[0]} | {row[1]}")
                break
        elif spell_choice == "2": 
            spell_name = input("Add choosen spell: ")
            spell_update = []
            with open(file_name, "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    if (spell_name != row[0]):
                        spell_update.append(row)
                    else:
                        spell_update.append([row[0], row[1], "True", row[3]])
            with open(file_name, "w") as f:
                writer = csv.writer(f)
                writer.writerows(spell_update)
            break

# Used for Wild Surge
def wild_magic(file_name):
    with open(file_name) as f:
        reader = csv.reader(f)
        # Rolls on the Wild Magic Table
        sample_roll = d20.roll("d20")
        # F string required output for D20 module
        sample_num = (f"{sample_roll.total}")
        
        for row in reader:
            if (sample_num == row[0]):
                print(f"{row[0]} - {row[1]} | {row[2]}")
                if row[3] != "0":
                    # Convert into f-string to allow d20 to pull from CSV file
                    num = (f"{row[3]}")
                    # Rolls from predetermine list inside CSV file
                    r = d20.roll(num)
                    # Prints total of dice value
                    print(r.total)
                break
            elif (sample_num == row[1]):
                print(f"{row[0]} - {row[1]} | {row[2]}")
                if row[3] != "0":
                    # Convert into f-string to allow d20 to pull from CSV file
                    num = (f"{row[3]}")
                    # Rolls from predetermine list inside CSV file
                    r = d20.roll(num)
                    print(r)
                break

def attack_roll():
    pass
