menor=999999999
maior=0

for c in range(1,6):
    peso = float(input(f'\nDigite o {c} valor: '))
    if peso < menor:
        menor=peso
    if peso > maior:
        maior=peso

print(f'O maior foi {maior} e o menor foi {menor} ')
