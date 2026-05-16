from CLASSES.ROOM import ROOM
from CLASSES.ENTITY import ENTITY, ATTRIBUTE_MODIFIER
from PUBLIC.Public_Enums import _SIDE, _GENDER, _ATTACK_DISTANCE, _DAMAGE_TYPE, _ATTRIBUTE, _MODIFIER_TYPE, _TYPE_RESISTANCES
from PUBLIC.Public_Random_Generators import Keyboard_Smash_Generator
from PUBLIC.Public_Standards import *

#ERROR
Error = ENTITY(Keyboard_Smash_Generator(),
                    random.choice(_GENDER.MALE, _GENDER.FEMALE, _GENDER.HERMAPHRODITE), 
                    random.randint(4, 12), random.randint(4, 12), random.randint(4, 12), 
                    random.randint(4, 12), random.randint(4, 12), random.randint(4, 12), 
                    [], [], [], 
                    random.choice(_ATTACK_DISTANCE.MELEE, _ATTACK_DISTANCE.RANGED), 
                    random.choice(_DAMAGE_TYPE.SLASHING, _DAMAGE_TYPE.FIRE, 
                                  _DAMAGE_TYPE.FROST, _DAMAGE_TYPE.BLUDGEONING, 
                                  _DAMAGE_TYPE.RADIANT, _DAMAGE_TYPE.MALIGNANT,
                                  _DAMAGE_TYPE.ELECTRIC, _DAMAGE_TYPE.POISONOUS))

#BRAIN EATER
Brain_Eater = ENTITY("Brain Eater",
                    _GENDER.MALE, 
                    5, 5, 5, 5, 5, 5, 
                    [], [], [], 
                    _ATTACK_DISTANCE.RANGED, 
                    _DAMAGE_TYPE.BLUDGEONING)

#CHAINSAW HEAD
Chainsaw_Head = ENTITY("Chainsaw Head",
                    _GENDER.MALE, 
                    2, 0, 2, 2, 3, 1, 
                    [], [], [], 
                    _ATTACK_DISTANCE.MELEE, 
                    _DAMAGE_TYPE.SLASHING)

Chainsaw_Head.Attribute_Modifiers.extend([
    ATTRIBUTE_MODIFIER(_ATTRIBUTE.EXTRA_ATTACKS, _MODIFIER_TYPE.ADDITIVE, 1, "Natural")
])

Hell_Tormenter = ENTITY("Hell Tormenter",
                    _GENDER.MALE, 
                    3, 12, 2, 6, 7, 1, 
                    [], [], [], 
                    _ATTACK_DISTANCE.MELEE, 
                    _DAMAGE_TYPE.BLUDGEONING)

Hell_Tormenter.Attribute_Modifiers.extend([
    ATTRIBUTE_MODIFIER(_TYPE_RESISTANCES.SLASHING_RESISTANCE, _MODIFIER_TYPE.ADDITIVE, 25, "Natural"),
    ATTRIBUTE_MODIFIER(_TYPE_RESISTANCES.BLUDGEONING_RESISTANCE, _MODIFIER_TYPE.ADDITIVE, 25, "Natural")
])

Succubus = ENTITY("Succubus",
                    _GENDER.MALE, 
                    2, 0, 2, 2, 3, 1, 
                    [], [], [], 
                    _ATTACK_DISTANCE.MELEE, 
                    _DAMAGE_TYPE.SLASHING)

Succubus.Attribute_Modifiers.extend([
    ATTRIBUTE_MODIFIER(_ATTRIBUTE.EXTRA_ATTACKS, _MODIFIER_TYPE.ADDITIVE, 1, "Natural")
])

