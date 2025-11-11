# while: (enquanto) a condição for verdadeira
condicao = True

while condicao:
    nome = input("Qual o seu nome?")
    print(f'seu nome é {nome}')

    if nome == 'sair':
        condicao = False
        break
print('acabou')