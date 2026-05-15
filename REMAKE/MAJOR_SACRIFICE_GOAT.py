from CLASSES.ENTITY import ENTITY
from SYSTEMS.Combat_System import COMBAT_DATA, COMBAT_SYSTEM
from PUBLIC.Public_Enums import _GENDER, _ATTACK_DISTANCE, _DAMAGE_TYPE, _ATTRIBUTE
Joana_Mata_Galinha = ENTITY("Joana Mata-Galinha", 
                            _GENDER.FEMALE,
                            5, 7, 2, 3, 1, 2,
                            [], [], [], 
                            _ATTACK_DISTANCE.MELEE,
                            _DAMAGE_TYPE.BLUDGEONING)

Joao_Mata_Galinha = ENTITY("João Mata-Galinha", 
                            _GENDER.FEMALE,
                            3, 3, 3, 1, 1, 2, 
                            [], [], [], 
                            _ATTACK_DISTANCE.RANGED,
                            _DAMAGE_TYPE.BLUDGEONING)

Maria = ENTITY("Mariazinha Mata-Galinha", 
                            _GENDER.FEMALE,
                            2, 2, 2, 2, 2, 2,
                            [], [], [], 
                            _ATTACK_DISTANCE.RANGED,
                            _DAMAGE_TYPE.BLUDGEONING)

def PrH(W):
    print(f"{W.Name} / HP : {W.Actual_Health} / {W.Total_Attribute(_ATTRIBUTE.MAX_HEALTH)}")

#COMBAT_SYSTEM.Combat_Between([Maria, Joao_Mata_Galinha],[Joana_Mata_Galinha])

print(                f"\n"
                f"╔══════════════════ {Maria.Name} ════════════════╗\n"
                f"  {Maria.Gender.name} | {Maria.Current_Attack_Distance.name} | {Maria.Current_Attack_Type.name}\n"
                f"╠═══════════════════ STATUS ════════════════════╣\n"
                f"  HP   {Maria.Actual_Health} / {Maria.Total_Attribute(_ATTRIBUTE.MAX_HEALTH)}"
                f"    |    Mana {Maria.Actual_Mana} / {Maria.Total_Attribute(_ATTRIBUTE.MAX_MANA)}\n"
                f"╠═════════════════ ATTRIBUTES ══════════════════╣\n"
                f" MUSCLES: {Maria.Total_Attribute(_ATTRIBUTE.MUSCLES):<3}\n"
                f" BONES:   {Maria.Total_Attribute(_ATTRIBUTE.BONES):<3}\n"
                f" HASTE:   {Maria.Total_Attribute(_ATTRIBUTE.HASTE):<3}\n"
                f" BRAIN:   {Maria.Total_Attribute(_ATTRIBUTE.BRAIN):<3}\n"
                f" MEMORY:  {Maria.Total_Attribute(_ATTRIBUTE.MEMORY):<3}\n"
                f" FAITH:   {Maria.Total_Attribute(_ATTRIBUTE.FAITH):<3}\n"
                f"╠═════════════════ COMBAT DATA ═════════════════╣\n"
                f"  Melee + {Maria.Total_Attribute(_ATTRIBUTE.MELEE_DAMAGE):<4}"
                f"  Ranged + {Maria.Total_Attribute(_ATTRIBUTE.RANGED_DAMAGE):<4}"
                f" Damage + {Maria.Total_Attribute(_ATTRIBUTE.DAMAGE)} %\n"
                f"  Dodge {Maria.Total_Attribute(_ATTRIBUTE.DODGE):} %"
                f"     Crit {Maria.Total_Attribute(_ATTRIBUTE.CRITICAL_CHANCE)}"
                f" ×{Maria.Total_Attribute(_ATTRIBUTE.CRITICAL_MULTIPLIER)}"
                f"    Regen {Maria.Total_Attribute(_ATTRIBUTE.MANA_REGEN)}\n"
                f"  Vamp {Maria.Total_Attribute(_ATTRIBUTE.VAMPIRISM):<4}"
                f"     Thorns {Maria.Total_Attribute(_ATTRIBUTE.THORNS):<4}"
                f"Shield {Maria.Total_Attribute(_ATTRIBUTE.NATURAL_SHIELD):<4}\n"
                f"╚═══════════════════════════════════════════════╝"
                )