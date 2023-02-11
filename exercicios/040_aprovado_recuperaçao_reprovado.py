print('\n')
n1=float(input('Digite a primeira nota: '))
n2=float(input('Digite a segunda nota: '))
n3=float(input('Digite a terceira nota: '))
n4=float(input('Digite a quarta nota: '))
n5=float(input('Digite a quinta nota: '))

media=(n1 + n2 +n3 + n4 + n5)/5

if media >= 7.0:
    print(f'Parabens sua média foi de {media} e você esta aprovado.')
elif media < 5.0:
    print(f'Sua média foi de {media} e você esta reprovado.')
else:
    print(f'Sua media foi de {media} e você esta de recuperação.')