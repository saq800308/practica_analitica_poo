from figuras_geometricas import figura_geometrica
from math import pi
class Esfera (figura_geometrica):
    def __init__(self,nombre):    
        super().__init__(nombre)

    @property
    def radio(self)->float:
        return self._radio
    
    @radio.setter
    def radio(self,radio:float):
        self._radio=radio

    def area(self):
        return 4*pi*(self.radio**2)


