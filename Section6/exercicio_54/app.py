numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def list_average(numbers):
    average = sum(numbers) / len(numbers)
    return average
average = list_average(numbers)
print("A média é: %d" % average)