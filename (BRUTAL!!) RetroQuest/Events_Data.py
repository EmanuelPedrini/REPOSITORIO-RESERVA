from Event import event
import random
from Globals import *
from Combat import combat
from Enemies_Data import marshmallowknight
import copy
#eventos neutros

def nothing(player):
    print("Nothing happens.")

def avoid(player):
    roll= random.randint(1,20) + player.total_dex
    if roll < 12:
        dmg=random.randint(4,7)*globaldangermathsoftcap
        player.toma(int(dmg))
        print(f"You accidentaly stepped on the trap and taked {int(dmg)} damage!")
    else:
        print("You avoided the trap in a involuntary reflex!")

def drinkfountain(player):
    roll= random.randint(1,20) + player.total_luck
    if roll > 7:
        hl= random.randint(6,10)*globaldangermathsoftcap
        player.heal(int(hl))
        print(f"The water have a taste of marshmallows and honey, you fell your body get refilled with jovial energy!")
    elif roll<=7:
        print("A marshmallow knight appears from the bushes before you can drink from the fountain, ainda starts a combat!")
        actenemy=[ copy.deepcopy(marshmallowknight) ]
        combat(player, actenemy)

def pactop1(player):
    player.lose_atr("bonus_hp", 5)
    player.gain_atr("gained_strg", 2)
    print("Ok, Sup kid.")

def pactop2(player):
    player.lose_atr("bonus_hp", 5)
    player.gain_atr("gained_intel", 2)
    print("Ok, Sup kid.")

def pactop3(player):
    player.lose_atr("bonus_hp", 5)
    player.gain_atr("gained_luck", 2)
    print("Ok, Sup kid.")

def pactop4(player):
    player.lose_atr("bonus_hp", 5)
    player.gain_atr("vampirism", 5)
    print("Ok, Sup kid.")

def ignore(player):
    print("You ignore.")

pedrasnocaminho=event("Stones in the path", "You encounter different rocks in the path and you decide to take a look",
    [
    ("Look under the rocks", nothing)
    ]
)

neutralevents=[pedrasnocaminho]

#eventos ruins
pisadaemarmadilha=event(
    "Pisada na armadilha", "In a moment of distraction, you look to the black skies of decandent world and comtemplate your existence, as you" \
    "return to reality, you realize that your feet is going on the direction of a BEAR TRAP!",
    [
        ("Avoid!", avoid)
    ]
)

pactocomdiabo=event(
    "Pact with the Devil", "The Devil appears in you front, and he says:\n (The Devil) - I offer you a pact, creature!",
    [
    ("+2 Stregth / -5 Max HP", pactop1),
    ("+2 Intelligence / -5 Max HP", pactop2),
    ("+2 Luck / -5 Max HP", pactop3),
    ("+5% Vampirism / -5 Max HP", pactop4),
    ("Ignore the Devil Pact", ignore)
    ]
)

badevents=[pisadaemarmadilha, pactocomdiabo]

#eventos bons
fontedecura = event(
    "Fonte de Cura", "You found a imposing fountain with healing magic simbols, Drink?",
    [
        ("Ignore", nothing),
        ("Drink", drinkfountain)
    ]
)

goodevents=[fontedecura]

#adicionar no futuro
# ultraevents=[]