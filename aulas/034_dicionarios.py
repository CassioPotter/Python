""".
dicionarios
são conhecido por mapas
tipo chave, valor
mostra chave e o valor
caso tente usar uma chave que não exista da keyerror
"""
print(type({}))
print('\n')
paises = {'br':'Brasil', 'eua':'estados unidos','py':'paraguai'}
print(type(paises))
print(paises)

print('\n')
pais = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')
print(type(pais))
print(pais)

print('\n')
print(paises['br'])

print('\n')
print(paises.get('br'))

