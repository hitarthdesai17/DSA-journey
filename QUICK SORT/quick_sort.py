def findPivotIndex(arr,first,last):
    pivot=arr[last]
    i=first-1
    for j in range(first,last):
        if(arr[j]<pivot):
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    i+=1
    arr[i],arr[last]=arr[last],arr[i]
    return i
def quickSort(arr,first,last):
    if  first>=last: return
    pIdx = findPivotIndex(arr,first,last)
    quickSort(arr,first,pIdx-1)
    quickSort(arr,pIdx+1,last)

arr=[32,54,31,22,45,23]
quickSort(arr,0,len(arr)-1)
print(arr)