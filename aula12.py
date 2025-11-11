frase = "essa frase é um tEstE".lower()

i = 0
maior_frequencia  = 0
letra_mais_frequente = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    frequencia_atual  = frase.count(letra_atual)

    if frequencia_atual  < maior_frequencia:
        maior_frequencia  = frequencia_atual
        letra_mais_frequente  = letra_atual

    i += 1

print(f'a letra que apareceu mais vezes foi: {letra_mais_frequente}, ela apareceu {maior_frequencia}x')