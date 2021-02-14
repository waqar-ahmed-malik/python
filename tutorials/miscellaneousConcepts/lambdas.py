# lambda a type of function with no def keyword.
# functionality is stored in a variable
# It can have any number of arguments
# It can support 1 line expressions to execute.

power = lambda n: n**2 if n % 2 == 0 else n**3    # n is the argument
print(power(5))

arithmetic = lambda a, b: a + b if (a + b) % 2 == 0 else a - b

print(arithmetic(5 , 3))
