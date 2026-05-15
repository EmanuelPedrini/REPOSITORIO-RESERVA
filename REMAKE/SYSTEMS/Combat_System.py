from CLASSES.ENTITY import ENTITY
from PUBLIC.Public_Enums import _ATTRIBUTE, _ATTACK_DISTANCE, _SIDE
from PUBLIC.Public_Classes import DAMAGE
from PUBLIC.Public_Standards import *

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
        Attack_Core_Value = (Attacker.Total_Attribute(Main_Attribute)) * 6
            
        Total_Attack = (Attack_Special_Value + Attack_Core_Value)
            
        if Attacker_Distance == _ATTACK_DISTANCE.RANGED:
            Total_Attack = 2 + ((Total_Attack) * 0.75)
        
        Total_Attack *= (1 + Attacker.Total_Attribute(_ATTRIBUTE.DAMAGE)/100)
            
        Static_Damage = max(0, int(Total_Attack * 0.85))
        Random_Damage = random.randint(0, int((Total_Attack) * 0.30))
        return Static_Damage + Random_Damage
    
    @staticmethod
    def Basic_Attack(Attacker, Target):
        if COMBAT_DATA.Attack_Roll(Target):
            Total_Damage_Amount = COMBAT_DATA.Calculate_Damage(Attacker)
            
            if COMBAT_DATA.Critical_Roll(Attacker):
                Total_Damage_Amount = int(Total_Damage_Amount * Attacker.Total_Attribute(_ATTRIBUTE.CRITICAL_MULTIPLIER))
                
            Damage_taken = DAMAGE(Total_Damage_Amount, 
                                Attacker.Current_Attack_Type, 
                                Attacker)
            
            Damage_Taken_After_Resistances = Target.Take_Damage(Damage_taken)
            
            Vampirism = Attacker.Total_Attribute(_ATTRIBUTE.VAMPIRISM)
            Target_Thorns = Target.Total_Attribute(_ATTRIBUTE.THORNS)
            
            if Vampirism > 0:
                Attacker.Heal(int(Damage_Taken_After_Resistances * Vampirism/100))
            
            if Target_Thorns > 0:
                Attacker.Take_Damage(DAMAGE(Target_Thorns, Target.Thorns_Type, Target))
            
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
        return None

    def Team_Dead(self, Team) -> bool:
        return all(e.Actual_Health <= 0 for e in Team)
    
    def Get_Winner(self) -> _SIDE | None:
        if self.Team_Dead(self.Team_A): 
            return _SIDE.ENEMY
        if self.Team_Dead(self.Team_B): 
            return _SIDE.PLAYER
        return None

    def Clean_Dead(self):
        self.Team_A = [ e for e in self.Team_A if e.Actual_Health > 0 ]
        self.Team_B = [ e for e in self.Team_B if e.Actual_Health > 0 ]
        self.Entities = self.Team_A + self.Team_B

            
    @staticmethod
    def Combat_Between(Players, Enemies):
        Combat = COMBAT_SYSTEM(Players, Enemies)
        Combat_Running = True
        
        while Combat_Running:
            pass
