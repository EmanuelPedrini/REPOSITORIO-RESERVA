from CLASSES.ENTITY import ENTITY
from PUBLIC.Public_Enums import _ATTRIBUTE, _ATTACK_DISTANCE, _SIDE, _GENDER
from PUBLIC.Public_Classes import DAMAGE
from PUBLIC.Public_Standards import *
from SYSTEMS.Command_System import Loop_Input, Target_Choice, Validate_Enumbered_Choice

class COMBAT_DATA:
    @staticmethod
    def Attack_Roll(Target):
        Entity_Dodge = Target.Total_Attribute(_ATTRIBUTE.DODGE)
        return (random.randint(1, 100) > Entity_Dodge)

    @staticmethod
    def Critical_Roll(Attacker):
        Entity_Critical_Chance = Attacker.Total_Attribute(_ATTRIBUTE.CRITICAL_CHANCE)
        return random.randint(1, 100) <= Entity_Critical_Chance
    
    @staticmethod
    def Counter_Attack_Roll(Target):
        Entity_Counter = Target.Total_Attribute(_ATTRIBUTE.COUNTERATTACK)
        return random.randint(1, 100) <= Entity_Counter
    
    @staticmethod
    def Calculate_Damage(Attacker):
        #CALCS
        Attacker_Distance = Attacker.Current_Attack_Distance
        
        if Attacker_Distance == _ATTACK_DISTANCE.MELEE:
            Special_Attribute = _ATTRIBUTE.MELEE_DAMAGE
            Main_Attribute = (_ATTRIBUTE.MUSCLES)
           
        else:
            Special_Attribute = (_ATTRIBUTE.RANGED_DAMAGE)
            Main_Attribute = (_ATTRIBUTE.HASTE)
            
        Attack_Special_Value = (Attacker.Total_Attribute(Special_Attribute) * 0.75)
        Attack_Core_Value = (Attacker.Total_Attribute(Main_Attribute)) * 10
            
        Total_Attack = (Attack_Special_Value + Attack_Core_Value)
            
        if Attacker_Distance == _ATTACK_DISTANCE.RANGED:
            Total_Attack = 2 + ((Total_Attack) * 0.75)
        
        Total_Attack *= (1 + Attacker.Total_Attribute(_ATTRIBUTE.DAMAGE)/100)
            
        Static_Damage = max(0, int(Total_Attack * 0.85))
        Random_Damage = random.randint(0, int((Total_Attack) * 0.30))
        return Static_Damage + Random_Damage
    
    @staticmethod
    def Basic_Attack(Attacker, Target, Can_Counter: bool = True):
        if COMBAT_DATA.Attack_Roll(Target):
            Total_Damage_Amount = COMBAT_DATA.Calculate_Damage(Attacker)
            
            if COMBAT_DATA.Critical_Roll(Attacker):
                Total_Damage_Amount = int(Total_Damage_Amount * Attacker.Total_Attribute(_ATTRIBUTE.CRITICAL_MULTIPLIER))
                
            Damage_taken = DAMAGE(Total_Damage_Amount, 
                                Attacker.Current_Attack_Type, 
                                Attacker)
            
            Damage_Taken_After_Resistances = Target.Take_Damage(Damage_taken)
            Fatal_Attack = (Target.Actual_Health) <= 0
            
            Vampirism = Attacker.Total_Attribute(_ATTRIBUTE.VAMPIRISM)
            Target_Thorns = Target.Total_Attribute(_ATTRIBUTE.THORNS)
            
            if Vampirism > 0:
                Attacker.Heal(int(Damage_Taken_After_Resistances * Vampirism/100))
            
            if Target_Thorns > 0:
                if not Fatal_Attack:
                    Attacker.Take_Damage(DAMAGE(Target_Thorns, Target.Thorns_Type, Target, Fathal=False))
            
            if Can_Counter:
                if not Fatal_Attack:
                    if COMBAT_DATA.Counter_Attack_Roll(Target):
                        COMBAT_DATA.Basic_Attack(
                            Target,
                            Attacker,
                            Can_Counter = False
                        )
                
            #TESTES TEMPORÁRIOS!!!
            print(f"{Attacker.Name} attacked {Target.Name}, causing {Damage_Taken_After_Resistances} damage! \n{Target.Name} HP: {Target.Actual_Health} / {Target.Total_Attribute(_ATTRIBUTE.MAX_HEALTH)}")
            return True
        else:
            print(f"{Attacker.Name} missed a attack against {Target.Name}")
            return False


