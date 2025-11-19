from figuras_geometricas import figura_geometrica
class Cubo_perfecto(figura_geometrica):
    def __init__(self,nombre):
        super().__init__(nombre)
        
    @property
    def lado(self)->float:
        return self._lado
    
    @lado.setter
    def lado(self,lado:float):
        self._lado=lado


    def area(self):
        return (self.lado**2)*6