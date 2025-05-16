# manipulação de string 2

nome = "Narayane"
print(nome[:4])

apelido = nome[4:]
print(apelido)

print(nome[:-4])#começa pela esquerda n(0)a(1)r(2)a(3)y(4)a(5)n(6)e(7) NARA
print(nome[-4:])#começa pela direita n(0)a(1)r(2)a(3)y(4)a(5)n(6)e(7) YANE

# print("Meu apelido é %s!" %nome[-4:])
print("Meu apelido é %s!" %nome[0:-1])#retira a ultima letra (-1) da esq para dir
print("Meu apelido é %s!" %nome[0-1:])#retira as letras e deixa a ultima da dir pra esq