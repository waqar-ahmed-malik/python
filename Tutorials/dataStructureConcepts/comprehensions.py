list_1 = [1, 2, 3, 4, 5, 6]
list_2 = ['a', 'b', 'c', 'd', 'e', 'f']

my_list = [(m, n) for m in list_1 if m == 1 for n in list_2 if n == 'a']

my_list = [(m, n) for m in list_1 for n in list_2 if n == 'a' if m == 1]

tuple_list = list(zip(list_1, list_2))

my_dict = {key: value for key in list_1 for value in list_2}

my_set = {n for n in [1, 2, 1, 2, 3, 4, 1, 2]}

'''
def gen_func(nums):
    for n in nums:
        yield n*n


for i in gen_func(list_1):
    print(i)
'''

my_generator = (n*n for n in list_1)

for i in my_generator:
    print(i)

