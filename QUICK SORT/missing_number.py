def missing_number(arr):
    i = 0
    while(i<len(arr)):
        crtIdx=arr[i]
        if(arr[i]!=len(arr) and arr[i]!=arr[crtIdx]):
            arr[i],arr[crtIdx]=arr[crtIdx],arr[i]
        else:
            i+=1
    for j in range(0,len(arr)):
        if(arr[j]!=j):
            return j
    return len(arr)
arr=[1,3,4,5,0]
print(missing_number(arr))