import random
from utils import rolld100
import sys
from Passive_Data import todasaspassivas
from Skill_Data import todasskills
from Atribute_Rewards_Data import todososgatr
from Commands import input_player
# from ColorText import *
import Globals
from Random_Names import generate_a_random_name, generate_a_random_nickname, generate_a_random_surname
from Mutation import allthemuts

class kimera:
    def __init__(self, name, surname, nickname, pronoun, possessive, 
                 strg, dex, vit, luck, cha, intel, 
                 dodge, 
                 vampirism, 
                 thorns, 
                 armor,
                 atkform, 
                 skills, 
                 passives,
                 mutations,
                 bonus_to_right,
                 bonus_to_left,
                 shieldstat = 0,  
                 status="Bone Eater"):
        
        #COISAS REVELANTES SÓ PARA A ESCRITA
        #NOME
        self.name = name
        self.surname = surname
        self.nickname = nickname

        #PRONOME (SHE / HE)
        self.pronoun = pronoun

        #PRONOME POSSESSIVO (HER / HIS)
        self.possessive = possessive

        #ONLY RELEVANT FOR BREEDING
        self.exhausted = False
        
        #TRIBUTOS BASE(SOMENTE COM BASE NA GENÉTICA)
        self.base_strg=strg
        self.base_dex=dex
        self.base_vit=vit
        self.base_luck=luck
        self.base_cha=cha
        self.base_intel=intel

        #TRIBUTOS SEM BONUS
        self.gained_strg=0
        self.gained_dex=0
        self.gained_vit=0
        self.gained_luck=0
        self.gained_cha=0
        self.gained_intel=0

        #TRIBUTOS BONUS
        self.bonus_strg = 0
        self.bonus_dex = 0
        self.bonus_vit = 0
        self.bonus_luck = 0
        self.bonus_cha = 0
        self.bonus_intel = 0

        #OUTROS
        self.bonus_mana_regen = 0
        self.bonus_mana_inicial = 0
        self.bonus_hp = 0
        self.dodge = dodge
        self.vampirism = vampirism
        self.thorns = thorns
        self.armor = armor
        self.shieldstat = shieldstat
        self.bonus_crit_chance = 0

        self.magicdmgbonus = 0
        self.temporary_magicdmgbonus = 0

        self.atkdmgbonus = 0
        self.temporary_atkdmgbonus = 0

        self.critmult = 2
        self.shield = 0

        self.skillcostmodifier = 0
        self.temporary_skillcostmodifier = 0
        
        self.atkform = atkform

        self.status = status

        self.age = 1

        #ACT
        self.actmana = 0
        self.acthp = 0

        #EXPERIÊNCIA
        self.level = 1
        self.xp = 0
        self.xptonext = 100
        
        #inventory system
        #inventario é so uma big lista anota ai
        self.inventory =[]

        self.stunned = False

        self.right_hand = True
        self.left_hand = True

        self.mainhand = random.choice(["Left Hand", "Right Hand"])
        if self.mainhand == "Left Hand":
            self.handpoints = -5
        else:
            self.handpoints = +5

        self.base_bonus_to_right = bonus_to_right
        self.base_bonus_to_left = bonus_to_left
        
        self.gained_bonus_to_right = 0
        self.gained_bonus_to_left = 0

        self.temporary_bonus_to_right = 0
        self.temporary_bonus_to_left = 0

        self.equipments = {
            "Weapon": None,
            "Armor": None,
            "Accessory": None
        }

        #skills pqp
        self.skills= list(skills)
        self.passives = list(passives)
        self.mutations = list(mutations)
        self.maxskills = 4
        self.maxpassives = 2
    
    #TOTAIS
    #TOTAL STRENGTH

    @property
    def total_atkdmgbonus(self):
        return self.atkdmgbonus + self.temporary_atkdmgbonus

    @property
    def total_bonus_to_right(self):
        return self.base_bonus_to_right + self.gained_bonus_to_right + self.temporary_bonus_to_right
    
    @property
    def total_bonus_to_left(self):
        return self.base_bonus_to_left + self.gained_bonus_to_left + self.temporary_bonus_to_left

    @property
    def total_strg(self):
        return self.base_strg + self.gained_strg + self.bonus_strg
    
    #TOTAL DEXTERITY
    @property
    def total_dex(self):
        return self.base_dex + self.gained_dex + self.bonus_dex
    
    #TOTAL VITALITY
    @property    
    def total_vit(self):
        return self.base_vit + self.gained_vit + self.bonus_vit
    
    #TOTAL LUCK
    @property    
    def total_luck(self):
        return self.base_luck + self.gained_luck + self.bonus_luck
    
    #TOTAL CHARISMA
    @property    
    def total_cha(self):
        return self.base_cha + self.gained_cha + self.bonus_cha
    
    #TOTAL INTELLIGENCE
    @property    
    def total_intel(self):
        return self.base_intel + self.gained_intel + self.bonus_intel
       
    #MAX HEALTH POINTS
    @property
    def max_hp(self):
        return (self.total_vit * 5)
    
    #TOTAL HEALTH POINTS
    @property
    def total_max_hp(self):
        t = max(1, (self.max_hp + self.bonus_hp))
        if self.acthp > t:
            self.acthp = t
        return t
    
    #MAX_MANA
    @property
    def max_mana(self):
        return self.total_cha * 5
    
    #MANA REGEN
    @property
    def mana_regen(self):
        return self.total_intel + self.bonus_mana_regen
    
    #MANA INICIAL
    @property
    def mana_inicial(self):
        return self.total_cha + self.bonus_mana_inicial
    
    @property
    def real_vampirism(self):
        return float(self.vampirism * (0.01))
    
    @property
    def total_dodge(self):
        return (4 * self.total_dex) + self.dodge
    
    @property
    def total_crit_chance(self):
        return (4 * self.total_luck) + self.bonus_crit_chance

    def gain_atr(self, attr, amount):
        setattr(self, attr, getattr(self, attr) + amount)

    def lose_atr(self, attr, amount):
        setattr(self, attr, getattr(self, attr) - amount)

    def add_item(self, item):
            self.inventory.append(item)
            print(f"> You obtained {item.name}!")

    def remove_item(self, item):
            if item in self.inventory:
                self.inventory.remove(item)
                print(f"> {item.name} got removed from your inventory!")
            else:
                print("> That item isn`t in your inventory")

    def itemequipped(self, item):
        for atrr, value in item.bonus.items():
            if hasattr(self, atrr):
                self.gain_atr(atrr, value)
            if item.slot=="Weapon":
                self.atkform=item.atkform

    def itemunequipped(self,item):
        for atrr, value in item.bonus.items():
            if hasattr(self, atrr):
                self.gain_atr(atrr, -value)
                
            if item.slot=="Weapon":
                self.atkform = "melee"

    def itemremove(self, slot):
        retirado2=self.equipments.get(slot)
        if retirado2 is not None:
            retirado2 = self.equipments[slot]
            self.itemunequipped(retirado2)
            self.inventory.append(retirado2)
            self.equipments[slot]=None
            print(f"> You unequipped [ {retirado2.name} ]!")
        else:
            print("No items equipped!")

    def equip(self,item):
        #so muda slot pra slot do item em questão
        slot = item.slot

        #removendo item se ja tem algo equipado
        if self.equipments[slot] is not None:
            retirado = self.equipments[slot]
            self.itemunequipped(retirado)
            self.inventory.append(retirado)
            print(f"> You unequipped [ {retirado.name} ]!")

        self.equipments[slot] = item
        if item in self.inventory:
            self.inventory.remove(item)
            print(f"> Equipped {item.name}")
        #
        self.itemequipped(item)

    def gain_shield(self, amount):
            self.shield += amount
            print(f"You gained {amount} Shield Points!")

        #regenerar mana
    def regen_mana(self):
        mnamt= self.mana_regen
        self.actmana += mnamt
        print(f"{self.name} regenerated {mnamt} Mana Points!")
        #Máximo de MANA
        if self.actmana > self.max_mana:
            self.actmana = self.max_mana

        #ganhar mana != regenerar mana
    def gain_mana(self, amount):
        self.actmana += amount
        if self.actmana > self.max_mana:
            self.actmana = self.max_mana
        print(f"{self.name} obtained {amount} Mana Points! \nNow {self.pronoun} have [ {self.actmana} / {self.max_mana} ] Mana Points")

    def mana_use(self, amountused):
        self.max_mana
        if self.actmana >= amountused:
            print(f"You actually have [ {self.actmana} / {self.max_mana} ] Mana Points! This is enough to cast this Ability!")

            self.actmana -= amountused
            print(f"Now you have [ {self.actmana} / {self.max_mana} ] Mana Points!")

    def choose_attack_hand(self):
        hand_choser = (random.randint(1, 100) + self.handpoints)
        if hand_choser >= 50 and self.right_hand: 
            return "Right Hand"
        elif self.left_hand:
            return "Left Hand"
        elif self.right_hand:
            return "Right Hand"
        else:
            return "Head"

           
        
    #BASIC ATTACK
    def basicattack(self, target, player):
            #rola o Dado
            roll = rolld100()
            rollcrit = rolld100()

            if roll > target.dodge:

                turnhand = self.choose_attack_hand()
                if turnhand == "Left Hand":
                    hand_bonus = self.total_bonus_to_left
                    for p in player.passives:
                          if p.trigger=="on_left_hit":
                             p.passiveactivationtrigger(self,damage)

                elif turnhand == "Right Hand":
                    hand_bonus = self.total_bonus_to_right
                    for p in player.passives:
                            if p.trigger=="on_right_hit":
                                p.passiveactivationtrigger(self,damage)
                else:
                    hand_bonus = 0

                #Computa o Dano
                basedmg = max(1, self.total_strg * 0.75) + hand_bonus
                randdmg = random.randint(0, int(self.total_strg * 0.5))

                damage = int(basedmg + randdmg) + self.total_atkdmgbonus
                crit = False
                if rollcrit < self.total_crit_chance:
                    damage *= self.critmult
                    crit = True
                
                if crit==True:
                    print(f"> {self.name} got A BRUTAL HIT!! Dealing [ {damage} ] MASSIVE DAMAGE using the {turnhand} to {target.name}")

                else:
                    print(f"> {self.name} HIT! Dealing [ {damage} ] DAMAGE using the {turnhand} to {target.name}")

                #Computa o tanto que tu curo com o ataque
                if self.vampirism != 0:
                    self.heal(max(1, int ( damage * (self.real_vampirism) ) ) )
                
                #Computa se o alvo tem Thorns
                if target.thorns != 0 and self.atkform=="melee":
                    Espinhado= int(target.thorns)
                    player.toma(int(Espinhado))
                    print(f"> You taked [ {Espinhado} ] damage from the enemy thorns!")
                
                for p in player.passives:
                    if p.trigger=="on_hit":
                        p.passiveactivationtrigger(self, damage)
                
                target.toma(damage, player)

                # if target.
                if target.acthp <= 0:
                    return
            else:
                print(f"You missed {target.name}, you rolled [ {roll} ] !")

    def toma(self, damage):
        if damage > self.shield:
            self.acthp -= (damage - self.shield)
            self.shield = 0
            self.acthp = max(0, self.acthp)
        else:
            self.shield -= damage
            

        for p in self.passives:
            if p.trigger=="on_damage":
                p.passiveactivationtrigger(self)
        self.death()

    def heal(self, amount):
        self.acthp += amount
        print(f"> {self.name} healed [ {amount} ] Hp")
        if self.acthp > self.total_max_hp:
            self.acthp = self.total_max_hp
            for pas in self.passives:
                if pas.trigger=="on_heal":
                    pas.passiveactivationtrigger(self)
    
    def gain_xp(self, xpamount):
        self.xp+=xpamount
        print(f"> {self.name} gained {xpamount} xp!")

    def gain_cents(self, amount):
        Globals.runcents += amount
        print(f"> {self.name} gained {amount} cents!")

    def lose_cents(self, amount):
        Globals.runcents -=amount
        print(f"> {amount} cents got away from your wallet!")

    def level_system(self):
        if self.xp>=self.xptonext:
            self.xp -= self.xptonext
            self.level +=1
            print(f"> The {self.name}  leveled up! Now {self.pronoun} is level {self.level}!")
            self.level_up_rewards()
            self.xptonext = int(100 * (1.5 ** (self.level - 1)))
    
    def level_up_rewards(self):
        totaloptions=[]
        totaloptions += random.sample(todososgatr, min(4, len(todososgatr)))

        #definindo se tu pode receber passivas
        if len(self.passives) < self.maxpassives:
            totaloptions += random.sample(todasaspassivas, min (4, len(todasaspassivas)))

        #mema traquera mas comm skills
        if len(self.skills) < self.maxskills:
            totaloptions += random.sample(todasskills, min (4, len(todasskills)))

        #receba tributos
        if not (len(self.passives) < self.maxpassives) and not (len(self.skills) < self.maxskills):
            totaloptions = random.sample(todososgatr, 4)
        currentoptions = []
        currentoptions = random.sample(totaloptions, 3)

        while Globals.gamerunning==1:
            ()
            for x, y in enumerate(currentoptions):
                print(f"{x+1} - {y.basename}")
            choice = input_player(player=self, actenemy=None)
            if not isinstance(choice, str):
                continue
            if choice.isdigit():
                sd=int(choice)-1
                if 0<= sd < len(currentoptions):
                    slc= currentoptions[sd]

                    if slc in todasaspassivas:
                        self.passives.append(slc)
                        print(f"{slc.basename} added to your skills!")
                        break

                    elif slc in todasskills:
                        self.skills.append(slc)
                        print(f"{slc.basename} added to your skills!")
                        break

                    elif slc in todososgatr:
                        slc.apply(self)
                        print(f"you gained {slc.basename}!")
                        break
                else:
                    print("Bro... choose something, stop scratching your butt")
            else:
                print("Really? this isn't is going to work you know that.")


    def death(self):
        if self.acthp<=0:
            print(f"the {self.name} got killed by a enemy and died in a horrible way!")
            Globals.gamerunning = 2
    
    @classmethod
    def breeding(cls, parent1, parent2):
        pronoun = random.choice(["She", "He"])
        if pronoun == "She":
            pos = "Her"
        else:
            pos = "His"
        
        def chooseATKFORM():
            AtkChoice = random.randint(1, 10)
            if AtkChoice <= 3:
                atf = "ranged"
            else:
                atf ="melee"
            return atf
        
        def inherit(stat1, stat2):
            return (random.choice([stat1, stat2]) + random.randint(-1, 1))
        
        if parent1.status=="Queen" or parent2.status=="Queen":

            st = "Princess"
        else:
            st = "Bone Eater"
    
        prttsk = []

        for s in parent1.skills + parent2.skills:

            if isinstance(s, list):
                prttsk.extend(s)

            else:
                prttsk.append(s)

        prttsk = list(set(prttsk))

        if prttsk:
            filho_possible_skills = random.sample(prttsk, random.randint(1, min(2, len(prttsk))))
        else:
            filho_possible_skills = []

        filho_totalpassives = []

        if filho_totalpassives:
            res = random.randint(1,100)
            if res > 40:
                filho_passives = [random.choice(filho_totalpassives)]
            else:
                filho_passives = []
        else:
            filho_passives = []

        ttmt = []

        for m in parent1.mutations + parent2.mutations:
            if isinstance(m, list):
                ttmt.extend(m)

            else:
                ttmt.append(m)

        ttmt = list(set(ttmt))

        if ttmt:
            filho_mt = random.sample(ttmt, random.randint(1, min(2, len(ttmt))))
        else:
            filho_mt = []

        name = generate_a_random_name()
        surname = generate_a_random_surname()
        nickname = generate_a_random_nickname()
        bs_strg0 = inherit(parent1.base_strg, parent2.base_strg)
        bs_dex0 = inherit(parent1.base_dex, parent2.base_dex)
        bs_vit0 = inherit(parent1.base_vit, parent2.base_vit)
        bs_luck0 = inherit(parent1.base_luck, parent2.base_luck)
        bs_cha0 = inherit(parent1.base_cha, parent2.base_cha)
        bs_intel0 = inherit(parent1.base_intel, parent2.base_intel)
        bs_bonus_left0 = inherit(parent1.base_bonus_to_left, parent2.base_bonus_to_left)
        bs_bonus_right0 = inherit(parent1.base_bonus_to_right, parent2.base_bonus_to_right)
        bs_dodge0 = 0
        bs_vampirism0 = 0
        bs_thorns0 = 0
        bs_armor0 = 0
        bs_atkform0 = chooseATKFORM()
        bs_skills0 = filho_possible_skills
        bs_passives0 = filho_passives
        bs_shieldstat0 = 0
        bs_status0 = st
        bs_mutations0 = filho_mt

        return cls(name, surname, nickname, pronoun, pos,
                    bs_strg0, bs_dex0, bs_vit0, bs_luck0, bs_cha0, bs_intel0,
                    bs_dodge0, bs_vampirism0, bs_thorns0, bs_armor0, bs_atkform0,
                    bs_skills0,bs_passives0, bs_mutations0,bs_bonus_right0, bs_bonus_left0, bs_shieldstat0, bs_status0
                    )
    
    @classmethod
    def randomkimera(cls, statusquokk, kimquality = 0):

        def random_status():
            qualidade = (random.randint(1, 100) * 1 + (kimquality / (kimquality + 10)))
            if qualidade <= 30:
                sts = 4
            elif 30 < qualidade <= 80:
                sts = 5
            else:
                sts = 6
            return sts
        
        pronoun = random.choice(["She", "He"])
        if pronoun == "She":
            pos = "Her"
        else:
            pos = "His"
        bs_skills = [random.choice(todasskills)]
        bs_mut = [random.choice(allthemuts)]

        def random_passive():
            rd = random.randint(1, 20)
            if rd <= 13:
                return []
            else:
                return [random.choice(todasaspassivas)]
            
                
        name = generate_a_random_name()
        surname = generate_a_random_surname()
        nickname = generate_a_random_nickname()
        return cls( name, surname, nickname, pronoun, pos, 
                   random_status(), random_status(), random_status(), random_status(), random_status(), random_status(),
                   0, 0, 0, 0, "melee", bs_skills, random_passive(), bs_mut, 0, random.randint(0, 2), 
                   0, statusquokk
        )

    
    #USAR DEEPCOPY NO LUGAR?
    # @classmethod
    # def clone(cls, cloned):
    #     bs_name = str(cloned.name + " " + "CLONE")
    #     bs_pronoun = cloned.pronoun
    #     bs_possessive = cloned.possessive
    #     bs_st = cloned.base_strg
    #     bs_dx = cloned.base_dex
    #     bs_vt = cloned.base_vit
    #     bs_lk = cloned.base_luck
    #     bs_ch = cloned.base_cha
    #     bs_it = cloned.base_intel
    #     bs_dodge = 0
    #     bs_vampirism = 0
    #     bs_thorns = 0
    #     bs_armor = 0 
    #     bs_atkform = cloned.atkform
    #     bs_skills = cloned.skills
    #     bs_passives = cloned.passives
    #     bs_shieldstat = 0
    #     bs_status = "Bone Eater" 
    #     return cls( bs_name, bs_pronoun, bs_possessive, 
    #                bs_st, bs_dx, bs_vt, bs_lk, bs_ch, bs_it, 
    #                bs_dodge, bs_vampirism, bs_thorns, bs_armor, bs_atkform,
    #                bs_skills, bs_passives, bs_shieldstat, bs_status
    #     )