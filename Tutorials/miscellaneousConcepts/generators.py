# We talked above about lazy evaluation, where we don’t compute the results right away,
# but when needed. That is exactly what a generator is and, if you have been using the range()
# function, you have been using them all along. We can create our own generators by writing
# functions that use the yield keyword instead of return. Return will fetch something,
# give it back to us and exit the function. With yield we can create a sequence and then we
# iterate over it when we need to. Yield does not stop the execution of the function,
# we can have logic after it too and it ‘remembers’ its previous value.
# Let’s take a look by implementing our own range, that will give us squares of
# the numbers we pass as arguments:

def squares(a, b):
    i = a
    while i < b:
        yield i**2
        i += 1

# Of course, we can use for to iterate, just like any other sequence we have seen before,
# or we can use the next() function to access the next element in our sequence,
# after we bind it to a variable. This is similar to the .next() special iterator method
# we have in Java. Try running the following snippets:

for num in squares(5, 10):
    print(num)
sequene = squares(5, 10)
print(next(sequene))
print(next(sequene))
