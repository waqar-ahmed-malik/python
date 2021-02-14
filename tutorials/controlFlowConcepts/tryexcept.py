import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise NameError('HiThere')
finally:
    print('Goodbye, world!')

'''
If the code in try block encounters an error then one of the except block runs.
If the code in try block is successful then the else block will run.
The finally clause runs whether or not the try statement produces an exception.
'''