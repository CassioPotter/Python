valor=float(input('\nDigite o valor em reais '))

dolar=valor/5.15
euro=valor/5.58

print(f'\nVocê entrou com o valor de {valor}R$')
print(f'Com esse valor você pode comprar {dolar:.2f}U$')
print('ou')
print(f'Com esse valor você pode comprar {euro:.2f}E')