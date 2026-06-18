n = int(input("Enter a number:"))
if(n%2!=0):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if(i==j or i+j==n+1):
                print("*",end="")
            else:
                print(" ",end="")
        print("")
else:
    print("X-Pattern not possible for even numbers")