nome=str(input('\nQual é o seu nome? ')).strip()

splitnome=nome.split()
primeironome=splitnome[0]
ultimonome=splitnome[len(splitnome)-1]

print(f'Seu primeiro nome é {primeironome}')
print(f'Seu ultimo nome é {ultimonome}')