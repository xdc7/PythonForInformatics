fh = open("..\\files\\mbox.txt")
wordDict = {}
for line in fh:
    if (line.startswith("From ")):
        words = line.split()
        wordDict[words[1]] = wordDict.get(words[1],0) + 1
wordList = []
for key, val in wordDict.items():
    wordList.append((val,key))
wordList.sort(reverse=True)
print(wordList[0])