nome=str(input('\nDigite seu nome completo por favor ')).strip()

maiusculo=nome.upper()
minusculo=nome.lower()
letra=len(nome)-nome.count(' ')
primeiro=nome.find(' ')

print(f'Seu nome em maiusculo {maiusculo}')
print(f'Seu nome em minusculo {minusculo}')
print(f'Seu nome tem {letra} letras')
print(f'Seu primeiro nome tem {primeiro} letras')
