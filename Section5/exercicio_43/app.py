numbers = [1, 2, 3, 4, 5]
first_guess = int(input("Guess one number between 1 and 5: "))
second_guess = int(input("Guess another number between 1 and 5: "))

i = 0
found = False

while i < len(numbers):
    if numbers[i] == first_guess:
        print("Found the first guess %d!" % first_guess)
        found = True
    elif numbers[i] == second_guess:
        print("Found the second guess %d!" % second_guess)
        found = True
    i += 1
if found != True:
    print("Neither guess was found!")