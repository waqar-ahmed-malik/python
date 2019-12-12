# Before importing python looks in the CWD, then Site Packages and then standard library locations.

import Functions                                                    # imports Functions.py
print(Functions.exist('procrastination is perfection.', 'e'))       # access exist function in Functions.py
# if there is any statement other then any function in Functions.py then they will also execute.

# Here it is importing the file as it is present in the same directory.
# Look at README.txt where we have installed the searchModule into site packages after creating the searchModule
# distribution.
