def reverse(n,rev=0):
    if n < 0:
            return -reverse(-n)

    if n==0: return rev
    return reverse(n//10 ,rev * 10 + (n%10))
print(reverse(-89))
    