from CLASSES.ENTITY import ENTITY
from PUBLIC.Public_Enums import _ATTRIBUTE, _ATTACK_DISTANCE
from PUBLIC.Public_Standards import *
from SYSTEMS.Command_System import Loop_Input

def Show_Character_Options(Character: ENTITY):
        Executed_Attacks = 1 + (Character.Total_Attribute(_ATTRIBUTE.EXTRA_ATTACKS))
        Maximum_Attacks = Executed_Attacks
        print(f"> It`s {Character.Name}'s Turn!")
        print(f"> {Character.Name} HP: {Character.Actual_Health} / {Character.Total_Attribute(_ATTRIBUTE.MAX_HEALTH)}")
        print(f"> {Character.Name} MANA: {Character.Actual_Mana} / {Character.Total_Attribute(_ATTRIBUTE.MAX_MANA)}")
        while True:
            if Character.Stunned:
                print(f"{Character.Name} is STUNNED!!")
                time.sleep(1)
                Character.stunned = False
                break
            print("> Time to Act!\n> Actions:")
            print(f"[ 1 ] - BASIC ATTACK [ {Executed_Attacks} / {Maximum_Attacks} ]")
            
            for Order, Skill in enumerate(Character.Skills):
                if Skill.Mana_Cost > 0:
                    print(f"[ {Order + 2} ] - {Skill.Name} ( {Skill.Mana_Cost} Mana )")
                else:
                    print(f"[ {Order + 2} ] - {Skill.Name}")
            Intent = Loop_Input()
                
            

def playerturn(Character, actenemy, sav2):
             choice = Loop_Input()     
             if choice =="1":
                    if Ataque_Basico_Nao_Disponivel:
                         print("You already used your basic attack this turn!")
                         continue
                    
                    else: 
                        target = escolhadealvo(Character, actenemy)
                        if target == None:
                             continue
                        
                        if target.acthp > 0:
                            Character.basicattack(target, Character)
                            Ataque_Basico_Nao_Disponivel = True

                        if target.acthp <= 0:
                            if target in actenemy:
                                actenemy.remove(target)
                            bomb = check_alive(Character, sav2)
                            if bomb:
                                 break
                            continue
            
             elif choice.isdigit():
                    sedex= int(choice) - 2
                       
                    if 0 <= sedex < len(Character.skills):
                         skill = Character.skills[sedex] 
                         skill.use(Character,escolhadealvo,actenemy)
                         conf = check_alive(Character, sav2)
                         if conf:
                              break
                    
                    else:
                         print("Sorry, that is a invalid Ability.")
                         continue
                       
             elif choice == "lookskill" or choice == "lksk":
                    print("YOUR SKILLS:")
                    for i, ski in enumerate(Character.skills):
                         print(f"[{i+1}] - {ski.basename} ( {ski.cost} Mana )")
                    analize_choice = input("Which skill you want to look closely?\n> ")
                    if analize_choice.isdigit():
                         sdx = int(analize_choice) - 1
                         if 0<= sdx <len(Character.skills):
                              skill_alisada = Character.skills[sdx]
                              print(f"{skill_alisada.basename}") 
                              print(f"- {skill_alisada.text}")
                              if skill_alisada.damage>0:
                                   print(f"DAMAGE: {skill_alisada.damage + (Character.temporary_magicdmgbonus + Character.magicdmgbonus)}")
                                   if skill_alisada.target=="allenemies":
                                        print(f"This skill cause damage to ALL ENEMIES.")
                                   else:
                                        print("This skill cause damage to a SINGLE TARGET.")

                              if skill_alisada.heal > 0:
                                   print(f"HEALING: {skill_alisada.heal}")

                              if skill_alisada.shieldgain > 0:
                                   print(f"SHIELD GAIN: {skill_alisada.shieldgain}")

                              if skill_alisada.cost > 0:
                                   print(f"MANA COST: {skill_alisada.cost - (Character.skillcostmodifier + Character.temporary_skillcostmodifier)}")
                              print("")
                         else:
                              print("Thats a invalid skill.")
                    else:
                         print("Please, type a valid choice. ")
                              


             elif choice in ("endturn", "et"):
                    print(f"{Character.name} ended {Character.possessive} turn!")
                    player_turn_end(Character)
                    break

             else:
               print("Sorry, thats a invalid Command.")
                