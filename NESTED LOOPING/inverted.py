n = int(input("Enter a number:"))
for i in range(1,n+1):
    for j in range(1,(n-i+1)+1): 
        print("*",end=" ")
    print("")


"""
When n is entered 5. The loop will be running from 1 to 5(6-1). Then inside another loop will run from j =1 to (n-i+1) 
As when i = 1 it becomes 5-1+1= 5 and will run inner loop 5 times and then increase i to 2
Now i =2 so inner loop will run till 5-2+1 = 4 And so on
"""