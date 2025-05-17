fruits = [ 'apple', 'banana', 'cherry', 'date', 'elderberry']
i = 0

while i < 5:
    print(fruits[i])
    i += 1
print("End of loop")


numbers = [1, 2, 3, 4, 5]
i = 0

while i < len(numbers):
    print(numbers[i])
    i += 1
print("End of loop")

# append
numbers = [1, 2, 3, 4, 5]
numbers.append('love')
print(numbers)

# delete
fruits = ['apple', 'banana', 'cherry']
del fruits[1]
print(fruits)  # Output: ['apple', 'cherry']