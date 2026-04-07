class atribute_reward:
    def __init__(self, name, what,amount): self.basename = name; self.what = what; self.amount = amount
    def apply(self, player): player.gain_atr(str(self.what), self.amount)
