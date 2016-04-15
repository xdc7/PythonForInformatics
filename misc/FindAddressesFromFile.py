handle = open('mbox-short.txt')
lst = []
count = 0
emailDict = {}
maxMailsNum = 0
maxMailsId = ''
for line in handle:
    l = line.rstrip()
    lineAsList = l.split()
    if len(lineAsList) > 0 and lineAsList[0] == ('From'):
        count += 1
        lst.append(lineAsList[1])
        emailDict[lineAsList[1]] = emailDict.get(lineAsList[1],0) + 1

for k,v in emailDict.items():
    if v > maxMailsNum:
        maxMailsNum = v
        maxMailsId = k


print ("{} {}".format(maxMailsId,str(maxMailsNum)))
print((emailDict.items()))

print ((5,1,3)[0] )