class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    def mostrar_saldo(self):
        print(f"El saldo de {self.titular} es ${self.__saldo} euros.")
    
    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto



    