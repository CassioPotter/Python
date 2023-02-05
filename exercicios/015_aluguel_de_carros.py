print('\nBem vindo a locadora de veiculos POTTER')

dia=int(input('Quantos dias voce ficou com o veiculo '))
km=int(input('Quantos km voce fez com o veiculo '))

valordia=dia*125
valorkm=km*0.8
valortotal=valordia+valorkm

print(f'\nVoce ficou {dia} com o veiculo ')
print(f'Com o valor por dia de 125R$, o valor ficou {valordia}')
print(f'Você andou {km}km com o veiculo')
print(f'Com o valor de 0,8R$, por km ficou {valorkm}')
print(f'Com o valor de {valordia}R$ + {valorkm}R$ o total ficou de {valortotal}R$')
