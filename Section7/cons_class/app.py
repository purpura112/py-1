class Car:

    wheels = 4  # Class variable shared by all instances

    def __init__(self, model, year):
        self.model = model
        self.year = year

mini = Car("Mini Cooper", 2020)
print(f"{mini.model} has {mini.wheels} wheels and was made in {mini.year}.")