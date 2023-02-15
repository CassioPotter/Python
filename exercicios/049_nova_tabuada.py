numero=int(input('\nDigite um valor para saber a sua tabuada: '))
for c in range(0,11,1):
    print(f'{numero} x {c:2} = {c * numero}')
    c=c+1