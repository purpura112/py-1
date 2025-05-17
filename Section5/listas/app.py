list_example = [1, 2, 3, 4, 5]
print(list_example)

list_names = ["Juan", "Pedro", "Maria"]
print(list_names)

list_mixed = [1, "Juan", 3.14, True]
print(list_mixed)

list_example[1] = 10
print(list_example)

#quantidade de elementos
print(len(list_example))
print(len(list_names))

if len(list_example) > 5:
    print("A lista tem mais de 5 elementos")
else:
    print("A lista tem 5 ou menos elementos")