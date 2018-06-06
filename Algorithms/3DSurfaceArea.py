def surfaceArea(A):
    a = [[0] * (len(A[0]) + 2)]


    for row in A:
        a.append([0] + row + [0])
    a.append([0] * (len(A[0]) + 2))

    # Bottom and top area
    ans = len(A) * len(A[0]) * 2

    # Side area is just the sum of differences
    # between adjacent cells. Be careful not to
    # count a side twice.
    for i in range(1, len(a)):
        for j in range(1, len(a[i])):
            ans += abs(a[i][j] - a[i - 1][j])
            ans += abs(a[i][j] - a[i][j - 1])
    return ans













A = [[1,2,3],
     [4,5,6],
     [7,8,9],
     [11,12,13]]

print(surfaceArea(A))