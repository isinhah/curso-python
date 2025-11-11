lista = [10, 20, 30, '40', True]
print('lista com vários tipos: ', lista)

lista[1] = 10
print('alterando o 20 por 10: ', lista)

lista.append(3.14)
lista.append(['a', 'b', 'c'])
print('adicionando à lista: ', lista)

lista.insert(2, 10) # indice, novo item
print('trocando o 30 por 10: ', lista)

lista.pop() # removendo o ultimo
print('removendo o ultimo: ', lista)
lista.pop(1) # removendo o elemento de indice 1
print('removendo o indice 1: ', lista)

lista.extend([40, 50, 60])
print('adicionando varios valores: ', lista)

print('primeiro elemento da lista:', lista[0])
print('ultimo elemento da lista:', lista[-1])
print('fatiando a lista de 4 em 4', lista[1:4])

del lista[0]
print('deletando um elemento por indice', lista)

lista.clear()
print('limpando a lista inteira: ', lista)