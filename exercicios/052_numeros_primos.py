numero=int(input('\nDigite um numero: '))
for c in range(1, numero+1):
    if numero % 1 ==0 and numero % numero == 0:
        print(f"O numero {numero} é primo.")
    else:
        print(f'O numero {numero} não é primo.')