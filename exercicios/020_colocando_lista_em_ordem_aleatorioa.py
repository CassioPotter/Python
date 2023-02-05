import random

n1=input('\nDigite o primeiro nome ')
n2=input('Digite o segundo nome ')
n3=input('Digite o terceiro nome ')
n4=input('Digite o quarto nome ')
n5=input('Digite o quinto nome ')

nomes=[n1, n2, n3, n4, n5]
random.shuffle(nomes)

print('A ordem aleatoria ficou')
print(nomes)