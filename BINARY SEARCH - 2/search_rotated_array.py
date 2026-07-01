def search(arr,target):
    f=0
    l=len(arr)-1
    while(f<=l):
        m=(f+l)//2
        if(arr[m]==target): return m
        elif(arr[f]<=arr[m]):
            if(target in range(arr[f],arr[m]+1)):
                l = m
            else: f=m+1
        else:
            if(target in range(arr[m+1],arr[l]+1)):
                f=m+1
            l=m
    return -1
arr=[4,5,6,7,0,1,2]
print(search(arr,0))