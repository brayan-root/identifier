#! /usr/bin/env python3
import os
dir = "Downtimer" #defining a variable
x = os.listdir(dir)
for name in x: #  Iterating Through the file names returned by file listdir()
    fullname = os.path.join(dir, name) # we join the directory to each of those file names and create a String with a valid full name..i.e it adds / or \ depending on the os
    if os.path.isdir(fullname): # use that full name to call os.path.isdir to check if it's a directory or a file
        print("{} is a directory".format(fullname))
    else:
        print("{} is a file".format(fullname))
        
        
        
    #By using os.path.join we can concatenate directories in a way that can be used with other os.path() functions.
