print('\nAnalisador de triangulo')

n1=float(input('Digite o primeiro valor: '))
n2=float(input('Digite o segundo valor: '))
n3=float(input('Digite o terceiro valor: '))

if n1 < n2+n3 and n2 < n1+n3 and n3 < n1+n2:
    print(f'Com os valores {n1}, {n2} e {n3} é possivel formar um triangulo.')

else:
    print(f'Com os valores {n1}, {n2} e {n3} não é possivel formar um triangulo')