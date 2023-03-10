"""
tuplas
são parecidas com listas, pela diferença de que:
são representadas por ()
são imutaveis
tuplas são definidas pela virgula

"""
tupla1 = (1, 2, 3, 4, 5)
tupla2 = 1, 2, 3, 4, 5
tupla3 = (1) #não e uma tupla
tupla4 = (1,)#é uma tupla
tupla5 = tuple(range(11))
tupla6 = tupla1 + tupla2
nome = tuple('cassio potter')
meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'desembro')
i = 0

print(type(()))

print('\n')
print(tupla1)
print(type(tupla1))

print("\n")
print(tupla2)
print(type(tupla2))

print('\n')
print(tupla3)
print(type(tupla3))

print('\n')
print(tupla4)
print(type(tupla4))

print('\n')
print(tupla5)
print(type(tupla5))

print('\n')
print(tupla6)
print(type(tupla6))

print('\n')
print( 3 in tupla1)

print('\n')
for n in tupla1:
    print(n)

print('\n')
print(tupla1.count(2))

print('\n')
print(nome)
print(nome.count('t'))

print('\n')
print(meses)
print(meses[8])
while i < len(meses):
    print(meses[i])
    i = i+1

print('\n')
print(meses.index('agosto'))