import Globals
from Kimera import kimera
from THE_HOLE import full_name_with_nickname, lookingsmaching
from Kimeras_Data import allkimeras
from Globals import looktheirteeths

listatmp =[]
for i in range(3):
    kimimpossible = kimera.randomkimera("Queen")
    listatmp.append(kimimpossible)

listasuitors = []
for i in range(5):
    kimimpossible02 = kimera.randomkimera("Princess")
    listasuitors.append(kimimpossible02)

def big_ass_choice(lista):
    while True:
        ()
        print("Your options:")
        for number, kimerainlist  in enumerate(lista):
             print((f"[{number+1}] - {full_name_with_nickname(kimerainlist)} ( SCORE: {lookingsmaching(kimerainlist)} )"))
        bixachoice = input("")
        if bixachoice.isdigit():
            sex_kimera = int(bixachoice) - 1
            if 0<= sex_kimera < len(lista):
                 bixaescolhida = lista[sex_kimera]
                 return bixaescolhida
            else:
                print("WHY ARE POINTING TO THE WALL?!")

        elif bixachoice == "lookteeths" or bixachoice=="lk":
            examchoice = input("Which one you want to see more closely?")
            if examchoice.isdigit():
                ex_kimera = int(examchoice) - 1
                if 0<= ex_kimera < len(lista):
                     bixaalisada = lista[ex_kimera]
                     looktheirteeths(bixaalisada)
            else:
                print("SAY A NUMBER BRO!")
        else:
            print("WHY ARE POINTING TO THE WALL?!")
            
def choice():
    print("Choice you MATRIARCH (Your first QUEEN)")
    escolhida = big_ass_choice(listatmp)
    escolhida.age += 3
    allkimeras.append(escolhida)

    print(f"You choose {full_name_with_nickname(escolhida)}")
    print("\033c", end="")
    print("OK, now choose some Princess!\n")

    escolhido01 = big_ass_choice(listasuitors)
    escolhido01.age += 3
    allkimeras.append(escolhido01)
    print(f"You choose {full_name_with_nickname(escolhido01)}")
    print("\033c", end="")
    print("OK, NOW choose another princess!\n")

    rest=[]
    for k in listasuitors:
        if k != escolhido01:
             rest.append(k)

    escolhido02 = big_ass_choice(rest)
    escolhido02.age += 3
    allkimeras.append(escolhido02)
    print(f"You choose {full_name_with_nickname(escolhido02)}")
    print("\033c", end="")
    print("")

    print("GOOD LUCK! BYE BYE")
    Globals.gamerunning = 1
def Choose_Language():
    Language_List = ["Português", "English"]
    while True:
        print("Choose your language:")
        for number, language  in enumerate(Language_List):
             print(f"[{number+1}] - {language}")
        Ch = input("> ")
        if Ch.isdigit():
            Ch_Lang = int(Ch) - 1
            if 0<= Ch_Lang < len(Language_List):
                 Chosed_Language = Language_List[Ch_Lang]
                 print(Chosed_Language)
                 return Chosed_Language
def tutorial():
    # Globals.Language = Choose_Language()
    print("Hello! I see it's your first time, playing so i need to teach you how things work here")
    print("First of all you gonna need a MATRIARCH for your KIMERA family!")
    print("Uh WHAT???!!!")
    print("YOU DON'T KNOW WHAT IS A KIMERA??!!")
    print("OH MAN!")
    print("WHAT KIDS LEARN THESE DAYS ON SCHOOL??!!")
    print("But ok... How can i describe what is a kimera?")
    print("Kimeras are like the NEW GENETIC INVENTION OF THE CENTURY!!")
    print("They are like tiny humanoid with animal features, THEY CAN COME IN EVERY FORM! or ANY SHAPE!")
    print("You can STRETCH and SMASH THEM!")
    print("AND THEY STILL ALIVE!")
    print("So kimeras have a very restrictive HIERARCHY.")
    print("You have 3 kimera status in a colony, QUEENS, PRINCESSES AND BONE EATERS.")
    print("BONE EATERS are the lowest rank in a colony, they serve only to reproduce between them and create new PRINCESSES")
    print("Only the QUEEN can give birth to new PRINCESSES")
    print("And only the PRINCESSES, can go in expeditions!")
    print("Yeah, you can send them in expeditions to collect things for you")
    print("Very convinient, RIGHT?")
    print("So in a act of of kindness, i'll give you some of my kimeras")


    choice()



                 

