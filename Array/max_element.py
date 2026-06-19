n=int(input("Enter size:"))
arr=[]
for i in range(0,n):
    arr.append(int(input("Enter element:")))
    
# arr = list(map(int, input().split()))
max_element=arr[0]
max_index=0
for i in range(1,len(arr)):
    if(max_element<arr[i]):
        max_element=arr[i]
        max_index=i
print("Max element =",max_element,"found at index",max_index)

fmax = max(arr[0],arr[1])
smax = min(arr[0],arr[1])
for i in range(2,n):
    if(arr[i]>fmax):
        smax=fmax
        fmax=arr[i]
    elif(arr[i]>smax and arr[i]!=fmax):
        smax=arr[i]
print("Second max element =",smax)
        