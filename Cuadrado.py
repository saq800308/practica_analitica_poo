from figuras_geometricas import figura_geometrica
class cuadrado(figura_geometrica):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado