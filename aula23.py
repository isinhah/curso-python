frutas = ['maçã', 'banana', 'uva', 'pera']

# usando enumerate para percorrer com índice
for indice, fruta in enumerate(frutas):
    print(indice, fruta)

# muda o índice inicial com start
for indice, fruta in enumerate(frutas, start=1):
    print(f'{indice} → {fruta}')

# o método enumerate() retorna pares (índice, valor)
lista_enumerada = list(enumerate(frutas))
print(lista_enumerada)