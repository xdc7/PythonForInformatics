def getDomainCount(filename="..\\files\\mbox.txt"):
    try:
        fh = open(filename)
    except:
        print("File not found")
        exit()
    domainCount = {}
    for line in fh:
        if line.startswith("From "):
            words = line.split()
            word = words[1]
            indexOfAt = word.index("@")
            word = word[indexOfAt+1:]
            domainCount[word] = domainCount.get(word,0) + 1
    return domainCount

print(getDomainCount())

#Bonus: get the domain from which the max number of emails were sent
from ex_04 import getMaxCountFromDictionary

print(getMaxCountFromDictionary(getDomainCount()))