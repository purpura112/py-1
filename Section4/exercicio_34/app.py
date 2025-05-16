numero = int(input("Digite um número de 1 a 10: "))

divisoes = 0
contador = numero

while contador > 0:
    if numero % contador == 0:
        divisoes = divisoes + 1

    contador  = contador - 1

if divisoes == 2:
    print("O número %d é primo." % numero)
else:
    print("O número %d não é primo." % numero)