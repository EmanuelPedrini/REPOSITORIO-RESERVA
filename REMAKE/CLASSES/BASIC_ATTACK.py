from PUBLIC.Public_Standards import *
from PUBLIC.Public_Enums import _DAMAGE_TYPE

#implementando um sistema de ataque básico diferente baseados nos antigos, usando ataque basic antigo e skill, agora vai ficar mais parecido com uma skill
class _SKILL:
    def __init__(self,
                 ID: int,
                 Name: str, 
                 Effects, 
                 Target_Type,
                 Damage_Type,
                 Calculation):
        
        self.ID  = ID
        self.Name = Name
        self.Effects = Effects
        self.Damage_Type = Damage_Type
        self.Calculation = Calculation
        self.Target_Type = Target_Type
        
        def Attack(self, Caster, Combat):
            Enemy_Targets = self.Target_Type(Caster, Combat)
            if not Enemy_Targets:
                return f"{Caster.Name} tried to ATTACK, but NO Enemy_Targets!"
            Report [f"{Caster.Name} used his BASIC ATTACK!"]






            for target in Enemy_Targets:
                # Report.append(f"-> {target.Name}")
                for effect in self.Effects:
                    result = effect.Apply(Caster, target, Combat)
                    if result:
                        Report.append(result)

            return "\n".join(Report)
        return f"{Caster.Name} doesn't have sufficient mana to cast {self.Name}"
    
    def __repr__(self):
        if self is None: return "INEXISTENT"
        else:
            return (
                f"HELLO I'AM A SKILL"
            )

class Effect:
    def Apply(self, Caster, Target, Combat):
        return ""

class DamageEffect(Effect):
    def __init__(self, Multiplier, Attribute, Type: _DAMAGE_TYPE):
        
        self.Multiplier = Multiplier
        self.Attribute = Attribute
        self.Type = Type
    

    def Apply(self, Caster, Target, Combat):
        
        Base_Amount = self.Attribute(Caster)
        damage = int(Base_Amount * self.Multiplier)

        Target.Take_Damage(DAMAGE(damage, self.Type, Caster))

        return f"-> {Target.Name} took {damage} damage"

class FixedDamageEffect(Effect):
    def __init__(self, Amount, Type: _DAMAGE_TYPE):
        self.Amount = Amount
        self.Type = Type

    def Apply(self, Caster, Target, Combat):
        Target.Take_Damage(DAMAGE(self.Amount, self.Type, Caster))

        return f"-> {Target.Name} took {self.Amount} damage"


class HealEffect(Effect):
    def __init__(self, Attribute, Multiplier):
        
        self.Multiplier = Multiplier
        self.Attribute = Attribute

    def Apply(self, Caster, Target, Combat):
        Base_Amount = self.Attribute(Caster)
        Healed_Amount = int(Base_Amount * self.Multiplier)

        Target.Heal(Healed_Amount)

        return f"-> {Target.Name} healed {Healed_Amount} HP"

class FixedHealEffect(Effect):
    def __init__(self, Amount):
        self.Amount = Amount
        
    def Apply(self, Caster, Target, Combat):
        Target.Heal(self.Amount)

        return f"-> {Target.Name} healed {self.Amount} HP"


class ShieldEffect(Effect):
    def __init__(self, Amount):
        self.Amount = Amount

    def Apply(self, Caster, Target, Combat):
        Target.Shield += self.Amount
        return f"-> {Target.Name} gained {self.Amount} shield"

class HealEffect(Effect):
    def __init__(self, Multiplier, Attribute):
        
        self.Multiplier = Multiplier
        self.Attribute = Attribute

    def Apply(self, Caster, Target, Combat):
        Base_Amount = self.Attribute(Caster)
        Healed_Amount = int(Base_Amount * self.Multiplier)

        Target.Heal(Healed_Amount)

        return f"-> {Target.Name} healed {Healed_Amount} HP"

class Targeting:
    @staticmethod
    def Enemy(Caster, Combat):
        Enemy_Targets = Combat.Get_Enemy_Team(Caster)
        if Caster.Side == _SIDE.PLAYER:
            Choosed_Target = Target_Choice(Enemy_Targets)
        elif Caster.Side == _SIDE.ENEMY:
            if not Enemy_Targets:
                return []
            else:
                return[random.choice(Enemy_Targets)]
        if not Enemy_Targets:
            return []
        return [Choosed_Target]

    @staticmethod
    def Self(Caster, Combat):
        return [Caster]

    @staticmethod
    def All_Enemies(Caster, Combat):
        return Combat.Get_Enemy_Team(Caster)
    
    @staticmethod
    def All_Ally(Caster, Combat):
        return Combat.Get_Ally_Team(Caster) 

Fireball = _SKILL(
    "fireball_skill",
    "Fireball",
    50,
    [FixedDamageEffect(120, _DAMAGE_TYPE.FIRE)],
    Targeting.All_Enemies
)
Vampiric_Bite = _SKILL(
    "vampiric_bite_skill",
    "Vampiric Bite",
    15,
    [FixedDamageEffect(20, _DAMAGE_TYPE.MALIGNANT)],
    Targeting.Enemy
)

class COMBAT_DATA:
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
    
    @staticmethod
    def Calculate_Damage(Attacker):
        #CALCS
        Attacker_Distance = Attacker.Current_Attack_Distance
        
        if Attacker_Distance == _ATTACK_DISTANCE.MELEE:
            Special_Attribute = _ATTRIBUTE.MELEE_DAMAGE
            Main_Attribute = (_ATTRIBUTE.MUSCLES)
           
        else:
            Special_Attribute = (_ATTRIBUTE.RANGED_DAMAGE)
            Main_Attribute = (_ATTRIBUTE.HASTE)
            
        Attack_Special_Value = (Attacker.Total_Attribute(Special_Attribute) * 0.75)
        Attack_Core_Value = (Attacker.Total_Attribute(Main_Attribute)) * 10
            
        Total_Attack = (Attack_Special_Value + Attack_Core_Value)
            
        if Attacker_Distance == _ATTACK_DISTANCE.RANGED:
            Total_Attack = 2 + ((Total_Attack) * 0.75)
        
        Total_Attack *= (1 + Attacker.Total_Attribute(_ATTRIBUTE.DAMAGE)/100)
            
        Static_Damage = max(0, int(Total_Attack * 0.90))
        Random_Damage = random.randint(0, int((Total_Attack) * 0.20))
        return Static_Damage + Random_Damage
    
    @staticmethod
    def Basic_Attack(Attacker, Target, Can_Counter: bool = True):
        if COMBAT_DATA.Attack_Roll(Target):
            Total_Damage_Amount = COMBAT_DATA.Calculate_Damage(Attacker)
            
            if COMBAT_DATA.Critical_Roll(Attacker):
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
                    if COMBAT_DATA.Counter_Attack_Roll(Target):
                        COMBAT_DATA.Basic_Attack(
                            Target,
                            Attacker,
                            Can_Counter = False
                        )
                
            #TESTES TEMPORÁRIOS!!!
            print(f"{Attacker.Name} attacked {Target.Name}, causing {Damage_Taken_After_Resistances} damage! \n{Target.Name} HP: {Target.Actual_Health} / {Target.Total_Attribute(_ATTRIBUTE.MAX_HEALTH)}")
            return True
        else:
            print(f"{Attacker.Name} missed a attack against {Target.Name}")
            return False
