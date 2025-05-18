casa = {
    "comodos": 6, 
    "paredes": "claras",
    "closet": True,
    "banheiros": 2,
}

print(casa)
print(casa["comodos"])

# add a new value to the dictionary
shoes = {}
shoes["sneakers"] = 3
shoes["heels"] = 2
print(shoes)
shoes["boots"] = 1
print(shoes)

# remove a value from the dictionary
del shoes["sneakers"]
print(shoes)
print(type(shoes))