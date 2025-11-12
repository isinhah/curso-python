frase = "  Python é incrível e divertido  "

# Limpar espaços
frase_limpa = frase.strip()

# Dividir em palavras
palavras = frase_limpa.split()

# Alterar letras
palavras_minusculas = [p.lower() for p in palavras]

# Juntar tudo de novo
nova_frase = ' '.join(palavras_minusculas)

print(nova_frase)  # "python é incrível e divertido"