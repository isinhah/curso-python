lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = [7, 8, 9]

lista_concatenada = lista1 + lista2
print("Concatenação: ", lista_concatenada)

lista1.extend(lista3) # estendendo a lista com extend()
print("Após a lista 1 estender a lista 2: ", lista1)

lista1 += [7, 8, 9] # estendendo a lista com +=
print('usando += para estender a lista: ', lista1)

lista_mista = ['a', 'b', 'c']
lista_mista.extend([1, 2, 3])
print('extend com tipos diferentes: ', lista_mista)