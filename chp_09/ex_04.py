from ex_03 import getEmailCounts

def getMaxCountFromDictionary(dictionary):
    maxNum = [None,None]
    for k,v in dictionary.items():
        #print("{}: {}".format(k,v))
        if maxNum[1] == None or v > maxNum[1]:
            maxNum[1] = v
            maxNum[0] = k
    return maxNum

print (getMaxCountFromDictionary(getEmailCounts()))