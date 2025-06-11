class Mammal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

class Dog(Mammal):
    def speak(self):
        return f"{self.name} barks."

class Cat(Mammal):
    def speak(self):
        return f"{self.name} meows."

for animal in [Dog("Pingo"), Cat("Daniel")]:
    print(animal.speak())

class Cow(Mammal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
    
    def speak(self):
        return f"{self.name} moos."
    
mimosa = Cow("Mimosa", 5)
print(mimosa.speak())
print(f"{mimosa.name} is {mimosa.age} years old.")