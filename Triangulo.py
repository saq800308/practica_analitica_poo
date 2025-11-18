from figuras_geometricas import figura_geometrica
class Triangulo(figura_geometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return(self.base*self.altura)/2