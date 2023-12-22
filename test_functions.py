import csv
import d20
from wild_magic_functions import wild_magic

def test_attack(file1, file2):
    print("=====Attack Menu=====")
    print("1. Spell Book")
    print("2. Back")
    user_choice = input("Please select option: ")
    # Opens Spell Book and allows user to cast the selected spell
    while user_choice != "2":
        if user_choice == "1":        
            print("=====Spell Book=====")
            spell_choice = ""
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
        break

                        
    # Rolls to attack using modifiers provided
    # Rolls damage for spell (if damaging)
    # Checks the spell level
    # 1st level or higher, does roll check for Wild Surge
    # On roll of 1, Surge effect occurs.
    # Roll on Surge table and uses Wild_Surge function