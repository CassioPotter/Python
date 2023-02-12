valor=float(input('\nQual o valor das compras? '))
modo=int(input('''Qual a forma de pagamento?
[1]-dinheiro
[2]-Debito
[3]-até 3x
[4]-4x ou mais
'''))

if modo == 1:
    desc=valor*20/100
    novo=valor-desc
    print(f'''Sua compra foi de {valor}R$
    com o desconto de {desc}R$
    vai ficar {novo}R$.''')
elif modo == 2:
    desc=valor*10/100
    novo=valor-desc
    print(f'''Sua compra foi de {valor}R$
    com o desconto de {desc}R$
    vai ficar {novo}R$.''')
elif modo == 3:
    print(f'''Sua compra foi de {valor}R$.''')
elif modo == 4:
    acre = valor*20/100
    novo = valor+acre
    print(f'''Sua compra foi de {valor}R$
    com o acrécimo de {acre}R$
    seu novo valor vai ficar {novo}R$.''')
else:
    print('Opção invalida.')