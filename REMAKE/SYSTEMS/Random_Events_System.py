from SYSTEMS.Command_System import Loop_Input
from PUBLIC.Public_Standards import *
from PUBLIC.Public_Enums import _DAMAGE_TYPE, _SITE
from PUBLIC.Public_Classes import DAMAGE
from CLASSES.EVENT import EVENT, Healing_Fountain, Stepping_on_Bear_Trap, Stones_on_the_Path
def Event_Generator(Rooms_Pool):
    Random_Event_Generator = random.randint(1, 1000)
    
    if Random_Event_Generator <= 212:
        return (_SITE.BAD_EVENT, random.choice(Bad_Events))

    elif Random_Event_Generator <= 537:
        return (_SITE.COMBAT, random.choice(Rooms_Pool))
    
    elif Random_Event_Generator <= 851:
        return (_SITE.NEUTRAL_EVENT, random.choice(Neutral_Events))
    
    else:
        return (_SITE.GOOD_EVENT, random.choice(Good_Events))

Good_Events = [Healing_Fountain]
Neutral_Events = [Stones_on_the_Path]
Bad_Events = [Stepping_on_Bear_Trap]