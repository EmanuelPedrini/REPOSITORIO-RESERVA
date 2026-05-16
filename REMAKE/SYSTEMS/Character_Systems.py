from CLASSES.ENTITY import ENTITY
from SYSTEMS.Combat_System import COMBAT_SYSTEM
from SYSTEMS.Combat_System import COMBAT_DATA
from PUBLIC.Public_Enums import _ATTRIBUTE, _ATTACK_DISTANCE, _GENDER
from PUBLIC.Public_Standards import *
from SYSTEMS.Command_System import Loop_Input, Target_Choice, Validate_Enumbered_Choice

# def Show_Character_Options(Character: ENTITY, Combat: COMBAT_SYSTEM):
    
#         Executed_Attacks = 1 + (Character.Total_Attribute(_ATTRIBUTE.EXTRA_ATTACKS))
#         Maximum_Attacks = Executed_Attacks
        
#         print(f"> It`s {Character.Name}'s Turn!")
#         print(f"> {Character.Name} HP: {Character.Actual_Health} / {Character.Total_Attribute(_ATTRIBUTE.MAX_HEALTH)}")
#         print(f"> {Character.Name} MANA: {Character.Actual_Mana} / {Character.Total_Attribute(_ATTRIBUTE.MAX_MANA)}")
        
#         while True:
#             if Character.Stunned:
#                 print(f"{Character.Name} is STUNNED!!")
#                 time.sleep(1)
#                 Character.stunned = False
#                 break
#             print("> Time to Act!\n> Actions:")
#             print(f"[ 1 ] - BASIC ATTACK [ {Executed_Attacks} / {Maximum_Attacks} ]")
            
#             for Order, Skill in enumerate(Character.Skills):
#                 if Skill.Mana_Cost > 0:
#                     print(f"[ {Order + 2} ] - {Skill.Name} ( {Skill.Mana_Cost} Mana )")
#                 else:
#                     print(f"[ {Order + 2} ] - {Skill.Name}")
                    
#             Intent = Loop_Input()
            
#             if Intent == "1":
#                 if Executed_Attacks >= Maximum_Attacks:
#                     print("You already used ALL your basic attacks this TURN")
                    
#                 else:
#                     Basic_Attack_Target = Target_Choice(Combat.Get_Enemy_Team(Character))
#                     if Basic_Attack_Target == None:
#                         continue
                    
#                     if Basic_Attack_Target.Actual_Health > 0:
#                         COMBAT_DATA.Basic_Attack(Character, Basic_Attack_Target)
#                         Executed_Attacks += 1
                        
#                     if Basic_Attack_Target.Actual_Health <= 0:
#                         Combat.Clean_Dead()
#                         if Combat.Get_Winner:
#                             break
                        
#             elif Intent.isdigit():
#                 Index = int(Intent) - 2
#                 if 0 <= Index < len(Character.Skills):
#                     Used_Skill = Character.Skill[Index]
#                     Skill.Cast(Character, Combat)
#                     Combat.Clean_Dead()
#                     if Combat.Get_Winner:
#                         break
#                 else:
#                     print("INVALID")
                    
#             elif Intent.lower() in ("endturn", "et", "end turn", "endt", "end_turn", "end", "stop", "break", "turn"):
#                 print(f"{Character.name} ended {"his" if Character.Gender == _GENDER.MALE else "her"} turn!")
#                 Character_turn_end(Character)
#                 break
            
#             else:
#                 print("INVALID")
#                 continue

# def Character_turn_end(Character):
#     pass