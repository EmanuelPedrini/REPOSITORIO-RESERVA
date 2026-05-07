from Skills import skill
# def playermanaflow(sm):
#     numb2 = sm.actmana
#     return numb2


#skills
fireball=skill("Fireball", "You cast a giant fireball to destroy your enemies!", 14, 0, 0, 9, target="allenemies", skproperty="")
healing= skill("Healing", "You heal your wounds", 0, 5, 0, 4, target="self", skproperty="any")
satorogojonaooooo= skill("Deep Purple", "Cause MASSIVE damage to a single target at a high mana cost.", 24, 0, 0, 14, target="enemy", skproperty="any")
manaflow=skill("Mana Flow", "you use all your actual mana and heal a equivalent amount.", 0, 0, 0, target="self", skproperty="ManaFlow")
lightning=skill("Lightning", "You cast multiple lightnings in a area", 8, 0, 0, 5, target="allenemies", skproperty="any")
magicspark=skill("Magic Spark", "A simple spell that every mage needs to know!", 4, 0, 0, 3, target="enemy",skproperty="any")
donothing=skill("Do nothing!", "You do nothing.", 0, 0, 0, 2, target="self", skproperty="any")
block =skill("Block", "You receive shield", 0, 0, 3, 2, target="self", skproperty="any")
bite=skill("Toe Bite", "You bite your enemy with the strength of a lion!", 3, 0, 0, 2, target="enemy", skproperty="HealOnHit")
bloodfeast=skill("Blood Feast", "You drink the blood of your enemies!", 6, 0, 0, 7, target="allenemies",skproperty="MassHealOnDmg")
teleport=skill("Teleport","You teleport above a enemy and cause damage.", 9, 0, 0, 5, target="enemy", skproperty="any")
arranhar=skill("Scratch", "Scratch the skin of your enemies!",4, 0, 0, 2, target="enemy", skproperty="any")
Manaboy=skill("Mana Cannibal", "Cause a massive damage to all enemies based on half of your actual mana", 0, 0, 0, 0, target="allenemies", skproperty="DamageBasedOnMana")
iceblast = skill("Ice Blast", "A freezing attack that may slow the enemy.", 7, 0, 0, 5, target="enemy", skproperty="slow")
poisoncloud = skill("Poison Cloud", "Release a toxic cloud damaging all enemies over time.", 5, 0, 0, 6, target="allenemies", skproperty="poison")
lifedrain = skill("Life Drain", "Steal life from your enemy.", 6, 0, 0, 5, target="enemy", skproperty="HealOnHit")
earthshield = skill("Earth Shield", "Raise a protective barrier of earth.", 0, 0, 5, 4, target="self", skproperty="buff_defense")
berserk = skill("Berserk", "Increase damage but reduce defense.", 9, 0, -2, 4, target="self", skproperty="buff_attack")
frostnova = skill("Frost Nova", "Freeze all enemies around you.", 6, 0, 0, 7, target="allenemies", skproperty="freeze")
shadowstrike = skill("Shadow Strike", "A fast attack with high critical chance.", 8, 0, 0, 4, target="enemy", skproperty="crit")
manashield = skill("Mana Shield", "Convert mana into protective shield.", 0, 0, 4, 3, target="self", skproperty="mana_shield")
explosion = skill("Explosion", "A powerful explosion that damages everyone including yourself.", 13, 0, 0, 8, target="allenemies", skproperty="selfdamage")
holy_light = skill("Holy Light", "A powerful healing spell.", 0, 12, 0, 8, target="self", skproperty="any")
curse = skill("Curse", "Weaken the enemy reducing their attack power.", 4, 0, 0, 5, target="enemy", skproperty="debuff_attack")
windslash = skill("Wind Slash", "Fast wind attack that hits all enemies.", 6, 0, 0, 4, target="allenemies", skproperty="any")
#lista de todas as skills
todasskills = [holy_light,curse,windslash,fireball,iceblast,poisoncloud,lifedrain,earthshield,berserk,frostnova,shadowstrike,manashield,explosion,healing,satorogojonaooooo, lightning, magicspark, donothing, bite, bloodfeast, teleport, arranhar, manaflow, Manaboy]