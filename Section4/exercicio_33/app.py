inicio = 0

while(inicio < 1):  # inicio aqui é menor que 1 e estático, sendo assim, 
                    # sempre vai pedir numero ao usuário
    numero = int(input("Digite um número de 0 a 5: "))
    
    print(numero)
    
    if numero == 0:
        print("Saindo do loop")
        break

    if numero > 5:
            print("Saindo do loop")
            break