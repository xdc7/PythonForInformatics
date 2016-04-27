import string
fh = open("..\\files\\romeo.txt")
wordDict = {}
for line in fh:
    line = line.translate(string.punctuation)
    line = line.lower()
    words = line.split()
    for word in words:
        wordDict[word] = wordDict.get(word, 0) + 1
wordList = []
for k,v in wordDict.items():
    wordList.append((v,k))
wordList.sort(reverse=True)
print(wordList)