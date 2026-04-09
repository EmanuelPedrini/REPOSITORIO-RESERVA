import Globals
# from ColorText import *
import random
from Furniture import furniture
from Furniture_Data import allthefurnitures

#THE HOLE
#FURNITURE
space = 100
ocuppiedspace = 0
furnitureonthecolony = []
yourfurnitures = []

#STATS
bones = 0
bonepiles = 0
pipes = 0
waterquality = 0
pipeshine = 0
foodquality = 0

def lose_money(moneyused):
    global bones
    bones -= moneyused

def gain_money(moneyused):
    global bones 
    bones += moneyused

def move(movedfurniture):
     furnitureonthecolony.append(movedfurniture)

def remove(removedfurnitute):
     furnitureonthecolony.remove(removedfurnitute)

def gainfurn(furn):
     yourfurnitures.append(furn)

def removefurn(rmvfurn):
     yourfurnitures.remove(rmvfurn)



# def HOLE_shop():
#         print(f"In distance, you can see a small hut and you decide to investigate.")
#         print(f"Entering on the the small hut, you discover it is a shop, a buff woman in a armor is leaning on the counter")
#         print(f"(Agnes) - Hey BRO! what`s up? want to buy something from my shop?")
#         shoptop =
#         shopactopt = random.sample(shoptop, min(5, len(shoptop)))

#         while Globals.gamerunning==1:
#             for cont, itemI in enumerate(shopactoptions):
#                 print(f"{cont+1} - {itemI.name}")

#             buyintend= input_player(player, None)
            
#             if buyintend.isdigit():
#                 realbuyintend = int(buyintend)-1
#                 if 0<= realbuyintend <len(shopactoptions):
#                     buyed = shopactoptions[realbuyintend]
#                     player.add_item(buyed)
#                     break
#                 else:
#                     print("BRO! STOP POINTING TO THE WALL!")
#             else:
#                 print(f"Lil sis, stop asking for {str(buyintend)}, you ask that every time!")
     
#      pass

# def rdiniti():
#     from Kimera import kimera
#     from Kimeras_Data import allkimeras
#     for k in range(5):
#         rd = kimera.randomkimera("Queen")
#         rd.age += 3
#         allkimeras.append(rd)

def show_list(listaesc):
    for numb, kimera  in enumerate(listaesc):   
                print((f"[{numb+1}] - {kimera.name} ( {kimera.status} )"))

def big_ass_print(choice, listap):
            while True:
                ()
                if choice.isdigit():
                        index = int(choice) - 1
                        if 0<= index <len(listap):
                            escolha = listap[index]
                            return escolha
                        else:
                            print("Out of the actual options")
                            break
                else:
                    print("Type the number of your choice")
                    break            

def lookingsmaching(theone):
    sumallstats = int(theone.base_strg + theone.base_dex + theone.base_vit +theone.base_intel + theone.base_cha + theone.base_luck)

    skpt = len(theone.skills)

    pspt = len(theone.passives)

    mtpt = len(theone.mutations)

    ptprtt = ((skpt * 11) + (pspt * 20) + (mtpt * 5))

    hdpt = (ptprtt / (ptprtt + 12))

    points = int((sumallstats * 100) * (1 + hdpt)) 

    return points
        
def look_teeths_again_Command():
    from Globals import looktheirteeths
    from Kimeras_Data import allkimeras
    print("Choose a Kimera to analize!")
    show_list(allkimeras)
    cxp = input("")
    alisada = big_ass_print(cxp, allkimeras)
    if alisada == None:
         return
    looktheirteeths(alisada)

def look_best_Command():
    # from Globals import looktheirteeths
    from Kimeras_Data import allkimeras
    print("Choose a Kimera to analize!")
    show_list(allkimeras)
    chcc = input("")
    alisada = big_ass_print(chcc, allkimeras)
    if alisada == None:
        return
    analise_da_alisada = lookingsmaching(alisada)
    print(f"Using a points scale {full_name_with_nickname(alisada)} received the score of {analise_da_alisada}.")

def Points_list():
     from Kimeras_Data import allkimeras
     for n, k in enumerate(allkimeras):
          print(f"[{n+1}] - {full_name_with_nickname(k)} / ( SCORE: {lookingsmaching(k)} )")

def lookcents_Command():
     global bones
     print(f"You actually have {bones} BONES")

    

def THE_HOLE():
    # rdiniti()
    from Kimeras_Data import allkimeras, actualize_breed, actualize_princesses, actualize_queen
    actualize_breed(allkimeras)
    actualize_princesses(allkimeras)
    actualize_queen(allkimeras)

    global bones

    print("Type your action!")
    print(f"ACTUAL BONES : {bones}")
    print("Type [ start ] to start a NEW RUN with a princess!")
    print("Type [ breed ] to start breeding 2 KIMERAS!")
    print("Type [ lookpoints ] to see the score of one KIMERA!")
    print("Type [ lookallpoints ] to see a list with all the KIMERAS and their scores!")
    print("Type [ shop ] to buy itens for your colony!")
    print("Type [ sleep ] to end the day!")

    input_player_in_the_hole()
        
def full_name_with_nickname(chose):
    full_name_nickname = f"{chose.name} {chose.nickname} {chose.surname}"
    return full_name_nickname

