entrada_usuario = input('digite a hora atual: ')

try:
    entrada_int = int(entrada_usuario)

    if 0 <= entrada_int <= 11:
        print('bom dia')
    elif 12 <= entrada_int <= 17:
        print('boa tarde')
    elif 18 <= entrada_int <= 23:
        print('boa noite')
except ValueError:
    print('horario incorreto')