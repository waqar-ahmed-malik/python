# filter takes a collection and filter out the elements from the collection
# on the condition specified in lambda

elements = [8, 1, 16, 30, 24]

multiples_of_3 = filter(lambda n: n % 3 == 0, elements)
for multiple_of_3 in multiples_of_3:
    print(multiple_of_3)

