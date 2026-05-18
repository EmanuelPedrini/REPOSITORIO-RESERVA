from PUBLIC.Public_Enums import _HIERARCHY
Player_Attributes = {
    "all_player_kimeras": [],
    "player_kimeras_lobby": [],
    "player_kimeras_fit_breeding": [],
    "player_kimeras_available_breeding": [],
    "player_princesses": [],
    "player_queen": [],
    "player_team": [],
    
}

def Actualize_Kimeras():
    Player_Attributes["player_princesses"].clear()
    Player_Attributes["player_queen"].clear()
    for Kimera in Player_Attributes["all_player_kimeras"].copy():
        
        if Kimera.Hierarchy_Level == _HIERARCHY.PRINCESS:
            Player_Attributes["player_princesses"].append(Kimera)
            
        elif Kimera.Hierarchy_Level == _HIERARCHY.QUEEN:
            Player_Attributes["player_queen"].append(Kimera)
        

def Available_for_Breeding():
    Available = []
    for Kimera in Player_Attributes["all_player_kimeras"].copy():
        if Kimera.Age > 2 and not Kimera.Exhausted:
            Available.append(Kimera)
    return Available