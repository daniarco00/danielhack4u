
def mi_decorador(funcion): #funcion de orden superior
    def envoltura():
        print("Estoy saludando en la envoltura del decorador antes de ejecutar la funcion")
        funcion()
        print("Estoy saludando en la envoltura del decorador despues de ejecutar la funcion ")
    return envoltura

@mi_decorador
def saludo():
    print("Hola estoy saludando dentro de la funcion")

saludo()