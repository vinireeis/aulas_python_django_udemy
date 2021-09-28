from pessoa import Cliente
from banco import Banco, ContaCorrente, ContaPoupanca

banco1 = Banco('Bradesco')
banco2 = Banco('Nubank')
banco1.incluir_agencia([118, 1010, 1551])
banco2.incluir_agencia(['0001'])

cliente1 = Cliente('Vinicius', 27)
cliente2 = Cliente('Larissa', 22)
cliente3 = Cliente('Joaozin', 59)

conta1 = ContaCorrente(118, 94358)
conta2 = ContaPoupanca('0001', 95294)
conta3 = ContaCorrente(1111, 656893)

cliente3.incluir_conta(conta3)
cliente1.incluir_conta(conta1)
cliente2.incluir_conta(conta2)

banco1.incluir_conta(conta1)
banco2.incluir_conta(conta2)
cliente1.get_contas(banco1)
banco1.incluir_cliente(cliente1)
banco2.incluir_cliente(cliente2)

conta1.depositar(200)
conta1.get_saldo()
conta2.depositar(1500)
conta2.get_saldo()
conta2.sacar(200)
conta2.get_saldo()
conta1.sacar(500)
conta1.get_saldo()
cliente1.contas[0].sacar(100)
cliente1.contas[0].get_saldo()


if banco1.autenticar(cliente3):
    cliente3.contas.depositar(1000)
    cliente3.contas.sacar(50)
else:
    print('Cliente não autenticado')
print()
if banco1.autenticar(cliente1):
    print('Cliente autenticado com sucesso')
    cliente1.contas[0].depositar(1000)
    cliente1.contas[0].sacar(50)
    cliente1.contas[0].get_saldo()
else:
    print('Cliente não autenticado')
