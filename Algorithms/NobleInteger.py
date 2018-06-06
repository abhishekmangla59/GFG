def nobleIntiger(A):
    A.sort()

    for i in range(0,len(A)):
        if(A[i]==len(A)-(i+1)):
            return 1


    return -1


print(nobleIntiger([1,2,3,3]))