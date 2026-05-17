# from PUBLIC.Public_Standards import *
import random
def Keyboard_Smash_Generator():
    Characters: list = ["%","0","&","#","@","!","?","4","$",
                        "7","9","+","{", "*", "-","_","=","[","]"]
    Final_Name = []
    for Char in range(random.randint(6, 16)):
          Final_Name.append(random.choice(Characters))
    return "".join(Final_Name)

def Generate_Random_Kimera_Name():
    First_Names = ["Bippy","Schiza","Bruttalia","Mary","Doroti",
                   "Mel-Mel","Mei-Mei","Lilim", "Lilith","Sausage",
                   "Chainsaw", "Shorty", "Squeezy", "Lettuce", "Zombbye",
                   "Soggy","Mama","Skinny", "Baloon","Cheeks","Pancake",
                   "Belly", "Goofy","Bubble", "Pancake", "Nail", 
                   "HotDog", "Noodles", "Funny","Miss", "Stupid",
                   "Sweetis", "Puffy", "Spaghetti","Sniffy", "Stinky", "Winky",
                   "Dizzy","Tiny", "Peebles", "Feet Fungus", "Tummy", "Fluffy", 
                   "Kimera"]
    
    Last_Names = [" Genocide", " Intestines", " Power Drill", " Bafemoth", 
                  " ThunderBones", " Head Beater", " Goat"," Uglyas'fuk",
                  " Fish Eater", " Dog Eater", " Woodpecker"," Crocodile", "Gpt",
                  " MixTape"," Hades", " Rimworld"," Isaac"," Hero"," ZERO", ("-"+ str(random.randint(1, 1000))),
                  "?!", " Meat Grinder", " Hamster Eater", "Bad Kidney", "Soup Criminal",
                  " Nuclear Baby"," Nuclear Waster"," Uranium"," Tax Evasion"," Floor Licker",
                  " Door Kicker"," Knee Biter"," Teeth Eater",", The Big"," Mama Killer",
                  "Papa Killer", ".exe"]
    
    Rare_Names = ["Osama Billaden", "Mc Sapato", "Donald NotDuck", "Karen", 
                  "Milton", "Tangananica", "Tangananá", "Bogart", "Samural",
                  "Napoleon Bonapita","Jhon Bimba","Elon Mustache","Saddam Hussem","Spongebob Squeezy-Pants",
                  "Shrek","Baby Eater"]
    
    Rare_Name_Chance = random.randint(1, 100)
    
    if Rare_Name_Chance <= 96: 
        Final_Name = "".join(random.choice(First_Names) + random.choice(Last_Names))
        
    elif Rare_Name_Chance <= 99:
        Final_Name = random.choice(Rare_Names)
        
    else:
        Final_Name = Keyboard_Smash_Generator()
        
    return Final_Name