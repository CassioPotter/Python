valor=float(input('\nQual o valor das compras? '))
modo=int(input('''Qual a forma de pagamento?
[1]-dinheiro
[2]-Debito
[3]-até 3x
[4]-4x ou mais
'''))

if modo == 1:
    desc=valor-(valor*20/100)
elif modo == 2: