allthebabies = []; allkimeras = []; allthekimerasforbreed = []; princesses = []
Queen = None

def actualize_queen(lista):
    global Queen
    Queen = None
    for qk in lista:
        if qk.status=="Queen":
            Queen = qk

def actualize_breed(lista):
    allthekimerasforbreed.clear()
    for kim in lista:
        if kim.age > 2:
            allthekimerasforbreed.append(kim)

def actualize_princesses(lista):
    princesses.clear()
    for k in lista:
        if k.age > 2 and k.status == "Princess":
            princesses.append(k)
    
