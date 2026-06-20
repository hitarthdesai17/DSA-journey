arr = [1,1,0,1,0,0,1,0,1,1]
i=j=0
while(i<len(arr)):
    if(arr[i]==0):
        arr[i],arr[j]=arr[j],arr[i]
        j +=1
    i+=1

print(arr)