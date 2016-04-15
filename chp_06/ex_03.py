"""
Count the number of times a letter appears in a word

"""

def letterCount(letter, word):
    count = 0
    word = word.lower()
    letter = letter.lower()
    for l in word:
        if l == letter:
            count += 1
    return count

print(letterCount("a", "Abracadabra!"))