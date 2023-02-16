primeiro_termo=int(input('\nDiga o primeiro termo: '))
razao=int(input('Qual a razao? '))
decimo = primeiro_termo + (10 - 1)*razao

for c in range(primeiro_termo, decimo, razao):
    print(c)