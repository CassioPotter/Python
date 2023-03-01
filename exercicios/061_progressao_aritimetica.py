primeiro_termo=int(input('Digite o primeiro termo da progressão: '))
razao=int(input('Digite a razão: '))
termo=primeiro_termo
cont=1

while cont<=10:
    print(f'{termo}=>',end='')
    termo=termo+razao
    cont+=1
