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
            _ATTRIBUTE.DODGE: lambda: 4 * self.Total_Attribute(_ATTRIBUTE.HASTE),
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
        if self is None: return "INEXISTENT"
        else:
            return (
                f"\n"
                f"╔══════════════════ {self.Name} ════════════════╗\n"
                f"  {self.Gender.name} | {self.Current_Attack_Distance.name} | {self.Current_Attack_Type.name}\n"
                f"╠═══════════════════ STATUS ════════════════════╣\n"
                f"  HP   {self.Actual_Health} / {self.Total_Attribute(_ATTRIBUTE.MAX_HEALTH)}"
                f"    |    Mana {self.Actual_Mana} / {self.Total_Attribute(_ATTRIBUTE.MAX_MANA)}\n"
                f"╠═════════════════ ATTRIBUTES ══════════════════╣\n"
                f" MUSCLES: {self.Total_Attribute(_ATTRIBUTE.MUSCLES):<3}\n"
                f" BONES:   {self.Total_Attribute(_ATTRIBUTE.BONES):<3}\n"
                f" HASTE:   {self.Total_Attribute(_ATTRIBUTE.HASTE):<3}\n"
                f" BRAIN:   {self.Total_Attribute(_ATTRIBUTE.BRAIN):<3}\n"
                f" MEMORY:  {self.Total_Attribute(_ATTRIBUTE.MEMORY):<3}\n"
                f"╠═════════════════ COMBAT DATA ═════════════════╣\n"
                f"  Melee + {self.Total_Attribute(_ATTRIBUTE.MELEE_DAMAGE):<4}"
                f"  Ranged + {self.Total_Attribute(_ATTRIBUTE.RANGED_DAMAGE):<4}"
                f" Damage + {self.Total_Attribute(_ATTRIBUTE.DAMAGE)} %\n"
                f"  Dodge {self.Total_Attribute(_ATTRIBUTE.DODGE):} %"
                f"     Crit {self.Total_Attribute(_ATTRIBUTE.CRITICAL_CHANCE)}"
                f" ×{self.Total_Attribute(_ATTRIBUTE.CRITICAL_MULTIPLIER)}"
                f"    Regen {self.Total_Attribute(_ATTRIBUTE.MANA_REGEN)}\n"
                f"  Vamp {self.Total_Attribute(_ATTRIBUTE.VAMPIRISM):<4}"
                f"     Thorns {self.Total_Attribute(_ATTRIBUTE.THORNS):<4}"
                f"Shield {self.Total_Attribute(_ATTRIBUTE.NATURAL_SHIELD):<4}\n"
                f"╚═══════════════════════════════════════════════╝"
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
                    Base = 100
                    
                if Attribute in [_ATTRIBUTE.CRITICAL_MULTIPLIER, _ATTRIBUTE.CRITICAL_CHANCE]:
                    return (Base + Total_Additives) * Total_Multiplicatives
                else: 
                    return int((Base + Total_Additives) * Total_Multiplicatives)
                
        elif isinstance(Attribute, _TYPE_RESISTANCES):
            return (0 + Total_Additives) * Total_Multiplicatives

                    