from Passives import passive

def strgonhit(kimera):
    kimera.gain_atr("bonus_strg", 1)

def intelonhit(kimera):
    kimera.gain_atr("bonus_intel", 1)

def intelonspell(kimera):
    kimera.gain_atr("bonus_intel", 1)

# def magicbnsonspell(kimera):
#     kimera.gain_atr("temporary_magicdmgbonus", 1)

# def n(kimera):
#     kimera.gain_atr("", 1)


#passivas
incansavel= passive("Tireless", "+1 strength when you take damage", strgonhit, "on_damage")
professionalconjurer=passive("Professional Conjurer", "+1 intel when you use a spell", intelonspell, "on_spell")
HardMind= passive("Hard Mind", "+1 intel when you take damage", intelonhit, "on_damage")
# Protagonista = passive("Protagonist","Gain +30% more XP",)
# Ace = passive("Ace", "+25% - Crit Chance",)
# Killer = passive("Killer","Gain +25% Crit Chance when killing a enemy")
# Strong = passive("", "")
# Collector = passive("", "")



#on_hit
#on_heal
#on_hit
#on_combat_end


#lista de passivas
todasaspassivas =[incansavel, professionalconjurer, HardMind]