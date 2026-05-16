from PUBLIC.Public_Standards import *
from PUBLIC.Public_Classes import DAMAGE
from PUBLIC.Public_Enums import _DAMAGE_TYPE

class _SKILL:
    def __init__(self,
                 ID: int,
                 Name: str, 
                 Mana_Cost: int, 
                 Effects, 
                 Target_Type):
        
        self.ID  = ID
        self.Name = Name
        self.Mana_Cost = Mana_Cost
        self.Effects = Effects
        self.Target_Type = Target_Type

    def Can_Cast(self, Caster):
        return (Caster.Actual_Mana >= self.Mana_Cost)

    def Cast(self, Caster, Combat):
        Enemy_Targets = self.Target_Type(Caster, Combat)

        if not Enemy_Targets:
            return f"{Caster.Name} tried to use {self.Name}, but NO Enemy_Targets!"
        
        Caster.Actual_Mana -= self.Mana_Cost
        Report = [f"{Caster.Name} used {self.Name}!"]

        for target in Enemy_Targets:
            Report.append(f"-> {target.Name}")
            for effect in self.Effects:
                result = effect.Apply(Caster, target, Combat)
                if result:
                    Report.append(result)

        return "\n".join(Report)
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

        return f"{Target.Name} took {damage} damage"

class FixedDamageEffect(Effect):
    def __init__(self, Amount, Type: _DAMAGE_TYPE):
        self.Amount = Amount
        self.Type = Type

    def Apply(self, Caster, Target, Combat):
        Target.Take_Damage(DAMAGE(self.Amount, self.Type, Caster))

        return f"{Target.Name} took {self.Amount} damage"


class HealEffect(Effect):
    def __init__(self, Attribute, Multiplier):
        
        self.Multiplier = Multiplier
        self.Attribute = Attribute

    def Apply(self, Caster, Target, Combat):
        Base_Amount = self.Attribute(Caster)
        Healed_Amount = int(Base_Amount * self.Multiplier)

        Target.Heal(Healed_Amount)

        return f"{Target.Name} healed {Healed_Amount} HP"

class FixedHealEffect(Effect):
    def __init__(self, Amount):
        self.Amount = Amount
        
    def Apply(self, Caster, Target, Combat):
        Target.Heal(self.Amount)

        return f"{Target.Name} healed {self.Amount} HP"


class ShieldEffect(Effect):
    def __init__(self, Amount):
        self.Amount = Amount

    def Apply(self, Caster, Target, Combat):
        Target.Shield += self.Amount
        return f"{Target.Name} gained {self.Amount} shield"

class HealEffect(Effect):
    def __init__(self, Multiplier, Attribute):
        
        self.Multiplier = Multiplier
        self.Attribute = Attribute

    def Apply(self, Caster, Target, Combat):
        Base_Amount = self.Attribute(Caster)
        Healed_Amount = int(Base_Amount * self.Multiplier)

        Target.Heal(Healed_Amount)

        return f"{Target.Name} healed {Healed_Amount} HP"

class Targeting:
    @staticmethod
    def Enemy(Caster, Combat):
        Enemy_Targets = Combat.Get_Enemy_Team(Caster)
        if not Enemy_Targets:
            return []
        return [random.choice(Enemy_Targets)]

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
    100,
    [FixedDamageEffect(25, _DAMAGE_TYPE.FIRE)],
    Targeting.All_Enemies
)