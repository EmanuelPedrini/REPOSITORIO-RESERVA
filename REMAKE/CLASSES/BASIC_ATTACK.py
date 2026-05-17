from PUBLIC.Public_Standards import *
from PUBLIC.Public_Enums import _DAMAGE_TYPE, _SIDE, _ATTRIBUTE, _ATTACK_DISTANCE
from PUBLIC.Public_Classes import DAMAGE
from SYSTEMS.Command_System import Loop_Input, Target_Choice
# from SYSTEMS.Combat_System import COMBAT_SYSTEM


#implementando um sistema de ataque básico diferente baseados nos antigos, usando ataque basic antigo e skill, agora vai ficar mais parecido com uma skill
class Effect:
    def Apply(self, Attacker, Target, Combat):
        return ""

class _BASIC_ATTACK:
    def __init__(self,
                 ID: str,
                 Name: str, 
                 Effects, 
                 
                 Target_Type,
                 Attack_Distance,
                 
                 Quantity,
                 Can_Critical_Hit,
                 Can_Apply_Vampirism):
        
        self.ID  = ID
        self.Name = Name
        self.Effects = Effects
        self.Target_Type = Target_Type
        
        self.Attack_Distance = Attack_Distance
        
        self.Quantity = Quantity
        self.Can_Critical_Hit = Can_Critical_Hit
        self.Can_Apply_Vampirism = Can_Apply_Vampirism
        
    @staticmethod
    def Attack_Roll(Target):
        Entity_Dodge = Target.Total_Attribute(_ATTRIBUTE.DODGE)
        return (random.randint(1, 100) > Entity_Dodge)

    @staticmethod
    def Critical_Roll(Attacker):
        Entity_Critical_Chance = Attacker.Total_Attribute(_ATTRIBUTE.CRITICAL_CHANCE)
        return random.randint(1, 100) <= Entity_Critical_Chance
    
    @staticmethod
    def Counter_Attack_Roll(Target):
        Entity_Counter = Target.Total_Attribute(_ATTRIBUTE.COUNTERATTACK)
        return random.randint(1, 100) <= Entity_Counter
    
    
    ############################################################
    
    @staticmethod
    def Calculate(self, Attacker):
        Attacker_Distance = self.Attack_Distance
        
        Total_Attack *= (1 + Attacker.Total_Attribute(_ATTRIBUTE.DAMAGE)/100)
            
        Static_Damage = max(0, int(Total_Attack * 0.90))
        Random_Damage = random.randint(0, int((Total_Attack) * 0.20))
        return Static_Damage + Random_Damage
    
    
    #############################################################
    
    def Attack(self, Attacker, 
                     Combat,
                     Can_Crit, 
                     Can_Counter: bool = True):
        
        Enemy_Targets = self.Target_Type(Attacker, Combat)
        
        if not Enemy_Targets:
            return f"{Attacker.Name} tried to ATTACK, but NO Enemy_Targets!"
            
        Report = [f"{Attacker.Name} used his BASIC ATTACK!"]
            
        for Target in Enemy_Targets:
            
            Report.append(f"-> {Target.Name}")
            
            for Effect in self.Effects:
                Result = Effect.Apply(Attacker, Target, Combat)
                if Result:
                    Report.append(Result)
    
    ##################################################################
    
        if self.Attack_Roll(Target):
            Total_Damage_Amount = self.Calculate(Attacker)
            
            if Can_Crit:
                if self.Critical_Roll(Attacker):
                    Total_Damage_Amount = int(Total_Damage_Amount * Attacker.Total_Attribute(_ATTRIBUTE.CRITICAL_MULTIPLIER))
                
            Damage_taken = DAMAGE(Total_Damage_Amount, 
                                Attacker.Current_Attack_Type, 
                                Attacker)
            
            Damage_Taken_After_Resistances = Target.Take_Damage(Damage_taken)
            Fatal_Attack = (Target.Actual_Health) <= 0
            
            Vampirism = Attacker.Total_Attribute(_ATTRIBUTE.VAMPIRISM)
            Target_Thorns = Target.Total_Attribute(_ATTRIBUTE.THORNS)
            
            if Vampirism > 0:
                Attacker.Heal(int(Damage_Taken_After_Resistances * Vampirism/100))
            
            if Target_Thorns > 0:
                if not Fatal_Attack:
                    Attacker.Take_Damage(DAMAGE(Target_Thorns, Target.Thorns_Type, Target, Fathal=False))
            
            if Can_Counter:
                if not Fatal_Attack:
                    if self.Counter_Attack_Roll(Target):
                        self.Basic_Attack(
                            Target,
                            Attacker,
                            Can_Counter = False
                        )
                        
        
        
        ######################################################
        
            print(f"{Attacker.Name} attacked {Target.Name}, causing {Damage_Taken_After_Resistances} damage! \n{Target.Name} HP: {Target.Actual_Health} / {Target.Total_Attribute(_ATTRIBUTE.MAX_HEALTH)}")
            return True
        else:
            print(f"{Attacker.Name} missed a attack against {Target.Name}")
            return False
        
        ####################################

    def __repr__(self):
        if self is None: return "INEXISTENT"
        else:
            return (
                f"HELLO I'AM A ATTACK"
            )














class DamageEffect(Effect):
    def __init__(self, Multiplier, Attribute, Type: _DAMAGE_TYPE):
        self.Multiplier = Multiplier
        self.Attribute = Attribute
        self.Type = Type
    

    def Apply(self, Attacker, Target, Combat):
        
        Base_Amount = self.Attribute(Attacker)
        damage = int(Base_Amount * self.Multiplier)

        Target.Take_Damage(DAMAGE(damage, self.Type, Attacker))

        return f"-> {Target.Name} took {damage} damage"

class FixedDamageEffect(Effect):
    def __init__(self, Amount, Type: _DAMAGE_TYPE):
        self.Amount = Amount
        self.Type = Type

    def Apply(self, Attacker, Target, Combat):
        Target.Take_Damage(DAMAGE(self.Amount, self.Type, Attacker))

        return f"-> {Target.Name} took {self.Amount} damage"


class HealEffect(Effect):
    def __init__(self, Attribute, Multiplier):
        
        self.Multiplier = Multiplier
        self.Attribute = Attribute

    def Apply(self, Attacker, Target, Combat):
        Base_Amount = self.Attribute(Attacker)
        Healed_Amount = int(Base_Amount * self.Multiplier)

        Target.Heal(Healed_Amount)

        return f"-> {Target.Name} healed {Healed_Amount} HP"

class FixedHealEffect(Effect):
    def __init__(self, Amount):
        self.Amount = Amount
        
    def Apply(self, Attacker, Target, Combat):
        Target.Heal(self.Amount)

        return f"-> {Target.Name} healed {self.Amount} HP"

class Targeting:
    @staticmethod
    def Enemy(Attacker, Combat):
        Enemy_Targets = Combat.Get_Enemy_Team(Attacker)
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


###################################################
Melee_Natural_Attack_Kimera = _BASIC_ATTACK(
    "melee_natural_attack_kimera",
    "BASIC ATTACK ( MELEE )",
    [FixedDamageEffect(120, _DAMAGE_TYPE.FIRE)],
    Targeting.All_Enemies,
    1,
    _ATTACK_DISTANCE.MELEE,
    True
)

