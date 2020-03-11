class Conta2:
    def __init__(self, numero, titular, data_abertura):
            self.numero         = numero
            self.titular        = titular
            self.data_abertura  = data_abertura
            

    def dados(self):
        print("Num conta: {}\nTitular: \n\t {} \n\t data de abertura: {}".format(self.numero, self.titular, self.data_abertura))

    
