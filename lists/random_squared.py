import random

random_numbers = [random.randint(0,49) for x in range (20)]
print(random_numbers)

squared_numbers = [item ** 2 for item in random_numbers]
print (squared_numbers)
