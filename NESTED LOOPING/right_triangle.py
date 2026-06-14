"""
Write a program to print this right angle triangle pattern
*
* *
* * *
* * * *
* * * * *
"""
n =int(input("Enter a number to print rows:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")#For number print j
    print("")