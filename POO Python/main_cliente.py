from cliente import Cliente
from conta   import Conta

cliente1 = Cliente('Hyury', 'Luiz', '12345678901')
conta1 = Conta('013-13', cliente1, 1313.13, 131313.13)

conta1.extrato2()

print("######################## QUESTÕES ########################")

print("\nPodemos criar uma Conta sem um Cliente?\n")
print("Não, pois o titular da conta é instanciado na classe Cliente, onde o mesmo "
      "é essencial para criação de uma conta por ser um parametro do construtor")

print("\nPodemos criar um Cliente sem uma Conta?\n")
print("Sim, pois  ele não possui nenhum tipo de dependencia com a classe Conta")
