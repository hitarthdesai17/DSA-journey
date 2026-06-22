def insertionsort(arr):
    for i in range(1,len(arr)):
        key,j=arr[i],i-1
        while(j>=0 and arr[j]>key):
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return print(arr)

arr1=[3,2,45,23,69,90,44]
insertionsort(arr1)