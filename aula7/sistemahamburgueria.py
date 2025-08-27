produto = 'hamburguer'
hamburguer = 25.90
cupom = "1234"
while True:
    pedido = input('Qual seu pedido? \n')
    if pedido == produto:
        print('pedido anotado\n')
        break
    else:
        print('não temos esse produto!\n')
verificarcupom = input('Você possui algum cupom? qual? \n')
if verificarcupom == cupom:
    print('cupom aplicado!\n')
    print(f'O total a ser pago é {hamburguer * 0.9}\n Programa finalizado!')
else:
    print(f'O total a ser pago é {hamburguer}\n Programa finalizado!')
