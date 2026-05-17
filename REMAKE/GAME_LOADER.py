from PUBLIC.Public_Standards import *
from SYSTEMS.Character_Systems import Actualize_Princesses, Actualize_Available_for_Breeding, Actualize_Queen, Refresh, Player_Attributes
from SYSTEMS.Command_System import Loop_Input, Validate_Enumbered_Choice
from CLASSES.BASIC_ATTACK import Melee_Natural_Attack
from DATA.TEST_FILE import Chainsaw_Head
from PUBLIC.Public_Enums import _GENDER, _ATTACK_DISTANCE, _DAMAGE_TYPE, _ATTRIBUTE, _TYPE_RESISTANCES, _SIDE, _HIERARCHY
from CLASSES.SKILLS import Fireball, Vampiric_Bite
from CLASSES.KIMERA import KIMERA

##TESTETESTE################################

Joana_Mata_Galinha = KIMERA("Joana Mata-Galinha", 
                            _GENDER.FEMALE,
                            6, 7, 2, 3, 1, 2,
                            [Fireball, Vampiric_Bite], [], [],
                            Melee_Natural_Attack,
                            _HIERARCHY.COMMONER)

Joao_Mata_Galinha = KIMERA("João Mata-Galinha", 
                            _GENDER.MALE,
                            3, 3, 3, 1, 1, 2,
                            [], [], [], 
                            Melee_Natural_Attack,
                            _HIERARCHY.COMMONER)

Mariazinha_Mata_Frango = KIMERA("Mariazinha Mata-Frango", 
                            _GENDER.FEMALE,
                            2, 10, 2, 2, 2, 2,
                            [Fireball, Vampiric_Bite], [], [], 
                            Melee_Natural_Attack,
                            _HIERARCHY.COMMONER)







############################################
class _GAME_STATE(Enum):
    EXPEDITION = 0
    MENU = 1
    LOBBY = 2
    TUTORIAL = 3
    SELECTION = 4
    
def GAME_MAIN_STATE(GAME_STATE: _GAME_STATE):
    match GAME_STATE:
        case _GAME_STATE.EXPEDITION:
            EXPEDITION()
        case _GAME_STATE.MENU:
            MENU()
        case _GAME_STATE.LOBBY:
            LOBBY()
        case _GAME_STATE.TUTORIAL:
            TUTORIAL
        # case _GAME_STATE.SELECTION:
            # SELECTION()
        case _:
            raise "GAME STATE ERROR!!!!"


def EXPEDITION():
    pass 
def MENU():
    pass
def LOBBY():
    pass
def TUTORIAL():
    pass

#TEAM SELECTION SYSTEM
@dataclass
class SELECTION_SYSTEM:
    def TEAM_SELECTION():
        Player_Team = []
        Refresh(Player_Attributes["all_player_kimeras"])
        (print("SELECT YOUR FIGHTERS!!\nIf you want to go back to LOBBY, type [ EXIT ]"))
        Elegible_Princess = Player_Attributes["player_princesses"].copy()
        while True:
            print("Choose your kimera!")
            for Order, Princess in enumerate(Elegible_Princess):
                print(f"[ {Order + 1} ] - { Princess.Name }")
            Kimera = input("> ")
            if Validate_Enumbered_Choice(Elegible_Princess, Kimera):
                Player_Team.append(Elegible_Princess[int(Kimera)])
            else:
                print("INVALID")
                continue

selec = SELECTION_SYSTEM.TEAM_SELECTION()

#TUTORIAL
@dataclass
class TUTORIAL_SYSTEM:
    def TUTORIAL():
        Player_Choices = []
        Random_Queens = None
        Random_Princesses = None
        (print("SELECT YOUR FIGHTERS!!\nIf you want to go back to LOBBY, type [ EXIT ]"))
        while True:
            for Order, Princess in enumerate(Random_Princesses):
                print(f"[ {Order + 1} ] - { Princess.Name }")
                
            Kimera = input("> ")
            
            if Validate_Enumbered_Choice(Random_Princesses, Kimera):
                Player_Choices.append(Random_Princesses[int(Kimera)])
            else:
                print("INVALID")
                continue