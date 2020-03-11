class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.numero     = numero
        self.titular    = titular
        self.saldo      = saldo
        self.limite     = limite

    def depositar(self, valor):
        self.saldo += valor

    def saca(self, valor):
        if (self.saldo < valor):
            return False
        else:
            self.saldo -=valor
            return True
        
    def extrato1(self):
        print("numero da conta: {}\nsaldo: {}".format(self.numero, self.saldo))

    def extrato2(self):
        print("numero da conta: {}\nsaldo: {}\n\nTitular: \n\t nome: {} \n\t sobrenome: {} \n\t cpf: {}".format(self.numero, self.saldo, self.titular.nome, self.titular.sobrenome, self.titular.cpf))
    
    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if (not retirou):
            return False
        else:
            destino.depositar(valor)
            return True
    
