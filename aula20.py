# tupla usando parenteses
tupla1 = (10, 20, 30)
print(tupla1)

# tupla sem parenteses
tupla2 = 10, 20, 30
print(tupla2)

# tupla com um unico elemento (precisa de virgula no final)
tupla3 = (5,)
print(tupla3)

# acesso por  indice
print('primeiro elemento: ', tupla1[0])
print('ultimo elemento: ', tupla2[-1])

# pode ter diferentes tipos de dados
tupla_mista = ('Python', 3.14, True, [1, 2, 3])
print('Tupla mista:', tupla_mista)

# é possível concatenar tuplas
nova_tupla = tupla1 + (50, 60)
print('Tuplas concatenadas:', nova_tupla)

# método count() e index()
print('Quantas vezes 20 aparece:', tupla1.count(20))
print('Posição do 30:', tupla1.index(30))

# desempacotando tuplas
coordenadas = (10, 20, 30)

x, y, z = coordenadas

print('x =', x)
print('y =', y)
print('z =', z)

# desempacotando listas
pessoa = ['Isabel', 20, 'Python']
nome, idade, linguagem = pessoa
print(f'{nome} tem {idade} anos e estuda {linguagem}.')

# usando *_
nome, *_ = ['isabel', 20, 'python']
print(f'{nome} tem {idade} anos e estuda {linguagem}.')