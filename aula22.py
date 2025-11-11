lista = []

while True:

    try:
        escolha_menu = int(input('1 - ADICIONAR ITEM\n'
                     '2 - APAGAR ITEM\n'
                     '3 - LISTAR ITENS\n'
                     '4 - SAIR\n'
                     'Escolha a opção: '))
    except ValueError:
        print('por favor digite um número válido (1 a 4)')
        continue

    if escolha_menu == 1:
        print('--- ADICIONAR ITEM ---')
        novo_item = input('Adicione o item na sua lista de compras: ')
        lista.append(novo_item)
        print('Item adicionado com sucesso!')
        continue
    elif escolha_menu == 2:
        print('--- APAGAR ITEM ---')
        try:
            print('--- SUA LISTA ATUAL ---')
            print(list(enumerate(lista)))
            item_existente = int(input('Qual é o número do item que você deseja apagar? '))
            lista.pop(item_existente)
            print('Item deletado com sucesso!')
        except (ValueError, IndexError):
            print('O número que você inseriu não existe na lista de compras.')
        continue
    elif escolha_menu == 3:
        print('--- SUA LISTA DE COMPRAS ---')
        for i, item in enumerate(lista):
            print(f'{i} - {item}')
        continue
    elif escolha_menu == 4:
        sair = input('Deseja sair? [S/N] ').lower()
        if sair.startswith('s'):
            print('programa encerrado')
            break
    else:
        print('você digitou errado')
        continue