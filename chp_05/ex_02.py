def getMax(ls):
    maxi = None
    for num in ls:
        if maxi == None or num > maxi:
            maxi = num
    return maxi

def getMin(ls):
    mini = None
    for num in ls:
        if mini == None or num < mini:
            mini = num
    return mini
count = 0
total = 0
nums = []
#average = 0
while True:
    userInput = input("Please a number or type 'done' to quit: ")
    if userInput.lower() == "done":
        print ("Numeric entries: {} ".format(nums))
        print ("Max of numeric entries: {} ".format(getMax(nums)))
        print ("Min of numeric entries: {} ".format(getMin(nums)))

        break

    try:
        userInput = int(userInput)
        nums.append(userInput)
        count += 1
        total += userInput
    except:
        print("Invalid number! Please enter numeric values or type 'done' to quit ")