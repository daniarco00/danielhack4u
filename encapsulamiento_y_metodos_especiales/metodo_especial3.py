class Pizza:

    def __init__(self, size, *ingredients):
        self.size = size
        self.ingredients = ingredients

    def description(self):
        return f"Tamaño: {self.size}, Ingredientes: {','.join(self.ingredients)}"



pizza = Pizza(12, "Chorizo", "Jamon", "Bacon", "Queso", "Tomate")
print(pizza.description())