class Car:
    def __init__(self, color, price):
        self.color = color
        self.price = price

    def new_color(self, color):
        self.color = color
    
    def display_color(self):
        return f"The car color is {self.color}"
    
car_1 = Car("Blue", 500000)
car_2 = Car("Red", 600000)
print(car_1.color, car_1.price)
print(car_2.color, car_2.price)

car_1.new_color("Green")
print(car_1.color, car_1.price)

# substitution of method
class Person:
    def greet(self):
        print("Hello, I am a person.")

class Kid(Person):
    pass

kid = Kid()
kid.greet()