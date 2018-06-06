def circularArrayRotation(a,m):
    a = a[m:] + a[:m]
    return a



print(circularArrayRotation([1,2,3,4],1))


