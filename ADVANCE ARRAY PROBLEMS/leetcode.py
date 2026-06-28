print("88 Number:Merge Sorted ARrays")
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i,j,k=m-1,n-1,len(nums1)-1
        while(i>=0 and j>=0):
            if(nums1[i]>nums2[j]):
                nums1[k]=nums1[i]
                i-=1
            else:
                nums1[k]=nums2[j]
                j-=1
            k-=1
        while j>=0:
            nums1[k]=nums2[j]
            j-=1
            k-=1

print("Question 26 - Remove Duplicates")
def removeDuplicates(   nums):
        j=1
        for i in range(len(nums)-1):
            if(nums[i]!=nums[i+1]):
                nums[j]=nums[i+1]
                j+=1
        return j
print("1089 : Duplicate Zeroes:")
def duplicate_zeroes(arr):
    i = 0
    while(i<len(arr)):
        if arr[i]==0:
            arr.insert(i,0)
            arr.pop()
            i+=1
        i+=1
print("283:Move Zeroes.")