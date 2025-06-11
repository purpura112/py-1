class Person:
    def __init__ (self, name, age):
        self.name = name
        self.age = age

class SuperHero(Person):
    def __init__(self, name, age, power):
        super().__init__(name, age)
        self.power = power

# create a SuperHero power
    def fly(self):
        print(f"{self.name} is flying with the power of {self.power}!")
    
    def super_strength(self):
        print(f"{self.name} is using super strength with the power of {self.power}!")

# call the methods
hero = SuperHero("Superman", 30, "flight")
hero.fly()
hero.super_strength()

hero2 = SuperHero("Hulk", 35, "super strength")
hero2.fly()
hero2.super_strength()