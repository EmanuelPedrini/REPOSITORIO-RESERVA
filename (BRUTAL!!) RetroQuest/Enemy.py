import random
import Globals

from utils import rolld100
from Itens_Data import todososequipamentos


class Enemy:
    def __init__(
        self,
        name,
        totalmaxhp,
        atk,
        vampirism,
        thorns,
        dodge,
        centsondeath,
        xpondeath,
        atkdist
    ):

        self.name = name

        # BASE STATS
        self.base_totalmaxhp = totalmaxhp
        self.base_atk = atk
        self.base_centsondeath = centsondeath
        self.base_xpondeath = xpondeath

        # SCALED STATS
        self.totalmaxhp = int(totalmaxhp * Globals.globaldangercalc)
        self.acthp = self.totalmaxhp

        self.atk = int(atk * Globals.globaldangercalc)

        self.centsondeath = int(
            centsondeath // Globals.globaldangercalc
        )

        self.xpondeath = int(
            xpondeath // Globals.globaldangercalc
        )

        # SECONDARY
        self.dodge = dodge
        self.vampirism = vampirism
        self.realvampirism = vampirism * 0.01
        self.thorns = thorns
        self.atkdist = atkdist

        # STATUS EFFECTS
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

    def apply_danger(self):
        scale = Globals.globaldangercalc

        self.totalmaxhp = int(self.base_totalmaxhp * scale)
        self.acthp = self.totalmaxhp

        self.atk = int(self.base_atk * scale)

        self.centsondeath = int(
            self.base_centsondeath / scale
        )

        self.xpondeath = int(
            self.base_xpondeath / scale
        )

    def take_damage(self, damage, player):

        if self.cursed:
            damage = int(damage * Globals.cursemultiplier)

        elif self.weakness:
            damage = int(damage * 1.5)

        self.acthp -= damage

        self.check_death(player)

    def heal(self, amount):

        self.acthp += amount

        if self.acthp > self.totalmaxhp:
            self.acthp = self.totalmaxhp

        print(f"> {self.name} healed {amount} HP")

    def attack(self, player):

        roll = rolld100()

        if roll > player.total_dodge:

            damage = self.atk

            damage = max(
                1,
                round(
                    damage * (1 - Globals.reds(player))
                )
            )

            if self.vampirism > 0:
                self.heal(
                    int(damage * self.realvampirism)
                )

            if player.thorns > 0 and self.atkdist == "m":

                thorn_damage = player.thorns

                self.take_damage(thorn_damage, player)

                print(
                    f"{self.name} received "
                    f"{thorn_damage} thorn damage!"
                )

            print(
                f"{self.name} attacked "
                f"{player.name} for {damage} damage!"
            )

            player.toma(damage)

        else:
            print(f"{self.name} missed!")

    def check_death(self, player):

        if self.acthp > 0:
            return

        cents = random.randint(
            self.centsondeath,
            self.centsondeath * 3
        )

        xp = random.randint(
            self.xpondeath,
            self.xpondeath * 3
        )

        item_roll = random.randint(
            1,
            100
        ) + player.total_luck

        max_items = 1 if item_roll < 75 else 2

        max_items = min(
            max_items,
            len(todososequipamentos)
        )

        loot = random.sample(
            todososequipamentos,
            max_items
        )

        print(f"{self.name} died!")

        Globals.gained_cents_battle += cents
        Globals.gained_xp_battle += xp

        for item in loot:
            Globals.gained_itens_battle.append(item)