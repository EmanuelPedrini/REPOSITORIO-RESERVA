from Enemy import enemy
import random
#enemies
fluffyskeleton=enemy("Fluffy Skeleton", 12, 5, 0, 0, 10, 10, 30, "r")
undeadgrandma=enemy("Undead Grandma", 20, 3, 0, 0, 0, 10, 30, "m")
dasbinich=enemy("DAS BIN ICH?!!", 15, 4, 0, 0, 0, 3, 30, "m")
unthought=enemy("Unthought", 7, 6, 0, 0, 50, 10, 30, "r")
kidvampire=enemy("Kid Vampire", 7, 6, 20, 0, 20, 15, 25, "m")
ironmaiden=enemy("Iron Maiden", 16, 2, 0, 3, 0, 5, 45, "m")
marshmallowknight=enemy("Marshmallow Knight", 20, 4, 0, 0, 0, 20, 40, "m")
wildkimera= enemy.wildquimera()

chainsawshark=enemy("Chainsaw Head Shark", 32, 9, 0, 0, 0, 30, 60, "m")
darknesscowboy=enemy("Cowboy of the Shadows", 26, 11, 0, 0, 20, 50, 50, "r")
hammerheadkimera=enemy("HammerHead Kimera", 44, 7, 20, 0, 10, 40, 70, "m")

enemiestofuse =[fluffyskeleton, undeadgrandma, dasbinich, unthought, kidvampire, ironmaiden, marshmallowknight]
fusioned1, fusioned2 = random.sample(enemiestofuse, 2)
beast = enemy.fusion(fusioned1,fusioned2)



enemiespool =[fluffyskeleton, undeadgrandma, dasbinich, unthought, kidvampire, ironmaiden, marshmallowknight, 
              beast, wildkimera]

enemiespoolact2 = [beast, wildkimera, chainsawshark, darknesscowboy, hammerheadkimera]