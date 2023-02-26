numero1=int(input('\nDigite o primeiro valor: '))
numero2=int(input('Digite o segundo valor: '))
opção=0


while opção != 5:
    opção=int(input('''QUAL A SUA OPÇÃO:
[1] SOMAR:
[2] MULTIPLICAR:
[3] MAIOR:
[4] NOVOS NUMEROS:
[5] SAIR DO PROGRAMA:'''))

    if opção == 1:
        soma=numero1+numero2
        print(f'A soma de {numero1} + {numero2} = {soma}')
    elif opção == 2:
        multiplicar=numero1*numero2
        print(f'A multiplicação de {numero1} x {numero2} = {multiplicar}')
    elif opção == 3:
        if numero1 > numero2:
            print(f'Entre {numero1} e {numero2} o maior é {numero1}')
        else:
            print(f'Entre {numero1} e {numero2} o maior é {numero2}')
    elif opção == 4:
        numero1=int(input('Digite o primeiro numero: '))
        numero2=int(input('Digite o segundo numero: '))
    else:
        print('Opção invalida. Digite novamente.')

