from CLASSES.SKILLS import _SKILL
from CLASSES.PASSIVES import _PASSIVE
from CLASSES.MUTATIONS import _MUTATIONS
from PUBLIC.Public_Enums import _ATTRIBUTE, _ATTACK_DISTANCE, _TYPE_RESISTANCES, _MODIFIER_TYPE, _GENDER, _EQUIPMENT_SLOTS, DAMAGE_RESISTANCE_MAP, _DAMAGE_TYPE
from PUBLIC.Public_Classes import DAMAGE
from PUBLIC.Public_Standards import Conversions, Clamp
# Só rodar pela raiz do projeto que essa porra para de chorar por causa de import

class ATTRIBUTE_MODIFIER():
    def __init__(self, 
                 Attribute:_ATTRIBUTE | _TYPE_RESISTANCES, 
                 Operation: _MODIFIER_TYPE, 
                 Value: float, 
                 Source):
        
        self.Attribute: _ATTRIBUTE | _TYPE_RESISTANCES = Attribute
        self.Operation: _MODIFIER_TYPE = Operation
        self.Value: float = Value
        self.Source = Source

class ENTITY:
    def __init__(self,
                 Name: str,
                 Gender: _GENDER,
                 Muscles: int,
                 Bones: int,
                 Haste: int,
                 Brain: int,
                 Memory: int,
                 Faith: int,
                 Skills: list[_SKILL],
                 Passives: list[_PASSIVE],
                 Mutations: list[_MUTATIONS],
                 Attack_Distance: _ATTACK_DISTANCE,
                 Attack_Type: _DAMAGE_TYPE,
                 ):
        
        # BASIC INFORMATION
        self.Name: str = Name
        self.Gender: _GENDER = Gender

        self.ATTRIBUTES = {
            _ATTRIBUTE.MUSCLES: Muscles,
            _ATTRIBUTE.HASTE: Haste,
            _ATTRIBUTE.BONES: Bones,
            _ATTRIBUTE.BRAIN: Brain,
            _ATTRIBUTE.MEMORY: Memory,
            _ATTRIBUTE.FAITH: Faith,
        }
        
        self.Derivative_Calculations = {
            _ATTRIBUTE.MAX_HEALTH: lambda: 200 + (25 * self.Total_Attribute(_ATTRIBUTE.BONES)),
            _ATTRIBUTE.DODGE: lambda: int(1.5 * self.Total_Attribute(_ATTRIBUTE.HASTE)),
            _ATTRIBUTE.MANA_REGEN: lambda: (self.Total_Attribute(_ATTRIBUTE.BRAIN) * 6),
            _ATTRIBUTE.MAX_MANA: lambda: 200 + (25 * self.Total_Attribute(_ATTRIBUTE.MEMORY)),
        }

        
        self.Attribute_Modifiers: list[ATTRIBUTE_MODIFIER] = []
        
        #================================
        #OS PADRÕES FORAM AUMENTADOS, O NOVO PADRÃO É A20
        
        #SKILL SYSTEM
        self.Skills: list[_SKILL] = Skills

        #PASSIVES SYSTEM
        self.Passives: list[_PASSIVE] = Passives
        
        #MUTATION SYSTEM
        self.Mutation: list[_MUTATIONS] = Mutations
        
        #THORNS SYSTEM
        self.Thorns_Type: _DAMAGE_TYPE = _DAMAGE_TYPE.SLASHING
        
        self.Shield = 0
        
        #ALL ATTRIBUTES
        self.All_Attributes_Addend: int = 0
        self.All_Attributes_Multiplier: float = 1

        #ATTACK SYSTEM
        self.Original_Attack_Distance: _ATTACK_DISTANCE = Attack_Distance
        self.Native_Attack_Distance: _ATTACK_DISTANCE = Attack_Distance
        self.Current_Attack_Distance: _ATTACK_DISTANCE = self.Native_Attack_Distance
        
        self.Original_Attack_Type: _ATTACK_DISTANCE = Attack_Type
        self.Native_Attack_Type: _ATTACK_DISTANCE = Attack_Type
        self.Current_Attack_Type: _ATTACK_DISTANCE = self.Native_Attack_Type
        
        # self.Equipment = {
        #     for slot in _EQUIPMENT_SLOTS
        # }
        
        self.Status_effect = []
        self.Stunned: bool = False
        
        self.Basic_Attack_Quantity = 1
        
        #INITIAL ACTUALS
        self.Actual_Health = self.Total_Attribute(_ATTRIBUTE.MAX_HEALTH)
        self.Actual_Mana = 0
        
    def Take_Damage(self, DAMAGE: DAMAGE) -> int:
        Final_Damage = self.Damage_Check(DAMAGE)  
        self.Actual_Health -= Final_Damage
        
        if self.Actual_Health <= 0:
            self.Death()
        return Final_Damage
    
    def Heal(self, Amount) -> int:
        Previous_Health = self.Actual_Health
        
        Before_Clamp_Health = self.Actual_Health + Amount
        After_Clamp_Health = Clamp(Before_Clamp_Health, self.Total_Attribute(_ATTRIBUTE.MAX_HEALTH))
        
        self.Actual_Health = After_Clamp_Health
        
        Difference = self.Actual_Health - Previous_Health
        
        return Difference

    def Damage_Check(self, DAMAGE: DAMAGE):
        if DAMAGE.Type == _DAMAGE_TYPE.TRUE_DAMAGE:
            Total_Damage = DAMAGE.Amount
        else:
            Entity_Resistance = self.Total_Attribute(DAMAGE_RESISTANCE_MAP[DAMAGE.Type])
            Entity_True_Resistance = self.Total_Attribute(_TYPE_RESISTANCES.TRUE_RESISTANCE)
            Base_Damage = DAMAGE.Amount * (1 - Conversions["Resistance_Conversion"](Entity_True_Resistance))
            Total_Damage = Base_Damage * (1 - Conversions["Resistance_Conversion"](Entity_Resistance))
        
        return max(1, int(Total_Damage))
    
    def Death(self):
        pass
    
    def __repr__(self):
        pf = lambda x: int((49 - len(x))/2)
        Bac = f"{self.Actual_Health} / {self.Total_Attribute(_ATTRIBUTE.MAX_HEALTH)}"
        if self is None: return "INEXISTENT"
        else:
            return (
            f"\n"
            f"{ "=" * (pf(self.Name) if (len(self.Name)%2==0) else (pf(self.Name)-1)) } {self.Name} {"="*(pf(self.Name))}\n"
            f"             {self.Gender.name:<11}|       {self.Current_Attack_Distance.name}\n"
            f"{"="*pf("STATUS")} STATUS {"="*pf("STATUS")}\n"
            f"   HP: {Bac:<17}|       MANA: {self.Actual_Mana} / {self.Total_Attribute(_ATTRIBUTE.MAX_MANA)}\n"
            f"{"="*pf("ATTRIBUTES")} ATTRIBUTES {"="*pf("ATTRIBUTES")}\n"
            f"   MUSCLES: {self.Total_Attribute(_ATTRIBUTE.MUSCLES):<11} |"
            f"       MEMORY:  {self.Total_Attribute(_ATTRIBUTE.MEMORY):<4}\n"
            f"   HASTE:   {self.Total_Attribute(_ATTRIBUTE.HASTE):<11} |"
            f"       BRAIN:   {self.Total_Attribute(_ATTRIBUTE.BRAIN):<4}\n"
            f"   BONES:   {self.Total_Attribute(_ATTRIBUTE.BONES):<11} |"
            f"       FAITH:   {self.Total_Attribute(_ATTRIBUTE.FAITH):<4}\n"
            f"{"="*pf("STATS")} STATS {"="*(pf("STATS")-1)}\n"
            f"   MELEE:  + {self.Total_Attribute(_ATTRIBUTE.MELEE_DAMAGE):<11}|       RANGED:  + {self.Total_Attribute(_ATTRIBUTE.RANGED_DAMAGE)}\n"
            f"   DAMAGE: + {str(self.Total_Attribute(_ATTRIBUTE.DAMAGE)) + " %":<11}|       DODGE:    {self.Total_Attribute(_ATTRIBUTE.DODGE)} %\n"
            f"   CRIT:     {str(self.Total_Attribute(_ATTRIBUTE.CRITICAL_CHANCE)) + " %":<11}|       MULTI:   x {float(self.Total_Attribute(_ATTRIBUTE.CRITICAL_MULTIPLIER))}\n"
            f"   VAMPIR:   {str(self.Total_Attribute(_ATTRIBUTE.VAMPIRISM)) + " %":<11}|       THORNS:    {self.Total_Attribute(_ATTRIBUTE.THORNS)}\n"
            f"   MANA/p.T  {self.Total_Attribute(_ATTRIBUTE.MANA_REGEN):<11}|       SHIELD     {self.Total_Attribute(_ATTRIBUTE.NATURAL_SHIELD)} \n"
            f"   COUNTER:  {str(self.Total_Attribute(_ATTRIBUTE.COUNTERATTACK)) + " %":<11}|\n"
            f"{"="*pf("RESISTANCES")} RESISTANCES {"="*(pf("RESISTANCES")-1)}\n"
            f"   SLASH:    {self.Total_Attribute(_TYPE_RESISTANCES.SLASHING_RESISTANCE):<11}|       BLUNT:     {self.Total_Attribute(_TYPE_RESISTANCES.BLUDGEONING_RESISTANCE)}\n"
            f"   FIRE:     {self.Total_Attribute(_TYPE_RESISTANCES.FIRE_RESISTANCE):<11}|       FROST:     {self.Total_Attribute(_TYPE_RESISTANCES.FROST_RESISTANCE)}\n"
            f"   POISON:   {self.Total_Attribute(_TYPE_RESISTANCES.POISONOUS_RESISTANCE):<11}|       ELECTRIC:  {self.Total_Attribute(_TYPE_RESISTANCES.ELECTRIC_RESISTANCE)}\n"
            f"   MALIGN:   {self.Total_Attribute(_TYPE_RESISTANCES.MALIGNANT_RESISTANCE):<11}|       RADIANT:   {self.Total_Attribute(_TYPE_RESISTANCES.RADIANT_RESISTANCE)}\n"
            f"   PSYCHIC:  {self.Total_Attribute(_TYPE_RESISTANCES.PSYCHIC_RESISTANCE):<11}|       TRUE:      {self.Total_Attribute(_TYPE_RESISTANCES.TRUE_RESISTANCE)}\n"
            f"{"="*50}\n"
            )
            
        
    def Total_Attribute(self, 
                        Attribute: 
                            _ATTRIBUTE | _TYPE_RESISTANCES):
        #MODIFIERS
        Attribute_Additive_Modifiers = []
        Attribute_Multiplicative_Modifiers = []
        
        #SEARCH FOR ATTRIBUTES
        for Modifier in self.Attribute_Modifiers:
            if Modifier.Attribute == Attribute:
                match Modifier.Operation:
                    
                    case _MODIFIER_TYPE.ADDITIVE:
                        Attribute_Additive_Modifiers.append(Modifier.Value)
                        
                    case _MODIFIER_TYPE.MULTIPLICATIVE:
                        Attribute_Multiplicative_Modifiers.append(Modifier.Value)
                        
        Total_Additives = sum(Attribute_Additive_Modifiers)
        Total_Multiplicatives = 1 + sum(Attribute_Multiplicative_Modifiers)
        
        if isinstance(Attribute, _ATTRIBUTE):
                if Attribute in self.ATTRIBUTES:
                    Base = (self.ATTRIBUTES[Attribute] + self.All_Attributes_Addend) * self.All_Attributes_Multiplier
                elif Attribute in self.Derivative_Calculations:
                    Base = self.Derivative_Calculations[Attribute]()
                elif Attribute == _ATTRIBUTE.CRITICAL_MULTIPLIER:
                    Base = 2
                else:
                    Base = 0
                    
                if Attribute in [_ATTRIBUTE.CRITICAL_MULTIPLIER, _ATTRIBUTE.CRITICAL_CHANCE]:
                    return (Base + Total_Additives) * Total_Multiplicatives
                else: 
                    return int((Base + Total_Additives) * Total_Multiplicatives)
                
        elif isinstance(Attribute, _TYPE_RESISTANCES):
            return (0 + Total_Additives) * Total_Multiplicatives

                    