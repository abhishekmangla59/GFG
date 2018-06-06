def solve(A):
    for i in range(0,len(A)):
        A[i]=float(A[i])

    for i in range(0, len(A) - 2):

        # Fix the second element as A[j]
        for j in range(i + 1, len(A) - 1):

            # Now look for the third number
            for k in range(j + 1, len(A)):
                sum = A[i] + A[j] + A[k]
                if sum>1 and sum<2:
                    return 1

        # If we reach here, then no
        # triplet was found
    return 0


print(solve(["0.366507", "0.234601", "2.126313", "1.372403", "2.022170", "0.308558", "2.120754", "1.561462"]))
