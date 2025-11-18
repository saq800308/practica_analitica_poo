from figuras_geometricas import figura_geometrica
class Cubo_perfecto(figura_geometrica):
    def __init__(self,lado):
        self.lado=lado

    def area(self):
        return (self.lado**2)*6