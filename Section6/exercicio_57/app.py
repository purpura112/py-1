def numbers_product(*args):
    product = 1
    for number in args:
        product *= number
    return product

print(numbers_product(1, 2, 3, 4, 5))