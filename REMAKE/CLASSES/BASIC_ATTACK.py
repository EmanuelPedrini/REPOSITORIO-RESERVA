from PUBLIC.Public_Standards import *
from PUBLIC.Public_Enums import _DAMAGE_TYPE, _SIDE, _ATTRIBUTE, _ATTACK_DISTANCE, _GENDER
from PUBLIC.Public_Classes import DAMAGE
from SYSTEMS.Command_System import Loop_Input, Target_Choice
# from SYSTEMS.Combat_System import COMBAT_SYSTEM


#implementando um sistema de ataque básico diferente baseados nos antigos, usando ataque basic antigo e skill, agora vai ficar mais parecido com uma skill
class Effect:
    def Apply(self, Attacker, Target, Combat):
        return ""

class Simple_Damage_Effect(Effect):
    def __init__(self, Attribute, Multiplier, 
                 Critical_Chance_Type, Critical_Multiplier_Type,
                 Vampirism_Type,
                 Type: _DAMAGE_TYPE):
        
        self.Multiplier = Multiplier
        self.Attribute = Attribute
        self.Type = Type
        self.Critical_Chance_Type = Critical_Chance_Type
        self.Critical_Multiplier_Type = Critical_Multiplier_Type
        self.Vampirism_Type = Vampirism_Type

    def Apply(self, Attacker, Target, Combat):
        
        Base_Amount = Attacker.Total_Attribute(self.Attribute)
        Damage = int(Base_Amount * self.Multiplier)
        if self.Critical_Chance_Type(Attacker):
            Damage = int(Damage * self.Critical_Multiplier_Type(Attacker))

        Damage_Taken_After_Resistances = Target.Take_Damage(DAMAGE(Damage, self.Type, Attacker))
        Vampirism = int(self.Vampirism_Type(Attacker, Damage_Taken_After_Resistances))
        if Vampirism > 0:
            Real_Heal = Attacker.Heal(Vampirism)
            if Real_Heal > 0:
                return f"-> {Target.Name} took {Damage_Taken_After_Resistances} damage, {Attacker.Name} healed {Real_Heal} HEALTH!\n"
            return f"-> {Target.Name} took {Damage_Taken_After_Resistances} damage, {Attacker.Name} healed HEALTH, but is already FULL HEALED!\n"
        return f"-> {Target.Name} took {Damage_Taken_After_Resistances} damage\n"

class TARGETING:
    @staticmethod
    def Enemy(Attacker, Combat):
        Enemy_Targets = Combat.Get_Enemy_Team(Attacker)
        if not Enemy_Targets:
            return []
        if Attacker.Side == _SIDE.PLAYER:
            Choosed_Target = Target_Choice(Enemy_Targets)
        elif Attacker.Side == _SIDE.ENEMY:
            if not Enemy_Targets:
                return []
            else:
                return[random.choice(Enemy_Targets)]
        if not Enemy_Targets:
            return []
        return [Choosed_Target]

    @staticmethod
    def Self(Attacker, Combat):
        return [Attacker]

    @staticmethod
    def All_Enemies(Attacker, Combat):
        return Combat.Get_Enemy_Team(Attacker)
    
    @staticmethod
    def All_Ally(Attacker, Combat):
        return Combat.Get_Ally_Team(Attacker) 

class Hit_Checking:
    
    @staticmethod
    def Attack_Roll(Target):
        Entity_Dodge = Target.Total_Attribute(_ATTRIBUTE.DODGE)
        return (random.randint(1, 100) > Entity_Dodge)
    
    @staticmethod
    def Always_Hit(Mibu):
        return True
    
    @staticmethod
    def Static_Chance(Mibu):
        return random.randint(1, 100) > 50

class Critical_Checking:
    
    @staticmethod
    def Critical_Roll(Attacker):
        Entity_Critical_Chance = Attacker.Total_Attribute(_ATTRIBUTE.CRITICAL_CHANCE)
        return random.randint(1, 100) <= Entity_Critical_Chance
    
    @staticmethod
    def Dont_Critical_Hit(Mibu):
        return False
    
    @staticmethod
    def All_or_Nothing(Mibu):
        return (random.randint(1,100)) > 50

