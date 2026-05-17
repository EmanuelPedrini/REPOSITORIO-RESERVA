from SYSTEMS.Command_System import Loop_Input
from PUBLIC.Public_Standards import *
from PUBLIC.Public_Enums import _DAMAGE_TYPE, _SITE
from PUBLIC.Public_Classes import DAMAGE
from CLASSES.EVENT import EVENT

def Event_Generator(Rooms_Pool):
    Random_Event_Generator = random.randint(1, 1000)
    
    if Random_Event_Generator <= 242:
        return (_SITE.BAD_EVENT, random.choice(Bad_Events))

    elif Random_Event_Generator <= 537:
        return (_SITE.COMBAT, random.choice(Rooms_Pool))
    
    elif Random_Event_Generator <= 851:
        return (_SITE.NEUTRAL_EVENT, random.choice(Neutral_Events))
    
    else:
        return (_SITE.GOOD_EVENT, random.choice(Good_Events))

def Random_Member(Party):
    return random.choice(Party)

#Data TEST!!!!!!!!!!!!!!!!!!!!!!!!
def Nothing(Party):
    print("Nothing happens.")

def Avoid(Interacted):
    Roll = random.randint(1, 100)
    if Roll < 40:
        Damage_Taken = random.randint(45, 65)
        print(f"accidentaly stepped on the trap and taked {int(Damage_Taken)} damage!")
    else:
        print(f"avoided the trap in a involuntary reflex!")

def Drink_Fountain(Interacted):
    Heal = random.randint(50, 65)
    print(f"The water have a taste of marshmallows and honey, you fell your body get refilled with jovial energy!")


Stones_on_the_Path = EVENT("STONES IN THE PATH", 
                        "You encounter different rocks in the path and you decide to take a look",
    [
    ("Look under the rocks", Nothing)
    ]
)

Stepping_on_Bear_Trap = EVENT(
    "BEAR TRAP?!!", 
    "In a moment of distraction, you look to the ETERNAL FIRE HELL, but as you" \
    "return to reality, you realize that your feet is going on the direction of a BEAR TRAP!",
    [
        ("Avoid!", Avoid)
    ]
)

Healing_Fountain =  EVENT(
    "HEALING FOUNTAIN", 
    f"Found a imposing fountain with healing magic simbols, Drink?",
    [
        ("Ignore", Nothing),
        ("Drink", Drink_Fountain)
    ]
)

Good_Events = [Healing_Fountain]
Neutral_Events = [Stones_on_the_Path]
Bad_Events = [Stepping_on_Bear_Trap]
