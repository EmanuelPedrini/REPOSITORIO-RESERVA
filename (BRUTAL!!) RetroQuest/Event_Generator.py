from Events_Data import badevents, neutralevents, goodevents
import random
import copy
import Globals
from Commands import input_player
from Bosses_Data import bossesact1
from Itens_Data import todososequipamentos
from FinalBoss import finalbosses
# from ColorText import *
# from Commands import 

def shop(player):
        print(f"In distance, you can see a small hut and you decide to investigate.")
        print(f"Entering on the the small hut, you discover it is a shop, a buff woman in a armor is leaning on the counter")
        print(f"(Agnes) - Hey BRO! what`s up? want to buy something from my shop?")
        shop_total_options = todososequipamentos
        shopactoptions = random.sample(shop_total_options, min(5, len(shop_total_options)))

        while Globals.gamerunning==1:
            #()
            for cont, itemI in enumerate(shopactoptions):
                print(f"{cont+1} - {itemI.name}")

            buyintend= input("")
            
            if buyintend.isdigit():
                realbuyintend = int(buyintend)-1
                if 0<= realbuyintend <len(shopactoptions):
                    buyed = shopactoptions[realbuyintend]
                    player.add_item(buyed)
                    break
                else:
                    print("BRO! STOP POINTING TO THE WALL!")
            else:
                print(f"Lil sis, stop asking for {str(buyintend)}, you ask that every time!")


def gerador_de_eventos(player):

    #número random que define o evento q vai retornar
    escolhadeevento= int((1 + (player.total_luck / (player.total_luck + 15))) * (random.randint(1, 100)))

    if Globals.bosscall!="notcalled":
        Globals.bosscall = "notcalled"
        if Globals.act ==1:
            boss = copy.deepcopy(random.choice(bossesact1))
            floorboss=[ boss ]

        elif Globals.act ==2:
            boss = copy.deepcopy(random.choice(finalbosses))
            floorboss = [ boss ]

        print(f"{boss.name} is going for YOU!\n HA!\n HAHA!\n HAHAHA!\n")
        return(67, floorboss)


    elif escolhadeevento <= 25:
        return (1, random.choice(badevents))
    
    #Combate aleatório
    elif escolhadeevento > 25 and escolhadeevento <= 50:

        quantidadeinimigos = random.randint(1, 3)
        actenemy = [
            copy.deepcopy(e) 
            for e in random.sample(Globals.actualpool, k=min(quantidadeinimigos, len(Globals.actualpool)))
            ]
        return (2, actenemy)
    
    elif 50 < escolhadeevento <=60:
        return (123, shop)
    
    elif escolhadeevento > 60 and escolhadeevento < 85:
        return (3, random.choice(neutralevents))
    
    else:
        return (4, random.choice(goodevents))