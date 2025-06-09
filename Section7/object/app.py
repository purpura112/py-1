class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

car_1 = Car("Toyota", 2020, "Red")
car_2 = Car("Honda", 2019, "Blue")
print(car_1.model, car_1.year, car_1.color)
print(car_2.model, car_2.year, car_2.color)