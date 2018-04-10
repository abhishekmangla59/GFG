def kangaroo(x1,v1,x2,v2):
    x=1
    flag = 0
    while(x<=10000):
        pos1 = x1+v1*x
        pos2 = x2+v2*x
        x = x+1
        if(pos1 == pos2):
            flag = 1
            break

    if(flag):
        return "YES"
    return "NO"


print(kangaroo(0,3,4,2))