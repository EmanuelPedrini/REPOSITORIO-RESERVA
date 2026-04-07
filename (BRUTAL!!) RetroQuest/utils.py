import random
def rolld100():
    return int(random.randint(1,100))
def rolld6():
    return int(random.randint(1,6))

def mult_rolld6(numdice):
    total=0
    for i in range(numdice):
        total +=random.randint(1, 6)
    return int(total)