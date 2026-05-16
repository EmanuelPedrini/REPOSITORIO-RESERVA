from CLASSES.ENTITY import ENTITY
from SYSTEMS.Combat_System import COMBAT_DATA, COMBAT_SYSTEM
from PUBLIC.Public_Enums import _GENDER, _ATTACK_DISTANCE, _DAMAGE_TYPE, _ATTRIBUTE, _TYPE_RESISTANCES, _SIDE
from CLASSES.SKILLS import Fireball
Joana_Mata_Galinha = ENTITY("Joana Mata-Galinha", 
                            _GENDER.FEMALE,
                            6, 7, 2, 3, 1, 2,
                            [], [], [], 
                            _ATTACK_DISTANCE.MELEE,
                            _DAMAGE_TYPE.BLUDGEONING,
                            Side=_SIDE.PLAYER)

Joao_Mata_Galinha = ENTITY("João Mata-Galinha", 
                            _GENDER.MALE,
                            3, 3, 3, 1, 1, 2, 
                            [], [], [], 
                            _ATTACK_DISTANCE.RANGED,
                            _DAMAGE_TYPE.BLUDGEONING, 
                            Side = _SIDE.PLAYER)

Mariazinha_Mata_Frango = ENTITY("Mariazinha Mata-Frango", 
                            _GENDER.FEMALE,
                            2, 2, 2, 2, 2, 2,
                            [], [], [], 
                            _ATTACK_DISTANCE.RANGED,
                            _DAMAGE_TYPE.BLUDGEONING)

Cassiano_Terrível = ENTITY("Cassiano Terrível", 
                            _GENDER.MALE,
                            1, 5, 3, 7, 7, 7,
                            [Fireball], [], [], 
                            _ATTACK_DISTANCE.MELEE,
                            _DAMAGE_TYPE.BLUDGEONING)

def PrH(W):
    print(f"{W.Name} / HP : {W.Actual_Health} / {W.Total_Attribute(_ATTRIBUTE.MAX_HEALTH)}")

#COMBAT_SYSTEM.Combat_Between([self, Joao_Mata_Galinha],[Joana_Mata_Galinha])
Combat = COMBAT_SYSTEM( [Joana_Mata_Galinha], [Mariazinha_Mata_Frango])
Combat.Combat_Between()