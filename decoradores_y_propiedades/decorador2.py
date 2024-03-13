import time

def cronometro(funcion):
    def envoltura(n):
        inicio = time.time()
        funcion(n)
        fin = time.time()
        print(f"Tiempo que tardo en ejecutarse: {fin - inicio}")
    return envoltura

@cronometro
def pausa_corta(num):
    time.sleep(num)
@cronometro
def pausa_larga(num):
    time.sleep(num)

pausa_corta(2)
pausa_larga(3)