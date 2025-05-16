lista_de_notas = [1, 10, 8, 5]

i = 0
soma_notas = 0

while i < 4:
    soma_notas = soma_notas + lista_de_notas[i]
    i = i + 1

media = soma_notas / 4
print("A média das notas é: %d" % (media))