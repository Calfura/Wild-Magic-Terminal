# Wild Magic - Sorcerer Terminal Application

## Description

Terminal application for the archetype of Wild Magic Sorcerer's, where it will roll on the d100 table of Wild Magic to determine what Wild Surge is casted. The terminal application will check if the spell casted was a cantrip(base level spell) or if it is a 1st level spell. It then will proceede to roll to check if a Wild Surge happens, outputs if the Surge does not occur or if the Surge occured. If a Surge occurs, it will roll on the d100 table and print out the Surge effect that happened (with possible additional rolls added).

The application will hold basic information about the character stats to use as modifiers for spells casted. A basic spell list will be used/added for the terminal application (as there are far to many spells to add, check and work on within a short amount of time). On first use, the app will create the additional csv files needed to record any data to be used as well as a way to delete old 'saved' files, so the user can add in new character data when appropriate.

## Features

### Character Stats

* Creation of character sheet for stats. Lists out each stat type and their value in order. (WIP) Character stat sheet will add a modifier to the dice roll to increase or decrease dice rolls for attacks or saves.

### Spells

* Spell-listing - A selection of spells that the terminal program will allow as choices to be added into the spellbook of the character, that the terminal will be able to handle and provide the correct outputs
* Spells - The selected spell's learnt from the spell-listing that the character know's and that the program can do rolls for and check for any Wild Surges (Spells allowed will be limited in early versions to allow testing and debugging. Additional spells will be added as further developed the program becomes).
