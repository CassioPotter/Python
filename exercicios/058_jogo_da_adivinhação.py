from random import randint

computador=randint(0, 10)
jogador=int(input('\nPensei em um numero, vamos ver se você acerta? '))
tentativa=0

while jogador != computador:
    jogador=int(input('Tente novamente '))
    tentativa=tentativa+1

print('Acertou')
print(F'Eu pensei no {computador} e voce acertou com {tentativa} tentativas')