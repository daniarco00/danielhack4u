class Punto:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, punto):
        return Punto(self.x + punto.x, self.y + punto.y)

    def __sub__(self, punto):
        return Punto(self.x - punto.x, self.y - punto.y)


p1 = Punto(2, 3)
p2 = Punto(5, 7)

print((p1 + p2).x, (p1 + p2).y)