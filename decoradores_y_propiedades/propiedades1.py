class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self._edad = edad
    @property
    def edad(self): # Getter
        return self._edad

    @edad.setter # Setter
    def edad(self, valor):
        if valor > 0:
            self._edad = valor
        else:
            raise ValueError("Edad negativa")


manolo = Persona("Manolo", 34)
print(manolo.edad) # Getter