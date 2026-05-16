from CLASSES.ENTITY import ENTITY
from PUBLIC.Public_Standards import *
from PUBLIC.Public_Enums import _ATTRIBUTE
def Enemy_AI_Choose(Enemy: ENTITY):
    My_Health = Enemy.Actual_Health
    My_Mana = Enemy.Actual_Mana
        Executed_Attacks = 0
        Maximum_Attacks = 1 + (Enemy.Total_Attribute(_ATTRIBUTE.EXTRA_ATTACKS))
        while True:
            self.Clean_Dead()
            if self.Get_Winner():
                break
            
            if Enemy.Stunned:
                print(f"{Enemy.Name} is STUNNED!!")
                time.sleep(1)
                Enemy.Stunned = False
                break
            
            print("Time to Act!\nActions:")
            print(f"[ 1 ] - BASIC ATTACK [ {Executed_Attacks} / {Maximum_Attacks} ]")
            
            for Order, Skill in enumerate(Enemy.Skills):
                if Skill.Mana_Cost > 0:
                    print(f"[ {Order + 2} ] - {Skill.Name} ( {Skill.Mana_Cost} Mana )")
                else:
                    print(f"[ {Order + 2} ] - {Skill.Name}")
                    
            Intent = Loop_Input()
            
            if Intent == "1":
                if Executed_Attacks >= Maximum_Attacks:
                    print("You already used ALL your basic attacks this TURN")
                    
                else:
                    Basic_Attack_Target = Target_Choice(self.Get_Enemy_Team(Enemy))
                    
                    if not Basic_Attack_Target:
                        continue
                    
                    if Basic_Attack_Target.Actual_Health > 0:
                        COMBAT_DATA.Basic_Attack(Enemy, Basic_Attack_Target)
                        Executed_Attacks += 1
                        continue
                        
            elif Intent.isdigit():
                Index = int(Intent) - 2
                if 0 <= Index < len(Enemy.Skills):
                    Used_Skill = Enemy.Skills[Index]
                    Casted = Used_Skill.Cast(Enemy, self)
                    print(Casted)
                    
                    continue
                else:
                    print("INVALID")
                    
            elif Intent.lower() in ("endturn", "et", "end turn", "endt", "end_turn", "end", "stop", "break", "turn"):
                print(f"{Enemy.Name} ended {"his" if Enemy.Gender == _GENDER.MALE else "her"} turn!")
                self.Character_turn_end(Enemy)
                break
            
            else:
                print("INVALID")
                continue   
