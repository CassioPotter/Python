km=int(input('\nDigite quantos km tera a viagem: '))

if km<=200:
    valor=km*0.5
    print(f'O valor da passagem de {km}km da {valor}R$')

else:
    valor=km*0.45
    print(f'O valor da passagem de {km}km, ja com os descontos da {valor}R$')