#EXEMPLO DA CLASSE ENTITY
class ENTITY:
    #Os atributos iniciais necessários para criar uma classe
    def __init__(self,
    Name: str):
        self.Name = Name

    #REPR é uma propriedade nativa do python, significa ao ser printado
    def __repr__(self):
        print(f"{self.Name}")

Maria = ENTITY("Mariazinha Mata-Frango")
print(Maria) #Vai printar "Mariazinha Mata-Frango"