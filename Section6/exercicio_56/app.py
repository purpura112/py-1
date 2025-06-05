def data(name, age, job, func):
    greeting = func(name, age, job)
    return greeting

def show_data(name, age, job):
    greet = f"Hello, my name is {name}, I am {age} years old and I work as a {job}."
    return greet

print(data("Alice", 30, "Engineer", show_data))