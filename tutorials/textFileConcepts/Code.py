'''
# Open a file and closing a file

f = open("pipConcepts", "r")        # open in read mode by default.
# r = read
# w = write
# a = append
# r+ = read and write
print(f.name)
f.close()                           # we have to close a file after we are done with it.
'''


'''
# Opening a file with a context manager so we don't have to close it.

with open("pipConcepts", "r") as f:         # after exiting the block file is closed automatically.
    print(f.name)
print(f.closed)                         # returns true. File is closed but we still have access t file object.
'''


'''
# read data in a single call, good for small files as all the data will be loaded into the memory.

with open("pipConcepts", "r") as f:
    f_contents = f.read()               # all of the file is being loaded in the memory.
    print(f_contents)
'''


'''
# read file line by line

with open("pipConcepts", "r") as f:
    f_contents = f.readlines()               # single line will be loaded at a time.
    print(f_contents)
'''


'''
# read a single line (cursor based)

with open("pipConcepts", "r") as f:
    f_contents = f.readline()               # first line in the file will be loaded.
    print(f_contents, end = '')             # end omits the new line inserted by print statement.
    f_contents = f.readline()               # second line in the file will be loaded.
    print(f_contents, end = '')
'''


'''
# read a single line (cursor based)
with open("pipConcepts", "r") as f:
    for line in f:                          # best way as only a single line is loaded in the memory at a time.
        print(line, end='')             # end omits the new line inserted by print statement.
'''


'''
# read file with no. of characters specified so that only that many characters will be loaded into the memory at a time.
with open("pipConcepts", "r") as f:
    size_to_read = 100
    f_contents = f.read(size_to_read)         # best way as only a single line is loaded in the memory at a time.
    while len(f_contents) > 0:
        print(f_contents, end='')
        f_contents = f.read(size_to_read)
'''


'''
# Cursor Manipulation in the file.
with open("pipConcepts", "r") as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)           # read 10 characters.
    f.tell()                                    # returns 10

    f_contents = f.read(size_to_read)           # read 10 characters from 11th position now.
    f.tell()                                    # returns 20

    f.seek(0)                                   # set the position to the start.
    f_contents = f.read(size_to_read)           # read 10 characters.
'''


# Writing to a file
'''
# Create a file or replace a file.

with open("fileObjects.txt", "w") as f:         # opens the file in write mode, create or replace strategy here.
    f.write('test')                             # writes to the file.
'''

# Read from one file and writes to another

'''
with open("pipConcepts", "r") as rf:
    with open("fileObjects.txt", "w") as wf:
        for line in rf:
            wf.write(line)
'''


# Read from image and write to image file
'''

with open("pipConcepts", "rb") as rf:               # binary mode
    with open("fileObjects.txt", "wb") as wf:       # binary mode
        for line in rf:
            wf.write(line)
'''


# Read binary file in chunks
'''
with open("pipConcepts", "rb") as rf:               # binary mode
    with open("fileObjects.txt", "wb") as wf:       # binary mode
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
'''
