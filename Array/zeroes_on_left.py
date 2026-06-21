arr = [1,1,0,1,0,0,1,0,1,1]
i=j=0
while(i<len(arr)):
    if(arr[i]==0):
        arr[i],arr[j]=arr[j],arr[i]
        j +=1
    i+=1

print(arr)

"""
class Solution:
    def moveZeros(self, arr):
        ones = [x for x in arr if x != 0]
        zeros = [0] * (len(arr) - len(ones))
        return ones + zeros

"""