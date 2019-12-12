# Initialize
empty = []
empty = list()
numbers = [0, 1, 2, 3, 4, 5]
alphabets = ['a', 'b', 'c', 'd', 'e']
mix = [1, 'a', 1.2]



# Slicing a list
# **************************** Always reverse first before Slicing **********************
name = ['w', 'r', 'a', 'q', 'a']
print(name[0] + ''.join(name[::-1][0:4]))


# Iterate over the list
for number in numbers:
    element = number

for i in range(len(numbers)):
    element = numbers[i]

for index, value in enumerate(alphabets, start=3):
    print(index, value)     # print index and value, index will start from 3 and not 0, No value is filtered here from list

index = mix.index(1.2) # return 0 based index of the element passed.


# Reverse a list
numbers = numbers[::-1]

# list Functions
sum_elements = sum(numbers)      
min_element = min(numbers)      
max_element = max(numbers)      
length = len(numbers)   # length can vary dynamically so the are known as mutable objects.

# Add elements to a list
alphabets.append('f')               # Append add element at the last
alphabets.insert(0, 'b')            # inserts 'a' at 0 index.

# Concat two list into a single list
alphabets.extend(numbers)

# Removing element from a list
alphabets.remove('a')             # requires the value to be removed and will remove the first occurrence. if element not present returns value error.
numbers.pop(2)                    # requires index from the value to be removed, if not specified, removes the last one.
