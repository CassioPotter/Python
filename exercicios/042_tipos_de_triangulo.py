print('\n')
n1=int(input('Digite o primeiro lado: '))
n2=int(input('Digite o segundo lado: '))
n3=int(input('Digite o terceiro lado: '))

if n1 < (n2+n3) and n2 < (n1+n3) and n3 < (n1+n2):
    if n1 == n2 == n3:
        print("Esse triangulo é equilatero.")
    elif n1 == n2 or n2 == n3 or n1 == n3:
        print('Esse triangulo é isósceles.')
    else:
        print('Esse triangulo é escaleno.')
else:
    print('Com esses valores não é popssivel formar um triangulo.')
    