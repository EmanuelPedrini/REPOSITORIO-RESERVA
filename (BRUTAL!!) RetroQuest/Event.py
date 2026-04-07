from Commands import input_player
import Globals
class event:
    def __init__(self, name, text, choices):
        self.name=name
        self.text=text
        self.choices=choices

    def trigger(self, player):
        #apresentação do evento
        print(f"EVENT: {self.name}")
        print(self.text)
        
        for i, (optiontext, _) in enumerate(self.choices,1):
             print(f"{i} - {optiontext}")
        while Globals.gamerunning==1:
            ()
            choice = input_player(player)
            if not isinstance(choice, str):
                return
            if choice.isdigit():
                    
                    choice= int(choice)-1

                    if 0<= choice < (len(self.choices)):
                         
                         _, effect =self.choices[choice]

                         effect(player)

                         break
                    
            print("Invalid Option")