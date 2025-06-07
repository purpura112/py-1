def division_func():
    if num2 == 0:
        return ValueError("Divisão por zero não é permitida.")
    else:
        result = num1 / num2
        print(f"A divisão de {num1} por {num2} é {result}.")
        return result

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# division_func(input1, input2)
# division_func(10, 2)