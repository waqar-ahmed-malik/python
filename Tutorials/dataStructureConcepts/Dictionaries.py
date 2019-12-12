# Curly braces are used to declare dictionaries each entry having a key and its value.
# Unordered, as insertion order and print order can be different.

Person = {
    'name':         'Adam',
    'occupation':   'Something',
    'age':          7,
    'New':              'Four'
}

# Accessing a single value in a dictionary
print(Person['name'])                           # Hashing algorithm with resizeable hash algorithm.
print(Person['New'])

# Initialize a key in a dictionary

Person['Address'] = 'New Address'

# Initialize if the key is needed in the program
Person.setdefault('Address', 'No address up until now')

# Iterating over a list
for key, value in sorted(Person.items()):       # Sorted function sorts the dictionary keys alphabetically. But the
    print(key, ':',  value)                     # dictionary keys should only be strings.


# Frequency Counter

VowelList = ['a', 'e', 'o', 'u', 'i']
Word = 'Kids Or Legends. You all are gonna die anyway.'
Found = []
FrequencyCounter = {}
for letter in VowelList:
    for i in range(len(Word)):
        if Word[i].upper() == letter.upper():
            FrequencyCounter.setdefault(letter, 0)
            FrequencyCounter[letter] += 1           # Destructive
for key, value in FrequencyCounter.items():
    print(key, ': ', value)


# for accessing a key and don't know if it exists then always use list.get('key')

dictionary = {'Name': 'Waqar', 'Age': 12, 'Hobbies': ['Music', 'Football']}
print(dictionary.get('Name'))   # returns Waqar
print(dictionary.get('Class'))   # returns None
print(dictionary.get('Class', 'Not Found'))   # returns Not Found

# To Update a dcitionary
dictionary.update({'Name': 'Waqar', 'Age': 22, 'Hobbies': ['Music', 'Trash Talk']})

# delete a key
del dictionary['Age']

# Add a key
dictionary.update({'Name': 'Waqar', 'Age': 22, 'Hobbies': ['Music', 'Trash Talk'], 'New Key': 'New Value'})
