import os
print(os.getcwd())
os.path.abspath("new.txt") #Gives an absolute path
os.rmdir("Downtimer") #removes only an empty directory
os.mkdir("Downtimer") #makes anew directory
os.chdir("Downtimer") # Mves to the specified directory
print(os.getcwd())
os.listdir("Downtimer") #returns a list of all the files and sub-directories in a given directory.


