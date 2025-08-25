

posicao = 0

while True:
    comando = int(input(f'\n\tSeu robô esta na posição {posicao}, o que deseja fazer? \n'
            '1 - Avançar. \n' \
            '2 - Recuar. \n' \
            '3 - Status. \n' \
            '4 - Desligar; \n' \
            ))

    if comando == '1':
        posicao += 1
        print('seu robô avançou!')
    elif comando == '2':
        if posicao < 0:
            print('\nerro! O seu robô ainda entá na posição inicial, mova-o para fente primeito\n')
        else:
            posicao -= 1
            print('seu robô recuo!\n')
    elif comando == '3':
        print(f'A posição atual do seu robô é {posicao}')
    elif comando == '4':
        print('programa finalizado!')
        break
    else:
        print('Opção invalida!\n')