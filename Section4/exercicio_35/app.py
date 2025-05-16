saque = int(input("Insira um valor: "))
cedula_1 = 0
cedula_10 = 0
cedula_20 = 0
cedula_50 = 0
cedula_100 = 0

while saque > 0:
    while saque >= 100:
        cedula_100 = cedula_100 + 1
        saque = saque - 100

    while saque >= 50:
        cedula_50 = cedula_50 + 1
        saque = saque - 50
    
    while saque >= 20:
        cedula_20 = cedula_20 + 1
        saque = saque - 20
    
    while saque >= 10:
        cedula_10 = cedula_10 + 1
        saque = saque - 10

    while saque >= 1:
        cedula_1 = cedula_1 + 1
        saque = saque - 1 
        print("você recebeu %d notas de R$100, %d notas de R$50, %d notas de R$20, %d notas de R$10, %d notas de R$1" % (cedula_100, cedula_50, cedula_20, cedula_10, cedula_1))
else:
    print("Valor inválido.")