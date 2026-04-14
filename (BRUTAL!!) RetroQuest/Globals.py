
globaldanger = 0
globaldangercalc = (1 + 0.03 * globaldanger ** 1.8)
gamerunning = 0
bosscall = "notcalled"

runcents = 0
cursemultiplier = 2

breeding = False
endofarun = False
act = 1
day = 1
gained_cents_battle = 0
gained_xp_battle = 0
gained_itens_battle = []
gained_kimeras_battle = []


# currentplayer = None


actualpool = list
from Enemies_Data import enemiespool, enemiespoolact2

if act == 1:
        actualpool = enemiespool
elif act == 2:
        actualpool = enemiespoolact2

from Kimeras_Data import allkimeras, allthekimerasforbreed, princesses

def reds(who):
    HC = 15
    reduction = who.armor / (who.armor + HC) 
    rdss = min(reduction, 0.90)
    return rdss

def clear():
    print("\033c", end="")

def looktheirteeths(analized):
    save = (analized.total_max_hp)
    print(f"\n=== {analized.nickname} STATS ===")
    print(f"Level: [ {analized.level} ]\nExperience Points:\n [ {analized.xp} / {analized.xptonext} ]")
    print(f"Health Points   : [ {analized.acthp} / {save} ] + ( {analized.shield} ) SHIELD")
    print(f"Mana Points : [ {analized.actmana} / {analized.max_mana} ]")
    print(f"Attributes:")
    print(f"STR : {analized.total_strg} ( {analized.base_strg} )")
    print(f"DEX : {analized.total_dex} ( {analized.base_dex} )")
    print(f"VIT : {analized.total_vit} ( {analized.base_vit} )")
    print(f"INT : {analized.total_intel} ( {analized.base_intel} )")
    print(f"CHA : {analized.total_cha} ( {analized.base_cha} )")
    print(f"LUCK: {analized.total_luck} ( {analized.base_luck} )")
    print(f"ARMOR: {analized.armor} [ {reds(analized)}% ]")
    print(f"THORNS: {analized.thorns}")
    print(f"DODGE: {analized.total_dodge} %")
    print(f"VAMPIRISM: {analized.vampirism} %")
    if analized.mainhand=="Left Hand":
         print(f"{analized.name} likes more {analized.possessive} LEFT HAND.")
    else:
         print(f"{analized.name} likes more {analized.possessive} RIGHT HAND.")

    print("SKILLS:")
    if analized.skills==[]:
        print("Any skills.")
    for l, b in enumerate(analized.skills):
            print(f"{l+1} - {b.basename}")

    print("PASSIVES:")
    if analized.passives==[]:
        print("Any passives.")
    for f, d in enumerate(analized.passives):
            print(f"{f+1} - {d.basename}")

def banned_from_twitter(banned):
    for lista in (allkimeras, allthekimerasforbreed, princesses):
        if banned in lista:
            lista.remove(banned) 