entrada_usuario = input('Digite seu primeiro nome: ')

entrada_str = str(entrada_usuario)

quantidade_letras = len(entrada_str)

if quantidade_letras <= 5:
    print("seu nome é curto")
else:
    print("seu nome é longo")