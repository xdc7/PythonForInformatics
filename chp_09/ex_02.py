try:
    fh = open ("..\\files\\mbox.txt")
except:
    print('file not found')
    exit()

dayCount = {}
for line in fh:
    line = line.rstrip()
    if line.startswith("From "):
        words = line.split()
        day = words[2]
        if day not in dayCount:
            dayCount[day] = 1
        else:
            dayCount[day] += 1

print(dayCount)