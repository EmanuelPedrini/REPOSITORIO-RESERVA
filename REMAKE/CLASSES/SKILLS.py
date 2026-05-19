from PUBLIC.Public_Standards import *
from PUBLIC.Public_Classes import DAMAGE
from PUBLIC.Public_Enums import _DAMAGE_TYPE, _SIDE
from SYSTEMS.Command_System import Target_Choice

class _SKILL:
    def __init__(self,
                 ID: str,
                 Name: str, 
                 Mana_Cost: int,
                 Mana_Type, 
                 Effects, 
                 Target_Type,
                 Quantity):
        
        self.ID  = ID
        self.Name = Name
        self.Mana_Cost = Mana_Cost
        self.Mana_Type = Mana_Type
        self.Effects = Effects
        self.Target_Type = Target_Type
        self.Quantity = Quantity

    def Cast(self, Caster, Combat):
        if self.Mana_Type(Caster, self.Mana_Cost):
            Enemy_Targets = self.Target_Type(Caster, Combat)

            if not Enemy_Targets:
                return f"{Caster.Name} tried to use {self.Name}, but NO Enemy_Targets!"
            
            Report = [f"{Caster.Name} used {self.Name}!"]

            for target in Enemy_Targets:
                for Times in range(self.Quantity):
                    for effect in self.Effects:
                        result = effect.Apply(Caster, target, Combat)
                        if result:
                            Report.append(result)

            return "\n".join(Report)
        return f"{Caster.Name} can't cast {self.Name.upper()}!"
    
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

        Real_Damage = Target.Take_Damage(DAMAGE(damage, self.Type, Caster))

        return f"-> {Target.Name} took {Real_Damage} damage"

class FixedDamageEffect(Effect):
    def __init__(self, Amount, Type: _DAMAGE_TYPE):
        self.Amount = Amount
        self.Type = Type

    def Apply(self, Caster, Target, Combat):
        Real_Damage = Target.Take_Damage(DAMAGE(self.Amount, self.Type, Caster))

        return f"-> {Target.Name} took {Real_Damage} damage"

class FixedHealEffect(Effect):
    def __init__(self, Amount):
        self.Amount = Amount
        
    def Apply(self, Caster, Target, Combat):
        Real_Heal = Target.Heal(self.Amount)

        return f"-> {Target.Name} healed {Real_Heal} HP"

# VOU TER QUE MODIFICAR ISSO DEPOIS #
# class ShieldEffect(Effect):
#     def __init__(self, Amount):
#         self.Amount = Amount

#     def Apply(self, Caster, Target, Combat):
#         Target.Shield += self.Amount
#         return f"-> {Target.Name} gained {self.Amount} shield"

class HealEffect(Effect):
    def __init__(self, Multiplier, Attribute):
        
        self.Multiplier = Multiplier
        self.Attribute = Attribute

    def Apply(self, Caster, Target, Combat):
        
        Base_Amount = self.Attribute(Caster)
        Healed_Amount = int(Base_Amount * self.Multiplier)

        Real_Heal = Target.Heal(Healed_Amount)

        return f"-> {Target.Name} healed {Real_Heal} HP"
    
class MANA_TYPE:
    def Standard_Mana_Type(Caster, Mana_Cost):
        if Caster.Actual_Mana >= Mana_Cost:
            Caster.Use_Mana(Mana_Cost)
            return True
        return False 
    
class Targeting:
    @staticmethod
    def Enemy(Caster, Combat):
        Enemy_Targets = Combat.Get_Enemy_Team(Caster)
        if not Enemy_Targets:
            return []
        
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
    MANA_TYPE.Standard_Mana_Type,
    [FixedDamageEffect(120, _DAMAGE_TYPE.FIRE)],
    Targeting.All_Enemies,
    1
)

Vampiric_Bite = _SKILL(
    "vampiric_bite_skill",
    "Vampiric Bite",
    15,
    MANA_TYPE.Standard_Mana_Type,
    [FixedDamageEffect(20, _DAMAGE_TYPE.MALIGNANT)],
    Targeting.Enemy,
    1
)