from Itens import item
#weapons
rustysword=item(name="Rusty sword", slot="Weapon",  bonus={"gained_dex": 2, "atkdmgbonus": 3}, atkform="melee")
iron_sword = item(name="Iron Sword", slot="Weapon", bonus={"gained_strg": 2, "atkdmgbonus": 3}, atkform="melee")
butchers_cleaver = item(name="Butcher's Cleaver", slot="Weapon", bonus={"gained_vit": 3, "atkdmgbonus": 2}, atkform="melee")
crossbow=item(name="Crossbow", slot="Weapon", bonus={"atkdmgbonus": 5}, atkform="ranged")
throwknife=item(name="Throw Knife", slot="Weapon", bonus={"atkdmgbonus": 3, "dex": 2}, atkform="ranged")
longbow=item(name="Long Bow", slot="Weapon", bonus={"atkdmgbonus": 4, "gained_dex": 1}, atkform="ranged")
boomerang=item(name="Boomerang", slot="Weapon", bonus={"atkdmgbonus": 2, "gained_dex": 1}, atkform="ranged")
brassknuckles=item(name="Brass Knuckles", slot="Weapon", bonus={"atkdmgbonus": 3, "gained_strg": 2}, atkform="melee")
cajado=item(name="Magic Staff", slot="Weapon", bonus={"gained_intel": 4}, atkform="ranged")

steel_sword = item(name="Steel Sword", slot="Weapon", bonus={"atkdmgbonus": 7, "gained_strg": 2}, atkform="melee")
axe = item(name="Axe", slot="Weapon", bonus={"atkdmgbonus": 9, "gained_strg": 3}, atkform="melee")
dagger = item(name="Dagger", slot="Weapon", bonus={"atkdmgbonus": 8, "gained_luck": 2}, atkform="melee")
fire_sword = item(name="Fire Sword", slot="Weapon", bonus={"atkdmgbonus": 11, "gained_strg": 2}, atkform="melee")
hammer = item(name="Hammer", slot="Weapon", bonus={"atkdmgbonus": 13, "gained_strg": 4}, atkform="melee")
katana = item(name="Katana", slot="Weapon", bonus={"atkdmgbonus": 12, "gained_luck": 3}, atkform="melee")

iron_armor = item(name="Iron Armor", slot="Armor", bonus={"defbonus": 7, "gained_hp": 15})
knight_armor = item(name="Knight Armor", slot="Armor", bonus={"defbonus": 9, "gained_hp": 20, "gained_strg": 1})
shadow_cloak = item(name="Shadow Cloak", slot="Armor", bonus={"defbonus": 8, "gained_luck": 2})
flame_robe = item(name="Flame Robe", slot="Armor", bonus={"defbonus": 10, "gained_intel": 2})
thunder_plate = item(name="Thunder Plate", slot="Armor", bonus={"defbonus": 12, "gained_strg": 2})
frozen_mail = item(name="Frozen Mail", slot="Armor", bonus={"defbonus": 13, "gained_hp": 25})

#lista com todas as weapons
todasaarmas=[rustysword, iron_sword, butchers_cleaver, crossbow, throwknife,boomerang,brassknuckles, longbow, cajado]

#armors
torn_clothes = item("Torn Clothes", "Armor", bonus={"thorns": 3} )
leather_armor = item("Leather Armor", "Armor", bonus={"gained_vit": 2} )
chainmail = item("Chainmail", "Armor", bonus={"armor": 3})

#lista com todas as armaduras
todasasarmors=[torn_clothes, leather_armor, chainmail]

#acsessories
old_ring = item("Old Ring", "Accessory",bonus={"gained_strg": 2})
mana_pendant = item("Mana Pendant", "Accessory",bonus={"gained_intel": 2} )
lucky_charm = item("Lucky Charm", "Accessory", bonus={"gained_luck": 2})

old_necklace = item(name="Old Necklace", slot="Accessory", bonus={"gained_hp": 5})
copper_ring = item(name="Copper Ring", slot="Accessory", bonus={"gained_strg": 1})
simple_bracelet = item(name="Simple Bracelet", slot="Accessory", bonus={"gained_hp": 3})
worn_amulet = item(name="Worn Amulet", slot="Accessory", bonus={"gained_intel": 1})
wooden_necklace = item(name="Wooden Necklace", slot="Accessory", bonus={"gained_hp": 4})
common_pendant = item(name="Common Pendant", slot="Accessory", bonus={"gained_intel": 2})

#lista com todos
todososacesssorios=[old_ring, mana_pendant, lucky_charm]

#lista com todos os equipamentos
todososequipamentos = todasaarmas + todososacesssorios + todasasarmors