lista_zerada = [0, 0, 0, 0, 0]
print(lista_zerada)

i = 0 
novo_valor = 0

while i < 5:
    novo_valor = int(input("Digite um número %d: " % i))
    lista_zerada[i] = novo_valor
    i = i + 1
print(lista_zerada)