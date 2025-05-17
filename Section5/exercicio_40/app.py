numbers = [0, 0, 0, 0, 0]
i = 0
# se a lista tiver numeros e usarmos append, 
# ele vai adicionar os numeros ao inves de substituir
while i < 5:
    numbers[i] = int(input("Enter a number %d: " % i))
    numbers.append(numbers[i])
    i += 1
print(numbers) # result will be [0, 0, 0, 0, 0, 1, 2, 3, 4, 5]

names = []
i = 0

while i < 5:
    user_name_input = input("Enter a name %d: " % i)
    names.append(user_name_input)
    i += 1
print(names) # result will be 5 names