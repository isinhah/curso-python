palavra_secreta = 'celular'
letras_acertadas = ''
tentativas = 0

print(6 * '*' + ' ADIVINHE A PALAVRA ' + 6 * '*' + '\n')

while True:
    letra_escolhida = input('Digite apenas uma letra: ').lower()

    if len(letra_escolhida) != 1:
        print('digite apenas uma letra!')
        continue

    tentativas += 1

    if letra_escolhida in palavra_secreta:
        for l in palavra_secreta:
            if letra_escolhida == l:
                print(l)
                letras_acertadas += letra_escolhida
                continue
            else:
                print('*')
                continue
    else:
        print('essa letra não está na palavra')
        continue

    palavra_formada = ''
    for l in palavra_secreta:
        if l in letras_acertadas:
            palavra_formada += l
        else:
            palavra_formada += '*'

    print('palavra formada: ' + palavra_formada)
    print('tentativas: ' + str(tentativas))

    if palavra_formada == palavra_secreta:
        print('parabéns! você acertou a palavra!')
        break

    sair = input('Deseja sair? [S/N] ').lower()
    if sair == 's':
        print('programa encerrado')
        break