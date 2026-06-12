import math
num = int(input("Enter number:"))
isPrime = True

for i in range(2,int(math.sqrt(num))+1):
    if(num%i==0):
        isPrime = False
        break
if(isPrime): print("Prime Number")
else : print("not a prime number")
    