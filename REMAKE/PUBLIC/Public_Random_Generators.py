# from PUBLIC.Public_Standards import *
import random
def Keyboard_Smash_Generator():
    Characters: list = ["%","0","&","#","@","!","?","4","$","7","9","+","{"]
    Final_Name = []
    for Char in range(random.randint(6, 16)):
          Final_Name.append(random.choice(Characters))
    return "".join(Final_Name)

print(Keyboard_Smash_Generator())