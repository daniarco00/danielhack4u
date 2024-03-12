class Libro:
    def __init__(self, autor, titulo):
        self.autor = autor
        self.titulo = titulo


    def __str__(self):
        return f"Titulo: {self.titulo}, Autor: {self.autor}"

    def __eq__(self, otro):
        return self.autor == otro.autor and self.titulo == otro.titulo



mi_libro = Libro("Daniel", "Como ser un Lamer")
libro_dos = Libro("Daniel", "Como ser un Hacker")
print(mi_libro)
print(f"Son iguales ambos libros? -> {mi_libro == libro_dos}")