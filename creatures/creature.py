from character import Character
from dice import DiceFactory

#Creature allgemein
class Creature(Character):
    def __init__(self):
        self.test = []
        self.close_hitpoint_dice = []
        self.close_damage_dice = []
        self.ranged_hitpoint_dice = []
        self.ranged_damage_dice = []
        self.description = None
        self.init_base_attributes()
        self.set_close_hitpoint_dice()
        self.set_ranged_hitpoint_dice()
        self.set_resistence([])
        self.set_immunity([])


    def set_attributes(self, array_attribute_values):
        if len(array_attribute_values) == 6:
            self.set_strength(array_attribute_values[0])
            self.set_dexterity(array_attribute_values[1])
            self.set_constitution(array_attribute_values[2])
            self.set_intelligence(array_attribute_values[3])
            self.set_wisdom(array_attribute_values[4])
            self.set_charisma(array_attribute_values[5])
        else:
            print("Error, wrong amount of attributes in given array.")

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

        if self.is_attackable() == False:
            cover_text = "100%"
        elif self.get_cover_bonus() >= 0:
            cover_text = str(self.cover_bonus)

        print(
            f"-------------------------------------------- \n"
            f"Klasse: {self.race} \n"
            f"Name: << {self.name} >>, {self.get_size()} (mod: {self.get_size_modificator()}), EP: {self.ep}  \n" 
            f"{self.get_description()} \n"
            f"-------------------------------------------- \n"          
            f"Rüstungsklasse: {self.get_rk()} inkl. Deckungsbonus: {cover_text} \n"
            f"Trefferpunkte: {self.get_hitpoints()} \n"           
            f"STR: {self.strength} ({self.strength_mod}) \n"
            f"GES: {self.dexterity} ({self.dexterity_mod}) \n"
            f"KON: {self.constitution} ({self.constitution_mod}) \n"
            f"INT: {self.intelligence} ({self.intelligence_mod}) \n"
            f"WEI: {self.wisdom} ({self.wisdom_mod}) \n"
            f"CHA: {self.charisma} ({self.charisma_mod}) \n"     
            f"Würfel Treffer - Nah: {close_hp_dices} , Fern: {ranged_hp_dices}\n"
            f"Würfel Schaden - Nah: {close_dmg_dices} , Fern: {ranged_dmg_dices}\n"
            f"Resistent gegen: {self.get_resistence()} \n"
            f"Immun gegen: {self.get_immunity()} \n"
        )

    def set_resistence(self,arrValues):
        self.resistence = arrValues

    def get_resistence(self):
       return self.resistence

    def set_immunity(self, arrValues):
        self.immunity = arrValues

    def get_immunity(self):
        return self.immunity

    def set_description(self, desc):
        self.description = "Beschreibung: " + desc

    def get_description(self):
        return self.description




