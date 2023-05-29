from character import Character

#Spieler Charakter
class Player(Character):
    level = 1
    training_bonus = 2
    trained_saves = []

    def __init__(self, *args):
        super().__init__(*args)
        self.set_hp_dice_sides(6)

    def show_attributes(self):
        self.cls()
        super().show_attributes()
        print(
            f"Level: {self.level} \n"
            f"Trefferpunkte: {self.hitpoints} \n"                
            f"Lvl: {self.level} (Training bonus: {self.training_bonus})"
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

    def set_ep(self, ep):
        """Set expierience points the player gained."""
        self.ep = ep
    def get_ep(self):
        """Returns gained expierience points."""
        return self.ep

class Magier(Player):
    def __init__(self, *args):
        super().__init__(*args)
        self.set_hp_dice_sides(6)


class Barde(Player):
    def __init__(self, *args):
        super().__init__(*args)
        self.set_hp_dice_sides(8)

class Kleriker(Player):
    def __init__(self, *args):
        super().__init__(*args)
        self.set_hp_dice_sides(8)

class Schurke(Player):
    def __init__(self, *args):
        super().__init__(*args)
        self.set_hp_dice_sides(8)

class Kämpfer(Player):
    def __init__(self, *args):
        super().__init__(*args)
        self.set_hp_dice_sides(10)


p1 = Magier("Kalle")
p1.show_attributes()