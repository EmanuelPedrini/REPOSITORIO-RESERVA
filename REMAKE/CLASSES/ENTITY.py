from CLASSES.SKILLS import _SKILL
from CLASSES.PASSIVES import _PASSIVE
from CLASSES.MUTATIONS import _MUTATIONS
from CLASSES.ITEM import _ITEM
from CLASSES.BASIC_ATTACK import _BASIC_ATTACK
from PUBLIC.Public_Enums import _ATTRIBUTE, _ATTACK_DISTANCE, _TYPE_RESISTANCES, _MODIFIER_TYPE, _GENDER, _SIDE, _EQUIPMENT_SLOTS, DAMAGE_RESISTANCE_MAP, _DAMAGE_TYPE
from PUBLIC.Public_Classes import DAMAGE
from PUBLIC.Public_Standards import Conversions, Clamp
# Só rodar pela raiz do projeto que essa porra para de chorar por causa de import

class ATTRIBUTE_MODIFIER():
    def __init__(self, 
                 Attribute:_ATTRIBUTE | _TYPE_RESISTANCES, 
                 Operation: _MODIFIER_TYPE, 
                 Value: float, 
                 Source,
                 Duration):
        
        self.Attribute: _ATTRIBUTE | _TYPE_RESISTANCES = Attribute
        self.Operation: _MODIFIER_TYPE = Operation
        self.Value: float = Value
        self.Source = Source
        self.Duration = Duration

