#conjuntos
#não possui valores duplicados
#não possui valores ordenados
#não são acessados via indice

s = set({1, 2, 3, 4, 5, 6, 7, 8, 9, 3})
s2 = {1, 2, 3, 4, 5, 5, 5, }
lista = [1, 2, 3, 4, 5, 5, 5]
s3 = set(lista)

print(type(s))
print(s)
# números duplicados não geram erros , mas não aparecem
print('\n')

print(type(s2))
print(s2)
print('\n')

print(lista)
print(s3)
print('\n')

if 3 in s:
    print('Tem o 3')
else:
    print('Não tem o 3')
print('\n')


