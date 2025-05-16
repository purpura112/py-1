# exercicio 16

salario = float(input("Insira seu salário: "))
aumento = float(input("Insira quanto em porcentagem recebeu de aumento: "))
saldo = salario + (salario * (aumento/100))

print("Seu salário com o aumento é de R$%.2f" %saldo) # .2f significa 2 float apos .
