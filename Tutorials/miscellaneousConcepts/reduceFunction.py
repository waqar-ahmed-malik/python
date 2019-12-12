from functools import reduce


# reduce take the first two arguments compute the results
# then take the third element and result of first two and so on.

numbers = [1, 2, 3, 4, 5]

running_sum = reduce(lambda x, y: x + y, numbers)

print(running_sum)