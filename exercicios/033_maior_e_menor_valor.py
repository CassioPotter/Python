n1=int(input('\nDigite o primeiro valor: '))
n2=int(input('Digite o segundo valor: '))
n3=int(input('Digite o terceiro valor: '))

menor=n1


if n2 < n1 and n2 < n3:
    menor=n2
elif n3 < n1 and n3 < n2:
    menor=n3

maior=n1

if n2 > n1 and n2 > n3:
    maior=n2
elif n3 > n1 and n3 > n2:
    maior=n3

print(f'O número menor é {menor} e o número maior é {maior}')