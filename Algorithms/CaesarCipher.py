def caesarCipher(s,k):

    for i in range(0,len(s)):
        if(s[i].isupper or s[i].islower):
            s[i] = chr(ord(s[i])+3)


    return s


print(caesarCipher("helloBitch",2))
