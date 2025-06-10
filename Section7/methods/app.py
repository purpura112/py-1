class Car:
    def __init__(self, color, price):
        self.color = color
        self.price = price

    def new_color(self, color):
        self.color = color
    
car_1 = Car("Blue", 500000)
car_2 = Car("Red", 600000)
print(car_1.color, car_1.price)
print(car_2.color, car_2.price)

car_1.new_color("Green")
print(car_1.color, car_1.price)

