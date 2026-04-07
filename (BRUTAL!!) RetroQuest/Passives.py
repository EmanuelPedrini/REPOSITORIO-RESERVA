#definindo passivas
class passive:
    def __init__(self, name, text, effect, trigger): #adicionar "TRIGGER" depois
        self.level = 1
        self.basename = name
        self.text = text
        self.effect = effect
        self.trigger = trigger

    def passiveactivationtrigger(self, kimera):
        self.effect(kimera)
    
    def level_up(self):
        self.level += 1
        print(f"{self.basename} leveled up to Lv {self.level}!")