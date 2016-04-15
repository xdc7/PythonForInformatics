fh = open('.\\files\\mbox.txt')

count = 0

# for line in fh:
#     #count += 1
#     line = line.rstrip()
#     if line.find('@uct.ac.za') > -1:
#         print(line)


#data = fh.read()
#print (data[40:100])
#print ("number of lines in mbox.txt {}".format(count))

wf = open('.\\files\\writeFile.txt', 'a')
wf.write("line1\n")
wf.write("line2\n")
wf.close()


wf2 = open('.\\files\\writeFile.txt','r')
wf2 = wf2.read()
print(repr(wf2))
