def data(name, age, job, func):
    greeting = func(name, age, job) # calls the function passed as an argument
    return greeting

def show_data(a, b, c):
    greet = f"Hello, my name is {a}, I am {b} years old and I work as a {c}." # creates the greeting string
    return greet

print(data("Alice", 30, "Engineer", show_data))