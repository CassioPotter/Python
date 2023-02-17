media=0
soma=0
homen=0
nomevelho=0


for c in range(1,6):
    print(f'\n----------{c} pessoa---')
    nome=str(input('Digite o seu nome: ')).strip().upper()
    idade=int(input('Digite a sua idade: '))
    sexo=str(input('Sexo [M/F]')).strip().upper()
    soma += idade

    if c == 1 and sexo in M:
        homen=idade
        nomevelho= nome
    if sexo in M and idade > homen:
        homen = idade
        nomevelho= nome

media=soma/c
print(f'A media de idade do grupo é {media}')
print(f'O homen mais velho é o {nomevelho} e tem {homen}')
