name = ["Anna", "John", "Mary"]
age = [20, 30, 40]

name_and_age = []

i = 0

while i < len(name):
    name_and_age.append((name[i]))
    i += 1

j = 0

while j < len(age):
    name_and_age.append((age[j]))
    j += 1
print(name_and_age) # result will be ['Anna', 'John', 'Mary', 20, 30, 40]