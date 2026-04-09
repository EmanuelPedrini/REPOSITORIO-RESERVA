from Turnmaster import Turnmaster; from Commands import input_player; from Commands import escolhadealvo
from Bosses import boss; import Globals; from Kimeras_Data import allkimeras; 
from FinalBoss import finalboss
combatfinished = False; bossbattle = False; finalbossbattle = False
def check_alive(playercur, enemieslist):
    global combatfinished
    alive = [e for e in enemieslist if e.acthp > 0]
    if not alive and not combatfinished:
        combatfinished=True
        combat_end(playercur)
        return True 
def resetbonus(player):
    player.bonus_strg = 0; player.bonus_dex = 0; player.bonus_vit = 0; player.bonus_luck = 0; 
    player.bonus_cha = 0; player.bonus_intel = 0; player.temporary_skillcostmodifier = 0; player.temporary_magicdmgbonus = 0
    player.temporary_bonus_to_right = 0; player.temporary_bonus_to_left = 0; player.temporary_atkdmgbonus = 0

def combat_start(player):
    player.actmana = player.mana_inicial; player.shield = player.shieldstat; resetbonus(player)

def combat_end(player):
    from THE_HOLE import full_name_with_nickname
    global bossbattle, finalbossbattle
    print("All enemies are DEAD! you WIN!")

    if Globals.gained_cents_battle>0:
        player.gain_cents(Globals.gained_cents_battle)
        Globals.gained_cents_battle = 0
        
    if Globals.gained_xp_battle>0:
        player.gain_xp(Globals.gained_xp_battle)
        Globals.gained_xp_battle = 0

    if Globals.gained_itens_battle:
         for itm in Globals.gained_itens_battle:
              player.add_item(itm)
    Globals.gained_itens_battle = []

    for ps in player.passives:
        if ps.trigger=="on_combat_end":
            ps.passiveactivationtrigger(player)

    resetbonus(player)

    while Globals.gamerunning==1:
        if player.xp >= player.xptonext:
               player.level_system()
        else:
            break

    if Globals.gained_kimeras_battle:
            for wk in Globals.gained_kimeras_battle[:]:
                print(f"A kimera named {full_name_with_nickname(wk)} that you fought against wants to join your colony in act of merciness")
                print("[1] - YES, ENTER MY COLONY")
                print("[2] - KILL YOUR RIVAL! NO MERCY!")
                cho=input("")
                if cho=="1":
                     print(f"{full_name_with_nickname(wk)} entered in your COLONY!")
                     allkimeras.append(wk)
                     Globals.gained_kimeras_battle.remove(wk)
                elif cho=="2":
                     print("YOU DECAPITATE THE WILD KIMERA! NO ROOM FOR PITY!")
                     Globals.gained_kimeras_battle.remove(wk)

                else:
                     print("Invalid")
                     continue
    Globals.gained_kimeras_battle = []
            
    if finalbossbattle:
        from Kimeras_Data import Queen
        from THE_HOLE import full_name_with_nickname
        print(f"As the battle heat stops, you perceives your mother stills alive in the battlefield although she is most dead than alive\n" \
        f"[ {full_name_with_nickname(Queen)} ] - KILL ME!! TAKE MY PLACE!")

        while Globals.gamerunning==1:
             print(f"[1] - KILL HER, SUBDUE YOUR OWN MOTHER AND BECAME THE NEW QUEEN. ({full_name_with_nickname(Queen)} will be REMOVED from your kimeras PERMANENTLY)")
             print(f"[2] - SAVE HER LIFE ({full_name_with_nickname(Queen)} will remain being a QUEEN and you a PRINCESS)")

             ultsss=input("")

             if ultsss == "1":
                  allkimeras.remove(Queen)
                  player.status = "Queen"
                  print(f"You kill and take your mother's place. That's cruel, but it's the Kimera's day-to-day")
                  return
             
             elif ultsss == "2":
                  print("You let your mother live and maintain the actual hierarchy!")
                  return
             
             else:
                  print("It's kill or not, buddy.")
                  continue


        import THE_HOLE

        convert = (Globals.runcents // 5)
        THE_HOLE.bones += convert

        Globals.runcents = 0
        convert = 0
        
        allkimeras.append(player)

        Globals.endofarun = True
        return
    
    elif bossbattle:
         if Globals.act ==1:
              Globals.act = 2

def player_turn_start():
     pass

def player_turn_end(player):
     player.regen_mana()

def turn_start():
     pass

def turn_end():
     pass

#definições de combate
def playerturn(player, actenemy, sav2):
        global bossbattle

        ppman = player.actmana
        ppantibug = player.total_max_hp

        print("> It`s Your Turn!")
        print(f"> {player.name} actually have {player.acthp} / {ppantibug} health points!")
        print(f"> You actually have [ {ppman} / {player.max_mana} ] Mana Points!")

        Ataque_Basico_Nao_Disponivel = False

        if player.stunned:
             print("You are stunned!")
             player.stunned = False
             return

        #Ações possíveis
        while Globals.gamerunning == 1:
             print(f"> HP: {player.acthp} / {player.total_max_hp} ")
             print(f"> MP: {player.actmana} / {player.max_mana} ")
             print("> Time to Act!\n> Actions:")
             print("[1] - BASIC ATTACK")
             for i, ski in enumerate(player.skills):
                  print(f"[{i+2}] - {ski.basename} ( {ski.cost} Mana )")
                  
             choice = input_player(player, actenemy)     
             if choice =="1":
                    if Ataque_Basico_Nao_Disponivel:
                         print("You already used your basic attack this turn!")
                         continue
                    
                    else: 
                        target = escolhadealvo(player, actenemy)
                        if target == None:
                             continue
                        
                        if target.acthp > 0:
                            player.basicattack(target, player)
                            Ataque_Basico_Nao_Disponivel = True

                        if target.acthp <= 0:
                            if target in actenemy:
                                actenemy.remove(target)
                            bomb = check_alive(player, sav2)
                            if bomb:
                                 break
                            continue
            
             elif choice.isdigit():
                    sedex= int(choice) - 2
                       
                    if 0 <= sedex < len(player.skills):
                         skill = player.skills[sedex] 
                         skill.use(player,escolhadealvo,actenemy)
                         conf = check_alive(player, sav2)
                         if conf:
                              break
                    
                    else:
                         print("Sorry, that is a invalid Ability.")
                         continue
                       
             elif choice == "look" or choice == "lk":
                    analize_choice = input("Which skill you want to look closely?")
                    if analize_choice.isdigit():
                         sdx = int(analize_choice) - 1

             elif choice in ("endturn", "et"):
                    print(f"{player.name} ended {player.possessive} turn!")
                    player_turn_end(player)
                    break

             else:
               print("Sorry, thats a invalid Command.")
                
def enemyturn(enemy, player):
        if enemy.stunned:
             print(f"{enemy.name} is STUNNED!")
             enemy.stunned = False
             return
        enemy.attack(player)
        if player.acthp <=0:
            player.death()

#ANCORA 1
def combat(player, enemies):
    global bossbattle, combatfinished, finalbossbattle
    combatfinished = False
    finalbossbattle = False
    bossbattle = False
    fullhpfinalboss= False
    sav = enemies
    oncombat=[player] + enemies
    tm = Turnmaster(oncombat)
    combat_start(player)
    boss_enemy = next((e for e in enemies if isinstance(e, boss)), None)
    final_enemy = next((e for e in enemies if isinstance(e, finalboss)), None)

    if final_enemy:
         if not fullhpfinalboss:
              for e in enemies:
                   e.acthp=e.totalmaxhp
                   fullhpfinalboss= True

         print(f"{final_enemy.intro}")

         bossbattle= True

         finalbossbattle = True


    elif boss_enemy:
         print(f"{boss_enemy.intro}")
         bossbattle = True
    
    else:
         print("TIME TO DIE!, from the tar of the void some enemies arise!")

    print("ACTION QUEUE:\n")
    savis = (player.total_max_hp)
    print(f"- {player.name} ( {player.acthp} / {savis})")
    print("")
    for e in enemies:
            if e.acthp > 0:
                print(f"- {e.name} ( {e.acthp} / {e.totalmaxhp} HP )")
            print("")
            
    #essa é a parte que define o loop do combat
    while Globals.gamerunning==1:
        #primeiro ele usa a função que remove os inimigos mortos, ela vem do turnmaster que ta em outro arquivo
        tm.removermortos()

        #ele checa se o player morreu
        if player.acthp <= 0:
            player.death()
            break

        #checa se os inimigos morreram
        comb = check_alive(player, enemies)
        if combatfinished:
             break
        
        actualturn = tm.vezdequem()
        if actualturn==player:
             playerturn(player, enemies, sav2=enemies)
        else:
             enemyturn(actualturn, player)
        
        if combatfinished:
             break

        tm.passarturno()