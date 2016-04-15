"""
Write a program to prompt for a file name,
and then read through the file and look for lines of the form:
X-DSPAM-Confidence: 0.8475 When you encounter a line that starts with
 “X-DSPAM-Confidence:” pull apart the line to extract the
  floating-point number on the line. Count these lines
  and then compute the total of the spam confidence values
  from these lines. When you reach the end of the file,
  print out the average spam confidence.
"""
filename = input("Enter a file name: \n")
try:
    count = 0
    total = 0
    fh = open(filename)
    for line in fh:
        line = line.rstrip()
        if line.startswith("X-DSPAM-Confidence:"):
            count += 1
            spamConfStartIndex = line.find(":") + 1
            spamConf = line[spamConfStartIndex:]
            spamConf = float(spamConf)
            spamConf = round(spamConf,5)
            total += spamConf
    avg = total/count
    avg = round(avg,6)
    print("Sum of Spam Confidence values: {}".format(total))
    print("Total number of Spam Confidence lines: {}".format(count))
    print("Average of Spam Confidence values: {}".format(avg))

except:
    print("File not found!")