class COMBAT_SYSTEM:
    def __init__(self, Team_A, Team_B):
        self.Entities = Team_A + Team_B
        self.Team_A = Team_A
        self.Team_B = Team_B
    
    def Get_Enemy_Team(self, Attacker) -> list:
        Enemy_Team = self.Team_B if Attacker in self.Team_A else self.Team_A
        Teaming = [ Enemy for Enemy in Enemy_Team if Enemy.Actual_Health > 0 ]
        if Teaming:
            return Teaming
        return []
    
    def Get_Ally_Team(self, Attacker):
        Ally_Team = self.Team_A if Attacker in self.Team_A else self.Team_B
        Teaming = [ Ally for Ally in Ally_Team if Ally.Actual_Health > 0 ]
        if Teaming:
            return Teaming
        return []

    def Team_Dead(self, Team) -> bool:
        return all(e.Actual_Health <= 0 for e in Team)
    
    def Get_Winner(self) -> _SIDE | None:
        if self.Team_Dead(self.Team_A): 
            return _SIDE.ENEMY
        elif self.Team_Dead(self.Team_B): 
            return _SIDE.PLAYER
        return None

    def Clean_Dead(self):
        self.Team_A = [ e for e in self.Team_A if e.Actual_Health > 0 ]
        self.Team_B = [ e for e in self.Team_B if e.Actual_Health > 0 ]
        self.Entities = self.Team_A + self.Team_B
        
    def Print_Label(self):
        pass
        
    def Character_turn_end(self, Character):
        pass
        
    def Show_Character_Options(self, Character: ENTITY):
        
            Executed_Attacks = 0
            Maximum_Attacks = 1 + (Character.Total_Attribute(_ATTRIBUTE.EXTRA_ATTACKS))
            
            print(f"It`s {Character.Name}'s Turn!")
            print(f"{Character.Name} HP: {Character.Actual_Health} / {Character.Total_Attribute(_ATTRIBUTE.MAX_HEALTH)}")
            print(f"{Character.Name} MANA: {Character.Actual_Mana} / {Character.Total_Attribute(_ATTRIBUTE.MAX_MANA)}")
            
            while True:
                self.Clean_Dead()
                if self.Get_Winner():
                    break
                
                if Character.Stunned:
                    print(f"{Character.Name} is STUNNED!!")
                    time.sleep(1)
                    Character.Stunned = False
                    break
                
                print("Time to Act!\nActions:")
                print(f"[ 1 ] - BASIC ATTACK [ {Executed_Attacks} / {Maximum_Attacks} ]")
                
                for Order, Skill in enumerate(Character.Skills):
                    if Skill.Mana_Cost > 0:
                        print(f"[ {Order + 2} ] - {Skill.Name} ( {Skill.Mana_Cost} Mana )")
                    else:
                        print(f"[ {Order + 2} ] - {Skill.Name}")
                        
                Intent = Loop_Input()
                
                if Intent == "1":
                    if Executed_Attacks >= Maximum_Attacks:
                        print("You already used ALL your basic attacks this TURN")
                        
                    else:
                        Basic_Attack_Target = Target_Choice(self.Get_Enemy_Team(Character))
                        
                        if not Basic_Attack_Target:
                            continue
                        
                        if Basic_Attack_Target.Actual_Health > 0:
                            COMBAT_DATA.Basic_Attack(Character, Basic_Attack_Target)
                            Executed_Attacks += 1
                            continue
                            
                elif Intent.isdigit():
                    Index = int(Intent) - 2
                    if 0 <= Index < len(Character.Skills):
                        Used_Skill = Character.Skills[Index]
                        Casted = Used_Skill.Cast(Character, self)
                        print(Casted)
                        
                        continue
                    else:
                        print("INVALID")
                        
                elif Intent.lower() in ("endturn", "et", "end turn", "endt", "end_turn", "end", "stop", "break", "turn"):
                    print(f"{Character.Name} ended {"his" if Character.Gender == _GENDER.MALE else "her"} turn!")
                    self.Character_turn_end(Character)
                    break
                
                else:
                    print("INVALID")
                    continue
                
    def Enemy_Turn(self, Enemy):
        Possible_Target = self.Get_Enemy_Team(Enemy)
        if not Possible_Target:
            self.Clean_Dead()
            return
        Wanted_Target = random.choice(self.Get_Enemy_Team(Enemy))
        COMBAT_DATA.Basic_Attack(Enemy, Wanted_Target)
        print("Enemy played a turn")

    def Combat_Between(self):
        
        Combat = COMBAT_SYSTEM(self.Team_A, self.Team_B)
        
        Combat_Running = True
        
        On_Combat_Entities = self.Team_A + self.Team_B
        
        tm = TURN_MASTER(On_Combat_Entities)
        
        while Combat_Running:
            
            tm.Clean_Dead()
            
            if Combat.Get_Winner():
                print(Combat.Get_Winner())
                break
            
            Actual_Turn = tm.Turn()
            if Actual_Turn.Alive :
                if Actual_Turn.Side == _SIDE.PLAYER:
                    Combat.Show_Character_Options(Actual_Turn)      
                elif Actual_Turn.Side == _SIDE.ENEMY:
                    Combat.Enemy_Turn(Actual_Turn)
            tm.Next_Turn()
            
            
        
        
class TURN_MASTER:
    def __init__(self, Entities):
        self.Entities = Entities
        self.turn = 0
        self.Round = 0

    def Turn(self):
        return self.Entities[self.turn]

    def Next_Turn(self):
        self.turn+=1
        if self.turn >= len(self.Entities):
            self.turn = 0

    def Clean_Dead(self):
        self.Entities = [e for e in self.Entities if e.Actual_Health > 0]
        if self.turn >= len(self.Entities):
            self.turn= 0
            self.Round += 1