arr1=[2,4,5]
arr2=[1,4,7]
ans =[0]*len(arr1+arr2)

i=k=j=0
while(i<len(arr1) and j<len(arr2)):
    if(arr1[i]<arr2[j]):
        ans[k]=arr1[i]
        i+=1
    else:
        ans[k]=arr2[j]
        j+=1
    k+=1
while(i<len(arr1)):
    ans[k]=arr1[i]
    i+=1
    k+=1
while(j<len(arr2)):
    ans[k]=arr2[j]
    j+=1
    k+=1
print(ans)