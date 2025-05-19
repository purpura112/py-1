def compare_numbers(num1):
    if num1 > 10:
        return "O número é maior que 10"
    elif num1 < 10:
        return "O número é menor que 10"
    else:
        return "O número é igual a 10"

print(compare_numbers(5))

name_one = "Lucas"
def name_length(name):
    if len(name) > 5:
        result = "O nome é maior que 5"
    elif len(name) < 5:
        result = "O nome é menor que 5"
    else:
        result = "O nome é igual a 5"
    return result
result_one = name_length(name_one)
print(result_one)
print(name_length("Thiago"))