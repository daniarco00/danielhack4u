class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.__kilometraje = 0

    def conducir(self, kilometros):
        if kilometros >= 0:
            self.__kilometraje += kilometros
        else:
            print("\n Los kilometros deben ser mayores o iguales a 0")

    def mostrar_kilometros(self):
        return self.__kilometraje


coche = Coche("Toyota", "Corolla")
coche.conducir(150)
print(coche.mostrar_kilometros())

