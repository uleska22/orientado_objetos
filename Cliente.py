class Cliente:
    def _init_(self, n, fone):
        self._nome = n
        self._telefone = fone

    def get_nome(self):
        return self._nome
    
    def set_nome(self, nome):
        self._nome = nome