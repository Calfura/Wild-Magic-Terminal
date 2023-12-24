import csv
from colored import (fg, attr, bg, style)
import d20
from math import floor

# Character Stat table data for CSV creation
new_char_file = [['stat', 'value', 'mod'],
                 ['STR', '', ''],
                 ['DEX', '', ''],
                 ['CON', '', ''],
                 ['INT', '', ''],
                 ['CHA', '', ''],
                 ['WIS', '', '']]

# Wild Magic table data for CSV creation
wild_magic_table = [["num1","num2","effect","dice"],
                    ["1","2","Roll on this table at the start of each of your turns for the next minute. Ignoring this result on subsequent rolls","0"],
                    ["3","4","For the next minute. You can see any invisible creature if you have line of sight to it","0"],
                    ["5","6","A modron chosen and controlled by the DM appears in an unoccupied space within 5 feet of you. Then disappears I minute later","0"],
                    ["7","8","You cast Fireball as a 3rd-level spell centered on yourself","8d6"],
                    ["9","10","You cast Magic Missile as a 5th-level spell","5d4+1"],
                    ["11","12","Roll a d10. Your height changes by a number of inches equal to the roll. If the roll is odd you shrink. If the roll is even you grow","1d10"],
                    ["13","14","You cast Confusion centered on yourself","0"],
                    ["15","16","For the next minute. You regain 5 hit points at the start of each of your turns","0"],
                    ["17","18","You grow a long beard made of feathers that remains until you sneeze. At which point the feathers explode out from your face","0"],
                    ["19","20","You cast Grease centered on yourself","0"],
                    ["21","22","Creatures have disadvantage on saving throws against the next spell you cast in the next minute that involves a saving throw","0"],
                    ["23","24","Your skin turns a vibrant shade of blue. A Remove Curse spell can end this effect","0"],
                    ["25","26","An eye appears on your forehead for the next minute. During that time you have advantage on Wisdom (Perception) checks that rely on sight","0"],
                    ["27","28","For the next minute. All your spells with a casting time of 1 action have a casting time of 1 bonus action","0"],
                    ["29","30","You teleport up to 60 feet to an unoccupied space of your choice that you can see","0"],
                    ["31","32","You are transported to the Astral Plane until the end of your next turn. After which time you return to the space you previously occupied or the nearest unoccupied space if that space is occupied","0"],
                    ["33","34","Maximize the damage of the next damaging spell you cast within the next minute","0"],
                    ["35","36","Roll a d10. Your age changes by a number of years equal to the roll. If the roll is odd you get younger (minimum 1 year old). If the roll is even you get older","1d10"],
                    ["37","38","1d6 flumphs controlled by the DM appear in unoccupied spaces within 60 feet of you and are frightened of you. They vanish after 1 minute","1d6"],
                    ["39","40","You regain 2d10 hit points","2d10"],
                    ["41","42","You turn into a potted plant until the start of your next turn. While a plant you are incapacitated and have vulnerability to all damage. If you drop to 0 hit points your pot breaks and your form reverts","0"],
                    ["43","44","For the next minute you can teleport up to 20 feet as a bonus action on each of your turns","0"],
                    ["45","46","You cast Levitate on yourself","0"],
                    ["47","48","A unicorn controlled by the DM appears in a space within 5 feet of you then disappears 1 minute later","0"],
                    ["49","50","You can't speak for the next minute. Whenever you try pink bubbles float out of your mouth","0"],
                    ["51","52","A spectral shield hovers near you for the next minute. Granting you a +2 bonus to AC and immunity to Magic Missile","0"],
                    ["53","54","You are immune to being intoxicated by alcohol for the next 5d6 days","5d6"],
                    ["55","56","Your hair falls out but grows back within 24 hours","0"],
                    ["57","58","For the next minute. Any flammable object you touch that isn't being worn or carried by another creature bursts into flame","0"],
                    ["59","60","You regain your lowest-level expended spell slot","0"],
                    ["61","62","For the next minute you must shout when you speak","0"],
                    ["63","64","You cast Fog Cloud centered on yourself","0"],
                    ["65","66","Up to three creatures you choose within 30 feet of you take 4d10 lightning damage","4d10"],
                    ["67","68","You are frightened by the nearest creature until the end of your next turn","0"],
                    ["69","70","Each creature within 30 feet of you becomes invisible for the next minute. The invisibility ends on a creature when it attacks or casts a spell","0"],
                    ["71","72","You gain resistance to all damage for the next minute","0"],
                    ["73","74","A random creature within 60 feet of you becomes poisoned for 1d4 hours","1d4"],
                    ["75","76","You glow with bright light in a 30-foot radius for the next minute. Any creature that ends its turn within 5 feet of you is blinded until the end of its next turn","0"],
                    ["77","78","You cast Polymorph on yourself. If you fail the saving throw you turn into a sheep for the spell's duration","0"],
                    ["79","80","Illusory butterflies and flower petals flutter in the air within 10 feet of you for the next minute","0"],
                    ["81","82","You can take one additional action immediately","0"],
                    ["83","84","Each creature within 30 feet of you takes 1d10 necrotic damage. You regain hit points equal to the sum of the necrotic damage dealt","1d10"],
                    ["85","86","You cast Mirror Image","0"],
                    ["87","88","You cast Fly on a random creature within 60 feet of you","0"],
                    ["89","90","You become invisible for the next minute. During that time other creatures can't hear you. The invisibility ends if you attack or cast a spell","0"],
                    ["91","92","If you die within the next minute. You immediately come back to life as if by the Reincarnate spell","0"],
                    ["93","94","Your size increases by one size category for the next minute","0"],
                    ["95","96","You and all creatures within 30 feet of you gain vulnerability to piercing damage for the next minute","0"],
                    ["97","98","You are surrounded by faint ethereal music for the next minute","0"],
                    ["99","100","You regain all expended sorcery points","0"]]

