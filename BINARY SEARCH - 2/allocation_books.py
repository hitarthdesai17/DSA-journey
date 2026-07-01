def isValid(arr,upperLimit,k):
    count,current_sum=1,0
    for i in range(0,len(arr)):
        if(current_sum+arr[i]>upperLimit):
            count+=1
            current_sum=arr[i]
            if(count>k):
                return False
        else: current_sum+=arr[i]
    return True
    pass
def findPages(arr,k):
    if k>len(arr):
        return -1
    first , last , ans = 0,0,-1
    for num in arr:
        last+=num
        first=max(num,first)
    while(first<=last):
        mid=(first+last)//2
        if(isValid(arr,mid,k)):
            ans=mid
            last=mid-1
        else: first = mid+1
    return ans
arr=[20,10,30,40]
print(findPages(arr,2))