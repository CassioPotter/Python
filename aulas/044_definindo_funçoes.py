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
