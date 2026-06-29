def sort_colours(arr):
    i,j,k=0,0,len(arr)-1
    while(i<=k):
        if(arr[i]==0):
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j+=1
        elif(arr[i]==2):
            arr[i],arr[k]=arr[k],arr[i]
            k-=1
        else:
            i+=1