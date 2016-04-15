__author__ = 'Juzer'

"""filename = input("Enter a filename: ")


if (filename != 'file.txt'):
    print("Invalid filename: '{0}'. Filename should be 'file.txt'".format(filename))
    exit()"""
filename = 'file.txt'
handle = open(filename,'r')
wordDictionary = {}

text = handle.read()
words = text.split()

for word in words:
    wordDictionary[word] = wordDictionary.get(word,0) + 1

bigCount = None
bigWord = None

for word, count in wordDictionary.items():
    if bigCount is None or count > bigCount:
        bigCount =count
        bigWord = word

print("The word '{0}' appears the most({1}) number of times in {2}".format(bigWord, bigCount, filename))


print("I'm excited about this course!")
























