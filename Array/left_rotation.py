#Left by 1 value
arr= [1,2,3,4,5]
temp = arr[0]
for i in range(len(arr)-1):
    arr[i]=arr[i+1]
arr[len(arr)-1]=temp
print(arr)

#Left by K value
