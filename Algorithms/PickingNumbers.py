def pickingNumbers(a):
    maximum=0
    freq = [0]*100

    for i in range(0,len(a)):
        freq[a[i]]+=1

    for i in range(2,100):
        maximum = max(maximum,freq[i]+freq[i-1])


    return maximum


print(pickingNumbers(10,[1,2,3,4,5,5,5,5,6,6]))