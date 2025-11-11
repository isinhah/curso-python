texto = "python".lower()

i = 0
tamanho_string = len(texto)
texto_antigo = ""
novo_texto = ""

for letra in texto:
     i += 1

     texto_antigo += f'{letra}'
     novo_texto += f'-{letra}'

print("TEXTO ANTIGO: " + texto_antigo)
print("NOVO TEXTO: " + novo_texto)