salario = int(input("Insira o seu salário: "))
print(salario)

if salario > 1000 and salario < 2000:
  print("Seu limite é de R$1000.")
elif salario > 2000 and salario < 4000:
  print("Seu limite é de R$2000.")
elif salario > 4000 and salario < 6000:
  print("Seu limite é de R$3000.")
elif salario > 10000:
  print("Fale com o gerente.")

else:
  print("Você não recebeu limite.")

