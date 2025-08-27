'''
exercicio 2 - validação e formatação de telefone
Crie um programa que recebe um numero de telefone com 11 digitos
1 - o numero e considerado invalido se tiver 3 ou mais digitos iguais
2 - o programa deve verificar se o numero tem 11 digitos e se todos os caracteres são numeros
3 - se o numero for valido o progrma deve formata-lo para o padrão (xx)xxxxx-xxxx
4 - o programa deve imprimir o numero formatado ou a mensagem de erro correspondente
'''



numero_formatado = ''
numero = input('insira um numero de telefone: \n')
valido = True
while True:
    if not numero.isdigit():
        print('Digite um numero válido sem letras!')
        break
    if len(numero) != 12 :
        print('numero de caracteres insuficientes ou caracteres demais!')
        break

    for a in numero:
        for b in numero:
            contador = 0
            if a == b:
                contador += 1
    if contador >= 3:
        valido = False
        print('erro, seu numero de telefone tem um numero q se repete 3 vezes!')
        break
    print(f'numero válido')