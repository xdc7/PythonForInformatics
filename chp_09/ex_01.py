word_dc = {}
fh = open('romeo.txt')

# for line in fh.readlines():
#     line = line.rstrip()
#     temp = line.split()
#     for word in temp:
#         word_dc.setdefault(word,"")
#
# #print(word_dc)
word_dc = {}
# Alternative solution using the dictionary get() method

for line in fh.readlines():
    line = line.rstrip()
    temp = line.split()
    for word in temp:
        word_dc[word] = word_dc.get(word, 0) + 1
print (word_dc)
