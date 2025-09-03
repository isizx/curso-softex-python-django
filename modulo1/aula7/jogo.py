'''
Jogo de advinhar o número

Crie um jogo simples onde o usuário deve advinhar um número
1 - Defina um número
2 - O jogador terá um número limitado de tentativas para advinhas o número
3 - A cada tentativa o programa deve informar se o palpite foi 'muito alto' ou 'muito baixo'
4 - Se o jogador acertar o numero em qualqer tentativa, exiba uma mensagem de parabens e encerre o programa
5 - Se o jogador esgotar as tentativas  sem acertar, revele o numero secreto e uma mensagem de gamer over 
betinha.  
'''
import random

numero_secreto = random.randint(1, 100)

print('\t\nBoas vindas ao jogo de advinhação!!\n')
print('\tvocê tem 5 tentativas!!\n')
print('\tDica: está entre 1 a 100!!\n')

for x in range(5):
    while True:
        try:
            chute = int(input(f'Faça sua a tentativa numero {x+1}° Digite seu palpite: \n'))
            break
        except ValueError:
            print('Entrada inválida. Por favor, digite um número inteiro!!')

    if chute == numero_secreto:
        print(f"Parabéns! Você acertou o número secreto ({numero_secreto}) na tentativa {x}!")
        break
    elif chute > numero_secreto:
        print('O seu palpite está muito alto em relação ao numero secreto!\n')
    elif chute < numero_secreto:
        print('O numero q chutou é muito baixo em relação ao numero secreto!\n')


print("\n--- Game Over pro betinha! ---")
print(f"Suas {x} tentativas acabaram.")
print(f"O número secreto era {numero_secreto}.")