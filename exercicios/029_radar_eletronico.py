velocidade=float(input('\nQual a velocidade registrada? '))

if velocidade > 70.0:
    limite=(velocidade-70)
    multa=limite*7.0
    print(f'Sua velocidade é de {velocidade} e esta {limite} acima do limite')
    print(f'Sua multa sera de {multa}')
else:
    print(f'Sua velocidade é de {velocidade} e você esta abaixo do limite, parabêns')