class Critical_Style:
    @staticmethod
    def Basic_Critical(Attacker):
        return Attacker.Total_Attribute(_ATTRIBUTE.CRITICAL_MULTIPLIER)
    
    @staticmethod
    def Fixed_Critical(Mibu):
        return 2
    
class Vampirism_Checking:
    
    @staticmethod
    def Basic_Vampirism(Attacker, Damage):
        return Damage * (Attacker.Total_Attribute(_ATTRIBUTE.VAMPIRISM)/100)

class _BASIC_ATTACK:
    def __init__(self,
                 ID: str,
                 Name: str, 
                 Effects, 
                 
                 Target_Type: TARGETING,
                 Attack_Distance: _ATTACK_DISTANCE,
                 
                 Quantity: int,
                 Hit_Check: Hit_Checking):
        
        self.ID  = ID
        self.Name = Name
        self.Effects = Effects
        self.Target_Type = Target_Type
        
        self.Attack_Distance = Attack_Distance
        
        self.Quantity = Quantity
        self.Hit_Check = Hit_Check
    
    @staticmethod
    def Counter_Attack_Roll(Target):
        Entity_Counter = Target.Total_Attribute(_ATTRIBUTE.COUNTERATTACK)
        return random.randint(1, 100) <= Entity_Counter
    
    def Basic_Attack(self, Attacker, Combat):
        Valid_Targets = self.Target_Type(Attacker, Combat)
        
        if not Valid_Targets:
            return "Mibu!"
        Report = [f"{Attacker.Name} used {'his' if Attacker.Gender == _GENDER.MALE else 'her'} BASIC ATTACK!\n"]
        
        for Target in Valid_Targets:
            if self.Hit_Check(Target):
                for Quant in range(self.Quantity):
                    for Effect in self.Effects:
                        Result = Effect.Apply(Attacker, Target, Combat)
                        if Result:
                            Report.append(Result)
            else:
                Report.append(f"-> {Attacker.Name} missed {Target.Name}!")
            
        return "".join(Report)
                
    def __repr__(self):
        if self is None: return "INEXISTENT"
        else:
            return (
                f"{self.Name}"
            )




Melee_Natural_Attack = _BASIC_ATTACK(
    "melee_natural_attack",
    "BASIC ATTACK ( MELEE )",
    [Simple_Damage_Effect(_ATTRIBUTE.MUSCLES, 10,
                        Critical_Checking.Critical_Roll, 
                        Critical_Style.Basic_Critical, 
                        Vampirism_Checking.Basic_Vampirism,  
                        _DAMAGE_TYPE.BLUDGEONING)
     ],
    TARGETING.Enemy,
    _ATTACK_DISTANCE.MELEE,
    3,
    Hit_Checking.Attack_Roll,
)

Ranged_Natural_Attack = _BASIC_ATTACK(
    "ranged_natural_attack",
    "RANGED ATTACK",
    [Simple_Damage_Effect(_ATTRIBUTE.HASTE, 9,
                        Critical_Checking.Critical_Roll, 
                        Critical_Style.Basic_Critical, 
                        Vampirism_Checking.Basic_Vampirism,  
                        _DAMAGE_TYPE.BLUDGEONING)
     ],
    TARGETING.Enemy,
    _ATTACK_DISTANCE.RANGED,
    1,
    Hit_Checking.Attack_Roll,
)

Melee_Spin_Attack = _BASIC_ATTACK(
    "melee_spin_attack",
    "SPIN ATTACK",
    [Simple_Damage_Effect(_ATTRIBUTE.MUSCLES, 8,
                        Critical_Checking.Dont_Critical_Hit, 
                        Critical_Style.Basic_Critical, 
                        Vampirism_Checking.Basic_Vampirism,  
                        _DAMAGE_TYPE.BLUDGEONING)
     ],
    TARGETING.All_Enemies,
    _ATTACK_DISTANCE.MELEE,
    1,
    Hit_Checking.Attack_Roll,
)