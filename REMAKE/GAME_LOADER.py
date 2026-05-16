from PUBLIC.Public_Standards import *

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
        case _GAME_STATE.SELECTION:
            SELECTION()
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
def SELECTION():
    pass