from PUBLIC.Public_Enums import _HIERARCHY
Player_Attributes = {
    "all_player_kimeras": [],
    "player_kimeras_lobby": [],
    "player_kimeras_fit_breeding": [],
    "player_kimeras_available_breeding": [],
    "player_princesses": [],
    "player_queen": [],
    "player_team": [],
    "player_vars": {},
}

def Actualize_Kimeras():
    Player_Attributes["player_princesses"].clear()
    Player_Attributes["player_queen"].clear()
    for Kimera in Player_Attributes["all_player_kimeras"].copy():
        
        if Kimera.Hierarchy_Level == _HIERARCHY.PRINCESS:
            Player_Attributes["player_princesses"].append(Kimera)
            
        elif Kimera.Hierarchy_Level == _HIERARCHY.QUEEN:
            Player_Attributes["player_queen"].append(Kimera)
        

def Actualize_fit_for_Breeding():
    Player_Attributes["player_kimeras_fit_breeding"].clear()
    
    for Kimera in Player_Attributes["all_player_kimeras"].copy():
        
        if Kimera.Age > 20:
            Player_Attributes["player_kimeras_fit_breeding"].append(Kimera)

def Actualize_Available_for_Breed():
    Player_Attributes["player_kimeras_available_breeding"].clear()
    
    for Kimera in Player_Attributes["all_player_kimeras"].copy():
        
        if not Kimera.Exhausted:
            Player_Attributes["player_kimeras_available_breeding"].append(Kimera)
    