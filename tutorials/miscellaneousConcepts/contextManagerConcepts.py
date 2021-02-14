# You probably already know that you can use a with block to deal with files and you
# no longer have to worry about closing said file.

# What happens is that a special object is created, called a context manager that works
# with the with keyword and automatically does something before and after the execution
# of the logic you have in the block. What’s cool about all this is that Python allows us
# to create our own context managers by writing a class that implements two special methods:
# __enter__() and __exit__(). They take care of, you guessed it, what happens when execution
# enters and exits your with block respectively.
# Methods with “__” before and after their names, such as “__init__” (the constructor),
# are special and have to do with they way Python implements some of its functionalities.
# Let’s take a look at the example below:

class DataManager():
    def __init__(self):
        self.file = None

    def __enter__(self):
        self.file = open('open.txt', 'w')
        return self.file
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()

with DataManager() as file:
    file.write('Hello')
