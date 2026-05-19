from CLASSES.ENTITY import ENTITY
class StatusEffect:
    def __init__(self, Name, Duration):
        self.Name = Name
        self.Duration = Duration

    def On_Apply(self, Target):
        pass

    def On_Turn_Start(self, Target):
        pass

    def On_Turn_End(self, Target):
        pass

    def On_Remove(self, Target):
        pass

    def Should_Remove(self, Target):
        if self.Duration is not None:
            return self.Duration <= 0
        return False

class Fire(StatusEffect):
    def __init__(self, amount):
        super().__init__("Fire", Duration=None)
        self.amount = amount

    def On_Turn_End(self, Target):
        if self.amount <= 0:
            return None
        Target.Take_Damage(self.amount)
        self.amount -= 1
        return f"{Target.Name} burns for {self.amount+1} damage!"

    def Should_Remove(self, Target):
        return self.amount <= 0
    
class Bleeding(StatusEffect):
    def __init__(self, amount):
        super().__init__("Bleed", Duration=None)
        self.amount = amount

    def On_Turn_End(self, Target):
        if self.amount <= 0:
            return None
        Take_Damage(Target, self.amount)
        self.amount += 1 

        return f"{Target.Name} is bleeding for {self.amount} damage!"

    def Should_Remove(self, Target):
        return self.amount <= 0
    