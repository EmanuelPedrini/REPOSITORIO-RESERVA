from CLASSES.KIMERA import KIMERA
from SYSTEMS.Combat_System import COMBAT_DATA, COMBAT_SYSTEM
from PUBLIC.Public_Enums import _GENDER, _ATTACK_DISTANCE, _DAMAGE_TYPE, _ATTRIBUTE, _TYPE_RESISTANCES, _SIDE
from CLASSES.SKILLS import Fireball, Vampiric_Bite

Joana_Mata_Galinha = KIMERA("Joana Mata-Galinha", 
                            _GENDER.FEMALE,
                            6, 7, 2, 3, 1, 2,
                            [Fireball, Vampiric_Bite], [], [], 
                            _ATTACK_DISTANCE.MELEE,
                            _DAMAGE_TYPE.BLUDGEONING,
                            Side=_SIDE.PLAYER)

Joao_Mata_Galinha = KIMERA("João Mata-Galinha", 
                            _GENDER.MALE,
                            3, 3, 3, 1, 1, 2, 
                            [], [], [], 
                            _ATTACK_DISTANCE.RANGED,
                            _DAMAGE_TYPE.BLUDGEONING)

Mariazinha_Mata_Frango = KIMERA("Mariazinha Mata-Frango", 
                            _GENDER.FEMALE,
                            2, 200, 2, 2, 2, 2,
                            [Fireball, Vampiric_Bite], [], [], 
                            _ATTACK_DISTANCE.RANGED,
                            _DAMAGE_TYPE.BLUDGEONING)

New_Kimera = KIMERA.Breeding_Between(Mariazinha_Mata_Frango, Joao_Mata_Galinha, 0, 0, 0)
print(New_Kimera)