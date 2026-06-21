#Left by 1 value
arr= [1,2,3,4,5]
temp = arr[0]
for i in range(len(arr)-1):
    arr[i]=arr[i+1]
arr[len(arr)-1]=temp
print(arr)

#Left by K value
arr1= [1,2,3,4,5]
k = int(input("How many times you want to rotate:"))
k=k%len(arr1) #If k is bigger than length of array this is used.
for j in range(1,k+1):
    temp1 = arr1[0]
    for i in range(len(arr1)-1):
        arr1[i]=arr1[i+1]
    arr1[len(arr1)-1]=temp1
print(arr1)

print("ALTERNATE METHOD:")
arr2=[1,2,3,4,5]
k = 2
temp = []
for i in range(len(arr2)):
    temp.append(arr2[(i+k)%len(arr2)])
print(temp)

print("\nBLOCKSWAP REVERSE ALGORITHM:")
array = [1,2,3,4,5]
n = int(input("How many times to rotate"))                                #For 3 
n = n%len(arr)
def reverse(array,i,j):
    while(i<j):
        temp = array[i]
        array[i]=array[j]
        array[j]=temp
        i+=1
        j-=1

reverse(array,0,n-1)                     #o,len-1
reverse(array,n,len(array)-1)            #o,k-1
reverse(array,0,len(array)-1)            #k,len-1
print(array)
