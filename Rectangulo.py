from figuras_geometricas import figura_geometrica
class Rectangulo(figura_geometrica):
    def __init__(self,largo,alto):
        self.largo=largo
        self.alto=alto

    def area(self):
        return self.largo*self.alto