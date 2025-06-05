def sum(a, b):
    return a + b

def multiply(a, b):
    return a * b

def apply_function(func, a, b):
    return func(a, b)

result = apply_function(sum, 5, 3)
print(f"Sum: {result}")

result = apply_function(multiply, 5, 3)
print(f"Product: {result}")
# This code defines two functions, `sum` and `multiply`, and a third function `apply_function`