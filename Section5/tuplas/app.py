# tuples are immutable lists, we use () instead of [] or {}

tuple_numbers = (1, 2, 3)
print(tuple_numbers)
print(tuple_numbers[0])
print(type(tuple_numbers))

# tuple iteration
for number in tuple_numbers:
    print(number)
# tuple unpacking
a, b, c = tuple_numbers
print(b)

i = 0
while i < len(tuple_numbers):
    print(tuple_numbers[i])
    i += 1