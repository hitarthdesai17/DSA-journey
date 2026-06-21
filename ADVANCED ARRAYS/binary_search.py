arr=[5,10,15,20,23,34,42,45,60]
target = int(input("Enter value to find:"))

def BinarySearch(arr,target):
    s,e=0,len(arr)-1
    while(s<=e):
        mid=(s+e)//2
        if(arr[mid]==target): return mid
        elif(arr[mid]>target): e=mid-1
        else: s=mid+1
    return -1

if(BinarySearch(arr,target)==-1): print("Element not found.")
else: print("Element Found:")