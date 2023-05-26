import random

class Dice:
    hp_dice = True
    """Klasse zur Erstellung von Wuerfelobjekten."""
    def __init__(self, sides=6, amount=1, bonus=0):
        self.set_dice(sides, amount, bonus)

    def enable_hp_dice_rules(self):
        self.hp_dice = True
    def disable_hp_dice_rules(self):
        self.hp_dice = False

    def set_dice(self, sides:int, amount:int, bonus=0):
        """
        Definition eines oder mehrerer Würfel.
        :param sides: Anzahl der Würfelseiten
        :param amount: Menge gleichartiger Würfel
        :param bonus: Fester Bonus zum Wurfergebnis eines Würfels
        :return: Objekt eines Würfels
        """
        self.sides = sides
        self.amount = amount
        self.bonus = bonus
        self.type = f"{amount}W{sides}"
        self.enable_hp_dice_rules()

    def get_type(self):
        """Rückgabe des Würfeltyps. Bspw 1W20."""
        return self.type

    def set_bonus(self, bonus):
        """Setzen eines Bonus der nach dem Wurf addiert wird."""
        self.bonus = int(bonus)

    def get_bonus(self):
        """Ausgabe des Bonus der nach dem Wurf addiert wird."""
        return self.bonus

    def roll(self):
        """Ausführung eines Wurfs mit dem aktuellen Würfel(n). Bspw. 2W6 würfelt 2x mit einem 6-seitigen Würfel."""
        roll_results = [] #single result/dice
        cnt = 0
        msg = self.__str__()
        for _ in range(self.amount):
            cnt += 1
            roll = random.randint(1, self.sides)
            msg = msg + ", Wurf " + str(cnt) + " => " + str(roll)

            if self.hp_dice == True:
                if roll <= 1:
                    msg = msg + "[MISSED]"
                    roll = 0

            roll_results.append(roll)

        sum_result = sum(roll_results)
        msg += f" = Summe: {sum_result}"
        if sum_result > 0:
            sum_result += self.bonus
            msg += f" + Bonus: {self.bonus}"
        msg = msg + " ==> Gesamt: " + str(sum_result)
        print(msg)
        return sum_result #sum of all dices

    def roll_initiative(self, dexternity_mod=0):
        """Initativewurf mit 1W20, um die Reihenfolge der Aktionen zu bestimmen. Addiert den Geschicklichkeitsmodifikator,
        sofern dieser als Parameter übergeben wurde."""
        return random.randint(1, 20) + dexternity_mod

    def roll_attribute(self, attribute_modificator:int):
        """Attributswurf (Geschicklichkeit, Weisheit, Charisma, Stärke, Konstitution, Intelligenz) plus zugehörigen Modifikator."""
        result = self.roll()
        result = result + attribute_modificator
        return result

    def roll_save(self, save_categories, training_value:int):
        """Rettungswurf mit Pruefung, ob charakter in einer der erlaubten kategorien geübt ist. """
        ret = self.roll()
        allowed = ["Geschicklichkeit", "Charisma", "Stärke", "Konstitution", "Intelligenz", "Weisheit"]
        for save in save_categories:
            if save in allowed:
                print(f"Additional training bonus for {save}: {training_value}")
                ret += training_value
                break
        print(f"Result save throw: {ret}")
        return ret

    def __str__(self):
        """String Representation eines Würfels. Bspw. '1W6'. """
        hp_flag = ""
        if self.hp_dice == True:
            hp_flag = "HP "

        return f"{hp_flag}{self.amount}W{self.sides}+{self.bonus}"


class DiceFactory:
    @staticmethod
    def create_dice(dice_type: str):
        """Erstellt einen Wuerfel mit einer standardisierten Angabe, wie 1W20."""
        dice_type = dice_type.lower()
        dice_arr = dice_type.split("w")
        if len(dice_arr) == 2:
            amount = int(dice_arr[0])
            sides = int(dice_arr[1])
            return Dice(sides,amount)
        else:
            return None
        return dice


dice = DiceFactory.create_dice("1W10")
print(f"{dice.amount} dice(s) with {dice.sides} sides.")
dice.disable_hp_dice_rules()
dice.set_bonus(100)
dice.roll()
# W20 = Dice(6,2)
# print(W20.roll_attribute(5))
# print(W20.roll_save(["dfs", "Panzerfrosch"], 3))
# print(W20.get_type())