def end_day():
    
    from Kimeras_Data import allkimeras, actualize_breed, actualize_princesses, actualize_queen
    from Kimera import kimera

    print(f"you finished the Day [ TOTAL DAYS: {Globals.day} ]")

    for i in allkimeras:
            i.age += 1
            i.exhausted = False

    Globals.day += 1
    rtt = random.randint(1, 100) + foodquality
    actualize_breed(allkimeras)
    actualize_princesses(allkimeras)
    actualize_queen(allkimeras)

    if rtt > 80:
         rndstt = "Princess"
    else:
         rndstt = "Bone Eater"

    straykimera = kimera.randomkimera(rndstt, pipeshine)
    straykimera.age += 4
    print(f"A {straykimera.status} named {full_name_with_nickname(straykimera)} ( SCORE: {lookingsmaching(straykimera)} ) wants to enter in the colony! should you let him enter?")

    while Globals.gamerunning==2:
        print("[1] - YES")
        print("[2] - NO")
        ults = input("")

        if ults == "1":
            allkimeras.append(straykimera)
            print(f"{full_name_with_nickname(straykimera)} entered in your colony!")
            return

        elif ults == "2":
            print("You kick the stray kimera away!")
            return

        else:
            print("Invalid choice.")
            continue



def Start_Command():
    Globals.gamerunning = 1

def Breeding_Command():
    from Kimera import kimera
    from Kimeras_Data import allthekimerasforbreed, allkimeras

    if Globals.breeding == True:
        print("You are breeding already, restarting the process...\n")
        Globals.breeding = False

        return
    
    disponiveis = []
    for k in allthekimerasforbreed:
        if k.exhausted != True:
            disponiveis.append(k)

    if len(disponiveis) < 2:
        print("All your kimeras are exhausted or you don't have sufficient disponible kimeras to breed.")
        return
         
    
    Globals.breeding = True

    while Globals.gamerunning == 2:
        ()
        print("Please, choose 2 kimeras to procreate!")
        for number, kimerainlist  in enumerate(allthekimerasforbreed):
            if kimerainlist.exhausted == True:
                print((f"[{number+1}] - {kimerainlist.name} ( {kimerainlist.status} ) ( EXHAUSTED ) ( SCORE: {lookingsmaching(kimerainlist)} )"))
            else:    
                print((f"[{number+1}] - {kimerainlist.name} ( {kimerainlist.status} ) ( DISPONIBLE ) ( SCORE: {lookingsmaching(kimerainlist)} )"))
        print("Choose the first kimera!")

        choice_for_breed = input_player_in_the_hole()

        if choice_for_breed.isdigit():
            index_kimera = int(choice_for_breed) - 1
            if 0<=index_kimera<len(allthekimerasforbreed):
                kimeraescolhida01 = allthekimerasforbreed[index_kimera]
                if kimeraescolhida01.exhausted == True:
                    print("This kimera can't breed today anymore")
                    continue
                else:
                    print(f"You choose {kimeraescolhida01.name} to be procreate!")

                kimeras_restantes = []
                for k in allthekimerasforbreed:
                    if k != kimeraescolhida01:
                        kimeras_restantes.append(k)
                         
                for number02, kimerainlist02  in enumerate(kimeras_restantes):
                    if kimerainlist02.exhausted == True:
                        print((f"[{number02+1}] - {kimerainlist02.name} ( {kimerainlist02.status} ) ( EXHAUSTED ) ( SCORE: {lookingsmaching(kimerainlist02)} )"))
                    else: 
                        print((f"[{number02+1}] - {kimerainlist02.name} ( {kimerainlist02.status} ) ( DISPONIBLE ) ( SCORE: {lookingsmaching(kimerainlist02)} )"))

                print(f"Chose other kimera!")

                choice_for_breed02 = input_player_in_the_hole()
                if choice_for_breed02.isdigit():
                        index_kimera02 = int(choice_for_breed02) - 1
                        if 0<= index_kimera02 <len(kimeras_restantes):
                            kimeraescolhida02 = kimeras_restantes[index_kimera02]
                            if kimeraescolhida02.exhausted == True:
                                print("This kimera can't breed today anymore")
                                continue
                            else:
                                print(f"You choose {kimeraescolhida02.name} to be procreate!")
                                baby = kimera.breeding(kimeraescolhida01, kimeraescolhida02)
                                print(f"{kimeraescolhida01.name} and {kimeraescolhida02.name} made a beatiful baby! and named as ( {full_name_with_nickname(baby)} )")

                                baby.acthp = baby.total_max_hp
                                allkimeras.append(baby)

                                kimeraescolhida01.exhausted = True
                                kimeraescolhida02.exhausted = True

                                Globals.breeding = False

                                return
            

                        else:
                            print("Type a valid number.")
                            Globals.breeding = False
                            break  
                else:
                    print("Type a valid number.") 
                    Globals.breeding = False
                    break
                            
            else:
                print("Type a valid number.")
                Globals.breeding = False
                break
        else:
            print("Type a valid number.")
            Globals.breeding = False
            break

actions = {
    "breed": Breeding_Command,
    "bd": Breeding_Command,
    "start": Start_Command,
    "sleep": end_day,
    "lookteeths": look_teeths_again_Command,
    "lk": look_teeths_again_Command,
    "lookpoints": look_best_Command,
    "lkpt": look_best_Command,
    "lookallpoints": Points_list,
    "lkallpt": Points_list,
    "lookbones": lookcents_Command
}

def input_player_in_the_hole():
    ()
    while Globals.gamerunning==2:
        ()
        comm = input("")
        if comm in actions:
            actions[comm]()
            continue
        else:
            return comm

