import math
n = int(input("Enter Number:"))
copy = n
sq = n*n
count = 0
while(n>0):
    count += 1
    n = math.floor(n/10)
if(sq%math.pow(10,count)==copy): print("Yes")
else: print("No")