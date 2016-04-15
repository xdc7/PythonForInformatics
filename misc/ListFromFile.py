data = open('romeo.txt')
finalList = []
for line in data:
    l = line.rstrip()
    words = l.split()
    for word in words:
        if word not in finalList:
            finalList.append(word)

print(finalList)