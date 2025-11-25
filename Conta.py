class Conta:
    def _init_(self, titular, numero, saldo):
        self.saldo = 0.0
        self.numero = numero
        self.titular = titular

        @property

        def saldo(self):
            return self._saldo
        
        @saldo.setter
        
        def saldo(self, saldo):
            if saldo < 0:
                print("o saldo não pode ser negativo")
            else:
                self._saldo = saldo