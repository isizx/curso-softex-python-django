'''Desafio de Programação: Validação de Triângulo
Seu objetivo: Escrever um algoritmo em Python que determine se três valores, fornecidos pelo usuário, podem formar um triângulo.

As Regras do Jogo
1- Teste se a entrada de dados é um número.
2- Se for um número teste se é positivo
3- Para que três lados (lA,lB,lC) formem um triângulo, eles devem obedecer a duas condições importantes:

A soma: A soma de quaisquer dois lados deve ser maior que o terceiro lado.

lA<lB+lC

lB<lA+lC

lC<lA+lB

A diferença: O valor absoluto da diferença entre dois lados deve ser menor que o terceiro lado.

lA>|lB-lC|

lB>|lA-lC|

lC>|lA-lB|

Dica: use o método abs() para ter o valor absoluto de um número.'''

lA = input("lado A: ")
lB = input("lado B: ")
lC = input("lado C: ")

if lA.isdigit() and lB.isdigit() and lC.isdigit():
    la = int(lA)
    lb = int(lB)
    lc = int(lC)

    if la > 0 and lb > 0 and lc > 0:
        
        condicao_soma = (la < lb + lc) and (lb < la + lc) and (lc < la + lb)

        condicao_diferenca = (la > abs(lb - lc)) and (lb > abs(la - lc)) and (lc > abs(la - lb))
        
        if condicao_soma and condicao_diferenca:
            print("Triângulo válido.")
        else:
            print("Triângulo inválido. As condições de soma e/ou diferença não são atendidas.")

    else:
        print("Entradas inválidas. Os lados devem ser números positivos.")
else:
    print("Entradas inválidas. Por favor, insira números inteiros.")