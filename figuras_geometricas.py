class figura_geometrica:
    def __init__(self, nombre):
        self.nombre = nombre

    def area(self):
        raise NotImplementedError("El método area() debe ser implementado por la subclase")
    