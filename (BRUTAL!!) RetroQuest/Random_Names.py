import random
from utils import rolld100
def generate_a_random_name():
    silabasnomeprincipal = ["ki", "me", "ra", "em", "ik", "mi", "zu", "ly"]
    nome = []
    for i in range(random.randint(2, 3)):
        nome.append(random.choice(silabasnomeprincipal))

    nomefinal = ("".join(nome).capitalize())

    return (nomefinal)

def generate_a_random_surname():
    listadesobrenomes=["Bafemoth", "Teeths", "Intestines", "Smash", "Power Drill", "Bubble","Samural", "Goofy Butt", "Dog Tongues", "ThunderBones", "StupdAs'fuk"]
    num = rolld100()
    if num <= 75:
        adicional = ""

    elif 75 < num < 92:
        adicional = "Dom "

    else:
        adicional = "Mc"

    sobrenome = f"{adicional}{random.choice(listadesobrenomes)}"

    return sobrenome

def generate_a_random_nickname():
    listadeapelidos=['"Blow"','"Small Head"', '"Hammer Head"', '"Nail"', '"Hand Finger"', '"Sausage Fingers"', '"Hot Dog"',
                      '"Chocolate Starfish"', '"Big Head"', '"Drill"', '"Chainsaw Head"', '"Dog Food"', '"Mama"', '"Airhead"', 
                      '"Pancake Head"', '"Goblin Nose"', '"Goofy Belly"', '"MC BigBelly"', '"Skinny"','"Noodle Arms"','"Baloon Cheeks"', 
                      '"Soggy Feet"']
    nickname=random.choice(listadeapelidos)
    return nickname

def generate_a_full_name():
    fullname = (f"{generate_a_random_name()} {generate_a_random_nickname()} {generate_a_random_surname()}")
    return fullname