# convert string to list
letters = "abcde"
print(type(letters))
letters_list = list(letters)
print(type(letters_list))
print(letters_list[1])

# convert list to string
a_list = ['hi', 'there', '123', '456']
example_str = print("".join(a_list))


# using startswith and endswith
example_str = "Hello, there big world!"
print(example_str.startswith("Hello"))
print(example_str.endswith("world!"))

# using lower and upper
print(example_str.lower())
print(example_str.upper())

# using in and not in
print("Hello" in example_str)
print("Hello" not in example_str)

# using count
bunch_of_fruits = "apple, banana, cherry, apple, banana"
print(bunch_of_fruits.count("apple"))
print(example_str.count("e"))

# using find
print(example_str.find("there"))

# using split
split_str = example_str.split(",")
split_str2 = example_str.split("e")
print(split_str)
print(split_str2)

# using replace
replaced_str = example_str.replace("Hello", "Hi")
print(replaced_str)
replaced_str2 = example_str.replace("e", "a", 1)
print(replaced_str2)

# using isdigit
example_string = "Anna is 2 years old"
print(example_string.isdigit())
example_string2 = "123.45"
print(example_string2.isdigit())
print(example_string2.replace(".", "").isdigit())