# Spell table data for CSV creation
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
    # Calls csv_create to reset csv's to default
    csv_create(file1, file2, file3)
    # Shows current menu title
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
    # Shows current menu title
    print(f"{style('bold')}{fg('yellow')}{bg('red')}=====Character Stats====={attr('reset')}")
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        # Skips title line
        reader.__next__()
        for row in reader:
            # Reading out Character stats
            print(f"{row[0]} | {row[1]} | {row[2]}")

# Gives a list of allowed spells to be used.
def spell_list(file_name):
    # Shows current menu title
    print(f"{style('bold')}{fg('yellow')}{bg('red')}=====Spell-list====={attr('reset')}\n")
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        # Skips title line
        reader.__next__()
        for row in reader:
                # Prints out allowed spell list for user
                print(f"{row[0]} | {row[1]}")

def spells(file_name):
    # Shows current menu title
    print(f"{style('bold')}{fg('yellow')}{bg('red')}=====Spellbook====={attr('reset')}")
    # Allows adding of spells into Spellbook
    print("1. Show Spells")
    print("2. Add Spells")
    print("3. Back")
    spell_choice = ""
    # User chooses from list above
    spell_choice = input("Please select an option: ")
    while spell_choice != "3":
        if spell_choice == "1":
            # Shows current menu title
            # Prints out the Spellbook for the user to see
            print(f"{style('bold')}{fg('yellow')}{bg('red')}=====Known Spells====={attr('reset')}\n")
            with open(file_name, "r") as f:
                reader = csv.reader(f)
                # Skips title line
                reader.__next__()
                for row in reader:
                    # Checks if spell is learnt
                    if row[2] == "True":
                        # Prints out spell name | spell level
                        print(f"{row[0]} | {row[1]}")
                # Breaks loop cycle to continue to main menu
                break
        elif spell_choice == "2":
            # Asks user for input
            spell_name = input("Add choosen spell: ")
            # Tuple for updating file
            spell_update = []
            with open(file_name, "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    # Checks for input and appends into spell_update
                    if (spell_name != row[0]):
                        spell_update.append(row)
                    # If false, updates chosen spell to being learned ("True")
                    else:
                        spell_update.append([row[0], row[1], "True", row[3]])
            # Rewrites spell file with updated list
            with open(file_name, "w") as f:
                writer = csv.writer(f)
                writer.writerows(spell_update)
            # Breaks loop to continue to main menu
            break

# Used for Wild Surge
def wild_magic(file_name):
    with open(file_name) as f:
        reader = csv.reader(f)
        # Rolls on the Wild Magic Table
        sample_roll = d20.roll("d100")
        # F string required output for D20 module
        sample_num = (f"{sample_roll.total}")
        for row in reader:
            # Checker for 1st number
            if (sample_num == row[0]):
                # Prints out Wild Surge
                # Roll Range = Row[0] - Row[1] | Wild Surge Effect Row[2]
                print(f"{row[0]} - {row[1]} | {row[2]}")
                # Checker for dice roll. Skips rolls on 0 value (null)
                if row[3] != "0":
                    # Convert into f-string to allow d20 to pull from CSV file
                    num = (f"{row[3]}")
                    # Rolls from predetermine list inside CSV file
                    r = d20.roll(num)
                    # Prints total of dice value
                    print(r.total)
                # Breaks loop to continue to main menu
                break
            # Checker for 2nd number
            elif (sample_num == row[1]):
                # Prints out Wild Surge
                # Roll Range = Row[0] - Row[1] | Wild Surge Effect Row[2]
                print(f"{row[0]} - {row[1]} | {row[2]}")
                # Checker for dice roll. Skips rolls on 0 value (null)
                if row[3] != "0":
                    # Convert into f-string to allow d20 to pull from CSV file
                    num = (f"{row[3]}")
                    # Rolls from predetermine list inside CSV file
                    r = d20.roll(num)
                    print(r)
                # Breaks loop to continue to main menu
                break

def attack(file1, file2):
    # Shows current menu title
    print("=====Attack Menu=====")
    # Option for using spells
    print("1. Spell Book")
    # Option to go back to Main Menu
    print("2. Back")
    # Asks the user to select an option from above
    user_choice = input("Please select option: ")
    # Opens Spell Book and allows user to cast the selected spell
    while user_choice != "2":
        if user_choice == "1":
            spell_list(file1) 
            # Shows current menu title   
            print("=====Spell Book=====")
            spell_choice = ""
            # Asks user to choose spell to attack with.
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
                            # Dice to be used for Wild Surge check
                            wild_n = ("1d20")
                            # Rolls the selected dice
                            wild_r = d20.roll(wild_n)
                            # If dice roll is 1, wild surge will occur
                            if (wild_r.total == 1):
                                # Prints out roll value
                                print(f"Roll: {wild_r.total}")
                                # Confirmation on Wild Surge
                                print("Wild Surge!!!")
                                # Runs wild_magic function on fail
                                wild_magic(file2)
                            # If dice roll is not 1, executes else block
                            else:
                                # Prints out roll value
                                print(f"Roll: {wild_r.total}")
                                # Confirmation on no Wild Surge
                                print("No Wild Surge")
        # Stops the loop and returns to main menu
        break