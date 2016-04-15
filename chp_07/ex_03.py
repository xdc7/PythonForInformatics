"""
Sometimes when programmers get bored or want
to have a bit of fun, they add a harmless Easter Egg
to their program ( en.wikipedia.org/wiki/Easter_egg_(media) ).
 Modify the program that prompts the user for the file name
 so that it prints a funny message when the user types in
 the exact file name “na na boo boo”.
 The program should behave normally for all other files which exist and don’t exist.

"""

filename = input("Enter a file name: ")
try:
    if filename == "na na boo boo":
        print("NA NA BOO BOO TO YOU - You have been punk'd")
        # exit()
    else:
        fh = open(filename)
        numOfLines = 0
        for line in fh:
            numOfLines += 1
        print ("This file contains {} lines".format(numOfLines))
except:
    print("File not found!")