def camelCase(s):
    count = 0

    if(s==""):
        return "Empty String"

    for i in range(1,len(s)):
        if(s[i].isupper()):
            count+=1

    return count+1


print(camelCase("aB"))