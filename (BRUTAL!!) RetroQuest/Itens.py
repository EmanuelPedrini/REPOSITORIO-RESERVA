class item:
    def _init_(self, name, uses=1, damageg=0, healg=0, manag=0, centsg=0, xpg=0):
        self.name = name
        self.uses = uses
        self.damageg = damageg
        self.healg = healg
        self.manag = manag
        self.centsg = centsg
        self.xpg = xpg

    def use(self, player, target=None):
        if self.uses <= 0:
            print(f"{self.name} has no uses left!")
            return

        print(f"{player.name} used {self.name}!")

        # HEAL
        if self.healg > 0:
            player.heal(self.healg)

        # MANA
        if self.manag > 0:
            player.actmana = min(player.maxmana, player.actmana + self.manag)
            print(f"{player.name} recovered {self.manag} mana!")
  
        # DAMAGE
        if self.damageg > 0 and target:
            target.toma(self.damageg, player)

        # MONEY
        if self.centsg > 0:
            player.gold += self.centsg
            print(f"{player.name} gained {self.centsg} gold!")

        # XP
        if self.xpg > 0:
            player.xp += self.xpg
            print(f"{player.name} gained {self.xpg} XP!")

        self.uses -= 1