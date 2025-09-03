'''
1- rodar em loop
2- ter conta e senha (validar)
3- encerrar atendimento 
4- cheque especial (limite saldo negaivo)
5- tentar 3 vezes a senha
6- opções (saque, deposito, saldo)
7- mostrar saldo apos saque
8- alterar senha
9- dizer o nome do usuario(boas vindas)
10- pagar boleto 
'''

#declaração---------

conta_corrente = "123456-7"
senha_usuario = "0000"
usuario = 'José'
saldo_atual = 0
limite_saldo_negativo = 500.00

while True:

    print('\t Bem vindo ao sistema de banco!')

    
    for i in range(3):
        conta = input('insira seu usuario: \n')
        senha = input('insira sua senha: \n')
        if conta == conta_corrente and senha == senha_usuario:
            print(f'Bem vindo ao sistemas de banco softex {usuario}!\n')
            acesso_permitido = True
            break
        else:
            print(f'Acesso inválido! Tentativa {i+1}/3\n')
            acesso_permitido = False
            break

    if acesso_permitido == False:
        break

    while True:
        opcao = input('Bem vindo ao menu! Insira uma opção válida: \n' \
                          '1 - Ver saldo. \n' \
                          '2 - Sacar valor. \n' \
                          '3 - Depositar. \n' \
                          '4 - Pagar boleto; \n' \
                          '5 - Alterar senha. \n' \
                          '6 - Sair. \n')
        if opcao == '1':
            print(f'O saldo do usuario {usuario} é {saldo_atual}\n')
        elif opcao == '2':
            valor_a_sacar = float(input('Insira o valor a ser sacado: \n'))
            if valor_a_sacar <= (saldo_atual + limite_saldo_negativo) :
                saldo -= valor_a_sacar
                print('saldo liberado, retire seu valor! \n')
            else:
                print('Saldo insuficiente, deposite um valor primeiro! \n')
        elif opcao == '3':
            print(f'{usuario}, seu saldo é {saldo}!')
            deposito = float(input('Insira o valor a ser depositado: \n'))
            if deposito < 0:
                print('erro, insira um valor positivo! \n')
            else:
                saldo += deposito
                print(f'{usuario}, seu saldo agora é {saldo}!')
        elif opcao == '4':
            boleto = float(input('Entre com o valor do boleto: \n'))
            if boleto < (saldo_atual + limite_saldo_negativo):
                saldo -= boleto
            else:
                print('Saldo insuficiente') 
        elif opcao == '5':
            senha_antiga = input('Digite a senha antiga: \n')
            senha_nova1 = input('Digite a nova senha: \n')
            senha_nova2 = input('Repita sua senha: \n')
            if senha_antiga == senha_usuario and senha_nova1 == senha_nova2:
                senha_usuario = senha_nova1
                print('senha atualizada com sucesso! \n')
            else:
                print('senha inválida! \n')

        elif opcao == '6':
            print('\tAtendimento finalizado!')
            break
        else:
            print('opção invalida!')

        
