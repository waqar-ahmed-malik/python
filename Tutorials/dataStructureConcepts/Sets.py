# Sets Don't Allow Duplicates
# Curly braces are used to declare but don't have key value pairs.

# empty set
set1 = set()
set1 = {}   # this isn't right as it will declare empty dictionary.


List = ['a', 'b', 'b', 'c']
Set = set(List)                 # removes the extra b from the list.
print(Set)

VowelList = ['a', 'e', 'o', 'u', 'i']
VowelSet = set(VowelList)
Word = 'Waqar Ahmed.'
WordSet = set(Word)

# UNION
Union = VowelSet.union(WordSet)             # returns a set having values of both VowelSet and WordSet.

# DIFFERENCE
Difference = VowelSet.difference(WordSet)        # present in VowelSet but not in WordSet.

# Intersection
Intersection = VowelSet.intersection(WordSet)        # common between the two.
print('Word: ', Word )
print(Intersection)
print(Union)
print(Difference)
