a,b=list(map(int,input("Enter Two Numbers").split()))
print("Standard Way:")
for i in range(min(a,b),0,-1):
    if(a%i==0 and b%i==0):
        print(i)
        break

print("Recursive Way:Brute Force")
def gcdBrute(a,b,i=None):
    if i is None:
        i = min(a,b)
    if a%i==0 and b%i==0:
        return i
    return gcdBrute(a,b,i-1) #Here loop is running
print("For 20 And 32\n",gcdBrute(20,32))

print("Recursive Way : Subtraction")
def gcdsubtract(a,b):
    if a==b:
        return a
    if a>b : 
        return gcdsubtract(a-b,a)
    if a<b : return gcdsubtract(a,b-a)
print("For 20 and 30\n",gcdsubtract(20,30))

print("Recursive Way: Euclidian")
def euclidian_gcd(a,b):
    if b==0:
        return a
    return euclidian_gcd(b,a%b)
print("For 99 & 102\n",euclidian_gcd(99,102))