from creatures.creature import Creature
from configparser import ConfigParser

class CreatureFactory:
    @staticmethod
    def create_creature(creature_type: str, configfile='creatures.ini'):
        creature_type = creature_type.lower()
        if len(creature_type) > 0:
            config = ConfigParser()

            #get creature values from ini file
            config.read(configfile)

            #check if category exist
            if config.has_section(creature_type): #e.g. [ork]
                # create creature object
                creature = Creature()
                creature.set_race(creature_type)
                creature.set_size(config.get(creature_type, 'SIZE'))
                creature.set_description(config.get(creature_type, 'DESC'))
                creature.set_ep(int(config.get(creature_type, 'ep')))
                creature.set_hitpoints(int(config.get(creature_type, 'hp')))
                creature.set_rk(int(int(config.get(creature_type, 'rk'))))
                creature.set_strength(int(config.get(creature_type, 'STR')))
                creature.set_dexterity(int(config.get(creature_type, 'GES')))
                creature.set_constitution(int(config.get(creature_type, 'KON')))
                creature.set_intelligence(int(config.get(creature_type, 'INT')))
                creature.set_wisdom(int(config.get(creature_type, 'WEI')))
                creature.set_charisma(int(config.get(creature_type, 'CHA')))
                if config.has_option(creature_type, 'RESISTENCE'):
                    creature.set_resistence(config.get(creature_type, 'RESISTENCE'))
                if config.has_option(creature_type, 'IMMUNITY'):
                    creature.set_immunity(config.get(creature_type, 'IMMUNITY'))

                # close combat dice hitpoints
                for x in range(1,3):
                    try:
                        dice_type = config.get(creature_type, 'CLOSE_HP_DICE_' + str(x))
                        bonus = config.get(creature_type, 'CLOSE_HP_DICE_'+str(x)+'_BONUS')
                        creature.set_close_hitpoint_dice(dice_type,bonus)
                    except:
                        pass

                # close combat dice damage
                for x in range(1, 3):
                    try:
                        dice_type = config.get(creature_type, 'CLOSE_DMG_DICE_' + str(x))
                        bonus = config.get(creature_type, 'CLOSE_DMG_DICE_' + str(x) + '_BONUS')
                        creature.set_close_damage_dice(dice_type, bonus)
                    except:
                        pass


                #ranged combat dice hitpoints
                for x in range(1, 3):
                    try:
                        dice_type = config.get(creature_type, 'RANGED_HP_DICE_' + str(x))
                        bonus = config.get(creature_type, 'RANGED_HP_DICE_' + str(x) + '_BONUS')
                        creature.set_ranged_hitpoint_dice(dice_type, bonus)
                    except:
                        pass

                #ranged combat dice damage
                for x in range(1, 3):
                    try:
                        dice_type = config.get(creature_type, 'RANGED_DMG_DICE_' + str(x))
                        bonus = config.get(creature_type, 'RANGED_DMG_DICE_' + str(x) + '_BONUS')
                        creature.set_ranged_damage_dice(dice_type,bonus)
                    except:
                        pass

            else:
                raise ValueError(f"Creature type {creature_type} not supported.")
                creature = None

            return creature


# creatureObj = CreatureFactory.create_creature("Ghul", "../creatures.ini")
# print(creatureObj.get_race())
# print(creatureObj.get_ep())
# print(creatureObj.get_hitpoints())
# creatureObj.show_attributes()