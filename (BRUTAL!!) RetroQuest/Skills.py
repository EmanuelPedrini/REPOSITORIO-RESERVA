
class skill:
    def __init__(self, name, text, damage=0, heal=0, shieldgain=0, cost=0, target="enemy", skproperty="any"):
          self.level = 1
          self.basename = name + f" Lv.{self.level}"
          self.text = text
          self.damage = damage
          self.cost = cost
          self.heal = heal
          self.shieldgain = shieldgain
          self.target = target
          self.skproperty = skproperty

    def total_mana_cost(self, player):
          return max(1, self.cost - (player.skillcostmodifier + player.temporary_skillcostmodifier))
    
    def total_skill_damage(self, player):
          return max(1, self.damage + (player.magicdmgbonus + player.temporary_magicdmgbonus))
       

    def nome_modificado(self):
        return f"{self.basename} Lv {self.level}"
    
    def level_up(self):
        self.level+=1
        print(f"{self.basename} leveled up to Lv {self.level}!")

    def use(self, player, escolhadealvo, actenemy):
            cos = self.total_mana_cost(player)
            bdmgs=self.total_skill_damage(player)

            if player.actmana < cos:
                   print(f"You actually have [ {player.actmana} / {player.max_mana} ] Mana Points! This isn`t enough to cast this Ability!")
                   return

            if self.target=="self":
                  for sp in player.passives:
                       if sp.trigger=="on_spell":
                           sp.passiveactivationtrigger(player)
                  player.mana_use(cos)

                  if self.skproperty == "ManaFlow":
                        babs =  player.actmana
                        player.actmana -= babs
                        player.heal(babs)

                  if self.heal!=0:
                        player.heal(self.heal)

                  if self.shieldgain!=0:
                       player.gain_shield(self.shieldgain)
                  return
            
            if self.target=="enemy":
                  dmgt=bdmgs
                  if self.skproperty=="HealOnHit":
                        target = escolhadealvo(player, actenemy)
                        if target==None:
                              return
                        
                        player.mana_use(cos)
                        target.toma(dmgt, player)
                        hkl=(int(dmgt * (1 + player.real_vampirism)))
                        player.heal(hkl)
                        print(f"{player.name} used {self.basename} and caused {dmgt} Damage to {target.name} and healed {hkl} health points based on the damage!")
                        for g in player.passives:
                             if g.trigger=="on_spell":
                                  g.passiveactivationtrigger(player)

                  elif self.damage!=0:
                        target = escolhadealvo(player, actenemy)
                        if target==None:
                              return
                        player.mana_use(cos)
                        print(f"{player.name} used {self.basename} dealing {dmgt} damage to {target.name}")
                        target.toma(dmgt, player)
                        for g in player.passives:
                             if g.trigger=="on_spell":
                                  g.passiveactivationtrigger(player)

                  if target.acthp<=0 and target in actenemy:
                        actenemy.remove(target)
                  return

            if self.target=="allenemies":
                  player.mana_use(cos)
                  dmgs = bdmgs
                  print(f"{player.name} used {self.basename}!")
                  for sp in player.passives:
                        if sp.trigger=="on_spell":
                              sp.passiveactivationtrigger(player)

                  if self.skproperty=="MassHealOnDmg":
                       for u in actenemy:
                            u.toma(dmgs, player)
                            print(f"{player.name} dealed {dmgs} DAMAGE to {u.name}!")
                            player.heal(int(player.real_vampirism * dmgs))
                        #     if u.acthp<=0:
                        #          actenemy.remove(u)

                  elif self.skproperty=="DamageBasedOnMana":
                        dmsbsm = player.actmana//2
                        player.actmana -= dmsbsm
                        for l in actenemy:
                              l.toma(dmsbsm, player)
                              print(f"{player.name} dealed {dmsbsm} DAMAGE to {l.name}!")

                  elif self.damage!=0:
                        for e in actenemy:
                             e.toma(dmgs, player)

                             print(f"{player.name} dealed {dmgs} DAMAGE to {e.name}!")
                        #      if e.acthp<=0:
                        #           actenemy.remove(e)
            else:
                  print("invalid target")
                  return