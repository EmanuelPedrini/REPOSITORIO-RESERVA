import sys
import Globals
from Skill_Data import *
from Passive_Data import *
from THE_HOLE import full_name_with_nickname
# import copy
# import random
# from Bosses_Data import bossesact1

# from Main import listadeeventos
def escolhadealvo(player, enemies):

    alive = [e for e in enemies if e.acthp > 0]

    print("Choose target:")

    for v, r in enumerate(alive):
        print(f"[{v+1}] {r.name} ({r.acthp} / {r.totalmaxhp} HP)")

    while Globals.gamerunning==1:
        ()
        choice = input_player(player, None)
        if not isinstance(choice, str):
            return

        if choice.isdigit():
            index = int(choice) - 1

            if 0 <= index < len(alive):
                return alive[index]

        print("Invalid target.")
        return

def lookyourteeth_command(player, enemy=None):
    from Globals import looktheirteeths
    looktheirteeths(player)
    
def showinventory_command(player=None, enemy=None):
    print("Your inventory:")
    for i, item in enumerate(player.inventory):
        print(f"[ {i+1} ] - {item.name}")
    if player.inventory==[]:
        print("> You don`t have any item in your inventory.")

def exam_enemy_command(player, actenemy):
        for e in actenemy:
            if e.acthp > 0:
                print(f"- {e.name} ( {e.acthp} / {e.totalmaxhp} HP )")
        if actenemy==None:
            print("Any enemy to analise.")


def look_wallet_command(player=None, enemy=None):
    print(f"You actually have {Globals.runcents} cents!")

def Devconsole_FullHealth_Command(player=None, enemy=None):
    player.heal(player.total_max_hp)
    print("You healed to full now, cheater.")

def Devconsole_InstaKillEnemy_Command(player, actenemy):
    if not actenemy:
        print("No enemies to erase")
        return
    target = escolhadealvo(player, actenemy)
    target.toma(999999999999999999999999999999999999, player)
    print(f"{target.name} got ERASED!")

def Devconsole_InstaKillAllEnemies_command(player, actenemy):
    if not actenemy:
        print("No enemies to erase")
        return
    for e in actenemy:
        e.toma(999999999999999999999999999999999999, player)
        print(f"{e.name} got ERASED!")

def Devconsole_Eventchange(player=None, enemy=None):
    pass

def Removeitem_Command(player, enemy=None):
    print(player.equipments)
    itrm = input("Remove from which slot?\nWeapon, Armor or Accessory?")
    if itrm == "Weapon" or itrm == "Armor" or itrm == "Accessory":
        player.itemremove(itrm)
    else:
        print("Invalid Slot")

def Devconsole_AddSkill_Command(player=None, enemy=None):
    skilldevadd = input(f"Please, input the NAME of the skill.")
    for s in todasskills:
        if skilldevadd == s.basename:
            player.skills.append(s) 
            print(f"Added {skilldevadd} to your actual skills!")
            return
    print(f"{skilldevadd} don`t exist in the skill list, incorrect typing or non existent.")

def Devconsole_ShowAllskills_Command(player=None, enemy=None):
    print("Skills:")
    for o in todasskills:
        print("-", o.basename)

def EquipItem_Command(player, enemy=None):

    print("Your inventory:")
    for p, it in enumerate(player.inventory):
        print(f"[ {p+1} ] - {it.name}")
    if player.inventory==[]:
        print("> You don`t have any item in your inventory.")
        return
    itmslc=input("Which item equip? ")
    if itmslc.isdigit():
        posicitem=int(itmslc)-1
        if 0<= posicitem <len(player.inventory):
            itmequip = player.inventory[posicitem]
            player.equip(itmequip)
    else:
        print("Thats isnt a number, dumb ass.")

def removeitemfrominventory_command(player=None, enemy=None):
    #mostra o inventário
    print("Your inventory:")
    for l, iti in enumerate(player.inventory):
        print(f"[ {l+1} ] - {iti.name}")
    if player.inventory==[]:
        print("You don`t have any item in your inventory.")
        return
    #pede qual o item
    itemretirado= input("Please, input the NAME of the item you want to remove.")
    # executa a ação de retirar o item
    for m in player.inventory:
        if itemretirado == m.name:
            player.remove_item(m)
            print(f"{itemretirado} got removed from your inventory.")
            return
    print("This item ins`t in your inventory.")

def EXIT_command(player=None, enemy=None):
    print("Your princess can't accept the shame of RUNNING LIKE A COWARD!")
    print(f"{player.nickname} commits SEPUKKU!!")
    print("Going back to THE HOLE...")
    Globals.gamerunning = 2

def CallBoss_Command(player, enemy=None):
    if Globals.bosscall=="called":
        print("The boss got called already, it`s on your on own now!!")

    else:
        ccc= input("Are you sure? Calling a Boss is a irreversible action! Type [YES] or [NO].\n")
    if ccc=="YES":
        Globals.bosscall = "called"
        print(f"A Boss from the act {Globals.act} is going for you")

    elif ccc=="NO":
        print("Boss call cancelled.")
        Globals.bosscall = "notcalled"

    else:
        print("Give a real answer, Dumb ass.")
        Globals.bosscall = "notcalled"
    
def testeskill(player=None, enemy=None):
    print(Globals.bosscall)

comandosglobais={
    "lookteeths" : lookyourteeth_command,
    "lk": lookyourteeth_command,
    "examenemy": exam_enemy_command,
    "exen": exam_enemy_command,
    "lookwallet": look_wallet_command,
    "lkw": look_wallet_command,
    "showinventory": showinventory_command,
    "devconsolefullhealth": Devconsole_FullHealth_Command,
    "EXIT": EXIT_command,
    "devconsoleaddskill": Devconsole_AddSkill_Command,
    "devconsoleshowskilllist": Devconsole_ShowAllskills_Command,
    "removeitem" : removeitemfrominventory_command,
    "devconsoleeraseenemy" : Devconsole_InstaKillEnemy_Command,
    "devconsoleeraseallenemies": Devconsole_InstaKillAllEnemies_command,
    "uneqitem":Removeitem_Command,
    "equipitem": EquipItem_Command,
    "callboss": CallBoss_Command,
    "test":testeskill
}



# negocio para ler input sempe
def input_player(player, actenemy=None):
    while True:
        if Globals.gamerunning!=1:
            return None
        
        comando = input("")

        if comando in comandosglobais:
            comandosglobais[comando](player, actenemy)
            continue

        return comando
