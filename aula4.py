entrada_usuario = input('digite a hora atual: ')

entrada_int = int(entrada_usuario)

try:
    if 0 <= entrada_int <= 11:
        print('bom dia')
    elif 12 <= entrada_int <= 17:
        print('boa tarde')
    else:
        print('boa noite')
except ValueError:
    print('horario incorreto')