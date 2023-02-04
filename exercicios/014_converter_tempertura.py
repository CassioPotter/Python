temperatura=float(input('\nOla, seja bem vindo(a).\nQual a temperatura em graus celsius '))

fahrenheit=temperatura*32
kelvin=temperatura*273

print(f'Você digitou {temperatura:.2f}C°')
print(f'Em Fahrenheit a temperatura fica {fahrenheit:.2f}F°')
print(f'Em Kelvin temos a temperatura de {kelvin:.2f}K°')