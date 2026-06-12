import math
import random
print("Question 1 : Calculate Compound Interest:")
p=int(input("Enter Principal Amount:"))
r=int(input("Enter Rate of interest:"))
t=int(input("Enter Number of years:"))

ci = p*math.pow(1+r/100,t) - p
ci = f"{ci:.3f}"
print("Compound interest is",ci)

"""
Alternate Method
print(f"Compound interest is {(p * math.pow(1 + r/100, t) - p):.3f}")
ci = p * math.pow(1 + r/100, t) - p

print(f"Compound interest is {ci:.3f}")
 """
print("Question 2 : Generate OTP")
print(math.floor(random.random()*9000+1000))

print("Question 3 : Find Area of triangle using Heron's Formula")
a=int(input("Enter side of triangle :"))
b=int(input("Enter side of triangle :"))
c=int(input("Enter side of triangle :"))
 
if(a+b<=c or a+c<=b or b+c<=a):
    print("Not Possible")
else:
    S=(a+b+c)/2  
    Area=math.sqrt(S*(S-a)*(S-b)*(S-c))
    print(f"Area of traingle is {Area:.3f}")

print("Question 4 : Circumference of circle")
r=int(input("Enter radius of circle:"))
circumference=2*math.pi*r
print("Circumference of circle is",circumference)    

print("If-Else Elif Loops")
if(10>5 or 5>9):
    print("Only works when if condition is true.")
elif(6>9):
    print("Works when if condition is false and elif is true.")
else:
    print("Works when no condition that is if and elif is failed!") 

print("Check if Number is even or odd")
num=int(input("enter sny number:"))
if(num%2==0):
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")

print("A program to check greatest of 3 numbers")
num1=int(input("Enter number 1"))
num2=int(input("Enter number 2"))
num3=int(input("Enter number 3"))

if(num1>=num2 and num1>=num3):
    print(f"{num1} is Greatest")
elif(num2>=num1 and num2>=num3):
    print(f"{num2} is Greatest")
else:
    print(f"{num3} is Greatest")