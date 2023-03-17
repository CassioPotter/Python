#funções
#pequena parte de código que executa tarefa especifica

def lin():
    print('--'*30)

def men(msg):
    print('-'*30)
    print(msg)
    print('-'*30)

def soma (a, b): #o valor que colocamos em soma substitui o a e b
    s=a+b
    print(s)

def som(*numeros):
    s=0
    for num in numeros:
        s+=num
    print(f'somando os valores {numeros} temos {s}')

def cont(*num):
    print(num)
    print(len(num))
    for valor in num:
        print(valor)

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos]*=2
        pos +=1





#programa principal
lin()
print('cassio potter')
lin()
print('karine carmona')
lin()

print('\n')

men('Cassio Potter')
men('Karine Carmona')

soma(4, 5)
soma(1, 1)

cont(1, 2, 3, 4, 5, 6)

valores=[1, 2, 3, 4, 5]
dobra(valores)
print(valores)

som(1, 2, 3, 4, 5)
som(6, 7, 8, 9, 0)