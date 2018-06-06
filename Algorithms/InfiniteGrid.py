def coverPoints(A,B):
    if(len(A)==0 or len(A)==1):
        return 0

    length = 0

    startx = A[0]
    starty = B[0]

    for i in range(0, len(A)):
        x = abs(startx - A[i])
        y = abs(starty - B[i])
        startx = A[i]
        starty = B[i]

        length+= max(x,y)


    return length


r