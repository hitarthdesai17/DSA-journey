n=5
i=1
while(i<=n):
    print(i)
    i+=1
import math
print("Sum of digit of number:")
num = int(input("Enter a number:"))
sum = 0
while(num>0):
    rem = num%10
    sum = sum + rem
    num = math.floor(num/10)
print(sum)