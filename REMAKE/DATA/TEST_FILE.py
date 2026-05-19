from CLASSES.ROOM import ROOM
from CLASSES.ENTITY import ENTITY, ATTRIBUTE_MODIFIER
from PUBLIC.Public_Enums import _SIDE, _GENDER, _ATTACK_DISTANCE, _DAMAGE_TYPE, _ATTRIBUTE, _MODIFIER_TYPE, _TYPE_RESISTANCES, _DURATION
from PUBLIC.Public_Random_Generators import Keyboard_Smash_Generator
from PUBLIC.Public_Standards import *
from CLASSES.BASIC_ATTACK import Melee_Natural_Attack, Ranged_Natural_Attack, Melee_Spin_Attack, Chainsaw_Head_Natural_Attack

#CHAINSAW HEAD
Chainsaw_Head = ENTITY("Chainsaw Head",
                    _GENDER.HERMAPHRODITE, 
                    1, 0, 2, 2, 3, 1, 
                    [], [], [], 
                    [Chainsaw_Head_Natural_Attack])

Chainsaw_Head.Attribute_Modifiers.extend([
    ATTRIBUTE_MODIFIER(_ATTRIBUTE.EXTRA_ATTACKS, _MODIFIER_TYPE.ADDITIVE, 2, Chainsaw_Head, _DURATION.PERMANENT)
])

#===========================================================================================================================================#
#SUCCUBUS

Succubus = ENTITY("Succubus",
                    _GENDER.FEMALE, 
                    2, 0, 2, 2, 3, 1, 
                    [], [], [], 
                    [Melee_Natural_Attack])

Succubus.Attribute_Modifiers.extend([
    ATTRIBUTE_MODIFIER(_ATTRIBUTE.EXTRA_ATTACKS, _MODIFIER_TYPE.ADDITIVE, 1, Succubus, _DURATION.PERMANENT)
])

#===========================================================================================================================================#
#MINOTAUR

Minotaur = ENTITY("Minotaur",
                    _GENDER.MALE, 
                    4, 18, 2, 2, 3, 1, 
                    [], [], [], 
                    [Melee_Spin_Attack])

Succubus.Attribute_Modifiers.extend([
    ATTRIBUTE_MODIFIER(_TYPE_RESISTANCES.SLASHING_RESISTANCE, _MODIFIER_TYPE.ADDITIVE, 15, Minotaur,  _DURATION.PERMANENT),
    ATTRIBUTE_MODIFIER(_TYPE_RESISTANCES.BLUDGEONING_RESISTANCE, _MODIFIER_TYPE.ADDITIVE, 15, Minotaur, _DURATION.PERMANENT)
])

#===========================================================================================================================================#
#DEMON BUREAUCRAT

Demon_Bureaucrat = ENTITY("Demon Bureaucrat",
                    _GENDER.MALE, 
                    2, 0, 2, 2, 3, 1, 
                    [], [], [], 
                    [Melee_Natural_Attack])

Chainsaw_Head.Attribute_Modifiers.extend([
    ATTRIBUTE_MODIFIER(_ATTRIBUTE.EXTRA_ATTACKS, _MODIFIER_TYPE.ADDITIVE, 1, Demon_Bureaucrat,  _DURATION.PERMANENT)
])
