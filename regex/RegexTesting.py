import re

data_01 = open("regex_sum_202249.txt")


#print sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] )

#print([nums] for nums in re.findall("[0-9]",data_01.read()))
#x = re.findall("[0-9]",data_01.read())
#x = data_01.read()



print (sum( [int(nums) for nums in re.findall('[0-9]+',data_01.read()) ] ))