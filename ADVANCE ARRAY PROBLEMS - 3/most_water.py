def mostarea(arr):
    i=0
    j=len(arr)-1
    ans=0
    while i<j:
        ans=max(ans,min(arr[i],arr[j])*(j-i))
        if(arr[i]<arr[j]): i+=1
        else: j-=1
    return ans

