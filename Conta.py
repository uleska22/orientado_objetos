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

        def saque(self, valor):
            if self.saldo >= valor:
                self.saldo = self.saldo - valor
                print("saque realizado com sucesso")
            else:
                print("saldo insuficiente")

        def deposita(self, valor):
            self.saldo = self.saldo + valor

        def extrato(self):
            print("cliente: ", self._titular, "saldo atual: ", self._saldo)