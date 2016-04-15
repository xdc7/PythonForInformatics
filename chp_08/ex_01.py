"""
Write a function called chop that takes a list and modifies it,
removing the first and last elements, and returns None .
Then write a function called middle that takes a list
and returns a new list that contains all but the first and last elements.
"""

def chop(ls):
    if len(ls) <1:
        pass
    elif len(ls) == 1:
        del ls[0]
    else:
        del ls[0]
        del ls[-1]

def middle(ls):
    return ls[1:-1]


ls2 = [1,2,'a', 'ace',90]
ls =[1]
chop(ls)
print(ls)

print(middle(ls2))