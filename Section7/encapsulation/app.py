class Plane:

    __wings = 2  # Private class variable

    def __init__(self, model, capacity):
        self.model = model
        self.capacity = capacity
    
    def show_wings(self):
        return self.__wings

boeing = Plane("Boeing 747", 660)
print(boeing.model)
print(boeing.capacity)

print(boeing.show_wings())