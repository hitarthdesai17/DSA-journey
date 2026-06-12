n=int(input("Enter a number:"))
fact = 1
for i in range(1,n+1):
    fact = fact*i #fact *= i
print(fact)

print("Program to Find Factor of a number:")
for i in range(i,(n/2)+1):
    if(n%i == 0): print(i)
print(n)

