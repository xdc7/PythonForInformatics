handle = open('mbox-short.txt')
lst = []
count = 0
hourDict = {}
maxMailsNum = 0
maxMailsId = ''
for line in handle:
    l = line.rstrip()
    lineAsList = l.split()
    if len(lineAsList) > 0 and lineAsList[0] == ('From'):
        count += 1
        hour = lineAsList[5].split(":")[0]
        hourDict[hour] = hourDict.get(hour,0) + 1




sortedHours = sorted(hourDict.items())

for k,v in sortedHours:
    print ("{} {}".format(str(k), str(v)))


