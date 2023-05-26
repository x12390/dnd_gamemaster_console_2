from character import Character

#Spieler Charakter
class Player(Character):
    def __init__(self, *args):
        self.init_base_attributes(*args)
        self.set_hp_dice_sides(6)
        # recalc rk after additonal attributes set
        self.change_rk(self.dexterity_mod)
        self.change_level(1)

    def show_attributes(self):
        self.cls()
        print(
            f"Klasse: {self.__class__.__name__} \n"
            f"Name: {self.name} \n"
            f"Größe: {self.size} \n"
            f"Stärke: {self.strength}, mod: {self.strength_mod}\n"
            f"Geschicklichkeit: {self.dexterity}, mod: {self.dexterity_mod} \n"
            f"Konstitution: {self.constitution}, mod: {self.constitution_mod} \n"
            f"Intelligenz: {self.intelligence}, mod: {self.intelligence_mod} \n"
            f"Charisma: {self.charisma}, mod: {self.charisma_mod} \n"
            f"Rüstungsklasse: {self.rk} \n"
            f"Level: {self.level} \n"
            f"Trefferpunkte: {self.hitpoints} \n"
            f"TP-Würfel: {self.hitpoint_dice_amount}W{self.hitpoint_dice_sides} \n"
            f"Deckungsbonus: {self.cover_bonus} \n"
            f"Geübte Rettungswürfe: {self.trained_saves} \n"
        )

    def change_level(self, val):
        self.level = self.level + val
        if self.level < 0:
            self.level = 1
        self.set_hp_dice_amount(self.level)
        self.recalc_hitpoints()

    def change_constitution(self, val):
        self.constitution = self.constitution + val
        self.constitution_mod = self.get_attribute_modificator(self.constitution)
        self.recalc_hitpoints()

    def add_trained_save(self):
        saves = ["Geschicklichkeit", "Charisma", "Stärke", "Konstitution", "Intelligenz", "Weisheit"]
        while True:
           print(f"Setze geübte Rettungswürfe:\n")
           cnt = 0
           for save in saves:
               print(f"{cnt}. {save}\n")
               cnt += 1
           ans = input("Wähle [0-5] or q: \n")
           choice = None
           if ans.isnumeric():
               choice = int(ans)
               if choice <= len(saves):
                   self.trained_saves.append(saves[choice])
           elif ans == "q":
               break

    def set_hp_dice_sides(self, sides):
        self.hitpoint_dice_sides = sides
        self.recalc_hitpoints()

    def recalc_hitpoints(self, bonus_hitpoints=0):
        hp = self.hitpoint_dice_sides
        if (self.constitution_mod > 0):
            hp = hp + (self.constitution_mod * self.level)
        else:
            hp = hp + self.constitution_mod
        hp = hp + bonus_hitpoints
        self.hitpoints = hp

class Magier(Character):
    def __init__(self, *args):
        self.init_base_attributes(*args)
        self.set_hp_dice_sides(6)


class Barde(Character):
    def __init__(self, *args):
        self.init_base_attributes(*args)
        self.set_hp_dice_sides(8)

class Kleriker(Character):
    def __init__(self, *args):
        self.init_base_attributes(*args)
        self.set_hp_dice_sides(8)

class Schurke(Character):
    def __init__(self, *args):
        self.init_base_attributes(*args)
        self.set_hp_dice_sides(8)

class Kämpfer(Character):
    def __init__(self, *args):
        self.init_base_attributes(*args)
        self.set_hp_dice_sides(10)