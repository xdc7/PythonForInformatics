"""
Write a while loop that starts at the last character in the string
and works its way backwards to the first character in the string,
printing each letter on a separate line, except backwards.

"""

def printLettersInReverse(word):
    index = 0
    counter = len(word)
    while (counter > 0):
        print(word[counter -1])
        counter -= 1

(printLettersInReverse("string"))