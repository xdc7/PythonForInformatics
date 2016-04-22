def getEmailCounts(filename="..\\files\\mbox.txt"):
    try:
        fh = open(filename)
    except:
        print("File not found")
        exit()

    emailCounts = {}
    for line in fh:
        if line.startswith("From "):
            words = line.split()
            email = words[1]
            emailCounts[email] = emailCounts.get(email, 0) + 1
    return (emailCounts)

#print(getEmailCounts())