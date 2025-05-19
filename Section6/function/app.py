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