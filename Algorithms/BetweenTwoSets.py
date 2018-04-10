def getTotolX(a,b):
    maxi = max(b)
    count = 0

    for i in range(1,maxi):
        flag = 1
        for element1 in a:
            if(i%element1!=0):
                flag = 0
        for element2 in b:
            if(element2%i!=0):
                flag = 0
        if(flag==1):
            count+=1

    if(a[0]==1):
        count+=1

    return count

print(getTotolX([1],[100]))





