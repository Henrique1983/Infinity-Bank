from operacoes import *
from banco import *


def menu():
    while True:
        print('------ BEM VINDO AO MENU ------')
        print('1 - Adicionar Conta')
        print('2 - Editar Nome')
        print('3 - Excluir Conta')
        print('4 - Consultar Conta')
        print('5 - Listar Todas as Contas')
        print('6 - Consultar Saldo')
        print('7 - Fazer Depósito')
        print('8 - Fazer Saque')
        print('9 - Transferência')
        print('10 - Sair')
        opcao = int(input('Selecione uma opção: '))
        if opcao == 1:
            nome = input('Digite o nome do cliente: ')
            saldo = float(input('Digite o saldo: '))
            adicionarConta(nome, saldo)
        elif opcao == 2:
            conta = int(input('Digite o número da conta: '))
            novoNome = input('Digite o novo nome: ')
            editarNome(novoNome, conta)
        elif opcao == 3:
            conta = int(input('Digite o número da conta: '))
            deletarConta(conta)
        elif opcao == 4:
            conta = int(input('Digite o número da conta: '))
            consultarCliente(conta)
        elif opcao == 5:
            conta = int(input('Digite o número da conta: '))
            listarTodasContas(conta)
        elif opcao == 6:
            conta = int(input('Digite o número da conta: '))
            consulta.consultarSaldo(conta)
        elif opcao == 7:
            conta = int(input('Digite o número da conta: '))
            valor = float(input('Digite o valor de deposito: '))
            deposito.depositar(conta, valor)
        elif opcao == 8:
            conta = int(input('Digite o número da conta: '))
            valor = float(input('Digite o valor de saque: '))
            saque.sacar(conta, valor)
        elif opcao == 9:
            contaOrigem = int(input('Digite o número da conta: '))
            contaDestino = int(input('Digite o número da conta: '))
            valor = float(input('Digite o valor de transferencia: '))
            transferencia.transferir(contaOrigem, contaDestino, valor)
        elif opcao == 10:
            print('---- VOCÊ SAIU DO PROGRAMA ----')
            break
        menu()