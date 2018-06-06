def minimumNumber(n,s):
    count = 0

    if(s==""):
        return 6

    num = False
    lower = False
    upper = False
    special = False
    specialChar = "!@#$%^&*()-+"

    for i in range(0,n):
        if(s[i].isupper()):
            upper = True
            continue
        if(s[i].islower()):
            lower = True
            continue
        if(s[i].isdigit()):
            num = True

    if any(char in specialChar for char in s):
        special = True






    if(not num):
        count +=1

    if (not lower):
         count += 1

    if (not upper):
         count += 1

    if (not special):
        count += 1

    #print(count)

    if(n>=6):
        return count
    if(n<6):
        if(n+count<6):
            return 6-n
        elif(n+count==6):
            return count
        elif(n+count>6):
            return count - (6-n)







print(minimumNumber(4,"a$a1"))

