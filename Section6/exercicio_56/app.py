def data(name, age, job, func):
    greeting = func(name, age, job)
    return greeting

def show_data(a, b, c):
    greet = f"Hello, my name is {a}, I am {b} years old and I work as a {c}."
    return greet

print(data("Alice", 30, "Engineer", show_data))