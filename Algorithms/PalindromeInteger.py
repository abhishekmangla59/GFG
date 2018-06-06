def isPalindrome(A):
    num = A
    if (A < 0):
        return 0
    sum = 0

    while A != 0:
        rem = A % 10
        sum = sum * 10 + rem
        A = A / 10

    if sum == num:
        return 1
    return 0





print(isPalindrome(7447))