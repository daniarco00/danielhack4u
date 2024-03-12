class MiLista:

    def __init__(self):
        self.data = [1, 2, 3, 4, 5]

    def __getitem__(self, index):
        return self.data[index]

lista = MiLista()
print(lista[0])

class Saludo:

    def __init__(self, saludo):
        self.saludo = saludo

    def __call__(self, nombre):
        return f"{self.saludo} {nombre}"

hola = Saludo("Hola")
print(hola("Manolo"))