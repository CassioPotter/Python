from random import randint
from time import sleep

itens = ('pedra', 'papel', 'tesoura')
comp = randint(0, 2)

joga = int(input('''\nQual e a sua jogada?
[0] - pedra
[1] - papel
[2] - tesoura
'''))

print('\nJO')
sleep(1)
print('\nKEN')
sleep(1)
print('\nPO')
sleep(1)

print('='*20)
print(f'Computador jogou {itens[comp]}')
print(f'Jogador jogou {itens[joga]}')
print('='*20)
print('\n')

if joga == 0: #pedra
    if comp == 0:
        print('Empate.')
    elif comp == 1:
        print('Computador venceu.')
    elif comp == 2:
        print('Jogador venceu.')

elif joga == 1: #papel
     if comp == 0:
        print('Jogador venceu.')
     elif comp == 1:
        print('Empate.')
     elif comp == 2:
        print('Computador venceu.')


elif joga == 2: #tesoura
     if comp == 0:
        print('Computador venceu.')
     elif comp == 1:
        print('Jogador venceu.')
     elif comp == 2:
        print('Empate.')


else:
    print('Opção invalida')        

print('\n')