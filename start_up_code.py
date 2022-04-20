from pack_assets import print_table, logo
from rpg_dialogue_mods import *
import money


def start_bootloader():
    print(logo)
    rpg_speak("Downloading code...", 0.035)
    rpg_speak("Ordering packs...", 0.035)
    rpg_speak("Ordering Structure Decks...", 0.035)
    rpg_speak("Loading collection...", 0.035)
    rpg_speak("Finishing loader...", 0.035)
    rpg_speak("Opening shop!", 0.035)
    start_up()



def start_up():
    print(logo)
    print("Current Money: $" + str(money.cash))
    print_table()
    print()
    rpg_speak("Options you can do:", 0.04)
    print('* Enter "Packs" for packs, or "Decks" for Structure Decks.')
    print('* Entering "Close" will close the shop.')
    print('* Entering "View Cards" will view what you collected.')
    print('* Entering "Search" to search your collection.')
    # print('* Entering "Clear" to clear visual bugs. (Visual bug must be on screen to work)')
    print()












