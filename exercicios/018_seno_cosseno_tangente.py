import math
angulo=float(input('\nDigite o angulo para saber o seno, cosseno e tangente '))

seno=math.sin(math.radians(angulo))
cosseno=math.cos(math.radians(angulo))
tangente=math.tan(math.radians(angulo))

print(f'Voce digitou o angulo {angulo}')
print(f'Com o angulo de {angulo} o seno é {seno:.2f}')
print(f'Com o angulo de {angulo} o cosseno é {cosseno:.2f}')
print(f'Com o angulo de {angulo} a tangente é {tangente:.2f}')