class INJURIE:
    def __init__(self, 
                 Attribute:_ATTRIBUTE | _TYPE_RESISTANCES, 
                 Operation: _MODIFIER_TYPE, 
                 Value: float
                 ):
        
        self.Attribute: _ATTRIBUTE | _TYPE_RESISTANCES = Attribute
        self.Operation: _MODIFIER_TYPE = Operation
        self.Value: float = Value
        
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
                 Basic_Attack: _BASIC_ATTACK,
                 Side: _SIDE = _SIDE.ENEMY
                 ):
        
        # BASIC INFORMATION
        self.Name: str = Name
        self.Gender: _GENDER = Gender
        self.Side: _SIDE = Side

        self.ATTRIBUTES = {
            _ATTRIBUTE.MUSCLES: Muscles,
            _ATTRIBUTE.HASTE: Haste,
            _ATTRIBUTE.BONES: Bones,
            _ATTRIBUTE.BRAIN: Brain,
            _ATTRIBUTE.MEMORY: Memory,
            _ATTRIBUTE.FAITH: Faith,
        }
        
        self.Derivative_Calculations = {
            _ATTRIBUTE.MAX_HEALTH: lambda: 100 + ((12 * self.Total_Attribute(_ATTRIBUTE.BONES) * self.Level)),
            _ATTRIBUTE.DODGE: lambda: int(1.5 * self.Total_Attribute(_ATTRIBUTE.HASTE)),
            _ATTRIBUTE.MANA_REGEN: lambda: 4 * (self.Total_Attribute(_ATTRIBUTE.BRAIN)),
            _ATTRIBUTE.MAX_MANA: lambda: 50 + ((6 * self.Total_Attribute(_ATTRIBUTE.MEMORY) * self.Level)),
        }

        
        self.Attribute_Modifiers: list[ATTRIBUTE_MODIFIER] = []
        
        #================================
        #OS PADRÕES FORAM AUMENTADOS, O NOVO PADRÃO É A20
        
        #SKILL SYSTEM
        self.Skills: list[_SKILL] = Skills

        #PASSIVES SYSTEM
        self.Passives: list[_PASSIVE] = Passives
        
        #MUTATION SYSTEM
        self.Mutations: list[_MUTATIONS] = Mutations
        
        #THORNS SYSTEM
        self.Thorns_Type: _DAMAGE_TYPE = _DAMAGE_TYPE.SLASHING
        
        self.Shield = 0
        self.Alive = True
        
        #ALL ATTRIBUTES
        self.All_Attributes_Addend: int = 0
        self.All_Attributes_Multiplier: float = 1
        
        #MUDANDO O SISTEMA DE ATAQUE BÁSICO
        self.Original_Attack: _BASIC_ATTACK = Basic_Attack
        self.Current_Attack: _BASIC_ATTACK = Basic_Attack 
        
        self.EQUIPMENTS = {
            _EQUIPMENT_SLOTS.HEAD: None,
            _EQUIPMENT_SLOTS.BODY: None,
            _EQUIPMENT_SLOTS.BOOTS: None,
            _EQUIPMENT_SLOTS.ACCESSORY: None,
            _EQUIPMENT_SLOTS.HAND: None,
        }
        
        self.Status_effect = []
        self.Injuries = []
        self.Stunned: bool = False
        
        self.Level = 1
        
        #INITIAL ACTUALS
        self.Actual_Health = self.Total_Attribute(_ATTRIBUTE.MAX_HEALTH)
        self.Actual_Mana = 0
        
        #PARÂMETROS TALVEZ TEMPORÁRIOS
        self.Can_Regenerate_Health: bool = True
        self.Can_Regenerate_Mana: bool =  True
        
        
    def Take_Damage(self, DAMAGE: DAMAGE) -> int:
        Final_Damage = self.Damage_Check(DAMAGE)
        if DAMAGE.Fatal:
            self.Actual_Health -= Final_Damage
        else:
            self.Actual_Health = max(1, self.Actual_Health - Final_Damage)
        
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
        self.Alive = False
    
    def __repr__(self):
        Bar_Half_Size = lambda x: int((49 - len(x))/2)
        Health_Bar = f"{self.Actual_Health} / {self.Total_Attribute(_ATTRIBUTE.MAX_HEALTH)} ( {(self.Actual_Health / self.Total_Attribute(_ATTRIBUTE.MAX_HEALTH))*100} % )"
        if self is None: return "INEXISTENT"
        else:
            return (
            f"\n"
            f"{ "=" * (Bar_Half_Size(self.Name) if (len(self.Name)%2==0) else (Bar_Half_Size(self.Name)-1)) } {self.Name} {"="*(Bar_Half_Size(self.Name))}\n"
            f"   {self.Gender.name:<21}|       {self.Current_Attack}\n"
            f"{"="*Bar_Half_Size("STATUS")} STATUS {"="*Bar_Half_Size("STATUS")}\n"
            f"   HP: {Health_Bar:<17}\n   MANA: {self.Actual_Mana} / {self.Total_Attribute(_ATTRIBUTE.MAX_MANA)} ( {(self.Actual_Mana / self.Total_Attribute(_ATTRIBUTE.MAX_MANA)) * 100} % )\n"
            f"{"="*Bar_Half_Size("ATTRIBUTES")} ATTRIBUTES {"="*Bar_Half_Size("ATTRIBUTES")}\n"
            f"   MUSCLES: {self.Total_Attribute(_ATTRIBUTE.MUSCLES):<11} |"
            f"       MEMORY:  {self.Total_Attribute(_ATTRIBUTE.MEMORY):<4}\n"
            f"   HASTE:   {self.Total_Attribute(_ATTRIBUTE.HASTE):<11} |"
            f"       BRAIN:   {self.Total_Attribute(_ATTRIBUTE.BRAIN):<4}\n"
            f"   BONES:   {self.Total_Attribute(_ATTRIBUTE.BONES):<11} |"
            f"       FAITH:   {self.Total_Attribute(_ATTRIBUTE.FAITH):<4}\n"
            f"{"="*Bar_Half_Size("STATS")} STATS {"="*(Bar_Half_Size("STATS")-1)}\n"
            f"   MELEE:  + {self.Total_Attribute(_ATTRIBUTE.MELEE_DAMAGE):<11}|       RANGED:  + {self.Total_Attribute(_ATTRIBUTE.RANGED_DAMAGE)}\n"
            f"   DAMAGE: + {str(self.Total_Attribute(_ATTRIBUTE.DAMAGE)) + " %":<11}|       DODGE:    {self.Total_Attribute(_ATTRIBUTE.DODGE)} %\n"
            f"   CRIT:     {str(self.Total_Attribute(_ATTRIBUTE.CRITICAL_CHANCE)) + " %":<11}|       MULTI:   x {float(self.Total_Attribute(_ATTRIBUTE.CRITICAL_MULTIPLIER))}\n"
            f"   VAMPIR:   {str(self.Total_Attribute(_ATTRIBUTE.VAMPIRISM)) + " %":<11}|       THORNS:    {self.Total_Attribute(_ATTRIBUTE.THORNS)}\n"
            f"   MANA/p.T  {self.Total_Attribute(_ATTRIBUTE.MANA_REGEN):<11}|       SHIELD     {self.Total_Attribute(_ATTRIBUTE.NATURAL_SHIELD)} \n"
            f"   COUNTER:  {str(self.Total_Attribute(_ATTRIBUTE.COUNTERATTACK)) + " %":<11}|\n"
            
            # f"{"="*Bar_Half_Size("SKILLS AND PASSIVES")} SKILLS AND PASSIVES {"="*(Bar_Half_Size("SKILLS AND PASSIVES")-1)}\n"
            # f"   SLASH:    {self.Total_Attribute(_TYPE_RESISTANCES.SLASHING_RESISTANCE):<11}|       BLUNT:     {self.Total_Attribute(_TYPE_RESISTANCES.BLUDGEONING_RESISTANCE)}\n"
            # f"   FIRE:     {self.Total_Attribute(_TYPE_RESISTANCES.FIRE_RESISTANCE):<11}|       FROST:     {self.Total_Attribute(_TYPE_RESISTANCES.FROST_RESISTANCE)}\n"
            # f"   POISON:   {self.Total_Attribute(_TYPE_RESISTANCES.POISONOUS_RESISTANCE):<11}|       ELECTRIC:  {self.Total_Attribute(_TYPE_RESISTANCES.ELECTRIC_RESISTANCE)}\n"
            # f"   MALIGN:   {self.Total_Attribute(_TYPE_RESISTANCES.MALIGNANT_RESISTANCE):<11}|       RADIANT:   {self.Total_Attribute(_TYPE_RESISTANCES.RADIANT_RESISTANCE)}\n"
            # f"   PSYCHIC:  {self.Total_Attribute(_TYPE_RESISTANCES.PSYCHIC_RESISTANCE):<11}|       TRUE:      {self.Total_Attribute(_TYPE_RESISTANCES.TRUE_RESISTANCE)}\n"
            
            f"{"="*Bar_Half_Size("RESISTANCES")} RESISTANCES {"="*(Bar_Half_Size("RESISTANCES")-1)}\n"
            f"   SLASH:    {self.Total_Attribute(_TYPE_RESISTANCES.SLASHING_RESISTANCE):<11}|       BLUNT:     {self.Total_Attribute(_TYPE_RESISTANCES.BLUDGEONING_RESISTANCE)}\n"
            f"   FIRE:     {self.Total_Attribute(_TYPE_RESISTANCES.FIRE_RESISTANCE):<11}|       FROST:     {self.Total_Attribute(_TYPE_RESISTANCES.FROST_RESISTANCE)}\n"
            f"   POISON:   {self.Total_Attribute(_TYPE_RESISTANCES.POISONOUS_RESISTANCE):<11}|       ELECTRIC:  {self.Total_Attribute(_TYPE_RESISTANCES.ELECTRIC_RESISTANCE)}\n"
            f"   MALIGN:   {self.Total_Attribute(_TYPE_RESISTANCES.MALIGNANT_RESISTANCE):<11}|       RADIANT:   {self.Total_Attribute(_TYPE_RESISTANCES.RADIANT_RESISTANCE)}\n"
            f"   PSYCHIC:  {self.Total_Attribute(_TYPE_RESISTANCES.PSYCHIC_RESISTANCE):<11}|       TRUE:      {self.Total_Attribute(_TYPE_RESISTANCES.TRUE_RESISTANCE)}\n"
            f"{"="*50}\n"
            )
            
    def Equip_Item(self, 
                   Item: _ITEM):
        pass
    
    def Unequip_Item(self, 
                     Item: _ITEM):
        pass
    
    def Remove_Item(self, 
                    Item: _ITEM):
        self.EQUIPMENTS[Item.Slot] = None
        
    
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

#TESTE
                    