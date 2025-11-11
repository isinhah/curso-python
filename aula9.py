numero = input("você quer a tabuada de qual número? ")
numero_maximo = input(f"até quanto vai ser a tabuada do número: {numero}? ")

numero_int = int(numero)
numero_maximo_int = int(numero_maximo)
contagem = int(0)

while contagem <= numero_maximo_int:
    resultado = numero_int * contagem
    print(f'{numero_int} x {contagem} = {resultado}')
    contagem += 1

print('acabou')