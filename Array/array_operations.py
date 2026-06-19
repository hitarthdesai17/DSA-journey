arr=[]
size=int(input("Enter Size of array:"))
sum = 0 
for i in range(0,size):
    arr.append(int(input("Enter element:")))
    sum = sum + arr[i]

print("Sum:",sum)
print("Mean:",sum/len(arr))

max = arr[0]
for i in range(1,size):
    if(max<arr[i]): max=arr[i]

print("MAX Element:",max)
print(arr)