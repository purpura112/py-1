# if aninhado

idade = int(input('Insira sua idade: '))

if idade >= 18:
  print("Você pode entrar na balada.")
  pagamento = input("Qual a forma de pagamento? ")
  if pagamento == "Pix":
    print("Leia o QR code.")
  else:
    print("Vá para a fila.")

else:
  print("Você não pode entrar na balada.")