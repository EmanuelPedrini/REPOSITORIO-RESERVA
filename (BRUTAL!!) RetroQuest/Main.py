
import Globals
from Combat import combat
from Kimeras_Data import princesses, allkimeras
from Event_Generator import gerador_de_eventos
from THE_HOLE import THE_HOLE
from Tutorial import tutorial, full_name_with_nickname
from Kimeras_Data import actualize_princesses, actualize_queen
from Globals import looktheirteeths
from Globals import banned_from_twitter
# import SacrificeGoat

def run_expedition():
    actualize_princesses(allkimeras)
    actualize_queen(allkimeras)
    (print("Welcome to KIMERAHALLA! if want to go back to THE HOLE, type [EXIT]"))

    Globals.act = 1
    Globals.globaldanger = 0
    Globals.endofarun = False
    Globals.bosscall = "notcalled"

#kimeras
    def kimera_choice():
        while True:
            ()
            print("Choose your kimera!")
            for i, char in enumerate(princesses):
                print(f"[{i+1}] - { full_name_with_nickname(char) }")

     #escolha
            choice=input(">  ")

            if choice.isdigit():
                charpos=int(choice)-1
                if 0 <= charpos <len(princesses):
                    actonrun = princesses[charpos]
                    banned_from_twitter(actonrun)
                    return actonrun
                
            elif choice == "lookteeths" or choice == "lk":
                lookedteeths = input("Who you wanna see closely?")
                if lookedteeths.isdigit():
                    lkth=int(lookedteeths)-1
                    if 0<= lkth <len(princesses):
                        looktheirteeths(princesses[lkth])
                        continue
                continue

                
            elif choice == "EXIT":
                Globals.gamerunning = 2
                print("Welcome Back to THE HOLE!")
                return None

            else:
                print("Sorry, that's ins't a valid choice")
                continue

    player = kimera_choice()
    if player is None:
        return
    
    # pgterminal.current_player = player
    
    print(f"Congrats! You chosed {full_name_with_nickname(player)}!")
    player.acthp = player.total_max_hp

    # create_attributes_window(player)  # agora é o personagem do jogador

    filadeeventos=[]
    while len(filadeeventos) < 2:
        ()
        filadeeventos.append(gerador_de_eventos(player))

    while Globals.gamerunning==1:
        if Globals.endofarun == True:
            filadeeventos.clear()
            Globals.gamerunning = 2
            break
        
        if Globals.bosscall == "called":
            Globals.bosscall = "notcalled"

            filadeeventos.clear()
            filadeeventos.append(gerador_de_eventos(player))

        evento = filadeeventos.pop(0)  # pega o atual
        tipo, oqé = evento

        if tipo == 1:
            oqé.trigger(player)

        elif tipo == 2:
            combat(player, oqé)

        elif tipo == 3:
            oqé.trigger(player)

        elif tipo == 4:
            oqé.trigger(player)

        elif tipo == 123:
            oqé(player)

        elif tipo == 67:
            combat(player, oqé)

        filadeeventos.append(gerador_de_eventos(player))
    return 

def main_state():
    while True:
        state=Globals.gamerunning

        if state==0:
            tutorial()

        elif state==1:
            run_expedition()

        else:
            THE_HOLE()

main_state()