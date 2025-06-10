class Car:
    def __init__(self, doors, engine, brand, price, solar_roof):
        self.doors = doors
        self.engine = engine
        self.brand = brand
        self.price = price
        self.solar_roof = solar_roof

car_1 = Car(2, "GT", "Ferrari", 500000, True)

print(car_1.doors, car_1.engine, car_1.brand, car_1.price, car_1.solar_roof)