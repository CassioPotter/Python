from math import hypot

co=float(input('\nQual o valor do cateto opsto? '))
ca=float(input('Qual o valor do cateto adjacente? '))

hi=(co**2+ca**2)**(1/2)
hi2=hypot(co, ca)

print(f'A hipotenusa é {hi:.2f}')
print(f'Usando o HYPOT a hipotenusa é {hi2:.2f}')