print('\n')
peso=float(input('Qual é o seu peso? '))
alt=float(input('Qual é a sua altura? '))

imc=peso/(alt**2)

if imc <= 18.5:
    print('Você esta abaixo do peso.')
elif imc <= 25:
    print('Você esta no peso ideal.')
elif imc <= 30:
    print('Você esta com sobrepeso.')
elif imc <= 40:
    print('Você esta com obesidade.')
else:
    print('Você esta com obesidade morbida.')