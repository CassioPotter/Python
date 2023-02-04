print('\nOla seja bem vindo')
preço=float(input('Qual o valor de suas compras '))
porcetagem=int(input('Qual a porcetagem de desconto que suas compras vão receber '))

desconto=preço-(porcetagem*preço/100)

print(f'Suas compras deu {preço}R$')
print(f'Com o desconto de {porcetagem}%')
print(f'O valor final ficou {desconto:.2F}R$')