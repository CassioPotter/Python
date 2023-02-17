frase=str(input('\nDigite uma frase: ')).upper().strip()
palavras=frase.split()
junto=''.join(palavras)
inverso=''

print(f'Sua frase foi {frase}')
print(f'As palavras {palavras}')
print(f'As palavras {junto}')
for letra in range(len(junto)-1, -1, -1):
    inverso+=junto[letra]
if inverso == junto:
    print('Palindromo')
else:
    print('Não é um palindromo')