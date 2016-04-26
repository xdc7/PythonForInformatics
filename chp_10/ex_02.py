fh = open("..\\files\\mbox-short.txt")
hourDict = {}
for line in fh:
    if (line.startswith("From ")):
        words = line.split()
        hourDict[words[5][:2]] = hourDict.get(words[5][:2],0) + 1
hourList = []
for k,v in hourDict.items():
    hourList.append((k,v))
hourList.sort()
print(hourList)