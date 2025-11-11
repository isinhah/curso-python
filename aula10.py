while True:
    print("*" * 6 + " CALCULADORA " + "*" * 6)
    primeiro_numero = input('Digite o primeiro número: ')
    segundo_numero = input('Digite o segundo número: ')
    operador_escolhido = input('Escolha UM dos operadores:'
                               '\n+ -> SOMAR'
                               '\n- -> SUBSTRAIR'
                               '\n* -> MULTIPLICAR'
                               '\n/ -> DIVIDIR'
                               '\n')

    try:
        primeiro_numero_float = float(primeiro_numero)
        segundo_numero_float = float(segundo_numero)
    except ValueError:
        print("ERRO! VOCÊ DIGITOU UM NÚMERO INVÁLIDO")
        continue

    if operador_escolhido == '+':
        resultado = primeiro_numero_float + segundo_numero_float
    elif operador_escolhido == '-':
        resultado = primeiro_numero_float - segundo_numero_float
    elif operador_escolhido == '*':
        resultado = primeiro_numero_float * segundo_numero_float
    elif operador_escolhido == '/':
        try:
            resultado = primeiro_numero_float / segundo_numero_float
        except ZeroDivisionError:
            print("ERRO! NÃO É POSSÍVEL DIVIDIR POR ZERO.")
            continue
    else:
        print('OPERADOR INVALIDO!')
        continue

    print(f'Resultado: {primeiro_numero_float} {operador_escolhido} {segundo_numero_float} = {resultado}')

    sair = input('Deseja sair? [S/N]').lower()
    if sair == 's':
        print('programa encerrado')
        break