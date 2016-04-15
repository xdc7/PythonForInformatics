import re

data_01 = open("regex_sum_202249.txt")
regexString = "[0-9]+"
numAsString = []
totalSum = 0
for line in data_01:
    l = line.rstrip()
    #print (l)
    numAsString = re.findall(regexString,l)
    for n in numAsString:
        if n != "":
            totalSum += int(n)


print (totalSum)

#optional 1 line solution using list comprehension:

#print (sum( [int(nums) for nums in re.findall('[0-9]+',data_01.read()) ] ))