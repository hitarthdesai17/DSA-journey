class Solution(object):
    def binarySearch(self,nums,target,isStart):
        first=0
        last=len(nums)-1
        ans=-1
        while(first<=last):
            mid=(first+last)//2
            if(nums[mid]==target):
                ans=mid
                if(isStart): last=mid-1
                else: first=mid+1
            elif(nums[mid]<target):
                first=mid+1
            else:
                last=mid-1
        return ans


    def searchRange(self, nums, target):
        start=self.binarySearch(nums,target,True)
        end=self.binarySearch(nums,target,False)
        return [start,end]
        
        