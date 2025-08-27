'''
Exercício 3 codificador e decodificador de frases

Crie um programa que codifica e decodifica uma frase, seguindo as regras abaixo.

cada vogal deve ser substituida pelo numero correspondente.

a - 1
e - 2
i - 3
o - 4
u - 5
'''

frase = input('Bem vindo ao seu decodificado e codificador de frases!\n insira uma frase: \n')
frase_codificada = '' 
frase_decodificada = '' 
for caractere in frase.lower():
    if caractere == 'a':
        frase_codificada += '1'
    elif caractere == 'e':
        frase_codificada += '2'
    elif caractere == 'i':
        frase_codificada += '3'
    elif caractere == 'o':
        frase_codificada += '4'
    elif caractere == 'u':
        frase_codificada += '5'
    else:
        frase_codificada += caractere

for caractere in frase.lower():
    if caractere == '1':
        frase_decodificada += 'a'
    elif caractere == '2':
        frase_decodificada += 'e'
    elif caractere == '3':
        frase_decodificada += 'i'
    elif caractere == '4':
        frase_decodificada += 'o'
    elif caractere == '5':
        frase_decodificada += 'u'
    else:
        frase_decodificada += caractere

print(f'frase original: {frase}\n')
print(f'frase codificada: {frase_codificada}\n')
print(f'frase decodificada: {frase_decodificada}\n')