from character import Character
from dice import DiceFactory

#Creature allgemein
class Creature(Character):
    close_hitpoint_dice = []
    close_damage_dice = []
    ranged_hitpoint_dice = []
    ranged_damage_dice = []
    def __init__(self, *args):
       super().__init__(*args)
       self.set_close_hitpoint_dice()
       self.set_ranged_hitpoint_dice()
    def set_close_hitpoint_dice(self, dice_type=0, bonus=0):
        dice = None
        if dice_type != 0:
            dice = DiceFactory.create_dice(dice_type)
            if dice is not None:
                dice.set_bonus(bonus)
                self.close_hitpoint_dice.append(dice)
    def get_close_hitpoint_dice(self):
        return self.close_hitpoint_dice

    def set_close_damage_dice(self, dice_type=0, bonus=0):
        dice = None
        if dice_type != 0:
            dice = DiceFactory.create_dice(dice_type)
            dice.disable_hp_dice_rules()
            if dice is not None:
                dice.set_bonus(bonus)
                self.close_damage_dice.append(dice)

    def get_close_damage_dice(self):
        return self.close_damage_dice

    def set_ranged_hitpoint_dice(self, dice_type=0, bonus=0):
        dice = None
        if dice_type != 0:
            dice = DiceFactory.create_dice(dice_type)
            if dice is not None:
                dice.set_bonus(bonus)
                self.ranged_hitpoint_dice.append(dice)

    def get_ranged_hitpoint_dice(self):
        return self.ranged_hitpoint_dice

    def set_ranged_damage_dice(self, dice_type=0, bonus=0):
        dice = None
        dice = DiceFactory.create_dice(dice_type)
        dice.disable_hp_dice_rules()
        if dice is not None:
            dice.set_bonus(bonus)
            self.ranged_damage_dice.append(dice)


    def get_ranged_damage_dice(self):
        return self.ranged_damage_dice

    #Axt
    def attack_close(self):
        ret = self.attack(self.close_hitpoint_dice, self.close_damage_dice)
        return ret

    #Speerwurf
    def attack_ranged(self):
        ret = self.attack(self.ranged_hitpoint_dice, self.ranged_damage_dice)
        return ret

    def attack(self, dices_tp, dices_dmg):
        """Angriffswurfe. Wichtig: dices_tp und dices_dmg sind Arrays die Wuerfelobjekte enthalten. Die Anzahl richtet sich
           nach der Konfiguration der Creature in der ini-Datei."""
        ret = []

        #Anzahl der Damagewürfel entscheidet über Attacken!
        dice_cnt = 0
        for dice in dices_tp:
            hitpoints = 0
            damage = 0
            dice_cnt += 1

            if dice is not None and dice.sides > 0:
                print(f"\n{self.race} '{self.name}': [hp,dmg]")
                #Wuerfel Trefferpunkte
                hitpoints = dice.roll()

                if hitpoints > 1:
                    #Trefferpunkt von mehr als 1 ist generell ein Treffer
                    #Gamemaster muss pruefen, ob mit der Anzahl Trefferpunkte die RK des Gegners erreicht wurde.
                    #Wenn ja, ist der Damage für den Gamemaster interessant, diesen teilt er dem Spieler mit.
                    hitpoints += self.cover_bonus #Deckung steigert die Geschicklichkeit (bswp. Auflehnen beim Zielen)

                    if dices_dmg is not None:
                        dice_dmg = dices_dmg[dice_cnt-1]
                        print(f"Dice {dice_cnt}: {dices_dmg[dice_cnt-1]} ")
                        if dice_dmg is not None:
                            damage = dice_dmg.roll()
                        ret.append(f"TP: {str(hitpoints)}")
                        ret.append(f"DMG: {str(damage)}")

                        if hitpoints >= 20:
                            #bei kritischem Treffer 2. Mal Schaden wuerfeln
                            damage = dice_dmg.roll()
                            ret.append(f"TP: {str(hitpoints)}")
                            ret.append(f"DMG: {str(damage)}")
                else:
                    #Trefferpunkt von 1 ist verfehlt und macht keinen Schaden
                    print("Ups, verfehlt!")
                    ret.append(f"TP: {str(hitpoints)}")
                    ret.append(f"DMG: {str(damage)}")

            else:
                print(f"\n{self.race} '{self.name}' [no attack available]!")

        return ret
    def show_attributes(self):
        self.cls()

        #Array mit Würfeln für Darstellung aufbereiten.
        close_hp_dices = ""
        for d in self.get_close_hitpoint_dice():
            close_hp_dices += str(d) + " "

        # Array mit Würfeln für Darstellung aufbereiten.
        ranged_hp_dices = ""
        for d in self.get_ranged_hitpoint_dice():
            ranged_hp_dices += str(d) + " "

        #Array mit Würfeln für Darstellung aufbereiten.
        close_dmg_dices = ""
        for d in self.get_close_damage_dice():
            close_dmg_dices += str(d) + " "

        # Array mit Würfeln für Darstellung aufbereiten.
        ranged_dmg_dices = ""
        for d in self.get_ranged_damage_dice():
            ranged_dmg_dices += str(d) + " "

        super().show_attributes()
        print(
            f"Würfel Treffer - Nah: {close_hp_dices} , Fern: {ranged_hp_dices}\n"
            f"Würfel Schaden - Nah: {close_dmg_dices} , Fern: {ranged_dmg_dices}\n"
        )

    def set_resistence(self,arrValues):
        self.resistence = arrValues

    def get_resistence(self):
       return self.resistence

    def set_immunity(self, arrValues):
        self.immunity = arrValues

    def get_immunity(self):
        return self.immunity






