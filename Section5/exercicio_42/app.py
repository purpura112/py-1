numbers = []
i = 0

while i <= 10:
    numbers.append(i)
    i += 1
print(numbers)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

j = 0
while j < len(numbers):
    if numbers[j] == 4:
        del numbers[j]
    j += 1
print(numbers)  # Output: [1, 2, 3, 5, 6, 7, 8, 9, 10]