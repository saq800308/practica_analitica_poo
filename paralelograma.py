from figuras_geometricas import figura_geometrica

class paralelograma(figura_geometrica):
    def __init__(self, nombre):
        super().__init__(nombre)

    @property 
    def altura(self)->float:
        return self._altura
    
    altura.setter
    def altura(self,altura:float):
        self._altura=altura

    @property
    def base(self)->float:
        return self._base
    
    base.setter
    def base(self,base:float):
        self._base=base
    
    def area(self):
        return self.base*self.altura