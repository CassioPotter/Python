from random import choice

nome1=input('\nDigite o primeiro nome ')
nome2=input('Digite o segundo nome ')
nome3=input('Digite o terceiro nome ')
nome4=input('Digite o quarto nome ')
nome5=input('Digite o quinto nome ')

listadenome=[nome1, nome2, nome3, nome4, nome5]
escolhido=choice(listadenome)

print(f'\nO nome escolhido foi {escolhido}')

