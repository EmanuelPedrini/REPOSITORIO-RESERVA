from Enemy import enemy
class boss(enemy):
    def __init__(self, name, totalmaxhp, atk, vampirism, thorns, dodge, centsondeath, xpondeath, atkdist, intro):
        super().__init__(name, totalmaxhp, atk, vampirism, thorns, dodge, centsondeath, xpondeath, atkdist)
        self.name = name
        self.intro = intro