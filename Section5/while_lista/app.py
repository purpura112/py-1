numbers = [1, 2, 3, 4, 5]
i = 0

while i < len(numbers):
    if numbers[i] == 3:
        print("Found 3!")
    i += 1

fruits = ['apple', 'banana', 'cherry', 'date']
j = 0
found = False

favorite_fruits_input = input("What is your favorite fruit?  ")

while j < len(fruits):
    if fruits[j] == favorite_fruits_input:
        print("Found the fruit %s!" % favorite_fruits_input)
        found = True
    j += 1 


if found != True:
        print("Fruit %s not found!" % favorite_fruits_input)
