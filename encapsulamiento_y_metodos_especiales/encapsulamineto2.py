class CuentaBancaria:


    def __init__(self, num_cuenta, titular, saldo_inicial=0):
        self.num_cuenta = num_cuenta
        self.titular = titular
        self.__saldo = saldo_inicial

    def depositar_dinero(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Saldo actual en la cuenta: {self.__saldo}")
        else:
            print("La cantidad a depositar debe ser mayor a 0")

    def retirar_dinero(self, cantidad):
        if cantidad > 0 and self.__saldo >= cantidad:
            self.__saldo -= cantidad
            print(f"Saldo actual en la cuenta: {self.__saldo}")
        else:
            print("La cantidad a retirar debe ser mayor a 0 y menor a su saldo")

    def mostrar_dinero(self):
        return f"Saldo actual en la cuenta: {self.__saldo}"



manolo = CuentaBancaria(123456, "Manolo", 1500)
manolo.depositar_dinero(500)
manolo.retirar_dinero(200)
print(manolo.mostrar_dinero())