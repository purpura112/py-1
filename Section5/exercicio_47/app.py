shoes = ['heels', 'white', 20]
bags = ['tote', 'black', 10]
dress = ['maxi', 'red', 30]
clothes = [shoes, bags, dress]

print("The items are: %s" % clothes)

for item in clothes:
    print("The item is: %s" % item) # print every item
    print("The item is: %s, the color is: %s, the price is: %d" % (item[0], item[1], item[2])) # print every item with its color and price