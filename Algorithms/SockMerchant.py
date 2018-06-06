def sockMerchant(n, anr):
    pair = [0]*100




    count = 0


    for i in range(0,n):
        pair[anr[i]]+=1
        #print(pair[anr[i]])


    for i in range(0,100):
        if(pair[i] is not 0 and pair[i]/2 >0):
            count += pair[i]/2

    return count


print(sockMerchant(9,[10,20,20,10,10,30,50,10,20]))




