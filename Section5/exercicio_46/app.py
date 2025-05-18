numbers = [7, 6, 567, 99, 1]
lowest_number = 2

for n in numbers:
    if n < lowest_number:
        lowest_number = n
print("O menor número é: %s" % lowest_number)