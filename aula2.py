try:
    entrada_usuario = input("digite um numero inteiro: ")

    numero_inteiro = int(entrada_usuario)

    if numero_inteiro % 2 == 0:
        print(f'o número {numero_inteiro} é par')
    else:
        print(f'o número {numero_inteiro} é ímpar')
except ValueError:
    print('Erro. Digite um numero inteiro.')