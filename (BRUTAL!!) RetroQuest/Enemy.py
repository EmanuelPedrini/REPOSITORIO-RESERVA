import random
import Globals

from utils import rolld100
from Itens_Data import todososequipamentos
# from 
class enemy:
    def __init__(self, name, totalmaxhp, atk, vampirism, thorns, dodge, centsondeath, xpondeath, atkdist):

        self.name = name
        #hp
        self.base_totalmaxhp = totalmaxhp
        self.base_atk = atk
        self.dodge = dodge
        self.base_centsondeath = centsondeath
        self.base_xpondeath = xpondeath


        self.totalmaxhp = int(totalmaxhp * Globals.globaldangercalc)
        self.acthp = self.totalmaxhp
        self.atk = int(atk * Globals.globaldangercalc)
        self.centsondeath = int(centsondeath // Globals.globaldangercalc)
        self.xpondeath = int(xpondeath // Globals.globaldangercalc)


        #secondary atributes
        self.vampirism = vampirism
        self.realvampirism = float(vampirism*0.01)
        self.thorns = thorns

        self.atkdist = atkdist

        #debuffs
        self.fire_amount = 0
        self.bleeding_amount = 0

        self.leech_amount = 0
        self.mana_leech_amount = 0

        self.bruise_amount = 0

        self.stunned = False
        self.cursed = False
        self.blind = False
        self.charmed = False
        self.weakness = False

        #self.dead=False
    #Ancora 3
    def apply_danger(self):
        scale = Globals.globaldangercalc
        self.totalmaxhp = int(self.base_totalmaxhp * scale)
        self.acthp = self.totalmaxhp
        self.atk = int(self.base_atk * scale)
        self.centsondeath = int(self.base_centsondeath / scale)
        self.xpondeath = int(self.base_xpondeath / scale)

    def toma(self, damage, player):
        if self.cursed:
            taked_damage = damage * Globals.cursemultiplier

        elif self.weakness:
            taked_damage = int(damage * 1.5)
            
        else:
            taked_damage = damage

        self.acthp -= taked_damage
        self.death(player)

    def heal(self, amount):
        self.acthp += amount
        if self.acthp > self.totalmaxhp:
            self.acthp = self.totalmaxhp
        print(f"> the enemy {self.name} healed [ {amount} ] Hp")

    def attack(self, player):
        roll= rolld100()
        if roll > player.total_dodge:
            damage =  self.atk

            damage = max(1, round(damage * (1 - Globals.reds(player))))

            if self.vampirism != 0:
                self.heal(int(damage*(self.realvampirism)))
            
            if player.thorns != 0 and self.atkdist == "m":
                tomado = player.thorns
                self.toma(tomado, player)
                print(f"The {self.name} taked {tomado} damage from your thorns!")

            print(f"{self.name} hit the {player.name} dealing {damage} damage!")
            player.toma(damage)
        else:
             print(f"{self.name} missed a attack against the {player.name}!")
    

    def death(self, player):
        if self.acthp <= 0:
            centsg = int(random.randint(self.centsondeath, self.centsondeath * 3))
            xpg = int(random.randint(self.xpondeath, self.xpondeath * 3))
            randomitemgain = random.randint(1, 100) + player.total_luck
            if randomitemgain < 75:
                maxitemgain=1
            else:
                maxitemgain=2  
            maxitemgain = min(maxitemgain, len(todososequipamentos))

            itemg = random.sample(todososequipamentos, maxitemgain)

            if self.name == "Wild Kimera":
                print(f"the {self.name} got KNOCKED OUT!")
                from Kimera import kimera
                rdkm = kimera.randomkimera("Bone Eater", Globals.globaldanger)
                rdkm.age+=3
                Globals.gained_kimeras_battle.append(rdkm)
            else:
                print(f"the {self.name} died!")

            Globals.gained_cents_battle+=centsg
            Globals.gained_xp_battle +=xpg
            if itemg:
                for it in itemg:
                    Globals.gained_itens_battle.append(it)

    @classmethod
    def fusion(cls, fus1, fus2):

        nam1 = fus1.name[: len(fus1.name)//2 ]
        nam2 = fus2.name[ len(fus2.name)//2: ]
        fusioname = (nam1 + nam2)

        def fusst(st1, st2):
            fusstt = ((st1 + st2)//2) * 1.7
            return int(fusstt)
        
        rdatkdist = random.choice([fus1.atkdist + fus2.atkdist])
        
        return cls(fusioname, fusst(fus1.totalmaxhp, fus2.totalmaxhp), fusst(fus1.atk, fus2.atk),
                   fusst(fus1.vampirism, fus2.vampirism), fusst(fus1.thorns, fus2.thorns), 
                   fusst(fus1.dodge, fus2.dodge), 
                   fusst(fus1.centsondeath, fus2.centsondeath), fusst(fus1.xpondeath, fus2.xpondeath),
                   rdatkdist)
    @classmethod
    def wildquimera(cls):
        rddat = random.choice(["m", "r"])
        return cls( "Wild Kimera", 
                   (random.randint(4, 8)*5), 
                   (random.randint(4, 8)),
                   (random.randint(0, 15)), 
                   (random.randint(0, 5)), 
                   (random.randint(0, 20)),
                   (random.randint(12,25)), 
                   (random.randint(20, 40)), 
                   rddat
        )
            # else:
                # Globals.gained_itens_battle.append(itemg)


            
        #     return True
        # return False
