# The decorator can be used on any number of functions it is compatible with,
# from the point of view of the signature of the argument function it works with,
# and it can extend the functionality of existing functions without modifying them.
# A common use case for decorators is performing validations.
# Let’s assume that we want to write functions that make some sort of operations on numbers,
# but we have to make sure that the numbers are positive. We can write a decorator 
# to validate our arguments. Let’s create our own example and investigate:


def validate_pozitive(func):
    def inner(*args, **kwargs):
        for arg in args:
            if arg < 0:
                raise Exception ('Invalid Number')
        result = func(*args, **kwargs)
        return result
    return inner     

@validate_pozitive
def calculation_excepting_only_positive_numbers(x, y, z):
    return x * y * z

    