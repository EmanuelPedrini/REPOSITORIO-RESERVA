from PUBLIC.Public_Standards import *
from SYSTEMS.Character_Systems import Player_Attributes, Actualize_Kimeras
from SYSTEMS.Command_System import Loop_Input, Validate_Enumbered_Choice
from CLASSES.BASIC_ATTACK import Melee_Natural_Attack, Ranged_Natural_Attack, Melee_Spin_Attack
from DATA.TEST_FILE import Chainsaw_Head
from PUBLIC.Public_Enums import _GENDER, _ATTACK_DISTANCE, _DAMAGE_TYPE, _ATTRIBUTE, _TYPE_RESISTANCES, _SIDE, _HIERARCHY
from CLASSES.SKILLS import Fireball, Vampiric_Bite
from CLASSES.KIMERA import KIMERA

##TESTETESTE################################

Joana_Mata_Galinha = KIMERA("Joana Mata-Galinha", 
                            _GENDER.FEMALE,
                            6, 7, 2, 3, 1, 2,
                            [Fireball, Vampiric_Bite], [], [],
                            [Melee_Spin_Attack],
                            _HIERARCHY.COMMONER)

Joao_Mata_Galinha = KIMERA("João Mata-Galinha", 
                            _GENDER.MALE,
                            3, 3, 3, 1, 1, 2,
                            [], [], [], 
                            [Melee_Natural_Attack],
                            _HIERARCHY.COMMONER)

Mariazinha_Mata_Frango = KIMERA("Mariazinha Mata-Frango", 
                            _GENDER.FEMALE,
                            2, 10, 2, 2, 2, 2,
                            [Fireball, Vampiric_Bite], [], [], 
                            [Ranged_Natural_Attack],
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

class CHOICE_SYSTEM:
    def CHOOSING(Minimum,
                 Maximum,
                 Options, 
                Text):
        User_Choices = []
            
        print(Text)
        
        while True:
            
            print("CHOOSE!")
            print("[ comfirm ] - To finish the SELECTION!")
            for Order, Princess in enumerate(Options):
                print(f"[ {Order + 1} ] - { Princess.Name }")
                
            Kimera = input("> ")
            
            if Kimera.lower() in ("end", "finish", "ed", "en", "ok", "let", "go", "finished", "fn", "comfirm"):
                if len(User_Choices) >= Minimum:
                    return User_Choices
                print(f"Choose at least {Minimum} KIMERAS to CONTINUE!")
                
            elif Validate_Enumbered_Choice(Options, Kimera):
                
                Choosed_Kimera = int(Kimera) - 1
                Choosed = Options[Choosed_Kimera]
                
                #REMOVING FROM OPTIONS
                Kimera_Choice = Options.pop(Choosed_Kimera)
                
                if len(User_Choices) < Maximum:
                    User_Choices.append(Kimera_Choice)
                    
                else:
                    print(f"Who do you want to REMOVE to add '{Choosed.Name}'?")
                    for Order, Princess in enumerate(User_Choices): 
                        print(f"[ {Order + 1} ] - {Princess.Name}")
                
                    Kimera_Removed = input("> ")
                    
                    if Validate_Enumbered_Choice(User_Choices, Kimera_Removed):
                        Removed_One = User_Choices.pop(int(Kimera_Removed) - 1)
                        
                        if Removed_One:
                            Options.append(Removed_One)
                            User_Choices.append(Choosed)
            
                    else:
                        print("INVALID")
                        continue
                
                print("Your choices:")
                for i in User_Choices: print(f"-> {i.Name}")
                
            else:
                print("INVALID")
                continue
#TEAM SELECTION SYSTEM
@dataclass
class SELECTION_SYSTEM(CHOICE_SYSTEM):
    def TEAM_SELECTION():
        Player_Team = []
        Actualize_Kimeras(Player_Attributes["all_player_kimeras"])
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
            
#TUTORIAL
@dataclass
class TUTORIAL_SYSTEM(CHOICE_SYSTEM):
    def TUTORIAL():
        Random_Initial_Princesses = []
        Random_Initial_Queens = []
        for Number in range(1, 10): Random_Initial_Princesses.append(KIMERA.Generate_Random(_HIERARCHY.PRINCESS, 0))
        for Number in range(1, 6): Random_Initial_Queens.append(KIMERA.Generate_Random(_HIERARCHY.QUEEN, 244))
        Princeses_Choice = TUTORIAL_SYSTEM.CHOOSING(4, 4, Random_Initial_Princesses, "Choose your PRINCESSES!")
        Queen_Choice = TUTORIAL_SYSTEM.CHOOSING(1, 1, Random_Initial_Queens, "Choose your QUEEN!")
        Player_Attributes["player_princesses"].extend(Princeses_Choice)
        Player_Attributes["player_queen"].extend(Queen_Choice)

tuts = TUTORIAL_SYSTEM.TUTORIAL()