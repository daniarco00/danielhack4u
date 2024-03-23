class Libro:
    def __init__(self, id, autor, titulo):
        self.id = id
        self.autor = autor
        self.titulo = titulo
        self.esta_prestado = False

    def __str__(self):
        return f"Libro({self.id}, Título: {self.titulo}, Autor: {self.autor})"
    def __repr__(self):
        return self.__str__()
class Biblioteca:
    def __init__(self, libro):
        self.libros = {}  # {1: Libro(1, Daniel Arco, Como ser un Lammer de potencia maxima), 2: Libro(2, Pepe Perez,
                                            # Aprende a colorear desde cero)}
    def agregar_libro(self, libro):
        if libro.id not in self.libros:
            self.libros[libro.id] = libro

        else:
            print(f"El {self.libro.id} ya existe en la biblioteca")

    @property

    def mostrar_libros(self):
        return [libro for libro in self.libros.values() if not libro.esta_prestado]

if __name__ == '__main__':

    biblioteca = Biblioteca(Libro)

    libro1 = Libro(1, "Daniel Arco", "Como ser un Lammer de potencia maxima")
    libro2 = Libro(2, "Pepe Perez", "Aprende a colorear desde cero")

    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)

    print(f"Libros en la biblioteca: {biblioteca.mostrar_libros}")