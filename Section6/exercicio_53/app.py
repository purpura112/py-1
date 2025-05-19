def numbers_list(numbers):
    for i in numbers:
        if i % 2 == 0:
            print("%d é par" % i)
        else:
            print("%d é ímpar" % i)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers_list(numbers)

def new_numbers_list(l):
    new_list = []
    for i in l:
        if i % 2 == 0:
            new_list.append(i)
    return new_list

new_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_list = new_numbers_list(new_numbers)
print(even_list)
# this code defines a function that takes a list of numbers and returns a new list containing only the even numbers from the original list. It then creates a list of numbers, calls the function with that list, and prints the resulting list of even numbers.