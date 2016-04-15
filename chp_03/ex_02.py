

try:
    hours = float(input("Enter the number of hours worked: "))
    rate = float(input("Enter the rate per hour: "))
    salary = 0

    if hours < 40:
        salary = hours * rate
    else:
        salary = (hours * rate) + (hours - 40) * 1.5 * rate
    print(("Your salary for the week is {}").format(salary))

except:
    print("Please enter numeric/ valid input")

