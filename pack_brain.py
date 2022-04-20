from card_pack_list import *
import money
import random
import os
from time import sleep
from start_up_code import *


class PackGenerator():
    def __init__(self):
        self.p_name = ""
        self.p_per = 0
        self.p_price = 0
        self.p_ID = ""
        self.num_buy = 0
        with open("collection.txt") as c:
            if c == "":
                pass
            else:
                self.collection = c.readlines()


    def desired_pack(self, name_wanted):
        global saved_data
        saved_data = []
        # Saves the pack names
        self.p_name = name_wanted
        for data in main_packs:
            match = data["Pack Name"]
            if self.p_name == match:
                for k in data:
                    saved_data.append(data[k])
        self.transaction_calc("Packs")


    def desired_deck(self, name_wanted):
        global saved_data
        saved_data = []
        # Saves the deck names
        self.p_name = name_wanted
        for data in deck_box:
            match = data["Structure Deck Name"]
            if self.p_name == match:
                for k in data:
                    saved_data.append(data[k])
        self.transaction_calc("Structure Deck")


    def transaction_calc(self, desired_item):
        global saved_data
        # Number of wanted purchases
        rpg_speak(f'How many purchases do you want of "{self.p_name}"?', 0.04)
        self.num_buy = int(input())

        # Filling out the other purchases details and re-calculating the total price of desired purchases.
        self.p_per = saved_data[1]
        if desired_item == "Structure Deck":
            self.p_ID = saved_data[3]
        elif desired_item == "Packs":
            self.p_ID = saved_data[4]

        self.p_price = saved_data[2]
        saved_data[2] = round(float(self.p_price * self.num_buy), 2)
        self.p_price = saved_data[2]

        # Transaction Check

        rpg_speak("\nCalculating Transactions...\n", 0.04)


        if money.cash >= self.p_price:
            rpg_speak("Transaction Successful! Here's the items you bought!", 0.04)
            money.cash -= self.p_price
            if desired_item == "Packs":
                self.generate_cards()
            elif desired_item == "Structure Deck":
                self.gen_stru_deck()

        else:
            rpg_speak("Transaction Error! Not enough money to buy these items!", 0.04)


    def generate_cards(self):
        print()
        list_get = ID_List[self.p_ID]
        sele_hold = ""
        sele_add = []

        for _ in range(0, (self.num_buy)):
            _ += 1
            os.system('clear')
            get_check = self.p_per
            while get_check != 0:
                sele_hold = random.choice(list_get)
                if sele_hold not in sele_add:
                    print(sele_hold)
                    sleep(0.15)
                    sele_add.append(sele_hold)
                    get_check -= 1
                    with open("collection.txt", mode="a") as cc:
                        cc.write(f"{sele_hold}\n")
            sele_add.clear()
            print()
            if _ < self.num_buy:
                if input(f"Enter any key to open next pack ({_}/{self.num_buy} packs opened): ") == True:
                    os.system('clear')
            else:
                if input(f"Enter any key to continue ({_}/{self.num_buy} packs opened): ") == True:
                    pass


    def gen_stru_deck(self):
        print()
        list_get = STR_ID_List[self.p_ID]
        current_hold = ""
        clear_check = 0
        card_loc = 0
        for _ in range(0, (self.num_buy)):
            _ += 1
            os.system('clear')
            get_check = self.p_per
            while get_check != 0:
                current_hold = list_get[card_loc]
                print(current_hold)
                sleep(0.15)
                card_loc += 1
                clear_check += 1
                
                if clear_check >= 45:
                    if input("\nEnter any key to go to next page. ") == True:
                        pass
                    clear_check = 0
                    os.system('clear')
                with open("collection.txt", mode="a") as cc:
                    cc.write(f"{current_hold}\n")
                get_check -= 1
            print()
            if _ < self.num_buy:
                if input(f"Enter any key to open next pack ({_}/{self.num_buy} Structure Decks opened): ") == True:
                    get_check -= 1
                    os.system('clear')
            else:
                if input(f"Enter any key to continue ({_}/{self.num_buy} Structure Decks opened): ") == True:
                    pass


    def create_collect(self):
        os.system('clear')
        clear_check = 0
        with open("collection.txt") as ccc:
            coll = ccc.readlines()
            for ccoll in coll:
                clear_check += 1
                ccoll = ccoll.strip()
                sleep(0.045)
                if clear_check >= 45:
                    print()
                    if input("Enter any key to go to next page. ") == True:
                        pass
                    clear_check = 0
                    os.system('clear')
                print(ccoll)


    def view_collected(self):
        self.create_collect()
        print()
        print("Options you can do:")
        print('* Entering "Search" to begin searching your collection.')
        print("* Enter anything else to exit.")
        print()
        if input().title() == "Search":
            self.search_collect()
        else:
            pass


    def search_collect(self):
        os.system('clear')
        total_found = 0
        search = input('What text do you want to search for in your collection?\n(Enter "exit" to exit): ')
        if search == "exit" or search == "Exit":
            os.system('clear')
            self.view_collected()
        else:
            os.system('clear')
            clear_check = 0
            rpg_speak(f'This is what was found for "{search}":\n', 0.04)
            with open("collection.txt") as cs:
                coll = cs.readlines()
                for skimm in coll:
                    skimm = skimm.strip()
                    sleep(0.025)
                    if search in skimm:
                        print(skimm)
                        total_found += 1
                        clear_check += 1
                    if clear_check >= 45:
                        if input("\nEnter any key to go to next page. ") == True:
                            pass
                        clear_check = 0
                        os.system('clear')
            
            print(f'\n{total_found} total cards with "{search}" in the name were found.')
            if input('Do you want to continue searching your collections?\n(Yes or No): ').title() == "Yes":
                os.system('clear')
                self.search_collect()
            else:
                pass


# TODO: Storing collected cards in a txt file (DONE)

# TODO: Resetting the repl somehow (DONE)

# TODO: 
            















