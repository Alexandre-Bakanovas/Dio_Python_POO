"""
Requisitos:
    -Depositar valores apenas positivos
    -Todos os depositos devem ser armazenados e exibidos na operação de extrato
    -Sistema deve permitir realizar 3 saques diários com limite de 500 por saque
    -Caso o usuário não tenha saldo, deve exibir a msg "Saque indisponível devido a saldo insuficiente"
    -Todos os saques devem ser exibidos em uma variável e exibidos na operação de extrato.
    -Função extrato deve listar todos os depósitos e saques realizados na conta.
    -Ao fim da listagem, deve-se exibir o saldo atual da conta
    -Valores devem ser exibidos com o formato R$ xxx.xx
"""

saldo  = 0
LIMITE_SAQUE = 3
lista_deposito = []
saquesRealizados = 0
lista_saque = []

while True:
    try:
        print("Menu BANCO")
        print('1 - Depositar')
        print('2 - Saque')
        print('3 - Extrato')
        print('4 - Sair')
        opcao = int(input('Digite o número da operação deseja realizar: '))
        if opcao >= 1 and opcao <=3:
            while opcao != 4:
                if opcao == 1:
                    try:
                        deposito = float(input('Digite quanto gostaria de depositar: '))
                        if deposito < 0:
                            print('Você deve depositar um valor acima de 0 e não negativo.')
                            print()
                        else:
                            saldo += deposito
                            lista_deposito.append(deposito)
                            print()
                            break
                    except:
                        print('Digite um valor válido.')
                        print()
                elif opcao == 2:
                    try:
                        saque = float(input('Digite quanto deseja sacar: '))
                        if saque > 500 or saquesRealizados >= LIMITE_SAQUE:
                            print('Não é possível realizar essa operação')

                        elif saque > saldo:
                            print()
                            print(f'Saldo insuficiente em conta. Você possui R$ {saldo:.2f}')
                            print()

                        else:
                            saquesRealizados += 1
                            saldo -= saque
                            lista_saque.append(saque)
                            print()
                            break
                    except:
                        print('Digite um valor válido.')
                        print()
                elif opcao == 3:
                    print()
                    print('EXTRATO BANCARIO: ')
                    print()
                    i = 1
                    print('DEPOSITOS')
                    for deposito in lista_deposito:
                        print(i, f' - R${deposito:.2f}')
                        i += 1
                    print('')
                    i = 1
                    print('SAQUES')
                    for retirada in lista_saque:
                        print(i, f' - R${retirada:.2f}')
                        i += 1
                    print()
                    print(f'Saldo em conta: R${saldo:.2f}')
                    print()
                    break
        elif opcao == 4:
            break
        else:
            print()
            print('Digite um número entre 1 e 4')
            print()
            continue
    except ValueError: 
        print()
        print('Digite um número entre 1 e 4')
        print()


print('Fim do programa.')
