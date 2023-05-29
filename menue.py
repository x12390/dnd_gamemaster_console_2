import cover_bonus
import sys


"""
1. Add a menu to a console application to manage activities.
2. Run a selected function.
3. Clear the output
4. Display the menu again or exit if done is selected
"""



from os import system, name
group = []

def cls():
   system('cls' if name=='nt' else 'clear')


def main_menu(title, topics):
    #standard Auswahlmenue mit Titel
    while True:
        cls()
        cnt = 0
        print(f"--- {title} ---")
        length = len(topics)
        for topic in topics:
            cnt += 1
            print(f"{cnt}. {topic}")


        choice = input(f"Bitte wählen [1-{length}] or q: ")
        if choice == "q":
           quit(0)
        elif choice.isnumeric():
            choice = int(choice)
            return choice

def sub_menu(title, topics):
    #standard Auswahlmenue mit Titel
    while True:
        cls()
        cnt = 0
        print(f"--- {title} ---")
        length = len(topics)
        for topic in topics:
            cnt += 1
            print(f"{cnt}. {topic}")


        choice = input(f"Bitte wählen [1-{length}] or q: ")
        if choice == "q":
           return choice
        elif choice.isnumeric():
            choice = int(choice)
            return choice

def select_menu_creatures(title, creature_list):
    group =[]
    #standard Auswahlmenue mit Titel
    while True:
        cls()
        cnt = 0
        print(f"--- {title} ---")
        length = len(creature_list)
        for creature_race in creature_list:
            cnt += 1
            print(f"{cnt}. {creature_race.upper()}")

        choice = input(f"Bitte wählen [1-{length}] or q: ")
        if choice == "q":
            return group

        elif choice.isnumeric() and int(choice) <= length:
            choice = int(choice)
            member = creature_list[choice-1]
            group.append(member)
        else:
            print("Wrong input.")

def select_menu_creatureObject(title, creature_obj_list):
    group =[]
    #standard Auswahlmenue mit Titel
    while True:
        cls()
        cnt = 0
        print(f"--- {title} ---")
        length = len(creature_obj_list)
        for creature in creature_obj_list:
            cnt += 1
            if creature.is_attackable() == False:
                marker = "[VOLLE DECKUNG]"
            else:
                marker = ""
            print(f"{cnt}. {(creature.race).upper()} {marker}")

        choice = input(f"Bitte wählen [1-{length}] or q: ")
        if choice == "q":
            return None

        elif choice.isnumeric() and int(choice) <= length:
            choice = int(choice)
            member = creature_obj_list[choice-1]
            return member
        else:
            print("Wrong input.")


def cover_selection():
    #Deckungsauswahl zur Bonusberechnung
    choice = sub_menu("Deckung", ["keine", "1/2 Deckung", "3/4 Deckung", "Volle Deckung"])
    cover_category = ""
    if choice == 1:
        cover_category = "none"
    elif choice == 2:
        cover_category = "half"
    elif choice == 3:
        cover_category = "big"
    else:
        cover_category = "full"

    return cover_bonus.cover_calculation(cover_category)







