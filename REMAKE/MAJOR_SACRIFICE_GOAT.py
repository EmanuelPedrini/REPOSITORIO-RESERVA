from CLASSES.KIMERA import KIMERA
from CLASSES.ENTITY import ATTRIBUTE_MODIFIER, _MODIFIER_TYPE
from SYSTEMS.Combat_System import COMBAT_SYSTEM
from CLASSES.BASIC_ATTACK import Melee_Natural_Attack, Melee_Spin_Attack, Ranged_Natural_Attack
from DATA.TEST_FILE import Chainsaw_Head
from PUBLIC.Public_Enums import _GENDER, _ATTACK_DISTANCE, _DAMAGE_TYPE, _ATTRIBUTE, _TYPE_RESISTANCES, _SIDE, _HIERARCHY
from CLASSES.SKILLS import Fireball, Vampiric_Bite

Joana_Mata_Galinha = KIMERA("Joana Mata-Galinha", 
                            _GENDER.FEMALE,
                            6, 7, 2, 3, 1, 2,
                            [Fireball, Vampiric_Bite], [], [],
                            [Melee_Spin_Attack],
                            _HIERARCHY.COMMONER)

Joao_Mata_Galinha = KIMERA("João Mata-Galinha", 
                            _GENDER.MALE,
                            3, 3, 3, 1, 1, 2,
                            [], [], [], 
                            [Melee_Natural_Attack],
                            _HIERARCHY.COMMONER)

Mariazinha_Mata_Frango = KIMERA("Mariazinha Mata-Frango", 
                            _GENDER.FEMALE,
                            2, 10, 2, 2, 2, 2,
                            [Fireball, Vampiric_Bite], [], [], 
                            [Ranged_Natural_Attack],
                            _HIERARCHY.COMMONER)

Mariazinha_Mata_Frango.Attribute_Modifiers.extend([
    ATTRIBUTE_MODIFIER(_ATTRIBUTE.VAMPIRISM, _MODIFIER_TYPE.ADDITIVE, 50, Mariazinha_Mata_Frango, "placeholder")
])

New_Kimera = KIMERA.Breeding_Between(Joana_Mata_Galinha, Joao_Mata_Galinha, 29, 29, 29)

COMBAT_SYSTEM([New_Kimera], [Chainsaw_Head]).Combat_Between()