dc = {'chuck' : 1 , 'annie' : 42, 'jan': 100}

"""
printing a dictionary in a 'sorted' way
"""
def printSortedDictionary(dc):
    kys = list(dc.keys())
    kys.sort()
    for k in kys:
        print("{}: {}".format(k, dc[k]))

"""
removing punctuation marks from text and converting all chars to lowercase
"""
import string
wordDict = {}
fh = open('romeo.txt')
for line in fh:
    line = line.rstrip()
    line = line.lower()
    line = line.translate(string.punctuation)
    words = line.split()
    for word in words:
        if word not in wordDict:
            wordDict[word] = 1
        else:
            wordDict[word] += 1
print(string.punctuation)
printSortedDictionary(wordDict)

