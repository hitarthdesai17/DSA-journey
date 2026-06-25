def isPowerOfTwo(num):

    return num > 0 and (num & (num-1)) == 0


print(isPowerOfTwo(8))

print(isPowerOfTwo(10))

def isPowerofFour(num):
    return num > 0 and (num & (num-1)) == 0 and num%3==1