from SYSTEMS.Command_System import Loop_Input
from PUBLIC.Public_Standards import *

class EVENT:
    def __init__(self, 
                 Name: str, 
                 Text: str, 
                 Choices: list):
        self.Name = Name
        self.Text = Text
        self.Choices = Choices

    def Trigger(self, player):
        while True:
            print(f"EVENT: {self.Name}")
            print(self.Text)

            for Order, (Choice_Text, _) in enumerate(self.Choices, 1):
                print(f"{Order} - {Choice_Text}")

            Choice = Loop_Input(player)
            
            if Choice.isdigit():                    
                    Choice = int(Choice)-1
                    if 0 <= Choice < (len(self.Choices)):
                         _, Effect = self.Choices[Choice]
                         Effect(player)
                         break
                    print("INVALID")
            print("INVALID")