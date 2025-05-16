renda = float(input('Insira sua renda: '))
print(renda)

limite = 0

if renda < 2000:
  limite = 1000
elif renda < 4000:
  limite = 2000
elif renda < 10000:
  limite = 3000
elif renda > 10000:
  print("Você precisa falar com o gerente.")
  limite = 3000

print("Parabéns, o teu cartão foi aprovado! O teu limite é de %d" %limite)