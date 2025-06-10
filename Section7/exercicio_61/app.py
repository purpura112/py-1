class Car:
    def __init__ (self, price, doors, gas_tank):
        self.price = price
        self.doors = doors
        self.gas_tank = gas_tank
    
    def fill_gas_tank(self, fill):
        gas_tank = 0
        if fill > 0:
            gas_tank += fill
            return f"Gas tank filled with {fill} liters."
        else:
            return "Invalid amount. Please enter a positive number."
    
    def drive(self, distance_km):
        km_per_liter = 10
        self.gas_tank -= distance_km / km_per_liter
        if self.gas_tank < 0:
            self.gas_tank = 0
            return "Gas tank is empty. Please refill."
        else:
            return f"Driven {distance_km} km. Remaining gas: {self.gas_tank} liters."


car_1 = Car(20000, 4, 50)
print(car_1.gas_tank)
print(car_1.drive(200))
print(car_1.gas_tank)
print(car_1.drive(400))
