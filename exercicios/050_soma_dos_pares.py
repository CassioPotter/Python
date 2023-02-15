soma=0
cont=0
for c in range(1,7):
    numero = int(input(f'\nDigite o {c} valor: '))
    if numero % 2 == 0:
        cont=cont+1
        soma=soma+numero
print(f'Você digitou {cont} valores de pares e a soma dos numeros pares é {soma}')

