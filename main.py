from menue import main_menu as selection
from menue import select_menu_creatures
from combat import combat
from configparser import ConfigParser

cfg = ConfigParser()
cfg.read("creatures.ini")
active_creatures = cfg.get('kreaturen', 'aktiv')
templist = active_creatures.split(",")
creature_list = []
for entry in templist:
    v= entry.strip()
    creature_list.append(v)

def main():

    enemies = []
    print(f"Gruppe: {','.join(enemies)} \n")
    while True:
        choice = selection("Hauptmenue", ["Gruppe erstellen", "Kampf"])

        if choice == 1:
            #Option Gruppe erstellen
            enemies = select_menu_creatures("Gruppe erstellen", creature_list)
            # cls()
            # print(f"""
            # A group of enemies arrived: \n
            # {enemies}
            # """)

        elif choice == 2:
            # Option Kampf
            back = combat(enemies)






if __name__ == "__main__":
    main()