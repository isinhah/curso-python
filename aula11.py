string = "palavra-junta"

i = 0
while i <len(string):
    letra = string[i]

    if letra == ' ':
        break

    print(letra)
    i += 1
else:
    print('nao encontrei um espaço nessa string')

print('fim')