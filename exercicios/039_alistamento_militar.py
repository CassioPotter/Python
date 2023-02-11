from datetime import date

print('\n')
nasc=int(input('Em qual ano você nasceu? '))

atual=date.today().year
idade = atual-nasc

print(f'Quem nasceu em {nasc} tem {idade} anos.')

if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE.')
elif idade > 18:
    saldo=idade-18
    print(f'Você deveria ter se alistado a {saldo} anos.')
elif idade < 18:
    saldo=18-idade
    print(f'Você deve se alistar em {saldo} anos.')





