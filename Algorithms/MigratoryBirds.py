def migratoryBirds(n,ar):
    count = [0]*6
    for i in range(0,n):
        count[ar[i]]+=1


    maxi = max(count)
    index = 10
    for i in range(1,6):
        if(count[i]==maxi):
            if(i<index):
                index = i


    return index



print(migratoryBirds(6,[2,2,4,1,1,1]))





