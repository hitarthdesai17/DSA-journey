def three_sum(nums):
    nums.sort()
    ans=[]
    for i in range(len(nums)-2):#Using n-2 because we need three numbers atleast so going till end is not worth

        if(i!=0 and nums[i-1]==nums[i]):continue
        j=i+1
        k=len(nums)-1

        while(j<k):
            sum = nums[i]+nums[j]+nums[k]

            if(sum==0):
                temp=[nums[i],nums[j],nums[k]]
                ans.append(temp)
                j+=1
                k-=1
                while(j<k and nums[j-1]==nums[j]):
                    j+=1
                while(j<k and nums[k+1]==nums[k]):
                    k-=1

            elif(sum<0):
                j+=1
            else:
                k-=1
    return ans
num=[-1,0,1,2,-1,-4]
print(three_sum(num))