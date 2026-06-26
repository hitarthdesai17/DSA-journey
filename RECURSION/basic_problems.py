#From N to 1
n=int(input())
for i in range(n,0,-1):
    print(i,end=" ")

#From 1 to N
def printNumbers(n):
        return list(range(1,n + 1))
print(printNumbers(n))

#Print Hello n times

def printHello(n: int):
        if n==0:
            return
        print("Hello")
        printHello(n-1)
        pass
