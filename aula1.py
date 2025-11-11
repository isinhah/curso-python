a = None
b = None
c = []
d = []

print(a is None) # true
print(b is not None) # false

print(a is b) # true

print(c == d) # true → listas com o mesmo conteúdo
print(c is d) # false → listas diferentes na memória

print(id(c)) # (endereço lógico) de c
print(id(d)) # (endereço lógico) de d