

posicao = 0

def avancar():
    posicao += 1
    print('seu robô avançou!')

def  recuar():
    if posicao < 0:
        print('\nerro! O seu robô ainda entá na posição inicial, mova-o para fente primeito\n')
    else:
        posicao -= 1
        print('seu robô recuou!\n')

def verificarstatus():
    print(f'A posição atual do seu robô é {posicao}')



while True:
    comando = int(input(f'\n\tSeu robô esta na posição {posicao}, o que deseja fazer? \n'
            '1 - Avançar. \n' \
            '2 - Recuar. \n' \
            '3 - Status. \n' \
            '4 - Desligar; \n' \
            ))

    if comando == '1':
        avancar()
    elif comando == '2':
        recuar()
    elif comando == '3':
        verificarstatus()
    elif comando == '4':
        print('programa finalizado!')
        break
    else:
        print('Opção invalida!\n')


    
   