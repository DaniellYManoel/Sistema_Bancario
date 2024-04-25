menu = '''
[1] Deposito
[2] Saque
[3] Extrato
[4] Sair
-> 
'''

saldo = 0
limite = 500
extrato = ''
numero_saque = 0
limite_saque = 3 

while True:
    opções = int(input(menu))
    if opções == 1:

        valor = float(input('Digite o valor do deposito: R$'))

        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
        else:
            print('Valor insuficiente. Digite um valor maior que 0!')
 
    elif opções == 2:

        valor = float(input('Digite o valor do deposito: R$'))

        # Verificações
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saque >= limite_saque

        if excedeu_saldo:
            print('Operação falhou! Você não tem saldo suficiente.')

        elif excedeu_limite:
            print('Operação falhou! O valor do saque excede o limite.')

        elif excedeu_saques:
            print('Operação falhou! Número máximo de saques excedido.')

        elif valor > 0:
            saldo -=valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saque += 1

        else:
            print('Operação falhou! O valor invalido')
        
        
    elif opções == 3:
        print('\n********** Extrato *********')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('******************************')

    elif opções == 4:
        break

    else:
        print('Opção invalida. Digite novamente!')

