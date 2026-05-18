from CLASSES.ENTITY import ENTITY
from PUBLIC.Public_Enums import _SIDE, _GENDER, _ATTRIBUTE, _DAMAGE_TYPE, _HIERARCHY
from PUBLIC.Public_Standards import *
from PUBLIC.Public_Random_Generators import Generate_Random_Kimera_Name
from CLASSES.BASIC_ATTACK import Melee_Natural_Attack, Ranged_Natural_Attack
from CLASSES.SKILLS import Fireball, Vampiric_Bite
class KIMERA(ENTITY):
    def __init__(self, 
                 Name, 
                 Gender, 
                 Muscles, Bones, Haste, Brain, Memory, Faith, 
                 Skills, 
                 Passives, 
                 Mutations, 
                 Basic_Attacks,
                 Hierarchy_Level,
                 Side = _SIDE.PLAYER):
        super().__init__(Name, 
                         Gender, 
                         Muscles, Bones, Haste, Brain, Memory, Faith, 
                         Skills, 
                         Passives, 
                         Mutations, 
                         Basic_Attacks, 
                         Side)
        self.Hierarchy_Level = Hierarchy_Level
        self.Out = False
        self.Age = 1
        self.Exhausted = False
        
    @classmethod
    def Breeding_Between(cls, First_Parent: KIMERA, 
                         Second_Parent: KIMERA, 
                         Breeding_Quality: int, 
                         Mutation_Rate: int, 
                         Mutation_Quality: int):
        
        def Hereditary_Attribute(First_Parent_Stat, Second_Parent_Stat, Breeding_Quality, Mutation_Rate, Mutation_Quality):
            Random_Breeding_Number = random.randint(1, 100)
            
            #DECIDES WHICH PARENT ATTRIBUTE THE CHILD WILL INHERIT
            if (Random_Breeding_Number + Breeding_Quality) > 50:
                Parent_Stat_Choosed = max(First_Parent_Stat, Second_Parent_Stat)
            else:
                Parent_Stat_Choosed = min(First_Parent_Stat, Second_Parent_Stat)
                
            Random_Mutation_Number = random.randint(1, 100)
            
            #DECIDES IF THE MUTATION WILL OCCUR
            if (Random_Mutation_Number + Mutation_Rate) >= 96:
                Mutation_Result_Roll = random.randint(1, 100)
            
            #DECIDES IF THE MUTATION WILL BE GOOD OR BAD
                if (Mutation_Result_Roll + Mutation_Quality) > 45:
                    Parent_Stat_Choosed += 1
                else:
                    Parent_Stat_Choosed -= 1
                    
            #RETURN DA FUNÇÃO
            return Parent_Stat_Choosed
        
        def Inherit_Mutations(First_Parent, Second_Parent):
            Parents_Mutations = set(First_Parent.Mutations + Second_Parent.Mutations)
            Parents_Mutations_Without_Repetition = list(Parents_Mutations)
            if Parents_Mutations:
                return random.sample(Parents_Mutations_Without_Repetition, 
                int((len(Parents_Mutations_Without_Repetition) + random.randint(-1, 1))/2))
            return []
        
        def Inherit_Abilities(First_Parent_Abilities, Second_Parent_Abilities, Breeding_Quality):
            Parents_Abilities = First_Parent_Abilities + Second_Parent_Abilities
            Random_Skill_Number = (random.randint(1, 100) + Breeding_Quality)
            if Parents_Abilities:
                if Random_Skill_Number >= 60:
                    return [random.choice(Parents_Abilities)]
                return []
            return []
        
        def Child_Hierarchy(First_Parent, Second_Parent):
            if First_Parent.Hierarchy_Level == _HIERARCHY.QUEEN or Second_Parent.Hierarchy_Level == _HIERARCHY.QUEEN:
                return _HIERARCHY.PRINCESS
            return _HIERARCHY.COMMONER
                
            
        return cls(Generate_Random_Kimera_Name(), 
                   
                random.choice([_GENDER.MALE, _GENDER.FEMALE]) if random.randint(1, 100) <= 85 else _GENDER.HERMAPHRODITE,
                
                Hereditary_Attribute(First_Parent.ATTRIBUTES[_ATTRIBUTE.MUSCLES], 
                                     Second_Parent.ATTRIBUTES[_ATTRIBUTE.MUSCLES], 
                                     Breeding_Quality, Mutation_Rate, Mutation_Quality),
                
                Hereditary_Attribute(First_Parent.ATTRIBUTES[_ATTRIBUTE.BONES], 
                                     Second_Parent.ATTRIBUTES[_ATTRIBUTE.BONES], 
                                     Breeding_Quality, Mutation_Rate, Mutation_Quality),
                
                Hereditary_Attribute(First_Parent.ATTRIBUTES[_ATTRIBUTE.HASTE], 
                                     Second_Parent.ATTRIBUTES[_ATTRIBUTE.HASTE], 
                                     Breeding_Quality, Mutation_Rate, Mutation_Quality),
                
                Hereditary_Attribute(First_Parent.ATTRIBUTES[_ATTRIBUTE.BRAIN], 
                                     Second_Parent.ATTRIBUTES[_ATTRIBUTE.BRAIN], 
                                     Breeding_Quality, Mutation_Rate, Mutation_Quality),
                
                Hereditary_Attribute(First_Parent.ATTRIBUTES[_ATTRIBUTE.MEMORY], 
                                     Second_Parent.ATTRIBUTES[_ATTRIBUTE.MEMORY], 
                                     Breeding_Quality, Mutation_Rate, Mutation_Quality),
                
                Hereditary_Attribute(First_Parent.ATTRIBUTES[_ATTRIBUTE.FAITH], 
                                     Second_Parent.ATTRIBUTES[_ATTRIBUTE.FAITH], 
                                     Breeding_Quality, Mutation_Rate, Mutation_Quality),
                
                Inherit_Abilities(First_Parent.Skills, Second_Parent.Skills, Breeding_Quality),
                
                Inherit_Abilities(First_Parent.Passives, Second_Parent.Passives, Breeding_Quality),
                
                Inherit_Mutations(First_Parent, Second_Parent),
                
                [random.choice([First_Parent.Original_Attack, Second_Parent.Original_Attack])],
                
                Child_Hierarchy(First_Parent, Second_Parent)
                
        )
        
    @classmethod
    def Generate_Random(cls, Hierarchy_Level, Random_Quality):
        def Random_Attribute():
            Random_Generator = (random.randint(1, 1000) + Random_Quality)
            if Random_Generator <= 193:
                return 4
            elif Random_Generator <= 879:
                return 5
            else:
                return 6
        return cls(
            Generate_Random_Kimera_Name(),
            random.choice([_GENDER.MALE, _GENDER.FEMALE]) if random.randint(1, 100) <= 85 else _GENDER.HERMAPHRODITE,
            Random_Attribute(),
            Random_Attribute(),
            Random_Attribute(),
            Random_Attribute(),
            Random_Attribute(),
            Random_Attribute(), 
            random.choice([Vampiric_Bite, Fireball
                           ]),
            [],
            [],
            [random.choice([Melee_Natural_Attack, Ranged_Natural_Attack])],
            Hierarchy_Level
        )
        