count = 0
total = 0
#average = 0
while True:
    userInput = input("Please a number or type 'done' to quit: ")
    if userInput.lower() == "done":
        print ("Total numeric entries: {} ".format(count))
        print ("Sum of numeric entries: {} ".format(total))
        if count > 0:
            print ("Average of numeric entries: {} ".format(total/count))
        break

    try:
        userInput = float(userInput)
        count += 1
        total += userInput
    except:
        print("Invalid number! Please enter numeric values or type 'done' to quit ")