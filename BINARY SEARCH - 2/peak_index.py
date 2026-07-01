#LEETCODE 852
def peak_index(arr):
    f=0
    l=len(arr)-1
    while(f<l):#STOP when f=l
        m=(f+l)//2
        if(arr[m]<=arr[m+1]):
            f=m+1
        else: l = m
    return f
print(peak_index(arr=[1,2,5,6,4,2,1]))
        
