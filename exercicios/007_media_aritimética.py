nota1=float(input('\nDigite a primeira nota do aluno '))
nota2=float(input('Digite a segunda nota do aluno '))
nota3=float(input('Digite a terceira nota do aluno '))

nota_total=(nota1+nota2+nota3)/3
print(f'\nO aluno teve {nota1}, {nota2}, {nota3}, e sua média final foi {nota_total:.2f}')