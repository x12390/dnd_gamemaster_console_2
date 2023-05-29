from dice import Dice
from os import system, name
import names




class Character:
    """Klasse fuer allgemeine Charaktermerkmale."""
    race = "Mensch"
    name = names.get_first_name(gender="male")
    description = None
    size = "mittelgross"
    size_mod = 0
    strength = 0
    strength_mod = 0
    dexterity = 0
    dexterity_mod = 0
    constitution = 0
    constitution_mod = 0
    intelligence = 0
    intelligence_mod = 0
    wisdom = 0
    wisdom_mod = 0
    charisma = 0
    charisma_mod = 0
    rk = 10 #default, menschliche Haut
    hitpoints = 0
    initiative = -1
    cover_bonus = 0  # Deckung 0: kein, 1: 1/2 = +2RK, 2: 3/4 = +5RK, 3: voll = Kein Angriff moeglich
    cover_text = "0"
    attackable = True
    ep = 0
    status = "aktiv"
    resistence = []
    immunity = []
    def __init__(self, *args):
        """
        Instanzierung kann mit optionalen Parametern erfolgen:
        1.) Name des Charakters
        2.) Stärke (STR)
        3.) Geschicklichkeit (GES)
        4.) Konstitutition (KON)
        5.) Intelligenz (INT)
        6.) Weisheit (WEI)
        7.) Charisma (CHA)

        Es handelt sich dabei um die typischen Attributwerte, die einen Rollenspielcharakter mitgegeben werden.
        Somit bildet diese Klasse die Basis für spezielle Spieler-Charaktere oder Kreaturen.

        Beispiel 1: gegner = Character("Franz",16,19,14,10,15,11)
        Beispiel 2: gegner = Character("Paul")
        """
        self.init_base_attributes(*args)

    def init_base_attributes(self, *args):
        if len(args) == 1:
            self.name = args[0]
        elif len(args) == 2:
            self.name = args[0]
            self.set_strength(args[1])
        elif len(args) == 3:
            self.name = args[0]
            self.set_strength(args[1])
            self.set_dexterity(args[2])
        elif len(args) == 4:
            self.name = args[0]
            self.set_strength(args[1])
            self.set_dexterity(args[2])
            self.set_constitution(args[3])
        elif len(args) == 5:
            self.name = args[0]
            self.set_strength(args[1])
            self.set_dexterity(args[2])
            self.set_constitution(args[3])
            self.set_intelligence(args[4])
        elif len(args) == 6:
            self.name = args[0]
            self.set_strength(args[1])
            self.set_dexterity(args[2])
            self.set_constitution(args[3])
            self.set_intelligence(args[4])
            self.set_wisdom(args[5])
        elif len(args) == 7:
            self.name = args[0]
            self.set_strength(args[1])
            self.set_dexterity(args[2])
            self.set_constitution(args[3])
            self.set_intelligence(args[4])
            self.set_wisdom(args[5])
            self.set_charisma(args[6])

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


    def show_attributes(self):

        print(
            f"-------------------------------------------- \n"
            f"Klasse: {self.race} \n"
            f"Name: << {self.name} >>, {self.get_size()} (mod: {self.get_size_modificator()}), EP: {self.ep}  \n"
            f"{self.get_description()} \n"
            f"-------------------------------------------- \n"
            f"Rüstungsklasse: {self.get_rk()} inkl. Deckungsbonus: {self.cover_text} \n"
            f"Trefferpunkte: {self.get_hitpoints()} \n"
            f"STR: {self.strength} ({self.strength_mod}) \n"
            f"GES: {self.dexterity} ({self.dexterity_mod}) \n"
            f"KON: {self.constitution} ({self.constitution_mod}) \n"
            f"INT: {self.intelligence} ({self.intelligence_mod}) \n"
            f"WEI: {self.wisdom} ({self.wisdom_mod}) \n"
            f"CHA: {self.charisma} ({self.charisma_mod}) \n"
            f"Resistent gegen: {self.get_resistence()} \n"
            f"Immun gegen: {self.get_immunity()} \n"
        )

    # Name des Charakters
    def set_name(self, name=None):
        '''
        Name des Charakters.
        Wird keine Name per Parameter festgelegt wird ein maennlicher Name generiert.
        '''

        if name is None:
            name = names.get_first_name(gender="male")
        self.name = name

    # Rasse / Race
    def set_race(self, race=None):
        """Setzt die Rasse des Charakters (bspw. Zwerg, Ork, Mensch, etc.).
        Es ist nur ein beschreibendes Merkmal.
        """
        self.race = race

    def get_race(self):
        """Gibt die Rasse zurueck."""
        return self.race

    #EP, Erfahrungspunkte / Experience Points
    def set_ep(self, ex):
        """Setzt die Erfahrungspunkte des Charakters."""
        self.ep = ex

    def get_ep(self):
        """Gibt die Erfahrungspunkte des Charakters zurueck."""
        return self.ep

    def set_level(self, lvl):
        self.level = lvl
        # calculate trainings_bonus
        if lvl <= 4:
            self.training_bonus = 2
        elif lvl > 4 and lvl <= 8:
            self.training_bonus = 3
        elif lvl > 8 and lvl <= 12:
            self.training_bonus = 4
        elif lvl > 12 and lvl <= 16:
            self.training_bonus = 5
        elif lvl > 16:
            self.training_bonus = 6


    # Attributsmodifikator
    def get_attribute_modificator(self, attribute_value):
        """
        Methode, die den Attributmodifikator für ein gegebenen Attributswert zurueckgibt.
        :param attribute_value: Attributwert des Charakters
        :return: Attributmodifikator
        """
        ret = -1

        modlist = [[1, -5], [2, -4], [3, -4], [4, -3], [5, -3], [6, -2], [7, -2], [8, -1], [9, -1], [10, 0],
                   [11, 0], [12, 1], [13, 1], [14, 2], [15, 2], [16, 3], [17, 3], [18, 4], [19, 4], [20, 5],
                   [21, 5], [22, 6], [23, 6], [24, 7], [25, 7], [26, 8], [27, 8], [28, 9], [29, 9], [30, 10]
                  ]

        for i in modlist:
            list_attribute_value = i[0]
            if list_attribute_value == attribute_value:
                ret = i[1]
        return ret

    # Groesse des Charakters
    def set_size(self, size):
        """
        Setzt die Groessenkategorie des Charakters.
        Beim Setzen wird automatisch der Groessenmodifikator berechnet und gesetzt.
        Der Default bei neu angelegten Charakteren ist "mittelgroß".
        :param size: Groessenkategorie. Erlaubt sind "kollosal", "gigantisch", "riesig", "groß", "mittelgroß", "klein", "sehr klein", "winzig", "mini".
        :return: Groessenmodifikator.
        """
        size_mods = [("kollosal", -8), ("gigantisch", -4), ("riesig", -2), ("gross", -1), ("mittelgross", 0),
                     ("klein", 1), ("sehr klein", 2), ("winzig", 4), ("mini", 8)]

        ret = None
        known_types = []
        for i in size_mods:
            cat = i[0]
            known_types.append(cat)
            if cat.lower() == size.lower():
                #set size modificator
                ret = self.size_mod = i[1]

        if ret is None:
            print(f"Size {size} not supported.")
            print(f"Supported types are: {known_types}")
            self.size = size + " [invalid]"
        else:
            #set size if size is a known type
            self.size = size

        return ret

    def get_size(self):
        """Rueckgabe Koerpergroessenbezeichnung."""
        return self.size

    def get_size_modificator(self):
        """Rueckgabe des Groessenmodifikators."""
        return self.size_mod

    def set_strength(self, val):
        """Setzt den Attributswert für Stärke."""
        self.strength = self.strength + val
        self.strength_mod = self.get_attribute_modificator(self.strength)

    def get_strength(self):
        """Rueckgabe des Attributwerts für Stärke."""
        return self.strength

    def set_dexterity(self, val):
        """Setzt den Attributswert für Geschicklichkeit."""
        self.dexterity = self.dexterity + val
        self.dexterity_mod = self.get_attribute_modificator(self.dexterity)

    def get_dexterity(self):
        """Rueckgabe des Attributwerts für Geschicklichkeit."""
        return self.dexterity

    def set_constitution(self, val):
        """Setzt den Attributswert für Konstitution."""
        self.constitution = self.constitution + val
        self.constitution_mod = self.get_attribute_modificator(self.constitution)

    def get_consitution(self):
        """Rueckgabe des Attributwerts für Konstitution."""
        return self.constitution

    def set_intelligence(self, val):
        """Setzt den Attributswert für Intelligenz."""
        self.intelligence = self.intelligence + val
        self.intelligence_mod = self.get_attribute_modificator(self.intelligence)

    def get_intelligence(self):
        """Rueckgabe des Attributwerts für Intelligenz."""
        return self.intelligence

    def set_wisdom(self, val):
        """Setzt den Attributswert für Weisheit."""
        self.wisdom = self.wisdom + val
        self.wisdom_mod = self.get_attribute_modificator(self.wisdom)

    def get_wisdom(self):
        """Rueckgabe des Attributwerts für Weisheit."""
        return self.wisdom

    def set_charisma(self, val):
        """Setzt den Attributswert für Charisma."""
        self.charisma = self.charisma + val
        self.charisma_mod = self.get_attribute_modificator(self.charisma)

    def get_charisma(self):
        """Rueckgabe des Attributwerts für Weisheit."""
        return self.charisma

    def set_rk(self, val):
        """Setzt den Wert für Rüstungsklasse."""
        self.rk = val
        if self.rk < 0:
            self.rk = 0

    def get_rk(self):
        """Rueckgabe der Rüstungsklasse (RK). Plus eventuellen Deckungsbonus."""
        rk = self.rk
        if self.cover_bonus > 0:
            rk = rk + self.cover_bonus
        return rk

    def set_hitpoints(self, hp):
        """Setzt den Wert für Trefferpunkte."""
        self.hitpoints = hp

    def get_hitpoints(self):
        """Rueckgabe der Trefferpunkte (Hitpoints)."""
        return self.hitpoints

    def set_cover_bonus(self, bonus):
        """Setzt den Wert für Deckungsbonus."""
        if bonus >= 0:
            self.cover_bonus = bonus
            self.attackable = True
        elif bonus == -1:
            self.attackable = False
            self.cover_text = "100%"
            print(f"{self.race} {self.name} ist nicht angreifbar, hat volle Deckung!")
        else:
            self.attackable = True

    def get_cover_bonus(self):
        """Rueckgabe der Deckungsbonus ."""
        return self.cover_bonus

    def set_initiative(self, initative_roll):
        """Setzt den Wert für Initative. Ergibt sich aus einem Initativwurf plus Geschicklichkeitsmodifikator."""
        self.initiative = initative_roll + self.dexterity_mod

    def get_initative(self):
        """Rueckgabe der Initiative des Charkaters (Hitpoints)."""
        return self.initiative

    def set_damage(self, damage):
        """Setzt den erlittenen Schaden.
        Der Schaden wird von den Trefferpunkten abgezogen, sofern der Charakter im Status angreifbar ist."""
        if self.attackable == True:
            self.hitpoints = self.hitpoints - damage
        else:
            print("Kann nicht angegriffen werden!")

    def set_status(self, status):
        """Setzt den Status. Möglich sind: 'aktiv', 'ohnmacht', 'tot'. """
        possible = ["aktiv", "ohnmacht", "tot"]
        if status.lower() in possible:
            self.status = status
        else:
            print("Statuswert nicht unterstützt. Bitte einen der folgenden angeben: aktiv, ohnmacht oder tot")

    def get_status(self, status):
        """Rueckgabe des character status (aktiv, ohnmacht, tot)."""
        return self.status

    def set_attackable(self, bool:bool):
        """Setzt den Wert für Angreifbarkeit.
        Bspw. hinter einen vollen Deckung kann nicht angegriffen werden.
        So das dann Angreifbarkeit auf False gesetzt werden muss."""
        self.attackable = bool

    def is_attackable(self):
        return self.attackable

    def set_description(self, desc):
        self.description = "Beschreibung: " + desc

    def get_description(self):
        return self.description

    def append_immunity(self, immunity):
        self.immunity.append(immunity)
    def set_immunity(self, immunity):
        self.immunity = immunity
    def get_immunity(self):
        return self.immunity
    def reset_immunity(self):
        self.immunity = []

    def append_resistence(self, resistence):
        self.resistence.append(resistence)
    def set_resistence(self, resistence):
        self.resistence = resistence
    def get_resistence(self):
        return self.resistence
    def reset_resistence(self):
        self.resistence = []

    def cls(self):
        system('cls' if name == 'nt' else 'clear')





