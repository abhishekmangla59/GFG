def superReducedString(s):
    i=1
    if(s==""):
        return "Empty String"

    while(i<len(s)):
        if(s[i]==s[i-1]):
            s = s[:i-1]+s[i+1:]
            i = 0
        i+=1


    if(s==""):
        return "Empty String"
    return s






print(superReducedString("aab"))