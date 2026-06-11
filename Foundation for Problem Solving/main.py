#Sum of Two Numbers
a=10
b=20
print(a+b)

"""
Relationship between String and Integer
->String + String = String (concatenation)
->String + Int = String (Concantenation)
->Int + Int = Int (Arithematic)
"""
c="Hello "
d="World"
print(c+d) #Hello World

print("Sum of ",a,"and ",b,"is",a+b)

print(str(1) + "1")

#Accept and Print the answer
age=int(input("enter age:"))
#For JS let age = Number(prompt("Enter age"));

#Question - Swap Two variables via 3 methods
print("Method-1 : Using Extra variable")

temp = a
a=b
b=temp
print(f"Value of a is {a} and value of b is {b}") 

print("Method-2: Using Maths")
e=30
f=40
e=e+f #e=70
f=e-f #70-40 = 30
e=e-f #70 - 30 = 40
print(f"Value of e is {e} and value of f is {f}")

print("Method 3 - Destructuring")
h = 10
m = 20
[h,m]=[m,h]
print(h,m)
