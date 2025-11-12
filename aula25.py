# split: separa a string em substrings
frase = "Python é incrível"
palavras = frase.split()
print(palavras)  # ['Python', 'é', 'incrível']

# separador personalizado
nomes = "Ana,João,Carlos".split(',')
print(nomes)  # ['Ana', 'João', 'Carlos']

# join: juntar elementos de uma lista em uma string
nomes = ['Ana', 'João', 'Carlos']
texto = ', '.join(nomes)
print(texto)  # "Ana, João, Carlos"

palavras = ['Python', 'é', 'incrível']
frase = '-'.join(palavras)
print(frase)  # "Python é incrível"

# strip: remove espaços ou caracteres extras, remove espacos em branco no comeco e final da string
texto = "   Olá, mundo!   "
print(texto.strip())   # "Olá, mundo!"

# Removendo caracteres específicos
mensagem = "---Python---"
print(mensagem.strip('-'))  # "Python"