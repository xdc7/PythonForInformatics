"""
Rewrite the program that prompts the user for a list of numbers
 and prints out the maximum and minimum of the numbers at the end
  when the user enters “done”. Write the program to store the numbers
   the user enters in a list and use the max() and min() functions to compute
   the maximum and minimum numbers after the loop completes.
"""
def maxNum(ls):
    m = None
    for n in ls:
        if m == None or m < n:
            m = n
    return m

def minNum(ls):
    m = None
    for n in ls:
        if m == None or m > n:
            m = n
    return m

nums = []
while(True):
    userInput = input("Please enter an integer or type 'done' to quit: ")
    if userInput.lower() == "done":
        break
    try:
        nums.append(int(userInput))
    except:
        print('Invalid input. Try again!')

print("Minimum entered number was: {}".format(minNum(nums)))
print("Maximum entered number was: {}".format(maxNum(nums)))