from random import randint
from time import sleep

print('\n')
print('=+='*20)
jogador=int(input('em qual numero eu pensei? '))
print('=+='*20)
computador=randint(0, 5)

print('processando...')
sleep(3)

if jogador==computador:
    print('PARABENS VOCÊ ACERTOU')
else:
    print(f"Errou, eu pensei no {computador} e não no {jogador}")