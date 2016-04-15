"""
Write a program to read through a file and print
the contents of the file (line by line) all in upper case.

"""

filename = input("Enter a file name: \n")

try:
    fh = open(filename, 'r')
    for line in fh:
        line = line.rstrip().upper()
        print (line)
except:
    print("File not found!")