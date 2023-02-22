sexo=str(input('\nInforme seu sexo [M/F] ')).strip().upper()[0]#so a primeira letra

while sexo not in 'M F':
    sexo=str(input('Dados invalido, por favor digite uma opção valida [M/F] ')).strip().upper()[0]

print(f'Dados registrado como {sexo}')