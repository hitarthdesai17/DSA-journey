
def sqrtBrute(x):

        i = 0

        while i * i <= x:
            i += 1

        return i - 1
print(sqrtBrute(900000000))