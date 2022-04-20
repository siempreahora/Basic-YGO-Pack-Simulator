from pack_brain import PackGenerator
from start_up_code import *
from card_pack_list import main_packs

import money
import os

if __name__ == "__main__":
    money.stash()

shop_open = True

shop = PackGenerator()

# start_bootloader()
# os.system('clear')
start_up()

# rpg_speak("", 0.055)


while shop_open:
    item_sele = input().title()
    if item_sele == "Close":
        shop_open = False
    elif item_sele == "Clear":
        os.system('clear')
        start_up()
    elif item_sele == "View Cards":
        shop.view_collected()
        os.system('clear')
        start_up()
    elif item_sele == "Search":
        shop.search_collect()
        os.system('clear')
        start_up()
    elif item_sele == "Packs":
        item_sele = input("Ok, what pack do you want? ").title()
        shop.desired_pack(item_sele)
        os.system('clear')
        start_up()
    elif item_sele == "Decks":
        item_sele = input("Ok, what Structure Deck do you want? ").title()
        shop.desired_deck(item_sele)
        os.system('clear')
        start_up()








# Deck Building = 45 cards per set / 5 cards per pack
# Champion Pack = 20 cards per set / 3 cards per pack


