# It maps a function to an iterable which will take each element to the function

def maximize(n):
    return n * 10

elements = [1, 2, 3]

maximized_elements = map(maximize, elements)
print(maximized_elements)
# This will return a map object and the result gets computed when we iterate element inside it.

for element in maximized_elements:
    print(element)


# Use of map and lambda
maximized_elements = map(lambda n: n * 10, elements)
for element in maximized_elements:
    print(element)

# Map object is not subscriptable so we have to iterate in a for loop