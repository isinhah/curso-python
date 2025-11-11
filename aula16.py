for i in range(10):
    if i == 2:
        print("i é 2, estou pulando de 2 em 2")
        continue
    if i == 8:
        print("i é 8, estou pulando de 8 em 8")
    for j in range(1, 3):
        print(i, j)
else:
    print("for completado com sucesso")