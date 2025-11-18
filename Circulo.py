from figuras_geometricas import figura_geometrica
class Circulo(figura_geometrica):
    def __init__(self,radio):
        self.radio=radio
        self.pi=3.1416

    def area(self):
        return self.pi*(self.radio**2)