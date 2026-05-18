from CLASSES.ROOM import ROOM
from CLASSES.ENTITY import ENTITY, ATTRIBUTE_MODIFIER
from PUBLIC.Public_Enums import _SIDE, _GENDER, _ATTACK_DISTANCE, _DAMAGE_TYPE, _ATTRIBUTE, _MODIFIER_TYPE, _TYPE_RESISTANCES
from PUBLIC.Public_Random_Generators import Keyboard_Smash_Generator
from PUBLIC.Public_Standards import *
from CLASSES.BASIC_ATTACK import Melee_Natural_Attack, Ranged_Natural_Attack, Melee_Spin_Attack

#CHAINSAW HEAD
Chainsaw_Head = ENTITY("Chainsaw Head",
                    _GENDER.MALE, 
                    2, 0, 2, 2, 3, 1, 
                    [], [], [], 
                    [Melee_Natural_Attack])

Chainsaw_Head.Attribute_Modifiers.extend([
    ATTRIBUTE_MODIFIER(_ATTRIBUTE.EXTRA_ATTACKS, _MODIFIER_TYPE.ADDITIVE, 1, Chainsaw_Head, "placeholder")
])
