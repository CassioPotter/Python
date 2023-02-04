print('\nVamos calcular quantos litros de tinta voce precisa para pinta uma parede dependendo da sua área')
altura=float(input('Qual a altura da sua parede? '))
largura=float(input('Qual a largura da sua parede? '))

area=altura*largura
tinta=area/3.25

print(f'Ola, segundo as medidas digitadas sua parede tem {area}m². ')
print(f'Para pintar essa medida você precisa ter {tinta:.1f}l de tinta a sua escolha.')
