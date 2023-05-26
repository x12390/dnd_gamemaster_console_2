from creatures.creature_factory import CreatureFactory
from dice import Dice
from menue import cls, select_menu, cover_selection, select_menu_creatureObject



def defense(targetObj):
    while True:
        cls()
        print(f"Ziel: {targetObj.race} {targetObj.name}")
        print(f"RK: {targetObj.get_rk()}")
        print(f"HP: {targetObj.get_hitpoints()}")
        print(f"EP: {targetObj.get_ep()}")

        if targetObj.is_attackable():
            dmg = input("Gewürfelten Schaden eingeben (q für beenden): ")
            if dmg.isnumeric() and int(dmg) >= 0:
                targetObj.set_damage(int(dmg))
            else:
                break
        else:
            print("Hat volle Deckung und ist nicht angreifbar!")
            dmg = input("q für beenden: ")
            break

def combat(group):
    """Ausfuehrung eines Kampfes."""

    ep = 0
    cls()
    print("--- Kampf ---")
    #Deckung wählen
    cover_bonus = cover_selection()


    #Objekte der Kreaturen in einen Array laden.
    creatures = []
    print("Gegner betreten das Schlachtfeld...")
    for member in group:
        creature = CreatureFactory.create_creature(member)
        creature.set_cover_bonus(cover_bonus)
        creatures.append(creature)
        print(f"{(creature.race).upper()} <<{creature.name}>>, RK: {creature.rk}, HP: {creature.hitpoints}, EP: {creature.ep}")


    #Initative wuerfeln, einmal fuer die gesamte Gruppe
    group_initiative = Dice().roll_initiative()
    print("\n--- INITIATIVE --- \nInitiative der Gegner: ", group_initiative)

    while True:
        cls()
        if len(creatures) < 1:
            print(f"Der Kampf brachte {ep} Erfahrungspunkte (EP).")
            return ep
            break

        choice = select_menu("Gegneraktion im Kampf", ["Fernangriff", "Nahangriff", "Verteidigung", "Fliehen", "Deckung wechseln", "Gruppe anzeigen"])
        if choice == 1:
            # Fernangriff wuerfeln
            for creature in creatures:
                print(creature.attack_ranged())

        elif choice == 2:
            # Nahangriff wuerfeln
            for creature in creatures:
                if creature.is_attackable():
                    #nur wer angreifbar ist, kann auch in den Nahkampf
                    print(creature.attack_close())

        elif choice == 3:
            # Verteidigung. Spieler wuerfeln Angriff [hp,dmg] und bestimmen wer angegriffen wird.
            # 1.) Auswahl Ziel: ORK
            # 2.) Anzeige: RK und HP und Deckung
            # 3.) Eingabe Damage wenn RK mit hp überschritten wurde! Damage von hp der Kreatur abziehen.
            # 4.) Zustandsprüfung: hp=0 : Ohnmacht, hp<=0 : Tod (Löschen aus Gruppe) aber EP merken
            # 5.) Gruppe leer = SIEG EP anzeigen
            cls()

            #Zielauswahl
            tarCreature = select_menu_creatureObject("Zielauswahl", creatures)
            if tarCreature is not None:
                defense(tarCreature)
                if tarCreature.get_hitpoints() == 0:
                    print(f"{tarCreature.race} ist ohnmächtig.")
                elif tarCreature.get_hitpoints() < 0:
                    print(f"{tarCreature.race} ist tot.")
                    ep += tarCreature.get_ep()
                    creatures.remove(tarCreature)

        elif choice == 4:
            # Fliehen
            # Eingabefeld für Gelegenheitswurf der Spieler eingeben, dieser verwendet seine "Reaktion"
            print("Rüüüückzug! Wir hauen ab!")

        elif choice == 5:
            # Deckung wechseln
            cover_bonus = cover_selection()
            print("New cover bonus: " + str(cover_bonus))
            for creature in creatures:
                creature.set_cover_bonus(cover_bonus)

        elif choice == 6:
            # Gruppe anzeigen
            while True:
                cls()
                for creature in creatures:
                        creature.show_attributes()
                input("q für beenden: ")
                break






#print(combat(["Ork", "Veteran", "Riesenspinne"]))