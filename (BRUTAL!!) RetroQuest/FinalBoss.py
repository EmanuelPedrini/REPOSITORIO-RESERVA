from Enemy import enemy; import Kimeras_Data
class finalboss(enemy):
    def __init__(self, name, intro):
        super().__init__(
            name , 
            totalmaxhp = 1 , 
            atk = 1 ,  
            vampirism =0 , 
            thorns = 0 , 
            dodge = 0 , 
            centsondeath = 100 , 
            xpondeath = 400 , 
            atkdist = "m"
            )
        self.intro = intro
        self.acthp = 0

    @property
    def totalmaxhp(self):
        if Kimeras_Data.Queen is None:
            return self._base_totalmaxhp
        return Kimeras_Data.Queen.total_max_hp * 5
   
    @totalmaxhp.setter
    def totalmaxhp(self, value):
        self._base_totalmaxhp = value

    @property
    def atk(self):
        if Kimeras_Data.Queen is None:
            return self._base_atk
        return Kimeras_Data.Queen.total_strg
    @atk.setter
    def atk(self, value):
        self._base_atk = value

    @property
    def vampirism(self):
        if Kimeras_Data is None:
            return self._base_vampirism
        return Kimeras_Data.Queen.vampirism
    @vampirism.setter
    def vampirism(self, value):
        self._base_vampirism = value

    @property
    def dodge(self):
        if Kimeras_Data is None:
            return self._base_dodge
        return Kimeras_Data.Queen.total_dodge
    @dodge.setter
    def dodge(self, value):
        self._base_dodge = value

    @property
    def thorns(self):
        if Kimeras_Data is None:
            return self._base_thorns
        return Kimeras_Data.Queen.thorns
    @thorns.setter
    def thorns(self, value):
        self._base_thorns = value

YourMama = finalboss("Your Mother", "ITS YOUR MOTHER!!!")
finalbosses = [YourMama]