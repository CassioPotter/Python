from datetime import date

print('\n')
nasc=int(input('Em que ano você nasceu? '))

atual=date.today().year
idade = atual-nasc

if idade<9:
    print(f'{idade} anos = mirin')
elif idade<14:
    print(f'{idade} anos = infantil')
elif idade<19:
    print(f'{idade} anos = junior')
elif idade<25:
    print(f'{idade} anos = senior')
else:
    print(f'{idade} anos = master')

