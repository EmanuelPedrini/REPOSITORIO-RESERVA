from Skills import skill
# def playermanaflow(sm):
#     numb2 = sm.actmana
#     return numb2


#skills
fireball=skill("Fireball", "You cast a giant fireball to destroy your enemies!", 14, 0, 0, 9, target="allenemies", skproperty="")
healing= skill("Healing", "You heal your wounds", 0, 5, 0, 4, target="self", skproperty="any")
satorogojonaooooo= skill("Deep Purple", "GOJO NOOOO", 18, 0, 0, 12, target="enemy", skproperty="any")
manaflow=skill("Mana Flow", f"you use all your actual mana (0) and heal a equivalent amount.", 0, 0, 0, target="self", skproperty="ManaFlow")
lightning=skill("Lightning", "You cast multiple lightnings in a area", 8, 0, 0, 5, target="allenemies", skproperty="any")
magicspark=skill("Magic Spark", "A simple spell that every mage needs to know!", 4, 0, 0, 3, target="enemy",skproperty="any")
donothing=skill("Do nothing!", "You do nothing.", 0, 0, 0, 2, target="self", skproperty="any")
block =skill("Block", "You receive shield", 0, 0, 3, 2, target="self", skproperty="any")
bite=skill("Toe Bite", "You bite your enemy with the strength of a lion!", 3, 0, 0, 2, target="enemy", skproperty="HealOnHit")
bloodfeast=skill("Blood Feast", "You drink the blood of your enemies!", 6, 0, 0, 7, target="allenemies",skproperty="MassHealOnDmg")
teleport=skill("Teleport","You teleport above a enemy and cause damage.", 9, 0, 0, 5, target="enemy", skproperty="any")
arranhar=skill("Scratch", "Scratch the skin of your enemies!",4, 0, 0, 2, target="enemy", skproperty="any")
Manaboy=skill("Mana Cannibal", "Cause a massive damage to all enemies based on half of your actual mana", 0, 0, 0, 0, target="allenemies", skproperty="DamageBasedOnMana")

#lista de todas as skills
todasskills = [fireball,healing,satorogojonaooooo, lightning, magicspark, donothing, bite, bloodfeast, teleport, arranhar, manaflow, Manaboy]