def sayHello(name):
    print("Hello %s" % name)

sayHello("Anna")

def add_nums(number):
    return number * 2
print("The result is %d" % add_nums(5))

def sayBye(name):
    return "Bye %s" % name
sayBye("Carla")
print(sayBye("Carla"))
print(sayBye("Carla") + " and see you soon")


# the 1st param is mandatory, the 2nd is optional
def sayHello2(name, greeting="Hello"):
    return "%s %s" % (greeting, name)
print(sayHello2("Anna"))
print(sayHello2("Anna", "Hi"))

# parameters can be passed as sequence
def sayHello3(*args):
    return " ".join(args)
print(sayHello3("Hello", "Nara", "and", "welcome!"))

def numbers(*args):
    return sum(args)
print("The sum is %d" % numbers(1, 2, 3, 4, 5))