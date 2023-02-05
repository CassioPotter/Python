numero=int(input('\nDigite um numero que iremos lhe passar as unidades, desenas, centenas e milhar '))

unidade=numero//1%10
dezena=numero//10%10
centena=numero//100%10
milhar=numero//1000%10

print(f'A unidade {unidade}')
print(f'A dezena {dezena}')
print(f'A centena {centena}')
print(f'O milhar {milhar}')