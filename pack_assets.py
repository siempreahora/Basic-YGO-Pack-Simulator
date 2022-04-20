from prettytable import PrettyTable
from card_pack_list import main_packs, deck_box

logo = ('''
___________________________________________________
   ______               __   ____             __  
  / ____/___ __________/ /  / __ \____ ______/ /__
 / /   / __ `/ ___/ __  /  / /_/ / __ `/ ___/ //_/
/ /___/ /_/ / /  / /_/ /  / ____/ /_/ / /__/ ,<   
\____/\__,_/_/   \__,_/  /_/    \__,_/\___/_/|_|  
   _____ _                 __      __             
  / ___/(_)___ ___  __  __/ /___ _/ /_____  _____ 
  \__ \/ / __ `__ \/ / / / / __ `/ __/ __ \/ ___/ 
 ___/ / / / / / / / /_/ / / /_/ / /_/ /_/ / /     
/____/_/_/ /_/ /_/\__,_/_/\__,_/\__/\____/_/    
            
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
''')


pack_table = PrettyTable()
stru_dek_table = PrettyTable()



pack_table.field_names = ["Pack Name", "Cards Per Pack", "Price Per Pack", "Cards In Set", "Pack ID"]

for data_got in main_packs:
    get_pack_name = data_got["Pack Name"]
    get_pack_per = data_got["Cards Per Pack"]
    get_pack_price = data_got["Price (Per Pack)"]
    get_pack_set = data_got["Cards In Set"]
    get_pack_ID = data_got["Pack ID"]

    compiled_data = []
    compiled_data.append(get_pack_name)
    compiled_data.append(get_pack_per)
    compiled_data.append("$" + str(get_pack_price))
    compiled_data.append(get_pack_set)
    compiled_data.append(get_pack_ID)


    pack_table.add_row(compiled_data)
    pack_table.align = "l"


stru_dek_table.field_names = ["Structure Deck Name", "Cards In Deck", "Price", "Deck ID"]

for stru_data in deck_box:
    get_stru_name = stru_data["Structure Deck Name"]
    get_stru_per = stru_data["Cards In Deck"]
    get_stru_price = stru_data["Price"]
    get_stru_ID = stru_data["Deck ID"]

    compiled_data = []
    compiled_data.append(get_stru_name)
    compiled_data.append(get_stru_per)
    compiled_data.append("$" + str(get_stru_price))
    compiled_data.append(get_stru_ID)


    stru_dek_table.add_row(compiled_data)
    stru_dek_table.align = "l"


def print_table():
    print(pack_table.get_string(sortby="Cards Per Pack"))
    print(stru_dek_table.get_string(sortby="Structure Deck Name"))






