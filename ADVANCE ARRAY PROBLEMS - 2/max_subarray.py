arr=[-2,1,-3,4,-1,2,1,-5,4]
f_sum=0
maxsum=float("-inf")
for i in range(len(arr)):
    f_sum+=arr[i]
    if(f_sum>maxsum):
        maxsum=f_sum
    if(f_sum<0):
        f_sum=0
print(maxsum)