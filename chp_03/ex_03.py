def calculateGrade(score):
    if score < 0.0 or score > 1.0:
            print ("Invalid score. Please enter score within range: 0.0 to 1.0")
    elif score >= 0.9:
        print ("Grade: A")
    elif score >= 0.8:
        print ("Grade: B")
    elif score >= 0.7:
        print ("Grade: C")
    elif score >= 0.6:
        print ("Grade: D")
    else:
        print ("Grade: F")

while (True):
    score = input("Please enter score (Valid range: 0.0 to 1.0) or q to quit: ")
    if score.lower() == "q":
        break
    try:
        score = float(score)
        calculateGrade(score)
    except:
        print("Please enter numeric values!")