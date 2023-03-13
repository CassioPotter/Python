#mapas sao representados por {}

receita = {"janeiro": 200, "fevereiro" : 300, "março": 400}

print(receita)

print('\n')
for chave in receita:
    print(chave)

print('\n')
for chave in receita:
    print(receita[chave])

print('\n')
for chave in receita:
    print(f'{chave} : {receita[chave]}')
    print(f'Em {chave} recebi {receita[chave]}')

print('\n')

