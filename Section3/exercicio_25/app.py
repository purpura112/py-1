num = int(input("Digite um número: "))

if num > 10:
  print("Ok")
  if num < 20:
    multi = num * 2
    print("A multiplicação de %d é %d." %(num, multi))
  else:
    multi2 = num * 5
    print(multi2)
  
else:
  print("Para prosseguir precisa ser maior que 10.")