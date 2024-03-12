class Caja:
    def __init__(self, *items):
        self.items = items

    def __len__(self):
        return len(self.items)

caja = Caja("Manzana", "Naranja", "Pera", "Uva", "Papaya")
print(len(caja))