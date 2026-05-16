from CLASSES.ENTITY import ENTITY
from PUBLIC.Public_Enums import _SIDE
class KIMERA(ENTITY):
    def __init__(self, Name, 
                Gender, 
                Muscles, Bones, Haste, Brain, Memory, Faith, 
                Skills, Passives, Mutations, 
                Attack_Distance, 
                Attack_Type, 
                Side = _SIDE.PLAYER):
        super().__init__(Name, 
                        Gender, 
                        Muscles, Bones, Haste, Brain, Memory, Faith, 
                        Skills, Passives, Mutations, 
                        Attack_Distance, 
                        Attack_Type, 
                        Side)