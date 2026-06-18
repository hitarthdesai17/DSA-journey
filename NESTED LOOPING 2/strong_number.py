n = int(input("Enter Number:"))
copy = n
ans = 0
while(n>0):
    dig=n%10
    fact = 1
    for i in range(1,dig+1):
        fact *= i
    ans = ans + fact
    n = n//10
if(ans==copy):
    print("Strong Number")
else:
    print("Not a Strong Number")