print('\n')
numero=int(input('Digite um numero para converter para as bases numericas: '))
escolha=int(input('''Para qual base de converssão você quer? 
[1] BINARIO
[2] OCTAL
[3] HEXADECIMAL
'''))

if escolha == 1:
    print(f'O numero {numero} para binario é {bin(numero)[2:]}')
elif escolha == 2:
    print(f'O numero {numero} para octal é {oct(numero)[2:]}')
elif escolha == 3:
    print(f'O número {numero} para hexadecimal é {hex(numero)[2:]}')
else:
    print('Valor invalido, tente novamente.')

