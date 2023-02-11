print('\n*'*20)
print('    BANCO POTTER')
print('*'*20)

casa=float(input('Qual o valor da casa: '))
salario=float(input('Digite o seu salario: '))
ano=int(input('Quantos anos de financiamento? '))

prestacao = casa/(ano*12)
minimo = salario*30/100

if prestacao <= minimo:
    print(f'Imprestimo concedido, o valor da prestação ficou {prestacao:.2f}R$')
else:
    print(('Imprestimo não concedido'))

    