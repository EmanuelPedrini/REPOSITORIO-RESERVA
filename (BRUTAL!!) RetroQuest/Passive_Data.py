from Passives import passive

def strgonhit(kimera):
    kimera.gain_atr("bonus_strg", 1)

def intelonhit(kimera):
    kimera.gain_atr("bonus_intel", 1)

def intelonspell(kimera):
    kimera.gain_atr("bonus_intel", 1)

def magicbnsonspell(kimera):
    kimera.gain_atr("magicdmgbonus", 1)


#passivas
incansavel= passive("Tireless", "+1 strength when you take damage", strgonhit, "on_damage")
professionalconjurer=passive("Professional Conjurer", "+1 intel when you use a spell", intelonspell, "on_spell")
gg=passive("Hard Mind", "+1 intel when you take damage", intelonhit, "on_damage")
#on_hit
#on_heal
#on_hit
#on_combat_end


#lista de passivas
todasaspassivas =[incansavel, professionalconjurer, gg]