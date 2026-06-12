n=int(input("Enter number of terms :"))
sum = 0
for i in range(1,n+1):
    sum += i #Sum = sum + i
print(sum )

print("Sum of all odd and even number seperately.")
even_sum=0
odd_sum=0
for i in range (1,n+1):
    if(i%2==0): even_sum = even_sum + i
    else : odd_sum = odd_sum + i
print("Even sum",even_sum)
print("Odd sum",odd_sum)