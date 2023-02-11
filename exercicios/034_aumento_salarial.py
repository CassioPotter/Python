salario=float(input('\nQual o seu sálario? '))

if salario <= 1250:
    novo = salario + (salario*15/100)
else:
    novo = salario + (salario * 10/100)

print(f'Seu salario era de {salario}R$ agora esta de {novo}R$')