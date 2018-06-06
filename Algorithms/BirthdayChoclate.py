def solve(n,s,d,m):
    count = 0
    for i in range(0,n-m):
        new = s[i:i+m]
        if(sum(new)==d):
            count+=1



    return count



print(solve())