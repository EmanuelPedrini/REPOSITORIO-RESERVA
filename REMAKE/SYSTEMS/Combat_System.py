import os
from CLASSES.ENTITY import ENTITY
from PUBLIC.Public_Enums import _ATTRIBUTE, _ATTACK_DISTANCE, _SIDE, _GENDER
from CLASSES.SKILLS import _SKILL
from PUBLIC.Public_Classes import DAMAGE
from CLASSES.BASIC_ATTACK import _BASIC_ATTACK
from PUBLIC.Public_Standards import *
from SYSTEMS.Command_System import Loop_Input, Target_Choice, Validate_Enumbered_Choice

class COMBAT_SYSTEM:
    def __init__(self, Team_A, Team_B):
        self.Entities = Team_A + Team_B
        self.Team_A = Team_A
        self.Team_B = Team_B
        self.Log = COMBAT_LOG()
    
    def Get_Enemy_Team(self, Attacker) -> list:
        Enemy_Team = self.Team_B if Attacker in self.Team_A else self.Team_A
        Teaming = [ Enemy for Enemy in Enemy_Team if Enemy.Alive ]
        if Teaming:
            return Teaming
        return []
    
    def Get_Ally_Team(self, Attacker):
        Ally_Team = self.Team_A if Attacker in self.Team_A else self.Team_B
        Teaming = [ Ally for Ally in Ally_Team if Ally.Alive ]
        if Teaming:
            return Teaming
        return []

    def Team_Dead(self, Team) -> bool:
        return all(not e.Alive for e in Team)
    
    def Get_Winner(self) -> _SIDE | None:
        
        if self.Team_Dead(self.Team_A): 
            return _SIDE.ENEMY
        
        elif self.Team_Dead(self.Team_B): 
            return _SIDE.PLAYER
        
        return None

    def Clean_Dead(self):
        self.Team_A = [ e for e in self.Team_A if e.Alive ]
        self.Team_B = [ e for e in self.Team_B if e.Alive ]
        self.Entities = self.Team_A + self.Team_B
        
    def Print_Label(self):
        pass
    
    #PARÂMETROS DE TEMPO EM COMBATE
    def Turn_Start(self):
        pass
    
    def Turn_End(self, Entity):
        self.Log.Add(f"{Entity.Name} ended {'his' if Entity.Gender == _GENDER.MALE else 'her'} TURN!")
        Entity.Regenerate_Mana(Entity.Total_Attribute(_ATTRIBUTE.MANA_REGEN))
        Entity.Heal(Entity.Total_Attribute(_ATTRIBUTE.HEALTH_REGEN))
        pass
    
    def Combat_End(self):
        pass
    
    def Combat_Start(self):
        pass
    
    def Round_Start(self):
        pass
    
    def Round_End(self):
        pass
    
    def Show_Options(self, Character, Ex, Max):
        Order = 1
        Log = []
        Log.append(f"[ 0 ] - END TURN!")
        for Attack in Character.Current_Attacks:
            Log.append(f"[ {Order} ] - {Attack.Name} [ {Ex} / {Max} ]")
            Order +=1

        for Skill in Character.Skills:
            if Skill.Mana_Cost > 0:
                Log.append(f"[ {Order} ] - {Skill.Name} [ {Skill.Mana_Cost} Mana ]")
                Order +=1
                
            else:
                Log.append(f"[ {Order} ] - {Skill.Name}")
                Order +=1
        return Log
                
    def Show_Action_Order(self, Actual_Turn):
        Log = []
        for Entity in self.Entities:
            if Entity == Actual_Turn:
                Log.append(f" -> {Entity.Name}")
            else:
                Log.append(f" {Entity.Name}")
        return Log
    
    def Build_Combat_Screen(self,
                            Actual_Turn,
                            Character = None,
                            Executed_Attacks = None,
                            Maximum_Attacks = None,
                            ):
        
        Screen = []
        Screen.append(" <=============== TURN ORDER ===============> \n")
        Screen.extend(self.Show_Action_Order(Actual_Turn))
        
        Screen.append("")
        Screen.append(f" <=============== COMBAT LOG ===============> \n")
        Recent_Logs = self.Log.Recent()
        
        if Recent_Logs:
            Screen.extend(Recent_Logs)
        else:
            Screen.append("Any action made already!")
            
        if Character is not None:
            Screen.append("")
            Screen.append(" <=============== CURRENT TURN =============> \n")
            Screen.append(f"It`s {Character.Name}'s Turn!")
            
            Screen.append(
                f"{Character.Name} HP: {Character.Actual_Health} / {Character.Total_Attribute(_ATTRIBUTE.MAX_HEALTH)}"
            )
            
            Screen.append(
                f"{Character.Name} MANA: {Character.Actual_Mana} / {Character.Total_Attribute(_ATTRIBUTE.MAX_MANA)}"
            )

            Screen.append("")
            Screen.append(" <=============== ACTIONS ==================> \n")
            
            Screen.extend(
                self.Show_Options(Character, Executed_Attacks, Maximum_Attacks)
            )
        return "\n".join(Screen)
    
    def Render_Combat_Screen(
        self,
        Actual_Turn,
        Character=None,
        Executed_Attacks=None,
        Maximum_Attacks=None
    ):
        self.Clear_Terminal()
        print(
            
        self.Build_Combat_Screen(
            Actual_Turn,
            Character,
            Executed_Attacks,
            Maximum_Attacks
        )
        
        )
    
    def Clear_Terminal(self):
        os.system("cls" if os.name == "nt" else "clear")
        
    def Show_Character_Options(self, Character):
        
            Executed_Attacks = 0
            Maximum_Attacks = 1 + (Character.Total_Attribute(_ATTRIBUTE.EXTRA_ATTACKS))

            while True:
                self.Clean_Dead()
                if self.Get_Winner():
                    break
                
                if Character.Stunned:
                    self.Log.Add(f"{Character.Name} is STUNNED!!")
                    time.sleep(1)
                    Character.Stunned = False
                    break

                self.Render_Combat_Screen(
                    Character,
                    Character,
                    Executed_Attacks,
                    Maximum_Attacks
                )

                Intent = Loop_Input()
                if Intent.isdigit():
                    Character_Options = Character.Current_Attacks + Character.Skills
                    Index = int(Intent) - 1
                    if 0 <= Index < len(Character_Options):
                        Used = Character_Options[Index]
                        if isinstance(Used, _SKILL):
                            Utilized = Used.Cast(Character, self)
                            self.Log.Add(Utilized)
                        elif isinstance(Used, _BASIC_ATTACK):
                            if Executed_Attacks < Maximum_Attacks:
                                Utilized = Used.Basic_Attack(Character, self)
                                Executed_Attacks += 1
                                self.Log.Add(Utilized)  
                            else:
                                Utilized = f"{Character.Name} used all ATTACKS for this TURN!"
                                self.Log.Add(Utilized)
                    elif Index == -1:
                        self.Turn_End(Character)
                        break
                    
                    else:
                        print("INVALID")
                        time.sleep(1)
                        
                elif Intent.lower() in ("endturn", "et", "end turn", "endt", "end_turn", "end", "stop", "break", "turn"):
                    self.Turn_End(Character)
                    break
                
                else:
                    print("INVALID")
                    time.sleep(1)
                    continue
        
    def Enemy_Turn(self, Enemy):
        Executed_Attacks = 0
        Maximum_Attacks = 1 + (Enemy.Total_Attribute(_ATTRIBUTE.EXTRA_ATTACKS))
        
        while True:
            self.Clean_Dead()
            if self.Get_Winner():
                break
            
            Possible_Skills = [Skill for Skill in Enemy.Skills if Skill.Can_Cast(Enemy)]
            if Enemy.Stunned:
                time.sleep(1)
                Enemy.Stunned = False
                break
        
            elif Executed_Attacks < Maximum_Attacks:
                if not Enemy.Current_Attacks:
                    return
                
                Attack_Report = random.choice(Enemy.Current_Attacks)
                Attack_Report = Attack_Report.Basic_Attack(Enemy, self)
                
                self.Log.Add(Attack_Report)
                
                self.Render_Combat_Screen(Enemy)
                time.sleep(0.7)
                
                Executed_Attacks += 1
                continue
              
            elif Possible_Skills:
                    Used_Skill = random.choice(Possible_Skills)
                    Casted = Used_Skill.Cast(Enemy, self)
                    
                    self.Render_Combat_Screen(Enemy)
                    time.sleep(0.7)
                    
                    self.Log.Add(Casted)
                    continue   
            else: 
                self.Log.Add(
                    f"{Enemy.Name} ended {'his' if Enemy.Gender == _GENDER.MALE else 'her'} TURN!"
                )
                
                self.Turn_End(Enemy)
                break

    def Combat_Between(self):
        Combat_Running = True
        
        On_Combat_Entities = self.Team_A + self.Team_B
        
        tm = TURN_MASTER(On_Combat_Entities)
        
        while Combat_Running:
            
            tm.Clean_Dead()
            if self.Get_Winner():
                print(self.Get_Winner())
                self.Combat_End()
                break
            Actual_Turn = tm.Turn()
            if Actual_Turn.Alive :
                if Actual_Turn.Side == _SIDE.PLAYER:
                    self.Show_Character_Options(Actual_Turn)      
                elif Actual_Turn.Side == _SIDE.ENEMY:
                    self.Render_Combat_Screen(Actual_Turn)
                    time.sleep(0.5)
                    self.Enemy_Turn(Actual_Turn)
            tm.Next_Turn()
            
class TURN_MASTER:
    def __init__(self, Entities):
        self.Entities = Entities
        self.turn = 0
        self.Round = 0

    def Turn(self):
        return self.Entities[self.turn]

    def Next_Turn(self):
        self.turn += 1
        if self.turn >= len(self.Entities):
            self.turn = 0

    def Clean_Dead(self):
        self.Entities = [e for e in self.Entities if e.Alive]
        if self.turn >= len(self.Entities):
            self.turn = 0
            self.Round += 1

class COMBAT_LOG:
    def __init__(self, 
                 Maximum_Lines = 9):
        self.Messages = []
        self.Maximum_Lines = Maximum_Lines
        
    def Add(self, Message):
        if not Message:
            return
        if isinstance(Message, list):
            self.Messages.extend(Message)
        else:
            self.Messages.extend(str(Message).splitlines())
            
    def Recent(self):
        return self.Messages[-self.Maximum_Lines:]
            