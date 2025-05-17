# create program that finds an element in a list and returns its index

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
number_guess = int(input("Guess a number between 1 and 10: "))
found = False

for num in numbers:
    if num == number_guess:
        print("Found the number %d!" % num)
        found = True
if found != True:
    print("Number not found!")